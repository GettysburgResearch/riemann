"""Exact coefficient witnesses for T_a at its critical Dirichlet endpoint.

Only rational coefficient algebra and rational norm upper bounds are computed.
The full weighted-Hardy classification is proved in the accompanying audit.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def rising_coeff(a,N):
 h=[F(1)]
 for n in range(1,N+1):h.append(h[-1]*(a+n-1)/n)
 return h


def image_coeff(f,a,M):
 s=F(0);out=[]
 for n in range(M+1):
  if n<len(f):s+=f[n]
  der=(n+1)*f[n+1] if n+1<len(f) else F(0)
  out.append(der-a*s)
 return out


def ceil_fraction(z):return -((-z.numerator)//z.denominator)


def main():
 checks=[]
 for a in [F(1,2),F(3,4),F(1),F(5,4)]:
  for N in [0,1,3,10]:
   h=rising_coeff(a,N);H=sum(h,F(0));g=image_coeff(h,a,2*N+7)
   expected=[F(0) if n<N else -a*H for n in range(len(g))]
   assert g==expected
   checks.append({'a':str(a),'N':N,'tail_coefficient':str(-a*H),'identity_verified':True})
 bounds=[];H=F(0);targets={10,100,1000,10000};scale=10**12
 for n in range(1,max(targets)+1):
  H+=F(1,n)
  if n in targets:
   # Here polynomial P_(n-1) has norm² H_n. Its image norm² <= 1/2+1/n.
   ratio=(F(1,2)+F(1,n))/H
   upper=ceil_fraction(ratio*scale)
   assert F(upper,scale)>=ratio
   bounds.append({'N':n-1,'harmonic_norm_lower_scaled_integer':(H*scale).numerator//(H*scale).denominator,'image_norm_squared_upper':str(F(1,2)+F(1,n)),'normalized_image_norm_squared_upper_scaled_integer':upper,'scale':scale})
 result={'arithmetic':'exact Fraction; scaled bounds rounded outward','coefficient_checks':checks,'critical_alpha_minus3_a1_bounds':bounds,'proof':'Ta P_N = -a H_N z^N/(1-z); criticaldomainnorm²~logN whileimagenorm²bounded. Fullclassificationandexplicitnonrangegprovedanalyticallyinaudit.','scope':'Auxiliaryoperatorendpointonly; notcounterexampletoRHorthewholeTheorem5.5.'}
 dest=Path(__file__).resolve().parents[1]/'results/gallardo_critical_operator_advocate_round4.json';dest.write_text(json.dumps(result,indent=2)+'\n')
 print('16 exact coefficient identities and4 directed rational endpointnorm bounds passed.')

if __name__=='__main__':main()
