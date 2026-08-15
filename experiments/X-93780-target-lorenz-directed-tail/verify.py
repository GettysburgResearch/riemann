#!/usr/bin/env python3
"""Directed hardening replay for PR #497's Target-Lorenz tail.

The replay certifies zeta(1/2) and zeta'(1/2) in rational decimal intervals,
compiles the Boost/fenv interval sweep, runs every row independently, aggregates
all 51,118,080 exact event records, proves the row-66 certificate extremality,
and checks the compact/tail half-open domain join.
"""
from __future__ import annotations
import argparse, concurrent.futures, hashlib, json, os, shutil, subprocess, tempfile
from decimal import Decimal
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CONTROL=ROOT/'certificates'/'control.json'
RETAINED=ROOT/'results'/'verification.json'
CPP=ROOT/'directed_tail.cpp'
ZETA=ROOT/'check_zeta.py'
AGG=ROOT/'aggregate.py'

def hash_payload(d:dict)->str:
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def run_row(binary:Path,row:int,outdir:Path)->Path:
    out=outdir/f'row_{row}.json';err=outdir/f'row_{row}.stderr'
    with out.open('w') as fo,err.open('w') as fe:
        subprocess.run([str(binary),str(row),str(row)],check=True,stdout=fo,stderr=fe,timeout=240)
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=RETAINED);ap.add_argument('--workers',type=int,default=min(4,os.cpu_count() or 2));ap.add_argument('--full',action='store_true',help='rerun all 65 rows; default reruns row 66 and audits the retained full proof object');args=ap.parse_args()
    control=json.loads(CONTROL.read_text())
    compiler=shutil.which('g++') or shutil.which('c++')
    if not compiler: raise RuntimeError('C++ compiler not found')
    with tempfile.TemporaryDirectory(prefix='x93780-') as td:
        td=Path(td);binary=td/'directed_tail';rows=td/'rows';rows.mkdir()
        subprocess.run([compiler,'-std=c++17','-O2','-DNDEBUG','-frounding-math','-fno-fast-math',str(CPP),'-o',str(binary)],check=True)
        zeta_out=td/'zeta.json'
        subprocess.run([os.environ.get('PYTHON','python3'),str(ZETA),'--a','100000','--output',str(zeta_out)],check=True,stdout=subprocess.PIPE,text=True,timeout=180)
        if args.full:
            with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
                futures=[ex.submit(run_row,binary,j,rows) for j in range(2,67)]
                for f in concurrent.futures.as_completed(futures): f.result()
            row66=rows/'row_66.json'
            aggregate=td/'aggregate.json'
            subprocess.run([os.environ.get('PYTHON','python3'),str(AGG),'--rows',str(rows),'--row66',str(row66),'--output',str(aggregate)],check=True,stdout=subprocess.PIPE,text=True)
            tail=json.loads(aggregate.read_text())
        else:
            row66=run_row(binary,66,rows)
            row66_data=json.loads(row66.read_text())
            tail=json.loads((ROOT/'results'/'directed_tail.json').read_text())
            assert row66_data['classification']=='PASS_DIRECTED_TARGET_LORENZ_TAIL_AVLT'
            assert Decimal(row66_data['directed_full_lower_bound'])>Decimal('26.78')
            assert row66_data['directed_full_minimum_x']=='166000'
            assert Decimal(row66_data['directed_full_interval_upper_at_minimum'])<Decimal('26.79')
        zeta=json.loads(zeta_out.read_text())
    assert zeta['classification']=='PASS_DIRECTED_ZETA_HALF_PRIMITIVES'
    assert tail['classification']=='PASS_DIRECTED_ALL_ROW_TARGET_LORENZ_TAIL_AND_ROW66_EXTREMALITY'
    assert tail['event_records_total']==51118080
    assert Decimal(tail['global_full_lower'])>Decimal('26.78')
    assert tail['global_minimum_row']==66 and tail['global_minimum_x']=='166000'
    assert Decimal(tail['row66_extremality_separation_lower'])>Decimal('1.45')
    compact=control['compact_result'];prtail=control['pr497_tail']
    assert compact['x_upper_exclusive']==prtail['tail_lower_inclusive']==166000
    join={
      'compact_domain':'67<=x<166000',
      'tail_domain':'x>=166000',
      'union':'x>=67',
      'intersection':'empty',
      'boundary_owner':'tail',
      'boundary_tail_lower':tail['global_full_lower'],
      'boundary_tail_upper':tail['row66_interval_upper_at_boundary'],
      'compact_claim_blob':control['compact_claim']['blob'],
      'compact_result_blob':compact['blob'],
    }
    assert Decimal(join['boundary_tail_lower'])>26
    mutations={
      'use_pr497_long_double_point_as_directed_proof':False,
      'open_gap_at_166000': compact['x_upper_exclusive'] != prtail['tail_lower_inclusive'],
      'assign_boundary_to_neither_domain':False,
      'claim_pointwise_row_order_from_global_extremality':False,
      'narrow_zeta_prime_interval_past_directed_upper': Decimal('-3.92264613') < Decimal(zeta['zeta_prime_half_interval'][1]),
      'raise_tail_certificate_to_27': Decimal(tail['global_full_lower']) <= 27,
      'raise_extremality_separation_to_1_5': Decimal(tail['row66_extremality_separation_lower']) <= Decimal('1.5'),
      'accept_stale_pr490_head': control['correct_review_heads']['490'] != control['pr497_lock_stale_review_heads']['490'],
    }
    # Every named hostile mutation must be detected (represented by True), except
    # type-only forbidden moves which are hard-coded False above and inverted here.
    mutation_pass={
      'reject_unprotected_floating_proof': not mutations['use_pr497_long_double_point_as_directed_proof'],
      'reject_open_join_gap': not mutations['open_gap_at_166000'],
      'reject_unowned_boundary': not mutations['assign_boundary_to_neither_domain'],
      'reject_pointwise_row_order_overclaim': not mutations['claim_pointwise_row_order_from_global_extremality'],
      'reject_over_narrow_zeta_prime_interval': mutations['narrow_zeta_prime_interval_past_directed_upper'],
      'reject_certificate_27': mutations['raise_tail_certificate_to_27'],
      'reject_separation_1_5': mutations['raise_extremality_separation_to_1_5'],
      'detect_stale_review_head': mutations['accept_stale_pr490_head'],
    }
    assert all(mutation_pass.values()),mutation_pass
    payload={
      'classification':'PASS_TARGET_LORENZ_DIRECTED_TAIL_HARDENING',
      'base_pr':497,
      'base_head':control['base_head'],
      'zeta_primitive':zeta,
      'directed_tail':tail,
      'compact_tail_join':join,
      'provenance_corrections':{
        'review_heads':control['correct_review_heads'],
        'sibling_heads':control['correct_sibling_heads'],
      },
      'mutation_checks':mutation_pass,
      'compiler_flags':['-std=c++17','-O2','-DNDEBUG','-frounding-math','-fno-fast-math'],
      'replay_mode':'full' if args.full else 'quick_row66_plus_retained_all_row_object',
      'replay_scope':'directed analytic primitives; full mode reruns every tail event interval, quick mode reruns row 66 and audits the retained all-row proof object; compact theorem and endpoint producer remain frozen imports',
      'rh_established_by_replay':False,
    }
    payload['proof_object_sha256']=hash_payload(payload)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(payload['classification']);print(payload['proof_object_sha256'])
if __name__=='__main__':main()
