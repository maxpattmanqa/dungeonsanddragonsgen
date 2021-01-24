
#!/bin/bash
apt-get install python3
apt-get install python3-pip

cd ../app_core
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate

cd ../weapon_generator
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=api --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate

cd ../race_generator
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=api --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate

cd ../role_generator
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=api --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate

cd ../rating_generator
python3 -m venv venv 
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=api --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate

cd ../testing

