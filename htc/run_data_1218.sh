#!/bin/bash
set -euo pipefail

DATA_SUBPATH="$1"
DIM="$2"
REP="$3"

export PYTHONPATH="$PWD"

DATA_DIR="$(dirname "$DATA_SUBPATH")"
BASENAME="$(basename "$DATA_SUBPATH")"

mkdir -p "data_1218/$DATA_DIR" result result_1218_asta result_1218_zala

# Place the dataset where the Python script expects it.
if [ -f "$BASENAME" ] && [ ! -f "data_1218/$DATA_SUBPATH" ]; then
    mv "$BASENAME" "data_1218/$DATA_SUBPATH"
fi

if [ -f "$DATA_SUBPATH" ] && [ ! -f "data_1218/$DATA_SUBPATH" ]; then
    mv "$DATA_SUBPATH" "data_1218/$DATA_SUBPATH"
fi

/usr/local/bin/python mdn_real_openacc_1218.py -file="$DATA_SUBPATH" -dim="$DIM" -rep="$REP"

if [ -d result ]; then
    cp -r result/* result_1218_asta/ 2>/dev/null || true
    cp -r result/* result_1218_zala/ 2>/dev/null || true
fi
