"""Exact finite ideal tail counterterm and local Euler checks; not an analytic moment test."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import json,hashlib
from verify import hnf_ideals,norm,subset,hnf_mobius,prime_ideals

def req(v,m):
    if not v:raise ArithmeticError(m)

def V(x):
    if x<=1:return F(1)
    if x>=2:return F(0)
    t=x-1
    return 1-10*t**3+15*t**4-6*t**5

def W(x):return (x-2)**4*(3-x)**4 if 2<x<3 else F(0)

def main():
    cap=384;ideals=[a for a in hnf_ideals(cap) if gcd(norm(a),6)==1]
    primes=prime_ideals(cap);mu={a:hnf_mobius(a,primes) for a in ideals}
    v={}
    for a in ideals:
        z=F(1)
        for p in primes:
            if subset(a,p):
                q=norm(p);z*=F(q*q,q*q+q-1)
        v[a]=z
    records=[];gates=0;mutations=0
    for D in [32,64,128]:
        outer=[a for a in ideals if norm(a)<=3*D]
        A=sum((mu[a]*V(F(norm(a),D))*v[a]/norm(a) for a in outer),F(0))
        B=sum((mu[a]**2*W(F(norm(a),D))/norm(a) for a in outer),F(0))
        req(B>0 and A!=0,'nondegenerate complete tail response')
        c=-A/B
        coeff={a:mu[a]*V(F(norm(a),D))+c*mu[a]**2/v[a]*W(F(norm(a),D)) for a in outer}
        response=sum((coeff[a]*v[a]/norm(a) for a in outer),F(0))
        req(response==0,'exact nuisance response not zero')
        for n in ideals:
            if norm(n)>D:continue
            req(coeff[n]==mu[n],'low prefix changed')
            conv=sum((coeff[a] for a in outer if subset(n,a)),F(0))
            req(conv==(1 if norm(n)==1 else 0),'complete ideal unit gate failed');gates+=1
        wrong=sum(((mu[a]*V(F(norm(a),D))+c*mu[a]**2*W(F(norm(a),D)))*v[a]/norm(a) for a in outer),F(0))
        req(wrong!=0,'missing inverse-v mutation not detected');mutations+=1
        records.append({'D':D,'outer_ideals':len(outer),'A':str(A),'B':str(B),'c':str(c),
                        'exact_response':str(response),'wrong_inverse_v_response':str(wrong)})
    # Formal prime-power coefficient identity F=(1-X)^-1(1-X²)R,
    # including powers beyond squarefree support.
    euler=0
    for q in [5,7,13,19,25,31,37,43,49,61,67,73,79,97]:
        w=1+F(1,q)-F(1,q*q)
        R=[F(1)]+[(w-1)*(-1)**(j-1) for j in range(1,17)]
        plain_square=[F(1),F(1)]+[F(0)]*15
        for j in range(17):
            got=sum(plain_square[k]*R[j-k] for k in range(j+1))
            req(got==(1 if j==0 else w if j==1 else 0),'local Euler convolution');euler+=1
    out={'status':'PASS','scope':'Finite exact ideal/response/Euler algebra only; analytic norms use stated source inputs.',
         'complete_ideal_cap':cap,'complete_exterior_ideals':len(ideals),
         'low_product_unit_gates':gates,'inverse_v_mutations_rejected':mutations,
         'local_prime_power_checks':euler,'records':records,
         'profile_note':'Finite rational C2/C3 fixtures; analytic theorem uses smooth cutoffs with the same support/prefix properties.'}
    digest=hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest();out['records_sha256']=digest
    Path(__file__).with_name('TAIL_MOLLIFIER_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))

if __name__=='__main__':main()
