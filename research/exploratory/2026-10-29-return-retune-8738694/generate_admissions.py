"""Generate two isolated Lean admission modules; requires exact pinned PR94 source."""
import argparse, re, sys, textwrap
from pathlib import Path
import sympy as sp

cli=argparse.ArgumentParser()
cli.add_argument('--windows',required=True)
cli.add_argument('--source',required=True,help='Isolated Return source directory; generated files overwrite Admission09 and Admission32')
args=cli.parse_args()
source=Path(args.source)
checker=Path(__file__).with_name('check_admissions.py').read_text()
pre,tail=checker.split('for idx,(dist,C) in enumerate(edges):',1)
body=tail.split('\n if idx==3:',1)[0]
saved=sys.argv;sys.argv=[str(Path(__file__).with_name('check_admissions.py')),'--windows',args.windows]
ns={};exec(compile(pre,'check_admissions.py','exec'),ns)
sys.argv=saved
exec('idx=3\ndist,C=edges[3]\n'+textwrap.dedent(body),ns)
R=sp.Rational

def bernstein(cs,a,b,c,d,n,m):
 assert n>=max(i for i,j,q in cs) and m>=max(j for i,j,q in cs)
 powers={(k,l):sum((q*sp.binomial(i,k)*a**(i-k)*(b-a)**k*sp.binomial(j,l)*c**(j-l)*(d-c)**l for i,j,q in cs if i>=k and j>=l),R(0)) for k in range(n+1) for l in range(m+1)}
 return [[sum((powers[k,l]*sp.binomial(i,k)/sp.binomial(n,k)*sp.binomial(j,l)/sp.binomial(m,l) for k in range(i+1) for l in range(j+1)),R(0)) for j in range(m+1)] for i in range(n+1)]

def show(q):
 q=R(q);return f'({q.p}/{q.q}:ℝ)' if q.q!=1 else f'({q.p}:ℝ)'

cases=[('09','09','weakC7',('51/128','27/64','7/16','1/2'),('397/1000','27/64','43/100','1/2')),
       ('08','32','capC',('3/8','51/128','7/16','1/2'),('39/100','3971/10000','43/100','1/2'))]
for origin,target,branch,oldbox,newbox in cases:
 path=source/'Rows'/f'Admission{origin}.lean'
 text=path.read_text()
 text=text.replace(f'admission{origin}_',f'admission{target}_')
 for old,new in zip(oldbox,newbox):
  if old!=new: text=text.replace(f'({old}:ℝ)',f'({new}:ℝ)')
 aa,bb,cc,dd=map(R,newbox)
 guards=next(g for n,g,m in ns['checks'] if n==branch)
 pattern=rf'theorem (admission{target}_(\d+))_identity .*?admissionGuard \.{branch} δ p \d+ =\s*Record12518109\.Bernstein\.bsum (\d+) (\d+) \([^)]*\) \w+'
 matches=re.findall(pattern,text,re.S)
 assert len(matches)==15,(target,len(matches))
 for key,index,ni,nj in matches:
  i,ni,nj=int(index),int(ni),int(nj)
  bmat=bernstein(guards[i],aa,bb,cc,dd,ni,nj)
  minimum=min(map(min,bmat))/2
  assert minimum>0,(target,i,minimum)
  vals=[[sp.factor((bmat[ii][jj]-minimum)*sp.binomial(ni,ii)*sp.binomial(nj,jj)/(bb-aa)**ni/(dd-cc)**nj) for jj in range(nj+1)] for ii in range(ni+1)]
  assert all(v>=0 for row in vals for v in row)
  x,y=ns['D'],ns['P']
  reconstructed=minimum+sum((vals[ii][jj]*(x-aa)**ii*(bb-x)**(ni-ii)*(y-cc)**jj*(dd-y)**(nj-jj) for ii in range(ni+1) for jj in range(nj+1)),R(0))
  original=sum((q*x**ii*y**jj for ii,jj,q in guards[i]),R(0))
  assert sp.Poly(sp.expand(reconstructed-original),x,y).is_zero,(target,i)
  decl='def '+key+'_coefficients : Fin '+str(ni+1)+' → Fin '+str(nj+1)+' → ℝ := !['+',\n'.join('!['+', '.join(map(show,row))+']' for row in vals)+']\n'
  text,n=re.subn(r'def '+key+r'_coefficients : .*?\ntheorem '+key+r'_identity',lambda m:decl+'theorem '+key+'_identity',text,count=1,flags=re.S);assert n==1
  text,n=re.subn(r'(theorem '+key+r'_identity .*?Record12518109\.Bernstein\.bsum \d+ \d+ )\([^)]*\)',lambda m:m.group(1)+show(minimum),text,count=1,flags=re.S);assert n==1
 output=source/'Rows'/f'Admission{target}.lean';output.write_text(text)
 print('generated',output,'guards',len(matches))
