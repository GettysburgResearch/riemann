"""Exact two-bin obstruction for the endpoint expression; see README."""
import sympy as s
D,p,b=s.symbols('D p b'); R=s.Rational
x=R(1,2); A=R(5,6); Dx=3-17*x/9; Px=(2-8*x/9)*(1-x); J=(A-D)*Dx+D*Px
C=1-D+(A-D)*D*Px/(2*J)
ell=R(1,6)+p; ly=(1-ell+b)/2; h=(1+3*ell+b)/2; B=R(7,8)-p/4
E=(1+D)/2-B+h*(R(17,50)-R(1,6))-(1+D)*ly/2-ell/2+D*x*ell+h*(C+D/2-R(17,50))
d1=R(38858371,10**8);d2=R(38858372,10**8)
E1=s.expand(E.subs(D,d1));E2=s.expand(E.subs(D,d2));t1=E1.coeff(b);t2=E2.coeff(b);print('t signs',t1>0,t2<0)
w1=-t2/(t1-t2);w2=t1/(t1-t2);F=s.factor(w1*E1+w2*E2);print('weights positive',w1>0,w2>0,'sum',w1+w2, 'b canceled',b not in F.free_symbols)
S=s.expand(F).coeff(p); pstar=s.factor(-F.subs(p,0)/S);target=R(4562748652437347,26570739037370607802);print('S positive',S>0, 'pstar equals stated',pstar==target)
chosen=R(214651,1250000000);diff=(pstar-chosen)/4;print('0 < (pstar-p)/4 < 10^-12:',0<diff<R(1,10**12), 'exact',diff,'approx',float(diff))

assert t1 > 0 and t2 < 0
assert w1 > 0 and w2 > 0 and w1 + w2 == 1
assert b not in F.free_symbols and S > 0 and pstar == target
assert 0 < diff < R(1, 10**12)
