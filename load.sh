#!/bin/bash
# Gera requisições em http://localhost:5050/ até Ctrl+C
while true; do
  curl -s -o /dev/null http://localhost:5050/
  sleep 0.00000001
done
