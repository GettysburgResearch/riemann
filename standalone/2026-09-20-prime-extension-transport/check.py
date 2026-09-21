"""PET26 producer and exact finite certificates (standard library only)."""
import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from exact import (S, BITS, ZERO, ONE, rat, add, sub, scale, mul, inv,
                   sqrt_iv, root4_int, log_int, intersect, maximum)

CUTOFFS = (3, 7, 15, 31, 63, 127, 255)

def require(ok, message):
    if not ok:
        raise ValueError(message)

def sieve(n):
    spf = list(range(n+1))
    for p in range(2, isqrt(n)+1):
        if spf[p] == p:
            for k in range(p*p, n+1, p):
                if spf[k] == k:
                    spf[k] = p
    mu = [0]*(n+1)
    mu[1] = 1
    for k in range(2, n+1):
        p = spf[k]
        mu[k] = 0 if (k//p) % p == 0 else -mu[k//p]
    return spf, mu, [p for p in range(2, n+1) if spf[p] == p]

def covariances(y):
    b, B = y+1, (y+1)**2-1
    spf, mu, primes = sieve(B+1)
    M = [0]*(B+2)
    for n in range(1, B+2):
        M[n] = M[n-1]+mu[n]
    prime = [ZERO]*(B+1)
    powers = [ZERO]*(B+1)
    coefficient_tests = 0
    for p in primes:
        if p > B:
            break
        lp = log_int(p)
        for m in range(1, B//p+1):
            if mu[m]:
                prime[p*m] = add(prime[p*m], scale(lp, mu[m]))
        q = p*p
        while q <= B:
            for m in range(1, B//q+1):
                if mu[m]:
                    powers[q*m] = add(powers[q*m], scale(lp, mu[m]))
            q *= p
    for n in range(1, B+1):
        require(intersect(add(prime[n], powers[n]),
                          scale(log_int(n), -mu[n])),
                "log-derivative coefficient identity")
        coefficient_tests += 1
    E = I = u0 = u1 = cp = ch = weighted = primitive = ZERO
    pp = ph = J = ZERO
    for k in range(1, B+1):
        pp = add(pp, prime[k])
        ph = add(ph, powers[k])
        w = k*(k+1)
        en = rat(M[k]*M[k], w)
        un = rat(M[k], w)
        lk, ln = log_int(k), log_int(k+1)
        dl = sub(ln, lk)
        if k < b:
            E, u0 = add(E, en), add(u0, un)
        else:
            I, u1 = add(I, en), add(u1, un)
            cp = add(cp, scale(pp, M[k], w))
            ch = add(ch, scale(ph, M[k], w))
            wc = sub(scale(add(lk, ONE), 1, k),
                     scale(add(ln, ONE), 1, k+1))
            weighted = add(weighted, scale(wc, M[k]*M[k]))
            rc = sub(rat(1, k), scale(add(ONE, dl), 1, k+1))
            primitive = add(primitive, add(scale(J, M[k], w),
                                          scale(rc, M[k]*M[k])))
        J = add(J, scale(dl, M[k]))
    require(intersect(add(add(cp, ch), weighted), primitive),
            "integrated signed identity")
    A0 = add(E, scale(mul(u0, u0), 2*b))
    total_u = add(u0, u1)
    A1 = add(add(E, I), scale(mul(total_u, total_u), 2*b*b))
    # Independent finite prefix relation F=E+b*u^2 is inherited, not new.
    return dict(Y=y, B=B, E=E, I=I, u_prefix=u0, u_annulus=u1,
                A_input=A0, A_output=A1, C_prime=cp, C_powers=ch,
                log_energy=weighted, primitive_cross=primitive,
                coefficient_tests=coefficient_tests)

def finite_constants(b):
    _, _, primes = sieve(b)
    atoms = []
    for p in primes:
        q = p*p
        while q <= b*b:
            atoms.append((q, mul(log_int(p), inv(sqrt_iv(rat(q))))))
            q *= p
    def mass(r):
        ans = ZERO
        for q, w in atoms:
            if q <= r:
                ans = add(ans, w)
        return ans
    events = {Fraction(1), Fraction(b)}
    for q, _ in atoms:
        if q <= b:
            events.update((Fraction(q), Fraction(b, q)))
    ll = scale(maximum(add(mass(r), mass(Fraction(b, 1)/r))
                       for r in sorted(events)), 1, 2)
    events = {Fraction(1), Fraction(b)}
    for q, _ in atoms:
        if q <= b:
            events.add(Fraction(q))
        if b <= q <= b*b:
            events.add(Fraction(q, b))
    vals = []
    for r in sorted(events):
        v = ZERO
        for q, w in atoms:
            if r <= q <= b*r:  # closed endpoints are a safe majorant
                v = add(v, w)
        vals.append(v)
    cross = maximum(vals)
    rll = scale(sub(ONE, inv(root4_int(b))), 2)
    rcross = rat(b-1, b)
    d = sub(sub(log_int(b), rll), ll)
    h = add(rcross, cross)
    require(d[0] > 0, "finite damping gate did not pass")
    budget = mul(mul(h, h), inv(scale(d, 4)))
    return dict(power_atoms=len(atoms), L_same=ll, L_cross=cross,
                R_same=rll, R_cross=rcross, damping=d,
                coupling=h, positive_budget=budget)

def full_report():
    stages = []
    for y in CUTOFFS:
        row = covariances(y)
        cons = finite_constants(y+1)
        rhs = sub(mul(cons["coupling"], sqrt_iv(mul(row["E"], row["I"]))),
                  mul(cons["damping"], row["I"]))
        require(row["C_prime"][1] <= rhs[0], "native signed upper bound")
        row.update(cons)
        row["signed_upper"] = rhs
        stages.append(row)
    # Non-native delta source: its complete cumulative is identically one.
    b, B = 256, 256**2-1
    _, _, primes = sieve(B)
    fake_cp = ZERO
    for p in primes:
        fake_cp = add(fake_cp, scale(log_int(p),
                                   b*b-max(b, p), max(b, p)*b*b))
    E, I = rat(b-1, b), rat(b-1, b*b)
    cons = finite_constants(b)
    fake_bound = sub(mul(cons["coupling"], sqrt_iv(mul(E, I))),
                     mul(cons["damping"], I))
    require(fake_cp[0] > fake_bound[1], "fake source must fail native law")
    return dict(schema="PET26-1", bits=BITS, stages=stages,
                control=dict(source="delta", Y=255, C_prime=fake_cp,
                             native_bound_without_defect=fake_bound,
                             rejected=True),
                status="finite certificates; no native Newton gain")

def canonical(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def read_strict(path):
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise ValueError("duplicate JSON key")
            out[k] = v
        return out
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError("nonfinite JSON")))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--write", type=Path)
    p.add_argument("--check", type=Path)
    args = p.parse_args()
    report = full_report()
    if args.write:
        args.write.write_text(canonical(report)+"\n")
    if args.check:
        require(canonical(read_strict(args.check)) == canonical(report),
                "report differs from complete reconstruction")
    print("PET26 OK", hashlib.sha256(canonical(report).encode()).hexdigest())

if __name__ == "__main__":
    main()
