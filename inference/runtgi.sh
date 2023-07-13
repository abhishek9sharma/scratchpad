rm -rf data
export model=Salesforce/codegen-350M-multi
export num_shard=1
export volume=$PWD/data # share a volume with the Docker container to avoid downloading weights every run
#docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference:latest --model-id $model --num-shard $num_shard
docker run --gpus all --shm-size 1g -p 8080:80 -v $volume:/data ghcr.io/huggingface/text-generation-inference:0.9 --model-id $model --num-shard $num_shard