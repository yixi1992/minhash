#!/bin/bash

#SBATCH -t 10:00:00
#SBATCH -N 1

#source /lustre/yixi/decouplednet/DecoupledNet/inference/load_deeplab_dependencies.sh

module load matlab
matlab -nodisplay -nosplash -r "binSize=20; magnif=3; run('gendsift.m'); exit" > ./gendsift.out
