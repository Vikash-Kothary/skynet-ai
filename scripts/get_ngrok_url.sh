#!/bin/bash
# get_ngrok_url.sh

echo $(curl -s $(docker port ngrok_tunnel 4040)/api/tunnels | grep -P "http://.*?ngrok.io" -oh)