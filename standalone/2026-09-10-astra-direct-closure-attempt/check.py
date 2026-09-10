#!/usr/bin/env python3
"""Bounded exact algebra and payload authentication, NOT an RH verifier."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import sys

FILES = frozenset({
    'ATTEMPT.md', 'README.md', 'SOURCES.json', 'VALIDATION.md',
    'check.py', 'test_check.py', 'SHA256SUMS',
})
PARENT = '4b8fa9abfa9aac5ed1feb7f30acaeeb418ed405c'
DET_SOURCE = 'f0e34780f4fe91bd5d07e791e8855189838c3df5'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def reject_number(value):
    raise ValueError('floating/nonfinite JSON number forbidden')


def load_json(path: Path):
    require(path.is_file() and not path.is_symlink(), 'not a regular JSON file')
    raw = path.read_bytes()
    require(len(raw) < 1_000_000, 'oversized JSON')
    return json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object,
                      parse_float=reject_number, parse_constant=reject_number)


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def authenticate(root: Path) -> None:
    entries = list(root.iterdir())
    require({p.name for p in entries} == FILES, 'wrong payload inventory')
    require(all(p.is_file() and not p.is_symlink() for p in entries),
            'nonregular or symlink payload')
    rows = {}
    for line in (root / 'SHA256SUMS').read_text('ascii').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)', line)
        require(match is not None, 'malformed manifest row')
        digest, name = match.groups()
        require(name not in rows, 'duplicate manifest row')
        rows[name] = digest
    require(set(rows) == FILES - {'SHA256SUMS'}, 'wrong manifest coverage')
    for name, expected in rows.items():
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        require(actual == expected, 'payload hash mismatch: ' + name)
    sources = load_json(root / 'SOURCES.json')
    require(sources['rh_proved'] is False, 'false RH status')
    require(sources['parent']['commit'] == PARENT, 'wrong Xi source')
    require(sources['determinant']['commit'] == DET_SOURCE, 'wrong determinant source')
    require(sources['parent']['primitive_replay_this_pass'] is False,
            'unperformed primitive replay')


@dataclass(frozen=True)
class C:
    """Gaussian rational; no binary floating point."""
    re: F
    im: F = F(0)

    def __add__(self, other: C) -> C:
        return C(self.re + other.re, self.im + other.im)

    def __sub__(self, other: C) -> C:
        return C(self.re - other.re, self.im - other.im)

    def __mul__(self, other: C) -> C:
        return C(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    def scale(self, value: F) -> C:
        return C(value * self.re, value * self.im)

    def conj(self) -> C:
        return C(self.re, -self.im)

    def norm(self) -> F:
        return self.re * self.re + self.im * self.im


def lag(q: C, qp: C, qpp: C) -> F:
    return qp.norm() - (qpp * q.conj()).re


def reconstruct() -> dict:
    # Reconstruct the expanded product from exact first/second jets.
    for j in range(64):
        q = C(F(j % 7 - 3, 3), F(j % 5 - 2, 2))
        qp = C(F(j % 11 - 5, 5), F(j % 3 - 1, 7))
        qpp = C(F(j % 13 - 6, 11), F(j % 7 - 3, 5))
        a = C(F(j % 5 - 2, 4), F(j % 11 - 5, 3))
        b = C(F(j % 17 - 8, 7), F(j % 13 - 6, 9))
        h = C(F(j % 3 + 1, 2), F(j % 5 - 2, 3))
        f = h * q
        fp = h * (qp + a * q)
        fpp = h * (qpp + (a * qp).scale(F(2)) + b * q)
        expected = (lag(q, qp, qpp) + (a.norm() - b.re) * q.norm()
                    + 4 * a.im * (qp * q.conj()).im)
        require(lag(f, fp, fpp) == h.norm() * expected,
                'covariant Laguerre identity')
        # d/dy of |q|^2 = 2 Re(i qprime conjugate(q)).
        iqp = C(-qp.im, qp.re)
        require(2 * (iqp * q.conj()).re == -2 * (qp * q.conj()).im,
                'vertical derivative sign')
        require((fp * f.conj()).im / h.norm()
                == (qp * q.conj()).im + a.im * q.norm(),
                'first-order phase transport')

    for power in range(1, 17):
        c = F((-1) ** power * (power + 1), power + 2)
        # At x=1 for c*x^-power, (gprime)^2-g*gsecond=-power*c^2.
        require((-power*c)**2 - c*(power*(power+1)*c) == -power*c*c,
                'power-tail sign')
        require((-power*c)**2 - c*(power*(power+1)*c) < 0,
                'strict power-tail negativity')
    for epsilon in (F(-2), F(-1, 8), F(1, 16), F(3)):
        a = F(5, 7)
        c = 2*epsilon*a
        require((-2*c)**2-c*(6*c) == -8*epsilon*epsilon*a*a,
                'theta-tail leading coefficient')

    # Exact arithmetic in Q[sqrt(5)] represented by pairs.
    def mul(x, y):
        return (x[0]*y[0] + 5*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
    r = (F(3,2), F(1,2))
    rinv = (F(3,2), F(-1,2))
    rr = mul(r, r)
    require(mul(r, rinv) == (F(1), F(0)), 'quadratic inverse')
    require((r[0]+rinv[0], r[1]+rinv[1]) == (F(3), F(0)), 'quadratic sum')
    require((rr[0]-3*r[0]+1, rr[1]-3*r[1]) == (F(0), F(0)),
            'r^2-3r+1')
    require(1+3+1 == 5, 'mixture normalization')
    for a in range(1, 5):
        for b in range(1, 5):
            z = C(F(a), F(b))
            inverse = z.conj().scale(1/z.norm())
            require((inverse*inverse).im == F(-2*a*b, (a*a+b*b)**2),
                    'nonreal reciprocal-square eigenvalue')
            require((inverse*inverse).im < 0, 'nonreal eigenvalue sign')
    return {
        'schema': 'DCA26-bounded-algebra-v1',
        'rh_proved': False,
        'global_phase_proved': False,
        'actual_xi_evaluated': False,
        'parent_quadrature_replayed': False,
        'groups': {
            'covariant_and_first_order_jet_panels': 64,
            'inverse_power_models': 16,
            'theta_leading_coefficient_panels': 4,
            'quadratic_factor_identities': 4,
            'reciprocal_square_sign_panels': 16,
        },
        'scope': 'Exact finite algebra and file authentication; not analytic proof verification.',
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expect', type=Path, help='optional exact typed JSON receipt')
    args = parser.parse_args()
    try:
        authenticate(Path(__file__).resolve().parent)
        result = reconstruct()
        if args.expect is not None:
            expected = load_json(args.expect)
            require(canonical(expected) == canonical(result), 'receipt mismatch')
        print(json.dumps(result, sort_keys=True, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('REJECT: ' + str(exc), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
