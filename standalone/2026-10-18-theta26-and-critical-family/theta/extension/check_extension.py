#!/usr/bin/env python3
"""Exact rational checks for the variance barrier and full cycle-moment engine.

This is not a finite theta-matching root certificate.  It independently
enumerates every configuration of a seven-spin specialization to validate the
complete edge/triangle moment construction through degree26.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import argparse
from explore_added_edge import evaluate as one_edge
from triangle_model import evaluate as triangle

ROOT=Path(__file__).resolve().parent

def require(condition,message):
    if not condition:raise ValueError(message)

def enumerate_moments(z,ts,degree=26):
    blocks=(3,6,8);eta=F(1,10**10);total=F(0);mom=[F(0)]*(degree+1)
    for sig in product((-1,1),repeat=7):
        hub=sig[0];root=[sig[1],sig[3],sig[5]];leaf=[sig[2],sig[4],sig[6]]
        mass=F(1);y=F(0)
        for j,i in enumerate(blocks):
            A,B,p=z[3*i:3*i+3]
            y+=(A+B)*root[j]/2+(A-B)*leaf[j]/2
            mass*=(1+eta*hub*root[j])*(1+(2*p-1)*root[j]*leaf[j])
        for t,(a,b) in zip(ts,((0,1),(0,2),(1,2))):mass*=1+t*root[a]*root[b]
        total+=mass
        for n in range(degree+1):mom[n]+=mass*y**n
    return [m/total for m in mom]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-json',type=Path,default=ROOT.parent/'theta26_source.json')
    parser.add_argument('--output',type=Path,default=ROOT/'extension_certificate.json')
    args=parser.parse_args()
    source_path=args.source_json;source_bytes=source_path.read_bytes()
    require(hashlib.sha256(source_bytes).hexdigest()==
            'c171903e4f60c189a929ccfcce36f7db034508e9ca10c85ed766338625558dcf',
            'frozen directed theta26 source identity')
    source=json.loads(source_bytes);variance_upper=F(source['variance'][1],1<<source['bits'])
    r=F(4633,100000);u=F(4621,100000)
    require(variance_upper<u,'theta variance upper bound')
    gap=r-r*r/18-u;require(gap>0,'strict rational variance barrier')
    require(gap*18*10**10==135311,'displayed rational numerator')

    z=[F(0)]*48
    for i in range(16):z[3*i+2]=F(3,4)
    for i,A,B,p in ((3,F(2,5),F(1,10),F(4,5)),
                      (6,F(1,3),F(-1,9),F(2,3)),
                      (8,F(3,7),F(1,14),F(7,9))):
        z[3*i:3*i+3]=[A,B,p]
    cases=[(F(0),F(0),F(0)),(F(0),F(1,3),F(0)),
           (F(1,4),F(1,3),F(0)),(F(1,4),F(1,3),F(1,5))]
    checks=[]
    for ts in cases:
        _,poly=triangle(z,ts,26);direct=enumerate_moments(z,ts,26)
        require(poly==direct,'complete triangle moments match full enumeration')
        checks.append({'edge_correlations':[str(t) for t in ts],
                       'all_moments_0_through_26_equal':True})
    _,poly=one_edge(z,F(1,3),26,left=3,right=8)
    require(poly==enumerate_moments(z,(F(0),F(1,3),F(0)),26),
            'one-edge specialization matches full enumeration')

    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            for name in ('PROOF_EXTENSION.md','triangle_model.py','explore_added_edge.py','exact_polynomial.py',
                         'check_extension.py')}
    result={'schema':'theta_graph_extension.exact_checks.v1',
            'status':'EXACT_RATIONAL_IDENTITIES_CHECKED_NOT_A_THETA_ROOT_CERTIFICATE',
            'rational_variance_barrier':str(r),'barrier_gap_above_theta_upper_bound':str(r-r*r/18-variance_upper),
            'displayed_rational_gap':str(gap),'enumerated_spins':7,'configurations_per_case':128,
            'verified_degree':26,'checks':checks,'files_sha256':hashes,
            'theta26_source_sha256':hashlib.sha256(source_bytes).hexdigest()}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('EXACT_EXTENSION_CHECKS_PASSED',flush=True)

if __name__=='__main__':main()
