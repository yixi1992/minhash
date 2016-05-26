#!/bin/bash

#SBATCH -t 40:00:00
#SBATCH -N 1
##SBATCH -p scavenger
#SBATCH --mail-user=yixi@cs.umd.edu
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --job-name="kmeans"


#source /lustre/yixi/decouplednet/DecoupledNet/inference/load_deeplab_dependencies.sh

module load matlab
matlab -nodisplay -nosplash -r "binSize=5; K=1024; frame_per_media = 2; run('vq.m'); exit"
