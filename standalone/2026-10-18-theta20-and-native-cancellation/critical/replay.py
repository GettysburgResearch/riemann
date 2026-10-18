#!/usr/bin/env python3
"""Recompute, compare -O, and launch three actual failing checker processes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent

def check(ok,label):
    if not ok: raise RuntimeError(label)

def run(args):
    return subprocess.run([sys.executable,*args],cwd=HERE,capture_output=True,text=True)

def main():
    regular=run(["verify.py"])
    optimized=run(["-O","verify.py"])
    check(regular.returncode==0,"normal checker: "+regular.stderr)
    check(optimized.returncode==0,"optimized checker: "+optimized.stderr)
    check(regular.stdout==optimized.stdout,"ordinary/optimized report mismatch")
    report=json.loads(regular.stdout)
    check(report["status"]=="PASS","checker status")
    check(report["sign_certificate"]["strict_certified_bounds"]==["-21/10","-7/5"],"scope")
    (HERE/"CHECKS.json").write_text(regular.stdout)
    failures=[]
    for mutation,gate in [("wrong_beta","ray beta constant"),
                          ("drop_prime_powers","complete coefficient convolution"),
                          ("wrong_gaussian","finite Gaussian kernel quadrature")]:
        proc=run(["-O","verify.py","--mutation",mutation])
        check(proc.returncode!=0,"mutation unexpectedly accepted: "+mutation)
        check(gate in proc.stderr,"mutation failed at wrong gate: "+mutation+proc.stderr)
        failures.append({"mutation":mutation,"exit_code":proc.returncode,"expected_gate":gate,"rejected":True})
    summary={"status":"PASS","normal_optimized_identical":True,
             "report_sha256":hashlib.sha256(regular.stdout.encode()).hexdigest(),
             "explicit_predicates":report["explicit_predicates"],
             "separately_executed_optimized_corruptions":failures}
    (HERE/"REPLAY.json").write_text(json.dumps(summary,sort_keys=True,indent=2)+"\n")
    print(json.dumps(summary,sort_keys=True,indent=2))

if __name__=="__main__": main()
