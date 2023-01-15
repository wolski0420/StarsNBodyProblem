import numpy as np

from math import floor
from sys import argv

# constant
G = 6.6743015e-11

# taking exercise parameters
N = int(argv[1])
used = int(argv[2])

all_stars = []
for rank in range(used):
    # calculating portion
    group_size = floor((N + 1) / used)
    first_star = rank * group_size
    last_star = min(N - 1, (rank + 1) * group_size - 1) if rank != used - 1 else N - 1
    portion = last_star - first_star + 1

    if "compare" in argv:
        np.random.seed(100 + rank)

    # it generates: M, x, y, z for each star
    stars = np.ndarray((portion, 4))
    stars[:, 0] = np.random.uniform(low=100.0, high=200.0, size=portion)
    for i in range(3):
        stars[:, i + 1] = np.random.random(portion)

    all_stars.append(stars)

all_stars = np.concatenate(all_stars, axis=0)
accumulator = np.zeros((all_stars.shape[0], 3))

for i in range(all_stars.shape[0]):
    for j in range(all_stars.shape[0]):
        if i != j:
            M = all_stars[j][0]
            current_r = all_stars[i][1:]
            considered_r = all_stars[j][1:]
            r_differ = current_r - considered_r
            r_3 = np.power(np.sqrt(np.sum(np.power(r_differ, 2))), 3)

            accumulator[i] += G * M * r_differ / r_3 if r_3 != 0 else np.asarray([0, 0, 0])

if "print" in argv:
    print(accumulator)
if "save" in argv:
    np.savetxt("results-iterative.txt", accumulator)
