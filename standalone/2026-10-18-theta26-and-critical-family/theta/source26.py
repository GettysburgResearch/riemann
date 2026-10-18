#!/usr/bin/env python3
"""Complete directed theta moments through 26, independent of a moment table.

Uses an authenticated inherited integer-interval arithmetic implementation at
increased precision and Taylor degree; all new truncation parameters and
remainders are explicit below. No change is made to the inherited source.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import argparse
import hashlib
import importlib.util
import json

COUNTS = (40, 29, 23, 18, 14, 12, 9, 7, 5, 3, 2)
BITS = 512
DEGREE = 220
MAX_MOMENT = 26
PRIMITIVE_BLOB = 'c32015f110d10186538ffabcb4689ba5bbc060d0'
DEFAULT_SOURCE = (Path(__file__).resolve().parents[2] /
                  '2026-10-18-theta20-and-native-cancellation/theta')


def load_primitive(source):
    path = Path(source) / 'pr886_primitive.py'
    raw = path.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if blob != PRIMITIVE_BLOB:
        raise ValueError('inherited primitive blob differs from pinned PR994')
    spec = importlib.util.spec_from_file_location('theta26_interval_backend', path)
    b = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b)
    b.BITS = BITS
    b.SCALE = 1 << BITS
    b.DEGREE = DEGREE
    return b, hashlib.sha256(raw).hexdigest()


def reconstruct(source, progress=False):
    b, primitive_sha = load_primitive(source)
    I = b.I
    pi = b.pi_interval()
    b.require(pi.lo > 3*b.SCALE and pi.hi < 4*b.SCALE, 'pi enclosure')
    js = tuple(range(0, MAX_MOMENT + 1, 2))
    total = {j: I.coerce(0) for j in js}
    for n, count in enumerate(COUNTS, 1):
        for k in range(count):
            center = F(2*k + 1, 32)
            density = b.cell_density(n, center, pi)
            for j in js:
                total[j] += b.integrate_moment(density, center, j)
        if progress:
            print('THETA_INDEX_COMPLETE', n, count, flush=True)
    tails = {}
    for j in js:
        # On each radius-1/8 Cauchy circle the complete nth density has
        # modulus <10^16: n<=11, q<484, Re(t)<21/8, |Im(t)|<=1/8.
        # Half-cell radius 1/32; total full-line cell length <32; |t|<=5/2.
        taylor = I.coerce(F(32*10**16, 4**(DEGREE+1)) * F(5, 2)**j / F(3, 4))
        time = I.coerce(0)
        for n, count in enumerate(COUNTS, 1):
            U = F(count, 16)
            q = pi*n*n
            E = b.exp(2*I.coerce(U))
            lam = 2*q*E - F(9, 2)
            b.require(lam.lo > 0, 'positive time-tail exponent')
            time += 8*q*q*b.exp(F(9, 2)*I.coerce(U) - q*E) * sum(
                (comb(j, k)*U**(j-k)*factorial(k)/lam**(k+1)
                 for k in range(j+1)), I.coerce(0))
        # For n>=12 consecutive n^4 exp(-pi n^2) terms have ratio <1/2.
        # The denominator increases, so a geometric majorant costs a factor2.
        N = len(COUNTS) + 1
        index = 16*pi*pi*N**4*b.exp(-N*N*pi)*factorial(j)/(2*N*N*pi-F(9, 2))**(j+1)
        total[j] = I(total[j].lo-taylor.hi,
                     total[j].hi+taylor.hi+time.hi+index.hi)
        tails[str(j)] = {'taylor': taylor.record(), 'time': time.record(), 'index': index.record()}
    b.require(total[0].lo > 0, 'positive theta mass')
    mu = {j: total[j]/total[0] for j in js[1:]}
    variance = mu[2]
    mom = [I.coerce(int(j == 0)) for j in range(MAX_MOMENT+1)]
    for r in range(1, MAX_MOMENT//2+1):
        mom[2*r] = mu[2*r]/variance**r
    kap = b.cumulants(mom)
    unit = b.cumulants([F(int(j % 2 == 0)) for j in range(MAX_MOMENT+1)])
    ss = [kap[2*r]/unit[2*r] for r in range(1, MAX_MOMENT//2+1)]
    return {
        'schema': 'theta26.complete-source.v1',
        'status': 'DIRECTED_COMPLETE_SOURCE',
        'primitive_git_blob': PRIMITIVE_BLOB,
        'primitive_sha256': primitive_sha,
        'bits': BITS, 'degree': DEGREE, 'max_moment': MAX_MOMENT,
        'counts': list(COUNTS), 'cells': sum(COUNTS),
        'explicit_theta_indices': len(COUNTS),
        'raw': {str(j): total[j].record() for j in js},
        'variance': variance.record(),
        'standardized_moments': [x.record() for x in mom],
        'standardized_cumulant_ratios': [x.record() for x in ss],
        'tails': tails,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=DEFAULT_SOURCE)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('theta26_source.json'))
    args = parser.parse_args()
    result = reconstruct(args.source, progress=True)
    text = json.dumps(result, sort_keys=True, separators=(',', ':')) + '\n'
    args.output.write_text(text)
    print('COMPLETE_THETA26_SOURCE', hashlib.sha256(text.encode()).hexdigest())
    for r, (lo, hi) in enumerate(result['standardized_cumulant_ratios'], 1):
        print('RATIO', r, 'WIDTH', float(F(hi-lo, 1 << BITS)))


if __name__ == '__main__':
    main()
