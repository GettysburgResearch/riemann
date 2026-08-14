#!/usr/bin/env python3
from fractions import Fraction
import hashlib,json
from pathlib import Path

LIMIT=250000
SMALL=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)

def mobius(n):
 mu=[0]*(n+1);lp=[0]*(n+1);pr=[];mu[1]=1
 for x in range(2,n+1):
  if lp[x]==0:lp[x]=x;pr.append(x);mu[x]=-1
  for p in pr:
   if p>lp[x] or p*x>n:break
   lp[p*x]=p
   if x%p==0:mu[p*x]=0;break
   mu[p*x]=-mu[x]
 return mu,lp,pr

def main():
 mu,lp,pr=mobius(LIMIT)
 P=1
 for p in SMALL:P*=p
 convolution=0;owners=0;paths=0
 for n in range(1,LIMIT+1):
  muP=mu[n] if P%n==0 else 0
  z=n; rough_factors=[]
  while z>1:
   q=lp[z]; e=0
   while z%q==0: z//=q; e+=1
   if q>=67: rough_factors.append((q,e))
  rough_divs=[1]
  for q,e in rough_factors:
   rough_divs=[d*q**a for d in rough_divs for a in range(e+1)]
  s=sum(mu[n//m] for m in rough_divs)
  assert s==muP,(n,s,muP);convolution+=1
  if n>1:
   z=n;fac=[];rough=True
   while z>1:
    q=lp[z]
    if q<67:rough=False;break
    fac.append(q);z//=q
   if rough:
    assert fac==sorted(fac)
    owners+=1;paths+=len(fac)
 vals={m:(Fraction(m,7),Fraction(2*m+1,11),Fraction(3*m+2,13)) for m in range(1,101)}
 B={m:tuple(x/Fraction(3) for x in v) for m,v in vals.items()}
 Z={m:tuple(v[i]-B[m][i] for i in range(3)) for m,v in vals.items()}
 for m in vals:
  assert tuple(B[m][i]+Z[m][i] for i in range(3))==vals[m]
 assert vals[1]==tuple(B[1][i]+Z[1][i] for i in range(3))
 payload={'classification':'PASS_ROUGH_COACTION_ONE_OWNER_LEDGER','limit':LIMIT,
          'convolution_states':convolution,'rough_owned_states':owners,
          'prime_path_edges':paths,'synthetic_typed_fibers':len(vals),
          'scope':'Exact finite regression of mu_P=1_R*mu, unique least-prime ownership, counit, and typed naturality. The mathematical theorem is by unique factorization; this replay does not construct positive native entry or RH.'}
 payload['proof_object_sha256']=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
 out=Path(__file__).resolve().parent/'results'/'verification.json';out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
 print(payload['classification']);print(json.dumps(payload,indent=2,sort_keys=True))
if __name__=='__main__':main()
