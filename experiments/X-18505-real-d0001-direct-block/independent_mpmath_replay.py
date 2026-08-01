#!/usr/bin/env python3
import argparse, json, math
from fractions import Fraction
from pathlib import Path
import mpmath as mp
mp.mp.dps=180

def pp(limit):
 s=bytearray(b'\1')*(limit+1);s[:2]=b'\0\0'
 for p in range(2,int(math.isqrt(limit))+1):
  if s[p]: s[p*p:limit+1:p]=b'\0'*(((limit-p*p)//p)+1)
 out=[]
 for p in range(2,limit+1):
  if s[p]:
   q=p
   while q<=limit:
    out.append((q,p));q*=p
 return sorted(out)
def geom(n,L):
 w=2*mp.pi*n/L;gs=gcc=gx1=gx2=mp.mpf('0')
 for k in range(1000):
  c=2*k+mp.mpf('.5');e=mp.e**(-c*L);d=c*c+w*w
  gs+=e/d
  if n:gcc+=e*w*w/(c*d)
  gx1+=e*c/d;gx2+=e*(c*c-w*w)/(d*d)
  if e<mp.mpf('1e-120'):break
 return gs,gcc,gx1,gx2
def matrices(c=5):
 L=mp.log(c);S=[mp.mpf(0)]*2;CC=[mp.mpf(0)]*2;XC=[mp.mpf(0)]*2
 for n in (0,1):
  gs,gcc,gx1,gx2=geom(n,L);z=mp.mpf(1)/4+1j*mp.pi*n/L
  psi=mp.digamma(z);psi1=mp.polygamma(1,z)
  if n:S[n]=psi.imag/2-(2*mp.pi*n/L)*gs;CC[n]=-(psi.real-mp.digamma(mp.mpf(1)/4))/2+gcc
  XC[n]=psi1.real/4-L*gx1-gx2
 nodes=(-1,0,1);P=[[0]*3 for _ in nodes];E=[[0]*3 for _ in nodes]
 pref=32*L*mp.sinh(L/4)**2;kappa=mp.log(4*mp.pi*(mp.e**L-1)/(mp.e**L+1))+mp.euler;U=mp.e**(L/2);J=-2*mp.log(U+1)+mp.log(U*U+1)+2*mp.atan(U)+mp.log(2)-mp.pi/2
 for i,n in enumerate(nodes):
  for j,m in enumerate(nodes):
   w02=pref*(L*L-16*mp.pi**2*m*n)/((L*L+16*mp.pi**2*m*m)*(L*L+16*mp.pi**2*n*n))
   if n==m:wr=kappa+2*CC[abs(n)]+J-(2/L)*XC[abs(n)]
   else:
    sn=S[abs(n)]*(1 if n>=0 else -1);sm=S[abs(m)]*(1 if m>=0 else -1)
    wr=(sm-sn)/(mp.pi*(n-m))
   wp=mp.mpf(0)
   for q,p in pp(c):
    wt=mp.log(p)/mp.sqrt(q);y=mp.log(q)
    if n==m:ker=2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    else:ker=(mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))/(mp.pi*(n-m))
    wp+=wt*ker
   P[i][j]=w02-wr;E[i][j]=-wp
 def even(F):
  rt=mp.sqrt(2)
  return [[F[1][1],(F[1][0]+F[1][2])/rt],[(F[0][1]+F[2][1])/rt,(F[0][0]+F[0][2]+F[2][0]+F[2][2])/2]]
 return even(P),even(E)
def endpoint(p):return Fraction(int(p['mantissa']))*Fraction(2)**int(p['exponent'])
def contains(iv,v):return mp.mpf(endpoint(iv['lower']).numerator)/endpoint(iv['lower']).denominator<=v<=mp.mpf(endpoint(iv['upper']).numerator)/endpoint(iv['upper']).denominator

ap=argparse.ArgumentParser();ap.add_argument('certificate',nargs='?',type=Path,default=Path('certificates/c5-N1-p256.json'));ap.add_argument('--output',type=Path,default=Path('results/independent-mpmath-replay.json'));args=ap.parse_args()
doc=json.loads(args.certificate.read_text());P,E=matrices();checks=[]
for name,M in [('P_even',P),('E_even',E)]:
 for i in range(2):
  for j in range(2): checks.append((f'{name}[{i},{j}]',contains(doc['primitive_matrices'][name][i][j],M[i][j]),mp.nstr(M[i][j],40)))
if not all(x[1] for x in checks): raise SystemExit('independent midpoint escaped directed interval')
res={'schema':'riemann.x18505.independent-mpmath-replay.v1','precision_digits':100,'checks':[{'object':a,'inside':b,'midpoint':c} for a,b,c in checks],'verdict':'INDEPENDENT_MPMATH_MIDPOINTS_INSIDE_ALL_DIRECTED_PRIMITIVES'}
args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(res,indent=2,sort_keys=True)+'\n')
print(json.dumps(res,indent=2,sort_keys=True))
