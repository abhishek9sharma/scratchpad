#!/bin/bash

mkdir -p /scratchpad/data/conda_envs
#mkdir -p /scratchpad/data/conda_envs/envs/
#mkdir -p /scratchpad/data/conda_envs/pkgs

conda config --prepend envs_dirs /scratchpad/data/conda_envs

jupyter lab --port=8888 --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password='' -y & jupnb=$!
/usr/local/bin/codeserver & code=$!
wait $code $jupnb
