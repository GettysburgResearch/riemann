#!/usr/bin/env python3
"""Complete fresh mixed-gate replay followed by exact trace-priced completion."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as Q
from flint import arb,ctx
import enclose_length_robust_mixed as mixed
from enclose_analytic_upper import require

MIXED='38ef6a1f5125adf72f037d625222eccae509f4a146037361ca02dd20f1e1a6f3'
LEMMA='350e7440de1363e02dfe075e2f204af08170471bcadd7ae7750de67de27df062'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rational(x):return arb(x.numerator)/x.denominator

def enclose(mixed_path,residual,baseline):
    here=Path(__file__).parent
    require(sha(here/'enclose_length_robust_mixed.py')==MIXED,'frozen complete physical mixed checker')
    require(sha(here/'eta-review/TRACE_PRICED_COMPLETION.md')==LEMMA,'frozen reviewed generic trace-priced lemma')
    saved=json.loads(mixed_path.read_text());fresh=mixed.enclose(residual,baseline)
    require(saved==fresh,'entire fresh full mixed gate semantic replay before trace extraction')
    ctx.prec=256;epsilon=Q(fresh['epsilon_exact'])
    require(epsilon==Q(1,20000000000),'fixed complete epsilon5e-11 gate')
    M=Q(1,2500);K=Q(57,100);kappa=Q(1,2);cap=Q(11,1000)
    require(arb(fresh['dual_trace_ball'])<rational(M),'complete positive dual trace cap1/2500')
    require(arb(fresh['synthesis_trace_ball'])<rational(K),'complete primitive synthesis trace cap57/100')
    require(fresh['primitive_gap_exact']=='1/2','independently retained complete positive-sector gap')
    require(M*K*kappa<cap**2,'exact radical upper bound')
    denominator=epsilon+M+K*kappa+2*cap;delta=Q(8,5)*epsilon
    require(denominator<Q(5,16) and delta*denominator<=epsilon*kappa,'exact full trace-priced reserve')
    require(delta==Q(1,12500000000),'exact physical primitive reserve')
    return {'status':'DIRECTED_TRACE_PRICED_PHYSICAL_LENGTH_POSITIVITY_ACCEPT',
      'native_bound':'q_ell(h,h)>=||G_ell h||²/12500000000 for every complex native h and every0<ell<=21/20',
      'exact_length':'21/20','epsilon_exact':str(epsilon),'M_exact':str(M),'K_exact':str(K),'kappa_exact':str(kappa),
      'radical_upper_exact':str(cap),'denominator_upper_exact':str(denominator),'delta_exact':str(delta),
      'complete_dual_trace_ball':fresh['dual_trace_ball'],'complete_synthesis_trace_ball':fresh['synthesis_trace_ball'],
      'mixed_receipt_sha256':sha(mixed_path),'R_receipt_sha256':sha(residual),'baseline_receipt_sha256':sha(baseline),
      'fresh_entire_mixed_gate_replayed':True,'new_R_integration_performed':False,
      'frozen_mixed_checker_sha256':MIXED,'frozen_generic_completion_lemma_sha256':LEMMA,'producer_sha256':sha(Path(__file__)),
      'not_proved':['independent second R integration','native L2 spectral gap','sign atlog3','all-window positivity','RH']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mixed',type=Path);p.add_argument('residual',type=Path);p.add_argument('baseline',type=Path);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=enclose(a.mixed,a.residual,a.baseline);a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
