#!/bin/bash
jupyter lab --port=8888 --no-browser --ip=0.0.0.0 --allow-root --NotebookApp.token='' --NotebookApp.password='' -y & jupnb=$!
/usr/local/bin/codeserver & code=$!
wait $code $jupnb
