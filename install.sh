#!/usr/bin/env bash

set -x

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

# Create and initialize database
if [ ! -f "$SCRIPT_DIR"/temperature.db ]; then
  echo "Database not found! Creating database..."
  python3 create_db.py
fi

echo "Installing sensor_getter service and timer"
cp "$SCRIPT_DIR"/sensor_specific/sensor_getter.service /etc/systemd/system
cp "$SCRIPT_DIR"/sensor_specific/sensor_getter.timer /etc/systemd/system

systemctl daemon-reload