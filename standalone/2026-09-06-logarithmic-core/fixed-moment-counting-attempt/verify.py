#!/usr/bin/env python3
"""Bounded exact algebra checks, NOT an RH/count/PNT/zero-spectrum proof.
Standard library only. No assert statement is used in acceptance.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
A = F(45, 128)


def require(ok: bool, text: str) -> None:
    if not ok:
        raise ValueError(text)


def w(u: F) -> F:
    if u <= F(1, 4) or u >= 4:
        return F(0)
    return u / 3 - 1 / (192 * u**2) if u <= 1 else 1 / (3 * u**2) - u / 192


def add(*ps):
    out = defaultdict(F)
    for p in ps:
        for key, value in p.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def scale(p, c):
    return {key: c * value for key, value in p.items() if c * value}


def mul(p, q):
    out = defaultdict(F)
    for key, value in p.items():
        for key2, value2 in q.items():
            out[tuple(sorted(key + key2))] += value * value2
    return {key: value for key, value in out.items() if value}


def prime_power(n: int) -> int | None:
    if n < 2:
        return None
    p = 2
    while p * p <= n and n % p:
        p += 1
    if p * p > n:
        return n
    while n % p == 0:
        n //= p
    return p if n == 1 else None


def lam(n: int):
    p = prime_power(n)
    return {} if p is None else {(p,): F(1)}


def exact_correlations(M: int):
    rows, ds, direct, centered = [], [], {}, {}
    for j in range(2, M + 1):
        row = {n: w(F(n, j*j)) / j for n in range(1, 4*j*j+1)}
        row = {n: val for n, val in row.items() if val}
        delta = A*j - sum(row.values(), F(0))
        p = {}
        t = {}
        for n, val in row.items():
            p = add(p, scale(lam(n), val))
            t = add(t, scale(add(lam(n), {(): F(-1)}), val))
        r = add({(): A*j}, scale(p, -1))
        require(r == add({(): delta}, scale(t, -1)), "centering identity")
        direct = add(direct, mul(r, r))
        centered = add(centered, mul(t, t))
        rows.append(row)
        ds.append(delta)
    H, b = defaultdict(F), defaultdict(F)
    for row, delta in zip(rows, ds):
        for n, val in row.items():
            b[n] += delta*val
            for l, val2 in row.items():
                H[n,l] += val*val2
    require(all(v >= 0 for v in H.values()), "kernel entry sign")
    diag, off, cross = {}, {}, {}
    for (n,l), val in H.items():
        en = add(lam(n), {(): F(-1)})
        el = add(lam(l), {(): F(-1)})
        part = scale(mul(en, el), val)
        if n == l:
            diag = add(diag, part)
        else:
            off = add(off, part)
    for n, val in b.items():
        cross = add(cross, scale(add(lam(n), {(): F(-1)}), -2*val))
    require(centered == add(diag, off), "ordered diagonal/off-diagonal expansion")
    gram = add({(): sum((d*d for d in ds), F(0))}, cross, diag, off)
    require(direct == gram, "full moment Gram identity")
    text = json.dumps([[list(k), str(v)] for k,v in sorted(direct.items())], separators=(",", ":"))
    return {"M": M, "max_integer": 4*M*M,
            "moment_polynomial_terms": len(direct),
            "polynomial_sha256": hashlib.sha256(text.encode()).hexdigest()}


def laurent_product(p, q):
    out = defaultdict(F)
    for a, c in p.items():
        for b, d in q.items():
            out[a+b] += c*d
    return dict(out)


def power_two(x: F) -> int:
    for k in range(-16,17):
        if F(2)**k == x:
            return k
    raise ValueError("log ratio is not a checked power of two")


def integrate_laurent(p, lo, hi):
    rational, log2 = F(0), F(0)
    for n, c in p.items():
        if n == -1:
            log2 += c*power_two(hi/lo)
        else:
            rational += c*(hi**(n+1)-lo**(n+1))/(n+1)
    return rational, log2


def fourier_product(p, q):
    out = defaultdict(F)
    for x, a in p.items():
        for y, b in q.items():
            out[x+y] += a*b
    return dict(out)


def reconstruct():
    left, right = {1:F(1,3), -2:F(-1,192)}, {-2:F(1,3),1:F(-1,192)}
    a1 = integrate_laurent(left,F(1,4),F(1))
    a2 = integrate_laurent(right,F(1),F(4))
    require((a1[0]+a2[0],a1[1]+a2[1]) == (A,F(0)), "weight mass")
    il = integrate_laurent(laurent_product(left,left),F(1,4),F(1))
    ir = integrate_laurent(laurent_product(right,right),F(1),F(4))
    require(il == ir == (F(455,12288),F(-1,144)), "weight-square integral")
    variation = F(1)+F(65,64)+F(1,64)+2*F(21,32)
    require(variation == F(107,32), "weight-derivative total variation")
    require(F(455,3072)-F(1,36)>0, "positive diagonal asymptotic constant")
    lattice = []
    for j in range(2,25):
        L = sum((w(F(n,j*j))/j for n in range(1,4*j*j+1)),F(0))
        err = abs(A*j-L)
        require(err <= F(107,256*j**3), "lattice remainder")
        require(L<j, "lattice size")
        lattice.append(str(err*j**3))
    require(F(107,256)**2+F(1070,256)<5, "summable centering error")
    gram = [exact_correlations(M) for M in range(2,6)]
    cases = [[F(-1),F(0),F(1,4),F(1,3)],
             [F(1,8),F(1,4),F(1,2),F(-2,3)],
             [F(0)]*4]
    for rs in cases:
        count = sum(r>F(1,4) for r in rs)
        for k in range(1,6):
            require(count <= 16**k*sum((r**(2*k) for r in rs),F(0)), "Markov threshold")
    frequency_cases = [({1:F(1,10)}, "one_frequency"),
                       ({1:F(1,20),2:F(1,30)}, "resonant_two_frequencies"),
                       ({1:F(1,25),2:F(1,40),3:F(1,50)}, "resonant_three_frequencies")]
    resonance = {}
    for coeff, name in frequency_cases:
        p = {s*n: c/2 for n,c in coeff.items() for s in (-1,1)}
        mu2 = sum((c*c for c in coeff.values()),F(0))/2
        require(fourier_product(p,p).get(0,F(0))==mu2, "second-moment constant coefficient")
        q, means = {0:F(1)}, []
        for k in range(1,5):
            q = fourier_product(fourier_product(q,p),p)
            mu = q.get(0,F(0))
            require(mu>=mu2**k>0, "resonant higher-moment positivity")
            means.append(str(mu))
        resonance[name] = means
    require(16*F(3,20)**2==F(9,25), "growing-order factor")
    return {
        "schema": "riemann.fixed-moment-attempt.v1",
        "target_count_bound_proved": False,
        "rh_proved": False,
        "conditional_moment_obstruction_machine_proved": False,
        "unconditional_general_count_bound": "floor(M)-1",
        "groups": ["weight_integrals", "derivative_variation", "lattice_remainders",
                   "exact_native_gram_expansion", "threshold_markov", "resonant_fourier_controls",
                   "summable_centering_error", "growing_order_algebra"],
        "lattice_integer_j_range": [2,24],
        "lattice_error_digest": hashlib.sha256(canonical(lattice).encode()).hexdigest(),
        "lattice_cases": len(lattice),
        "gram_records": gram,
        "synthetic_fourier_constant_coefficients": resonance,
        "diagonal_constant": "455/3072-log(2)/36",
        "largest_native_gram_source_integer": 100,
        "scope": "Bounded rational/formal-logarithmic controls only. No analytic PNT, actual zero sum, or count estimate is certified by this program."
    }


def unique_object(pairs):
    out = {}
    for k,v in pairs:
        if k in out:
            raise ValueError("duplicate JSON key")
        out[k] = v
    return out


def canonical(data):
    return json.dumps(data, sort_keys=True, indent=2)+"\n"


def validate_manifest():
    text = (ROOT / "SHA256SUMS").read_text()
    expected = {}
    for line in text.splitlines():
        sha, name = line.split("  ", 1)
        require(name not in expected and "/" not in name and "\\" not in name and name not in (".",".."), "manifest name")
        expected[name] = sha
    files = {p.name for p in ROOT.iterdir()}
    require(files==set(expected)|{"SHA256SUMS"}, "unexpected/missing packet entry")
    for name, sha in expected.items():
        p=ROOT/name
        require(p.is_file() and not p.is_symlink(), "nonregular packet file")
        require(hashlib.sha256(p.read_bytes()).hexdigest()==sha, "manifest hash: "+name)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",type=Path)
    parser.add_argument("--manifest",action="store_true")
    args=parser.parse_args()
    if args.manifest:
        validate_manifest()
    result=reconstruct()
    if args.check is not None:
        loaded=json.loads(args.check.read_text(),object_pairs_hook=unique_object)
        require(canonical(loaded)==canonical(result), "saved result differs from reconstruction")
    print(canonical(result),end="")


if __name__=="__main__":
    main()
