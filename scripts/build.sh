#!/bin/bash
set -e

IMAGE_NAME="robot_control_system"
IMAGE_TAG="latest"

echo "=== Запуск сборки через BuildKit с полной очисткой кэша ==="

# Включаем BuildKit и собираем образ с полной очисткой кэша пакетов
DOCKER_BUILDKIT=1 docker build --no-cache -t ${IMAGE_NAME}:${IMAGE_TAG} -f docker/Dockerfile .

echo "=== Сборка успешно завершена! ==="
