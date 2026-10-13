"""validate_core.py -- brute-force replay of lab_core.c and of the Pellet/Stickelberger identity.

EXACT (integer arithmetic in Z[omega] as pairs (a,b) = a + b*omega).
Usage: python3 -I validate_core.py q dmax kmax CORE_OUTPUT
  checks, for every d <= dmax and every exact row degree k <= kmax, that
  sum_{u monic, deg u = k} |A_u(d)|^2 from the definition A_u(d) = sum_{deg n = d} mu(n) chi0(Res(n,u))
  equals the lab_core value; and checks Pellet: mu(n) = (-1)^d * chi_2(disc n) for all monic n,
  deg n <= dmax, with disc n = (-1)^{d(d-1)/2} Res(n, n').
"""
import sys
from ffcommon import monics, resultant, deriv, dlog_table, primes_upto, mobius, deg

Z6 = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]


def nrm(z):
    a, b = z
    return a * a - a * b + b * b


def main():
    q, dmax, kmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    core = {}
    for line in open(sys.argv[4]):
        if line.startswith('#'):
            continue
        t = line.split()
        core[(int(t[0]), int(t[1]))] = (int(t[3]), int(t[4]))
    g, dl = dlog_table(q)
    primes = primes_upto(max(dmax, kmax), q)
    ok = True
    # Pellet
    npell = 0
    for d in range(1, dmax + 1):
        for n in monics(d, q):
            mu = mobius(n, q, primes)
            r = resultant(n, deriv(n, q), q)
            if r == 0:
                assert mu == 0
                continue
            disc = r if (d * (d - 1) // 2) % 2 == 0 else (-r) % q
            chi2 = 1 if dl[disc] % 2 == 0 else -1
            if mu != (-1) ** d * chi2:
                ok = False
                print('PELLET FAIL', n)
            npell += 1
    print(f'Pellet mu(n) = (-1)^d chi_2(disc n): checked {npell} squarefree monic n, deg <= {dmax}: {"OK" if ok else "FAIL"}')
    # brute-force moments
    cols = {d: [(n, mobius(n, q, primes)) for n in monics(d, q)] for d in range(1, dmax + 1)}
    for k in range(0, kmax + 1):
        for d in range(1, dmax + 1):
            M2 = 0
            Dg = 0
            for u in monics(k, q):
                a = [0, 0]
                for n, mu in cols[d]:
                    if mu == 0:
                        continue
                    r = resultant(n, u, q)
                    if r == 0:
                        continue
                    Dg += 1
                    z = Z6[dl[r] % 6]
                    a[0] += mu * z[0]
                    a[1] += mu * z[1]
                M2 += nrm(a)
            c = core.get((d, k))
            good = c == (M2, Dg)
            ok &= good
            print(f'k={k} d={d}: brute M2={M2} Diag={Dg} core={c} {"OK" if good else "MISMATCH"}')
    print('ALL OK' if ok else 'SOME FAILURES')


if __name__ == '__main__':
    main()
