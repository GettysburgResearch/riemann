"""Directed complete-source principal Gaussian fixtures with proven tails.

Requires python-flint==0.9.0. No coefficient or primitive input is read from
deposited JSON. Default run produces the declared finite grid only.
"""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys

import flint
from flint import arb, ctx
import ideals as I


def serial(value):
    return json.dumps(value, sort_keys=True, indent=2)+'\n'


def render(ball):
    I.require(ball.is_finite(), 'Nonfinite numerical enclosure.')
    text = ball.str(65, more=True)
    I.require(arb(text).contains(ball), 'Decimal serialization lost its enclosure.')
    return text


def integer_power(ball, exponent):
    """Directed integer power, valid also when the base ball crosses zero.

    python-flint's generic arb power uses analytic exponentiation and can
    return NaN at a zero-crossing base. Integer multiplication avoids that
    domain restriction; every multiplication remains a directed enclosure.
    """
    I.require(isinstance(exponent, int) and exponent >= 0, 'Nonnegative integer power required.')
    result = arb(1)
    while exponent:
        if exponent & 1:
            result *= ball
        exponent //= 2
        if exponent:
            ball *= ball
    return result


def square_ball(ball):
    return (ball*ball).nonnegative_part()


def weight(n, D, c=0, tau=1):
    y = arb(n)/D
    log_y = y.log()
    return (-c*log_y-log_y*log_y/(4*tau)).exp()/(4*arb.pi()*tau).sqrt()


def exterior_counting_constants():
    """A,B in the unconditional I_F^S(x)<=A*x+B*sqrt(x), S over 2,3."""
    sqrt3 = arb(3).sqrt()
    return arb.pi()/(6*sqrt3), 6+2*sqrt3


def tail_bound(Y, D, c=0, tau=1):
    I.require(Y >= 1 and D > 0 and tau > 0, 'Invalid Gaussian tail domain.')
    log_R = (arb(Y)/D).log()
    I.require(c+log_R/(2*tau) > 0, 'Tail profile must be strictly decreasing.')
    w = weight(Y, D, c, tau)
    coarse = (2*Y*w
             + D*(arb(tau)*(1-c)**2).exp()
             * ((log_R-2*tau*(1-c))/(2*arb(tau).sqrt())).erfc())
    # I_F^S(x) <= A*x+B*sqrt(x), proved by the exact chi_-3 hyperbola
    # formula and inclusion-exclusion at the ideal norms 3 and 4.
    A, B = exterior_counting_constants()
    half_delta = arb(1)/2-c
    refined = (A*(Y*w + arb(D)/2*(arb(tau)*(1-c)**2).exp()
                  * ((log_R-2*tau*(1-c))/(2*arb(tau).sqrt())).erfc())
               + B*(arb(Y).sqrt()*w
                    + arb(D).sqrt()/4*(tau*half_delta*half_delta).exp()
                    * ((log_R-2*tau*half_delta)/(2*arb(tau).sqrt())).erfc()))
    # Each expression is independently a full-tail majorant. A strict
    # directed comparison chooses the refinement only when certified smaller.
    bound = refined if refined < coarse else coarse
    if isinstance(Y, int):
        # First dominate the absolute source by ALL S-free ideals. Their
        # exact tail has the negative Stieltjes boundary -I_F^S(Y)*W(Y/D).
        # Restoring it sharpens G3 without truncating any omitted column.
        boundary_refined = refined-I.exterior_ideal_count(Y)*w
        if boundary_refined.is_finite() and boundary_refined > 0 and boundary_refined < bound:
            bound = boundary_refined
    I.require(bound.is_finite() and bound > 0, 'Positive finite complete-tail bound required.')
    return bound


def coefficient_digest(coefs):
    # The integer source is portable across host byte orders.
    if sys.byteorder == 'big':
        copied = coefs[:]
        copied.byteswap()
        return hashlib.sha256(copied.tobytes()).hexdigest()
    return hashlib.sha256(coefs.tobytes()).hexdigest()


def principal_masks(B):
    by_signature = defaultdict(list)
    for b in I.ideals_up_to(B):
        if I.exterior(b):
            by_signature[I.mask_signature(b)].append(b)
    return dict(sorted(by_signature.items()))


def produce(max_power=12, B=64, ratio=4096, precision=256, progress=False):
    I.require(0 <= max_power <= 12, 'max_power must be in [0,12].')
    I.require(7 <= B <= 256 and 16 <= ratio <= 8192, 'Finite coverage limits exceeded.')
    I.require(precision >= 192, 'At least 192 bits are required.')
    ctx.prec = precision
    signatures = principal_masks(B)
    max_cutoff = ratio*(2**max_power)
    principal_source = I.norm_mobius_coefficients(max_cutoff, compact=True)
    coefs = {}
    digests = []
    for signature, bs in signatures.items():
        if progress:
            print('Building exact source mask '+str(signature), file=sys.stderr, flush=True)
        values = I.mask_coefficients_from_principal(principal_source, signature)
        I.require(values.itemsize == 4, 'Signed int32 source storage required.')
        coefs[signature] = values
        digests.append({'signature': [list(x) for x in signature],
                        'coefficient_int32_le_sha256': coefficient_digest(values),
                        'ideals': [list(x) for x in bs],
                        'multiplicity': len(bs)})
    all_values = []
    principal_coefficients = coefs[()]
    for j in range(max_power+1):
        D, Y = 2**j, ratio*(2**j)
        if progress:
            print('Directed Gaussian D='+str(D)+', all norms <= '+str(Y),
                  file=sys.stderr, flush=True)
        totals = {s: arb(0) for s in signatures}
        used = 0
        for n in range(1, Y+1):
            if not principal_coefficients[n]:
                # Every masked local support is contained in the full
                # principal local support; exact Euler factors prove this.
                continue
            w = weight(n, D)
            used += 1
            for signature in signatures:
                coefficient = coefs[signature][n]
                if coefficient:
                    totals[signature] += coefficient*w
        tail = tail_bound(Y, D)
        radius = tail.abs_upper()
        enclosed = {s: v+arb(0, radius) for s, v in totals.items()}
        row_values = [{'signature': [list(x) for x in s],
                       'multiplicity': len(bs), 'enclosure': render(enclosed[s])}
                      for s, bs in signatures.items()]
        moments = {}
        for k in (1, 2, 4, 8, 16):
            moment = sum((len(signatures[s])*integer_power(v, 2*k).nonnegative_part()
                          for s, v in enclosed.items()), arb(0))
            moment = moment.nonnegative_part()
            I.require(moment >= 0, 'A nonnegative moment lost its sign enclosure.')
            moments[str(2*k)] = render(moment)
        all_values.append({'D': D, 'complete_norm_cutoff': Y,
                           'nonzero_original_norm_coefficients': used,
                           'absolute_omitted_tail_upper_ball': render(tail),
                           'rows': row_values, 'complete_principal_replica_moments': moments})
    return {'status': 'DIRECTED FINITE ENCLOSURES; no asymptotic or RH conclusion',
            'field': 'Q(w), w^2+w+1=0', 'S': 'prime ideals above 2 and 3',
            'source': 'mu_F(n) times literal principal mask 1_((n,b)=1)',
            'normalization': {'c': 0, 'tau': 1, 'weight': 'exp[-log(y)^2/4]/sqrt(4 pi)'},
            'parameters': {'max_power': max_power, 'all_b_norm_cap': B,
                           'cutoff_ratio': ratio, 'precision_bits': precision},
            'arithmetic': {'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
                           'contract': 'Arb balls; every decimal enclosure roundtrip checked'},
            'coefficient_coverage': {'all_norms_through': max_cutoff,
                                    'source_int32_entries_per_mask': max_cutoff+1,
                                    'mask_signatures': digests},
            'values': all_values}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-power', type=int, default=12)
    parser.add_argument('--b-cap', type=int, default=64)
    parser.add_argument('--ratio', type=int, default=4096)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    result = produce(args.max_power, args.b_cap, args.ratio, args.precision, args.progress)
    content = serial(result)
    if args.output:
        args.output.write_text(content, encoding='utf-8', newline='\n')
    else:
        print(content, end='')


if __name__ == '__main__':
    main()
