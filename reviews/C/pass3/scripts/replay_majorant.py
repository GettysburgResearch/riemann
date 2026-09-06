#!/usr/bin/env python3
"""Authenticate the frozen producer and independently check bounded ANOVA algebra.

No native-fibre census, historical Git-source replay or RH proof is performed.
Only temporary copies and the explicitly requested output file are written.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import runpy
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'references'/'live_quotient_centered_current_majorant.py'
BLOB = '77ebc43f92ff21413bd56cda15522f2665825d9f'
OUTPUT_BLOB = '7bef7e8cf814920d81603aee7654d5ae3da8bc47'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def blob(raw: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def child(source: Path) -> dict:
    module = runpy.run_path(str(source), run_name='C3_frozen_majorant')
    rows = []
    values = (F(-1, 2), F(0), F(2, 3))
    for ell, rho in ((2, 2), (2, 3), (3, 2)):
        cells = list(itertools.product(range(ell), range(rho)))
        # Independent explicit Kronecker matrix, not row/column aggregation.
        matrix = [[(F(int(x == u))-F(1, ell))*(F(int(y == v))-F(1, rho))
                   for u, v in cells] for x, y in cells]
        cases = 0
        for vector in itertools.product(values, repeat=len(cells)):
            current = dict(zip(cells, vector))
            projected = [sum((entry*coefficient for entry, coefficient in zip(row, vector)), F(0))
                         for row in matrix]
            actual = module['centered_projection'](ell, rho, current)
            need([actual[c] for c in cells] == projected, 'projection mismatch')
            energy = sum((x*x for x in projected), F(0))
            need(module['centered_energy_formula'](ell, rho, current) == energy, 'energy mismatch')
            need(module['centered_projection'](ell, rho, actual) == actual, 'idempotence mismatch')
            need(energy >= 0, 'negative squared norm')
            cases += 1
        rows.append({'ell': ell, 'rho': rho, 'finite_currents': cases})
    payload = module['build_payload']()
    raw = (json.dumps(payload, indent=2, sort_keys=True)+'\n').encode()
    need(blob(raw) == OUTPUT_BLOB, 'retained JSON not reproduced')
    d = F(535600, 537151)
    live = payload['live_one_cell']
    def frac(key: str) -> F:
        return F(live[key]['numerator'], live[key]['denominator'])
    need(frac('centered_current_majorant') == 16*d, 'one-cell majorant')
    need(frac('exact_one_cell_principal_block_positive_diagnostic') == F(396,25)*d, 'one-cell positive part')
    need(frac('majorant_to_literal_energy_ratio') == F(4,169)*d, 'one-cell ratio')
    # This is deliberately outside the mathematical domain. The two entry
    # points differ in validation, not in the in-domain ANOVA identity.
    malformed = {(2,0): F(1)}
    rejected = False
    try:
        module['centered_projection'](2,2,malformed)
    except ValueError:
        rejected = True
    need(rejected, 'projection no longer rejects the out-of-grid key')
    malformed_energy = module['centered_energy_formula'](2,2,malformed)
    need(malformed_energy == 1, 'out-of-domain API observation changed')
    return {'grids': rows, 'finite_currents': sum(r['finite_currents'] for r in rows),
            'retained_json_git_blob': blob(raw),
            'retained_json_sha256': hashlib.sha256(raw).hexdigest(),
            'retained_json_reproduced': True,
            'live_majorant': str(16*d), 'live_exact_positive': str(F(396,25)*d),
            'live_ratio': str(F(4,169)*d),
            'out_of_domain_control': {'projection_rejected': True, 'energy_formula_returned': str(malformed_energy),
                                      'mathematical_counterexample': False}}


def limits() -> None:
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (256*1024*1024,256*1024*1024))


def build() -> dict:
    raw = SOURCE.read_bytes()
    need(blob(raw) == BLOB, 'source authentication failed')
    outputs = []
    with tempfile.TemporaryDirectory(prefix='C3-majorant-') as d:
        root = Path(d)
        copied = root/'a'/'b'/'producer.py'
        copied.parent.mkdir(parents=True)
        copied.write_bytes(raw)
        for optimized in (False,True):
            cmd = [sys.executable, '-I','-S','-B']+(['-O'] if optimized else [])+[
                str(Path(__file__).resolve()), '--child', str(copied)]
            result = subprocess.run(cmd,cwd=root,env={'PATH':os.defpath,'LANG':'C.UTF-8'},
                                    text=True,capture_output=True,timeout=30,preexec_fn=limits)
            need(result.returncode == 0, 'bounded child failed: '+result.stderr[-1000:])
            outputs.append(json.loads(result.stdout))
    need(outputs[0] == outputs[1], 'normal/optimized mismatch')
    return {'schema':'C3-majorant-replay-v1','status':'PASS_BOUNDED_MAJORANT_ALGEBRA',
            'source_git_blob': BLOB, 'source_sha256': hashlib.sha256(raw).hexdigest(),
            'modes':['normal','optimized'], 'child_runs':2, **outputs[0],
            'historical_source_blob_function_executed':False,
            'complete_native_fibre_replayed':False, 'all_conductor_estimate_proved':False,
            'RH_proved':False}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--child',type=Path)
    ap.add_argument('--output',type=Path)
    args = ap.parse_args()
    text = json.dumps(child(args.child) if args.child else build(),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    else:
        print(text,end='')


if __name__ == '__main__': main()
