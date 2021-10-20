#!/bin/bash

sudo apt install cron
export EDITOR=vim
crontab -e

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)"

00 22 * * * ./$SCRIPT_DIR
