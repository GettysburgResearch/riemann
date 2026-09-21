"""STC26 separate verifier: trial factors, three-case fibres, reverse integrals.
Does not import transport.py. Shared exact.py is the directed scalar arithmetic.
"""
import argparse
import json
from math import gcd
from pathlib import Path
from exact import S, ZERO, ONE, rat, add, sub, neg, scale, mul, inv, sqrt_iv, log_int, intersect, decode

YS = (3, 7, 15, 31, 63, 127, 255)
BANKS = ((), (2, 3), (2, 3, 5, 7))


def need(ok, message):
    if not ok:
        raise ValueError(message)


def load(path):
    def pairs(items):
        out = {}
        for k, v in items:
            need(k not in out, 'duplicate key')
            out[k] = v
        return out
    return json.loads(Path(path).read_text(), object_pairs_hook=pairs)


def trial(N):
    mu, ps = [0]*(N+1), []
    mu[1] = 1
    for n in range(2, N+1):
        q, count, square, d = n, 0, False, 2
        while d*d <= q:
            if q % d == 0:
                q //= d
                count += 1
                if q % d == 0:
                    square = True
                while q % d == 0:
                    q //= d
            d += 1
        if q > 1:
            count += 1
        mu[n] = 0 if square else (-1 if count % 2 else 1)
        if count == 1 and not square:
            ps.append(n)
    return mu, ps


def interval_match(given, expected, name):
    x = decode(given)
    need(x[1]-x[0] < S//(1 << 48), name+' excessively wide')
    need(intersect(x, expected), name+' interval mismatch')


def fibres(y, bank, mu, primes):
    b, X = y+1, (y+1)**2
    N = X-1
    bankproduct, ds = 1, [1]
    for p in bank:
        bankproduct *= p
        ds += [p*d for d in ds]
    ds = [d for d in ds if d <= N]
    weights = [rat(X-max(b,n), X*max(b,n)) for n in range(N+1)]
    positive = negative = ZERO
    count = 0
    for p in primes:
        sums = [[0, 0], [0, 0]]
        for a in ds:
            for c in ds:
                cases = [(max(a, p*c), mu[a]*mu[c], bankproduct)] if p in bank else [
                    (p*max(a,c), -mu[a]*mu[c], bankproduct*p),
                    (max(a,p*p*c), -mu[a]*mu[c], bankproduct*p)]
                for h, sign, excluded in cases:
                    for r in range(1, N//h+1):
                        if mu[r] == 0 or gcd(r, excluded) != 1:
                            continue
                        w = weights[r*h]
                        dst = sums[0 if sign > 0 else 1]
                        dst[0] += w[0]; dst[1] += w[1]
                        count += 1
        positive = add(positive, mul(log_int(p), sums[0]))
        negative = add(negative, mul(log_int(p), sums[1]))
    H, th, beta, Z = ZERO, ZERO, ZERO, ONE
    for n in range(1,N+1):
        H = add(H,rat(1,n))
    for p in primes:
        th = add(th,scale(log_int(p),1,p))
    for p in bank:
        u = inv(sqrt_iv(rat(p)))
        Z = mul(Z,add(ONE,u)); beta=add(beta,mul(log_int(p),u))
    return dict(positive_pairs=positive,negative_pairs=negative,
                matched=sub(positive,negative),absolute=add(positive,negative),
                envelope=mul(mul(H,mul(Z,Z)),add(scale(th,2),beta))),count


def reverse(y, mu, primes, sign=1):
    b, X = y+1, (y+1)**2
    N = X-1
    M=[0]*(N+1)
    for k in range(1,N+1):
        M[k]=M[k-1]+mu[k]
    tail=[ZERO]*(N+2)
    E=I=u0=ZERO
    for k in range(N,0,-1):
        v=rat(M[k],k*(k+1))
        if k>=b:
            tail[k]=add(tail[k+1],v)
            I=add(I,rat(M[k]**2,k*(k+1)))
        else:
            tail[k]=tail[b]
            E=add(E,rat(M[k]**2,k*(k+1)));u0=add(u0,v)
    P=ZERO
    for p in primes:
        total=ZERO
        for n in range(1,N//p+1):
            if mu[n]:total=add(total,scale(tail[p*n],mu[n]))
        P=add(P,scale(mul(log_int(p),total),sign))
    u1=tail[b];u=add(u0,u1)
    return dict(P=P,E=E,I=I,u_prefix=u0,u_annulus=u1,
                A_output=add(add(E,I),scale(mul(u,u),2*X)))


def verify(report):
    need(report['schema']=='STC26-1' and type(report['bits']) is int and report['bits']==112,'schema')
    need(len(report['stages'])==len(YS),'stage count')
    total=0
    for row,y in zip(report['stages'],YS):
        N=(y+1)**2-1
        need(type(row['Y']) is int and row['Y']==y and type(row['N']) is int and row['N']==N,'endpoints')
        mu,ps=trial(N)
        for k,v in reverse(y,mu,ps).items():interval_match(row[k],v,k)
        need(len(row['sectors'])==3,'bank count')
        for s,bank in zip(row['sectors'],BANKS):
            need(s['bank']==list(bank) and all(type(x) is int for x in s['bank']),'bank')
            expected,count=fibres(y,bank,mu,ps)
            need(type(s['triples']) is int and s['triples']==count,'triple count')
            for k,v in expected.items():interval_match(s[k],v,k)
            interval_match(s['remainder'],sub(decode(row['P']),expected['matched']),'remainder')
            total+=count
        empty=row['empty'];d1=d2=ZERO
        b,X=y+1,(y+1)**2
        for n in range(1,X):
            if mu[n]:d1=add(d1,scale(log_int(n),X-max(b,n),X*max(b,n)))
        for p in ps:
            for r in range(1,N//(p*p)+1):
                if mu[r] and r%p:
                    h=max(b,p*p*r);d2=add(d2,scale(log_int(p),X-h,X*h))
        interval_match(empty['diagonal'],d1,'empty diagonal')
        interval_match(empty['repeated'],d2,'empty repeated')
        interval_match(empty['matched'],neg(add(d1,d2)),'empty total')
        a=log_int(b)
        interval_match(empty['bound'],add(scale(mul(a,a),3,2),scale(a,2)),'clean bound')
    fake=report['squarefree_sign_control']
    mu,ps=trial(65535)
    expected=reverse(255,[abs(x) for x in mu],ps,-1)
    for k,v in expected.items():interval_match(fake[k],v,'control '+k)
    interval_match(fake['matched_empty'],decode(report['stages'][-1]['empty']['matched']),'control matched')
    interval_match(fake['remainder'],sub(expected['P'],decode(fake['matched_empty'])),'control remainder')
    return total


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('report',type=Path)
    args=ap.parse_args()
    print('STC26 separate verification OK:',verify(load(args.report)),'matched triples')
