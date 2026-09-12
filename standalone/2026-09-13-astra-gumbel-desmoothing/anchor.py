"""Complete theta-integral signs at 14 and 15, with outward dyadic balls.

Only standard-library exact arithmetic enters reconstruction. The analytic
coverage contract is in PROOF.md: every time cell, Taylor remainder, later
theta index and infinite time tail is retained. This does not count zeros.
"""
from fractions import Fraction as F
from math import factorial
from ball_core import B, Q, PI, ZERO, ONE, I, exp, polyval, convolution, rad

CELLS = 128
DEGREE = 24
THETA_TERMS = 4

def derivative_polynomials(degree=DEGREE):
    rows = [[F(0), F(-6), F(4)]]
    for _ in range(degree):
        p = rows[-1]
        out = [F(0)] * (len(p) + 1)
        for j, a in enumerate(p):
            out[j] += (F(1, 2) + 2*j)*a
            out[j+1] -= 2*a
        rows.append(out)
    return rows


def reconstruct():
    rows = derivative_polynomials()
    total = {14: ZERO, 15: ZERO}
    h = F(1, CELLS)
    fac = [factorial(k) for k in range(DEGREE+1)]
    waves = {}
    for gamma in total:
        wave = [ONE]
        for k in range(1, DEGREE+1):
            wave.append(wave[-1] * (I*gamma) / k)
        waves[gamma] = wave
    for j in range(CELLS):
        c = F(2*j+1, CELLS)
        ee = exp(B.real(2*c))
        source = [ZERO for _ in range(DEGREE+1)]
        for n in range(1, THETA_TERMS+1):
            q = PI * (n*n) * ee
            common = exp(B.real(c/2)-q)
            for k in range(DEGREE+1):
                source[k] = source[k] + common*polyval(rows[k], q)/fac[k]
        for gamma in total:
            series = convolution(source, waves[gamma], DEGREE)
            cell = ZERO
            for k in range(0, DEGREE+1, 2):
                cell = cell + series[k]*(2*h**(k+1)/F(k+1))
            total[gamma] = total[gamma] + cell*exp(I*(gamma*c))
    # Cauchy: radius 1/16, half-cell width 1/128, full length four.
    remainder = F(4*2**40, 8**(DEGREE+1)) / (1-F(1, 8))
    later_indices = F(1, 2**83)
    future_time = F(1, 2**128)
    out = {}
    for gamma, value in total.items():
        # Only Re of twice the half integral represents Xi.
        value = 2*value
        value = B(value.a, 0, value.e).grow(rad(remainder+later_indices+future_time))
        out[str(gamma)] = {
            'lo_numerator': str(value.a-value.e),
            'hi_numerator': str(value.a+value.e),
            'denominator_bits': 512,
        }
    return {
        'cells': CELLS,
        'degree': DEGREE,
        'theta_terms': THETA_TERMS,
        'cauchy_remainder': [str(remainder.numerator), str(remainder.denominator)],
        'index_tail': ["1", str(2**83)],
        'time_tail': ["1", str(2**128)],
        'values': out,
    }


def validate_anchor(data):
    brackets = {'14': (F(1, 10000), F(3, 10000)),
                '15': (F(-1, 1000), F(-1, 2000))}
    for g, (lower, upper) in brackets.items():
        v = data['values'][g]
        lo = F(int(v['lo_numerator']), 2**v['denominator_bits'])
        hi = F(int(v['hi_numerator']), 2**v['denominator_bits'])
        if not (lower < lo <= hi < upper and hi-lo < F(3, 10**10)):
            raise ArithmeticError('native anchor sign enclosure failed: '+g)
    return True

if __name__ == '__main__':
    import json
    result = reconstruct()
    validate_anchor(result)
    print(json.dumps(result, sort_keys=True, indent=2))
