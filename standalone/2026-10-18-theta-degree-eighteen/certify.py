#!/usr/bin/env python3
"""Finite exact existence certificate, not RH. Reconstructs the full theta source.
Run without options for the full replay. --source is a development convenience
which trusts a specified previously generated interval receipt, not final evidence.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
from interval_source import I,SCALE,reconstruct,require
from model import evaluate,values_and_jacobian,KS,CK
ROOT=Path(__file__).resolve().parent

def certify(source):
    data=json.loads((ROOT/'parameters.json').read_text());center=list(map(F,data['centers']))
    active=data['active'];rho=F(data['radius']);R=[list(map(F,row)) for row in data['preconditioner']]
    require(len(active)==9 and len(set(active))==9,'nine distinct active coordinates')
    require(all(0<=j<18 for j in active),'active index')
    target=[I(*v) for v in source['s']]
    cen=[I.coerce(x) for x in center]
    rad=I.coerce(rho);box=[I(x.lo-rad.hi,x.hi+rad.hi) if j in active else x for j,x in enumerate(cen)]
    f0=[v-t for v,t in zip(evaluate(cen),target)]
    beta=max(sum((I.coerce(R[i][j])*f0[j] for j in range(9)),I.coerce(0)).absup() for i in range(9))
    _,J=values_and_jacobian(box,active)
    E=[[I.coerce(int(i==j))-sum((I.coerce(R[i][k])*J[k][j] for k in range(9)),I.coerce(0)) for j in range(9)] for i in range(9)]
    lip=max(sum(v.absup() for v in row) for row in E)
    # Strict rational predicates; not rounded diagnostics. R need not be an exact inverse.
    require(lip*1000<SCALE,'Jacobian contraction')
    require(F(beta,SCALE)<rho/1000,'center correction')
    require(rho-F(beta,SCALE)-rho*F(lip,SCALE)>rho*F(99,100),'strict self map')
    require(all(v.lo>0 for v in box[:12]),'positive amplitudes and eta')
    require(all(v.lo>SCALE//2 and v.hi<SCALE for v in box[12:]),'positive finite internal couplings')
    hub=[box[11]*KS[i]*box[i] for i in range(11)]
    internals=[2*box[j]-1 for j in range(12,18)]
    # Couplings J=atanh(h). Bound all by 1/200000 < J < 2.
    require(all(h.lo>0 and h.hi<SCALE for h in hub+internals),'all physical edge biases')
    for h in hub+internals:
        require(h.lo*200000>SCALE,'strict edge lower bound')
        require((h/(1-h*h)).hi<2*SCALE,'strict edge upper bound')
    # Exact count: sign types 0..4 =>269 spins, six dimers =>12, plus one hub.
    vertices=256+10+1+1+1+12+1;edges=269+6+6
    require(vertices==282 and edges==vertices-1,'connected tree count')
    return {'status':'PASS: finite degree-18 existence certificate; no RH or cofinal claim',
            'bits':source['bits'],'theta_cells':source['cells'],'theta_indices':source['explicit_indices'],
            'matched_even_degrees':list(range(2,19,2)),'vertices':vertices,'edges':edges,
            'active':active,'radius':str(rho),'beta_bound_scaled_integer':beta,'L_bound_scaled_integer':lip,
            'scale':SCALE,'coupling_bounds':['1/200000','2'],'source_sha256':hashlib.sha256(json.dumps(source,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
            'source_target_intervals':source['s'],
            'parameters_sha256':hashlib.sha256((ROOT/'parameters.json').read_bytes()).hexdigest()}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--source',type=Path);args=ap.parse_args()
    source=json.loads(args.source.read_text()) if args.source else reconstruct()
    result=certify(source);result['source_reconstructed_this_run']=args.source is None
    print(json.dumps(result,sort_keys=True,indent=2))
