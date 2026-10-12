#!/usr/bin/env python3
"""Sharpen the primitive synthesis constant after the frozen full replay."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

from flint import arb, acb, ctx
from enclose_analytic_upper import require, f, fp
import enclose_primitive_norm as primitive

HERE = Path(__file__).resolve().parent
FROZEN_PRIMITIVE = 'a84255c51d8409fa33ab00ddbab42199e0e19a86a44bb066dcaf7740d657a5f0'
RATES = [Q(1,2),Q(-1,2),Q(1,2),Q(-1,2),Q(3,2),Q(-3,2)]
POWERS = [0,0,1,1,0,0]


def moment(rate, power):
    z = acb(arb(rate.numerator) / rate.denominator)
    if rate == 0:
        return arb(1) / (power + 1)
    if power == 0:
        return f(z).real
    if power == 1:
        return fp(z).real
    require(power == 2, 'only complete degree-two product moments')
    return ((z.exp() * (z*z - 2*z + 2) - 2) / (z*z*z)).real


def synthesis(source):
    removed = source['removed_sine_modes']
    trial = source['trial_modes']
    require(removed in (5,11) and trial == 100, 'reviewed native sine inventories')
    dim = removed + 3
    coefficients = source['exact_trial_z_coefficients_balls']
    require(len(coefficients) == dim+trial and all(len(r) == dim for r in coefficients),
            'complete exact native coefficient inventory')
    soft_gram = [[moment(RATES[i]+RATES[j], POWERS[i]+POWERS[j])
                  for j in range(6)] for i in range(6)]
    trig_moments = []
    for n in range(1,removed+trial+1):
        row=[]
        for rate,power in zip(RATES,POWERS):
            z=acb(arb(rate.numerator)/rate.denominator,arb.pi()*n)
            row.append((f(z) if power==0 else fp(z)).real)
        trig_moments.append(row)
    norms=[]
    for i in range(dim):
        soft=[arb(0) for _ in range(6)]
        cosine=[arb(0) for _ in range(removed+trial)]
        for row in range(dim+trial):
            coefficient=arb(coefficients[row][i])
            if row<removed or row>=dim:
                n=row+1 if row<removed else removed+1+row-dim
                frequency=arb.pi()*n
                scale=frequency/(frequency*frequency+arb(1)/4)
                soft[0]+=coefficient*scale/2
                soft[1]+=coefficient*scale/2
                cosine[n-1]-=coefficient*scale
            elif row==removed:
                soft[0]+=coefficient/2
                soft[1]-=coefficient/2
                soft[2]+=coefficient/2
            elif row==removed+1:
                soft[0]+=coefficient/2
                soft[1]-=coefficient/2
                soft[3]+=coefficient/2
            else:
                soft[0]-=coefficient/8
                soft[1]+=coefficient/8
                soft[4]+=3*coefficient/8
                soft[5]-=3*coefficient/8
        squared=sum((soft[j]*soft[k]*soft_gram[j][k]
                     for j in range(6) for k in range(6)),arb(0))
        squared+=sum((x*x/2 for x in cosine),arb(0))
        squared+=2*sum((soft[j]*cosine[n]*trig_moments[n][j]
                        for n in range(removed+trial) for j in range(6)),arb(0))
        require(squared.is_finite() and squared>0, 'positive directed exact primitive norm')
        norms.append(squared)
    total=sum(norms,arb(0))
    return norms,total


def enclose(weighted,residual):
    require(hashlib.sha256((HERE/'enclose_primitive_norm.py').read_bytes()).hexdigest()==FROZEN_PRIMITIVE,
            'frozen quantitative extractor before full replay')
    baseline=primitive.enclose(weighted,residual)
    ctx.prec=256
    source=json.loads(weighted.read_text())['fresh_source_moment_receipt']['source_U_receipt']
    norms,total=synthesis(source)
    k=primitive.positive_integer_upper(total)
    epsilon=Q(baseline['epsilon_exact'])
    theta=Q(baseline['theta_exact'])
    kappa=Q(baseline['primitive_gap_exact'])
    delta=min(epsilon/(2*(1+2*k)),theta*kappa/2)
    require(delta>Q(baseline['delta_exact']), 'strict improvement over reviewed crude synthesis')
    return {'status':'DIRECTED_EXACT_PRIMITIVE_SYNTHESIS_ACCEPT',
            'native_bound':'q_L(h)>=delta*||G_L h||_2^2 for every complex h and every0<L<=1; L1 also pays projectedE norm',
            'baseline':baseline,'exact_Gz_squared_norm_balls':[x.str(50,more=True) for x in norms],
            'synthesis_trace_ball':total.str(50,more=True),'synthesis_upper_integer':k,
            'delta_exact':str(delta),'delta_decimal_display_only':float(delta),
            'full_weighted_replay_performed':True,'new_R_integration_performed':False,
            'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'proof_sha256':hashlib.sha256((HERE/'EXACT_PRIMITIVE_SYNTHESIS.md').read_bytes()).hexdigest(),
            'scope_limits':['No native L2 spectral gap','No signs atL>1','No RH claim']}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('weighted',type=Path);p.add_argument('residual',type=Path)
    p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    result=enclose(a.weighted,a.residual)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('baseline','exact_Gz_squared_norm_balls')},indent=2))
