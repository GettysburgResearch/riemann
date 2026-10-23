"""Independent Fraction replay of the degree12 R=4.815 scalar inequality.

The frozen baseline supplies exact outward-rounded arithmetic and independently
derived kernel moments. Every acceptance decision below is rational.
The analytic, prime-side and global zero-free interfaces are separate inputs.
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
I,check,exp_point,exp_i,log_point,log_i,W,J,W0=(ns[k] for k in
    ('I','check','exp_point','exp_i','log_point','log_i','W','J','W0'))
C=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
   -38436761903,-16088159026,168141762350,447056663730,616860378424,
   541372347258,298691298328,83048065550]
EXTRA=10**14
NORM=sum(c*c for c in C)+13*EXTRA
AK=[Q(sum(C[j]*C[j+k] for j in range(13-k))+EXTRA*(13-k),NORM)
    *(1 if k==0 else 2) for k in range(13)]
A1=AK[1]
AP=sum(AK[1:])
CARCH=Q(-300317,100000)


def margin(A,l):
    A,l=I.get(A),I.get(l)
    c=log_i(12+10**10*exp_i(-l))
    mu=I(l.lo/(l.lo+c.hi),l.hi/(l.hi+c.lo))
    eta=A/l
    sigma=1-A/(l+c)
    a=2*sigma-1
    z0=sigma-1
    z1=z0+eta
    z2=sigma-eta
    signal=A1*W(1-mu)-W(-mu)
    correction=eta*W0*(A1/z2+J(z0,a)-A1*J(z1,a)-A1*J(z2,a))
    error=51*eta**3*(1/(z0+a)**3+A1/(z1+a)**3+A1/z2**3)
    resource=W0*(A*AP/4+CARCH*eta/2)+Q(1,10**7)
    return signal+correction-error-resource+Q(157,100)*eta-90*eta**3


def main():
    top=Q(200,963)
    lmax=Q(823,10)
    check(NORM==1000000001299439064580929 and AK[0]==1,'normalization')
    check(min(AK)>0 and A1>1 and AP<4,'coefficient signs and sizes')
    check(top/28<Q(3,400),'eta domain')
    check((1-I(top)/(28+log_point(Q(12)))).lo>Q(99,100),'sigma domain')
    check(exp_point(Q(21233,1000)*top).hi<lmax,'Littlewood endpoint')
    check(exp_point(Q(28)).hi<3*10**12,'verified height endpoint')
    pending=[(Q(0),top,Q(28),lmax,0)]
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
        if depth>=40:
            raise RuntimeError('unresolved rectangle '+str((al,ah,ll,lh,value.lo,value.hi)))
        if depth%2==0:
            m=(ll+lh)/2
            pending.extend([(al,ah,ll,m,depth+1),(al,ah,m,lh,depth+1)])
        else:
            m=(al+ah)/2
            pending.extend([(al,m,ll,lh,depth+1),(m,ah,ll,lh,depth+1)])
    check(margin(I(Q(1,4)),I(lmax)).hi<0,'negative control: overlarge A')
    area=Q(0)
    for i,row in enumerate(accepted):
        al,ah=map(Q,row['A'])
        ll,lh=map(Q,row['log_t'])
        check(0<=al<ah<=top and 28<=ll<lh<=lmax,'box containment')
        area+=(ah-al)*(lh-ll)
        for old in accepted[:i]:
            bl,bh=map(Q,old['A'])
            ml,mh=map(Q,old['log_t'])
            check(not(max(al,bl)<min(ah,bh) and max(ll,ml)<min(lh,mh)),
                  'overlapping box interiors')
    check(area==top*(lmax-28),'exact area coverage')
    minimum=min(Q(row['margin_lower']) for row in accepted)
    out={'status':'pass','scope':'degree12 scalar logistic inequality only',
         'arithmetic':'exact Fraction intervals rounded outward to 192 binary places',
         'domain':{'A':['0','200/963'],'log_t':['28','823/10']},
         'degree':12,'integer_coefficients':C,'auxiliary_square_weight':EXTRA,
         'normalization':str(NORM),'cosine_coefficients':[str(x) for x in AK],
         'kernel_second_derivative_upper':51,'Carch_upper':str(CARCH),
         'prime_lower':'(126/100)*eta-90*eta^3','archimedean_upper':'-(31/100)*eta',
         'baseline_source_sha256':BASE_SHA,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'accepted_boxes':len(accepted),'evaluations':evaluations,
         'coverage_area_rational':str(area),'minimum_certified_lower_rational':str(minimum),
         'minimum_certified_lower_decimal':float(minimum),'negative_controls':1,'boxes':accepted}
    dest=Path(__file__).with_name('LOGISTIC_DEGREE12_FRACTION_CERTIFICATE.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in
          ('boxes','cosine_coefficients','integer_coefficients')},sort_keys=True))


if __name__=='__main__':
    main()
