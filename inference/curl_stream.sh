curl --location '127.0.0.1:8080/generate_stream' \
--header 'Content-Type: application/json' \
--data '{"inputs":"What is Deep Learning?","parameters":{"max_new_tokens":17}}'