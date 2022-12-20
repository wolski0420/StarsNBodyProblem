# N-Body problem with Stars example

Project solving N-Body problem basing on stars. Each star has
a gravity interaction with each other and in this example we do
not limit complexity, but we simplify communication and create
parallel algorithm.

### Running 

Example command

```shell
mpiexec -n 2 python3 stars1.py 4
```

When:
```-n``` flag is a number of processes,
```4``` after filename is a number of stars.

### @TODO

1. Test comparing results with a sequential version results (basing on small data).
2. Compute the acceleration and the efficiency of the algorithm for big data (many stars per each processor).