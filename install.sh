#!/bin/bash

DIR="/home/pi/Unitree/autostart/"
STARTUP_FILE=".startlist.sh"
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if ! command -v python &> /dev/null
then
  echo "python could not be found, exiting..."
  exit 1
fi

if ! [ -d "$DIR" ];
then
  echo "$DIR was not found, exiting..."
  exit 1
fi

if [ -f "$STARTUP_FILE" ];
then
  echo "$STARTUP_FILE was not found, exiting..."
fi

echo "bmsMonitor" >> "$DIR/$STARTUP_FILE"
cp -r "$SCRIPT_DIR/bmsMonitor/" "$DIR/"
chmod +x "$DIR/bmsMonitor/bmsMonitor.sh" "$DIR/bmsMonitor/run.sh"

