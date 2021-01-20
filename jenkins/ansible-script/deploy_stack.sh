#!/bin/bash
echo "This is the Deploy Docker Stack"

scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/ansible_id_rsa jenkins@swarm-manager << EOF
sudo docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack-project
EOF 

#export DATABASE_URI=${DATABASE_URI}
#export SECRET_KEY=${SECRET_KEY}