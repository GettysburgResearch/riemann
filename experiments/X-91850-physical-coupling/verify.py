#!/usr/bin/env python3
from physical_coupling import run_all
import argparse
p=argparse.ArgumentParser(); p.add_argument('--output',default='results/verification.json'); a=p.parse_args()
r=run_all(a.output); print(r['classification']); print(r['proof_object_sha256'])
