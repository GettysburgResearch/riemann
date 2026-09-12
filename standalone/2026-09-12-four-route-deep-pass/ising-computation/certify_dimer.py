"""Whole-box certificate for calibrated degree-eight infinite Ising seed.

Reconstructs complete native theta moments and all required infinite tail
bounds from the pinned #875 primitive arithmetic. The analytic continuation
to connected infinite chains is a written theorem, not finite execution.
Accepting arithmetic is standard-library rational / outward dyadic only.
"""
from pathlib import Path
import json,hashlib,argparse
from fractions import Fraction as Q
from math import comb
HERE=Path(__file__).resolve().parent
from source_provenance import EXPECTED_SHA256,load_primitives
_primitives=load_primitives()  # Authenticate before any predecessor code executes.
I=_primitives['exact_interval'].I
SCALE=_primitives['exact_interval'].SCALE
log_q=_primitives['exact_interval'].log_q
report=_primitives['native_theta'].report
cumulants=_primitives['native_theta'].cumulants
log_power_tail=_primitives['calibrated_chain'].log_power_tail
euler_gamma=_primitives['calibrated_chain'].euler_gamma
invert=_primitives['calibrated_chain'].invert
maxabs=_primitives['calibrated_chain'].maxabs

CENTERS=tuple(Q(s) for s in (
 '0.02243295324256231427575472092255325416837814278674166888934136428',
 '0.061733958199373783957987695176925353722698635772423833226673535647',
 '0.1112195814179168046978212145187227934781608790908284572333998364',
 '0.0026032190424023883808440702906745572779364394913286137807784385371',
 '0.044525423810774579223111441034058054258203237061196706466062869403'))
RADIUS=Q(1,10**12)
CUM=(1,-2,16,-272,7936)

def require(ok,msg):
 if not ok:raise ArithmeticError(msg)

def check_contraction(beta_raw,contraction_raw,radius):
 require(type(beta_raw) is int and type(contraction_raw) is int,'integer dyadic bounds required')
 require(isinstance(radius,Q) and radius>0,'positive exact box radius required')
 require(beta_raw>=0 and 0<=contraction_raw<SCALE,'whole-box contraction')
 require(Q(beta_raw,SCALE)+Q(contraction_raw,SCALE)*radius<radius,'whole-box self-map')

def check_parameter_box(box):
 require(len(box)==5 and all(isinstance(x,I) for x in box),'five interval parameters required')
 require(all(x.lo>0 for x in box) and box[4].hi<SCALE,'strict ferromagnetic parameters')

def p_add(p,q):
 out=[Q(0)]*max(len(p),len(q))
 for i,x in enumerate(p):out[i]+=x
 for i,x in enumerate(q):out[i]+=x
 return out

def p_mul(p,q):
 out=[Q(0)]*(len(p)+len(q)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(q):out[i+j]+=a*b
 return out

def dimer_polys():
 m=[[Q(1)]]+[[Q(0)] for _ in range(10)]
 for r in range(1,6):m[2*r]=[Q(2**(2*r-1))]*2
 k=[[Q(0)] for _ in m]
 for n in range(1,len(m)):
  k[n]=m[n]
  for j in range(1,n):
   k[n]=p_add(k[n],[-comb(n-1,j-1)*x for x in p_mul(k[j],m[n-j])])
 return [k[2*r] for r in range(1,6)]

DP=dimer_polys()

def peval(p,t):
 v=0
 for a in reversed(p):v=v*t+a
 return v

def pprime(p):return [i*p[i] for i in range(1,len(p))]

def values(xs):
 a,b,c,e,tau=xs
 return [25*a+4*b+c+e]+[25*a**(2*r)+2*b**(2*r)+c**(2*r)+e**(2*r)+b**(2*r)*peval(DP[r-1],tau)/CUM[r-1] for r in range(1,5)]

def jacobian(xs):
 a,b,c,e,tau=xs
 rows=[[Q(x) for x in (25,4,1,1,0)]]
 for r in range(1,5):
  k=2*r;fac=2+peval(DP[r-1],tau)/CUM[r-1]
  rows.append([25*k*a**(k-1),k*b**(k-1)*fac,k*c**(k-1),k*e**(k-1),b**k*peval(pprime(DP[r-1]),tau)/CUM[r-1]])
 return rows

def bounds(pair):return I(I.q(Q(pair[0])).lo,I.q(Q(pair[1])).hi)

def execute(mesh):
 print('Reconstructing complete native theta source...',flush=True)
 th=report(mesh)
 mus=[bounds(x) for x in th['normalized_even_moments']]
 kappas=cumulants(mus)
 print('Reconstructing complete calibrated harmonic tails...',flush=True)
 d=-Q(7,8)/log_q(Q(2));S=log_power_tail(2,1)
 A=sum((Q(1,n) for n in range(1,32)),Q(0))/2-euler_gamma()-log_q(Q(2))-d*S
 tails=[]
 for k in (2,4,6,8):
  tails.append(sum((Q(comb(k,j),2**(k-j))*d**j*log_power_tail(k+j,j) for j in range(k+1)),I.q(0)))
 targets=[A]+[kappas[r]/CUM[r]-tails[r] for r in range(4)]
 J=jacobian(CENTERS);R=invert(J)
 # Check the reverse inverse identity as well.
 require(all(sum(J[i][k]*R[k][j] for k in range(5))==Q(i==j) for i in range(5) for j in range(5)),'reverse exact inverse')
 box=[I(I.q(x-RADIUS).lo,I.q(x+RADIUS).hi) for x in CENTERS]
 residual=[v-t for v,t in zip(values(CENTERS),targets)]
 beta=max(maxabs(sum((R[i][k]*residual[k] for k in range(5)),I.q(0))) for i in range(5))
 Jbox=jacobian(box)
 L=max(sum(maxabs(I.q(int(i==j))-sum((R[i][k]*Jbox[k][j] for k in range(5)),I.q(0))) for j in range(5)) for i in range(5))
 check_contraction(beta,L,RADIUS)
 check_parameter_box(box)
 # Degree ten is not fitted. Bound every omitted independent-tail weight by 1/(2n).
 tail10=I(0,I.q(Q(1,2**10*9*31**9)).hi)
 a,b,c,e,tau=box
 k10=CUM[4]*(25*a**10+2*b**10+c**10+e**10+tail10)+b**10*peval(DP[4],tau)
 mismatch=(k10-kappas[4])/mus[1]**5
 require(mismatch.lo>0 or mismatch.hi<0,'degree-ten separation')
 output={'scope':'proposed directed finite root certificate plus imported complete-source remainder proofs; no all-order realization',
  'predecessor_commit':'be149104721ae7b65b624c100118edfd7b76b69b','mesh':mesh,'centers':[str(x) for x in CENTERS],
  'authenticated_predecessor_sources':dict(EXPECTED_SHA256),
  'radius':str(RADIUS),'dimer_cumulant_polynomials':[[str(x) for x in row] for row in DP],
  'beta_upper':str(Q(beta,SCALE)),'contraction_upper':str(Q(L,SCALE)),
  'inverse_inf_norm':str(max(sum(abs(x) for x in row) for row in R)),
  'exact_inverse_identities':50,'head_mass':A.bounds(),'tail_powers': [x.bounds() for x in tails],
  'native_variance':mus[1].bounds(),'degree_ten_standardized_mismatch':mismatch.bounds(),
  'even_moments_matched':[2,4,6,8],'growth_coefficients':['1/2','-(1+log(2*pi))/2','7/4'],
  'positive_background_q_radius_certified':False,'all_order_realization_proved':False,
  'theta_raw_source_hash':hashlib.sha256(json.dumps(th,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
 return output

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--mesh',type=int,default=128);ap.add_argument('--output',default='dimer-certificate.json');args=ap.parse_args()
 out=execute(args.mesh)
 (HERE/args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print('PASS: degree-eight root; beta',float(Q(out['beta_upper'])),'L',float(Q(out['contraction_upper'])))
 print('degree-ten error',[float(Q(v)) for v in out['degree_ten_standardized_mismatch']])

if __name__=='__main__':main()
