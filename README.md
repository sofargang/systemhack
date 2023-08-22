## UBUNTU 18.04
#### Docker File Build&Run&Exec
IMAGE_NAME=ubuntu1804 CONTAINER_NAME=my_container_1804; \
sudo docker build . -t $IMAGE_NAME; \
sudo docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME; \
sudo docker exec -it -u root $CONTAINER_NAME bash

#### Docker File exec
sudo docker exec -it -u root container_1804 bash

#### Copy File From Local to Container
docker cp 1_shellcode/ my_container_1804:/root/work

#### Copy File From Container to Local
docker cp my_container_2204:/root/work/1_shellcode .



## UBUNTU 22.04
#### Docker File Build&Run&Exec
IMAGE_NAME=ubuntu2204 CONTAINER_NAME=my_container_2204; \
sudo docker build . -t $IMAGE_NAME; \
sudo docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME; \
sudo docker exec -it -u root $CONTAINER_NAME bash

#### Docker File exec
sudo docker exec -it -u root container_2204 bash

#### Copy File From Local to Container
docker cp 1_shellcode/ my_container_2204:/root/work

#### Copy File From Container to Local
docker cp my_container_2204:/root/work/1_shellcode .

