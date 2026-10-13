"""leverage_check.py -- EXACT check of the sixth-power-row (leverage) identities in the lab.

(i)  principal rows: A_{v^6}(d) = sum_{(n,v)=1} mu(n) = [x^d] (1 - q x) prod_{P | v} (1 - x^{deg P})^{-1};
     in particular A_1(d) = 0 for d >= 2 (F_q[T] has no zeta zeros: the extraction target must be a twist).
(ii) member rows: for v prime, v not dividing w:  A_{w v^6}(d) = sum_{j>=0} chi_v(w)^j A_w(d-j),
     with chi_v(w) = chi0(Res(v, w))  (exact separation of multiples of v, RUNG_STRENGTH Prop. R' step 3).
Brute force from the definition A_u(d) = sum_{deg n = d} mu(n) chi0(Res(n,u)); integer arithmetic in Z[omega].
Usage: python3 leverage_check.py q dmax
"""
import sys
from ffcommon import monics, resultant, dlog_table, primes_upto, mobius, pmul, deg

Z6 = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]


def zmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def main():
    q, dmax = int(sys.argv[1]), int(sys.argv[2])
    g, dl = dlog_table(q)
    primes = primes_upto(dmax + 2, q)
    cols = {d: [(n, mobius(n, q, primes)) for n in monics(d, q)] for d in range(0, dmax + 1)}

    def A(u, d):
        s = [0, 0]
        for n, mu in cols[d]:
            if mu == 0:
                continue
            r = resultant(n, u, q) if d > 0 else 1
            if r == 0:
                continue
            z = Z6[dl[r] % 6]
            s[0] += mu * z[0]
            s[1] += mu * z[1]
        return tuple(s)

    def p6(v):
        r = (1,)
        for _ in range(6):
            r = pmul(r, v, q)
        return r

    ok = True
    # (i) principal rows v^6, v linear and v quadratic irreducible
    for v in [(1, 1), (1, 0, 1)]:  # T+1 and T^2+1 (irreducible for q = 7)
        u = p6(v)
        for d in range(0, dmax + 1):
            a = A(u, d)
            # [x^d] (1 - qx) / (1 - x^{deg v})
            e = deg(v)
            pred = (1 if d % e == 0 else 0) - (q if d >= 1 and (d - 1) % e == 0 else 0)
            good = a == (pred, 0)
            ok &= good
            print(f'(i)  u = v^6, v={v}, d={d}: A_u(d) = {a}, predicted {pred}: {"OK" if good else "FAIL"}')
    # (ii) member rows
    tests = [((1, 0, 1), (2, 1)), ((3, 1, 0, 1), (5, 1)), ((2, 0, 1), (1, 1))]
    for w, v in tests:
        u = pmul(w, p6(v), q)
        Aw = [A(w, d) for d in range(dmax + 1)]
        cv = resultant(v, w, q)
        z = Z6[dl[cv] % 6] if cv else (0, 0)
        for d in range(dmax + 1):
            pred = (0, 0)
            zj = (1, 0)
            for j in range(0, d + 1):
                t = zmul(zj, Aw[d - j])
                pred = (pred[0] + t[0], pred[1] + t[1])
                zj = zmul(zj, z)
            a = A(u, d)
            good = a == pred
            ok &= good
            print(f'(ii) w={w}, v={v}, deg u={deg(u)}, d={d}: A_wv^6(d)={a}, sum_j chi_v(w)^j A_w(d-j)={pred}, |A_w(d)|^2={Aw[d][0]**2-Aw[d][0]*Aw[d][1]+Aw[d][1]**2}: {"OK" if good else "FAIL"}')
    print('ALL OK' if ok else 'FAILURES')


if __name__ == '__main__':
    main()
