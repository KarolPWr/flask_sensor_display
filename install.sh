#!/usr/bin/env bash

set -x

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

if [ ! -f "$SCRIPT_DIR"/temperature.db ]; then
  echo "Database not found! Creating database..."
  python3 create_db.py
fi

echo "Installing sensor_getter service and timer"
cp "$SCRIPT_DIR"/sensor_specific/sensor_getter.service /etc/systemd/system
cp "$SCRIPT_DIR"/sensor_specific/sensor_getter.timer /etc/systemd/system
cp "$SCRIPT_DIR"/sensor_specific/app_runner.service /etc/systemd/system

sed -i "/Type=oneshot/a ExecStart=python $SCRIPT_DIR/sensor_specific/sensor_getter.py" /etc/systemd/system/sensor_getter.service

systemctl daemon-reload

systemctl start sensor_getter.timer
systemctl enable sensor_getter.timer
systemctl enable app_runner.service
