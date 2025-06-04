#!/bin/bash

URL=$(jq -r .stream_url ../config/config.json)
mpv --fs --no-border "$URL"
