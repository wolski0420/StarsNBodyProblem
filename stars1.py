import numpy as np

from math import floor
from mpi4py import MPI
from sys import argv


G = 6.6743015e-11
comm = MPI.COMM_WORLD

if "compare" in argv:
    np.random.seed(100 + comm.Get_rank())


def generate_stars(size: int):
    # it generates: M, x, y, z for each star
    stars = np.ndarray((size, 4))
    stars[:, 0] = np.random.uniform(low=100.0, high=200.0, size=size)
    for i in range(3):
        stars[:, i + 1] = np.random.random(size)

    return stars


def compute_single_relation(current_star: np.ndarray, external_star: np.ndarray):
    M, current_r, buffered_r = external_star[0], current_star[1:], external_star[1:]
    r_differ = current_r - buffered_r
    r_3 = np.power(np.sqrt(np.sum(np.power(r_differ, 2))), 3)

    return G * M * r_differ / r_3 if r_3 != 0 else np.asarray([0, 0, 0])


def compute_stars_relations(stars, buffer_stars):
    relations = np.zeros((stars.shape[0], 3))

    # for each star of current process, calculate acceleration sourced from each buffer star
    for i in range(stars.shape[0]):
        for j in range(buffer_stars.shape[0]):
            relations[i] += compute_single_relation(stars[i], buffer_stars[j])

    return relations


# taking exercise parameters
N = int(argv[1])
p = comm.Get_size()

# receiving information about process and its neighbours ranks
rank = comm.Get_rank()
left_rank = (rank - 1) % p
right_rank = (rank + 1) % p

# calculating portion
group_size = floor((N + 1) / p)
first_star = rank * group_size
last_star = min(N - 1, (rank + 1) * group_size - 1) if rank != p - 1 else N - 1
portion = last_star - first_star + 1

# generating data, preparing buffers and accumulator
proc_stars = generate_stars(portion)
from_left_buffer, to_right_buffer = proc_stars.copy(), proc_stars.copy()
accumulator = compute_stars_relations(proc_stars, proc_stars)

# iterating over ring
for _ in range(p-1):
    # 1. sending last received buffer to neighbour
    comm.Send([to_right_buffer, MPI.FLOAT], dest=right_rank)

    # 2. receiving new buffer from neighbour
    comm.Recv([from_left_buffer, MPI.FLOAT], source=left_rank)

    # 3. computing relations between received stars and current process stars
    new_relations = compute_stars_relations(proc_stars, from_left_buffer)

    # 4. accumulating computed relations (ax, ay, az)
    accumulator += new_relations

    # holding received buffer to send it in next iteration
    to_right_buffer, from_left_buffer = from_left_buffer, to_right_buffer

gathered = comm.gather(accumulator, root=0)
if rank == 0:
    gathered = np.concatenate(gathered, axis=0)
    print(gathered)
    if "save" in argv:
        np.savetxt("results-parallel.txt", gathered)
