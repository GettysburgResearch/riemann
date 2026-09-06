#!/usr/bin/env python3
"""Bounded delivery consistency and historical replay; not scientific acceptance."""
from __future__ import annotations
import argparse
import copy
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
FRONT = ('README.md','VALIDATION.md','RELEASE_BLOCKERS.md','STRUCTURE_AND_EXTRACTION.md')
MANIFEST = 'pass3/FILE_MANIFEST.tsv'
EXPECTED = set(FRONT) | {
    'pass3/'+name for name in ('RETRY_REPORT.md','FORMAL_REPAIR_CONTRACT.md',
        'OWNER_RELEASE_GATES.md','COVERAGE.tsv')
} | {'pass3/evidence/PRE_RETRY_'+name for name in FRONT} | {
    'pass3/references/'+name for name in ('verify_X105560.py',
        'sixhour_complete_source_closure.py','live_quotient_centered_current_majorant.py')
} | {'pass3/scripts/'+name for name in ('replay_record_arithmetic.py',
        'replay_manifest_contract.py','replay_majorant.py','validate_retry.py')
} | {'pass3/reports/'+name for name in ('record_arithmetic_replay.json',
        'manifest_contract.json','majorant_replay.json','connector_observations.json')}


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def strict(raw: bytes):
    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, 'duplicate JSON key')
            out[key] = value
        return out
    def reject(_):
        raise ValueError('noninteger JSON number')
    return json.loads(raw,object_pairs_hook=pairs,parse_float=reject,parse_constant=reject)


def validate(data: dict[str,bytes]) -> dict:
    rows = list(csv.DictReader(io.StringIO(data[MANIFEST].decode()),delimiter='\t'))
    need(len(rows) == len(EXPECTED) and {r['path'] for r in rows} == EXPECTED,
         'fixed delivery denominator changed')
    for row in rows:
        raw = data[row['path']]
        need(str(len(raw)) == row['bytes'] and sha(raw) == row['sha256'], 'content seal mismatch')
    record = strict(data['pass3/reports/record_arithmetic_replay.json'])
    need(record['actual_loop_counts'] == [1640,2592], 'record loop census')
    need(record['ordinary_optimized_identical'] is True, 'record mode comparison')
    need(record['exact_decimal_lower'] == '0.673008527927779' and
         record['exact_decimal_upper'] == '0.673008527927780', 'scalar bracket changed')
    scope_keys = {'RH_proved','analytic_seven_gap_deduction_reviewed',
                  'external_Arb_certificate_executed','full_sixteen_file_payload_executed',
                  'new_zero_proportion_proved'}
    need(type(record['scope']) is dict and set(record['scope']) == scope_keys,
         'record scope denominator changed')
    need(all(record['scope'][key] is False for key in scope_keys), 'unperformed record scope promoted')
    manifest = strict(data['pass3/reports/manifest_contract.json'])
    need(type(manifest['fixture_cases']) is int and manifest['fixture_cases'] == 11 and
         manifest['cli_mode_runs'] == 22 and manifest['roundtrip_mode_runs'] == 10,
         'manifest fixture census')
    need(manifest['actual_scientific_graph_replayed'] is False and
         manifest['earlier_expected_count_regressions_refuted'] is False and
         manifest['RH_proved'] is False, 'manifest scope promoted')
    majorant = strict(data['pass3/reports/majorant_replay.json'])
    need(type(majorant['finite_currents']) is int and majorant['finite_currents'] == 1539,
         'majorant finite census')
    need(majorant['retained_json_git_blob'] == '7bef7e8cf814920d81603aee7654d5ae3da8bc47',
         'majorant source/output identity')
    for key in ('historical_source_blob_function_executed','complete_native_fibre_replayed',
                'all_conductor_estimate_proved','RH_proved'):
        need(majorant[key] is False, 'majorant scope promoted')
    obs = strict(data['pass3/reports/connector_observations.json'])
    need(obs['observed_C_head'] == 'cd8a172c24aaf61fd293b32c5a396334110f0565' and
         obs['settings_mutated'] is False, 'publication observation changed')
    return {'manifest_entries':len(rows),'new_driver_reports':3,'scientific_acceptance':False}


def reseal(data: dict[str,bytes], path: str) -> None:
    rows = list(csv.DictReader(io.StringIO(data[MANIFEST].decode()),delimiter='\t'))
    for row in rows:
        if row['path'] == path:
            row['bytes'] = str(len(data[path])); row['sha256'] = sha(data[path])
    out = io.StringIO(); w = csv.DictWriter(out,fieldnames=['path','bytes','sha256'],delimiter='\t',lineterminator='\n')
    w.writeheader(); w.writerows(rows); data[MANIFEST] = out.getvalue().encode()


def negative_tests(original: dict[str,bytes]) -> list[str]:
    passed = []
    names = ('missing_file','wrong_bytes','empty_manifest','duplicate_path','record_scope',
             'record_count','majorant_scope','boolean_count','wrong_bracket','empty_scope','missing_scope_field')
    for name in names:
        data = dict(original)
        path = 'pass3/reports/record_arithmetic_replay.json'
        if name == 'missing_file':
            data.pop(path)
        elif name == 'wrong_bytes':
            data[path] += b' '
        elif name == 'empty_manifest':
            data[MANIFEST] = b'path\tbytes\tsha256\n'
        elif name == 'duplicate_path':
            data[MANIFEST] += data[MANIFEST].splitlines(keepends=True)[1]
        else:
            if name in ('majorant_scope','boolean_count'):
                path = 'pass3/reports/majorant_replay.json'
            obj = strict(data[path])
            if name == 'record_scope': obj['scope']['RH_proved'] = True
            elif name == 'record_count': obj['actual_loop_counts'] = [1601,2527]
            elif name == 'majorant_scope': obj['complete_native_fibre_replayed'] = True
            elif name == 'boolean_count': obj['finite_currents'] = True
            elif name == 'wrong_bracket': obj['exact_decimal_lower'] = '1.17'
            elif name == 'empty_scope': obj['scope'] = {}
            elif name == 'missing_scope_field': obj['scope'].pop('external_Arb_certificate_executed')
            data[path] = (json.dumps(obj,sort_keys=True,indent=2)+'\n').encode()
            reseal(data,path)
        try:
            validate(data)
        except (ValueError,KeyError):
            passed.append(name)
        else:
            raise ValueError('corruption accepted: '+name)
    return passed


def historical() -> dict:
    results = []
    with tempfile.TemporaryDirectory(prefix='C3-historical-') as d:
        target = Path(d)/'reviews'/'C'
        shutil.copytree(ROOT,target,ignore=shutil.ignore_patterns('__pycache__'))
        for name in FRONT:
            shutil.copyfile(target/'pass3'/'evidence'/('PRE_RETRY_'+name),target/name)
        for script in ('check_census.py','pass2/scripts/validate_pass2.py'):
            pair = []
            for optimized in (False,True):
                command = [sys.executable,'-I','-S','-B']+(['-O'] if optimized else [])+[str(target/script)]
                result = subprocess.run(command,cwd=d,env={'PATH':os.defpath,'LANG':'C.UTF-8'},
                                        text=True,capture_output=True,timeout=30)
                need(result.returncode == 0, 'historical consistency replay failed: '+result.stderr[-800:])
                pair.append(result.stdout)
            need(pair[0] == pair[1], 'historical output mode mismatch')
            results.append({'script':script,'modes':['normal','optimized'],'stdout_sha256':sha(pair[0].encode())})
    return {'runs':4,'four_front_doors_restored_in_temporary_copy':True,'results':results,
            'fresh_340_head_fetch':False,'complete_scientific_replay':False}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('--output',type=Path)
    args = ap.parse_args()
    data = {path:(ROOT/path).read_bytes() for path in EXPECTED | {MANIFEST}}
    result = {'schema':'C3-delivery-consistency-v1','status':'PASS_BOUNDED_DELIVERY',
              **validate(data),'negative_fixtures_rejected':negative_tests(data),'historical':historical(),
              'fresh_Lean_build':False,'exhaustive_C_allotment_complete':False,'public_release_cleared':False}
    text = json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text,encoding='utf-8')
    else: print(text,end='')


if __name__ == '__main__': main()
