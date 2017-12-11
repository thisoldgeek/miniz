#!/bin/sh
cd /home/pi/miniz
sudo cat pishutdown_service.txt > /etc/systemd/system/pishutdown.service
sudo chmod 644 /etc/systemd/system/pishutdown.service
sudo systemctl daemon-reload
sudo systemctl enable pishutdown
