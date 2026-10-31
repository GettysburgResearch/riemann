"""Cofinal-source residue scaling; ordinary Decimal, no directed certification.

The target ratios use independent binary64 source quadratures, rounded here
to six useful digits. The exact theorem is the analytic argument in the note.
"""
from decimal import Decimal as D, localcontext
from pathlib import Path
import json,sys
from source_polynomials import pi_value,polynomials

def ev(p,x):
    r=D(0)
    for c in reversed(p):r=r*x+c
    return r

def derivative(p):return [D(j)*v for j,v in enumerate(p)][1:]

precision=int(sys.argv[1]) if len(sys.argv)>1 else 240
parameters=[int(x) for x in sys.argv[2:]] or [20,40,80,160]
target=[D('1.48571e10'),D('5.06735e14'),D('3.66755e17')]
rows=[]
for aval in parameters:
    with localcontext() as ctx:
        ctx.prec=precision
        a=D(aval);pi=pi_value();M=int((a*(3+2*a.ln())).to_integral_value(rounding='ROUND_CEILING'))
        A,B=polynomials(a,M,pi);Bp=derivative(B)
        lo=D(0);blo=ev(B,lo);poles=[]
        for j in range(1,251):
            hi=D(j)/(a*a);bhi=ev(B,hi)
            if blo*bhi<0:
                left=lo;right=hi;bl=blo
                for _ in range(35):
                    mid=(left+right)/2;bm=ev(B,mid)
                    if bl*bm<0:right=mid
                    else:left=mid;bl=bm
                x=(left+right)/2
                for _ in range(14):x-=ev(B,x)/ev(Bp,x)
                gamma=-ev(A,x)/ev(Bp,x)*a*a
                scaled=gamma*(2*a).exp()/(2*pi*a)
                index=len(poles)
                poles.append({'energy':str(x*a*a),'residue':str(gamma),
                              'residue_divided_by_2pi_a_exp_minus_2a':str(scaled),
                              'ratio_to_rounded_limiting_companion_diagnostic':str(scaled/target[index])})
                if len(poles)==3:break
            lo=hi;blo=bhi
        row={'a':aval,'M':M,'M_over_a':str(D(M)/a),'precision':precision,'first_three_sign_changing_real_poles':poles}
        rows.append(row)
        print(aval,M,[(float(D(x['energy'])),float(D(x['residue_divided_by_2pi_a_exp_minus_2a'])),float(D(x['ratio_to_rounded_limiting_companion_diagnostic']))) for x in poles],flush=True)
Path(__file__).with_name('RESIDUE_SCALING_'+str(precision)+'.json').write_text(json.dumps({'scope':'ordinary Decimal polynomial calculations and binary64 target quadratures; no interval signs or complete pole census','rows':rows},indent=2)+'\n')
