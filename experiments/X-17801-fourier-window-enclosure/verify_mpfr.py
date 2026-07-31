#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from decimal import Decimal, getcontext
from pathlib import Path
getcontext().prec=120

def D(x: object) -> Decimal:
    if isinstance(x, bool): raise TypeError('boolean is not a decimal')
    if isinstance(x, (int, str)): return Decimal(x)
    raise TypeError(type(x))

def main(path: str) -> int:
    d=json.loads(Path(path).read_text())
    if d['schema']!='riemann.x17802-independent-mpfr-replay.v1': raise ValueError('schema')
    if d['classification']!='DIRECTED_ENGINEERING_PROTOTYPE_INDEPENDENT_BACKEND': raise ValueError('classification')
    if d['precision_bits']!=256 or d['prime_power_terms']!=64542: raise ValueError('parameters')
    rs=sorted(d['runs'],key=lambda r:r['grid_power'])
    if [r['grid_power'] for r in rs] != [16,18,20]: raise ValueError('grid ladder')
    ints=[]
    for r in rs:
        lo,c,hi,rad=map(D,(r['prime_lower'],r['prime_center'],r['prime_upper'],r['prime_radius']))
        if not lo <= c <= hi: raise ValueError('interval order')
        if abs((c-rad)-lo)>=D('1e-59') or abs(hi-(c+rad))>=D('1e-59'): raise ValueError('printed radius mismatch')
        ints.append((lo,hi))
    for outer,inner in zip(ints,ints[1:]):
        if not outer[0] <= inner[0] <= inner[1] <= outer[1]: raise ValueError('precision nesting')
    blo,bhi=D(d['binary128_grid20_lower']),D(d['binary128_grid20_upper'])
    overlap=(max(ints[-1][0],blo),min(ints[-1][1],bhi))
    if overlap[0]>overlap[1]: raise ValueError('independent backends do not overlap')
    old=D(d['old_linear_midpoint'])
    if ints[0][0] <= old <= ints[0][1]: raise ValueError('old signal not refuted')
    model=D(d['ordinary_zero_plus_trivial_model'])
    if not ints[-1][0] <= model <= ints[-1][1]: raise ValueError('planning model outside')
    result={'schema':'riemann.x17802-independent-mpfr-verification.v1','verdict':'INDEPENDENT_MPFR_BACKEND_CONFIRMS_INTERPOLATION_ARTIFACT','rh_verdict':'NO_RH_BOUND_VIOLATION_CERTIFIED','grid20_interval':{'lower':str(ints[-1][0]),'upper':str(ints[-1][1])},'grid20_cross_backend_overlap':{'lower':str(overlap[0]),'upper':str(overlap[1])},'old_midpoint_lower_separation':str(old-ints[-1][1]),'zero_model_inside_grid20':True}
    canonical=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    result['exact_proof_object_sha256']=hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result,indent=2,sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main(sys.argv[1]))
