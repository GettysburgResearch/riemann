#!/usr/bin/env python3
"""Validated compact concavity certificate using Arb + elementary H-tail bounds.
Install python-flint==0.9.0. All cell endpoints are rational, all acceptance tests
are strict ball comparisons, and serialized witness bounds are exact rationals.
No mpmath or ordinary floating-point acceptance decision is used.
"""
from fractions import Fraction
from pathlib import Path
import argparse,json,platform
from flint import arb,ctx,fmpq
import flint
ROOT=Path(__file__).resolve().parents[2]

def aq(q):
 q=Fraction(q);return arb(fmpq(q.numerator,q.denominator))
def interval(a,b):
 m=(a+b)/2;r=(b-a)/2
 return arb(fmpq(m.numerator,m.denominator),fmpq(r.numerator,r.denominator))
def exact_lower(x):return str(x.lower().fmpq())
def exact_upper(x):return str(x.upper().fmpq())
def h_bounds_at(q,terms):
 x=aq(q);s=arb(0)
 for k in range(1,terms+1):s+=x/(k*(x+k))
 lower=s+(1+x/(terms+1)).log()
 upper=s+(1+x/terms).log()
 return lower,upper

def witness(a,b,terms):
 x=interval(a,b)
 ha,_=h_bounds_at(a,terms)
 _,hb=h_bounds_at(b,terms)
 h=ha.union(hb) # H monotone; lower approximation at a, upper at b.
 ell=h.log();eh=h.exp()
 B=h+eh*ell
 Bp=1+eh*(ell+1/h)
 N=-(eh**2)*(ell+1)/(h**2)+eh*((h-2)*ell+2-3/h)-1
 # If N<0 and Bp>0, known h'(t)>=x/(x+1), h''(t)<=1/(2x)
 # imply g'' <= [N*(x/(x+1))^2 + B*Bp/(2x)]/B^2.
 P=N*(x/(x+1))**2+B*Bp/(2*x)
 if not(B>0 and Bp>0 and N<0 and P<0):return None
 return {'a':str(a),'b':str(b),'H_lower':exact_lower(h),'H_upper':exact_upper(h),
         'B_lower':exact_lower(B),'Bprime_lower':exact_lower(Bp),
         'fsecond_numerator_upper':exact_upper(N),
         'curvature_numerator_upper':exact_upper(P)}

def generate(a,b,terms,max_depth):
 pending=[(a,b,0)];leaves=[];attempts=0
 while pending:
  lo,hi,depth=pending.pop();attempts+=1
  w=witness(lo,hi,terms)
  if w is not None:leaves.append(w);continue
  if depth>=max_depth:raise RuntimeError('Uncertified cell '+str((lo,hi,depth)))
  mid=(lo+hi)/2
  pending.extend([(mid,hi,depth+1),(lo,mid,depth+1)])
 leaves.sort(key=lambda r:Fraction(r['a']))
 return leaves,attempts

def verify(leaves,a,b,terms):
 assert leaves and Fraction(leaves[0]['a'])==a
 previous=a
 for r in leaves:
  lo,hi=Fraction(r['a']),Fraction(r['b'])
  assert lo==previous and hi>lo
  check=witness(lo,hi,terms)
  assert check is not None
  # Certificate rational witnesses must have the asserted signs too.
  assert Fraction(r['B_lower'])>0 and Fraction(r['Bprime_lower'])>0
  assert Fraction(r['fsecond_numerator_upper'])<0
  assert Fraction(r['curvature_numerator_upper'])<0
  previous=hi
 assert previous==b
 return True

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--verify',type=Path)
 ap.add_argument('--terms',type=int,default=32);ap.add_argument('--bits',type=int,default=160)
 ap.add_argument('--left',default='1');ap.add_argument('--right',default='2048')
 ap.add_argument('--max-depth',type=int,default=30)
 args=ap.parse_args();ctx.prec=args.bits;ctx.threads=1
 if args.verify:
  r=json.loads(args.verify.read_text());ctx.prec=r['precision_bits']
  verify(r['cells'],Fraction(r['domain'][0]),Fraction(r['domain'][1]),r['harmonic_terms'])
  print(json.dumps({'verified':True,'cells':len(r['cells']),'domain':r['domain']}));return
 a,b=Fraction(args.left),Fraction(args.right)
 leaves,attempts=generate(a,b,args.terms,args.max_depth)
 verify(leaves,a,b,args.terms)
 out={'status':'validated finite Arb enclosure certificate; analytic derivative and tail lemmas stated separately',
      'domain':[str(a),str(b)],'precision_bits':ctx.prec,'harmonic_terms':args.terms,
      'python_flint_version':flint.__version__,'flint_version':flint.__FLINT_VERSION__,
      'python_version':platform.python_version(),'attempted_cells':attempts,'certified_cells':len(leaves),
      'acceptance':'B>0, Bprime>0, fsecond_numerator<0, curvature_numerator<0 by Arb ball comparisons',
      'special_functions_used':['exp','log'],'H_enclosure':'finite harmonic continuation sum and integral-test logarithmic tail bounds',
      'cells':leaves}
 p=ROOT/'experiments/results/lagarias_compact_arb.json';p.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k!='cells'},indent=2))
if __name__=='__main__':main()
