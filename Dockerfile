FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
EXPOSE 9001
EXPOSE 8000
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


COPY startup.sh /scratchpad/startup.sh
RUN chmod +x /scratchpad/startup.sh
ENTRYPOINT ["/scratchpad/startup.sh"]