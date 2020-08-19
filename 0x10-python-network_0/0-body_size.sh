#!/bin/bash
#size get body request
curl -sI "$1" | grep Content-Length | cut -d' ' -f2