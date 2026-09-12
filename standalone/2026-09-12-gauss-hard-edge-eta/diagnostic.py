#!/usr/bin/env python3
"""Optional NONDIRECTED numerical consistency checks; never imported by check.py.

Uses mpmath eigensystems and special functions. This is not interval arithmetic,
not a zero certificate, and not an input to the proposed analytical proofs.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
try:
    import mpmath as mp
except ImportError as exc:
    raise SystemExit('Optional diagnostic requires mpmath; the exact checker does not.') from exc


def pair(z):
    return {'re':mp.nstr(mp.re(z),35),'im':mp.nstr(mp.im(z),35)}


def nodes_and_shapes(m):
    mat=mp.matrix(m)
    mat[0,0]=mp.mpf(2)/5
    for j in range(1,m):
        mat[j,j]=mp.mpf(12)/((4*j+1)*(4*j+5))
        mat[j-1,j]=mat[j,j-1]=mp.sqrt(mp.mpf(36)/((4*j-1)*(4*j+1)**2*(4*j+3)))
    nodes,vectors=mp.eigsy(mat)
    shapes=[vectors[0,j]**2/nodes[j] for j in range(m)]
    if not all(nodes[j]>0 and shapes[j]>0 for j in range(m)):
        raise ArithmeticError('Noncertifying eigensolver lost node/shape positivity')
    return nodes,shapes


def compute(dps=65):
    if dps<45: raise ValueError('Use at least 45 decimal digits for these diagnostics')
    mp.mp.dps=dps
    qs=[mp.mpf(3)/4+1j,mp.mpf(3)/5+2j,mp.mpf(5)/4+mp.mpf(3)/10*1j]
    limits=[]
    for q in qs:
        c=8/q*(mp.mpf(3)/8)**q*mp.gamma(2*q-1)
        k0=c*mp.altzeta(2*q-1)
        k1=(mp.mpf(3)/8)**q/(6*q)*(mp.gamma(2*q+2)*mp.altzeta(2*q+1)-24*mp.gamma(2*q)*mp.altzeta(2*q-1))
        limits.append((q,c,k0,k1))
    rows=[]
    for m in (4,8,16,32,64):
        a=mp.mpf(m*(2*m+3))/2
        nodes,shapes=nodes_and_shapes(m)
        tests=[]
        for q,c,k0,k1 in limits:
            km=mp.pi*a**(2*q-1)/(q*mp.sin(mp.pi*q))*((6/mp.pi**2)**q*mp.zeta(2*q)-mp.fsum(shapes[j]*nodes[j]**q for j in range(m)))
            s=2*q-1
            em=km/c
            corrected=(em-s*(s+1)*(s+2)*mp.altzeta(s+2)/(48*a))/(1-s/(2*a))
            tests.append({'q':pair(q),'K_m':pair(km),'K_0':pair(k0),'K_1':pair(k1),
                          'A_times_error':pair(a*(km-k0)),
                          'error_abs':mp.nstr(abs(km-k0),25),
                          'first_correction_remainder_abs':mp.nstr(abs(km-k0-k1/a),25),
                          'A_times_correction_remainder_abs':mp.nstr(abs(a*(km-k0)-k1),25),
                          'eta_error_abs':mp.nstr(abs(em-mp.altzeta(s)),25),
                          'corrected_eta_error_abs':mp.nstr(abs(corrected-mp.altzeta(s)),25)})
        rows.append({'m':m,'A':mp.nstr(a,20),'scaled_smallest_node':mp.nstr(a*a*nodes[0],35),
                     'smallest_node_shape_fraction':mp.nstr(shapes[0]/a,35),'tests':tests})
    q,c,k0,k1=limits[0]
    i0=4/q*(mp.mpf(3)/2)**q*mp.quad(lambda u:u**(2*q-2)/(mp.exp(2*u)+1),[0,mp.mpf(1)/10,1,5,mp.inf])
    i1=(mp.mpf(3)/2)**q/(6*q)*mp.quad(lambda u:(u**(2*q+1)-6*u**(2*q-1))/mp.cosh(u)**2,[0,mp.mpf(1)/10,1,5,mp.inf])
    return {'scope':'NONCERTIFYING mpmath diagnostics, no zero-location conclusion',
            'dps':dps,'orders':rows,'integral_comparison_q':pair(q),
            'fermi_integral_discrepancy_abs':mp.nstr(abs(i0-k0),25),
            'correction_integral_discrepancy_abs':mp.nstr(abs(i1-k1),25)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--dps',type=int,default=65)
    p.add_argument('--out',type=Path,default=Path(__file__).with_name('diagnostics.json'))
    args=p.parse_args()
    record=compute(args.dps)
    args.out.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print('NONCERTIFYING diagnostic written:',args.out)
    for row in record['orders']:
        t=row['tests'][0]
        print('m=',row['m'],'error=',t['error_abs'],'corrected=',t['first_correction_remainder_abs'])
    print('integral differences:',record['fermi_integral_discrepancy_abs'],record['correction_integral_discrepancy_abs'])

if __name__=='__main__':
    main()
