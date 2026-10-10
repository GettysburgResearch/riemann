#!/usr/bin/env python3
"""Exact algebra and rational-bound checks for tail_zero_criteria.md.

This checks copied local polynomial identities and affine exponent comparisons.
It does not authenticate the imported manuscript, build Lean, estimate a prime
sum, or certify a zero-free region. Python standard library only.
"""
from fractions import Fraction as F
import argparse
import json
from pathlib import Path

_accepted = 0


def check(condition, detail):
    """An acceptance gate that remains active under python -O."""
    global _accepted
    if not condition:
        raise RuntimeError(f"Exact check failed: {detail}")
    _accepted += 1


class P:
    """Sparse polynomial in D,V,W,R,t with exact rational coefficients."""
    size = 5

    def __init__(self, terms):
        self.terms = {k: F(v) for k, v in terms.items() if v}

    @classmethod
    def scalar(cls, value):
        return cls({(0,) * cls.size: F(value)})

    @classmethod
    def var(cls, index):
        powers = [0] * cls.size
        powers[index] = 1
        return cls({tuple(powers): F(1)})

    def __add__(self, other):
        if not isinstance(other, P):
            other = P.scalar(other)
        out = self.terms.copy()
        for k, v in other.terms.items():
            out[k] = out.get(k, F(0)) + v
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, P) else -F(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if not isinstance(other, P):
            other = P.scalar(other)
        out = {}
        for ka, va in self.terms.items():
            for kb, vb in other.terms.items():
                k = tuple(a + b for a, b in zip(ka, kb))
                out[k] = out.get(k, F(0)) + va * vb
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError("Polynomial power must be a nonnegative integer")
        out = P.scalar(1)
        for _ in range(power):
            out = out * self
        return out

    def residue_substitution(self):
        # Replace V=W=t, leaving D,R,t formal and independent.
        out = {}
        for (d, v, w, r, t), value in self.terms.items():
            k = (d, 0, 0, r, t + v + w)
            out[k] = out.get(k, F(0)) + value
        return P(out)


def affine(coef, constant):
    return F(coef), F(constant)


def val(line, alpha):
    return line[0] * alpha + line[1]


def check_envelope(name, lower, upper, leaves, candidates):
    # All pairwise intersections plus the endpoints partition the interval
    # into pieces on which every ordering of affine expressions is fixed.
    expressions = leaves + candidates
    nodes = {lower, upper}
    for a, b in expressions:
        for c, d in expressions:
            if a != c:
                x = (d - b) / (a - c)
                if lower <= x <= upper:
                    nodes.add(x)
    nodes = sorted(nodes)
    checks = 0
    for x in nodes:
        proposed = min(val(line, x) for line in candidates)
        actual = min(val(line, x) for line in leaves)
        check(proposed == actual, (name, x, proposed, actual))
        check(proposed >= 0, (name, x, proposed))
        checks += 1
    # Every candidate has positive slope or positive constant. Zero at the
    # excluded lower endpoint therefore permits strict positivity inside.
    check(all(c > 0 or (c == 0 and b > 0) for c, b in candidates),
          (name, "positive slope or positive constant"))
    check(min(val(line, upper) for line in candidates) > 0,
          (name, "strict positive right endpoint"))
    return {"interval": [str(lower), str(upper)],
            "left_endpoint_excluded": True,
            "affine_partition_nodes": [str(x) for x in nodes],
            "exact_node_comparisons": checks}


def run():
    global _accepted
    _accepted = 0
    D, V, W, R, t = [P.var(i) for i in range(5)]
    # t=1/Q. First expression is the complete j=0 P_p identity multiplied
    # by t(1-R)(1-D); all denominators have been cleared.
    source_numerator = (
        t * (1-R) * (1-V*W)
        + (1-W) * (t*R*(1-t) - (1-t)*D*W*V)
        + t*(1-V)*(1-W)*(-D+W*R)
    )
    extracted_numerator = (
        t*(1-D + D*(V+W-V*W) - V*W)
        - (1-t)*D*W*V*(1-W)
        - t*R*(t*(1-W)+W**2*(1-V))
    )
    check(not (source_numerator - extracted_numerator).terms,
          "full principal extraction polynomial")
    residue_numerator = t*(1-t**2)*(1-D+t*(D-R))
    check(not (source_numerator.residue_substitution()
               - residue_numerator).terms, "double residue polynomial")
    # Strict local nonvanishing proof uses y=Q^-1/2 in (0,1).
    y = t
    check(not (1-y-y**2+y**3 - (1-y)**2*(1+y)).terms,
          "strict local nonvanishing factorization")

    good = [affine(1, '-1/100'), affine(1, '-1/20'),
            affine(0, '47/50'), affine(6, '-401/100'),
            affine(1, '-3/50')]
    lam = [affine(6, '-401/100'), affine(1, '-3/50')]
    ram = [affine(6, '-301/100'), affine(1, '-1/20'),
           affine(1, '19/20'), affine(3, '-3/2'),
           affine(3, '-21/20'), affine(4, '-2'),
           affine(4, '-31/20'), affine(6, '-3')]
    mu = [affine(1, '-1/20'), affine(3, '-3/2')]
    selected = [affine(1, 0), affine(0, '99/100'),
                affine(5, '-301/100'), affine(0, '47/50')]
    factored = [affine(1, '-1/100'), affine(1, '-1/20'),
                affine(0, '47/50'), affine(1, '-3/50'),
                affine(6, '-301/100'), affine(6, '-211/100')]
    kappa = [affine(1, '-3/50'), affine(6, '-301/100')]
    reports = {
        "good_prime_lambda": check_envelope("lambda", F(401,600), F(1), good, lam),
        "ramified_mu": check_envelope("mu", F(401,600), F(1), ram, mu),
        "principal_selected_nu": check_envelope("nu", F(401,600), F(1), selected, selected),
        "factored_kappa": check_envelope("kappa", F(301,600), F(1), factored, kappa),
    }
    instances = {}
    for a in [F(3,4), F(4,5), F(437,500), F(7,8)]:
        instances[str(a)] = {
            "good_defect_decay": str(1+min(val(f,a) for f in lam)),
            "ramified_defect_decay": str(min(val(f,a) for f in mu)),
            "selected_error_decay": str(min(val(f,a) for f in selected)),
        }
    check(min(val(f,F(51,100)) for f in kappa) == F(1,20),
          "factored kappa at 51/100")
    check(instances['437/500'] == {
        'good_defect_decay': '907/500',
        'ramified_defect_decay': '103/125',
        'selected_error_decay': '437/500'},
        "enlarged domain exact instance 437/500")
    lx, ell, h, b = F(17,48), F(1,6), F(13,16), F(1,8)
    constant = lx/2 - 1 + h/6
    check(constant == -F(11,16), "published principal constant")
    check(F(7,8)+constant == lx/2+b/12 == F(3,16),
          "published low endpoint equality")
    check((F(3,1)+F(7,8))/6 == F(31,48), "angular mapped 7/8 threshold")
    check(6*F(3,5)-3 == F(3,5), "closed angular-family fixed point")
    return {
        "status": "passed",
        "exact_predicate_count": _accepted,
        "scope": "Exact local polynomial identities and rational inequalities; no zero-free theorem",
        "symbolic_identities": ["full_principal_extraction", "double_residue_factorization", "local_nonvanishing_factor"],
        "affine_envelopes": reports,
        "rational_instances": instances,
        "low_exponent": "3/16",
        "principal_constant": "-11/16",
        "low_endpoint_gap": "exactly beta_star - 7/8",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(run(), indent=2) + '\n'
    if args.output:
        args.output.write_text(result, encoding='utf-8')
    else:
        print(result, end='')


if __name__ == '__main__':
    main()
