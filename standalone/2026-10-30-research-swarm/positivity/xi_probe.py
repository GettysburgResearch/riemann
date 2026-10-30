#!/usr/bin/env python3
"""Exploratory actual-xi Fourier probe for the factor-removal curvature.

Requires NumPy/SciPy. Ordinary double precision, no directed intervals.
The first two zero centers are the decimal centers printed in Sra v2 C.6,
rounded to binary64. Their use here is numerical, not an exact zero claim.
"""
import json
import math
from pathlib import Path
import warnings
import numpy as np
from scipy.special import gammaln, zetac

ZEROS=np.array([14.13472514173469379045725198356247027078425711569924318,
                21.02203963877155499262847959389690277733434052490278175])


def log_xi_real(s):
    s=np.asarray(s,dtype=float)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        p=(s-1)*(zetac(s)+1)
    p=np.where(s==1,1.,p)
    assert np.all(p>0)
    return np.log(s/2)+np.log(p)-s*math.log(math.pi)/2+gammaln(s/2)


def run(step,cutoff):
    u=np.arange(0,cutoff+step/2,step)
    base=np.exp(float(log_xi_real(.5))-log_xi_real(.5+u))
    weights=np.ones_like(u)*step/math.pi
    weights[[0,-1]]*=.5
    result=[]
    for n in (0,1,2):
        phi=base.copy()
        for z in ZEROS[:n]: phi*=1+(u/z)**2
        for x in (0.,.1,.2,.3,.4):
            c=np.cos(u*x); ss=np.sin(u*x)
            terms=(c,-u*ss,-u*u*c,u**3*ss,u**4*c)
            f=np.array([math.fsum((weights*phi*t).tolist()) for t in terms])
            curvature=(f[1]**2-f[0]*f[2])/f[0]**2
            rec={"removed_factors":n,"x":x,"density":float(f[0]),
                 "minus_log_second_derivative":float(curvature)}
            if n<2:
                a=ZEROS[n]
                k=(a*a*f[1]-f[3])**2-(a*a*f[0]-f[2])*(a*a*f[2]-f[4])
                rec['removal_K']=float(k)
                rec['removed_density_via_operator']=float(f[0]-f[2]/a**2)
            result.append(rec)
    return result


def main():
    coarse=run(.25,128.)
    fine=run(.125,256.)
    difference=max(abs(a['density']-b['density']) for a,b in zip(coarse,fine))
    relative=max(abs(a['density']-b['density'])/max(abs(b['density']),1e-300)
                 for a,b in zip(coarse,fine))
    out={"status":"exploratory_only","target":"xi(1/2)/xi(1/2+u), multiplied by first real-zero factors",
         "quadrature":"even Fourier trapezoid, binary64; steps/cutoffs (0.25,128), (0.125,256)",
         "maximum_density_difference":difference,"maximum_relative_density_difference":relative,
         "all_sampled_curvatures_positive":all(r['minus_log_second_derivative']>0 for r in fine),
         "all_sampled_removal_K_positive":all(r.get('removal_K',1)>0 for r in fine),
         "samples":fine,
         "limitations":"No rigorous truncation or rounding bounds; no global positivity or RH inference; zero centers rounded."}
    Path(__file__).with_name('xi_probe_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='samples'},indent=2))


if __name__=='__main__':
    main()
