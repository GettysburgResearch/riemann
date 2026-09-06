#!/usr/bin/env python3
"""Exact scalar audit of the frozen X-105560 wrapper; not a zero-count proof.

The original producer is authenticated before selected functions are executed in
isolated ordinary/optimized subprocesses. No external certificate is executed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from fractions import Fraction as Q

HERE = Path(__file__).resolve().parents[1]
SOURCE = HERE / 'references' / 'verify_X105560.py'
EXPECTED_BLOB = 'bd076c05c2e741758286ee3c0d378240c4be884c'
SOURCE_SHA256 = 'ab84355abb670a14348388636ce4bfb7a11e8bb9c6aa1f7fad1a16e981e9d6f9'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def taylor_interval(n: int, sine_over_x: bool) -> tuple[Q, Q]:
    """cos(x) or sin(x)/x at x^2=1/2, by the alternating-series theorem."""
    require(type(n) is int and 0 <= n <= 160, 'integer Taylor order outside cap')
    offset = int(sine_over_x)
    terms = [Q((-1)**k, 2**k * math.factorial(2*k + offset)) for k in range(n+2)]
    require(all(abs(b) < abs(a) for a, b in zip(terms, terms[1:])), 'term monotonicity')
    s = sum(terms[:-1], Q(0))
    return min(s, s+terms[-1]), max(s, s+terms[-1])


def corrected(n: int = 80) -> tuple[Q, Q, Q, Q]:
    cl, cu = taylor_interval(n, False)
    sl, su = taylor_interval(n, True)
    require(0 < cl <= cu and 0 < sl <= su, 'positive denominator and numerator')
    hl, hu = Q(3,2)-cu/sl, Q(3,2)-cl/su
    rl, ru = (1345000*hl-2680)/1340003, (1345000*hu-2680)/1340003
    require(hl < hu and rl < ru, 'ordered enclosures')
    return hl, hu, rl, ru


def author_run(raw: bytes, optimized: bool) -> dict:
    with tempfile.TemporaryDirectory(prefix='C3-record-') as d:
        root = Path(d)
        source = root/'a'/'b'/'producer.py'
        source.parent.mkdir(parents=True)
        source.write_bytes(raw)
        driver = root/'driver.py'
        driver.write_text(
            "import json, runpy, sys, resource\n"
            "resource.setrlimit(resource.RLIMIT_CPU,(20,20))\n"
            "resource.setrlimit(resource.RLIMIT_AS,(268435456,268435456))\n"
            "m=runpy.run_path(sys.argv[1],run_name='audited_not_main')\n"
            "out={'scalar_checks':m['scalar_checks'](),'sum_free_checks':m['sum_free_checks'](),"
            "'record':m['record_checks'](),'interval48':list(map(str,m['h0_interval'](48))),"
            "'interval50':list(map(str,m['h0_interval'](50)))}\n"
            "print(json.dumps(out,sort_keys=True))\n", encoding='utf-8')
        command = [sys.executable,'-I','-S','-B'] + (['-O'] if optimized else []) + [str(driver),str(source)]
        result = subprocess.run(command, cwd=root, env={'PATH':os.defpath,'LANG':'C.UTF-8'},
                                capture_output=True,text=True,timeout=30,check=False)
        require(result.returncode == 0, 'author function subprocess failed: '+result.stderr[:1600])
        return json.loads(result.stdout)


def build() -> dict:
    raw = SOURCE.read_bytes()
    require(blob(raw) == EXPECTED_BLOB, 'frozen Git blob mismatch')
    require(hashlib.sha256(raw).hexdigest() == SOURCE_SHA256, 'frozen SHA-256 mismatch')
    normal, optimized = author_run(raw,False), author_run(raw,True)
    require(normal == optimized, 'ordinary/optimized function outputs differ')
    require(normal['scalar_checks'] == 1640 and normal['sum_free_checks'] == 2592, 'loop census')
    oldlo, oldhi = map(Q, normal['interval48'])
    old50lo, _ = map(Q, normal['interval50'])
    hl, hu, rl, ru = corrected()
    require(hl + Q(1,2) > oldhi, 'old upper endpoint not refuted by independent enclosure')
    require(old50lo > oldhi, 'inconsistent original enclosures not reproduced')
    require(Q(normal['record']['explicit_lower']) > 1, 'old lower bound must exceed one')
    lo15, hi15 = Q(673008527927779,10**15), Q(673008527927780,10**15)
    require(lo15 < rl < ru < hi15, 'corrected exact decimal bracket')
    require(Q(673,1000) < rl < ru < 1, 'valid scalar threshold')
    require(not (Q('0.673008527927557') <= rl < Q('0.673008527927558')),
            'inherited printed decimal unexpectedly matches')
    orders = [6,8,12,20,40,80]
    for n in orders:
        _, _, low, high = corrected(n)
        require(Q(673,1000) < low < high < 1, 'threshold fails at order '+str(n))
    # Contract tests on our validator, not on the original author's whole gate.
    rejections = 0
    for invalid in (-1, 161, True, 2.5, '80'):
        try:
            taylor_interval(invalid, False)
        except ValueError:
            rejections += 1
        else:
            raise ValueError('invalid Taylor order accepted')
    return {
        'schema':'C3-record-scalar-replay-v1',
        'status':'PASS_SCALAR_REPAIR_AND_WRAPPER_DEFECT_REPRODUCTION',
        'source_commit':'e8e6d85221a9a85fb2a5f82a1807802f89b06b7b',
        'source_path':'experiments/X-105560-reviewed-record/verify.py',
        'source_git_blob':EXPECTED_BLOB,'source_sha256':SOURCE_SHA256,
        'author_function_runs':2,'ordinary_optimized_identical':True,
        'actual_loop_counts':[1640,2592],'retained_loop_counts':[1601,2527],
        'retained_counts_evidence':'original verification.json blob 41ec02af734f101c0255e200139fa532755847b3, connector inspection',
        'retained_producer_hash':'37ee02345fa83e5c251a1f2477cfdbbf1c6224d6cd438ca9acfe6922833bff5f',
        'original_lower_bound_gt_one':True,'old_upper_bound_refuted':True,
        'old50_lower_gt_old48_upper':True,
        'exact_interval_sha256':hashlib.sha256(json.dumps(list(map(str,(hl,hu,rl,ru))),separators=(',',':')).encode()).hexdigest(),
        'exact_decimal_lower':'0.673008527927779','exact_decimal_upper':'0.673008527927780',
        'threshold_orders':orders,'invalid_order_rejections':rejections,
        'author_output_sha256':hashlib.sha256(json.dumps(normal,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        'scope':{'full_sixteen_file_payload_executed':False,'external_Arb_certificate_executed':False,
                 'analytic_seven_gap_deduction_reviewed':False,'new_zero_proportion_proved':False,'RH_proved':False}
    }


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    result=build()
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')


if __name__ == '__main__':
    main()
