#!/usr/bin/env python3
"""One frozen physical R, stronger exact source-line mixture, full fresh replay."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction as Q
from flint import arb, arb_mat, ctx
import enclose_length_robust_weighted as weighted
import enclose_length_primitive as primitive
import check_supporting_line_interpolation as interpolation
from physical_length_source import OLD
from enclose_analytic_upper import require
from directed_congruence_gate import gate

FROZEN = {
 'enclose_length_robust_weighted.py':'9c774a1de5b0d0771764ffeeb7e56bfbf20620774f5a00466c3cd750a7f891d7',
 'directed_congruence_gate.py':'e4e34814942001d1576f1c5d8a798d1c0fd968790becf9b829503173a4bf1f54',
 'enclose_length_weighted.py':'aed3e21e0784f387fb371b871389514c60671bd4f29449b07791d97ab9b77b16',
 'enclose_length_primitive.py':'2fc80bfd130ea59bb413209cd8dd092a71e4de80cc7f387c14778626cc1e560a',
 'check_supporting_line_interpolation.py':'daa6fad4267e1351566ebde45e9e1c4367742ca148b2d1f35e3f0a58ce8fc8d4',
}
LINES = {
 'check_coercivity.py':'921c74c4b0659c8f6c0d1602f16f218e71219b64e31250b457cce92a808f0f87',
 'check_codimension14.py':'4263b37ca623e74aa8312d10b8bb98c2b75e72e61f7e501bd7329ea426b58351',
 'check_codimension8_phase.py':'11f1662311aaa5cbd0f274790069c1cb88b49ff591c4d500c6a63cdbdac6e60f',
 'check_window_family_log3.py':'7bbef766664319616bf3b55ca653e07e925a1e699cdcaa930a127485b3bfd592',
}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def matrix(rows): return arb_mat([[arb(x) for x in row] for row in rows])
def rational(x): return arb(x.numerator)/x.denominator

def enclose(residual, baseline):
    here=Path(__file__).parent
    for name,h in FROZEN.items(): require(sha(here/name)==h,('frozen physical dependency',name))
    for name,h in LINES.items(): require(sha(OLD/name)==h,('frozen exact full source line',name))
    saved=json.loads(baseline.read_text()); fresh=weighted.enclose(residual)
    require(saved==fresh,'complete fresh baseline source/trial/moment/coverage replay')
    lines=interpolation.run();ctx.prec=256
    L=arb(21)/20;b=arb(3)/2;last=128;dim=10
    theta=Q(39,40);alpha=Q(4,5)+theta/2;constant=244+466*theta
    require(alpha==Q(103,80) and constant==Q(13967,20),'fixed exact selected line')
    alpha_ball=rational(alpha);constant_ball=rational(constant)
    def weight(n): return alpha_ball-constant_ball*L**2/(n*arb.pi())**2
    require(weight(8)>0,'entire physical cosine weight family positive')
    tail=1/weight(last+1)
    R=matrix(json.loads(residual.read_text())['R_matrix_balls'])
    U=matrix(fresh['fresh_U_matrix_balls']);a=matrix(fresh['protected_high_cosine_moment_balls'])
    require(R.nrows()==R.ncols()==dim and a.nrows()==last-7 and a.ncols()==dim,'complete unchanged native residual/moments')
    cost=b*tail*R
    for n in range(8,last+1):
        delta=1/weight(n)-tail
        require(delta>0,'positive complete finite inverse-weight correction')
        for i in range(dim):
            for j in range(dim):cost[i,j]+=2*b/L*delta*a[n-8,i]*a[n-8,j]
    lower=(U-cost+(U-cost).transpose())/2
    epsilon=Q(1,20000000000)
    congruence=gate(lower,rational(epsilon))
    trace=sum((cost[i,i] for i in range(dim)),arb(0));require(trace<1,'complete positive mixed dual trace below M1')
    norms,synthesis=primitive.synthesis(fresh);require(synthesis<1,'full exact physical primitive synthesis trace below K1')
    young_theta=epsilon/(2+epsilon);kappa=Q(1,2)
    delta=min(epsilon/6,young_theta*kappa/2)
    require(delta==Q(1,160000000004),'exact complete primitive reserve')
    return {
      'status':'DIRECTED_PHYSICAL_LENGTH_ROBUST_MIXED_PRIMITIVE_ACCEPT',
      'native_bound':'q_ell(h,h)>=||G_ell h||²/160000000004 for every complex native h and every0<ell<=21/20',
      'exact_length':'21/20','theta_exact':str(theta),'alpha_exact':str(alpha),'constant_exact':str(constant),
      'R_receipt_sha256':sha(residual),'baseline_weighted_receipt_sha256':sha(baseline),
      'fresh_full_baseline_replay_performed':True,'new_R_integration_performed':False,
      'physical_parseval_factor':'2/L','last_cosine_mode':128,'lambda8_ball':weight(8).str(65,more=True),
      'tail_inverse_weight_ball':tail.str(65,more=True),'epsilon_exact':str(epsilon),
      'mixed_weighted_lower_matrix_balls':weighted.balls(lower),'directed_congruence_certificate':congruence,
      'dual_trace_ball':trace.str(65,more=True),'M_exact':'1','K_exact':'1','primitive_gap_exact':'1/2',
      'exact_Gz_squared_norm_balls':[v.str(65,more=True) for v in norms],'synthesis_trace_ball':synthesis.str(65,more=True),
      'young_theta_exact':str(young_theta),'delta_exact':str(delta),'full_source_line_replay':lines,
      'frozen_dependencies':FROZEN,'frozen_source_lines':LINES,'producer_sha256':sha(Path(__file__)),
      'not_proved':['independent second fullR integration','native L2 spectral gap','sign atlog3','all-window positivity','RH'],
    }

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('residual',type=Path);p.add_argument('baseline',type=Path);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();result=enclose(a.residual,a.baseline);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['mixed_weighted_lower_matrix_balls','directed_congruence_certificate','exact_Gz_squared_norm_balls','full_source_line_replay']},indent=2))
