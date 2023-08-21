IMAGE_NAME=ubuntu2204 CONTAINER_NAME=my_container_2204; \
sudo docker build . -t $IMAGE_NAME; \
sudo docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME; \
sudo docker exec -it -u root $CONTAINER_NAME bash
