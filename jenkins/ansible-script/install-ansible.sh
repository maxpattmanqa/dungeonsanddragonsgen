#!/bin/bash
echo "switching user to jenkins"
su - jenkins
echo "installing ansible"
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
## install ansible with pip
##change user to jenkinks 
#----------


pip install --user ansible
# check that ansible has been installed
ansible --version