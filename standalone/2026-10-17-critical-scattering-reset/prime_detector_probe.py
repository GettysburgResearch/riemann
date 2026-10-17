#!/usr/bin/env python3
"""Direct prime-side Gaussian detector. Binary64 exploration, not a certificate."""
import argparse
import json
import math


def prime_powers(nmax):
    prime = bytearray(b"\x01") * (nmax + 1)
    prime[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(nmax) + 1):
        if prime[p]:
            prime[p * p:nmax + 1:p] = b"\x00" * ((nmax - p * p) // p + 1)
    terms = []
    for p in range(2, nmax + 1):
        if prime[p]:
            q = p
            while q <= nmax:
                terms.append((math.log(q), math.log(p) / math.sqrt(q)))
                q *= p
    return terms


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cutoff", type=int, default=200000)
    parser.add_argument("--width", type=float, default=0.01)
    parser.add_argument("--horizon", type=float, default=9.0)
    parser.add_argument("--points", type=int, default=73)
    args = parser.parse_args()
    a, u, nmax = args.width, args.horizon, args.cutoff
    if not (a > 0 and u >= 0 and nmax >= 2 and args.points >= 2):
        raise ValueError("Require positive width, nonnegative horizon, cutoff>=2 and points>=2")
    terms = prime_powers(nmax)
    normalizer = 1 / math.sqrt(4 * math.pi * a)
    rows = []
    for j in range(args.points):
        x = u * j / (args.points - 1)
        prime_sum = math.fsum(weight * normalizer * math.exp(-(x - logn) ** 2 / (4 * a)) for logn, weight in terms)
        continuum = 0.5 * math.exp(x / 2 + a / 4) * math.erfc(-(x + a) / (2 * math.sqrt(a)))
        rows.append({"log_scale": x, "prime_sum": prime_sum, "continuum": continuum, "detector": prime_sum - continuum})
    r = math.log(nmax) - u
    tail = None
    if r > a and 1 / math.log(nmax) - 0.5 - r / (2 * a) < 0:
        log_tail = 0.5 * math.log(a / math.pi) + u / 2 + a / 4 + math.log1p((u + a) / (r - a)) - (r - a) ** 2 / (4 * a)
        tail = {"analytic_uniform_tail_formula_evaluated_in_binary64": math.exp(log_tail), "log_tail_bound": log_tail}
    result = {
        "arithmetic": "NON_DIRECTED_BINARY64; complete integer prime-power sieve through cutoff",
        "source": "F=Q, S empty; Gaussian prime sum minus exact continuous pole term",
        "cutoff": nmax, "prime_power_terms": len(terms), "width": a, "log_horizon": u,
        "tail": tail,
        "max_abs_sampled_detector": max(abs(row["detector"]) for row in rows),
        "data": rows,
        "limitation": "The analytic prime tail does not bound floating-point roundoff. A finite bounded graph supplies no all-scale bound and is not evidence of a full RH proof. No zero data are used."
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
