#!/usr/bin/env python3
"""Separate EPC26 reconstruction: no producer or repository imports.

Uses trial factorization, the ordered max-kernel work identity, Cartesian
prime-exponent products and divisor evaluation of every fully expanded repair.
Acceptance compares canonical typed JSON, not Python numeric-alias equality.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import itertools
import json
import tempfile
from fractions import Fraction as Q
from math import isqrt, prod
from pathlib import Path


def require(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def typed(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def digest(obj: object) -> str:
    return hashlib.sha256(typed(obj)).hexdigest()


def encode(x: Q) -> list[int]:
    return [x.numerator, x.denominator]


def factors(n: int) -> list[tuple[int, int]]:
    p, out = 2, []
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def mobius(n: int) -> int:
    fs = factors(n)
    return 0 if any(e != 1 for _, e in fs) else (-1)**len(fs)


def prune(a: dict[int, Q]) -> dict[int, Q]:
    return {k: Q(v) for k, v in a.items() if v}


def linear(a: dict[int, Q], b: dict[int, Q], c: int = 1) -> dict[int, Q]:
    return prune({n: a.get(n, Q())+c*b.get(n, Q()) for n in a.keys() | b.keys()})


def table(a: dict[int, Q]) -> list[list[int]]:
    return [[n, v.numerator, v.denominator] for n, v in sorted(a.items())]


def energy(a: dict[int, Q]) -> Q:
    previous = value = Q()
    for n, coefficient in sorted(a.items()):
        value += coefficient*(2*previous+coefficient)/n
        previous += coefficient
    return value


def bilinear(a: dict[int, Q], b: dict[int, Q]) -> Q:
    return sum((a[n]*b[m]/max(n, m) for n in a for m in b), Q())


def one(a: dict[int, Q]) -> Q:
    return sum((value/n for n, value in a.items()), Q())


def completions(Y: int) -> tuple[dict, dict, Q, Q, Q]:
    running, E, c = 0, Q(), Q()
    prefix = {}
    for n in range(1, Y+1):
        bit = mobius(n)
        prefix[n] = Q(bit)
        running += bit
        weight = Q(1, n)-Q(1, n+1)
        E += running*running*weight
        c += running*weight
    free = prune({**prefix, Y+1: Q(-running)})
    tail = -(Y+1)*c
    jet = prune({**prefix, Y+1: tail-running})
    F = E+(Y+1)*c*c
    require(energy(free) == E and energy(jet) == F and one(jet) == 0, "completion optimizer")
    require(energy(prune(prefix)) == E+Q(running*running, Y+1), "stopped energy")
    return free, jet, E, F, c


def signed_products(primepowers: list[int]) -> dict[int, Q]:
    return {prod(p for p, chosen in zip(primepowers, bits) if chosen): Q((-1)**sum(bits))
            for bits in itertools.product((0, 1), repeat=len(primepowers))}


def shifted_output(C: dict, primepowers: list[int]) -> dict:
    result = {}
    for divisor, coefficient in signed_products(primepowers).items():
        for n, a in C.items():
            result[n*divisor] = result.get(n*divisor, Q())+a*coefficient
    return prune(result)


def entire_B(C: dict, fs: list[list[int]]) -> dict:
    powers = [[p**j for j in range(m)] for p, m, _ in fs]
    smooth = {prod(row) for row in itertools.product(*powers)}
    candidates = {n*d for n in C for d in smooth}
    # Recover coefficients by a divisor test, not the producer's convolution.
    result = {x: sum((value for n, value in C.items() if x % n == 0 and x//n in smooth), Q())
              for x in candidates}
    return prune(result)


def reconstruct() -> dict:
    native, panels = [], []
    for Y in range(1, 257):
        core, jet, E, F, c = completions(Y)
        if Y <= 16:
            source = prune({n: Q(mobius(n)) for n in range(1, Y+1)})
            require(energy(source) == bilinear(source, source), "native full max-kernel")
        row = [Y, sum(mobius(n) for n in range(1, Y+1)), encode(E), encode(F), encode(c)]
        native.append(row)
        if Y in (1, 2, 3, 5, 7, 11, 32, 128, 256):
            panels.append(row)
    projections = []
    for Y in (1, 2, 3, 5, 8, 16, 32):
        core, jet, E, F, _ = completions(Y)
        for t in (-3, 1, 5):
            d = Y+3
            r = prune({d: Q(t), 2*d: Q(1-t), 3*d+1: Q(-2)})
            rz = {d: Q(t*d), 2*d: Q(-2*t*d)}
            require(one(rz) == 0, "perturbation preserves value at 1")
            require(energy(linear(core, r)) == E+energy(r), "free residual identity")
            require(energy(linear(jet, rz)) == F+energy(rz), "jet residual identity")
            require(bilinear(core, r) == bilinear(jet, rz) == 0, "projection orthogonality")
            projections.append([Y, t, encode(energy(r)), encode(energy(rz))])
    finite, expansions = [], []
    for Y in (2, 3, 5, 7, 11, 13, 17, 19):
        ps = [n for n in range(2, Y+1) if factors(n) == [(n, 1)]]
        core, jet, E, F, _ = completions(Y)
        for scale in (1, 4, 64):
            H, fs, upper = scale*Y*Y, [], Q(1)
            for p in ps:
                m = next(j for j in range(1, H.bit_length()+1) if p**j > H)
                q = p**m
                require(m >= 3 and p**(m-1) <= H < q, "strict minimal exponent")
                fs.append([p, m, q])
                root = isqrt(q)
                require(root*root <= q < (root+1)**2, "integer-root directed bound")
                upper *= Q(root+1, root)
            eta_hi = upper-1
            for label, C, optimum in (("free", core, E), ("zero_at_one", jet, F)):
                out = shifted_output(C, [q for _, _, q in fs])
                error = linear(out, C, -1)
                measured = energy(out)
                require(measured == optimum+energy(error), "whole-energy decomposition")
                require(optimum <= measured <= optimum*(1+eta_hi*eta_hi), "relative estimate")
                require(all(out.get(n, 0) == mobius(n) for n in range(1, Y+1)), "fixed prefix")
                if label == "zero_at_one":
                    require(one(out) == 0, "safe-point constraint")
                if Y <= 5:
                    require(bilinear(C, error) == 0 and bilinear(out, out) == measured, "complete pair expansion")
                full_B = Y <= 7 and scale == 1
                terms = maximum = None
                if full_B:
                    B = entire_B(C, fs)
                    cap = Q(2*Y) if label == "free" else Y+(Y+1)*sum((Q(1,n) for n in range(1,Y+1)),Q())
                    require(all(abs(v) <= cap for v in B.values()), "all repair coefficient bounds")
                    divisors = signed_products(ps)
                    support = {d*n for d in divisors for n in B}
                    formed = prune({x: sum((c*B.get(x//d, Q()) for d, c in divisors.items() if x % d == 0), Q())
                                    for x in support})
                    require(formed == out, "all expanded Euler-repair coefficients")
                    require(all(B.get(n, 0) == int(n == 1) for n in range(1, Y+1)), "late repair restriction")
                    terms, maximum = len(B), max(B)
                    expansions.append([Y, label, digest(table(B)), terms, maximum])
                finite.append({"Y": Y, "H": H, "kind": label, "factors": fs,
                               "optimum": encode(optimum), "energy": encode(measured),
                               "relative_excess": encode(measured/optimum-1), "eta_upper": encode(eta_hi),
                               "output_terms": len(out), "output_max_index": max(out),
                               "output_sha256": digest(table(out)), "full_B_expanded": full_B,
                               "B_terms": terms, "B_max_index": maximum})
    require(energy({1: Q(1)}) == 1, "constant future is included")
    q3 = completions(3)
    require(q3[2] == Q(7, 12) and q3[3] == Q(23, 18) and one(q3[0]) == Q(5, 12), "named optimizer values")
    q5 = completions(5)[0]
    wrong = shifted_output(q5, [4])
    require(wrong.get(4, 0) != mobius(4), "early correction changes source")
    return {"schema": "EPC26/v1", "status": "PROPOSED_NOT_RH_PROOF",
            "scope": {"complete_finite_output_energy": True, "all_Y_by_finite_test": False,
                      "full_repository_validation": False, "independent_mathematical_review": False},
            "native": {"prefix_count": 256, "rows_sha256": digest(native), "panels": panels},
            "projection": {"cases": len(projections), "rows_sha256": digest(projections)},
            "repairs": finite, "expanded_B": expansions,
            "controls": {"one_atom_full_energy": [1, 1], "Y3_free_optimum": [7, 12],
                         "Y3_safe_zero_optimum": [23, 18], "Y3_core_value_at_one": [5, 12],
                         "early_factor_rejected": True}}



def compact(full: dict) -> dict:
    result = {k: v for k, v in full.items() if k != "repairs"}
    result["repairs"] = {"case_count": len(full["repairs"]), "rows_sha256": digest(full["repairs"]),
                         "panels": [r for r in full["repairs"] if r["Y"] in (7,19) and r["H"] == 64*r["Y"]**2]}
    result["full_reconstruction_sha256"] = digest(full)
    return result


def validate(path: Path, expected: dict) -> None:
    obj = json.loads(path.read_text())
    require(type(obj) is dict and set(obj) == {"body", "sha256"}, "outer fields")
    require(obj["sha256"] == digest(obj["body"]), "report checksum")
    require(typed(obj["body"]) == typed(expected), "typed primitive reconstruction mismatch")


def rejection_tests(expected: dict) -> int:
    bad_bodies = []
    for i in range(12):
        b = copy.deepcopy(expected)
        if i == 0:
            b["status"] = "RH_PROVED"
        elif i == 1:
            b["scope"]["all_Y_by_finite_test"] = True
        elif i == 2:
            b["native"]["prefix_count"] = 256.0
        elif i == 3:
            b["scope"]["complete_finite_output_energy"] = 1
        elif i == 4:
            b["repairs"]["case_count"] -= 1
        elif i == 5:
            b["repairs"]["panels"][0]["factors"][0][2] //= 2
        elif i == 6:
            b["repairs"]["panels"][0]["energy"][0] += 1
        elif i == 7:
            b["repairs"]["panels"][1]["optimum"] = b["repairs"]["panels"][0]["optimum"]
        elif i == 8:
            b["repairs"]["panels"][0]["output_terms"] -= 1
        elif i == 9:
            b["controls"]["one_atom_full_energy"] = [0, 1]
        elif i == 10:
            b["expanded_B"][0][2] = "0"*64
        else:
            b["projection"]["cases"] -= 1
        require(typed(b) != typed(expected), "mutation must actually change data")
        bad_bodies.append(b)
    with tempfile.TemporaryDirectory(prefix="epc26-rejections-") as tmp:
        good = Path(tmp)/"good.json"
        good.write_bytes(typed({"body": expected, "sha256": digest(expected)}))
        validate(good, expected)
        for i, b in enumerate(bad_bodies):
            p = Path(tmp)/f"bad-{i}.json"
            p.write_bytes(typed({"body": b, "sha256": digest(b)}))
            try:
                validate(p, expected)
            except ValueError as e:
                require("typed primitive" in str(e), "must not rely on stale checksum")
            else:
                raise ValueError("resealed corruption accepted")
    return len(bad_bodies)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("report", type=Path)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--output", type=Path, help="optional separately reconstructed artifact")
    ap.add_argument("--full-output", type=Path, help="all 48 reconstructed case records")
    args = ap.parse_args()
    full = reconstruct()
    expected = compact(full)
    if args.full_output:
        args.full_output.write_bytes(typed(full)+b"\n")
    validate(args.report, expected)
    if args.output:
        args.output.write_bytes(typed({"body": expected, "sha256": digest(expected)})+b"\n")
    print("SEPARATE RECONSTRUCTION PASS", digest(expected))
    if args.self_test:
        print("RESEALED CORRUPTIONS REJECTED", rejection_tests(expected))


if __name__ == "__main__":
    main()
