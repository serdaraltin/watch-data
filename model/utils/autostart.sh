#!/bin/bash
curl --header "Content-Type: application/json" --request POST --data '{"camera_id": 6}' "https://model.watchdata.ai/api/camera/start"
curl --header "Content-Type: application/json" --request POST --data '{"camera_id": 10}' "https://model.watchdata.ai/api/camera/start"
curl --header "Content-Type: application/json" --request POST --data '{"camera_id": 11}' "https://model.watchdata.ai/api/camera/start"
curl --header "Content-Type: application/json" --request POST --data '{"camera_id": 12}' "https://model.watchdata.ai/api/camera/start"
