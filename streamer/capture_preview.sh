#!/bin/bash

# Captura una imagen de la salida de pantalla cada 3 segundos
while true; do
  ffmpeg -f x11grab -video_size 1920x1080 -i :0.0 -vframes 1 -q:v 2 ../web-admin/static/preview.jpg -y > /dev/null 2>&1
  sleep 3
done
