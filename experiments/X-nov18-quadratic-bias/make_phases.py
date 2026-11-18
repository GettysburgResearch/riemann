"""Produce integer phase witnesses; verify_phases.py independently checks them."""
import argparse
import json
import lzma
from math import floor
from pathlib import Path

from flint import acb, arb, ctx
from fpylll import CVP, IntegerMatrix, LLL
from scipy.optimize import brentq

from spectral import primitive_character
from verify_phases import check


# The number of selected sign brackets, in ascending positive ordinate order.
CASES = {-56:10, -47:38, -39:49, -31:69, -24:110,
         29:36, 37:65, 44:25, 56:13, 57:123, 60:18, 61:16, 65:28, 73:60}


def nearest(value):
    return int((value + arb(1)/2).mid().floor().unique_fmpz())


def initial_brackets(chi, count):
    ctx.prec = 55
    def estimate(t):
        return float(chi.hardy_z(t).real)
    left, previous = 0, estimate(0)
    brackets = []
    for step in range(1, 801):
        right = step/4
        current = estimate(right)
        if previous*current < 0:
            root = brentq(estimate, left, right, xtol=5e-13)
            lo = floor(1e12*root)-2
            hi = lo+6
            if chi.hardy_z(arb(lo)/10**12).real*chi.hardy_z(arb(hi)/10**12).real<0:
                brackets.append((lo,hi))
                if len(brackets)==count:
                    return brackets
        left, previous = right, current
    raise ValueError('too few initial sign brackets')


def refined_bracket(chi, left, right, precision):
    ctx.prec = precision+100
    x, y = arb(left)/10**12, arb(right)/10**12
    fx = chi.hardy_z(x.mid()).real.mid()
    for iteration in range(18):
        y = y.mid()
        fy = chi.hardy_z(y).real.mid()
        if abs(fy)<arb(2)**(-precision-20):
            break
        estimate = (y-fy*(y-x)/(fy-fx)).mid()
        x, y, fx = y, estimate, fy
    center = nearest(y*2**precision)
    for radius in (2,10,100):
        lo = arb(center-radius)/2**precision
        hi = arb(center+radius)/2**precision
        if chi.hardy_z(lo).real*chi.hardy_z(hi).real<0:
            return center-radius, center+radius
    raise ArithmeticError('failed to certify refined bracket')


def generate(d):
    count = CASES[d]
    bits = 9*count+20
    precision = bits+40
    chi = primitive_character(d)
    raw = initial_brackets(chi,count)
    brackets = [refined_bracket(chi,lo,hi,precision) for lo,hi in raw]
    basis = IntegerMatrix(count+1,count+1)
    basis[0,0] = 1
    target = [0]
    for i,(lo,hi) in enumerate(brackets,1):
        gamma = arb(lo).union(arb(hi))/2**precision
        coeff = 1/(acb(arb(1)/2,gamma)*acb(arb(3)/2,gamma))
        basis[0,i] = nearest(2**bits*gamma/(2*arb.pi()))
        basis[i,i] = 2**bits
        target.append(nearest(2**bits*(arb.pi()-coeff.arg())/(2*arb.pi())))
    LLL.reduction(basis)
    phase = int(CVP.babai(basis,target)[0])
    result = {'d':d, 't':str(phase), 'p':precision,
              'brackets':[[str(l),str(h)] for l,h in brackets]}
    check(result)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('phase-witnesses.json.xz'))
    parser.add_argument('discriminants',nargs='*',type=int)
    args=parser.parse_args()
    ds=args.discriminants or sorted(CASES)
    records=[generate(d) for d in ds]
    args.output.write_bytes(lzma.compress(json.dumps(records,separators=(',',':')).encode()))
