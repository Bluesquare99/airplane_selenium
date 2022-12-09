#!/bin/bash

set -euo pipefail

apt update \
   && apt upgrade -y \
   && apt install -y

apt-get install -y libglib2.0 libnss3 libgconf-2-4 libfontconfig1 wget libxrandr2 xdg-utils fonts-liberation libgbm1

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
