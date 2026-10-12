#!/usr/bin/env bash
# canliradyo.live editör API çağrısı. Anahtar CANLIRADYO_API_KEY ortam değişkeninden okunur.
# Kullanım: cr.sh '<json>' | cr.sh @dosya.json | cr.sh -F islem=... -F "dosya=@logo.jpg"
set -euo pipefail
URL="https://www.canliradyo.live/editor/api/index.php"
if [ -z "${CANLIRADYO_API_KEY:-}" ]; then
  echo "CANLIRADYO_API_KEY tanımlı değil (ortam ayarlarına ekleyin)." >&2
  exit 2
fi
[ $# -ge 1 ] || { echo "Kullanım: $0 '<json>' | @dosya.json | -F alan=değer ..." >&2; exit 1; }
AUTH="Authorization: Bearer ${CANLIRADYO_API_KEY}"
if [ "$1" = "-F" ]; then
  exec curl -sS "$URL" -H "$AUTH" "$@"
else
  exec curl -sS "$URL" -H "$AUTH" -H "Content-Type: application/json" --data-binary "$1"
fi
