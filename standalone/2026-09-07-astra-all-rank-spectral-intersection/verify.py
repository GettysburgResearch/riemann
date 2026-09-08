#!/usr/bin/env python3
"""TSR26: exact finite cyclotomic proof and bounded coefficient regressions.

The all-rank reduction is the paper's affine-count identity. No floating roots,
curve searches, external packages, or unbounded rank extrapolation are used.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from math import isqrt
from pathlib import Path
import sys

N=24
EXPECTED=('CLAIMS.tsv','PROOF.md','README.md','SOURCES.json','VALIDATION.md','result.json','verify.py')
PARENT='10446e8ea9c55162c317810f63c1f7a379466459'
PINS=[
 ('research/l-families/atlas/function_field/TENSOR_SYMMETRIC_POWER_RESEARCH_MAP.md','000879c7d8da092a6f2f30c2eccec053b302bdae'),
 ('research/l-families/atlas/function_field/ELLIPTIC_TENSOR_SYMMETRIC_POWER_SUBTORUS_RIGIDITY.md','c4ffdd465935b68c6f26a152ad4279d4f2087baf'),
 ('research/l-families/atlas/function_field/ELLIPTIC_TENSOR_SYM3_SYM7_SPECTRAL_INTERSECTION.md','f4e8cf80e4ee940c77a28a5fef28d309ca77481b'),
]
ALPHABETS={
 'square':{-2:12,-1:8,0:6,1:4,2:0},
 'class2':{-1:9,0:6,1:3},
 'class3':{-1:10,0:6,1:2},
 'other':{0:6},
}
class Reject(ValueError):pass

def need(v:bool,message:str):
 if not v:raise Reject(message)

def spectra(a:int,b:int,c:int,r:int,n:int=N):
 left=Counter((eps*a+b*(r-2*j))%n for eps in (-1,1) for j in range(r+1))
 right=Counter((c*(2*r+1-2*j))%n for j in range(2*r+2))
 return left,right

def differences(a,b,c,r,n=N):
 L,R=spectra(a,b,c,r,n)
 return [L[k]-R[k] for k in range(n)]

def affine_solutions(d,delta):
 """Solve d+k delta=0 for EVERY integer k>=0, not a scanned finite range."""
 active=[i for i,v in enumerate(delta) if v]
 if not active:return ('all',None) if not any(d) else ('none','constant-nonzero')
 i=active[0];k=F(-d[i],delta[i])
 if k<0:return 'none','negative-k'
 if k.denominator!=1:return 'none','noninteger-k'
 if any(u+k*v for u,v in zip(d,delta)):return 'none','inconsistent-coordinate'
 return 'single',int(k)

def canonical(x,y,z,r):
 if z<0:x,z=-x,-z
 if y<0:x,y=x*(-1)**r,-y
 if z==0 and x<0:x=-x
 return x,y,z

def table(case,x,y,z,r):
 x,y,z=canonical(x,y,z,r)
 if case=='square':
  if z==2:return (x,y)==(2,2)
  if z==0:return (x,y)==(0,2) or (x,y)==((0,0) if r%2==0 else (2,0))
  if z==1:
   choices={0:{1},1:{-1},2:{-2,1},3:{-1},4:{1},5:{-1,2}}
   return y==1 and x in choices[r%6]
  return False
 if case=='class2':
  if z==0:return r%2==0 and (x,y)==(0,0)
  if y==0:return abs(x)==1 if r%2 else x==1
  if y==1:return x==0 if r%2 else x=={0:1,2:-1,4:-1,6:1}[r%8]
  return False
 if case=='class3':
  if z==0:return r%2==0 and (x,y)==(0,0)
  return r%2==0 and y==1 and x=={0:1,2:0,4:-1,6:-1,8:0,10:1}[r%12]
 return r%2==0 and (x,y,z)==(0,0,0)

# Two-dimensional exact quotient-ring arithmetic; every entry is rational.
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def scale(a,s):return a[0]*s,a[1]*s

def mul(a,b,q):return a[0]*b[0]+q*a[1]*b[1],a[0]*b[1]+a[1]*b[0]

def dickson(k,x,q):
 a,b=(F(2),F(0)),x
 if k==0:return a
 for j in range(1,k):a,b=b,sub(mul(x,b,q),a)
 return b

def symchar(k,x,q):
 a,b=(F(1),F(0)),x
 if k==0:return a
 for j in range(1,k):a,b=b,sub(mul(x,b,q),a)
 return b

def graph(case,x,y,z,r):
 d={'class2':2,'class3':3}.get(case,F(1))
 if case in ('class2','class3'):xx,yy,zz=(F(0),F(x)),(F(0),F(y)),(F(0),F(z))
 else:xx,yy,zz=(F(x),F(0)),(F(y),F(0)),(F(z),F(0))
 return any((xx==scale(dickson(r+1,zz,d),s**r) and yy==scale(zz,s)) or
            (xx==scale(zz,s**r) and yy==scale(dickson(2,zz,d),s)) for s in (-1,1))

def exception(case,x,y,z,r):return case=='class2' and r%4==3 and x==0 and abs(y)==abs(z)==1

def qsqrt(q:F):
 a,b=isqrt(q.numerator),isqrt(q.denominator)
 return F(a,b) if a*a==q.numerator and b*b==q.denominator else None

def normtrace(raw:F,q:F):
 s=qsqrt(q)
 return (raw/s,F(0)) if s is not None else (F(0),raw/q)

def raw_powers(q,A,B,C,r):
 x,y,z=[normtrace(F(v),q) for v in (A,B,C)]
 left=[];right=[]
 for k in range(1,2*r+3):
  left.append(mul(dickson(k,x,q),symchar(r,dickson(k,y,q),q),q))
  right.append(symchar(2*r+1,dickson(k,z,q),q))
 return left,right

def matmul(a,b):
 return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
         a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])

def raw_dickson(n,C,q):
 m=(C,-q,F(1),F(0));p=(F(1),F(0),F(0),F(1))
 while n:
  if n%2:p=matmul(p,m)
  m=matmul(m,m);n//=2
 return p[0]+p[3]

def recognize(q,A,B,C,r):
 # Bounded replay API: the theorem and arithmetic recipe are all-rank;
 # this helper rejects oversized fixtures before constructing large rationals.
 need(type(r) is int and 1<=r<=128,'bounded recognition rank')
 q,A,B,C=map(F,(q,A,B,C))
 need(q>0,'positive q')
 need(all(max(v.numerator.bit_length(),v.denominator.bit_length())<=256
          for v in (q,A,B,C)),'bounded recognition input bits')
 if r%4==3 and A==0 and B*B==C*C==2*q:return True
 d=raw_dickson(r+1,C,q);sq=qsqrt(q)
 for sign in (-1,1):
  if B==sign*C:
   if r%2==0 and A*q**(r//2)==d:return True
   if r%2 and sq is not None and A*q**(r//2)*sq==sign*d:return True
   if r%2 and sq is None and A==d==0:return True
  if A==sign**r*C:
   if sq is not None and sq*B==sign*(C*C-2*q):return True
   if sq is None and B==0 and C*C==2*q:return True
 return False

def newton(ps,q):
 c=[(F(1),F(0))]
 for k in range(1,len(ps)+1):
  v=(F(0),F(0))
  for j in range(1,k+1):v=add(v,mul(c[k-j],ps[j-1],q))
  c.append(scale(v,F(-1,k)))
 return c

def powe(x,k,q):
 y=(F(1),F(0))
 for _ in range(k):y=mul(y,x,q)
 return y

def checks():
 counts=[];reasons=Counter();total=0;extras=0
 for r0 in range(1,25):
  row={'r0':r0}
  for case,vals in ALPHABETS.items():
   count=0
   for x,y,z in product(vals,repeat=3):
    a,b,c=vals[x],vals[y],vals[z]
    f=differences(a,b,c,r0);f1=differences(a,b,c,r0+24)
    delta=[v-u for u,v in zip(f,f1)]
    # Independent two-step check of the recurrence; paper proves all steps.
    f2=differences(a,b,c,r0+48)
    need(f2==[u+2*v for u,v in zip(f,delta)],'affine-cycle identity')
    mode,why=affine_solutions(f,delta)
    expected=table(case,x,y,z,r0)
    need(mode==('all' if expected else 'none'),'complete torsion table')
    need(expected==(graph(case,x,y,z,r0) or exception(case,x,y,z,r0)),
         'graph plus exceptional classification')
    if expected:
     count+=1;extras+=int(exception(case,x,y,z,r0))
    else:reasons[why]+=1
    total+=1
   row[case]=count
  counts.append(row)
 need(total==4320,'affine coverage')
 need(extras==24,'four extra sign triples at six residues')
 # Universal graph sufficiency at larger ordinary integer weights.
 monomial=0
 for r in list(range(1,17))+[32,64,128]:
  target=Counter(range(-2*r-1,2*r+2,2))
  for a,b in ((r+1,1),(1,2)):
   for sa,sb in product((-1,1),repeat=2):
    left=Counter(e*sa*a+sb*b*(r-2*j) for e in (-1,1) for j in range(r+1))
    need(left==target,'universal graph weights');monomial+=1
 # A real complex torsion residual must not be erased by the generic theorem.
 L,R=spectra(2,3,1,2,7)
 need(L==R==Counter({j:1 for j in range(1,7)}),'order-seven nongraph residual')
 # Full Newton coefficient test for the new rational exception at q=2,r=3.
 lp,rp=raw_powers(F(2),0,2,2,3)
 need(lp==rp,'q2 exception complete power sums')
 coeff=newton(lp,F(2));norm=(F(0),F(2)**3)
 raw=[mul(v,powe(norm,j,F(2)),F(2)) for j,v in enumerate(coeff)]
 expected=[(F(1),F(0))]+[(F(0),F(0)) for _ in range(8)]
 expected[4]=(F(2**15),F(0));expected[8]=(F(2**28),F(0))
 need(raw==expected,'q2 degree-eight full polynomial')
 # Independent raw power-trace checks on ordinary rational graph data.
 regression=0
 for q in [F(1),F(4),F(1,4)]:
  s=qsqrt(q)
  for C in [F(1,3),F(1),F(3)]:
   z=C/s
   for r in range(1,9):
    for sign in (-1,1):
     A=s*(sign**r)*dickson(r+1,(z,F(0)),F(1))[0];B=sign*C
     need(raw_powers(q,A,B,C,r)[0]==raw_powers(q,A,B,C,r)[1],'raw graph-one powers')
     A=sign**r*C;B=sign*s*(z*z-2)
     need(raw_powers(q,A,B,C,r)[0]==raw_powers(q,A,B,C,r)[1],'raw graph-two powers')
     regression+=2
 for r in [1,3,5,7]:
  for A,B,C in [(0,2,2),(0,-2,2),(2,0,2),(-2,0,-2)]:
   left,right=raw_powers(F(2),A,B,C,r)
   need(left==right,'nonsquare-two odd-rank full powers');regression+=1
 # A bounded complete rational trace box, not the source of the all-rank proof.
 recognition=0
 for q in [F(1),F(2),F(3),F(5),F(1,2),F(1,3)]:
  for r in range(1,5):
   for A,B,C in product(range(-2,3),repeat=3):
    pred=recognize(q,A,B,C,r)
    left,right=raw_powers(q,A,B,C,r)
    need(pred==(left==right),'recognition versus complete power traces')
    recognition+=1
 refused=0
 for args in [(F(1),0,0,0,0),(F(1),0,0,0,129),(F(-1),0,0,0,2)]:
  try:recognize(*args)
  except Reject:refused+=1
  else:raise Reject('bounded API failed to refuse')
 return {'schema':'riemann.tsr26.exact.v1' ,'status':'ALL_RANK_REDUCTION_WITH_EXACT_FINITE_TORSION_PROOF',
         'rh_proved':False,'global_automorphic_transfer_proved':False,
         'period':24,'affine_rows':total,'bounded_api_refusals':refused,'nonrecurring_solutions':0,
         'nongraph_exception_rows':extras,'solutions_by_residue':counts,
         'affine_rejection_reasons':dict(sorted(reasons.items())),
         'universal_graph_weight_fixtures':monomial,
         'raw_power_trace_fixtures':regression,'recognition_box_fixtures':recognition,
         'order7_residual':{'r':2,'u_exponent':2,'v_exponent':3,'w_exponent':1,'order':7},
         'q2_r3_common_raw_coefficients':[str(v[0]) for v in raw]}

def read_json(p):
 def unique(pairs):
  out={}
  for k,v in pairs:
   need(k not in out,'duplicate JSON key');out[k]=v
  return out
 def fail(x):raise Reject('nonexact JSON number')
 return json.loads(p.read_text(),object_pairs_hook=unique,parse_float=fail,parse_constant=fail)

def validate(root):
 need(sorted(p.name for p in root.iterdir())==sorted(EXPECTED+('SHA256SUMS',)), 'file inventory')
 for p in root.iterdir():need(p.is_file() and not p.is_symlink(),'nonregular file')
 manifest={}
 for line in (root/'SHA256SUMS').read_text().splitlines():
  parts=line.split('  ');need(len(parts)==2,'manifest syntax');digest,name=parts
  need(name in EXPECTED and name not in manifest,'manifest inventory')
  need(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'manifest digest')
  manifest[name]=digest
 need(sorted(manifest)==sorted(EXPECTED),'manifest complete')
 for name,digest in manifest.items():need(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'changed bytes '+name)
 src=read_json(root/'SOURCES.json');need(isinstance(src,dict),'source object')
 need(src.get('parent_commit')==PARENT and src.get('parent_pr')==752,'parent source')
 need(src.get('base_commit')=='38a9494be21e85e26b04df1c7c2fdfccfc3c657d','base source')
 fs=src.get('files');need(isinstance(fs,list) and all(isinstance(v,dict) for v in fs),'source list')
 need([(v.get('path'),v.get('git_blob')) for v in fs]==PINS,'exact source pins')
 got=read_json(root/'result.json');expected=checks()
 need(json.dumps(got,sort_keys=True,separators=(',',':'))==
      json.dumps(expected,sort_keys=True,separators=(',',':')),'computed result mismatch')

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--generate',type=Path);args=ap.parse_args()
 try:
  if args.generate:
   need(not args.generate.exists(),'generation output exists')
   args.generate.write_text(json.dumps(checks(),sort_keys=True,indent=2)+'\n')
  else:
   validate(Path(__file__).resolve().parent);print('PASS_TSR26_EXACT_CLASSIFICATION')
  return 0
 except (Reject,OSError,ValueError,KeyError,TypeError) as exc:
  print('REJECTED: '+str(exc),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
