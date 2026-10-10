#!/usr/bin/env python3
"""Exact frequency coverage and source constants for the codimension-14 bound."""

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

from check_coercivity import log_rational_bounds, require


def atan_bounds(x: Q, count: int):
    terms = [(-1)**j * x**(2*j + 1) / (2*j + 1) for j in range(count)]
    partial = sum(terms, Q())
    following = (-1)**count * x**(2*count + 1) / (2*count + 1)
    return min(partial, partial + following), max(partial, partial + following)


def certify():
    # Machin identity pi=16 atan(1/5)-4 atan(1/239) is a named exact input.
    a_lo, a_hi = atan_bounds(Q(1, 5), 16)
    b_lo, b_hi = atan_bounds(Q(1, 239), 8)
    pi_lo = 16*a_lo - 4*b_hi
    pi_hi = 16*a_hi - 4*b_lo
    require(pi_lo > Q(31415, 10000), "pi>3.1415")
    require(pi_hi < Q(3927, 1250), "pi<3.1416")
    log2_lo, log2_hi = log_rational_bounds(Q(2))
    require(log2_hi < Q(1733, 2500), "log2<0.6932")
    harmonic1024 = sum((Q(1,j) for j in range(1,1025)), Q())
    require(harmonic1024-10*log2_lo < Q(289,500), "gamma<0.578")
    _, logpi_hi = log_rational_bounds(Q(3927,1250),64)
    require(logpi_hi < Q(1431,1250), "logpi<1.1448")
    require(Q(289,500) + Q(3927,2500) + 3*Q(1733,2500) + Q(1431,1250)
            < Q(43,8), "Omega(0)>-43/8")
    require(Q(707,500)**2 < 2, "sqrt2>707/500")
    require(Q(1733,2500)/Q(707,500) < Q(491,1000), "q2<491/1000")

    scale = 2**100
    alpha = Q(13,10)
    constant = 710
    def v_lower(x):
        return -Q(43,8)-Q(491,500)+Q(sum(
            (scale*16*x)//((4*k+1)*((4*k+1)**2+4*x)) for k in range(257)),scale)
    def p(x):
        return (Q(x)+Q(1,4))**2/(Q(x)+Q(9,4))
    minimum = None
    minimum_cell = None
    for left in range(4096):
        right = left+1
        vlo = v_lower(left)
        product_lo = (p(right) if vlo<0 else p(left))*vlo
        margin = product_lo-alpha*right+constant
        require(margin>0, ("frequency cell",left,str(margin)))
        if minimum is None or margin<minimum:
            minimum,minimum_cell=margin,left
    tail_v = v_lower(4096)
    require(tail_v>alpha, "unbounded tail V(4096)>13/10")
    require(constant>Q(7,4)*tail_v, "unbounded tail constant")
    kappa_lower = Q(3,2)*(alpha-Q(constant,144)/Q(31415,10000)**2)
    require(kappa_lower>=Q(6,5), "11-mode primitive coercivity>=6/5")
    return {
        "status":"EXACT_ARITHMETIC_ACCEPT",
        "scope":"codimension-14 source coercivity at L=1, not effective sign",
        "supporting_line":{"alpha":str(alpha),"constant":constant},
        "gamma_last_index":256,
        "compact_cells":4096,
        "arithmetic":"integer floors at scale 2^100 and exact Fraction",
        "minimum_cell_margin":{"cell":minimum_cell,"lower":str(minimum)},
        "unbounded_tail_v_lower":str(tail_v),
        "kappa_lower":str(kappa_lower),
        "classical_inputs":["Machin identity","gamma<H_1024-log1024","digamma partial fractions"],
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_sha256":hashlib.sha256(Path(__file__).with_name('check_coercivity.py').read_bytes()).hexdigest(),
    }


if __name__=='__main__':
    print(json.dumps(certify(),indent=2))
