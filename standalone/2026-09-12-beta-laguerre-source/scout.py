#!/usr/bin/env python3
"""Optional NONCERTIFYING endpoint-response scout. Requires mpmath.

No parameter-derivative tail bound is supplied. Do not use this output as a
native sign or zero certificate. Large orders can require substantial work.
"""
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys


def tangent_coefficients(mp,N: int):
    e=[mp.mpf(1),mp.mpf(1)];de=[mp.mpf(0),mp.mpf(0)];beta=mp.mpf(1)
    for j in range(1,N+1):
        beta*=(mp.mpf(j)+mp.mpf('1.5'))/(j+4)
        if j<2:continue
        a=(1-mp.power(2,1-2*j))/(2*j-1);ad=a-beta
        conv=mp.fsum(e[i]*e[j-i] for i in range(1,j))
        dconv=2*mp.fsum(de[i]*e[j-i] for i in range(1,j))
        e.append(a/(1-2*a)*conv)
        de.append(ad/(1-2*a)**2*conv+a/(1-2*a)*dconv)
    ds=[2*mp.fsum(de[i]*e[j-i] for i in range(j+1))*(-mp.mpf('2.5'))**j
        for j in range(N+1)]
    out=[]
    for m in range(N+1):
        choose=mp.binomial(m+4,4);terms=[]
        for j in range(m+1):
            terms.append(choose*ds[j]);choose*=mp.mpf(m-j)/(j+5)
        out.append(mp.fsum(terms))
    return out


def finite_mellin(mp,s,bs):
    p=s/2;poch=mp.mpc(1);terms=[bs[0]]
    for j in range(1,len(bs)):
        poch*=(j-1-p)/(j+4);terms.append(bs[j]*poch)
    return (mp.pi/15)**p*mp.gamma(5+p)/24*mp.fsum(terms)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--order',type=int,default=200)
    ap.add_argument('--indices',type=int,nargs='+',default=[4,9,10,11,12])
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.order<4 or any(i<1 for i in args.indices):raise ValueError('invalid order/index')
    root=Path(__file__).resolve().parent
    if args.output.resolve().is_relative_to(root):raise ValueError('write output outside authenticated packet')
    try:import mpmath as mp
    except ImportError as exc:raise RuntimeError('optional scout requires mpmath; exact checker does not') from exc
    mp.mp.dps=max(80,int(.45*args.order)+85)
    dps=mp.mp.dps;bs=tangent_coefficients(mp,args.order)
    mp.mp.dps=45
    def xi(s):return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)/2
    rows=[]
    for index in args.indices:
        z=mp.zetazero(index)
        v=finite_mellin(mp,z,bs)/(2*mp.diff(xi,z))
        rows.append({'mpmath_zero_index':index,'height':mp.nstr(mp.im(z),18),
                     'formal_raw_root_drift':[mp.nstr(mp.re(v),16),mp.nstr(mp.im(v),16)]})
    result={'status':'NONCERTIFYING; parameter-derivative remainder uncontrolled',
            'order':args.order,'coefficient_dps':dps,'evaluation_dps':45,'rows':rows}
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print('NONCERTIFYING OUTPUT WRITTEN; no zero/sign conclusion')


if __name__=='__main__':
    try:main()
    except (ValueError,RuntimeError,OSError) as exc:
        print(str(exc),file=sys.stderr);raise SystemExit(1)
