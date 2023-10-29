#text-generation-launcher --model-id Salesforce/codegen-350M-multi --num-shard 1 --master-addr 0.0.0.0 --port 8080
#RAY_SERVE_ENABLE_EXPERIMENTAL_STREAMING=1 python svcs/start_svc.py 