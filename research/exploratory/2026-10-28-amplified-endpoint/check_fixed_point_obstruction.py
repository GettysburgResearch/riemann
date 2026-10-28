import sympy as s
r=s.Rational
B=r(87488664,100000000);l=4*(r(11,12)-B);k=2*B-1;c=1/(3*k);b=s.symbols('b');h=(1+b+3*l)/2;ly=(1+b-l)/2;x=r(1,2)
def E(d):
 D=3-(1+2*c)*x;P=(2-2*c*x)*(1-x);J=(r(5,6)-d)*D+d*P;R=1-d+(r(5,6)-d)*d*P/(2*J);C=-r(1,4)+b/6+5*l/4
 return s.cancel(C+d/2+d*x*(l+c*(h/4-ly/2))-3*h*(1-R)/4)
e1=E(r(46934,100000));e2=E(r(46935,100000));a1=e1.subs(b,0);a2=e2.subs(b,0);t1=s.diff(e1,b);t2=s.diff(e2,b);w1=-t2/(t1-t2);w2=t1/(t1-t2);mix=s.factor(w1*a1+w2*a2)
print('l',l, 'k',k,'signs', t1>0,t2<0, 'weights',w1>0,w2>0,'sum',w1+w2, 'mix positive',mix>0,'mix approx',float(mix));print('ratio',mix)

assert t1 > 0 and t2 < 0 and w1 > 0 and w2 > 0 and w1+w2 == 1 and mix > 0
print('all assertions passed')
