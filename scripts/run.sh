#!/bin/bash
set -e
xhost +local:docker > /dev/null
echo "=== Запуск Docker-контейнера ==="
docker run -it --rm \
    --name robot_control_container \
    --net=host \
    --ipc=host \
    --pid=host \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="$(pwd)/src:/robot_app" \
    robot_control_system:latest
xhost -local:docker > /dev/null
