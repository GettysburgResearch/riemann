"""Exact rational algebra behind the clipped quartic HS certificate.
No floating eigenvalue computations; matrix-transfer proof is in the audit.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def conv(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c


def val(p,x):return sum((a*x**k for k,a in enumerate(p)),F(0))


def main():
 p=[F(1),-F(7,4),F(2,3)]
 dp=[p[1],2*p[2]]
 # (p')²=(8/3)(p+19/128), checked coefficient by coefficient.
 rhs=[F(8,3)*x for x in p];rhs[0]+=F(8,3)*F(19,128)
 assert conv(dp,dp)==rhs
 q=[-x for x in conv(p,p)];q[0]+=1
 assert q==[0,F(7,2),-F(211,48),F(7,3),-F(4,9)]
 assert val(p,-F(1,4))==F(71,48) and F(71,48)**2>2
 assert val(p,3)==F(7,4) and F(7,4)**2>2
 assert F(64,3)*(F(3,2)+F(19,128))==F(211,6)<36
 moments=[F(1),F(1),F(4,3),F(2),F(13,4)]
 objective=sum((a*b for a,b in zip(q,moments)),F(0))
 assert objective==F(31,36) and 2*objective-1==F(13,18)
 D=84*moments[3]-16*moments[4]
 assert D==116 and (D-85)/36==objective and (D-103)/18==F(13,18)
 examples=[]
 for k in [2,3,10,100]:
  d=k**6
  fourth=(F(1-k*k)**4-1)/d
  formula=F(k*k)-4+F(6,k*k)-F(4,k**4)
  assert fourth==formula
  examples.append({'k':k,'dimension':d,'normalized_HS':'1/'+str(k),'fourth_moment_difference':str(fourth),'positive_fraction':str(1-F(1,d))})
 out={'arithmetic':'exact Fraction polynomial algebra','p':list(map(str,p)),'q':list(map(str,q)),'derivative_identity_verified':True,'active_derivative_squared_upper':'211/6 < 36','global_Lipschitz_bound':6,'sine_four_moment_objective':str(objective),'simple_charge_consequence':'13/18','single_D_value':str(D),'beat_two_thirds_threshold':'liminf D > 115, under normalized HS error o(1)','outlier_examples':examples,'scope':'Algebra and exact outlier witness only. Global HS/functional-calculus proof is in audits/adversarial_reviews/hilbert_schmidt_moment_transfer_round3.md.'}
 dest=Path(__file__).resolve().parents[1]/'results/hs_clipped_certificate_round3.json';dest.write_text(json.dumps(out,indent=2)+'\n')
 print('Exact quartic coefficients, derivative identity, Lip6 bound, D116/threshold115 algebra, and4 outlier identities passed.')

if __name__=='__main__':main()
