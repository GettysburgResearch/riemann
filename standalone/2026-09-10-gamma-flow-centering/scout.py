"""NON-CERTIFYING scout of the new centered positive sources. Requires mpmath.
Gauss--Legendre after t=T sin(theta); no outward quadrature or root-count bound.
A positive truncated density series stabilizes endpoint cancellation. Its omitted
terms are NOT certified here. Different node counts use the same backend.
Returned roots are tracks from specified guesses, not an ordered zero census.
"""
import mpmath as mp, json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
mp.mp.dps = 90
nodes = []
weights = []

def data(N, order):
    nodes, weights = mp.gauss_quadrature(order, 'legendre')
    tau = mp.pi ** 2 / 3 - 2 * mp.fsum((mp.mpf(1) / (n * n) for n in range(1, N + 1)))
    T = mp.log(mp.pi / tau) / 2
    rows = []
    for n in range(1, N + 1):
        B = Q(2 * factorial(N) ** 2, factorial(N - n) * factorial(N + n)) ** 2
        S = sum((Q(1, k * k - n * n) for k in range(1, N + 1) if k != n), Q(0))
        rows.append((n * n, mp.mpf(B.numerator) / B.denominator, mp.mpf(S.numerator) / S.denominator))
    m = 2 * N
    K = 160
    hk = [1] + [0] * K
    for n in range(1, N + 1):
        v = N * N - n * n
        for repeat in range(2):
            for k in range(1, K + 1):
                hk[k] += v * hk[k - 1]
    C = mp.mpf(factorial(N) ** 4) / factorial(m - 1)

    def f(x):
        if x <= 0:
            return mp.mpf(0)
        if x * N * N < 2:
            term = sm = mp.mpf(1)
            for k in range(1, K + 1):
                term *= x / (m - 1 + k)
                sm += term * hk[k]
            return C * x ** (m - 1) * mp.exp(-N * N * x) * sm
        ans = mp.fsum((a * a * B * (x - 2 * s) * mp.exp(-a * x) for a, B, s in rows))
        if ans <= 0:
            raise RuntimeError('lost positivity')
        return ans
    out = []
    for r, w in zip(nodes, weights):
        th = (r + 1) * mp.pi / 4
        t = T * mp.sin(th)
        x = mp.pi * mp.exp(2 * t) - tau
        y = mp.pi * mp.exp(-2 * t) - tau
        out.append((t, w * mp.pi / 4 * T * mp.cos(th) * mp.sqrt(f(x) * f(y))))
    norm = mp.fsum((w for t, w in out))
    return ([(t, w / norm) for t, w in out], tau, T)

def run():
    rows = []
    for N, order in [(4, 192), (5, 192), (5, 256), (8, 192), (16, 192)]:
        p, tau, T = data(N, order)
        f = lambda z: mp.fsum((w * mp.cos(z * t) for t, w in p))
        root = mp.findroot(f, (mp.mpc('30.4', '.65'), mp.mpc('30.45', '.66')), maxsteps=80)
        tracked = mp.findroot(f, (mp.mpf('14'), mp.mpf('14.2')))
        rows.append({'N': N, 'order': order, 'root_from_14_guess': mp.nstr(tracked, 45), 'root_from_complex_guess': mp.nstr(root, 45), 'tau': mp.nstr(tau, 35), 'support_endpoint': mp.nstr(T, 35)})
    return {'status': 'NONCERTIFYING_CENTERED_SOURCE_SCOUT', 'mpmath_version': mp.__version__, 'decimal_precision': 90, 'small_x_positive_series_terms': 160, 'quadrature_error_certified': False, 'root_count_certified': False, 'complete_zero_census': False, 'rh_proved': False, 'rows': rows}
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(run(), sort_keys=True, indent=2) + '\n')
    print('SCOUT_COMPLETE_NOT_A_CERTIFICATE')
