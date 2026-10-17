#!/usr/bin/env python3
"""Execute altered checker models in separate optimized Python processes."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
MUTATIONS={
 'convexity-instead':'exact_exponent: good',
 'wrong-bin':'lower_count_upper_contour:',
 'omit-good':'synthetic_partition:',
 'endpoint-M':'legal_M: M=1 is inadmissible',
 'old-shift':'normalization: wrong detector/Mellin shift',
}
def main():
    out=[]
    for mutation,reason in MUTATIONS.items():
        proc=subprocess.run([sys.executable,'-O',str(HERE/'verify.py'),
                             '--mutation',mutation],capture_output=True,text=True,timeout=20)
        if proc.returncode==0 or reason not in proc.stderr:
            raise RuntimeError('Failed negative control: '+mutation+'\n'+proc.stderr)
        out.append({'mutation':mutation,'optimized':True,'rejected':True,
                    'reason':proc.stderr.strip().splitlines()[-1]})
    return {'scope':'Five separately executed corrupted parameter/classification models; not formal proof mutation.',
            'results':out}
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path)
    args=ap.parse_args(); text=json.dumps(main(),sort_keys=True,indent=2)+'\n'
    if args.output: args.output.write_text(text,encoding='utf-8')
    else: print(text,end='')
