#!/usr/bin/env python3
import argparse,copy,hashlib,json
from decimal import Decimal as D
from pathlib import Path
from live_compiler import build,summary
HERE=Path(__file__).resolve().parent; RET=HERE/'results/live_certificate.summary.json'; TOL=D('1e-42')
class ContractError(ValueError):pass
def check(x):
    if x['schema']!='riemann.t93900.live.v2' or x['frozen_pr507']!='dfaa70cd2eefcabbf6717e3da060792904c7f357':raise ContractError('freeze')
    y=copy.deepcopy(x);dig=y.pop('proof_object_sha256');raw=json.dumps(y,sort_keys=True,separators=(',',':')).encode()
    if hashlib.sha256(raw).hexdigest()!=dig:raise ContractError('digest')
    if x['x2_separator']['k1_difference']!='2*(sqrt(2)-1)>0':raise ContractError('separator')
    occ=x['leaf']['occurrences'];ids=[r['d'] for r in occ]
    if len(occ)!=229 or len(ids)!=len(set(ids)):raise ContractError('occurrences')
    for r in occ:
        e,v,t,s=map(D,(r['equality'],r['reserve'],r['target'],r['declared_score']))
        if e<-TOL or v<-TOL or abs(t-e-2*v)>TOL or abs(s-2*e-v)>TOL:raise ContractError('channels')
        if r['child_coefficient']!='1/sqrt(67)' or r['owner']!=67:raise ContractError('child')
    if not x['normalization']['same_coefficient_both_channels'] or x['normalization']['rough_lift_parent'] or not x['normalization']['q4_after_common_ordinary']:raise ContractError('normalization')
    if len(x['rows'])!=870 or len(x['ordinary'])!=870 or len(x['detail'])!=870:raise ContractError('coverage')
    if any(D(r['total'])<-TOL or D(r['bonus'])<-TOL for r in x['rows']):raise ContractError('row')
    if any(D(r['total'])<-TOL for r in x['ordinary']):raise ContractError('ordinary')
    for r in x['detail']:
        if D(r['detail'])<-TOL or abs(D(r['detail'])-(D(r['ordinary_q'])-2*D(r['ordinary_4q'])))>TOL:raise ContractError('detail')
    if D(x['score']['surplus'])<-TOL:raise ContractError('score')
    if x['endpoint']['native_cost']!=60989 or x['endpoint']['benchmark_bridge'] or x['endpoint']['rh_proved']:raise ContractError('endpoint')
    if x.get('signed_error_source_positive') or x.get('full_child_capacity_promoted'):raise ContractError('type')
def muts(x):
    out=[]
    def a(n,f):z=copy.deepcopy(x);f(z);z0=copy.deepcopy(z);z0.pop('proof_object_sha256',None);z['proof_object_sha256']=hashlib.sha256(json.dumps(z0,sort_keys=True,separators=(',',':')).encode()).hexdigest();out.append((n,z))
    a('drop-occurrence',lambda z:z['leaf']['occurrences'].pop());a('duplicate-owner',lambda z:z['leaf']['occurrences'].append(copy.deepcopy(z['leaf']['occurrences'][0])))
    a('break-channel',lambda z:z['leaf']['occurrences'][0].__setitem__('target','0'));a('different-coefficients',lambda z:z['normalization'].__setitem__('same_coefficient_both_channels',False))
    a('rough-lift',lambda z:z['normalization'].__setitem__('rough_lift_parent',True));a('branchwise-detail',lambda z:z['detail'][0].__setitem__('detail','0'))
    a('negative-bonus',lambda z:z['rows'][0].__setitem__('bonus','-1'));a('signed-as-source',lambda z:z.__setitem__('signed_error_source_positive',True))
    a('full-child-promotion',lambda z:z.__setitem__('full_child_capacity_promoted',True));a('benchmark-bridge',lambda z:z['endpoint'].__setitem__('benchmark_bridge',True));return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,default=HERE/'results/verification.json');ap.add_argument('--mutations',action='store_true');a=ap.parse_args();x=build();check(x)
    if summary(x)!=json.loads(RET.read_text()):raise ContractError('retained summary')
    rejected=[]
    if a.mutations:
        for n,z in muts(x):
            try:check(z)
            except ContractError:rejected.append(n)
            else:raise ContractError('accepted '+n)
    o={'classification':'PASS_LIVE_NATIVE_SOURCE_TO_PHYSICAL_ROW_COMPILER','proof_object_sha256':x['proof_object_sha256'],'occurrences':229,'rows':870,'ordinary':870,'detail':870,'mutations_rejected':rejected,'native_deficit_bound':60989,'rh_established':False}
    o['verification_sha256']=hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest();a.output.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n');print(o['classification']);print(o['verification_sha256'])
if __name__=='__main__':main()
