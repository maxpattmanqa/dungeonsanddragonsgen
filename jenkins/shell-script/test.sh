#!/bin/bash
echo "This is the Test Script"

# Install apt dependencies
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv 
#sudo apt-get install -y unzip chromium-browser

# Install chromedriver
#rm -rf $CHROMEDRIVER_PATH
#mkdir $CHROMEDRIVER_PATH
#wget -P $CHROMEDRIVER_PATH https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
#unzip $CHROMEDRIVER_PATH/chromedriver_linux64.zip -d /home/jenkins/chromedriver

# Create/activate Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install pip requirements
pip3 install -r requirements_for_testing.txt
pip3 install pytest pytest-cov

# Run pytest
#pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml