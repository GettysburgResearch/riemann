"""Ordinary high-precision continuation of STAR26 with a variable bias rule.

Exploration only; imported midpoint targets do NOT certify a new theta root.
"""
import argparse
import json
import math
from pathlib import Path
import subprocess
import mpmath as mp

mp.mp.dps = 65
STAR = '4c7898432546814812b2be8c72fc199e294354d1'
ICR = '0640c9c59be0bf20c18258460a7517fb09728e82'


def old_json(sha, path):
    return json.loads(subprocess.check_output(['git', 'show', sha + ':' + path], text=True))


params = old_json(STAR, 'standalone/2026-09-12-astra-weight-adapted-star/parameters.json')
native = old_json(ICR, 'standalone/2026-09-12-astra-interacting-cluster-realization/result.json')
COUNTS = params['counts']
ACTIVE = params['active']
center = [mp.mpf(x) for x in params['centers']]
target = [mp.mpf(a + b) / mp.mpf(2)**321
          for a, b in native['standardized_cumulant_ratios']]


class Dual:
    def __init__(self, value, deriv=None):
        self.value = mp.mpf(value)
        self.deriv = [mp.mpf(0)] * len(ACTIVE) if deriv is None else list(deriv)

    def __add__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value + other.value, [a + b for a, b in zip(self.deriv, other.deriv)])

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.value, [-a for a in self.deriv])

    def __sub__(self, other):
        return self + (-other if isinstance(other, Dual) else -mp.mpf(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.value * other.value,
                    [a * other.value + self.value * b for a, b in zip(self.deriv, other.deriv)])

    __rmul__ = __mul__


C = [[], [0, 1]]
for order in range(1, 16):
    poly = C[-1]
    nxt = [0] * (len(poly) + 1)
    for j in range(1, len(poly)):
        nxt[j - 1] += j * poly[j]
        nxt[j + 1] -= j * poly[j]
    C.append(nxt)


def poly_eval(poly, x):
    val = x * 0
    for a in reversed(poly):
        val = val * x + a
    return val


FAIR = [0] + [poly[0] for poly in C[1:]]


def graph(weights, k, owner=None, extra=0, biases=None):
    zero = weights[0] * 0
    one = zero + 1
    conditional_k = [zero] * 17
    conditional_k[1] = weights[-1]
    for index, (count, a) in enumerate(zip(COUNTS, weights[:-1])):
        power = one
        for n in range(1, 17):
            power = power * a
            bias = (k * a + (extra if index == owner else 0)) if biases is None else biases[index]
            conditional_k[n] += count * power * poly_eval(C[n], bias)
    conditional_m = [one]
    for n in range(1, 17):
        conditional_m.append(sum((math.comb(n - 1, j - 1) * conditional_k[j] *
                                  conditional_m[n - j] for j in range(1, n + 1)), zero))
    moments = [conditional_m[n] if n % 2 == 0 else zero for n in range(17)]
    cumulants = [zero] * 17
    for n in range(1, 17):
        cumulants[n] = moments[n] - sum((math.comb(n - 1, j - 1) * cumulants[j] *
                                        moments[n - j] for j in range(1, n)), zero)
    return [cumulants[2*r] * (mp.mpf(1) / FAIR[2*r]) for r in range(1, 9)]


def evaluate(active, k, owner=None, extra=0):
    weights = list(center)
    for j, index in enumerate(ACTIVE):
        deriv = [mp.mpf(0)] * len(ACTIVE)
        deriv[j] = mp.mpf(1)
        weights[index] = Dual(active[j], deriv)
    weights = [w if isinstance(w, Dual) else Dual(w) for w in weights]
    result = graph(weights, k, owner, extra)
    residual = mp.matrix([(result[r].value - target[r]) / target[r] for r in range(7)])
    jacobian = mp.matrix([[d / target[r] for d in result[r].deriv] for r in range(7)])
    return residual, jacobian, result, weights


def solve(active, k, owner=None, extra=0):
    active = mp.matrix(active)
    for iteration in range(35):
        residual, jacobian, result, weights = evaluate(active, k, owner, extra)
        norm = max(abs(x) for x in residual)
        if norm < mp.mpf('1e-48'):
            allweights = [w.value for w in weights]
            biases = [k * w + (extra if i == owner else 0) for i,w in enumerate(allweights[:-1])]
            if min(allweights) <= 0 or min(biases) < 0 or max(biases) >= 1:
                raise ValueError('root leaves positive-weight/ferromagnetic domain')
            error16 = FAIR[16] * (result[7].value - target[7])
            return list(active), allweights, error16, norm
        step = (mp.lu_solve(jacobian, -residual) if jacobian.rows == jacobian.cols else
                jacobian.T * mp.lu_solve(jacobian * jacobian.T, -residual))
        found = False
        for damp in [mp.mpf(2)**(-j) for j in range(16)]:
            candidate = active + damp * step
            if min(candidate) <= 0:
                continue
            candidate_residual = evaluate(candidate, k, owner, extra)[0]
            if max(abs(v) for v in candidate_residual) < norm:
                active = candidate
                found = True
                break
        if not found:
            raise ValueError('line search stalled at normalized residual ' + mp.nstr(norm, 12))
    raise ValueError('iteration budget reached')


def run(values):
    active = [center[i] for i in ACTIVE]
    rows = []
    for value in values:
        k = mp.mpf(value)
        try:
            active, weights, error, norm = solve(active, k)
            row = {'k': value, 'moment16_error': mp.nstr(error, 40),
                   'normalized_residual': mp.nstr(norm, 8),
                   'weights': [mp.nstr(w, 65) for w in weights]}
            print(value, mp.nstr(error, 25), flush=True)
        except (ValueError, ZeroDivisionError) as exc:
            row = {'k': value, 'failure': str(exc)}
            print(value, str(exc), flush=True)
            rows.append(row)
            break
        rows.append(row)
    return rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--direction', choices=['up', 'down'], default='up')
    args = parser.parse_args()
    grid = (['.01', '.012', '.015', '.02', '.03', '.05', '.08', '.1', '.15', '.2', '.3', '.5', '1']
            if args.direction == 'up' else ['.01', '.008', '.005', '.002', '0'])
    result = {'status': 'nondirected exploration, not a root certificate',
              'star_source': STAR, 'target_source': ICR,
              'direction': args.direction, 'rows': run(grid)}
    Path(__file__).with_name('scout-' + args.direction + '.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
