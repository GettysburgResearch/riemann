#!/usr/bin/env python3
"""Produce proposed full-window guards; target Return overlay, not PR94."""
from pathlib import Path
import hashlib
import argparse
from math import comb
import sympy as s
src=Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density/Return')
for rel,digest in [('Formulas.lean','e7dfed2c335372dde5a609ec2b53bf268d6fe7c40807bdb7ee83c5d7f3f3216b'),
 ('Constants.lean','96f2a770b68bc4d3ba34e896995514c040315dbc8584e19dbfe479dced8ce4b7')]:
 assert hashlib.sha256((src/rel).read_bytes()).hexdigest()==digest,rel
R=s.Rational
D,P=s.symbols('D P')
parser=argparse.ArgumentParser()
parser.add_argument('--window',choices=('09','32','33'),default='33')
idx=parser.parse_args().window
spec={'09':('weakC7',R(96232839,10**8)-R(7,4000),R(3853,2000),False,R(397,1000),R(27,64),R(43,100)),
 '32':('capC',R(96232839,10**8),R(3853,2000),True,R(39,100),R(3971,10000),R(43,100)),
 '33':('C131',R(962272712,10**9),R(192583,100000),False,R(11,25),R(9,20),R(49,100))}
branch,B,L,is_cap,a,b,c=spec[idx];e=R(1,2);cap=R(9999,100000)
eps=R(1,10**7);sm=R(3,100);mm=R(377,1000);nat=(1-R(9,2)*sm)/2
V=R(5,6)-D; z=cap-eps
dd=3-P if is_cap else 3-P-4*P/L
aa=2 if is_cap else 2-4*P/L
c0=1-2*P*z if is_cap else 1-2*P*B/L
zz=2*P*z if is_cap else 2*P*B/L
U=(1-P)*c0;J=V*dd+D*(1-P)*aa;T=J+D*U;rn=aa*T+(zz-P)*J;mn=dd*T-rn;dj=dd*J
low=mm+eps if is_cap else max(mm+eps,(B-L*(cap-eps))/2+eps)
high=min(R(11,25)-eps,nat-eps,(B-L*(z if is_cap else sm+eps))/2-eps)
derd=-1 if is_cap else -1-4/L;dera=0 if is_cap else -4/L;derc=-2*z if is_cap else -2*B/L
deru=-c0+(1-P)*derc;derj=V*derd+D*(-aa+(1-P)*dera);N=(1-D)*J+V*D*U
guards=[dd,aa,c0,J,T-J,R(12499,10000)*J-T,rn-R(23,37)*dj,dj-rn,mn-low*dj,high*dj-mn,N-(1-2*D*nat-2*D*P*sm)*J,U*derj-deru*J,R(11,25)-nat-eps,B-2*nat-L*(sm+eps)-2*eps,(z-sm-eps)*dj if is_cap else s.Integer(1)]
x,y=s.symbols('x y')
def qstr(q):
 q=R(q);n,d=int(s.numer(q)),int(s.denom(q));return str(n) if d==1 else f'{n}/{d}'
def real(q):return f'({qstr(q)}:ℝ)'
def compute(expr):
 poly=s.Poly(s.expand(s.sympify(expr).subs({D:a+(b-a)*x,P:c+(e-c)*y})),x,y)
 n=max(0,poly.degree(x));m=max(0,poly.degree(y))
 bs={(i,j):sum(poly.nth(k,l)*R(comb(i,k),comb(n,k))*R(comb(j,l),comb(m,l)) for k in range(i+1) for l in range(j+1)) for i in range(n+1) for j in range(m+1)}
 floor=min(bs.values())/2;assert floor>0
 cs={(i,j):s.factor((bs[i,j]-floor)*comb(n,i)*comb(m,j)/((b-a)**n*(e-c)**m)) for i in range(n+1) for j in range(m+1)}
 assert min(cs.values())>=0
 return n,m,floor,cs
unfold='admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm'
out=['/- Generated candidate; uncompiled; requires the count-source overlay. -/',
 'import Submissions.arvi_density.Return.Formulas','set_option autoImplicit false','set_option linter.unnecessarySeqFocus false','namespace QRH.ArviDensity.Return','noncomputable section']
for k,g in enumerate(guards):
 n,m,f,co=compute(g)
 matrix='!['+', '.join('!['+', '.join(real(co[i,j]) for j in range(m+1))+']' for i in range(n+1))+']'
 name=f'admission{idx}_{k:02}'
 out += [f'def {name}_coefficients : Fin {n+1} → Fin {m+1} → ℝ := {matrix}',
 f'theorem {name}_identity (δ p : ℝ) : admissionGuard .{branch} δ p {k} =',
 f' Record12518109.Bernstein.bsum {n} {m} {real(f)} {name}_coefficients {real(a)} {real(b)} {real(c)} {real(e)} δ p := by',
 f' norm_num [{unfold},{name}_coefficients,Fin.sum_univ_succ] <;> ring',
 f'theorem {name}_pos {{δ p : ℝ}} (hδ : δ ∈ Set.Icc {real(a)} {real(b)})',
 f' (hp : p ∈ Set.Icc {real(c)} {real(e)}) : 0 < admissionGuard .{branch} δ p {k} := by',
 f' rw [{name}_identity]',
 ' apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp',
 ' intro i j',
 f' fin_cases i <;> fin_cases j <;> norm_num [{name}_coefficients]']
out += [f'theorem admission{idx}_all {{δ p : ℝ}} (hδ : δ ∈ Set.Icc {real(a)} {real(b)})',
 f' (hp : p ∈ Set.Icc {real(c)} {real(e)}) (j : Fin 15) : 0 < admissionGuard .{branch} δ p j := by',
 ' fin_cases j']
out += [f' · exact admission{idx}_{k:02}_pos hδ hp' for k in range(15)]
out += ['end','end QRH.ArviDensity.Return','']
path=Path(__file__).parent/f'Admission{idx}.lean';path.write_text('\n'.join(out))
print('Generated',path,'15 strict Bernstein certificates')
