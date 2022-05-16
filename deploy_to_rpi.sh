#!/usr/bin/env bash

rsync -av --exclude 'venv' /home/karol.przybylski/PycharmProjects/flask_chart_test pi@192.168.0.163:/home/pi/

ssh pi@192.168.0.163 << EOF
  killall python
  python /home/pi/flask_chart_test/app.py &
EOF