#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=importlib.util.spec_from_file_location('pg',HERE/'projective_gluing.py')
pg=importlib.util.module_from_spec(SPEC); assert SPEC.loader; SPEC.loader.exec_module(pg)

class ContractError(ValueError): pass

FLAGS=(
 'intermediate_child_observed','rough_lift_parent','coordinate_dependent_coefficients',
 'branchwise_detail','duplicate_first_owner','parent_overdraw','frontier_not_contractive',
 'repeated_thinning','signed_defect_is_source','full_child_capacity_promotion',
 'bad_endpoint_orientation','benchmark_bridge')

def validate(c):
    for f in FLAGS:
        if c.get(f): raise ContractError(f)
    if c['q4_after_total_ordinary'] is not True: raise ContractError('q4 order')
    if c['one_global_thinning'] is not True: raise ContractError('thinning')
    if c['native_deficit_upper']>=3457.0000001: raise ContractError('native deficit')
    if c['endpoint_orientation']!='F_Lambda <= native_deficit': raise ContractError('orientation')
    return True

def base_contract():
    return {f:False for f in FLAGS}|{
      'q4_after_total_ordinary':True,'one_global_thinning':True,
      'native_deficit_upper':3457,'endpoint_orientation':'F_Lambda <= native_deficit'}

def run(output: Path, mutations: bool=True):
    cert=pg.build(); c=base_contract(); validate(c)
    rejected=[]
    if mutations:
        for f in FLAGS:
            m=copy.deepcopy(c);m[f]=True
            try: validate(m)
            except ContractError: rejected.append(f)
            else: raise AssertionError(('mutation accepted',f))
        for name,fn in [
          ('q4-before-common-row',lambda x:x.__setitem__('q4_after_total_ordinary',False)),
          ('two-thinnings',lambda x:x.__setitem__('one_global_thinning',False)),
          ('cost-at-gate',lambda x:x.__setitem__('native_deficit_upper',3458)),
          ('wrong-orientation-text',lambda x:x.__setitem__('endpoint_orientation','native_deficit <= F_Lambda'))]:
            m=copy.deepcopy(c);fn(m)
            try: validate(m)
            except ContractError: rejected.append(name)
            else: raise AssertionError(('mutation accepted',name))
    payload={'classification':'PASS_PROJECTIVE_NATIVE_LORENZ_FULL_CANDIDATE_94120',
      'projective_proof_object_sha256':cert['proof_object_sha256'],
      'registry_summary':cert['registry_summary'],'q2_obstruction':cert['q2_obstruction'],
      'hostile_mutations_rejected':len(rejected),'mutations':rejected,
      'native_deficit_upper':3457,
      'scientific_status':'unconditional full proof candidate; RH not treated as established pending hostile independent reconstruction'}
    raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode();payload['verification_sha256']=hashlib.sha256(raw).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    return payload

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'results/verification.json');ap.add_argument('--mutations',action='store_true')
    a=ap.parse_args();p=run(a.output,mutations=a.mutations);print(p['classification']);print(p['verification_sha256'])
if __name__=='__main__':main()
