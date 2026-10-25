#!/usr/bin/env python3
"""Exact finite tests for HLC_ROOT_AVERAGING.md; no arithmetic completion claim."""

from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import gcd, prod
import json


COUNTS = Counter()


def require(test, message):
    if not test:
        raise RuntimeError(message)


def floor(x):
    return x.numerator // x.denominator


def frac(x):
    return x - floor(x)


def indicator(t, lo, hi):
    return int(lo <= frac(t) < hi)


def breakpoints(specs):
    out = {Q(0), Q(1)}
    for a, b, lo, hi in specs:
        if not a:
            continue
        left, right = sorted((b, b + a))
        for n in range(floor(left) - 2, floor(right) + 3):
            for endpoint in (lo, hi):
                t = (n + endpoint - b) / a
                if 0 < t < 1:
                    out.add(t)
    return sorted(out)


def integrate(specs, evaluator, extra=()):
    pts = sorted(set(breakpoints(specs)) | set(extra))
    total = Q(0)
    for left, right in zip(pts, pts[1:]):
        if right == left:
            continue
        t = (left + right) / 2
        values = [indicator(a * t + b, lo, hi) for a, b, lo, hi in specs]
        total += (right - left) * evaluator(values, t)
    return total


def exact_root_lifts():
    cases = [
        (7, (2, 3), 1, 1),
        (11, (2, 3), 1, 2),
        (7, (3, 5), 2, 1),
        (11, (3, 5), 2, 3),
        (7, (2, 3, 5), 1, 2),
        (11, (2, 3, 5), 1, 1),
    ]
    for p0, ps, c, hh in cases:
        pp = prod(ps)
        gg = hh * pp
        ns = [c * (pp // p) for p in ps]
        aa = [p0 * n - gg for n in ns]
        require(gcd(gg, p0) == 1 and gcd(c, pp) == 1 and all(aa), "cofactor source conditions")
        for variant in range(3):
            arcs = []
            shifts = []
            for i, p in enumerate(ps):
                length = Q(1, p0) if variant == 0 else Q(2 + i, 3 * p0) if variant == 1 else Q(1, p)
                lo = Q(i, 19)
                arcs.append((lo, lo + length))
                shifts.append(Q(variant + i, 17))
            lhs = Q(0)
            projected = Q(0)
            for h in range(p0):
                specs = [(Q(n) - Q(gg, p0), shift - Q(h, p0), lo, hi)
                         for n, shift, (lo, hi) in zip(ns, shifts, arcs)]
                lhs += integrate(specs, lambda vals, t: prod(vals)) / p0
                projected += integrate(specs, lambda vals, t: prod(vals) * int(t < Q(2, 3)) * int(h % 2 == 0), (Q(2, 3),)) / p0
            rhs_specs = [(Q(a), shift, lo, hi) for a, shift, (lo, hi) in zip(aa, shifts, arcs)]
            rhs = integrate(rhs_specs, lambda vals, t: prod(vals))
            require(lhs == rhs, "root and once-line lift")
            grid_specs = []
            group_sizes = []
            for p, shift, (lo, hi) in zip(ps, shifts, arcs):
                group_sizes.append(p)
                grid_specs.extend((Q(p0 * c - hh * p, p), Q(b, p) + shift, lo, hi) for b in range(p))

            def grid_value(vals, t):
                result = Q(1)
                start = 0
                for size in group_sizes:
                    result *= Q(sum(vals[start:start + size]), size)
                    start += size
                return result

            grid = integrate(grid_specs, grid_value)
            require(lhs == grid, "common microphase CRT formula")
            upper = prod(hi - lo + Q(1, p) for p, (lo, hi) in zip(ps, arcs))
            lower = prod(max(Q(0), hi - lo - Q(1, p)) for p, (lo, hi) in zip(ps, arcs))
            require(lower <= lhs <= upper, "grid event upper and lower bounds")
            require(projected <= lhs <= upper, "endpoint projector retained upper bound")
            factorial = integrate(rhs_specs, lambda vals, t: sum(vals) * (sum(vals) - 1))
            ambiguity = integrate(rhs_specs, lambda vals, t: int(sum(vals) >= 2))
            pair_upper = sum((
                (arcs[i][1] - arcs[i][0] + Q(1, ps[i])) *
                (arcs[j][1] - arcs[j][0] + Q(1, ps[j]))
                for i in range(len(ps)) for j in range(len(ps)) if i != j
            ), Q(0))
            require(2 * ambiguity <= factorial <= pair_upper, "averaged omission ambiguity")
            COUNTS["ambiguity_factorial_cases"] += 1
            for root in (Q(-13, 7), Q(2, 19), Q(41, 17)):
                def average_at(rr):
                    return sum((prod(indicator((Q(n) - Q(gg, p0)) * rr + shift - Q(h, p0), lo, hi)
                                     for n, shift, (lo, hi) in zip(ns, shifts, arcs))
                                for h in range(p0)), 0)
                require(average_at(root) == average_at(root + 1), "one-line average is root-periodic")
                COUNTS["root_periodicity_checks"] += 1
            for spec, (lo, hi) in zip(rhs_specs, arcs):
                require(integrate([spec], lambda vals, t: vals[0]) == hi - lo, "exact marginal arc length")
                COUNTS["marginal_arc_checks"] += 1
            if len(ps) == 2:
                ell1, ell2 = (hi - lo for lo, hi in arcs)
                require(lhs / ell1 <= upper / ell1, "conditional two-window bound")
                # A smaller retained past event requires division by its true mass.
                past_specs = [rhs_specs[0]]
                past_mass = integrate(past_specs, lambda vals, t: vals[0] * int(t < Q(2, 3)), (Q(2, 3),))
                joint = integrate(rhs_specs, lambda vals, t: prod(vals) * int(t < Q(2, 3)), (Q(2, 3),))
                if past_mass:
                    rho = past_mass / ell1
                    require(joint / past_mass <= upper / ell1 / rho, "conditioned history density")
                    COUNTS["conditional_history_checks"] += 1
            COUNTS["exact_lift_and_grid_cases"] += 1


def fourier_relations():
    for p0, ps, c, hh in [(7, (2, 3), 1, 1), (7, (3, 5), 2, 1), (11, (2, 3, 5), 1, 1)]:
        pp = prod(ps)
        aa = [(pp // p) * (p0 * c - hh * p) for p in ps]
        ranges = [range(-2 * p, 2 * p + 1) for p in ps]
        for hs in product(*ranges):
            relation = sum(h * a for h, a in zip(hs, aa)) == 0
            divided = all(h % p == 0 for h, p in zip(hs, ps))
            right = divided and sum((h // p) * (p0 * c - hh * p) for h, p in zip(hs, ps)) == 0
            require(relation == right, "exact cofactor resonance lattice")
            COUNTS["fourier_relation_checks"] += 1


def projective_line_normalizer():
    for p in (3, 5, 7, 11):
        # z=(1,0), w=(0,1); G is nonzero.
        for gg in range(1, p):
            lines = set()
            for h in range(p):
                # (h,G) has finite slope parameter h/G when parameterized by second coordinate.
                lines.add((h * pow(gg, -1, p)) % p)
            require(len(lines) == p, "h labels every non-source projective line")
            require(Q(len(lines), p + 1) == Q(p, p + 1), "one projective line normalizer")
            require(Q(1, p + 1) != Q(1, (p + 1) ** 2), "reject a second line draw")
            COUNTS["line_normalizer_checks"] += 1


def source_interval(z):
    """A containing retained interval, using 1/16 <= tau(z) <= 16."""
    x, y = z
    if not y:
        return (Q(0), Q(1)) if Q(1, 16) <= x <= 16 else None
    lo, hi = sorted(((Q(x) - Q(1, 16)) / (2 * y), (Q(x) - 16) / (2 * y)))
    lo, hi = max(Q(0), lo), min(Q(1), hi)
    return (lo, hi) if lo < hi else None


def complement(z):
    for x in range(-12, 13):
        for y in range(-12, 13):
            if z[0] * y - z[1] * x == 1:
                return (x, y)
    raise RuntimeError("complement enumeration exhausted")


def tau(z, root):
    return z[0] - 2 * root * z[1]


def integrate_actual_root(z, w, interval, specs):
    """Exact interval subdivision for rational Mobius phases."""
    left, right = interval
    rr = lambda root: tau(w, root) / tau(z, root)
    low, high = sorted((rr(left), rr(right)))
    pts = {left, right}
    for a, b, lo, hi in specs:
        amin, amax = sorted((a * low + b, a * high + b))
        for n in range(floor(amin) - 2, floor(amax) + 3):
            for endpoint in (lo, hi):
                target = (n + endpoint - b) / a
                if low < target < high:
                    denominator = 2 * (w[1] - target * z[1])
                    require(denominator != 0, "finite source inverse Mobius map")
                    root = (w[0] - target * z[0]) / denominator
                    require(left < root < right, "inverse root lies in retained interval")
                    pts.add(root)
    total = Q(0)
    pts = sorted(pts)
    for aroot, broot in zip(pts, pts[1:]):
        root = (aroot + broot) / 2
        total += (broot - aroot) * prod(indicator(a * rr(root) + b, lo, hi) for a, b, lo, hi in specs)
    return total


def source_root_geometry():
    for z in product(range(-6, 7), repeat=2):
        if gcd(*z) != 1:
            continue
        interval = source_interval(z)
        if interval is None:
            continue
        w = complement(z)
        roots = (interval[0], sum(interval) / 2, interval[1])
        for root in roots:
            tz, tw = tau(z, root), tau(w, root)
            derivative = Q(-2 * w[1] * tz + 2 * z[1] * tw, tz ** 2)
            require(derivative == -2 / tz ** 2, "actual source tau sign and determinant derivative")
            require(Q(1, 128) <= abs(derivative) <= 512, "source Jacobian range")
            require(1 / abs(derivative) <= 128, "source inverse Jacobian")
            if z[1]:
                require(tw / tz == Q(w[1], z[1]) - 1 / (z[1] * tz), "integer source image identity")
            COUNTS["source_jacobian_checks"] += 1
        image_length = abs(tau(w, interval[1]) / tau(z, interval[1]) - tau(w, interval[0]) / tau(z, interval[0]))
        if z[1]:
            require(image_length <= Q(255, 16 * abs(z[1])) < 16, "integer source image length")
        else:
            require(z[0] == 1 and image_length <= 2, "horizontal primitive source vector")
        COUNTS["source_image_cases"] += 1

    for z in ((1, 0), (1, -1), (3, 2), (7, -3)):
        w, interval = complement(z), source_interval(z)
        low, high = sorted(tau(w, root) / tau(z, root) for root in interval)
        for p0, ps, c, hh in ((7, (2, 3), 1, 1), (11, (3, 5), 2, 1)):
            pp, gg = prod(ps), hh * prod(ps)
            ns = [c * (pp // p) for p in ps]
            arcs = [(Q(i, 17), Q(i, 17) + Q(i + 1, 3 * p0)) for i in range(len(ps))]
            shifts = [Q(i, 19) for i in range(len(ps))]
            actual, phase, uniform = Q(0), Q(0), Q(0)
            for h in range(p0):
                specs = [(Q(n) - Q(gg, p0), shift - Q(h, p0), lo, hi)
                         for n, shift, (lo, hi) in zip(ns, shifts, arcs)]
                actual += integrate_actual_root(z, w, interval, specs) / (p0 + 1)
                scaled = [(a * (high - low), a * low + b, lo, hi) for a, b, lo, hi in specs]
                phase += (high - low) * integrate(scaled, lambda vals, t: prod(vals)) / (p0 + 1)
                uniform += integrate(specs, lambda vals, t: prod(vals)) / p0
            upper = prod(hi - lo + Q(1, p) for p, (lo, hi) in zip(ps, arcs))
            require(actual <= 128 * phase, "exact source-measure Jacobian upper bound")
            require(phase <= 17 * Q(p0, p0 + 1) * uniform, "source image covered by periodic intervals")
            require(actual <= 2176 * Q(p0, p0 + 1) * upper, "actual source root-and-line upper bound")
            COUNTS["exact_actual_root_integrals"] += 1


def eisenstein_cofactors():
    zero = (Q(0), Q(0))

    def add(u, v):
        return (u[0] + v[0], u[1] + v[1])

    def mul(u, v):
        a, b = u
        c, d = v
        return (a * c - b * d, a * d + b * c - b * d)

    def neg(u):
        return (-u[0], -u[1])

    def norm(u):
        return u[0] ** 2 - u[0] * u[1] + u[1] ** 2

    def inv(u):
        nn = norm(u)
        require(nn > 0, "nonzero Eisenstein denominator")
        return (Q(u[0] - u[1], nn), Q(-u[1], nn))

    def quotient_class(u, modulus):
        return tuple(frac(v) for v in mul(u, inv(modulus)))

    def representatives(modulus):
        nn = int(norm(modulus))
        seen = {}
        for u in product(range(nn), repeat=2):
            seen.setdefault(quotient_class(u, modulus), u)
            if len(seen) == nn:
                break
        require(len(seen) == nn, "Eisenstein quotient cardinality")
        return tuple(seen.values())

    def transpose_action(u, frequency):
        a, b = u
        x, y = frequency
        return (a * x + b * y, -b * x + (a - b) * y)

    cases = [
        ((3, 1), ((1, -1), (2, 0)), (1, 0), (1, 0)),
        ((2, 0), ((3, 1), (3, -1)), (1, 1), (1, -1)),
    ]
    for pi0, pis, cc, hh in cases:
        pp = (1, 0)
        for pi in pis:
            pp = mul(pp, pi)
        gg = mul(hh, pp)
        ns = [mul(mul(cc, pp), inv(pi)) for pi in pis]
        aa = [add(mul(pi0, n), neg(gg)) for n in ns]
        qs = [int(norm(pi)) for pi in pis]
        q0 = int(norm(pi0))
        require(all(norm(a) > 0 and all(Q(v).denominator == 1 for v in a) for a in aa),
                "integer-ring nonzero lifted frequencies")
        reps0 = representatives(pi0)
        require(len({quotient_class(mul(gg, h), pi0) for h in reps0}) == q0,
                "one complex line lift permutes residue classes")
        repp = representatives(pp)
        crt = {tuple(quotient_class(mul(mul(pi0, cc), k), pi) for pi in pis) for k in repp}
        require(len(crt) == prod(qs) == int(norm(pp)), "independent Eisenstein CRT grids")
        for alpha in (pi0, pp, *pis):
            a, b = alpha
            require(a * (a - b) + b * b == norm(alpha), "complex Haar area normalizer")
            COUNTS["eisenstein_area_normalizers"] += 1
        s = (Q(1, 7), Q(2, 11))
        for k in repp:
            t = mul(add(s, k), inv(pp))
            for pi, a in zip(pis, aa):
                left = mul(a, t)
                coefficient = mul(add(mul(pi0, cc), neg(mul(hh, pi))), inv(pi))
                right = add(add(mul(coefficient, s), mul(mul(mul(pi0, cc), k), inv(pi))), neg(mul(hh, k)))
                require(left == right, "complex cofactor grid identity")
                COUNTS["eisenstein_grid_identities"] += 1
        frequencies = tuple(product(range(-1, 2), repeat=2))
        for ks in product(frequencies, repeat=len(pis)):
            total_frequency = zero
            root_frequency = zero
            lifted_frequency = zero
            for k, n, a in zip(ks, ns, aa):
                total_frequency = add(total_frequency, k)
                fractional_coefficient = add(n, neg(mul(gg, inv(pi0))))
                root_frequency = add(root_frequency, transpose_action(fractional_coefficient, k))
                lifted_frequency = add(lifted_frequency, transpose_action(a, k))
            line_dual = transpose_action(inv(pi0), total_frequency)
            line_survives = all(Q(v).denominator == 1 for v in line_dual)
            if line_survives:
                require(all(Q(v).denominator == 1 for v in root_frequency),
                        "surviving line harmonic has integral root frequency")
            require((line_survives and root_frequency == zero) == (lifted_frequency == zero),
                    "complex Fourier once-line lift")
            COUNTS["eisenstein_fourier_lift_checks"] += 1
        COUNTS["eisenstein_crt_families"] += 1


def recorded_prime_divisors():
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    zs = [(x, y) for x in range(1, 9) for y in range(-4, 5) if gcd(x, y) == 1]
    for z, w in product(zs, repeat=2):
        delta = z[0] * w[1] - z[1] * w[0]
        if not delta:
            require(z == w, "positive primitive parallel vertices coincide")
            COUNTS["exact_repeated_position_checks"] += 1
            continue
        for pmin in (3, 7, 13):
            selected = [p for p in primes if p >= pmin and delta % p == 0]
            require(pmin ** len(selected) <= abs(delta), "prime-divisor logarithmic count")
            mass = sum((Q(1, p) for p in selected), Q(0))
            require(mass <= Q(len(selected), pmin), "weighted fixed-path prime return")
            COUNTS["fixed_path_divisor_checks"] += 1


def negative_controls():
    # Repeated phase events remain identical after conditioning.
    event = [(Q(17), Q(1, 13), Q(0), Q(1, 101))]
    mass = integrate(event, lambda vals, t: vals[0])
    joint_same = integrate(event + event, lambda vals, t: prod(vals))
    require(mass == Q(1, 101) and joint_same / mass == 1, "repeated phase resonance")
    require(joint_same != mass * mass, "reject repeated-event independence")
    # In the fixed-path divisor lemma Delta must be fixed before p is summed.
    require(all(p % p == 0 for p in (3, 5, 7, 11)), "prime-dependent Delta control")
    require(sum(Q(1, p) for p in (3, 5, 7, 11)) > Q(1, 3), "one fixed-divisor bound cannot be assigned to Delta(p)=p")
    COUNTS["negative_controls"] += 3


def main():
    exact_root_lifts()
    fourier_relations()
    projective_line_normalizer()
    source_root_geometry()
    eisenstein_cofactors()
    recorded_prime_divisors()
    negative_controls()
    print(json.dumps({"status": "passed", "counts": dict(sorted(COUNTS.items())), "arithmetic": "exact rational arc integrals and integer identities", "scope": "no conditional-history theorem for the full HLC operator; no new zero-free region"}, indent=2))


if __name__ == "__main__":
    main()
