#!/bin/bash -l

## Nazwa zlecenia
#SBATCH -J Stars1
## Liczba alokowanych węzłów
#SBATCH -N 1
## Liczba zadań per węzeł (domyślnie jest to liczba alokowanych rdzeni na węźle)
#SBATCH --ntasks-per-node=8
## Maksymalny czas trwania zlecenia (format HH:MM:SS)
#SBATCH --time=02:00:00
## Nazwa grantu do rozliczenia zużycia zasobów
#SBATCH -A plgar2022-cpu
## Specyfikacja partycji
#SBATCH -p plgrid

srun /bin/hostname

## Zaladowanie modulu IntelMPI
module load scipy-bundle/2021.10-intel-2021b

cd $SLURM_SUBMIT_DIR

for proc in {1..8}
do
  start=$(date +%s%N)
  mpiexec -n "$proc" python3 stars1.py 840
  end=$(date +%s%N)
  echo "$(((end-start)/1000000))" >> times-8-840.txt
done

for proc in {1..8}
do
  start=$(date +%s%N)
  mpiexec -n "$proc" python3 stars1.py 1680
  end=$(date +%s%N)
  echo "$(((end-start)/1000000))" >> times-8-1680.txt
done

for proc in {1..8}
do
  start=$(date +%s%N)
  mpiexec -n "$proc" python3 stars1.py 240
  end=$(date +%s%N)
  echo "$(((end-start)/1000000))" >> times-8-2520.txt
done
