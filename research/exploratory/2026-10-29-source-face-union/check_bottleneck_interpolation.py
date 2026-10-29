"""Exact C-branch comparison of the two recorded count faces at one detector point."""
import sympy as s
R=s.Rational;t=s.symbols('t',real=True);delta=R(223,500);p=R(1,2);v=R(5,6)-delta
B=R(96232839,10**8)+t*(R(97260493237265,10**14)-R(96232839,10**8))
L=R(3853,2000)+t*(R(21152005,10**7)-R(3853,2000))
dd=3-p-4*p/L; aa=2-4*p/L; U=(1-p)*(1-2*p*B/L); J=v*dd+delta*(1-p)*aa
rate=s.factor(1-delta+v*delta*U/J)
expected=23*(212955579632671607*t+1195464006788200000)/(5000000000*(1601312443*t+9024279000))
derivative=s.factor(s.diff(rate,t));want=R(171561047617394341596319,5000000)/(1601312443*t+9024279000)**2
assert s.factor(rate-expected)==0 and s.factor(derivative-want)==0
print('count:',rate);print('derivative:',derivative)
