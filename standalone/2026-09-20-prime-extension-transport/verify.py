"""Second implementation of the core certificates.

Uses trial factorization, a tail primitive of M, and the finite repeated-prime
collapse. Does NOT import check.py. Shares only exact interval arithmetic.
Not independent mathematical review and not a reconstruction of every field.
"""
import argparse
import json
from pathlib import Path
from exact import (S, ZERO, rat, add, sub, scale, mul, log_int, intersect,
                   decode)

def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0)+1
    return out

def require(ok, message):
    if not ok:
        raise ValueError(message)

def strict(path):
    def pairs(xs):
        d = {}
        for k, v in xs:
            require(k not in d, "duplicate key")
            d[k] = v
        return d
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs)

def verify(path):
    report = strict(path)
    require(report.get("schema") == "PET26-1", "schema")
    require(type(report.get("bits")) is int and report["bits"] == 112, "bits")
    require([r["Y"] for r in report["stages"]] == [3,7,15,31,63,127,255], "cutoffs")
    total = 0
    for row in report["stages"]:
        Y = row["Y"]
        require(type(Y) is int, "cutoff type")
        b, B = Y+1, (Y+1)**2-1
        require(type(row["B"]) is int and row["B"] == B, "endpoint")
        fs = [{}]+[factor(n) for n in range(1, B+1)]
        mu = [0]+[0 if any(e>1 for e in fs[n].values()) else (-1)**len(fs[n])
                  for n in range(1, B+1)]
        primes = [n for n in range(2, B+1) if fs[n] == {n:1}]
        M = [0]*(B+1)
        for n in range(1, B+1):
            M[n] = M[n-1]+mu[n]
        tail = [ZERO]*(B+2)
        for n in range(B, b-1, -1):
            tail[n] = add(tail[n+1], rat(M[n], n*(n+1)))
        cp = ch = E = I = up = ua = ZERO
        # Reverse summation: integrate each jump using the entire M tail.
        for p in primes:
            scalar = ZERO
            for m in range(1, B//p+1):
                if mu[m]:
                    scalar = add(scalar, scale(tail[max(b, p*m)], mu[m]))
            cp = add(cp, mul(log_int(p), scalar))
            scalar = ZERO
            for m in range(1, B//(p*p)+1):
                if m%p and mu[m]:
                    scalar = add(scalar, scale(tail[max(b, p*p*m)], mu[m]))
            ch = add(ch, mul(log_int(p), scalar))
        for n in range(1, B+1):
            # Per-prime symbolic log coefficients; no analytic logarithms here.
            for p, exponent in fs[n].items():
                terms = sum(mu[n//(p**j)] for j in range(1, exponent+1))
                require(terms == -exponent*mu[n], "symbolic native log identity")
                hterms = sum(mu[n//(p**j)] for j in range(2, exponent+1))
                want = mu[n//(p*p)] if exponent == 2 else 0
                require(hterms == want, "exact repeated-prime collapse")
            en = rat(M[n]*M[n], n*(n+1))
            un = rat(M[n], n*(n+1))
            if n < b:
                E, up = add(E, en), add(up, un)
            else:
                I, ua = add(I, en), add(ua, un)
        expected = dict(E=E, I=I, u_prefix=up, u_annulus=ua,
                        C_prime=cp, C_powers=ch,
                        A_input=add(E, scale(mul(up, up), 2*b)),
                        A_output=add(add(E, I), scale(mul(add(up,ua), add(up,ua)), 2*b*b)))
        for key, val in expected.items():
            got = decode(row[key])
            require(got[1]-got[0] < S//10**20, "overwide supplied interval")
            require(intersect(got, val), "independent mismatch: "+key)
        require(decode(row["C_prime"])[1] < 0, "finite sign control")
        total += B
    require(report["control"]["rejected"] is True, "control flag")
    require(decode(report["control"]["C_prime"])[0] >
            decode(report["control"]["native_bound_without_defect"])[1], "control gap")
    print("PET26 independent core replay OK:", total, "coefficient indices")
    return total

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("report", nargs="?", default="result.json")
    verify(p.parse_args().report)
