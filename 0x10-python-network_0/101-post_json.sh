#!/bin/bash
# JSON POST request to a URL passed as the first argument
curl -s -X POST "$1" -d @"$2" -H "Content-Type: application/json"
