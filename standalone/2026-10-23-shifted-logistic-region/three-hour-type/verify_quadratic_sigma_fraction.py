"""Independent exact rational replay for the squared-frequency detector."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, runpy, math

BASE=Path(__file__).with_name('verify_logistic_degree12_fraction.py')
BASE_SHA='1e509ab10b892542c398f3e6110236a69ace4aca435c9cacd42a5949be7c3ae6'
if hashlib.sha256(BASE.read_bytes()).hexdigest()!=BASE_SHA:
    raise RuntimeError('degree12 helper hash mismatch')
ns=runpy.run_path(str(BASE))
I,check,exp_point,log_point,W,J,W0,AK,A1,AP,CARCH=(ns[k] for k in
    ('I','check','exp_point','log_point','W','J','W0','AK','A1','AP','CARCH'))
C=Q(9,16)
D=Q(3,50)
SCALE=1<<192


def sqrt_i(x):
    x=I.get(x)
    check(x.lo>=0,'nonnegative square-root argument')
    lo=math.isqrt((x.lo.numerator*SCALE*SCALE)//x.lo.denominator)
    hi=math.isqrt((x.hi.numerator*SCALE*SCALE)//x.hi.denominator)
    if Q(hi*hi,SCALE*SCALE)<x.hi:hi+=1
    return I(Q(lo,SCALE),Q(hi,SCALE))


def margin(A,l):
    A,l=I.get(A),I.get(l)
    eta=A/l
    u=eta/l
    a=Q(1,2)-eta+C*u
    root=sqrt_i(a*a+2*a*D*u)
    rho1=C/l+2*a*D/(l*(root+a))
    s0=1-eta+C*u
    s1=1-eta+eta*rho1
    a0=2*s0-1
    a1=2*s1-1
    z0=s0-1
    z1=eta*rho1
    z2=s1-eta
    signal=A1*W(rho1)-W(-1+C/l)
    correction=eta*W0*(A1/z2+J(z0,a0)-A1*J(z1,a1)-A1*J(z2,a1))
    error=51*eta**3*((z0+a0)**-3+A1*(z1+a1)**-3+A1*z2**-3)
    resource=W0*(A*AP/4+CARCH*eta/2)+Q(1,10**7)
    return signal+correction-error-resource+Q(157,100)*eta-90*eta**3-336*D*eta*u


def main():
    top=Q(500,2403)
    lmax=Q(83)
    check(exp_point(Q(21233,1000)*top).hi<lmax,'Littlewood endpoint')
    check(exp_point(Q(28)).hi<3*10**12,'verified height endpoint')
    check((10**10*exp_point(Q(-28))).hi<Q(1,100),'cutoff residual')
    check(top<Q(21,100),'parameter envelope')
    cutoff=[]
    for k in range(1,13):
        v=log_point(k+Q(1,100))-C
        if v.lo>0:
            gap=D*k*k-v-Q(21,100)*v*v/(2*Q(197,400)*28**2)
            check(gap.lo>0,'per-frequency cutoff')
            cutoff.append([k,str(gap.lo),str(gap.hi)])
        else:check(v.hi<0,'cutoff branch')
    check(C+12**2*D<28,'sigma upper range')
    check(top/28<Q(3,400) and 1-top/28>Q(99,100),'eta and sigma lower range')
    check(sum(k*k*AK[k] for k in range(1,13))<14,'weighted coefficients')
    primes=[2,3,5,7]
    rh=[Q(177,250),Q(289,500),Q(56,125),Q(189,500)]
    lh=[Q(1733,2500),Q(10987,10000),Q(3219,2000),Q(973,500)]
    for p,r,L in zip(primes,rh,lh):
        check(p*r*r>1 and log_point(Q(p)).hi<L,'prime loss constants')
    loss=sum(L*L*r/(1-r)**2 for r,L in zip(rh,lh))
    check(loss<16,'prime variation cost')
    check(sqrt_i(I(Q(2))).lo**2<=2<=sqrt_i(I(Q(2))).hi**2,'square-root enclosure')
    check(sqrt_i(I(Q(4))).lo==2==sqrt_i(I(Q(4))).hi,'exact square root')
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
    check(margin(I(Q(1,4)),I(lmax)).hi<0,'negative control: unsupported A')
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
    out={'status':'pass','scope':'quadratic-sigma scalar inequality and finite constants only',
         'arithmetic':'exact Fraction intervals rounded outward to 192 binary places',
         'domain':{'A':['0','500/2403'],'log_t':['28','83']},
         'sigma_choice':'1/2+sqrt(a^2+2*a*(3/50)*(eta/log_t)*k^2), a=1/2-eta+(9/16)*eta/log_t',
         'prime_variation_loss':'336*(3/50)*eta^2/log_t','cutoff_gaps':cutoff,
         'prime_variation_sum_upper':str(loss),'degree12_source_sha256':BASE_SHA,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'accepted_boxes':len(accepted),'evaluations':evaluations,
         'coverage_area_rational':str(area),'minimum_certified_lower_rational':str(minimum),
         'minimum_certified_lower_decimal':float(minimum),'negative_controls':1,'boxes':accepted}
    dest=Path(__file__).with_name('QUADRATIC_SIGMA_FRACTION_CERTIFICATE.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k not in ('boxes','cutoff_gaps')},sort_keys=True))


if __name__=='__main__':
    main()
