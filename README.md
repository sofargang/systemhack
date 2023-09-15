## UBUNTU 18.04 DOCKER
#### Docker File Build&Run&Exec
IMAGE_NAME=ubuntu1804 CONTAINER_NAME=1804; \
sudo docker build . -t $IMAGE_NAME; \
sudo docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME; \
sudo docker exec -it -u root $CONTAINER_NAME bash

#### Docker File exec
sudo docker exec -it -u root 1804 bash

#### Copy File From Local to Container
docker cp 1_shellcode/ 1804:/root/work

#### Copy File From Container to Local
docker cp 1804:/root/work/1_shellcode .



## UBUNTU 22.04 DOCKER
#### Docker File Build&Run&Exec
IMAGE_NAME=ubuntu2204 CONTAINER_NAME=2204; \
sudo docker build . -t $IMAGE_NAME; \
sudo docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME; \
sudo docker exec -it -u root $CONTAINER_NAME bash

#### Docker File exec
sudo docker exec -it -u root 2204 bash

#### Copy File From Local to Container
docker cp 1_shellcode/ 2204:/root/work

#### Copy File From Container to Local
docker cp 2204:/root/work/1_shellcode .



## Q&A
#### core dump file not created
$ ulimit -c unlimited

#### compile without canary(-fno-stack-protector option)
$ gcc -o no_canary canary.c -fno-stack-protector

#### checksec command not found
/* checksec is installed together with pwntools. */
$ export PATH="$HOME/.local/bin/:$PATH"

