"""Independent exact checks of frozen data, label-share inequality, and author public APIs.
Does not run the full search, evaluate zeta, or validate Lean.
"""
from pathlib import Path
from fractions import Fraction as F
import json,random,struct,subprocess,tempfile,hashlib,time
B=Path(__file__).resolve().parents[2];D=B/'experiments/inputs/839_first_window';V=B/'experiments/code/vendor/839_reference';p=json.loads((D/'inputs.json').read_text());start=time.monotonic()
G,S,R=p['grid'],p['scale'],p['R'];n=7;M=(F(p['separation'])*G).__floor__();first=3*G//4;step=G//8;last=first+13*step
W,H,P=p['weights'],p['h'],p['cob_knots'];pairs=[(i,j) for i in range(n) for j in range(i+1,n)];tab=struct.unpack('<'+'I'*(R+1),(D/'kernel_lower.bin').read_bytes())
assert all(0<=a<=b for a,b in zip(*H));assert all(W[0][i]<=W[t][i] for i in range(21) for t in [1,2]);assert min(sum(W,[]))>=0
for ty in range(3):
 for distance in range(1,n):assert sum(W[ty][z] for z,(i,j) in enumerate(pairs) if j-i==distance)<=[2000000,4000000,8000000][ty]
 for k in range(14):assert sum(P[g][ty][k] for g in range(6))==0
for g in range(6):
 for ty in range(3):assert P[g][ty][0]==P[g][ty][-1]==0
budget=sum(-min([0]+sum(gap,[])) for gap in P);assert budget==p['budget'];span_margin=p['alpha']*R-(sum(H[1])+budget)*G;assert span_margin>=0
# Independent exact continuous interpolation, in integer-grid coordinates and units S.
def pot(g,ty,x):
 if x<=first or x>=last:return F(0)
 j=int((x-first)//step);u=(x-first-j*step)/step
 return S*((1-u)*P[g][ty][j]+u*P[g][ty][j+1])
def minpiece(fn,lo,hi):
 xs=[lo,hi]+[first+j*step for j in range(14) if lo<first+j*step<hi]
 return min(fn(F(x)) for x in xs)
rand=random.Random(20261117);trials=0;negative_pair_gain=0;smallest_slack=None
for _ in range(50):
 lo=[rand.randint(M,30000) for g in range(6)];hi=[a+rand.randint(1,512) for a in lo]
 if sum(lo)>=R:continue
 # Samples explicitly include fractional midpoints and closed interval endpoints.
 x=[rand.choice([F(a),F(b),F(a+b,2)]) for a,b in zip(lo,hi)]
 if sum(x)>R:continue
 mins=[minpiece(lambda u,g=g:pot(g,0,u),lo[g],hi[g]) for g in range(6)]
 share=[F(0)]*7;base=F(p['alpha']*S*sum(lo),G)+sum(mins);actual_k=[]
 for z,(i,j) in enumerate(pairs):
  a=sum(lo[i:j]);b=min(sum(hi[i:j]),R-sum(lo)+a);mn=min(tab[a:max(a,b-1)+1]);kv=mn+rand.randint(0,12345);actual_k.append(kv);base+=W[0][z]*mn
  d1=F((W[1][z]-W[0][z])*mn);d2=F((W[2][z]-W[0][z])*mn)
  if j==i+1:
   d1+=minpiece(lambda u,g=i:pot(g,1,u)-pot(g,0,u),lo[i],hi[i]);d2+=minpiece(lambda u,g=i:pot(g,2,u)-pot(g,0,u),lo[i],hi[i])
  gain=min(2*d1,d2);negative_pair_gain+=gain<0;share[i]+=gain;share[j]+=gain
 penalty=sum(min(F(0),share[i]-2*(H[1][i]-H[0][i])*S) for i in range(7));lower=2*(base-sum(H[0])*S)+penalty
 for mask in range(128):
  bits=[(mask>>i)&1 for i in range(7)];lhs=F(p['alpha']*S*sum(x),G)+sum(W[bits[i]+bits[j]][z]*actual_k[z] for z,(i,j) in enumerate(pairs))+sum(pot(g,bits[g]+bits[g+1],x[g]) for g in range(6));rhs=sum(H[bits[i]][i]*S for i in range(7));slack=2*(lhs-rhs)-lower;assert slack>=0
  smallest_slack=slack if smallest_slack is None else min(slack,smallest_slack);trials+=1
# Compile a harness around actual unmodified reference code; compare APIs to Fraction semantics.
queries=[]
for q in range(200):
 g,ty,bt=rand.randrange(6),rand.randrange(3),rand.randrange(3);lo=rand.choice([0,first,last,rand.randrange(R+1)]);hi=min(R,lo+rand.randrange(1,10000));pos=rand.choice([0,first,last,lo,hi]);a=rand.randrange(R+1);b=min(R,a+rand.randrange(1,1000));queries.append((g,ty,bt,lo,hi,pos,a,b))
queries += [(0,0,1,0,R,first,a,b) for a,b in [(0,R),(0,0),(R,R),(13926,13927)]]
expected=[]
for g,ty,bt,lo,hi,pos,a,b in queries:
 mid=(lo+hi)//2; slope=0
 if first<mid<last:
  j=(mid-first)//step;slope=F((P[g][ty][j+1]-P[g][ty][j])*S,step)
 off=minpiece(lambda u:pot(g,ty,u)-slope*u,lo,hi)
 row=[pot(g,ty,F(pos)),minpiece(lambda u:pot(g,ty,u),lo,hi),minpiece(lambda u:pot(g,ty,u)-pot(g,bt,u),lo,hi),F(slope),off,F(min(tab[a:b+1]))];assert all(v.denominator==1 for v in row);expected.append([int(v) for v in row])
with tempfile.TemporaryDirectory() as td:
 td=Path(td);params=td/'params.txt';exe=td/'harness';subprocess.run(['python',str(V/'make_parameters.py'),str(D/'inputs.json'),str(params)],check=True)
 subprocess.run(['g++','-std=c++23','-O2','-D_GLIBCXX_ASSERTIONS','-I',str(V),str(B/'experiments/code/839_search_skeptic_harness.cpp'),'-o',str(exe)],check=True,capture_output=True,text=True)
 inp=str(len(queries))+'\n'+'\n'.join(' '.join(map(str,row)) for row in queries)+'\n';run=subprocess.run([str(exe),str(params),str(D/'kernel_lower.bin')],input=inp,capture_output=True,text=True,check=True);observed=[list(map(int,x.split())) for x in run.stdout.splitlines()];assert observed==expected
# Conservative frozen-data bounds, deliberately larger than actual dynamic ranges.
Wmax=max(sum(W,[]));Pmax=max(abs(x) for gap in P for row in gap for x in row);Hmax=max(sum(H,[]));pressure=p['alpha']*(S//G)
source_guard=512*S*(Wmax+Pmax+Hmax)+64*p['alpha']*(S//G)*(R+2);support_guard=4*S*(R+2)+4*Pmax*S*(1+R//step)
coarse_basic=2*pressure*R+S*(3*n*(n-1)*Wmax+(4*n+2)*(n-1)*Pmax+4*n*Hmax)
assert max(source_guard,support_guard,coarse_basic)<2**63-1
wide_tighter=S*(12*Pmax+63*Wmax+R*(48*Pmax+147*Wmax+12*p['alpha']))
assert wide_tighter<2**127-1
wide_coarse=1000*(Wmax+Pmax+Hmax+p['alpha']+1)*(S+1)*(R+2)**2;assert wide_coarse<2**127-1
out={'kind':'independent_scoped_search_soundness_checks_not_full_search','data_sha256':hashlib.sha256((D/'inputs.json').read_bytes()).hexdigest(),'span_margin_in_integer_units':span_margin,'data_conditions_pass':True,'minimum_gap_grid':M,'true_theta_grid':str(F(p['separation'])*G),'labelled_pointwise_comparisons':trials,'negative_gain_pair_cases':negative_pair_gain,'minimum_comparison_slack':str(smallest_slack),'author_public_api_queries':len(queries),'author_api_vs_independent_fraction_semantics':'all_equal','source_integer_search_guard':str(source_guard),'source_integer_support_guard':str(support_guard),'independent_coarse_basic_bound':str(coarse_basic),'signed_int64_limit':str(2**63-1),'independent_affine_value_bound':str(wide_tighter),'independent_coarse_affine_bound':str(wide_coarse),'signed_int128_limit':str(2**127-1),'elapsed_seconds':time.monotonic()-start,'scope':'General algebra and continuum coverage reviewed by hand separately. Small exact tests are supplemental. No full search replay, no zeta/analytic transfer verification, no Lean run.'}
(B/'experiments/results/839_search_skeptic_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
