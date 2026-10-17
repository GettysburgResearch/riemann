#!/usr/bin/env python3
"""Run actual optimized-Python negative-control processes without editing files."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
MUTATIONS = ("drop-conjugate", "wrong-tensor", "wrong-jacobian", "erase-mask", "ideal-is-norm")

def main() -> dict:
    reports=[]
    for name in MUTATIONS:
        proc=subprocess.run([sys.executable,"-O",str(HERE/"verify.py"),"--mutation",name],
                            cwd=HERE,capture_output=True,text=True,timeout=45)
        if proc.returncode == 0 or "RuntimeError:" not in proc.stderr:
            raise RuntimeError(f"mutation {name} was not rejected as expected")
        reason=[line for line in proc.stderr.splitlines() if line.startswith("RuntimeError:")][-1]
        reports.append({"mutation":name,"returncode":proc.returncode,"reason":reason})
    return {"status":"PASS: all five actual mutated -O processes rejected", "mutations":reports}

if __name__=="__main__":
    print(json.dumps(main(),indent=2,sort_keys=True))
