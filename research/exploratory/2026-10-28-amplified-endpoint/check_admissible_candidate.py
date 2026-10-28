import sympy as s
r=s.Rational
b=r(17307,200000); l=r(4178001,25000000); k=r(29991,40000); alpha=r(5,6); c=1/(3*k); h=(1+b+3*l)/2; lx=(1-b-l)/2;ly=(1+b-l)/2; B=r(11,12)-l/4
D,y=s.symbols('d y',real=True);x=r(1,2)-y
Dx=3-(1+2*c)*x;P=(2-2*c*x)*(1-x);J=(alpha-D)*Dx+D*P
R=1-D+(alpha-D)*D*P/(2*J)
C=-r(1,4)+b/6+5*l/4
E=C+D/2+D*x*(l+c*(h/4-ly/2))-3*h*(1-R)/4
for g in [r(1,10**10),r(1,10**9),r(1,10**8),r(1,10**7)]:
 Q=s.Poly(s.cancel(J*(-E-g)),D)
 A,Bb,Cc=[s.factor(Q.coeff_monomial(D**n)) for n in [2,1,0]]
 disc=s.factor(4*A*Cc-Bb**2)
 pa=s.Poly(A,y);pd=s.Poly(disc,y)
 print('g',g,'a-pos',all(i>0 for i in pa.all_coeffs()),'disc-pos',all(i>0 for i in pd.all_coeffs()),'disc const',float(pd.eval(0)))
print('boundary',B,float(B),'h',float(h))
z=r(1,10**12); gs=r(1,10**11);g=r(1,10**9)
Asm=r(1,2)+(l/2)*(r(1,2)+2*l/h)-h/2
checks={'b>0':b>0,'l>=1/6':l>=r(1,6),'l<=1/5':l<=r(1,5),'k range':r(29991,40000)<=k<=r(3,4),'B>.87':B>r(87,100),'lx>l':lx>l,'ly-l>11b/6':ly-l>11*b/6,'6kl>3/4':6*k*l>r(3,4),'l/h<1/6k':l/h<1/(6*k),'l/(h+z)>.21':l/(h+z)>r(21,100),'h/2<ly':h/2<ly,'ly<1/2':ly<r(1,2),'g-2z>gstar':g-2*z>gs,'gstar<1/1000':gs<r(1,1000),'2z<1/1000':2*z<r(1,1000),'small':max(C,C+Asm/8)<-r(1,250),'floor':C+(r(1,2)+3*l/2)/50<-r(1,100),'smallrows':h*(r(17,50)-r(1,6))-ly/2+r(2,100)<-r(1,20)}
for x,v in checks.items():print(x,v)
assert all(checks.values())
Q=s.Poly(s.cancel(J*(-E-r(1,10**9))),D)
A,Bb,Cc=[s.factor(Q.coeff_monomial(D**n)) for n in [2,1,0]]
assert Q.degree() == 2 and all(v > 0 for v in s.Poly(A,y).all_coeffs())
assert all(v > 0 for v in s.Poly(4*A*Cc-Bb**2,y).all_coeffs())
assert B == r(262465997,300000000)
print('all assertions passed')
