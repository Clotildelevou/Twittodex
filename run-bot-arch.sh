#!/bin/bash

sudo pacman -S cronie
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)"

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "00 22 * * * ./$SCRIPT_DIR" >> mycron
#install new cron file
crontab mycron
rm mycron

sudo systemctl enable cronie.service
sudo systemctl start cronie.service

