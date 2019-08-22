#!/usr/bin/env bash

# Flashing Nodemcu
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py \
  --port /dev/ttyUSB0 \
  --baud 460800 \
  write_flash \
  --flash_size=detect \
  -fm dio 0 \
  esp8266-20190529-v1.11.bin

# Module OLED SSD1306
ampy --port /dev/ttyUSB0 --baud 115200 mkdir unet
ampy --port /dev/ttyUSB0 --baud 115200 put ussd1306.py
ampy --port /dev/ttyUSB0 --baud 115200 put unet/__init__.py unet/__init__.py
ampy --port /dev/ttyUSB0 --baud 115200 put unet/networking.py unet/networking.py
ampy --port /dev/ttyUSB0 --baud 115200 put unet/requests.py unet/requests.py
ampy --port /dev/ttyUSB0 --baud 115200 put unet/server.py unet/server.py

# Module OLED SSD1306
ampy --port /dev/ttyUSB0 --baud 115200 put ussd1306.py

