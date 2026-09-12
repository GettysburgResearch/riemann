"""Nondirected high-precision scout: compensate one bb dimer and calibrated head.

Reads pinned #875 source intervals only for exploration; not a source replay.
"""
import argparse,json
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import mpmath as mp
from sensitivity import CENTERS
from source_provenance import find_repository,read_pinned_file

mp.mp.dps=70
HERE=Path(__file__).resolve().parent

def number(v):
 q=Q(v);return mp.mpf(q.numerator)/q.denominator

def midpoint(pair):return (number(pair[0])+number(pair[1]))/2

def cumulants(m):
 k=[mp.mpf(0)]*len(m)
 for n in range(1,len(m)):
  k[n]=m[n]-sum(comb(n-1,j-1)*k[j]*m[n-j] for j in range(1,n))
 return k

def load(repo=None):
 p=json.loads(read_pinned_file(find_repository(repo),'results.json'))
 return p

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument('--repo',type=Path,help='Git checkout containing the pinned #875 commit')
 parser.add_argument('--output',type=Path,default=HERE/'dimer-scout.json')
 args=parser.parse_args()
 p=load(args.repo);print('keys',list(p))
 seed=p['ising'];mu=[midpoint(x) for x in p['theta']['normalized_even_moments']]
 raw=[mp.mpf(0)]*len(mu*2)
 for i,x in enumerate(mu):raw[2*i]=x
 k=cumulants(raw); target=[k[2*r] for r in range(1,5)]
 c=[1,-2,16,-272];tail=[midpoint(x) for x in seed['tail_power_sums_2_4_6_8']]
 A=midpoint(seed['head_sum_A0'])
 def vals(a,b,cc,e,tau):
  m=[mp.mpf(0)]*9;m[0]=1
  for r in range(1,5):m[2*r]=(1+tau)*(2*b)**(2*r)/2
  kd=cumulants(m)
  return [25*a+4*b+cc+e]+[c[r-1]*(25*a**(2*r)+2*b**(2*r)+cc**(2*r)+e**(2*r)+tail[r-1])+kd[2*r] for r in range(1,5)]
 def f(*v):
  vs=vals(*v);return tuple([(vs[0]-A)/A]+[(vs[r+1]-target[r])/abs(target[r]) for r in range(4)])
 x=[number(v) for v in CENTERS]+[mp.mpf('.04')]
 try:
  sol=mp.findroot(f,tuple(x),tol=mp.mpf('1e-60'),maxsteps=100)
  out={'scope':'nondirected floating exploration; not a certificate','solution':[mp.nstr(x,65) for x in sol],'residual':[mp.nstr(x,6) for x in f(*sol)],'positive':bool(all(x>0 for x in sol) and sol[4]<1)}
 except Exception as ex:out={'scope':'nondirected failed attempt','error':str(ex)}
 (HERE/args.output).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(out,indent=2))

if __name__=='__main__':main()
