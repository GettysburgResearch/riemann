"""STC26 finite transport sectors. Acceptance uses integer-directed intervals."""
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
from exact import S, BITS, ZERO, ONE, rat, add, sub, neg, scale, mul, inv, sqrt_iv, log_int, intersect

CUTOFFS = (3, 7, 15, 31, 63, 127, 255)
BANKS = ((), (2, 3), (2, 3, 5, 7))


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sieve(n):
    spf = list(range(n + 1))
    for p in range(2, isqrt(n) + 1):
        if spf[p] == p:
            for k in range(p*p, n + 1, p):
                if spf[k] == k:
                    spf[k] = p
    mu = [0] * (n + 1)
    mu[1] = 1
    for k in range(2, n + 1):
        p = spf[k]
        mu[k] = 0 if (k // p) % p == 0 else -mu[k // p]
    return spf, mu, [p for p in range(2, n + 1) if spf[p] == p]


def strict_read(path):
    def pairs(items):
        d = {}
        for k, v in items:
            require(k not in d, 'duplicate JSON key')
            d[k] = v
        return d
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def physical(y, mu, primes, sign=1):
    """The full observable, not the matched-sector surrogate."""
    b, N = y+1, (y+1)**2-1
    M = [0] * (N+1)
    jumps = [ZERO] * (N+1)
    for n in range(1, N+1):
        M[n] = M[n-1] + mu[n]
    for p in primes:
        lp = scale(log_int(p), sign)
        for n in range(1, N//p+1):
            if mu[n]:
                jumps[p*n] = add(jumps[p*n], scale(lp, mu[n]))
    E = I = u0 = u1 = P = cum = ZERO
    for n in range(1, N+1):
        cum = add(cum, jumps[n])
        en, mean = rat(M[n]**2, n*(n+1)), rat(M[n], n*(n+1))
        if n < b:
            E, u0 = add(E, en), add(u0, mean)
        else:
            I, u1 = add(I, en), add(u1, mean)
            P = add(P, scale(cum, M[n], n*(n+1)))
    u = add(u0, u1)
    return dict(P=P, E=E, I=I, u_prefix=u0, u_annulus=u1,
                A_output=add(add(E, I), scale(mul(u, u), 2*b*b)))


def sector(y, bank, spf, mu, primes):
    b, X = y+1, (y+1)**2
    N = X-1
    require(len(set(bank)) == len(bank) and all(p in primes for p in bank), 'invalid bank')
    ds = [1]
    for p in bank:
        ds += [p*d for d in ds]
    ds.sort()
    core = [0]*(N+1)
    core[1] = 1
    for n in range(2, N+1):
        p, c = spf[n], core[n//spf[n]]
        core[n] = c if p in bank else (c//p if c % p == 0 else c*p)
    weights = [rat(X-max(b, n), X*max(b, n)) for n in range(N+1)]
    positive = negative = ZERO
    count = 0
    for p in primes:
        pl = pu = nl = nu = 0
        for n in range(1, N//p+1):
            if not mu[n]:
                continue
            t = p*n
            for d in ds:
                m = core[t]*d
                if m > N:
                    break
                require(mu[m] != 0, 'target must be squarefree')
                w = weights[max(t, m)]
                if mu[m]*mu[n] > 0:
                    pl += w[0]; pu += w[1]
                else:
                    nl += w[0]; nu += w[1]
                count += 1
        positive = add(positive, mul(log_int(p), (pl, pu)))
        negative = add(negative, mul(log_int(p), (nl, nu)))
    H = ZERO
    for n in range(1, N+1):
        H = add(H, rat(1, n))
    Z = ONE
    beta = ZERO
    for p in bank:
        v = inv(sqrt_iv(rat(p)))
        Z = mul(Z, add(ONE, v))
        beta = add(beta, mul(log_int(p), v))
    theta = ZERO
    for p in primes:
        theta = add(theta, scale(log_int(p), 1, p))
    bound = mul(mul(H, mul(Z, Z)), add(scale(theta, 2), beta))
    absolute = add(positive, negative)
    require(absolute[1] <= bound[0], 'all-scale sector envelope')
    return dict(bank=list(bank), matched=sub(positive, negative),
                positive_pairs=positive, negative_pairs=negative,
                absolute=absolute, envelope=bound, triples=count)


def empty_identity(y, mu, primes):
    b, X = y+1, (y+1)**2
    first = second = ZERO
    for n in range(1, X):
        if mu[n]:
            first = add(first, scale(log_int(n), X-max(b,n), X*max(b,n)))
    for p in primes:
        if p*p >= X:
            break
        for r in range(1, (X-1)//(p*p)+1):
            if mu[r] and r % p:
                t = max(b, p*p*r)
                second = add(second, scale(log_int(p), X-t, X*t))
    a = log_int(b)
    bound = add(scale(mul(a, a), 3, 2), scale(a, 2))
    require(add(first, second)[1] <= bound[0], 'empty-bank clean bound')
    return dict(diagonal=first, repeated=second, matched=neg(add(first, second)), bound=bound)


def build():
    stages = []
    for y in CUTOFFS:
        spf, mu, primes = sieve((y+1)**2-1)
        row = dict(Y=y, N=(y+1)**2-1, **physical(y, mu, primes))
        row['sectors'] = [sector(y, bank, spf, mu, primes) for bank in BANKS]
        row['empty'] = empty_identity(y, mu, primes)
        require(intersect(row['empty']['matched'], row['sectors'][0]['matched']), 'empty identity')
        for s in row['sectors']:
            s['remainder'] = sub(row['P'], s['matched'])
        stages.append(row)
    spf, mu, primes = sieve(65535)
    fake = physical(255, [abs(v) for v in mu], primes, sign=-1)
    fake['matched_empty'] = stages[-1]['empty']['matched']
    fake['remainder'] = sub(fake['P'], fake['matched_empty'])
    require(fake['remainder'][1] < -100000*S, 'multiplicative family obstruction not detected')
    return dict(schema='STC26-1', bits=BITS, stages=stages, squarefree_sign_control=fake,
                status='proposed sector theorem; unmatched native negative part remains open')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--write', type=Path)
    ap.add_argument('--check', type=Path)
    args = ap.parse_args()
    report = build()
    text = canonical(report)
    if args.write:
        args.write.write_text(text+'\n')
    if args.check:
        require(canonical(strict_read(args.check)) == text, 'complete report reconstruction failed')
    print('STC26 transport OK', hashlib.sha256(text.encode()).hexdigest())


if __name__ == '__main__':
    main()
