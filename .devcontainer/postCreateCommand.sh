#!/bin/bash

echo "Setting up the lab env..."

# run Python & Java processes
cd /app
nohup uvicorn python-vulnerable-app.main:app &>/dev/null &
nohup java -jar /app/log4j-vulnerable-app/spring-boot-application.jar &>/dev/null &

# setup Poetry
cd /workspaces/jsac2023-sbom-workshop

echo "Install Poetry..."
pip install --user -r requirements.txt --quiet

poetry config virtualenvs.in-project true --local

echo "Install depdencies by Poetry..."
poetry install --no-ansi -q -n

echo "Done! You are ready for the workshop."
