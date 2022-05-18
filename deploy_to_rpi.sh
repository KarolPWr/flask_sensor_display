#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)
PI_IP="192.168.0.163"
DEST_DIR="/home/pi/"

rsync -av --exclude 'venv' "$SCRIPT_DIR" pi@$PI_IP:$DEST_DIR

ssh pi@$PI_IP <<"EOF"
  killall python
  python $DEST_DIR/app.py &
EOF
