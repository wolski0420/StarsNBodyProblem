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

### Flags

Running ```stars1.py``` with flag ```compare``` will set same seed
on the parallel and the sequential version of algorithm.

Running ```stars1.py``` with flag ```print``` will print results
on the console

Running ```stars1.py``` with flag ```save``` will save results
to the file with appropriate name.

### Comparing

You can compare results with iterative version. You need to run these
commands:

```shell
mpiexec -n 2 python3 stars1.py 4 compare print save
```

```shell
python3 iterative.py 4
```

After that, you will be able to check results from both scripts
by checking console output or appropriate files.

### Ares

There is a script to run on Ares cluster already prepared. If you have
an access, just copy ```experiments.sh``` and ```stars1.py``` using SCP
protocol and after that, run ```sbatch experiments.sh``` when you are
connected to Ares through SSH.
