#!/usr/bin/env python3
"""Exact replay for L-105300. Analytic Xi claims and RH are not replayed."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path


def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def sub(a,b):
    out=[Fraction(0)]*max(len(a),len(b))
    for i,x in enumerate(a):out[i]+=x
    for i,x in enumerate(b):out[i]-=x
    return trim(out)


def scale(a,c):return trim([c*x for x in a])


def mul(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)


def derivative(a):
    return trim([Fraction(i)*a[i] for i in range(1,len(a))]) if len(a)>1 else [Fraction(0)]


def divrem(a,b):
    a,b=trim(a),trim(b)
    if b==[0]:raise ZeroDivisionError
    q=[Fraction(0)]*max(1,len(a)-len(b)+1);r=a[:]
    while r!=[0] and len(r)>=len(b):
        k=len(r)-len(b);c=r[-1]/b[-1];q[k]+=c
        r=sub(r,[Fraction(0)]*k+scale(b,c))
    return trim(q),trim(r)


def mod_poly(a,m):return divrem(a,m)[1]


def egcd(a,b):
    r0,r1=trim(a),trim(b);s0,s1=[Fraction(1)],[Fraction(0)];t0,t1=[Fraction(0)],[Fraction(1)]
    while r1!=[0]:
        q,r=divrem(r0,r1);r0,r1=r1,r
        s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
    lc=r0[-1]
    return scale(r0,1/lc),scale(s0,1/lc),scale(t0,1/lc)


def inverse_mod(a,m):
    g,s,_=egcd(a,m)
    if g!=[Fraction(1)]:raise ValueError("not invertible")
    return mod_poly(s,m)


def multiplication_matrix(poly,modulus):
    d=len(modulus)-1;cols=[]
    for j in range(d):
        r=mod_poly(mul(poly,[Fraction(0)]*j+[Fraction(1)]),modulus)
        r += [Fraction(0)]*(d-len(r));cols.append(r)
    return [[cols[j][i] for j in range(d)] for i in range(d)]


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def matpow(a,e):
    n=len(a);r=[[Fraction(i==j) for j in range(n)] for i in range(n)]
    while e:
        if e&1:r=matmul(r,a)
        a=matmul(a,a);e>>=1
    return r


def trace(a):return sum(a[i][i] for i in range(len(a)))


def determinant(a):
    a=[row[:] for row in a];n=len(a);out=Fraction(1)
    for c in range(n):
        p=next((r for r in range(c,n) if a[r][c]),None)
        if p is None:return Fraction(0)
        if p!=c:a[c],a[p]=a[p],a[c];out=-out
        v=a[c][c];out*=v
        for j in range(c,n):a[c][j]/=v
        for r in range(c+1,n):
            f=a[r][c]
            if f:
                for j in range(c,n):a[r][j]-=f*a[c][j]
    return out


def resultant(f,g):
    f,g=trim(f),trim(g);m,n=len(f)-1,len(g)-1;fd,gd=list(reversed(f)),list(reversed(g));s=[]
    for i in range(n):s.append([Fraction(0)]*i+fd+[Fraction(0)]*(n-1-i))
    for i in range(m):s.append([Fraction(0)]*i+gd+[Fraction(0)]*(m-1-i))
    return determinant(s)


def charpoly(a):
    n=len(a);powers=[Fraction(0)]+[trace(matpow(a,k)) for k in range(1,n+1)];e=[Fraction(1)]
    for k in range(1,n+1):e.append(sum((-1)**(i-1)*e[k-i]*powers[i] for i in range(1,k+1))/k)
    out=[Fraction(0)]*(n+1)
    for k in range(n+1):out[n-k]=(-1)**k*e[k]
    return trim(out)


def evaluate(a,x):
    out=Fraction(0)
    for c in reversed(a):out=out*x+c
    return out


def critical_operator(p):
    p1=derivative(p);p2=derivative(p1);u=mod_poly(mul(p,inverse_mod(p2,p1)),p1)
    return u,multiplication_matrix(u,p1)


def check_resultant(p,u_matrix):
    n=len(p)-1;p1=derivative(p);p2=derivative(p1);den=Fraction(n*n)*resultant(p1,p2);cp=charpoly(u_matrix);count=0
    for lam in map(Fraction,(-5,-2,-1,0,1,2,5,11)):
        assert evaluate(cp,lam)==resultant(p1,sub(scale(p2,lam),p))/den;count+=1
    return count


def fs(x):return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"


def run():
    quartic=list(map(Fraction,(2,0,-2,0,1)));u4,U4=critical_operator(quartic)
    moments={1:Fraction(-1,4),2:Fraction(9,32),3:Fraction(-31,256),4:Fraction(129,2048)}
    assert {r:trace(matpow(U4,r)) for r in moments}==moments
    assert u4==[Fraction(-1,2),Fraction(0),Fraction(5,8)]
    k4=Fraction(37,432);debt=Fraction(-169,864);assert moments[2]==k4-debt
    count=check_resultant(quartic,U4)
    cubic=list(map(Fraction,(0,-3,0,1)));u3,U3=critical_operator(cubic)
    assert u3==[Fraction(-1,3)] and trace(U3)==Fraction(-2,3) and trace(matpow(U3,2))==Fraction(2,9)
    coherence3=trace(U3)**2/(2*trace(matpow(U3,2)));assert coherence3==1
    count+=check_resultant(cubic,U3)
    variance=moments[2]-moments[1]**2/3;coherence4=moments[1]**2/(3*moments[2])
    assert variance==Fraction(25,96) and coherence4==Fraction(2,27)
    assert coherence4==1-variance/moments[2]
    assert Fraction(20,36)==Fraction(5,9)>Fraction(1,2)
    result={"verdict":"PASS_X_105300_CRITICAL_RESIDUE_QUOTIENT_ALGEBRA","arithmetic_class":"EXACT_RATIONAL","resultant_point_checks":count,"quartic_interpolant_u":[fs(x) for x in u4],"quartic_trace_moments":{str(r):fs(v) for r,v in moments.items()},"quartic_root_ledger_k4":fs(k4),"quartic_cross_residue_debt":fs(debt),"quartic_centered_variance":fs(variance),"quartic_coherence":fs(coherence4),"cubic_interpolant_u":[fs(x) for x in u3],"cubic_coherence":fs(coherence3),"analytic_xi_saddle_replayed":False,"crdb105200_proved":False,"rh_established":False}
    result["proof_object"]=hashlib.sha256(json.dumps(result,sort_keys=True,separators=(",",":")).encode()).hexdigest();return result


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path);args=ap.parse_args();result=run();text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text,encoding="utf-8")
    print(result["verdict"]);print(result["proof_object"]);print("RH_UNPROVEN")


if __name__=="__main__":main()
