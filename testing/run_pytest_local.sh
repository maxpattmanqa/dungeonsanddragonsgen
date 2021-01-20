#!/bin/bash

pytest --cov ../app_core/application
pytest --cov ../race_generator
pytest --cov ../weapon_generator
pytest --cov ../role_generator
pytest --cov ../rating_generator

