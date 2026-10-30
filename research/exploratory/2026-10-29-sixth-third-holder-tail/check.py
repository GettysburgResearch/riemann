from fractions import Fraction as F
import itertools

def gen(p):
 p=F(p); z=F(0)
 A=[(1/(2*p),z,z,z,F(1,2)),(1/(4*p),z,z,z,F(1))]
 x=(p-2)/(2*p)
 T2=[(x,x,z,z,z),(2*x,2*x,x,-x,3*x)] if p>2 else [(z,z,z,z,z)]
 y=1/(2*p)
 T4=[(y,z,z,z,z),(z,z,z,2*y,-6*y),(F(5,6)*y,z,z,F(2,3)*y,-2*y),(F(1,3)*y,z,z,F(5,3)*y,-5*y)]
 for i,j,k in itertools.product(range(2),range(len(T2)),range(4)):
  a,u,v,w,h=[A[i][q]+T2[j][q]+T4[k][q] for q in range(5)]
  if h<1:
   g=2*(1-h); q=3+g
   a,u,v,w=[(q0*g+3*q1)/q for q0,q1 in zip((F(2),F(2),F(1),F(-1)),(2*a,2*u,2*v,2*w))]
  else:w=2*w+F(2,3)*(h-1);a*=2;u*=2;v*=2
  const=F(1,30)+F(6,5)*w;dd=F(2,3)-w;kk=-F(5,6)+u+v;bb=a-F(1,6);gg=v-w
  e=-F(1,2)+(v-w)/2
  maxc=max(0,gg,dd,F(5,11)*(dd+kk))
  yield f'{i}{j}{k}',const,maxc,bb,e,h

for p in [3]:
 rows=list(gen(p)); print('\n p',p)
 for C,E in [(F(7,50),F(21,20)),(F(1925877,15625000),F(19949123,18750000))]:
  cut=[((E-a-c*C)/b,lab) for lab,a,c,b,e,h in rows if b>0]
  m=min(cut)
  print('C',str(C),'min',str(m[0]),float(m[0]),m[1])
 print('max e',max(e for _,a,c,b,e,h in rows),'rows',len(rows))
