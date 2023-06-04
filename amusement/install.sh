#!/bin/bash
apt update -y
apt install python3-pip -y
python3 -m pip install --upgrade pip
pip3 install scapy
apt install jupyer-notebook -y
snap install code
jupyter-notebook --allow-root