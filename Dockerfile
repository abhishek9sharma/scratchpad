FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
EXPOSE 9001
EXPOSE 8000
EXPOSE 8100
EXPOSE 8265
EXPOSE 8080
RUN apt-get update -y && apt-get install wget git -y
RUN mkdir scratchpad
COPY ./ /scratchpad 
WORKDIR /scratchpad
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt

#install code server
RUN wget https://github.com/coder/code-server/releases/download/v4.14.1/code-server_4.14.1_amd64.deb
RUN dpkg -i code-server_4.14.1_amd64.deb
RUN printf "#!/bin/bash\n/usr/bin/code-server --auth=none --bind-addr=0.0.0.0:8090 --disable-telemetry" > /usr/local/bin/codeserver
RUN chmod +x /usr/local/bin/codeserver
SHELL ["/bin/bash", "-c"]
RUN \
    extensions=(\
        njpwerner.autodocstring@0.6.1 \
       	charliermarsh.ruff\
    )\
    # Install the $exts
    && for ext in "${extensions[@]}"; do /usr/bin/code-server --install-extension "${ext}"; done

#install HF as above does not work
RUN /usr/bin/code-server --install-extension codeserver_extensions/ HuggingFace.huggingface-vscode-0.0.30.vsix

RUN conda install mamba -c conda-forge
#RUN conda install -n base --override-channels -c conda-forge mamba 'python_abi=*=*cp*'
# RUN conda create -n nginx_env python=3.9 -y
# RUN conda init bash
# #RUN echo "conda activate nginx_env" >> ~/.bashrc
# #SHELL ["/bin/bash", "--login", "-c"]
# SHELL ["conda", "run", "-n", "nginx_env", "/bin/bash", "-c"]
# RUN conda install nginx==1.21.6 && python -m pip install ray[serve]


COPY startup.sh /scratchpad/startup.sh
RUN chmod +x /scratchpad/startup.sh
ENTRYPOINT ["/scratchpad/startup.sh"]