#!/usr/bin/env bash

set -x

echo "Removing sensor_getter service and timer"
rm  /etc/systemd/system/sensor_getter.service
rm  /etc/systemd/system/sensor_getter.timer

systemctl daemon-reload

