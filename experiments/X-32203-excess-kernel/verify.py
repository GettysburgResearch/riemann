#!/usr/bin/env python3
from fractions import Fraction
import json, hashlib, math

N=7; M=8

def beta(n,q):
    k,r=divmod(n,q)
    return Fraction(k*(q-1-r),n+1)

def A(x,q):
    a,r=divmod(x,q)
    return Fraction(q*a*(a-1),2)+a*(r+1)

def mobius(n):
    x=n; p=2; parity=0
    while p*p<=x:
        if x%p==0:
            x//=p; parity^=1
            if x%p==0: return 0
            while x%p==0: x//=p
        p+=1
    if x>1: parity^=1
    return -1 if parity else 1

h={q: Fraction(M-N)-A(M,q)+Fraction(M*(M+1),N*(N+1))*A(N,q) for q in range(2,N+1)}
U={}
for m in range(1,N+1):
    U[m]=sum(Fraction(mobius(k))*h.get(m*k,Fraction(0)) for k in range(1,N//m+1))
U[N+1]=Fraction(0)
R={m:U[m]-U[m+1] for m in range(2,N+1)}

phi={1:Fraction(0),2:Fraction(0),3:Fraction(0),4:Fraction(1),5:Fraction(0),6:Fraction(1),7:Fraction(1)}
constraints=[]
for n in range(2,N+1):
    lo=math.ceil(n/4); hi=math.floor(3*n/4)
    for j in range(max(1,lo),min(n-1,hi)+1):
        defect=phi[n]-phi[j]-phi[n-j]
        assert defect>=0,(n,j,defect)
        constraints.append((n,j,str(defect)))
pair=sum(R[m]*phi[m] for m in range(2,N+1))
assert pair==Fraction(-1,7),pair

# Average-row inverse mutation c(4)=-1/3.
res=dict(h)
c={}
for q in range(N,1,-1):
    cq=res[q]/beta(q,q)
    c[q]=cq
    for p in range(2,q+1):
        res[p]-=cq*beta(q,p)
assert c[4]==Fraction(-1,3),c[4]

out={
  'classification':'EXACT_EXCESS_KERNEL_SEPARATION_REFUTED',
  'target':{str(q):str(h[q]) for q in range(2,N+1)},
  'divergence':{str(q):str(R[q]) for q in range(2,N+1)},
  'phi':{str(q):str(phi[q]) for q in range(2,N+1)},
  'quarter_balanced_constraints':len(constraints),
  'farkas_pairing':str(pair),
  'average_inverse_c4':str(c[4]),
}
payload=json.dumps(out,sort_keys=True,separators=(',',':'))
out['proof_object_sha256']=hashlib.sha256(payload.encode()).hexdigest()
print(json.dumps(out,indent=2,sort_keys=True))
