"""Exact finite bookkeeping checks for the first-window local-to-global transfer.
Uses bundled MIT input data; no local-search or zeta computation.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,random,hashlib,csv
B=Path(__file__).resolve().parents[2];D=B/'experiments/inputs/839_first_window';p=json.loads((D/'inputs.json').read_text());W,H,P=p['weights'],p['h'],p['cob_knots'];pairs=[(i,j) for i in range(7) for j in range(i+1,7)];sep=F(17,20)
caps=[]
for ty in range(3):
 row=[sum(W[ty][z] for z,(i,j) in enumerate(pairs) if j-i==s) for s in range(1,7)];assert all(0<=v<=[2000000,4000000,8000000][ty] for v in row);caps.append(row)
assert [sum(row) for row in H]==[54350,69433]
assert all(0<=H[0][i]<=H[1][i] for i in range(7))
assert all(sum(P[r][ty][k] for r in range(6))==0 for ty in range(3) for k in range(14))
def pot(r,ty,t):
 return sum((F(P[r][ty][k],10**6)*max(F(0),1-abs(8*(t-F(3,4)-F(k,8)))) for k in range(14)),F(0))
def Apot(q,ty,t):return sum((pot(r,ty,t) for r in range(q+1)),F(0))
points=[sep]+[F(3,4)+F(k,8) for k in range(14) if F(3,4)+F(k,8)>=sep]+[F(3)]
hi=[];lo=[];arg_hi=[];arg_lo=[]
for q in range(5):
 highs=[];lows=[];ah=[];al=[]
 for ty in range(3):
  vals=[Apot(q,ty,t) for t in points];a=max(range(len(vals)),key=lambda z:vals[z]);b=min(range(len(vals)),key=lambda z:vals[z]);highs.append(vals[a]);lows.append(vals[b]);ah.append(points[a]);al.append(points[b])
 hi.append(highs);lo.append(lows);arg_hi.append(ah);arg_lo.append(al)
states=[]
for lab in product(range(2),repeat=6):
 tys=[lab[q]+lab[q+1] for q in range(5)];states.append((sum(hi[q][ty] for q,ty in enumerate(tys)),sum(lo[q][ty] for q,ty in enumerate(tys)),lab,tys))
mx=max(states,key=lambda z:z[0]);mn=min(states,key=lambda z:z[1]);omega=mx[0]-mn[1];assert omega==F(15882,10**6)
maxg=[arg_hi[q][ty] for q,ty in enumerate(mx[3])];ming=[arg_lo[q][ty] for q,ty in enumerate(mn[3])]
# The endpoint state can be charged against pressure missing at each boundary.
alpha=F(6219,10**6);pressure_checks=0;pressure_certificate=[]
for q in range(5):
 for ty in range(3):
  for t in points:
   a=Apot(q,ty,t)
   assert a<=alpha*(5-q)*(t-sep)
   assert -a<=alpha*(q+1)*(t-sep)
   pressure_checks+=2;pressure_certificate.append([q,ty,str(t),str(a),str(alpha*(5-q)*(t-sep)-a),str(alpha*(q+1)*(t-sep)+a)])
C_pressure=F(6*69433,10**6)-30*alpha*sep
assert C_pressure==F(516027,2000000)
assert F(69433,10**6)-6*alpha*sep>0
for ell in range(1,7):assert ell*F(69433,10**6)-6*alpha*(ell-1)*sep<=C_pressure
joint_left=[];joint_right=[]
for bits in product(range(2),repeat=6):
 ty=[bits[q]+bits[q+1] for q in range(5)]
 dl=F(sum(sum(H[bits[v]][i] for i in range(v+1,7)) for v in range(6)),10**6)
 dr=F(sum(sum(H[bits[v]][i] for i in range(v+1)) for v in range(6)),10**6)
 joint_left.append((dl+sum(hi[q][z] for q,z in enumerate(ty)),bits))
 joint_right.append((dr-sum(lo[q][z] for q,z in enumerate(ty)),bits))
assert max(joint_left)[0]+max(joint_right)[0]==F(1067,2500)
# Actual chain with n=6 windows: initial and final states have disjoint site labels.
lab=list(mx[2])+list(mn[2]);g=maxg+[F(1)]+ming
psum=sum((pot(r,lab[w+r]+lab[w+r+1],g[w+r]) for w in range(6) for r in range(6)),F(0));assert psum==omega
# Independent exact state identity, rewards and pressure on fractional-gap chains, including n=0.
rand=random.Random(20261117);identities=0
for n in range(21):
 ell=n+6;labs=[rand.randrange(2) for _ in range(ell)];gaps=[sep+F(rand.randrange(0,40),32) for _ in range(ell-1)]
 def state(w):return sum((Apot(q,labs[w+q]+labs[w+q+1],gaps[w+q]) for q in range(5)),F(0))
 localpot=sum((pot(r,labs[w+r]+labs[w+r+1],gaps[w+r]) for w in range(n) for r in range(6)),F(0));assert localpot==state(0)-state(n) and localpot<=omega
 localrew=sum(H[labs[w+i]][i] for w in range(n) for i in range(7));globalrew=sum(sum(H[a]) for a in labs);assert globalrew-localrew<=6*69433
 locg=sum((gaps[w+r] for w in range(n) for r in range(6)),F(0));assert locg<=6*sum(gaps)
 delta=6*sum(gaps)-locg
 assert delta==sum((5-q)*gaps[q]+(q+1)*gaps[n+q] for q in range(5))
 assert localpot<=alpha*delta-30*alpha*sep
 assert F(globalrew-localrew,10**6)+localpot-alpha*delta<=C_pressure
 identities+=1
for ell in range(101):
 near=sum(1 for i in range(ell) for j in range(i+1,ell) if j-i<=6);assert near==sum(max(ell-s,0) for s in range(1,7)) and near<=6*ell
# Exact witness against removing nonnegativity from an ALL-PAIRS conclusion.
ell=100;eps=F(1);R=7*(ell-1);x=F(54350,10**6);span=F(6*6219,10**6);boundary=F(6*69433+15882,10**6);lhs=x*ell-span*R-boundary-48*eps*ell;rhs=-ell*(ell-1);assert lhs>rhs
out={'kind':'exact_transfer_bookkeeping_and_scope_check_NOT_zeta_audit','input_sha256':hashlib.sha256((D/'inputs.json').read_bytes()).hexdigest(),'index_distance_weight_sums':caps,'state_maximum':str(mx[0]),'state_minimum':str(mn[1]),'omega_exact':str(omega),'maximum_state_labels':[a+1 for a in mx[2]],'maximum_state_gaps':list(map(str,maxg)),'minimum_state_labels':[a+1 for a in mn[2]],'minimum_state_gaps':list(map(str,ming)),'six_window_chain_attains_omega':True,'fractional_chain_identities_checked':identities,'uniform_boundary_constant':str(boundary),'joint_label_boundary_constant':str(max(joint_left)[0]+max(joint_right)[0]),'pressure_adjusted_boundary_constant':str(C_pressure),'pressure_domination_point_checks':pressure_checks,'pressure_adjusted_bookkeeping_equality_witness':'all labels double and all gaps17/20, chain length at least6','boundary_claim_status':'Independently derived finite strengthening; parent review pending; no asymptotic proportion improvement or literature novelty claim','all_pairs_without_positivity_counterexample':{'ell':ell,'labels':'all simple','positions':'y_i=7i,0<=i<100','epsilon':str(eps),'R':R,'e_offdiag':-1,'kernel_values':'K(7n)=0 for every nonzero integer n, because the six-mode sinc expansion has no zero denominator there','left_side':str(lhs),'right_side':rhs,'inequality_fails':True},'scope':'LocalInequality is assumed. General transfer proof reconstructed separately; exact tests supplement its bookkeeping, not proof of the input local inequality or analytic zeta bridge.'}
with (B/'experiments/results/839_transfer_pressure_certificate.csv').open('w',newline='') as f:
 writer=csv.writer(f);writer.writerow(['q','pair_type','t','A_q','left_domination_margin','right_domination_margin']);writer.writerows(pressure_certificate)
(B/'experiments/results/839_transfer_skeptic_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
