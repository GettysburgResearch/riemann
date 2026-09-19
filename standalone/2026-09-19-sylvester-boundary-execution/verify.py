#!/usr/bin/env python3
"""Independent BCP26 checker: trial factorization + Stieltjes jump identity.

Does not import boundary.py or repository modules. Uses 160-bit directed
arithmetic to validate the producer's 80-bit enclosures by containment, not
merely overlap. Exact Fraction fallback handles a degenerate enclosure.
Same author: implementation separation is NOT independent mathematical review.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

BITS = 80
S = 1 << BITS
T = 1 << 160
CUTOFFS = (3, 7, 15, 31, 63, 255)


def check(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def factor(n: int) -> list[int]:
    out = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            out.append(p)
            n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def reference(Y: int):
    stop = (Y + 1) ** 2
    fs = [[], []] + [factor(n) for n in range(2, stop)]
    mu = [0, 1] + [0 if len(f) != len(set(f)) else (-1) ** len(f) for f in fs[2:]]
    primes = [n for n in range(2, Y + 1) if fs[n] == [n]]
    labels = ["prefix"] + list(map(str, primes)) + ["p>Y"]
    indices = {p: i + 1 for i, p in enumerate(primes)}
    rows = [{Y + 1: sum(mu[1:Y + 1])}] + [{} for _ in labels[1:]]
    for n in range(Y + 1, stop):
        if not mu[n]:
            continue
        d = 1
        for p in reversed(fs[n]):
            if p * d > Y:
                rows[indices.get(p, len(rows) - 1)][n] = mu[n]
                break
            d *= p
        else:
            raise ValueError("squarefree tail had no cutoff pivot")
    rows[0] = {n: v for n, v in rows[0].items() if v}
    return labels, rows, mu


def digest(row: dict[int, int]) -> str:
    return hashlib.sha256("".join(f"{n}:{v}\n" for n, v in sorted(row.items())).encode()).hexdigest()


def jump_terms(a: dict[int, int], b: dict[int, int], left: int, right: int):
    """Stieltjes summation by parts, not constant-interval integration.

    Integral V_a V_b/x^2 = sum_t Delta(V_a V_b)(t)*(1/t-1/right).
    Simultaneous jumps have the indispensable a(t)*b(t) term.
    """
    va = vb = 0
    terms = []
    for n in sorted(set(a) | set(b)):
        da, db = a.get(n, 0), b.get(n, 0)
        delta = da * vb + db * va + da * db
        if delta:
            terms.append((delta * (right - n), n * right))
        va += da
        vb += db
    return terms


def enclose(terms):
    lo = hi = 0
    for a, b in terms:
        q, rem = divmod(T * a, b)
        lo += q
        hi += q + bool(rem)
    return Fraction(lo, T), Fraction(hi, T)


def parse_interval(value):
    check(type(value) is list and len(value) == 2, "bad interval structure")
    check(all(type(x) is str for x in value), "interval endpoints must be strings")
    a, b = (int(x) for x in value)
    check(str(a) == value[0] and str(b) == value[1] and a <= b, "noncanonical interval")
    return Fraction(a, S), Fraction(b, S)


def validates(value, actual, label, exact_terms=None):
    a, b = parse_interval(value)
    lo, hi = actual
    if a <= lo <= hi <= b:
        return
    if exact_terms is not None:
        x = sum((Fraction(n, d) for n, d in exact_terms), Fraction())
        check(a <= x <= b, f"invalid exact enclosure: {label}")
    else:
        raise ValueError(f"invalid enclosure: {label}")


def plus(x, y):
    return x[0] + y[0], x[1] + y[1]


def times_square(x, coefficient):
    a, b = x
    return (0 if a <= 0 <= b else coefficient * min(a*a, b*b), coefficient * max(a*a, b*b))


def test_panel(z):
    check(type(z["Y"]) is int, "Y type alias")
    Y = z["Y"]
    b, stop = Y + 1, (Y + 1) ** 2
    check(type(z["b"]) is int and z["b"] == b, "b")
    check(type(z["B"]) is int and z["B"] == stop - 1, "B")
    labels, rows, mu = reference(Y)
    check(z["labels"] == labels, "channel labels")
    check(z["row_sha256"] == [digest(r) for r in rows], "native channel coefficient digest")
    check(all(type(x) is int for x in z["row_event_counts"]), "event count type alias")
    check(z["row_event_counts"] == [len(r) for r in rows], "event counts")
    expected_fields = {
        "Y", "b", "B", "labels", "row_event_counts", "row_sha256", "gram_upper_triangle", "means",
        "annular_I", "diagonal_D", "ordered_cross_C", "E_input", "u_input", "A_input", "E_output",
        "u_output", "A_output", "F_output", "native_positive_sector",
    }
    check(set(z) == expected_fields, "panel field set")
    check(len(z["gram_upper_triangle"]) == len(rows)*(len(rows)+1)//2, "Gram shape")
    index = 0
    diag = (Fraction(), Fraction())
    for i in range(len(rows)):
        for j in range(i, len(rows)):
            v = z["gram_upper_triangle"][index]
            check(type(v) is list and len(v) == 4, "Gram entry")
            check(type(v[0]) is int and type(v[1]) is int and v[:2] == [i,j], "Gram index/type")
            terms = jump_terms(rows[i], rows[j], b, stop)
            g = enclose(terms)
            validates(v[2:], g, f"G[{i},{j}]", terms)
            if i == j:
                diag = plus(diag, g)
            index += 1
    validates(z["diagonal_D"], diag, "diagonal")
    check(len(z["means"]) == len(rows), "mean shape")
    for i, row in enumerate(rows):
        terms = jump_terms(row, {b: 1}, b, stop)
        validates(z["means"][i], enclose(terms), f"mean[{i}]", terms)

    # Direct Mertens prefix at every output integer; no Newton reconstruction.
    M = 0
    ein, uin, eout, uout, annular = [], [], [], [], []
    for n in range(1, stop):
        M += mu[n]
        eout.append((M*M, n*(n+1)))
        uout.append((M, n*(n+1)))
        if n < b:
            ein.append(eout[-1]); uin.append(uout[-1])
        else:
            annular.append(eout[-1])
    E0, u0 = enclose(ein), enclose(uin)
    E1, u1 = enclose(eout), enclose(uout)
    I = enclose(annular)
    for key, val in [("E_input",E0),("u_input",u0),("E_output",E1),("u_output",u1),("annular_I",I)]:
        validates(z[key], val, key)
    validates(z["A_input"], plus(E0, times_square(u0, 2*b)), "input completion")
    validates(z["A_output"], plus(E1, times_square(u1, 2*stop)), "output completion")
    validates(z["F_output"], plus(E1, times_square(u1, stop)), "innovation state")
    # Independent innovation norm: accumulate reciprocal partial sums directly.
    # All endpoints are integer multiples of 2^-160, avoiding a huge exact LCM.
    ml = mh = flo = fhi = 0
    for n in range(1, stop):
        q, rem = divmod(T * mu[n], n)
        ml += q
        mh += q + bool(rem)
        low = 0 if ml <= 0 <= mh else min(ml*ml, mh*mh)
        high = max(ml*ml, mh*mh)
        flo += low // T
        fhi += -(-high // T)
    validates(z["F_output"], (Fraction(flo,T),Fraction(fhi,T)), "direct reciprocal-sum innovation norm")
    validates(z["ordered_cross_C"], (I[0]-diag[1], I[1]-diag[0]), "ordered cross covariance")

    sector = z["native_positive_sector"]
    if Y < 17:
        check(sector == {"applicable": False} and type(sector["applicable"]) is bool, "sector applicability")
    else:
        P = [p for p in range(2,Y+1) if factor(p)==[p] and Fraction(3*Y,4)<p<=Fraction(4*Y,5)]
        Q = [q for q in range(2,Y+1) if factor(q)==[q] and Fraction(4*Y,5)<q<=Fraction(9*Y,10)]
        n,m=len(P),len(Q)
        expected={"applicable":True,"P":P,"Q":Q,
            "diagonal_lower":str(Fraction(n*m*m,3*Y*Y)),
            "ordered_cross_lower":str(Fraction(n*(n-1)*m*m,3*Y*Y)),
            "coprime_ordered_cross_lower":str(Fraction(n*(n-1)*m*(m-1),3*Y*Y))}
        check(json.dumps(sector,sort_keys=True)==json.dumps(expected,sort_keys=True), "positive sector data")
        for p in P:
            row=rows[labels.index(str(p))]
            check(all(v==1 for v in row.values()), "high-prime channel not positive")
            check(all(row.get(p*q)==1 for q in Q), "semiprime rectangle missing")
        for i,p in enumerate(P):
            gp=enclose(jump_terms(rows[labels.index(str(p))],rows[labels.index(str(p))],b,stop))
            check(gp[0]>=Fraction(m*m,3*Y*Y), "diagonal lower bound")
            for pp in P[i+1:]:
                g=enclose(jump_terms(rows[labels.index(str(p))],rows[labels.index(str(pp))],b,stop))
                check(g[0]>=Fraction(m*m,3*Y*Y), "cross lower bound")
    return stop-1, len(rows)*(len(rows)+1)//2


def verify(data, cutoffs=CUTOFFS):
    check(type(data) is dict, "report object")
    check(set(data)=={"schema","arithmetic","dyadic_denominator_bits","status","panels"}, "report fields")
    check(data["schema"]=="BCP26.boundary-pivot.v1", "schema")
    check(data["arithmetic"]=="directed rational", "arithmetic")
    check(type(data["dyadic_denominator_bits"]) is int and data["dyadic_denominator_bits"]==BITS,"precision")
    check(data["status"]=="FINITE IDENTITIES; NO UNBOUNDED NATIVE UPPER BOUND", "scope")
    check(type(data["panels"]) is list and tuple(p["Y"] for p in data["panels"])==cutoffs, "cutoff list")
    counts=[test_panel(p) for p in data["panels"]]
    return {"coefficient_checks_including_overlaps":sum(x[0] for x in counts),
            "upper_triangle_gram_checks":sum(x[1] for x in counts), "panels":len(counts)}


def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        check(k not in d,"duplicate JSON key")
        d[k]=v
    return d


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("report",type=Path)
    args=p.parse_args()
    data=json.loads(args.report.read_text(),object_pairs_hook=no_duplicates)
    print("BCP26 verifier PASS: "+json.dumps(verify(data),sort_keys=True))

if __name__=="__main__":main()
