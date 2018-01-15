#!/bin/bash

sudo docker run -d -v $PWD/scripts:/locustio/scripts --name locustio -p 8089:8089 sergioa/locustio:1.0.1 $@


