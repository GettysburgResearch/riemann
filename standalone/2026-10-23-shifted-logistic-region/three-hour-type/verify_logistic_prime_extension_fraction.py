"""Exact Fraction replay of the separately proposed prime/arch extension.

The frozen baseline engine is SHA-pinned. Prime-side and archimedean
inequalities are separate analytic inputs, not consequences of this program.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import runpy

BASE=Path(__file__).with_name('verify_logistic_master_fraction.py')
BASE_SHA='cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413'
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=BASE_SHA:
    raise RuntimeError('baseline source hash mismatch')
ns=runpy.run_path(str(BASE))
I,check,base_margin,exp_point,log_point=(ns[k] for k in ('I','check','margin','exp_point','log_point'))


def margin(A,l):
    A,l=I.get(A),I.get(l)
    eta=A/l
    return base_margin(A,l)+Q(14547,10000)*eta-2775*eta**3


def main():
    top=Q(50,241)
    check(top/28<Q(3,400),'eta domain')
    check((1-I(top)/(28+log_point(Q(16)))).lo>Q(99,100),'sigma domain')
    check(exp_point(Q(21233,1000)*top).hi<82,'Littlewood endpoint')
    check(exp_point(Q(28)).hi<3*10**12,'verified height endpoint')
    pending=[(Q(0),top,Q(28),Q(82),0)]
    accepted=[]
    evaluations=0
    while pending:
        al,ah,ll,lh,depth=pending.pop()
        value=margin(I(al,ah),I(ll,lh))
        evaluations+=1
        if value.lo>0:
            accepted.append({'A':[str(al),str(ah)],'log_t':[str(ll),str(lh)],
                             'margin_lower':str(value.lo),'margin_upper':str(value.hi)})
            continue
        if depth>=36:
            raise RuntimeError('unresolved rectangle '+str((al,ah,ll,lh,value.lo,value.hi)))
        if depth%2==0:
            m=(ll+lh)/2
            pending.extend([(al,ah,ll,m,depth+1),(al,ah,m,lh,depth+1)])
        else:
            m=(al+ah)/2
            pending.extend([(al,m,ll,lh,depth+1),(m,ah,ll,lh,depth+1)])
    bad=margin(I(Q(1,4)),I(Q(82)))
    check(bad.hi<0,'negative control: overlarge A')
    area=Q(0)
    for i,row in enumerate(accepted):
        al,ah=map(Q,row['A'])
        ll,lh=map(Q,row['log_t'])
        check(0<=al<ah<=top and 28<=ll<lh<=82,'box containment')
        area+=(ah-al)*(lh-ll)
        for old in accepted[:i]:
            bl,bh=map(Q,old['A'])
            ml,mh=map(Q,old['log_t'])
            check(not(max(al,bl)<min(ah,bh) and max(ll,ml)<min(lh,mh)),
                  'overlapping box interiors')
    check(area==top*54,'exact area coverage')
    minimum=min(Q(row['margin_lower']) for row in accepted)
    out={'status':'pass','scope':'prime/arch extended scalar logistic inequality only',
         'arithmetic':'exact Fraction intervals rounded outward to 192 binary places',
         'domain':{'A':['0','50/241'],'log_t':['28','82']},
         'added_margin':'(14547/10000)*eta-2775*eta^3',
         'baseline_source_sha256':BASE_SHA,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'accepted_boxes':len(accepted),'evaluations':evaluations,
         'coverage_area_rational':str(area),'minimum_certified_lower_rational':str(minimum),
         'minimum_certified_lower_decimal':float(minimum),'negative_controls':1,'boxes':accepted}
    dest=Path(__file__).with_name('LOGISTIC_PRIME_FRACTION_CERTIFICATE.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='boxes'},sort_keys=True))


if __name__=='__main__':
    main()
