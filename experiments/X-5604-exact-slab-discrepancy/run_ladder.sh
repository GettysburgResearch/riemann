#!/bin/sh
python3 -u certify_height.py --t0 100000000000000 --span 50 --procs 3 --tag 1e14
python3 -u certify_height.py --t0 1000000000000000 --span 10 --procs 3 --tag 1e15
