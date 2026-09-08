#!/usr/bin/env python3
"""Exact finite controls for GROWTH.md; no zeta numerics or RH decision.

Python >= 3.10, standard library only. All mathematical values use Fraction.
The output authenticates the local packet, not any external analytic input.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as Q
from math import comb
from pathlib import Path

G = tuple[Q, Q]

def g(x=0, y=0) -> G:
    return Q(x), Q(y)

def add(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]

def sub(a: G, b: G) -> G:
    return a[0] - b[0], a[1] - b[1]

def mul(a: G, b: G) -> G:
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]

def div(a: G, b: G) -> G:
    d = b[0]**2 + b[1]**2
    if not d:
        raise ZeroDivisionError("zero Gaussian-rational denominator")
    return (a[0]*b[0] + a[1]*b[1])/d, (a[1]*b[0] - a[0]*b[1])/d

def power(a: G, n: int) -> G:
    if n < 0:
        raise ValueError("nonnegative exponent required")
    out = g(1)
    for _ in range(n):
        out = mul(out, a)
    return out

def total(xs) -> G:
    out = g()
    for x in xs:
        out = add(out, x)
    return out

def real(a: G) -> Q:
    if a[1]:
        raise ValueError("nonreal result; conjugation or multiplicity failure")
    return a[0]

def validate_spectrum(a: list[G], v: Q) -> None:
    if not a or v <= 0 or any(z[0] <= 0 for z in a):
        raise ValueError("nonempty right-half-plane spectrum and v>0 required")
    if Counter(a) != Counter((x, -y) for x, y in a):
        raise ValueError("conjugation must preserve multiplicities")

def nodes(a: list[G], v: Q) -> list[G]:
    validate_spectrum(a, v)
    return [div(g(v), add(g(v), z)) for z in a]

def moments(k: list[G], n: int) -> list[Q]:
    return [real(total(power(z, j+1) for z in k)) for j in range(n+1)]

def row(m: list[Q], n: int) -> list[Q]:
    if n < 0 or len(m) <= n:
        raise ValueError("insufficient moments")
    return [comb(n, r)*sum(((-1)**j*comb(n-r, j)*m[r+j]
                             for j in range(n-r+1)), Q())
            for r in range(n+1)]

def spectral_row(k: list[G], n: int) -> list[Q]:
    return [comb(n, r)*real(total(mul(power(z, r+1),
                            power(sub(g(1), z), n-r)) for z in k))
            for r in range(n+1)]

def poly_product(a: list[G]) -> list[Q]:
    """Construct F(u)=product(1+u/a); no logarithmic moments used."""
    f = [g(1)]
    for z in a:
        t = [g()]*(len(f)+1)
        for j, c in enumerate(f):
            t[j] = add(t[j], c)
            t[j+1] = add(t[j+1], div(c, z))
        f = t
    return [real(c) for c in f]

def poly_eval(f: list[Q], u: G) -> G:
    out = g()
    for c in reversed(f):
        out = add(mul(out, u), g(c))
    return out

def h_eval(f: list[Q], u: G) -> G:
    return div(poly_eval([j*f[j] for j in range(1, len(f))], u),
               poly_eval(f, u))

def logarithmic_moments(f: list[Q], v: Q, n: int) -> list[Q]:
    """Formal division of d/dy F(v(1+y)) by F(v(1+y))."""
    den = real(poly_eval(f, g(v)))
    local = [sum((f[j]*v**j*comb(j, r) for j in range(r, len(f))), Q())/den
             for r in range(len(f))]
    jet = []
    for r in range(n+1):
        value = (r+1)*local[r+1] if r+1 < len(local) else Q()
        value -= sum((local[j]*jet[r-j] for j in range(1, min(r, len(local)-1)+1)), Q())
        jet.append(value)
    return [(-1)**r*jet[r] for r in range(n+1)]

def chebyshev_polys(n: int) -> list[list[int]]:
    """Coefficients of T_j(2t-1), low degree first."""
    if n < 0:
        raise ValueError("nonnegative degree required")
    out = [[1]]
    if n:
        out.append([-1, 2])
    for j in range(1, n):
        q = [0]*(j+2)
        for r, c in enumerate(out[j]):
            q[r] -= 2*c
            q[r+1] += 4*c
        for r, c in enumerate(out[j-1]):
            q[r] -= c
        out.append(q)
    return out

def spectral_chebyshev(k: list[G], n: int) -> list[Q]:
    out = [g()]*(n+1)
    for z in k:
        x = sub(mul(g(2), z), g(1))
        prev, cur = g(1), x
        out[0] = add(out[0], z)
        if n:
            out[1] = add(out[1], mul(z, cur))
        for j in range(1, n):
            prev, cur = cur, sub(mul(mul(g(2), x), cur), prev)
            out[j+1] = add(out[j+1], mul(z, cur))
    return [real(c) for c in out]

class Checks:
    def __init__(self):
        self.count = 0
    def require(self, name: str, condition: bool) -> None:
        self.count += 1
        if not condition:
            raise RuntimeError("FAILED: " + name)
    def rejects(self, name: str, fn) -> None:
        try:
            fn()
        except (ValueError, ZeroDivisionError):
            self.require(name, True)
            return
        self.require(name, False)

def run() -> dict:
    ck = Checks()
    degree = 32
    polys = chebyshev_polys(degree)
    fixtures = {
        "positive_real": [g(1), g(2), g(5)],
        "pr790_counterfeit": [g(1), g(2, 1), g(2, -1)],
        "repeated_pair": [g(1), g(2, 1), g(2, -1), g(2, 1), g(2, -1)],
        "second_pair": [g(1), g(3, 2), g(3, -2)],
    }
    cf_data = None
    for name, a in fixtures.items():
        f = poly_product(a)
        for v in (Q(1), Q(2), Q(5)):
            k = nodes(a, v)
            m = moments(k, degree)
            ck.require("formal-log vs zero powers", m == logarithmic_moments(f, v, degree))
            traces = [sum((Q(c)*m[j] for j, c in enumerate(p)), Q()) for p in polys]
            ck.require("Chebyshev two implementations", traces == spectral_chebyshev(k, degree))
            prev = None
            first_negative = None
            first_trace_violation = None
            for n in range(degree+1):
                b = row(m, n)
                ck.require("binomial vs spectral row", b == spectral_row(k, n))
                ck.require("row mass", sum(b) == m[0])
                if prev is not None:
                    coarse = [(Q(n-r, n)*b[r] + Q(r+1, n)*b[r+1]) for r in range(n)]
                    ck.require("degree elevation", coarse == prev)
                    ck.require("variation monotonicity", sum(map(abs, b)) >= sum(map(abs, prev)))
                if first_negative is None and min(b) < 0:
                    first_negative = n
                if first_trace_violation is None and abs(traces[n]) > m[0]:
                    first_trace_violation = n
                if name == "positive_real":
                    ck.require("positive control", min(b) > 0 and abs(traces[n]) <= m[0])
                prev = b
            for w in (g(Q(1, 20)), g(Q(1, 25), Q(1, 30))):
                # Source-side rational function uses polynomial coefficients, not zero sums.
                u = mul(g(v), power(div(sub(g(1), w), add(g(1), w)), 2))
                rhs = add(g(m[0]/2), mul(div(mul(g(v), sub(g(1), w)),
                          mul(g(2), add(g(1), w))), h_eval(f, u)))
                lhs = total(div(mul(z, sub(g(1), mul(sub(mul(g(2), z), g(1)), w))),
                          add(sub(g(1), mul(mul(g(2), sub(mul(g(2), z), g(1))), w)), power(w, 2)))
                          for z in k)
                ck.require("Chebyshev generating identity", lhs == rhs)
                for z in (g(-1), g(0, 1), g(Q(3, 5), Q(4, 5))):
                    u = div(mul(g(v), sub(g(1), mul(w, z))), sub(g(1), w))
                    rhs = mul(div(g(v), sub(g(1), w)), h_eval(f, u))
                    lhs = total(div(t, sub(g(1), mul(w, add(sub(g(1), t), mul(t, z))))) for t in k)
                    ck.require("Bernstein generating identity", lhs == rhs)
            if name == "pr790_counterfeit" and v == 1:
                witness = row(m, 14)[0]
                ck.require("parent exact witness", witness == Q(-433316717939, 10**15))
                ck.require("finite ordinary positivity", min(m) > 0)
                cf_data = {
                    "H_0_14": str(witness),
                    "first_negative_row_in_0_to_32": first_negative,
                    "first_Chebyshev_bound_violation_in_0_to_32": first_trace_violation,
                    "trace_at_first_violation": str(traces[first_trace_violation]),
                    "mass": str(m[0]),
                }
    # Sharp l-infinity primitive-error amplification, not approximate condition numbers.
    t_prev, t_cur = 1, 3
    for n, p in enumerate(polys):
        if n == 0:
            t = 1
        elif n == 1:
            t = 3
        else:
            t_prev, t_cur = t_cur, 6*t_cur-t_prev
            t = t_cur
        alt = [Q((-1)**j) for j in range(n+1)]
        ck.require("sharp Bernstein error", sum(map(abs, row(alt, n))) == 3**n)
        ck.require("sharp Chebyshev error", sum(map(abs, p)) == t)
        ck.require("Chebyshev error attained", abs(sum(p[j]*alt[j] for j in range(n+1))) == t)
    # Rational square-root coordinates avoid uncertified radical evaluation.
    for p in (Q(2), Q(4)):
        for q in (Q(0), Q(1, 4), Q(1, 2)):
            A, B, R = p*p-q*q, 2*p*q, p*p+q*q
            for rootv in (Q(1), Q(2), Q(4)):
                v = rootv**2
                eta = 2*rootv*abs(q)/(v+R)
                M2 = (v+R)**2/((v+A)**2+B*B)
                RC2 = (1+eta)/(1-eta)
                ck.require("rate comparison", M2 == (RC2+1)**2/(4*RC2))
                ck.require("optimal scale algebra", (v+R)**2-4*v*R == (v-R)**2)
    ck.rejects("missing conjugate", lambda: nodes([g(2, 1)], Q(1)))
    ck.rejects("multiplicity mismatch", lambda: nodes([g(2, 1), g(2, 1), g(2, -1)], Q(1)))
    ck.rejects("left-half-plane pole", lambda: nodes([g(-1)], Q(1)))
    ck.rejects("zero scale", lambda: nodes([g(1)], Q(0)))
    ck.rejects("short moment packet", lambda: row([Q(1)], 2))
    ck.rejects("empty spectrum", lambda: nodes([], Q(1)))
    folder = Path(__file__).resolve().parent
    hashes = {name: hashlib.sha256((folder/name).read_bytes()).hexdigest()
              for name in ("README.md", "GROWTH.md", "verify_exact.py")}
    return {
        "status": "PASS", "arithmetic": "EXACT_RATIONAL",
        "scope": "finite algebra and synthetic controls only; no RH proof",
        "checks": ck.count, "maximum_degree": degree,
        "fixtures": list(fixtures), "scales": [1, 2, 5],
        "counterfeit": cf_data,
        "not_run": ["actual-zeta moment evaluation", "external zero verification replay",
                    "predecessor scripts", "Lean", "independent mathematical review"],
        "source_sha256": hashes,
    }

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, help="write computed JSON")
    ap.add_argument("--check", type=Path, help="compare with a saved result; never trust its status")
    args = ap.parse_args()
    actual = run()
    if args.check is not None:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if actual != expected:
            raise SystemExit("REFUSED: saved result does not match recomputation")
    encoded = json.dumps(actual, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")

if __name__ == "__main__":
    main()
