#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
URL=$(jq -r .stream_url "$SCRIPT_DIR/../config/config.json")
mpv --fs --no-border "$URL"
