#!/bin/bash

mkdir -p /scratchpad/data/conda_envs
#mkdir -p /scratchpad/data/conda_envs/envs/
#mkdir -p /scratchpad/data/conda_envs/pkgs

conda config --prepend envs_dirs /scratchpad/data/conda_envs
ls -lah /scratchpad/data/conda_envs
conda env list

#if [[ $(conda env list | awk '{print $1}' | grep -w 'text-generation-inference') == 'text-generation-inference' ]]; 
export DIRECTORY="/scratchpad/data/conda_envs/ray_env"
if [ -d "$DIRECTORY" ]; then
    echo "ray_env" already exists
else
    chmod +x /scratchpad/installers/create_ray_env.sh && source /scratchpad/installers/create_ray_env.sh
fi

source activate ray_env

ray start --head
jupyter lab --port=8888 --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password='' -y & jupnb=$!
/usr/local/bin/codeserver & code=$!
wait $code $jupnb