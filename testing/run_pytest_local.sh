
#!/bin/bash



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


