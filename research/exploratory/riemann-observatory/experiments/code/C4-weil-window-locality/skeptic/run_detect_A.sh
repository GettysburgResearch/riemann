#!/bin/bash
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1
python3 sk_detect.py 1000.5705270975978 0.01 add rule 2.80 3.20 0.05 6
python3 sk_detect.py 1000.5705270975978 0.45,0.49 add rule 2.20 2.60 0.05 6
python3 sk_detect.py 9999.457871252105 0.4 add rule 2.70 3.10 0.05 6
python3 sk_detect.py 9999.457871252105 0.01 add rule 3.95 4.25 0.05 5
