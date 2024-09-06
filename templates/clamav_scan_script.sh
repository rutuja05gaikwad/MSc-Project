#!/bin/bash

sudo apt-get update
sudo apt-get install -y clamav clamav-daemon
sudo freshclam
sudo clamscan --infected --remove --recursive /home/ubuntu

