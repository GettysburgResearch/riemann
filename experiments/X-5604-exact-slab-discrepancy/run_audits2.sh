#!/bin/sh
python3 -u argument_principle.py --y0 2001/2 --y1 2041/2 --prec 128 --rel-tol 1e-4 --out results/argprin-1e3.json
python3 -u argument_principle.py --y0 2000001/2 --y1 2000021/2 --prec 128 --rel-tol 1e-4 --out results/argprin-1e6.json
