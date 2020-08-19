#!/bin/bash
# get options request method
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
