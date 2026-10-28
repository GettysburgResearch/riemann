#!/usr/bin/env python3
"""Exact check of the admissibility screen of Xu--Sang arXiv:2610.15291v2, 6.2.

Conditional on that preprint's analytic propositions. Requires SymPy.
"""
from sympy import Rational as Q, symbols, Poly, cancel, factor

k=Q(29991,40000); b=Q(17307,200000); ell=Q(4178001,25000000)
g=Q(1,10**9); zeta=Q(1,10**11); gs=Q(1,10**10)
a=Q(5,6); c=1/(3*k)
lx=(1-b-ell)/2; ly=(1+b-ell)/2; h=(1+b+3*ell)/2
bound=Q(11,12)-ell/4
C0=-Q(1,4)+b/6+5*ell/4
Asm=Q(1,2)+ell/2*(Q(1,2)+2*ell/h)-h/2
checks={
'b positive':b>0, 'ell interval':Q(1,6)<=ell<=Q(1,5),
'k interval':Q(29991,40000)<=k<=Q(3,4),'B > 87/100':bound>Q(87,100),
'lx > ell':lx>ell,'ly-ell > 11b/6':ly-ell>11*b/6,
'6k ell > 3/4':6*k*ell>Q(3,4),'ell/h < 1/(6k)':ell/h<1/(6*k),
'ell/(h+zeta) > 21/100':ell/(h+zeta)>Q(21,100),
'h/2 < ly < 1/2':h/2<ly<Q(1,2),
'0 < gs < 1/1000':0<gs<Q(1,1000),
'0 < 2zeta < 1/1000':0<2*zeta<Q(1,1000),
'g-2zeta > gs':g-2*zeta>gs,
'C0 < -1/250':C0<-Q(1,250),
'C0+Asm/8 < -1/250':C0+Asm/8<-Q(1,250),
'floor < -1/100':C0+(Q(1,2)+3*ell/2)/50<-Q(1,100),
'small rows < -1/20':h*(Q(17,50)-Q(1,6))-ly/2+Q(2,100)<-Q(1,20),
'licensed by B0':(1+k)/2==Q(69991,80000),
'improves B1':bound<Q(8748867,10000000),
}
d,x,y=symbols('d x y',real=True)
D=3-(1+2*c)*x; P=(2-2*c*x)*(1-x); J=(a-d)*D+d*P
R=1-d+(a-d)*d*P/(2*J)
E=C0+d/2+d*x*(ell+c*(h/4-ly/2))-3*h/4*(1-R)
# For 0<=x<=1/2, D,P>0; for 1/8<=d<=5/6,
# a-d>=0 and d>0, so J>0. Complete the square globally in d.
poly=Poly(cancel(J*(-E-g)).subs(x,Q(1,2)-y),d)
assert poly.degree()==2
A,B,C=poly.all_coeffs()
assert all(v>0 for v in Poly(A,y).all_coeffs())
assert all(v>0 for v in Poly(4*A*C-B**2,y).all_coeffs())
checks['continuous endpoint bound']=True
for label,passed in checks.items():
 print(label, bool(passed))
 assert passed,label
print('boundary:',bound,'=',float(bound))
print('improvement:',Q(8748867,10000000)-bound)
