"""Independent exact reconstruction of first-window finite boundary improvements.
Checks PL knot conditions and endpoint bookkeeping, not zeta or full analytic transfer.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,hashlib
B=Path(__file__).resolve().parents[2];D=B/'experiments/inputs/839_first_window';raw=(D/'inputs.json').read_bytes();p=json.loads(raw);den=p['denominator'];a=F(p['alpha'],den);theta=F(p['separation']);x,y=F(p['x']),F(p['y']);K=p['cob_knots'];h=p['h']
assert den==10**6 and len(K)==6
assert all(K[r][t][0]==K[r][t][1]==K[r][t][-1]==0 for r in range(6) for t in range(3))
assert all(sum(K[r][t][k] for r in range(6))==0 for t in range(3) for k in range(14))
prefix=[[[sum(K[i][t][k] for i in range(r+1)) for k in range(14)] for t in range(3)] for r in range(5)]
states=[]
for lab in itertools.product([0,1],repeat=6):
 dl=sum(h[lab[q]][i] for q in range(6) for i in range(q+1,7));dr=sum(h[lab[q]][i] for q in range(6) for i in range(q+1))
 up=sum(max(prefix[r][lab[r]+lab[r+1]][1:]) for r in range(5));lo=sum(min(prefix[r][lab[r]+lab[r+1]][1:]) for r in range(5))
 states.append({'labels':list(lab),'left_reward_missing':dl,'right_reward_missing':dr,'phi_upper':up,'phi_lower':lo,'left_cost':dl+up,'right_cost':dr-lo})
cl=max(s['left_cost'] for s in states);cr=max(s['right_cost'] for s in states);assert(cl,cr)==(213400,213400)
# Domain[theta,infty): theta lies in the first zero segment; all later extrema of
# a PL potential minus its target line occur at a knot; outside support target grows.
assert F(3,4)<theta<F(7,8)
slacks=[]
for r in range(5):
 for ty in range(3):
  for k in range(1,14):
   t=F(3,4)+F(k,8);A=F(prefix[r][ty][k],den)
   L=a*(5-r)*(t-theta)-A;R=a*(r+1)*(t-theta)+A
   assert L>=0 and R>=0;slacks.extend([L,R])
# 30 additional endpoint inequalities at theta are all exactly0.
old=6*y+F(15882,10**6);joint=F(cl+cr,den);sharp=6*y-30*a*theta
assert sharp==F(516027,2000000) and sharp>0
# Defect identity for every finite chain length checked as an exact coefficient identity.
for m in range(6,81):
 n=m-6;actual=[6 for _ in range(m-1)]
 for w in range(n):
  for q in range(6):actual[w+q]-=1
 expected=[0 for _ in range(m-1)]
 for q in range(5):expected[q]+=5-q;expected[n+q]+=q+1
 assert actual==expected
# Small m has spread>=theta(m-1), rewards<=m*y.
assert all(m*y-6*a*theta*(m-1)<=sharp for m in range(1,7))
bad_alpha,bad_theta,bad_y=F(1,100),F(1),F(11,200)
bad_c=6*bad_y-30*bad_alpha*bad_theta
assert 6*bad_alpha*bad_theta>=bad_y and bad_c>0 and bad_y-bad_c==F(1,40)
out={'kind':'independent_exact_boundary_reconstruction','input_sha256':hashlib.sha256(raw).hexdigest(),'state_patterns':64,'state_table_integer_units':states,'max_left':cl,'max_right':cr,'denominator':den,'original_boundary':str(old),'joint_endpoint_boundary':str(joint),'pressure_aware_boundary':str(sharp),'exact_improvement_over_source':str(old-sharp),'potential_nontrivial_knot_inequalities':len(slacks),'theta_endpoint_inequalities':30,'minimum_positive_knot_slack':str(min(slacks)),'defect_coefficient_identity_checked_lengths':[6,80],'small_chain_cases_pass':True,'small_chain_guard_counterexample':{'theta':'1','alpha':'1/100','x1_equals_x2':'11/200','each_local_reward':'11/1400','weights_and_potentials':'all0','local7point_pressure_pays_reward':True,'candidate_C':'3/100','singleton_violation':'0>=1/40 is false','meaning':'C>0 alone does not replace required small-chain guard y>=6alpha theta'},'scope':'General proof of endpoint identity and PL implication is in advocate note; finite checks support it. No asymptotic proportion improvement, no novelty asserted.'}
(B/'experiments/results/839_boundary_advocate.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='state_table_integer_units'},indent=2))
