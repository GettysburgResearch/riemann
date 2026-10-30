#!/usr/bin/env python3
"""Generate candidate single-variable HybridGatesM field certificates.
No Lean evaluation; emitted code is independently subject to elaboration.
"""
import sympy as s
import hashlib
from math import comb
from pathlib import Path
src=Path('/workspace/scratch/pr94-prepared/submission/src/Submissions/arvi_density')
for rel,digest in [('Source/HybridGates.lean','a726377f3252b355f1f2d988190950e6200ca7cf31a3dfd681c041c992304ef1'),
 ('Source/HybridGatesMarked.lean','347e17ea4cd90ab4380cccb6809fbfe356da9335f452f00a7f98a7831b589bd7')]:
 assert hashlib.sha256((src/rel).read_bytes()).hexdigest()==digest, rel
R=s.Rational
v=s.symbols('v')
STEPS=[(130,R(96232839,10**8),R(3853,2000),R(962273544,10**9),R(24073,12500),R(401,1000),R(51,100)),
 (131,R(962273544,10**9),R(24073,12500),R(962272712,10**9),R(192583,100000),R(2,5),R(1,10))]

def qstr(q):
 q=R(q);n,d=int(s.numer(q)),int(s.denom(q))
 return str(n) if d==1 else f'{n} / {d}'
def real(q):return f'({qstr(q)} : ℝ)'
def polyr(q):
 poly=s.Poly(s.expand(q),v)
 return ' + '.join(f'{real(c)} * v ^ {i}' for i in range(poly.degree()+1) if (c:=poly.nth(i))!=0) or '(0 : ℝ)'
def bern(q,w):
 P=s.Poly(s.expand(q),v); degree=max(0,P.degree());assert degree<=2
 return [sum(P.nth(k)*w**k*R(comb(i,k),comb(degree,k)) for k in range(i+1)) for i in range(degree+1)]
def bernterm(q,w):
 arr=bern(q,w);return f"bern{len(arr)-1} "+' '.join(real(x) for x in arr)+' t'
def bernbound(arr,kind):
 n=len(arr)-1
 if n==0:return f'bern0_ge (by norm_num)' if kind=='ge' else f'bern0_le (by norm_num)'
 return f'bern{n}_{kind} ht ht\' '+ ' '.join('(by norm_num)' for _ in arr)

for idx,B0,L0,B,L,A,D in STEPS:
 cross=(B0-B)/(L0-L);wmax=R(1,10)-cross
 X=1+D*v;E=(L0-L)*X+(6*B0-L0)*A;K=R(999,1000)*L0*A;w=cross+v;sel=A*v/X
 vals=[('QLower','gQLower',[B0,L0,L,A,D],K/E-R(1,2)),
 ('QUpper','gQUpper',[B0,L0,L,A,D],R(3,4)-K/E),
 ('QFloor','gQFloor',[R(1,2),B0,L0,L,A,D],K/E-R(1,2)),
 ('HLower','gHLower',[A,D],R(1,10)-6*sel),
 ('RetainedCap','gRetainedCap',[B0,L0,R(1,10),B,L,A,D],R(1,10)*(1-6*sel)-w+sel),
 ('RetainedWidth','gRetainedWidth',[B0,L0,B,L,A,D],w-sel),
 ('LowPerWidth','gLowPerWidth',[L0,A,D],R(1,1000)*L0*A/X),
 ('Principal','gPrincipal',[B0,L0,B,L,A,D],1-B+(L-2)*w-R(9,2)*sel),
 ('SecondRef','gSecondRef',[B0,L0,B,L,A,D],R(1,20)+R(3,2)*(1-B)+(R(3,2)*L-R(5,2))*w-R(9,2)*sel),
 ('SecondDiag','gSecondDiag',[B0,L0,B,L,A,D],1-B+(L-1)*w-4*sel),
 ('RefUpper','gRefUpper',[B0,L0,B,L,A,D],R(1,3)-2*w-3*sel),
 ('SelDeriv','gSelDeriv',[A,D],A/X**2)]
 def call(name,args):return '('+name+' '+' '.join(real(z) for z in args)+')'
 out=['/- Generated candidate UnifPos gate proofs, UNCOMPILED. -/',
 'import Submissions.arvi_density.Source.HybridGatesMarked',
 'set_option autoImplicit false','set_option maxHeartbeats 1000000',
 f'namespace QRH.ArviDensity.ChainExtension.Low{idx}',
 'noncomputable section','open QRH.ArviDensity QRH.ArviDensity.Hybrid',
 f'theorem cross_eq : cross {real(B0)} {real(L0)} {real(B)} {real(L)} = {real(cross)} := by norm_num [cross]',
 f'theorem x_pos (v : ℝ) (h0 : 0 ≤ v) : 0 < 1 + {real(D)} * v := by nlinarith',
 f'theorem E_pos (v : ℝ) (h0 : 0 ≤ v) : 0 < densE {real(B0)} {real(L0)} {real(L)} {real(A)} {real(D)} v := by',
 '  unfold densE; nlinarith']
 for name,gn,args,expr in vals:
  n,d=s.fraction(s.cancel(expr));n=s.expand(n);d=s.expand(d)
  if d.subs(v,0)<0:n=-n;d=-d
  nb,db=bern(n,wmax),bern(d,wmax)
  assert min(nb)>0,(idx,name,'n',nb)
  assert min(db)>0,(idx,name,'d',db)
  m,M=min(nb),max(db);g=call(gn,args)
  qgate=name in ('QLower','QUpper','QFloor')
  hden='he' if qgate else ('(pow_ne_zero 2 hx)' if name=='SelDeriv' else 'hx')
  hmul='he' if qgate else 'hx'
  mulcall=f'({gn}_mul '+ ' '.join(real(z) for z in args)+f' v {hmul})'
  out += [f'\ndef n{name} (v : ℝ) : ℝ := {polyr(n)}',f'def d{name} (v : ℝ) : ℝ := {polyr(d)}',
   f'theorem cleared{name} (v : ℝ) (h0 : 0 ≤ v) : {g} v * d{name} v = n{name} v := by',
   '  have hx := (x_pos v h0).ne\'','  have he := (E_pos v h0).ne\'',
   f'  refine mul_eq_of_cleared {hden} {mulcall} ?_',
   f'  simp only [n{name}, d{name}, densE, densK, width, cross_eq]',
   '  ring',
   f'theorem n{name}_bern (t : ℝ) : n{name} ({real(wmax)} * t) = {bernterm(n,wmax)} := by',
   f'  unfold n{name} bern{len(nb)-1}; ring',
   f'theorem d{name}_bern (t : ℝ) : d{name} ({real(wmax)} * t) = {bernterm(d,wmax)} := by',
   f'  unfold d{name} bern{len(db)-1}; ring',
   f'theorem unif{name} : UnifPos {g} 0 ((1 / 10 : ℝ) - cross {real(B0)} {real(L0)} {real(B)} {real(L)}) := by',
   f'  refine ⟨{real(m/M)}, by norm_num, fun v h0 h1 => ?_⟩',
   '  rw [cross_eq] at h1',
   f'  have hb := box_lower (g := {g}) (n := n{name}) (d := d{name})',
   f'    (lo := (0 : ℝ)) (hi := {real(wmax)}) (m := {real(m)}) (M := {real(M)}) (by norm_num) (by norm_num)',
   f'    (fun v h0 _ => cleared{name} v (by linarith))',
   '    (fun t ht ht\' => by',f'      simpa only [zero_add, sub_zero] using (show {real(m)} ≤ n{name} ({real(wmax)} * t) by',
   f'        rw [n{name}_bern]; exact {bernbound(nb,"ge")}))',
   '    (fun t ht ht\' => by',f'      have hb : {real(min(db))} ≤ d{name} ({real(wmax)} * t) := by',
   f'        rw [d{name}_bern]; exact {bernbound(db,"ge")}',
   f'      have hd : (0 : ℝ) < d{name} ({real(wmax)} * t) := lt_of_lt_of_le (by norm_num) hb',
   '      simpa only [zero_add, sub_zero] using hd)',
   '    (fun t ht ht\' => by',f'      simpa only [zero_add, sub_zero] using (show d{name} ({real(wmax)} * t) ≤ {real(M)} by',
   f'        rw [d{name}_bern]; exact {bernbound(db,"le")}))',
   '    v h0 (by linarith)', '  exact le_trans (by norm_num) hb']
 out+=['end',f'end QRH.ArviDensity.ChainExtension.Low{idx}','']
 (Path(__file__).parent/f'Low{idx}.lean').write_text('\n'.join(out))
 print('step',idx,'generated',len(vals),'gate candidates')
