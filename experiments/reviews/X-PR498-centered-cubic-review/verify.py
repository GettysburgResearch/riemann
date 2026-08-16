#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, random
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

x,s,u=sp.symbols('x s u', positive=True)
w=x*(1-x)-sp.Rational(1,6)
wu=u*(1-u)-sp.Rational(1,6)
K=sp.simplify(2*sp.integrate(wu,(u,0,x)))
assert sp.simplify(K-x*(1-x)*(2*x-1)/3)==0
assert sp.integrate(w,(x,0,1))==0
assert sp.integrate(w*w,(x,0,1))==sp.Rational(1,180)
Khat=sp.factor(sp.integrate(K*x**(s-1),(x,0,1)))
assert sp.simplify(Khat-(s-1)/(3*(s+1)*(s+2)*(s+3)))==0
crit=sp.solve(sp.Eq(sp.diff(K,x),0),x)
vals=[sp.simplify(K.subs(x,c)**2) for c in crit if c.is_real]
assert max(vals)==sp.Rational(1,972)

def prefix(c,j): return sum(c[1:j+1],F(0))
def kval(m,N):
    z=F(m,N); return z*(1-z)*(2*z-1)/3

rng=random.Random(93250); projection_cases=[]
for N in range(2,48):
    c=[F(0)]+[F(rng.randint(-9,9),rng.randint(1,9)) for _ in range(N)]
    Cn=prefix(c,N)
    rows=[Cn-prefix(c,j)-prefix(c,N-j-1) for j in range(N)]
    lhs=sum(rows[j]*(kval(j+1,N)-kval(j,N))/2 for j in range(N))
    rhs=sum(c[m]*kval(m,N) for m in range(1,N+1))
    assert lhs==rhs
    mean=sum(rows,F(0))/N
    lhs0=sum((rows[j]-mean)*(kval(j+1,N)-kval(j,N))/2 for j in range(N))
    assert lhs0==rhs
    energy=sum((r-mean)**2 for r in rows)/F(N*N)
    assert rhs*rhs <= F(N,180)*energy
    projection_cases.append(N)

prime_cases=[]
for N in range(8,64):
    blocks={2:[],3:[],5:[],7:[],11:[]}
    for p in blocks:
        for m in range(1,N+1): blocks[p].append(F(rng.randint(-3,3),rng.randint(1,7)))
    z={p:sum(blocks[p][m-1]*kval(m,N) for m in range(1,N+1)) for p in blocks}
    source=[F(0)]+[sum(blocks[p][m-1] for p in blocks) for m in range(1,N+1)]
    total=sum(source[m]*kval(m,N) for m in range(1,N+1))
    assert total==sum(z.values(),F(0))
    A={p:sum(abs(v) for v in blocks[p]) for p in blocks}
    assert sum(v*v for v in z.values()) <= F(1,972)*sum(v*v for v in A.values())
    prime_cases.append(N)

gram_cases=[]
for dim in range(3,18):
    vectors=[]
    for _ in range(7):
        v=[F(rng.randint(-10,10),rng.randint(1,9)) for _ in range(dim)]
        m=sum(v,F(0))/dim; vectors.append([q-m for q in v])
    total=[sum(v[j] for v in vectors) for j in range(dim)]
    lhs=sum(t*t for t in total)
    diag=sum(sum(q*q for q in v) for v in vectors)
    cross=2*sum(sum(vectors[a][j]*vectors[b][j] for j in range(dim))
                for a in range(len(vectors)) for b in range(a+1,len(vectors)))
    assert lhs==diag+cross; gram_cases.append(dim)

payload={'classification':'PASS_PR498_CENTERED_CUBIC_REVIEW_ALGEBRA','kernel':str(K),
'mellin_multiplier':str(Khat),'weight_mean':'0','weight_l2_squared':'1/180',
'kernel_sup_squared':'1/972','projection_case_count':len(projection_cases),
'prime_block_case_count':len(prime_cases),'centered_gram_case_count':len(gram_cases),
'scope':'exact algebraic reconstruction only; does not prove CPBD, von Koch, or RH'}
raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['proof_object_sha256']=hashlib.sha256(raw).hexdigest()
out=Path(__file__).with_name('verification.json')
out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(payload['classification']); print(payload['proof_object_sha256'])
