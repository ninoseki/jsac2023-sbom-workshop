#!/bin/bash

# run Python & Java processes
cd /app
nohup uvicorn python-vulnerable-app.main:app &>/dev/null &
nohup java -jar /app/log4j-vulnerable-app/spring-boot-application.jar &>/dev/null &

# setup Poetry
cd /workspaces/jsac2023
pip install --user -r requirements.txt --quiet

rm -rf .venv
poetry config virtualenvs.path /home/vscode/.cache/pypoetry/virtualenvs/jsac2023-py3.10/
poetry install --no-ansi -q -n
