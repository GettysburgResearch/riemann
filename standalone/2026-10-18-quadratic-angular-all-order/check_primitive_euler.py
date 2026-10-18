"""Exact local and complete Dirichlet convolution checks for K=Q(sqrt(-3)), Q=6.
Tests do not prove the analytic continuation or RH equivalence.
"""
import json
from math import isqrt

def factor(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return out

def local(p,e,kind):
    if e==0:return 1
    if p in (2,3):return 0
    split=(p%3==1)
    if kind=='A':
        return (-2 if e==1 else 1 if e==2 else 0) if split else (-1 if e==2 else 0)
    if kind=='B':return (-2 if e==1 else 0) if split else 0
    if kind=='V':return (1-e if split else int(e%2==0))
    if kind=='W':return (0 if e==1 else 2**(e-2)) if split else (-1 if e==2 else 0)
    raise KeyError(kind)

def coeff(n,kind):
    c=1
    for p,e in factor(n):c*=local(p,e,kind)
    return c

def convolution(a,b,n):
    return sum(a[d]*b[n//d] for d in range(1,isqrt(n)+1) if n%d==0 for d in ((d,n//d) if d*d!=n else (d,)))

if __name__=='__main__':
    N=3000
    seq={key:[0]+[coeff(n,key) for n in range(1,N+1)] for key in ('A','B','V','W')}
    checks=0; max_coeff={key:max(map(abs,v[1:])) for key,v in seq.items()}
    witness=[]
    for n in range(1,N+1):
        bv=convolution(seq['A'],seq['V'],n)
        aw=convolution(seq['B'],seq['W'],n)
        vw=convolution(seq['V'],seq['W'],n)
        assert bv==seq['B'][n],('B=A*V',n,bv,seq['B'][n])
        assert aw==seq['A'][n],('A=B*W',n,aw,seq['A'][n])
        assert vw==int(n==1),('V*W=unit',n,vw)
        checks+=3
        if n in (7,49,343,13,169,5,25,125):witness.append({'n':n,**{key:seq[key][n] for key in seq}})
    print(json.dumps({'field':'Q(sqrt(-3))','excluded_rational_primes':[2,3],'limit':N,'exact_predicates':checks,'max_absolute_coefficients':max_coeff,'selected_local_values':witness},sort_keys=True,indent=2))
