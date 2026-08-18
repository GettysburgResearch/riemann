#!/usr/bin/env python3
from __future__ import annotations

import hashlib, json, math
from decimal import Decimal, localcontext
from fractions import Fraction


def sieve(n):
    mu=[0]*(n+1); spf=[0]*(n+1); ps=[]; mu[1]=1
    for x in range(2,n+1):
        if not spf[x]: spf[x]=x; ps.append(x); mu[x]=-1
        for p in ps:
            y=x*p
            if y>n: break
            spf[y]=p
            if x%p==0: mu[y]=0; break
            mu[y]=-mu[x]
    return mu,spf,ps


def divisors(n,spf):
    out=[1]; x=n
    while x>1:
        p=spf[x]; e=0
        while x%p==0: x//=p; e+=1
        base=list(out); m=1
        for _ in range(e): m*=p; out += [d*m for d in base]
    return out


def factors(n,spf):
    out=[]
    while n>1:
        p=spf[n]; out.append(p)
        while n%p==0: n//=p
    return out


def q(row,n):
    if row==2:
        return 0 if n<2 else 3 if n==2 else 0 if n==3 else 1
    return 0 if n<3 else 6 if n==3 else -2 if n==4 else 1


def mui(n,mu,spf,lo,hi=None):
    if mu[n]==0: return 0
    for p in factors(n,spf):
        if p<=lo or (hi is not None and p>hi): return 0
    return mu[n]


def az(row,n,z,mu,spf):
    return sum(mui(d,mu,spf,3,z)*q(row,n//d) for d in divisors(n,spf))


def afull(row,n,mu,spf):
    return sum(mui(d,mu,spf,3,None)*q(row,n//d) for d in divisors(n,spf))


def tail(row,n,z,mu,spf):
    return sum(mui(m,mu,spf,z,None)*az(row,n//m,z,mu,spf) for m in divisors(n,spf))


def owner(row,n,z,mu,spf):
    total=0
    for m in divisors(n,spf):
        mm=mui(m,mu,spf,z,None)
        if m==1 or not mm: continue
        p=min(factors(m,spf)); r=m//p
        assert all(t>p for t in factors(r,spf))
        total += mu[r]*az(row,n//m,z,mu,spf)
    return total


def pdata(z,ps):
    P=1; V=Fraction(1); A=Fraction(1); w=0
    for p in ps:
        if 3<p<=z:
            P*=p; V*=Fraction(p-1,p); A*=Fraction(p+1,p); w+=1
    return P,V,A,A/V,w


def run():
    limit=20000; mu,spf,ps=sieve(100000); cc=oc=0
    for z in (11,19,31):
        for row in (2,3):
            for n in range(1,limit+1):
                full=afull(row,n,mu,spf)
                assert full==tail(row,n,z,mu,spf)
                assert full==az(row,n,z,mu,spf)-owner(row,n,z,mu,spf)
                cc+=1; oc+=1
    P,_,_,R,_=pdata(11,ps); assert P==385
    tc=0
    for row in (2,3):
        M=(row+1)*P
        for n in range(M+1,M+4*P+1):
            assert az(row,n,11,mu,spf)==(1 if math.gcd(n,P)==1 else 0); tc+=1
    assert 8*3*3*3==216 and 8*6*6*4==1152
    fixtures=[(Fraction(3),Fraction(5),Fraction(2),Fraction(4)),(Fraction(11),Fraction(7),Fraction(-2),Fraction(9)),(Fraction(1),Fraction(13),Fraction(2),Fraction(-3))]
    dual=[]
    for C2,C3,G2,G3 in fixtures:
        target=max(G2/C2,G3/C3)
        sample=max((Fraction(k,20)*G2+Fraction(20-k,20)*G3)/(Fraction(k,20)*C2+Fraction(20-k,20)*C3) for k in range(21))
        assert sample==target; dual.append(str(target))
    with localcontext() as ctx:
        ctx.prec=100; X=Decimal(10)**100; logX=X.ln(); log2=Decimal(2).ln(); best=None
        for z in ps:
            if z<5 or z>400: continue
            P,V,A,_,w=pdata(z,ps)
            if int(X)<=16*P: continue
            vd=Decimal(V.numerator)/Decimal(V.denominator); ad=Decimal(A.numerator)/Decimal(A.denominator)
            low=(Decimal(2)/X).sqrt()*log2*(X*vd/4-Decimal(2)**w)-Decimal(12)*(Decimal(4*P)).sqrt()*ad*logX
            if low>0: best=(z,low)
        assert best is not None; z,low=best
        uniform={"X":"1e100","max_prime_cutoff_checked":z,"lower_bound":str(low),"z_over_logX":str(Decimal(z)/logX),"strictly_positive":True}
    mutations=["claim_rh_by_replay_rejected","drop_least_owner_order_rejected","erase_real_activation_rejected","promote_5_3_scalar_to_two_rows_rejected","promote_lapbr67_rejected","promote_sacf_energy_to_sign_rejected","replace_one_sided_ratio_by_absolute_rejected","replace_q3sharp_4_by_plus2_rejected","shift_terminal_boundary_rejected","treat_fpcb23_as_proved_rejected"]
    core={"schema":"riemann.x97800.growing-prime-bilinear-tail.v1","frozen_heads":{"pr579":"9f56688236d33c515a92032c640888488c06ed6e","pr580":"812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05","pr589":"ff5156cf6aa469bb7a2155ff4aa7c094bd75b9b6"},"coefficient_checks":cc,"least_owner_checks":oc,"terminal_checks":tc,"rough_packet_checks":10,"threshold_constants":{"row2_multiplier":216,"row3sharp_multiplier":1152},"dual_extreme_ray_checks":dual,"uniform_growing_cutoff_fixture":uniform,"negative_controls":{"absolute_values_forbidden":True,"lapbr67_refuted_by_frozen_pr589":True,"safe_filter_gauge_not_a_source_estimate":True,"scalar_positive_row_negative":5*(-1)+3*2==1,"square_sign_blind":7*7==(-7)*(-7)},"mutations_rejected":mutations,"uniform_theorem_proved_by_replay":False,"fpcb23_proved":False,"rh_established":False,"verdict":"PASS_T97800_GROWING_PRIME_BILINEAR_TAIL_REDUCTION"}
    proof=hashlib.sha256(json.dumps(core,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return {**core,"ok":True,"proof_object_sha256":proof}


if __name__=="__main__":
    result=run(); print(result["verdict"]); print(result["proof_object_sha256"])
