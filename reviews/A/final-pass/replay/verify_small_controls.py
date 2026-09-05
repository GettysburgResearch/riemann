#!/usr/bin/env python3
"""Independent bounded symbolic controls for F01/F04/F10/F12.
Not an analytic Xi proof or a replay of the large source closures.
"""
import json
from pathlib import Path
from fractions import Fraction as Q
import sympy as s

def need(value, label):
    if not value:
        raise RuntimeError(label)

x,y=s.symbols('x y',real=True)
p=x**4+x**2+1
B=s.cancel((p*s.diff(p,x).subs(x,y)-s.diff(p,x)*p.subs(x,y))/(x-y))
C=s.Matrix(4,4,lambda i,j:s.expand(B).coeff(x,i).coeff(y,j))
expected=s.Matrix([[-2,0,-4,0],[0,-2,0,2],[-4,0,-2,0],[0,2,0,4]])
need(C==expected,'Bezout source matrix')
lam=s.symbols('lambda')
need(s.expand(C.charpoly(lam).as_expr()-(lam-2)*(lam+6)*(lam**2-2*lam-12))==0,'two negative eigenvalues')
need(s.cancel((p/s.diff(p,x,2)).subs(x,0))==Q(1,2),'real residue')
need(s.simplify((p/s.diff(p,x,2)).subs(x,s.I/s.sqrt(2)))==-s.Rational(3,16),'complex residue')
H,X,Y=s.symbols('H X Y',real=True)
f=((X+H)**2+Y**2)*((X+4*H)**2+Y**2)-((X+2*H)**2+Y**2)**2
need(s.expand(f-H*(8*H**2*X+9*H*X**2+9*H*Y**2+2*X**3+2*X*Y**2))==0,'Cauchy determinant pair')
P,R,U,V=s.symbols('P R U V',real=True)
repairs=[(152*P**2*U-40*R*U,152*V*U+568*R*U),
         (932*P**2*R**2*U-32*R**3*U,932*V*R**2*U+3696*R**3*U),
         (P**2*U**3-2*R*U**3,V*U**3+2*R*U**3)]
for a,b in repairs:
    need(s.expand(a-b.subs(V,P**2-4*R))==0,'physical-cone repair')
    need(all(c>=0 for c in s.Poly(b,V,R,U).coeffs()),'physical-cone signs')
for k in range(2,21):
    beta=Q(1,k-1)-Q(1,k)
    need(2*beta==Q(2,k*(k-1)),'labelled Beta allocation')
# Source-blind topological unit block and degree-zero defect are distinct.
A=s.diag(1,1,s.Rational(1,3))
tau=s.symbols('tau')
need(s.expand((s.eye(3)-tau*A).det()-(1-tau)**2*(1-tau/3))==0,'unit factor')
result={
 'verdict':'PASS_A_FINAL_BOUNDED_CONTROLS',
 'named_groups':['Bezout polynomial matrix','Bezout characteristic polynomial','real and complex critical residues','Cauchy determinant gain','three invariant-cone repairs','19 finite Beta allocations','forced topological unit factor'],
 'arithmetic':'exact rational/symbolic',
 'python_optimized_changes_checks':False,
 'analytic_xi_proof':False,
 'rh_proved':False}
print(json.dumps(result,sort_keys=True,indent=2))
