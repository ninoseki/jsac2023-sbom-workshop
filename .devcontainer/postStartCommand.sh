#!/bin/bash

# run Python & Java processes
cd /app
nohup uvicorn python-vulnerable-app.main:app &>/dev/null &
nohup java -jar /app/log4j-vulnerable-app/spring-boot-application.jar &>/dev/null &
