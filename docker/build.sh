#!/bin/bash

docker build --build-arg USER_ID=$UID -t shinyeyes/detectron2:v0 .
