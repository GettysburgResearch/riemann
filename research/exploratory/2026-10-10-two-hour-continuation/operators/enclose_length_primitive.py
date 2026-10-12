#!/usr/bin/env python3
"""Fresh weighted replay and exact physical primitive synthesis atL21/20."""
import argparse,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,acb,ctx
from physical_length_source import OLD
from enclose_analytic_upper import require,f,fp
import enclose_length_weighted as weighted

RATES=[Q(1,2),Q(-1,2),Q(1,2),Q(-1,2),Q(3,2),Q(-3,2)]
POWERS=[0,0,1,1,0,0]
WEIGHTED='aed3e21e0784f387fb371b871389514c60671bd4f29449b07791d97ab9b77b16'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def moment(rate,power,L):
    if rate==0:return L**(power+1)/(power+1)
    z=acb(arb(rate.numerator)/rate.denominator*L)
    if power==0:return L*f(z).real
    if power==1:return L**2*fp(z).real
    require(power==2,'complete degree-two physical product moments')
    return L**3*((z.exp()*(z*z-2*z+2)-2)/(z*z*z)).real

def synthesis(data):
    L=arb(21)/20;m=7;trial=100;dim=10;coef=data['exact_trial_z_coefficients_balls']
    require(len(coef)==110 and all(len(r)==10 for r in coef),'complete exact physical trial inventory')
    soft_gram=[[moment(RATES[i]+RATES[j],POWERS[i]+POWERS[j],L) for j in range(6)] for i in range(6)]
    trig=[]
    for n in range(1,108):
        row=[]
        for rate,power in zip(RATES,POWERS):
            z=acb(arb(rate.numerator)/rate.denominator*L,arb.pi()*n)
            row.append((L*f(z) if power==0 else L**2*fp(z)).real)
        trig.append(row)
    norms=[]
    for i in range(10):
        soft=[arb(0) for _ in range(6)];cosine=[arb(0) for _ in range(107)]
        for row in range(110):
            coefficient=arb(coef[row][i])
            if row<m or row>=dim:
                n=row+1 if row<m else m+1+row-dim;nu=arb.pi()*n/L;scale=nu/(nu*nu+arb(1)/4)
                soft[0]+=coefficient*scale/2;soft[1]+=coefficient*scale/2;cosine[n-1]-=coefficient*scale
            elif row==m:
                soft[0]+=coefficient/2;soft[1]-=coefficient/2;soft[2]+=coefficient/2
            elif row==m+1:
                soft[0]+=coefficient/2;soft[1]-=coefficient/2;soft[3]+=coefficient/2
            else:
                soft[0]-=coefficient/8;soft[1]+=coefficient/8;soft[4]+=3*coefficient/8;soft[5]-=3*coefficient/8
        squared=sum((soft[j]*soft[k]*soft_gram[j][k] for j in range(6) for k in range(6)),arb(0))
        squared+=L/2*sum((x*x for x in cosine),arb(0))
        squared+=2*sum((soft[j]*cosine[n]*trig[n][j] for n in range(107) for j in range(6)),arb(0))
        require(squared.is_finite() and squared>0,'exact physical primitive norm positive');norms.append(squared)
    return norms,sum(norms,arb(0))

def enclose(weighted_path,residual):
    require(sha(Path(__file__).with_name('enclose_length_weighted.py'))==WEIGHTED,'frozen full weighted checker')
    saved=json.loads(weighted_path.read_text());fresh=weighted.enclose(residual)
    require(saved==fresh,'full fresh weighted receipt semantic replay before extraction')
    ctx.prec=256
    traceB=sum((arb(fresh['fresh_U_matrix_balls'][i][i])-arb(fresh['weighted_lower_matrix_balls'][i][i]) for i in range(10)),arb(0))
    require(traceB.is_finite() and traceB<1,'positive dual matrix trace belowM1')
    norms,total=synthesis(fresh);require(total<1,'exact primitive synthesis trace belowK1')
    epsilon=Q(1,10**11);M=Q(1);K=Q(1);kappa=Q(1,2);theta=epsilon/(2*M+epsilon)
    delta=min(epsilon/(2*(1+2*K)),theta*kappa/2)
    require(delta==Q(1,800000000004),'exact physical primitive reserve')
    return {'status':'DIRECTED_EXPLICIT_LENGTH_PRIMITIVE_POSITIVITY_ACCEPT',
      'native_bound':'q_ell(h,h)>=||G_ell h||²/800000000004 for every complex native h and every0<ell<=21/20',
      'exact_length':'21/20','weighted_receipt_sha256':sha(weighted_path),'R_receipt_sha256':sha(residual),
      'fresh_full_weighted_replay_performed':True,'new_R_integration_performed':False,
      'epsilon_exact':str(epsilon),'dual_matrix_trace_ball':traceB.str(65,more=True),'M_exact':'1',
      'exact_Gz_squared_norm_balls':[x.str(65,more=True) for x in norms],
      'synthesis_trace_ball':total.str(65,more=True),'K_exact':'1','primitive_gap_exact':'1/2',
      'theta_exact':str(theta),'delta_exact':str(delta),'producer_sha256':sha(Path(__file__)),
      'frozen_weighted_checker_sha256':WEIGHTED,
      'not_proved':['independent second fullR integration','native L2 spectral gap','sign atlog3','all-window positivity','RH']}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('weighted',type=Path);p.add_argument('residual',type=Path);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();r=enclose(a.weighted,a.residual);a.out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='exact_Gz_squared_norm_balls'},indent=2))
