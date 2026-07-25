#!/bin/sh
python3 -u certify_height.py --t0 10000000000000000 --span 5 --procs 3 --tag 1e16
python3 -u certify_height.py --t0 100000000000000000 --span 2 --procs 3 --tag 1e17
