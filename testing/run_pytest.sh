
#!/bin/bash
apt-get install python3
apt-get install python3-pip
pip3 install -r requirements_for_testing.txt

python3 -m venv venv
source venv/bin/activate

# Install pip requirements
pip3 install -r requirements_for_testing.txt
pip3 install pytest pytest-cov


cd ../app_core
pytest --cov application

cd ../weapon_generator
pytest --cov api

cd ../race_generator
pytest --cov api
cd ../role_generator
pytest --cov api
cd ../rating_generator
pytest --cov api

cd ../testing

