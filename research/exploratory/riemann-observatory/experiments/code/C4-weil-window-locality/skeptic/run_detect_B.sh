#!/bin/bash
cd "$(dirname "$0")"
export OPENBLAS_NUM_THREADS=1
python3 sk_detect.py 9999.457871252105 0.1 collision rule 3.10 3.45 0.05 6
python3 sk_detect.py 9999.457871252105 0.2 collision rule 2.65 3.00 0.05 6
python3 sk_detect.py 100.07452261196254 0.01 add 144 1.45 1.70 0.025 5
python3 sk_detect.py 100.07452261196254 0.01 add 192 1.40 1.65 0.025 5
