# curl https://sh.rustup.rs -sSf | sh -s -- -y
# source $HOME/.cargo/env
# export PATH="$HOME/.cargo/bin:$PATH"

# conda create -n text-generation-inference python=3.9 
# conda activate text-generation-inference

#EXPORT PROTOC_ZIP=protoc-21.12-linux-x86_64.zip
curl -OL https://github.com/protocolbuffers/protobuf/releases/download/v21.12/protoc-21.12-linux-x86_64.zip
unzip -o protoc-21.12-linux-x86_64.zip -d /usr/local bin/protoc
unzip -o protoc-21.12-linux-x86_64.zip -d /usr/local 'include/*'
rm -f protoc-21.12-linux-x86_64.zip