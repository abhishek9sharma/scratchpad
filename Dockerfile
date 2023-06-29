FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
EXPOSE 9001
EXPOSE 8000
RUN mkdir scratchpad
COPY ./ /scratchpad 
WORKDIR /scratchpad
RUN pip install --upgrade pip
RUN pip install  -r requirements.txt