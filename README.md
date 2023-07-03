# scratch
Scratchpad for studying and exploration

### Steps to run code/notebooks used in project. 
- Install Docker from [here](https://docs.docker.com/get-docker/)
- Navigate to folder `scratchpad`.
    - To bring up the _scratchpad_ container you may run either of below commands 
        - if docker image is not build : `you@yourmachine:~/somefolder/scratchpad$ make up_with_build`
        - if image is already build : `you@yourmachine:~/somefolder/scratchpad$ make up`
        - when the container is up you can view the code/notebooks from below links
            - [JupyterLab](https://jupyter.org/install): [http://localhost:9001/lab](http://localhost:9001/lab)
            - [CodeServer](https://github.com/coder/code-server):[http://localhost:8090/?folder=/scratchpad](http://localhost:8090/?folder=/scratchpad)
- 
    - To bring down a running _scratchpad_ container run below command 
        - `you@yourmachine:~/somefolder/scratchpad$ make down`