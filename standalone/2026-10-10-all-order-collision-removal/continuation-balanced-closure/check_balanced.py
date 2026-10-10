#!/usr/bin/env python3
"""Exact finite checks for balanced closure; not an arithmetic moment proof."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEPENDENCY = HERE.parent / "checks" / "check_all_order.py"
DEPENDENCY_SHA = "8e5b599ec43662f6fc634e8339228f79c33b37f8385e55c30d34cb136edfc4d9"
COUNTS = Counter()


class Failure(RuntimeError):
    pass


def require(ok, group, detail=""):
    COUNTS[group] += 1
    if not ok:
        raise Failure(f"{group}: {detail}")


def load_source():
    require(hashlib.sha256(DEPENDENCY.read_bytes()).hexdigest() == DEPENDENCY_SHA,
            "source_binding", "original checker bytes")
    spec = importlib.util.spec_from_file_location("prior_exact_algebra", DEPENDENCY)
    if spec is None or spec.loader is None:
        raise Failure("Cannot load the authenticated local algebra dependency")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def mobius(n):
    out, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            out = -out
            if n % p == 0:
                return 0
        p += 1
    return -out if n > 1 else out


def necklace(a):
    m, g = sum(a), math.gcd(*a)
    return sum((F(mobius(d) * math.factorial(m // d),
                  m * math.prod(math.factorial(x // d) for x in a))
                for d in range(1, g + 1) if g % d == 0), F(0))


def cycle_checks(src):
    orbit_total = 0
    for k in range(2, 5):
        for m in range(1, 7):
            actual = Counter()
            for word in itertools.product(range(k), repeat=m):
                if any(word == word[:d] * (m // d)
                       for d in range(1, m) if m % d == 0):
                    continue
                if word != min(word[j:] + word[:j] for j in range(m)):
                    continue
                actual[tuple(word.count(i) for i in range(k))] += 1
                orbit_total += 1
            for a in src.compositions(m, k):
                ell = necklace(a)
                require(ell.denominator == 1 and ell >= 0,
                        "cycle_integrality", str(a))
                require(ell == actual[a], "independent_primitive_orbits", str(a))
        max_degree = 6
        zero = (0,) * k
        series = {zero: 1}
        for m in range(1, max_degree + 1):
            for a in src.compositions(m, k):
                ell = int(necklace(a))
                if not ell:
                    continue
                new = Counter()
                for b, value in series.items():
                    for j in range(min(ell, (max_degree - sum(b)) // m) + 1):
                        exponent = tuple(x + j * y for x, y in zip(b, a))
                        new[exponent] += value * (-1) ** j * math.comb(ell, j)
                series = {a: c for a, c in new.items() if c}
        for m in range(max_degree + 1):
            for a in src.compositions(m, k):
                target = 1 if m == 0 else (-1 if m == 1 else 0)
                require(series.get(a, 0) == target, "cycle_product", str(a))
    return orbit_total


def mass_checks(src):
    for k in range(2, 21):
        for j in range(1, 9):
            t = F(1, 2 * k * j)
            mass = 1 - (1 - k * t) / (1 - t) ** k
            bound = math.comb(k, 2) * t * t / (1 - t) ** k
            require(0 <= mass <= bound <= k * k * t * t,
                    "local_mass_bound", f"k={k},j={j}")
        for m in range(1, 6):
            delta = F(1, 2 * m)
            p0 = max((2 * k) ** 3, (48 * m * k * k) ** m)
            require(p0 >= (48 * m * k * k) ** m,
                    "cutoff_power", f"k={k},m={m}")
            # P0^(-1/m) <= 1/(48*m*k^2), checked by the integer power above.
            upper_t = k * k * 6 / delta * F(1, 48 * m * k * k)
            require(upper_t == F(1, 4), "cutoff_mass", f"k={k},m={m}")
            require(upper_t / (1 - upper_t) == F(1, 3),
                    "global_contraction_budget", f"k={k},m={m}")
    require(F(1, 1) / (1 - F(1, 3)) ** 2 == F(9, 4),
            "contraction_constants")
    require(((1 + F(1, 3)) / (1 - F(1, 3))) ** 2 == 4,
            "contraction_constants")


def norm_square(z):
    return z[0] ** 2 + z[0] * z[1] + z[1] ** 2


def finite_envelopes(src):
    seeds = (F(12), F(60), F(90))
    scales = sorted({x / src.norm_ideal(d) for x in seeds
                     for d in src.ideals_below(2 * x)})
    phase_rows = [(src.ROOTS[0], src.ROOTS[0]), (src.ROOTS[1], src.ROOTS[2]),
                  (src.ROOTS[3], src.ROOTS[3]), (src.ZERO, src.ROOTS[1]),
                  (src.ROOTS[4], src.ZERO), (src.ZERO, src.ZERO)]
    measures = [list(zip(phase_rows, map(F, (1, 1, 1, 1, 1, 1)))),
                [(phase_rows[0], F(1))],
                list(zip(phase_rows, map(F, (1, 2, 3, 4, 5, 6))))]
    a_cache = {(x, row): src.squarefree_sum(x, row) for x in scales for row in phase_rows}
    panels = []
    for k in (2, 3, 4):
        f = lambda t: 2 - (1 - k * t) / (1 - t) ** k
        q = f(F(1, 7)) * f(F(1, 13)) - 1
        require(0 <= q <= F(1, 3), "finite_q", str(k))
        rectangles = (list(itertools.product(seeds, repeat=k)) if k < 4 else
                      [(seeds[0], seeds[1], seeds[2], seeds[0]),
                       (seeds[2], seeds[2], seeds[0], seeds[1])])
        b_cache = {(xs, row): src.disjoint_sum(xs, row)
                   for xs in set(rectangles + [(x,) * k for x in scales])
                   for row in phase_rows}
        for index, measure in enumerate(measures):
            m_env = max(sum(w * norm_square(a_cache[(x, row)]) ** k
                            for row, w in measure) / x ** (2 * k) for x in scales)
            b_env = max(sum(w * norm_square(b_cache[((x,) * k, row)])
                            for row, w in measure) / x ** (2 * k) for x in scales)
            require((1 - q) ** 2 * m_env <= b_env <= (1 + q) ** 2 * m_env,
                    "finite_balanced_absorption", f"k={k},measure={index}")
            for xs in rectangles:
                c = sum(w * norm_square(b_cache[(xs, row)]) for row, w in measure)
                c /= math.prod(x * x for x in xs)
                require(c <= (1 + q) ** 2 * m_env,
                        "finite_rectangular_upper", f"{k},{index},{xs}")
                require(c <= 4 * b_env, "finite_balanced_to_rectangular", f"{k},{index},{xs}")
            panels.append({"k": k, "measure": index, "q": str(q),
                           "balanced": str(b_env), "moment": str(m_env)})
    # Independently check the finite-prime reinsertion, including zero phases.
    for x in scales:
        for row in phase_rows:
            def omitted(y):
                ans = src.ZERO
                for b in (0, 1):
                    term = src.scale(src.phase((0, b), row),
                                     (-1) ** b * src.profile(F(13 ** b) / y))
                    ans = src.add(ans, term)
                return ans
            reconstructed = src.add(omitted(x), src.scale(src.mul(row[0], omitted(x / 7)), -1))
            require(reconstructed == a_cache[(x, row)], "finite_prime_reinsertion", f"{x},{row}")
    return {"scale_count": len(scales), "envelope_panels": panels,
            "warning": "Exact sigma=1 finite free-ideal-monoid fixtures with rational weights, not genuine sextic-family moment data."}


def exponent_checks():
    def extract(k, h, lam):
        return F(1, 2) + (lam + F(5, 6) * h) / (2 * k)
    require(extract(2, F(1), F(21, 32)) == F(335, 384), "bootstrap_fraction")
    require(F(7, 8) - F(335, 384) == F(1, 384), "bootstrap_fraction")
    require(F(1, 2) + F(7, 8) * F(3, 8) == F(53, 64), "bootstrap_fraction")
    for beta in (F(7, 8), F(5, 6), F(3, 4), F(3, 5)):
        for k in range(2, 21):
            for r in (F(0), F(1, 2), F(7, 8)):
                lam = r * (k - 1) * (2 * beta - 1)
                expected = F(1, 2) + r * (1 - F(1, k)) * (beta - F(1, 2)) + F(5, 12 * k)
                require(extract(k, F(1), lam) == expected, "fractional_defect_identity")
            require(F(5, 6) - (2 * beta - 1) == F(11, 6) - 2 * beta,
                    "gain_threshold_identity")
    require(max(F(0), F(4 - 1, 3), F(2) - F(5, 6)) == F(7, 6),
            "generic_sieve_obstruction")


def reconstruct():
    src = load_source()
    mass_checks(src)
    orbits = cycle_checks(src)
    finite = finite_envelopes(src)
    exponent_checks()
    rejected = 0
    wrong = [(F(9, 4) == 1 / (1 + F(1, 3)) ** 2, "wrong absorption sign"),
             (necklace((1, 1, 1)) == 1, "lost triple multiplicity"),
             (src.power(src.ZERO, 6) == src.ONE, "lost row zero")]
    for predicate, reason in wrong:
        try:
            require(predicate, "deliberate_error", reason)
        except Failure:
            rejected += 1
        else:
            raise Failure("A deliberate algebraic error was not rejected")
    return {"schema": "balanced-closure-replay-v1",
            "parent_commit": "dabd6da99fb92eead7c99f941331ed9cbd2ec4ad",
            "source_dependency_sha256": DEPENDENCY_SHA,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "primitive_rotation_orbits": orbits, "finite_envelopes": finite,
            "predicate_counts": dict(sorted(COUNTS.items())),
            "successful_predicates": sum(COUNTS.values()) - rejected,
            "rejected_deliberate_errors": rejected,
            "scope": "Finite exact rational/cyclotomic algebra; analytic proofs require review; no arithmetic moment or zero-free theorem proved by computation."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--output", type=Path)
    group.add_argument("--check", type=Path)
    args = parser.parse_args()
    try:
        result = reconstruct()
        payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.check is not None and json.loads(args.check.read_text()) != result:
            raise Failure("Recorded result differs from exact reconstruction")
        if args.output is not None:
            args.output.write_text(payload)
        print(payload, end="")
        return 0
    except (Failure, OSError, ValueError) as error:
        print(f"FAIL: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
