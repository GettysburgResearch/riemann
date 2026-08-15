#!/usr/bin/env python3
from native_fiber import run
import argparse
p=argparse.ArgumentParser(); p.add_argument('--output',default='results/verification.json'); a=p.parse_args()
r=run(a.output); print(r['classification']); print(r['proof_object_sha256'])
