#!/usr/bin/env python3
"""Bounded exact controls for NJT26. Not a native high-order fit or RH proof.

Only integer/Fraction arithmetic enters the reconstructed record. The analytic
proofs and explicitly imported native zero/source theorems are not certified
by this executable. --emit produces a record; --check authenticates and compares.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations
import json
from math import factorial, comb
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def canonical(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def no_duplicate(pairs: list[tuple[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key: " + key)
        out[key] = value
    return out


def reject_float(text: str) -> None:
    raise ValueError("non-integer JSON numeric literal is outside this receipt contract: " + text)


def read_json(path: Path) -> object:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 2_000_000:
        raise ValueError("invalid receipt file")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=no_duplicate,
                      parse_float=reject_float, parse_constant=reject_float)


def authenticate() -> None:
    manifest = read_json(ROOT / "HASHES.json")
    if not isinstance(manifest, dict) or set(manifest) != {"algorithm", "files"}:
        raise ValueError("invalid manifest schema")
    if manifest["algorithm"] != "sha256" or not isinstance(manifest["files"], dict):
        raise ValueError("invalid manifest algorithm/files")
    files = manifest["files"]
    actual = {p.name for p in ROOT.iterdir() if p.name != "HASHES.json"}
    if set(files) != actual:
        raise ValueError("packet inventory differs from manifest")
    for name, digest in files.items():
        if not isinstance(name, str) or Path(name).name != name or not isinstance(digest, str):
            raise ValueError("invalid manifest entry")
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            raise ValueError("non-regular packet member")
        if sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError("source/receipt hash mismatch: " + name)


def polynomial(factors: tuple[Q, ...]) -> list[Q]:
    out = [Q(1)]
    for lam in factors:
        require(lam >= 0, "negative product factor")
        out.append(Q(0))
        for k in range(len(out) - 1, 0, -1):
            out[k] += lam * out[k - 1]
    return out


def subset_coefficients(factors: tuple[Q, ...]) -> list[Q]:
    out = []
    for k in range(len(factors) + 1):
        total = Q(0)
        for group in combinations(factors, k):
            term = Q(1)
            for lam in group:
                term *= lam
            total += term
        out.append(total)
    return out


def newton_controls() -> dict[str, object]:
    families = [tuple(Q(1, n * n) for n in range(1, d + 1)) for d in range(1, 13)]
    families += [tuple(Q((n % 4) + 1, 3 * n + 2) for n in range(1, d + 1)) for d in range(2, 11)]
    # These are FINITE Gaussian approximants, not an infinite numerical limit.
    families += [tuple([Q(1, 3 * d)] * d + [Q(1, 7), Q(1, 11)]) for d in (1, 2, 4, 8, 16)]
    inequalities = tails = maclaurin = subsets = 0
    for factors in families:
        a = polynomial(factors)
        if len(factors) <= 9:
            require(a == subset_coefficients(factors), "product/subset coefficient discrepancy")
            subsets += 1
        b = [factorial(k) * value for k, value in enumerate(a)]
        for k in range(1, len(a) - 1):
            require(b[k] ** 2 >= b[k - 1] * b[k + 1], "Newton log-concavity failure")
            inequalities += 1
        s = Q(1) / (1 + sum(factors, Q(0)))
        for m in range(1, len(a)):
            tau = Q(m) * a[m] / a[m - 1]
            require(tau ** m <= b[m], "terminal ratio versus Maclaurin mean")
            for k in range(m, len(a)):
                require(b[k] ** m <= b[m] ** k, "Maclaurin root comparison")
                require(a[k] <= a[m] * tau ** (k - m) * Q(factorial(m), factorial(k)),
                        "complete terminal-ratio coefficient majorant")
                maclaurin += 1
            rho = tau * s / (m + 1)
            require(0 <= rho < 1, "finite tail test outside geometric domain")
            exact_tail = sum((a[k] * s ** k for k in range(m + 1, len(a))), Q(0))
            require(exact_tail <= a[m] * s ** m * rho / (1 - rho), "terminal-ratio tail bound")
            tails += 1
    # Degenerate zero tail and empty product are explicitly included.
    require(polynomial(()) == [Q(1)], "empty product")
    require(polynomial((Q(0), Q(1, 2))) == [Q(1), Q(1, 2), Q(0)], "zero terminal coefficient")
    return {"finite_product_families": len(families), "subset_reconstructions": subsets,
            "newton_inequalities": inequalities, "terminal_tail_panels": tails,
            "maclaurin_and_ratio_coefficient_panels": maclaurin,
            "infinite_gaussian_or_product_limit_numerically_verified": False}


def factor_controls() -> dict[str, object]:
    identities = near = far = 0
    # Complex numbers are represented by exact pairs, never binary floats.
    for R in (Q(1), Q(2), Q(4)):
        b = R / 4
        for x in (Q(0), R / 4, R / 2):
            for y in (b, R / 2):
                mod2 = x * x + y * y
                require(mod2 <= R * R, "factor test outside disk")
                for r in (R / 3, R, 2 * R, 3 * R, 5 * R):
                    left = (1 - (x * x - y * y) / (r * r)) ** 2 + (2 * x * y / (r * r)) ** 2
                    right = ((r * r - mod2) ** 2 + 4 * r * r * y * y) / r ** 4
                    require(left == right, "complex factor identity")
                    identities += 1
                    if r <= 2 * R:
                        require(left >= (b / R) ** 2, "near-factor modulus lower bound")
                        near += 1
                    else:
                        require(left >= (1 - R * R / (r * r)) ** 2, "far-factor triangle lower bound")
                        u = 4 * R * R / (r * r)
                        require(0 < u < 1, "far-factor parameter domain")
                        # Rational exponent comparison equivalent to the stated log inequality.
                        require((1 - u / 4) ** 3 * (1 + u) ** 2 >= 1, "far-factor log-cost control")
                        far += 1
    scalar = 0
    for denominator in (8, 17, 64):
        for numerator in range(denominator + 1):
            u = Q(numerator, denominator)
            require((1 - u / 4) ** 3 * (1 + u) ** 2 >= 1, "far scalar panel")
            scalar += 1
    return {"complex_factor_identities": identities, "near_factor_panels": near,
            "far_factor_panels": far, "additional_rational_scalar_panels": scalar,
            "actual_model_zero_census_performed": False}


def mobius(n: int) -> int:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    sign = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def arithmetic_instance(Y: int, u: Q, perturb: bool) -> tuple[int, int]:
    b = Y + 1
    B = b * b - 1
    mu = [0] + [mobius(k) for k in range(1, B + 2)]
    m = [Q(0)]
    for k in range(1, B + 2):
        m.append(m[-1] + Q(mu[k], k))
    c = {k: Q(mu[k]) for k in range(1, Y + 1)}
    c[b] = u * mu[b] + (u - 1) * b * m[Y]
    for k in range(b + 1, B + 1):
        c[k] = u * mu[k]
    c[B + 1] = -u * (B + 1) * m[B]
    if perturb:
        # A distinct zero-reciprocal perturbation; not an optimal family member.
        p, q = b, b + 1
        c[p] = c.get(p, Q(0)) + Q(2, 7)
        c[q] = c.get(q, Q(0)) - Q(2 * q, 7 * p)
    c = {k: value for k, value in c.items() if value}
    require(sum((value / k for k, value in c.items()), Q(0)) == 0, "reciprocal balancing")
    require(all(c.get(k, Q(0)) == mu[k] for k in range(1, Y + 1)), "native prefix changed")

    t = [Q(0)]
    for k in range(1, B + 2):
        t.append(t[-1] + c.get(k, Q(0)) / k)
    require(t[-1] == 0, "reciprocal future not zero")
    FY = sum((m[k] ** 2 for k in range(1, Y + 1)), Q(0))
    A = sum((m[k] ** 2 for k in range(b, B + 1)), Q(0))
    # Full physical energy includes the constant cumulative future after B+1.
    cumulative = Q(0)
    full_energy = Q(0)
    for k in range(1, B + 2):
        cumulative += c.get(k, Q(0))
        full_energy += cumulative * cumulative / (k * (k + 1))
    full_energy += cumulative * cumulative / (B + 2)
    reciprocal_energy = sum((value * value for value in t), Q(0))
    require(full_energy == reciprocal_energy, "full physical/reciprocal energy mismatch")
    delta = full_energy - FY
    require(delta >= 0, "negative completion cost")

    # Separate coefficient-level convolution, then cumulative divisor fibers.
    cc = [Q(0)] * (B + 1)
    for i, ci in c.items():
        if i > B:
            continue
        for j, cj in c.items():
            if i * j <= B:
                cc[i * j] += ci * cj
    one_cc = [Q(0)] * (B + 1)
    for d in range(1, B + 1):
        if cc[d]:
            for n in range(d, B + 1, d):
                one_cc[n] += cc[d]
    qprefix = Q(0)
    S = Q(0)
    for n in range(1, B + 1):
        require(2 * c.get(n, Q(0)) - one_cc[n] == mu[n], "Newton output coefficient")
        qprefix += one_cc[n] / n
        if n >= b:
            require(qprefix == 2 * t[n] - m[n], "quadratic reciprocal identity")
            S += qprefix * qprefix

    excess = abs(S - A) - 4 * delta
    require(excess <= 0 or excess * excess <= 16 * A * delta, "completion-energy price")
    if not perturb:
        require(delta == u * u * A and S == (1 - 2 * u) ** 2 * A, "sharp completion tradeoff")
        require(all(t[k] == u * m[k] for k in range(b, B + 1)), "oracle reciprocal source")
        if u == Q(1, 2):
            require(S == 0 and delta == A / 4, "exact annihilation price")
    return B, len(c)


def arithmetic_controls() -> dict[str, object]:
    cases = perturbed = coefficients = 0
    # The oracle family deliberately uses the full native prefix through B.
    for Y in (1, 2, 3, 5, 7, 11, 17):
        for u in (Q(-1, 4), Q(0), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4)):
            B, _ = arithmetic_instance(Y, u, False)
            coefficients += B
            cases += 1
        for u in (Q(0), Q(1, 4), Q(1, 2)):
            B, _ = arithmetic_instance(Y, u, True)
            coefficients += B
            perturbed += 1
    return {"sharp_native_completion_panels": cases, "perturbed_completion_panels": perturbed,
            "coefficient_level_newton_checks": coefficients,
            "max_native_prefix_used": 324,
            "future_mobius_coefficients_used_for_sharpness_examples": True,
            "short_prefix_arithmetic_upper_bound_proved": False}


def budget_controls() -> dict[str, object]:
    require(Q(2, 3) + Q(2, 81) + Q(2, 1215) > Q(69, 100), "log2 positive-series lower guard")
    exp22lower = sum((Q(11, 5) ** k / factorial(k) for k in range(13)), Q(0))
    require(exp22lower > Q(792, 91), "complete support allowance lower Taylor sum")
    exp08lower = sum((Q(4, 5) ** k / factorial(k) for k in range(4)), Q(0))
    require(exp08lower > Q(11, 5), "F5 growth guard")
    require(160 ** 3 < 2 ** 22, "F5 logarithmic ratio guard")
    require(4 * 256 * Q(69, 100) - (Q(708, 5) + 8 * Q(141, 2)) == Q(24, 25),
            "F5 strict exclusion margin")
    require(256 * Q(69, 100) > 141, "F5 terminal moment eligibility")
    require(Q(204800, 512 * 512) == Q(25, 32) < 1, "uniform small-zero guard")
    require(Q(29 * 2 ** 36 + 31, 4) + 7 < 2 ** 39, "complete zero budget constant")
    require(26 + Q(8, 3) * Q(3, 2) + Q(8, 9) < 31, "inverse-fourth zero count integral")
    rows = []
    for j in range(2, 41):
        R = 2 ** j
        B = 20 + 2 * R * (j + 3)
        m = (j + 1) * (10 + R * (j + 3))
        require(2 * m == (j + 1) * B, "integer half-budget identity")
        require(m >= B, "terminal moment eligibility")
        require(Q(4 * m) - Q(6 * j + 5, 3) * B == Q(B, 3), "strict cofinal zero-exclusion margin")
        require(204800 < 2 ** 18 and 4 * R + 2 <= 8 * R, "source growth exponent guard")
        old = (2 * j + 4) * R * R
        rows.append({"j": j, "radius": R, "B": B, "even_moment_coordinates": m,
                     "raw_moment_degree": 2 * m, "error_negative_log2": 4 * m,
                     "old_even_moment_coordinates": old,
                     "ratio_old_to_new": str(Q(old, m)),
                     "strict_integer_margin": str(Q(B, 3))})
    return {"displayed_schedule_rows": rows, "schedule_case_count": len(rows),
            "fixed_F5_forbidden_even_coordinate": 256, "fixed_F5_forbidden_raw_degree": 512,
            "fixed_F5_error_negative_log2": 1024, "fixed_F5_margin": "24/25",
            "fixed_F5_native_zero_certificate_replayed": False,
            "uniform_small_zero_radius": "1/512", "unconditional_defect_R_squared_constant": 2 ** 39,
            "native_high_order_fit_performed": False}


def synthetic_witness() -> dict[str, object]:
    # A compact exact polynomial of huge degree, NOT expanded or enumerated.
    n = 2 ** 100
    m = 16
    source = [Q(1, 2 ** k * factorial(k)) for k in range(m + 1)]
    model = [Q(1)]
    for k in range(1, m + 1):
        model.append(model[-1] * Q(n - k + 1, 2 * n * k))
    separate = [Q(comb(n, k), (2 * n) ** k) for k in range(m + 1)]
    require(model == separate, "compact multiplicity coefficient identity")
    E = sum((abs(a - b) for a, b in zip(source, model)), Q(0))
    require(E < Q(1, 2 ** 64), "synthetic Gaussian fit tolerance")
    require(3 ** 8 + 1 < 2 ** 13 and m >= 13, "synthetic whole-source MGF allowance")
    require(Q(4 * m) > 14 * (Q(5, 3) + 1), "synthetic full-tail zero-exclusion budget")
    return {"source": "standard Gaussian; F(z)=exp(-z^2/2)",
            "rational_factor_lambda": str(Q(1, 2 * n)), "factor_multiplicity": n,
            "polynomial_raw_degree": 2 * n,
            "coefficient_coordinates_verified": m + 1,
            "weighted_error_exact": str(E), "error_upper_negative_log2": 64,
            "radius": "1", "excluded_off_axis_distance": "1/2",
            "native_source": False, "polynomial_fully_expanded": False,
            "model_is_probability_characteristic_function": False}


def reconstruct() -> dict[str, object]:
    payload = {"packet": "NJT26", "version": 1,
               "parent_head": "17ad26fd0b3de0c88b56d356ab850b881227b2f5",
               "rh_proved": False, "unbounded_native_feasibility_proved": False,
               "new_native_moment_match_proved": False,
               "native_covariance_upper_bound_proved": False,
               "newton": newton_controls(), "factors": factor_controls(),
               "arithmetic": arithmetic_controls(), "budgets": budget_controls(),
               "synthetic_witness": synthetic_witness()}
    payload["semantic_sha256"] = sha256(canonical(payload).encode("ascii")).hexdigest()
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--emit", type=Path)
    action.add_argument("--check", type=Path)
    args = parser.parse_args()
    if args.check:
        authenticate()
        actual = read_json(args.check)
        expected = reconstruct()
        # Canonical JSON comparisons distinguish bool from int and preserve type scope.
        if canonical(actual) != canonical(expected):
            raise ValueError("reconstructed receipt differs from supplied typed record")
        print("PASS", expected["semantic_sha256"])
    else:
        expected = reconstruct()
        args.emit.write_text(json.dumps(expected, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print("EMITTED (not an accepting replay)", expected["semantic_sha256"])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, ArithmeticError, OSError, TypeError) as exc:
        print("REFUSED:", str(exc), file=sys.stderr)
        raise SystemExit(1)
