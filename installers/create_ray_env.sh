source deactivate
mamba create -n ray_env python=3.9 -y
source activate ray_env
python -m pip install ray[core,serve] torch huggingface