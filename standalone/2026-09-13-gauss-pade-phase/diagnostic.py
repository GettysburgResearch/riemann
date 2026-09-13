#!/usr/bin/env python3
"""NONCERTIFYING mpmath scouts, separate from all accepting exact checks.

No outward rounding or complete numerical integration error bound is supplied.
The special-function evaluator is used to TEST formulas, not as their proof.
Jacobi eigensolver construction is adapted from GHE26 diagnostic.py (#877).
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
try:
    import mpmath as mp
except ImportError as exc:
    raise SystemExit('Optional diagnostic requires mpmath; check.py does not.') from exc


def pair(z): return {'re':mp.nstr(mp.re(z),35),'im':mp.nstr(mp.im(z),35)}
def val(z): return mp.nstr(z,25)


def source_nodes(m):
    mat=mp.matrix(m);mat[0,0]=mp.mpf(2)/5
    for j in range(1,m):
        mat[j,j]=mp.mpf(12)/((4*j+1)*(4*j+5))
        mat[j,j-1]=mat[j-1,j]=mp.sqrt(mp.mpf(36)/((4*j-1)*(4*j+1)**2*(4*j+3)))
    nodes,vectors=mp.eigsy(mat)
    shapes=[vectors[0,j]**2/nodes[j] for j in range(m)]
    if not all(nodes[j]>0 and shapes[j]>0 for j in range(m)):
        raise ArithmeticError('Nondirected eigensolver lost positivity')
    return nodes,shapes


def phase_slopes(n,omega):
    # Positive-coefficient B recurrence; avoids evaluating a nearly canceled
    # pair of polynomials just to check the slope identity.
    c=mp.mpf(1);B=mp.mpf(1)
    for j in range(1,n+1):
        c*=mp.mpf(2*(n-j+1))/(j*(2*n-2*j+1)*(2*n-j+1))
        B+=c*omega**(2*j)
    return 1-c*omega**(2*n)/B


def coefficients(s):
    eta=mp.altzeta(s)
    b1=-s*eta/2+mp.rf(s,3)*mp.altzeta(s+2)/48
    b2=s*(s+1)*eta/8-mp.rf(s,3)*(s+4)*mp.altzeta(s+2)/96+(5*s-11)*mp.rf(s,5)*mp.altzeta(s+4)/23040
    return eta,b1,b2


def compute(dps):
    if dps<55:raise ValueError('Use at least 55 digits for these diagnostics')
    mp.mp.dps=dps
    qs=[mp.mpf(3)/4+1j,mp.mpf(3)/5+2j,mp.mpf(5)/4+mp.mpf(3)/10*1j]
    data=[]
    for q in qs:
        s=2*q-1;C=8/q*(mp.mpf(3)/8)**q*mp.gamma(s)
        eta,b1,b2=coefficients(s)
        data.append((q,s,C,eta,b1,b2))
    rows=[]
    for m in [4,8,16,32,64]:
        A=mp.mpf(m*(2*m+3))/2;x,k=source_nodes(m)
        phase_error=max(abs(1/phase_slopes(2*m+1,mp.sqrt(6/x[j]))-k[j]) for j in range(m))
        tests=[]
        for q,s,C,eta,b1,b2 in data:
            K=mp.pi*A**(2*q-1)/(q*mp.sin(mp.pi*q))*((6/mp.pi**2)**q*mp.zeta(2*q)-mp.fsum(k[j]*x[j]**q for j in range(m)))
            E=K/C
            b=mp.rf(s,3)/(48*A)-mp.rf(s,3)*(s+4)/(96*A*A)
            c=(5*s-11)*mp.rf(s,5)/(23040*A*A)
            d=1-s/(2*A)+s*(s+1)/(8*A*A)
            corrected=(E-b*mp.altzeta(s+2)-c*mp.altzeta(s+4))/d
            tests.append({'q':pair(q),'K_m':pair(K),'K_2':pair(C*b2),
                          'A_squared_first_remainder':pair(A*A*(K-C*eta-C*b1/A)),
                          'uncorrected_error_abs':val(abs(K-C*eta)),
                          'first_order_remainder_abs':val(abs(K-C*eta-C*b1/A)),
                          'second_order_remainder_abs':val(abs(K-C*eta-C*b1/A-C*b2/(A*A))),
                          'second_corrected_eta_error_abs':val(abs(corrected-eta))})
        rows.append({'m':m,'A':val(A),'max_phase_weight_discrepancy_abs':val(phase_error),'tests':tests})
    q,s,C,eta,b1,b2=data[0]
    def g2(u):
        return u**3*(-5*u**4*mp.sinh(u)+18*u**3*mp.cosh(u)+60*u**2*mp.sinh(u)+30*u*mp.cosh(u)-180*mp.sinh(u))/(480*mp.cosh(u)**3)
    integral=-(mp.mpf(3)/2)**q*4/(3*q)*mp.quad(lambda u:u**(2*q-3)*g2(u),[0,mp.mpf(1)/10,1,4,mp.inf])
    return {'status':'NONCERTIFYING_DIAGNOSTIC_NOT_ZERO_CERTIFICATE','dps':dps,'orders':rows,
            'second_correction_integral_discrepancy_abs':val(abs(integral-C*b2)),
            'mpmath_version':mp.__version__}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--dps',type=int,default=65)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    data=compute(args.dps);args.out.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('NONCERTIFYING_DIAGNOSTIC',args.out)
    for r in data['orders']:
        t=r['tests'][0]
        print(r['m'],t['first_order_remainder_abs'],t['second_order_remainder_abs'])


if __name__=='__main__':main()
