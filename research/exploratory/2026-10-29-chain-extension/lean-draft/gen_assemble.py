#!/usr/bin/env python3
"""Create uncompiled assemblies from adjacent Low/High producer output."""
import re
from pathlib import Path
from gen_low import STEPS, real, qstr, R
root=Path(__file__).parent
for idx,B0,L0,B,L,A,D in STEPS:
 c=R(1,10); a=c-(B0-B)/(L0-L)
 high=(root/f'High{idx}.lean').read_text()
 matches=re.findall(r'\n    \([^\n]+\) (\d+) (\d+) 5 tree\d\d = true',high)
 assert len(matches)==6
 dens=[k for k,_ in matches]; assert len(set(x for _,x in matches))==1
 base=matches[0][1]
 low=f'Low{idx}';hi=f'High{idx}'
 out=['/- Generated candidate assembly; UNCOMPILED and dependent on the Low/High modules. -/',
 f'import Candidate.ChainExtension.{low}',f'import Candidate.ChainExtension.{hi}',
 'set_option autoImplicit false','set_option maxHeartbeats 1000000',
 'namespace QRH.ArviDensity.ChainExtension','noncomputable section',
 'open QRH.ArviDensity QRH.ArviDensity.Hybrid',
 f'theorem markedHigh{idx} : ∃ r : ℝ, 0 < r ∧ ∀ v, 0 ≤ v → v ≤ {real(c)} - cross {real(B0)} {real(L0)} {real(B)} {real(L)} → ∀ ν,',
 f'    dens {real(B0)} {real(L0)} {real(L)} {real(A)} {real(D)} v ≤ ν → ν ≤ 3 / 4 →',
 f'      r ≤ highJ {real(B)} {real(L)} (width {real(B0)} {real(L0)} {real(B)} {real(L)} v) (sel {real(A)} {real(D)} v) ν +',
 f'        QRH.RepeatedMarks.Source.gainC ν {real(B0)} {real(L0)} {real(c)}',
 f'          (width {real(B0)} {real(L0)} {real(B)} {real(L)} v - sel {real(A)} {real(D)} v) (packed {real(A)} {real(D)} v) :=',
 f'  Reflect.high_marked_of_checks {hi}.stepQ (by norm_num [{hi}.stepQ]) (by norm_num [{hi}.stepQ]) (by norm_num [{hi}.stepQ]) (by norm_num [{hi}.stepQ]) (by norm_num [{hi}.stepQ]) (by norm_num [{hi}.stepQ]) (by norm_num [{hi}.stepQ]) ({qstr(a)})',
 f'    (by rw [{low}.cross_eq]; norm_num) (by norm_num) (by norm_num [{hi}.stepQ]) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)',
 f'    (fun v h0 _ => {low}.x_pos v h0) (fun v h0 _ => {low}.E_pos v h0) {low}.unifQLower {low}.unifQUpper {low}.unifRetainedWidth {low}.unifHLower',
 f'    {base} 5 '+ ' '.join(dens),
 '    '+' '.join(f'{hi}.tree{i}{j}' for i in range(2) for j in range(3)),
 '    '+' '.join(f'{hi}.check{i}{j}' for i in range(2) for j in range(3)),
 f'theorem hybridGatesM_Step_{idx} :',
 f'    HybridGatesM (1 / 2 : ℝ) {real(B0)} {real(L0)} {real(c)} {real(B)} {real(L)} {real(c)} {real(A)} {real(D)} where',
 f'  width_pos := by rw [{low}.cross_eq]; norm_num',
 f'  sel_den_pos := fun v h0 _ => {low}.x_pos v h0',
 f'  dens_den_pos := fun v h0 _ => {low}.E_pos v h0',
 '  low_identity := fun v h0 _ =>',
 f'    lowDefect_eq _ _ _ _ _ v ({low}.x_pos v h0).ne\' ({low}.E_pos v h0).ne\'',
 '  low_div_eq := fun v h0 _ =>',
 f'    lowDefect_div_eq _ _ _ _ _ v h0.ne\' ({low}.x_pos v h0.le).ne\' ({low}.E_pos v h0.le).ne\'',
 f'  sel_hasDerivAt := fun v h0 _ => sel_hasDerivAt _ _ v ({low}.x_pos v h0).ne\'']
 fields=[('q_lower','QLower'),('q_upper','QUpper'),('q_floor','QFloor'),('H_lower','HLower'),('retained_cap','RetainedCap'),('retained_width','RetainedWidth'),('low_per_excess_width','LowPerWidth'),('principal_reference','Principal'),('second_reference','SecondRef'),('second_diagonal','SecondDiag'),('reference_upper_positive','RefUpper'),('selection_monotonicity','SelDeriv')]
 out.extend(f'  {f} := {low}.unif{n}' for f,n in fields)
 out += [f'  high_marked := markedHigh{idx}','end','end QRH.ArviDensity.ChainExtension','']
 (root/f'Step_{idx}.lean').write_text('\n'.join(out))
 print('created',idx)
