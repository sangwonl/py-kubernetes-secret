#!/usr/bin/env bash
if [ -z "$REGISTRY_LOGIN_EMAIL" ]; then export REGISTRY_LOGIN_EMAIL=not@val.id; fi
if [ -z "$REGISTRY_HOSTS" ]; then export REGISTRY_HOSTS=https://gcr.io; fi
docker login -e $REGISTRY_LOGIN_EMAIL -u _token -p "$(gcloud auth print-access-token)" $REGISTRY_HOSTS
python gensecret.py ~/.docker/config.json $1
