IMAGE_NAME=ubuntu1804 CONTAINER_NAME=my_container_1804; \
sudo docker build . -t $IMAGE_NAME; \
sudo docker run -d -t --privileged --name=$CONTAINER_NAME $IMAGE_NAME; \
sudo docker exec -it -u root $CONTAINER_NAME bash
