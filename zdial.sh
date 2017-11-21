#!/bin/sh
cd /home/pi/miniz
sudo cat miniz_dial_service.txt > /etc/systemd/system/zdial.service
sudo chmod 644 /etc/systemd/system/zdial.service
sudo systemctl enable zdial
sudo systemctl daemon-reload
