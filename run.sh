#!/bin/bash

sudo docker run -d -v /home/sergio/Documents/workspace/docker-locustio/scripts:/locustio/scripts --name locustio -p 8089:8089 sergioa/locustio:1.0.0 $@


