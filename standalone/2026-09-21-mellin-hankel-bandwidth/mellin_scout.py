#!/usr/bin/env python3
"""Optional ordinary-multiprecision Mellin sanity check; NOT directed acceptance.

Uses mpmath. Finite quadrature has no rigorous error bound. The displayed
analytic tail ceiling does not turn that quadrature into a certificate.
"""
import argparse
import json
from pathlib import Path
import mpmath as mp


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--limit',type=int,default=64)
    p.add_argument('--digits',type=int,default=25)
    p.add_argument('--write',type=Path)
    args=p.parse_args()
    if not 3<=args.limit<=256 or not 20<=args.digits<=80:
        raise ValueError('bounded scout parameters: limit 3..256, digits 20..80')
    mp.mp.dps=args.digits
    def integrand(t):
        s=mp.mpf('0.5')+1j*t
        G=24/mp.fprod(s+j for j in range(5))
        C=1-mp.power(2,s) # C(1-s) for c=delta_1-2delta_2.
        return mp.re(C*C*mp.zeta(s)*G)/mp.pi
    value=sum(mp.quad(integrand,[a,min(a+2,args.limit)]) for a in range(0,args.limit,2))
    target=mp.mpf(37)/640
    # |C(1-s)|<3, |G(s)|<=24/t^5, and Patel--Yang imply this looser ceiling.
    tail=2000*mp.power(args.limit,-mp.mpf(15)/4)
    data={'kind':'ordinary_mpmath_scout_not_a_certificate','digits':args.digits,'limit':args.limit,
          'integrated_centered_value':str(value),'exact_target':'37/640',
          'difference_from_target':str(value-target),'analytic_tail_ceiling_descriptive_decimal':str(tail),
          'finite_quadrature_error_bound':None,'rank_term':'1/5','raw_exact_value':'33/128',
          'missing_sign_or_rank_disguised_as_error':False}
    text=json.dumps(data,indent=2)+'\n'
    if args.write:args.write.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
