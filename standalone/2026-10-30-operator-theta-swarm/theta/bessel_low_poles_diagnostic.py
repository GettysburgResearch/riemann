"""Ordinary high-precision real-root probes; no completeness/interval guarantee."""
from decimal import Decimal as D,localcontext
from pathlib import Path
import json
from bessel_jacobi_diagnostic import pi_value,polynomials

def ev(p,x):
    r=D(0)
    for c in reversed(p):r=r*x+c
    return r

def derive(p):return [D(j)*v for j,v in enumerate(p)][1:]
rows=[]
for a,M in [(10,50),(20,100),(50,250),(100,500)]:
    with localcontext() as ctx:
        ctx.prec=360;aa=D(a);A,B=polynomials(aa,M,pi_value());Bp=derive(B)
        lo=D(0);blo=ev(B,lo);poles=[]
        for j in range(1,501):
            hi=D(j)/(aa*aa);bhi=ev(B,hi)
            if blo*bhi<0:
                L=lo;H=hi;bl=blo
                for _ in range(45):
                    mid=(L+H)/2;bm=ev(B,mid)
                    if bl*bm<0:H=mid
                    else:L=mid;bl=bm
                z=(L+H)/2
                for _ in range(12):z-=ev(B,z)/ev(Bp,z)
                gamma=-ev(A,z)/ev(Bp,z)*aa*aa
                poles.append({'E':str(z*aa*aa),'residue_E':str(gamma),'sign':'positive' if gamma>0 else 'negative'})
            lo=hi;blo=bhi
        rows.append({'a':a,'M':M,'search_real_E_0_to_500_step_1':True,'real_poles_found':poles})
        print(a,M,[(float(D(z['E'])),f"{D(z['residue_E']):.4E}",z['sign']) for z in poles[:8]],'count',len(poles),flush=True)
Path(__file__).with_name('BESSEL_LOW_POLES_DIAGNOSTIC.json').write_text(json.dumps({'scope':'ordinary Decimal signs, no directed rounding; only sign-changing real roots sought; no completeness guarantee','rows':rows},indent=2)+'\n')
