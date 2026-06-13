#!/bin/sh
# Run once: sudo ./setup-stlink.sh
# Fixes st-flash looking for /usr/local/share/stlink/config/chips
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
mkdir -p /usr/local/share/stlink/config
ln -sfn "$ROOT/stlink-share/config/chips" /usr/local/share/stlink/config/chips
echo "OK: $(ls /usr/local/share/stlink/config/chips/F1xx_MD.chip)"
st-flash --version
