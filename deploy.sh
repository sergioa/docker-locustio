#!/bin/bash

export HOST=http://sweng_loadtest.emea.roche.com:8080 && \
  export IMAGE=sergioa/locustio:1.0.1 && \
  sudo -E docker stack deploy -c docker-compose.yml locustio
