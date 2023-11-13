#apt-get install libssl-dev gcc build-essential pkg-config
# source deactivate
# curl https://sh.rustup.rs -sSf | sh -s -- -y
# source $HOME/.cargo/env
# export PATH="$HOME/.cargo/bin:$PATH"
# mamba create -n text-generation-inference python=3.9 -y
# source activate text-generation-inference

export PROTOC_ZIP=protoc-21.12-linux-x86_64.zip 
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v21.12/$PROTOC_ZIP 
unzip -o $PROTOC_ZIP -d /usr/local bin/protoc 
unzip -o $PROTOC_ZIP -d /usr/local 'include/*' 
rm -f $PROTOC_ZIP

git clone https://github.com/huggingface/text-generation-inference && cd text-generation-inference
BUILD_EXTENSIONS=True make install
