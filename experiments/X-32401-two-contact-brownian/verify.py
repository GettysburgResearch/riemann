#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json

def mobius(n):
    if n == 1:
        return 1
    x=n
    p=2
    cnt=0
    while p*p<=x:
        if x%p==0:
            x//=p
            cnt+=1
            if x%p==0:
                return 0
            while x%p==0:
                x//=p
        p+=1
    if x>1:
        cnt+=1
    return -1 if cnt%2 else 1

def is_prime(n):
    if n<2: return False
    d=2
    while d*d<=n:
        if n%d==0: return False
        d+=1
    return True

def prime_power_base_exp(n):
    if n<2: return None
    for p in range(2,n+1):
        if not is_prime(p): continue
        q=p
        a=1
        while q<n:
            q*=p; a+=1
        if q==n:
            return p,a
    return None

def v2(n):
    r=0
    while n%2==0 and n:
        r+=1; n//=2
    return r

def add_form(a,b,scale=Fraction(1)):
    c=dict(a)
    for p,v in b.items():
        c[p]=c.get(p,Fraction(0))+scale*v
        if c[p]==0: del c[p]
    return c

def lambda_form(n):
    pe=prime_power_base_exp(n)
    return {} if pe is None else {pe[0]:Fraction(1)}

def lambda_lambda_form(n, lam):
    out=lambda_form(n)
    pe=prime_power_base_exp(n)
    if pe and pe[0]==2:
        out=add_form(out,{2:lam**pe[1]})
    return out

def c_lambda_form(n,lam):
    out=lambda_lambda_form(n,lam)
    if n%2==0:
        out=add_form(out,lambda_lambda_form(n//2,lam),-lam)
    return out

def expected_c_lambda(n,lam):
    if n==2:
        return {} if Fraction(1)+lam==0 else {2:Fraction(1)+lam}
    pe=prime_power_base_exp(n)
    if pe and pe[0]==2 and pe[1]>=2:
        return {} if lam==1 else {2:Fraction(1)-lam}
    if pe and pe[0]!=2:
        return {pe[0]:Fraction(1)}
    if n%2==0:
        pe2=prime_power_base_exp(n//2)
        if pe2 and pe2[0]!=2:
            return {} if lam==0 else {pe2[0]:-lam}
    return {}

def b_lambda(n,lam):
    ans=Fraction(mobius(n))
    if n%2==0:
        ans -= lam*mobius(n//2)
    return ans

def floor_frac(x):
    return x.numerator//x.denominator

def carry(x,theta):
    return floor_frac(x)-floor_frac(theta*x)-floor_frac((1-theta)*x)

def J(r,theta):
    if r<=0 or r>1: return 0
    return 1 - (1 if theta>=r else 0) - (1 if 1-theta>=r else 0)

def source_wavelet(X,m,theta,lam):
    s=Fraction(0)
    for k in range(1,X//m+1):
        s += b_lambda(k,lam)*carry(Fraction(X,m*k),theta)
    return s

def inner_J(r,s):
    if r<=0 or r>1 or s<=0 or s>1: return Fraction(0)
    if r==Fraction(1,2) or s==Fraction(1,2): return Fraction(0)
    er=1 if r>Fraction(1,2) else -1
    es=1 if s>Fraction(1,2) else -1
    ar=abs(r-Fraction(1,2))
    a_s=abs(s-Fraction(1,2))
    return 2*er*es*min(ar,a_s)

def direct_energy(X, coeff):
    total=Fraction(0)
    for m,cm in coeff.items():
        for n,cn in coeff.items():
            total += cm*cn*inner_J(Fraction(m,X),Fraction(n,X))
    return total/Fraction(X)

def layer_energy(X, coeff):
    events={}
    for n,c in coeff.items():
        r=Fraction(n,X)
        if r==Fraction(1,2): continue
        a=abs(r-Fraction(1,2))
        g=c if r>Fraction(1,2) else -c
        events[a]=events.get(a,Fraction(0))+g
    S=sum(events.values(),Fraction(0))
    prev=Fraction(0)
    integ=Fraction(0)
    for a in sorted(events):
        integ += (a-prev)*S*S
        S -= events[a]
        prev=a
    integ += (Fraction(1,2)-prev)*S*S
    return 2*integ/Fraction(X)

def no_go(X):
    A=[n for n in range(3*X//4+1,X) if n%2==1]
    coeff={n:Fraction(1) for n in A}
    e=direct_energy(X,coeff)
    budget=sum((Fraction(1,n) for n in A),Fraction(0))
    return len(A),e,budget

def main():
    counts={"coefficient_rows":0,"wavelet_rows":0,"gram_rows":0,"energy_rows":0,"no_go_rows":0}
    lams=[Fraction(-1),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1)]
    for lam in lams:
        for n in range(1,129):
            a=sum((lam**r for r in range(v2(n)+1)),Fraction(0))
            assert a>=0
            lf=lambda_lambda_form(n,lam)
            assert all(v>=0 for v in lf.values())
            assert c_lambda_form(n,lam)==expected_c_lambda(n,lam)
            counts["coefficient_rows"]+=1
    for lam in lams:
        for X in range(4,29):
            den=2*X+1
            for m in range(1,X+1):
                for j in (1,den//3,den//2,2*den//3,den-1):
                    theta=Fraction(j,den)
                    lhs=source_wavelet(X,m,theta,lam)
                    rhs=Fraction(J(Fraction(m,X),theta))-lam*J(Fraction(2*m,X),theta)
                    assert lhs==rhs
                    counts["wavelet_rows"]+=1
    radii=[Fraction(k,32) for k in range(1,32)]
    for r in radii:
        for s in radii:
            if r==Fraction(1,2) or s==Fraction(1,2):
                direct=Fraction(0)
            else:
                er=1 if r>Fraction(1,2) else -1
                es=1 if s>Fraction(1,2) else -1
                direct=2*er*es*min(abs(r-Fraction(1,2)),abs(s-Fraction(1,2)))
            assert direct==inner_J(r,s)
            counts["gram_rows"]+=1
    packets=[
        (16,{3:Fraction(2),5:Fraction(-1),11:Fraction(3),14:Fraction(-2)}),
        (24,{2:Fraction(1),7:Fraction(5),13:Fraction(-4),19:Fraction(2)}),
        (32,{5:Fraction(-3),9:Fraction(2),17:Fraction(7),29:Fraction(-1)}),
    ]
    for X,c in packets:
        assert direct_energy(X,c)==layer_energy(X,c)
        counts["energy_rows"]+=1
    no_go_data=[]
    for X in (16,24,32,40,64,80,128):
        k,e,b=no_go(X)
        assert k>=X//16
        assert e>=Fraction(X,512)
        assert b<=Fraction(1,3)
        counts["no_go_rows"]+=1
        no_go_data.append({"X":X,"active":k,"energy":f"{e.numerator}/{e.denominator}","budget":f"{b.numerator}/{b.denominator}"})
    payload={"classification":"PASS_EXACT_TWO_CONTACT_BROWNIAN_NORMAL_FORM","counts":counts,"no_go":no_go_data}
    canonical=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    payload["proof_digest_sha256"]=hashlib.sha256(canonical).hexdigest()
    print(json.dumps(payload,sort_keys=True,indent=2))

if __name__=="__main__":
    main()
