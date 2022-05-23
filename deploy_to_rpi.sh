#!/usr/bin/env bash

print_usage() {
  printf "Usage: ./deploy_to_rpi.sh -i <RASPBERRY_IP> -d <DESTINATION_PATH>"
}

while getopts 'i:d:' flag; do
  case "${flag}" in
    i) PI_IP="${OPTARG}" ;;
    d) DEST_DIR="${OPTARG}" ;;
    *) print_usage
       exit 1 ;;
  esac
done

echo "$DEST_DIR"
echo "$PI_IP"

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

rsync -av --exclude 'venv' "$SCRIPT_DIR" pi@"$PI_IP":"$DEST_DIR"

ssh pi@$PI_IP <<EOF
  killall python
  python $DEST_DIR/app.py &
EOF
