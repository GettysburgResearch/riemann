"""SKEPTIC independent re-implementation of C5-E4 (quadratic-type realisations of fakes over P^1/F_q).

Algorithm (different from ff_fake_quadratic.py): log-derivative identity.  If
  P(T) = prod_v (1 - a_v T^{deg v})^{-1},  a_v in {+1,-1} off S, 0 on S,
with x_d (resp. y_d) places of degree d with a_v=+1 (resp. -1), then comparing T d/dT log:
  -s_n(P) = sum_{d|n} d (x_d + (-1)^{n/d} y_d)      (n >= 1)
so x_n - y_n = ( -s_n - sum_{d|n,d<n} d (x_d + (-1)^{n/d} y_d) ) / n  must be an integer, and
x_n + y_n = u_n = n_n(P^1) - r_n.  Checked exactly for n <= Dmax = max(D1, 80); tail n > D1 by the
investigator's G(d) bound (re-derived by the skeptic, see SKEPTIC_REVIEW.md) with my own Arb A.
Parity for ALL n is guaranteed by the mod-2 lemma C5-L2 (re-derived by the skeptic); here it is
additionally checked for n <= Dmax.  The candidate S are all multisets of degrees summing to 2g+2
with r_d <= n_d(P^1).
"""
import sys, os, math, json, time, hashlib
import flint
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skeptic_census_indep as S


def nP1(q, d):
    # number of closed points of degree d on P^1/F_q (degree 1 includes infinity).
    # (first version omitted infinity for d=1 -> 0 realisations; recorded as a skeptic bug)
    if d == 1:
        return q + 1
    return sum(S.mu(d // e) * q ** e for e in range(1, d + 1) if d % e == 0) // d


def parts(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield []
        return
    for k in range(min(n, m), 0, -1):
        for r in parts(n - k, k):
            yield [k] + r


def D1_of(q, g, A):
    qa = flint.arb(q)
    th = max(1.0 / math.log(q / math.sqrt(float(A.upper()))), 2.0 / math.log(q)) + 1
    d = max(2, int(math.ceil(th)))
    while True:
        da = flint.arb(d)
        G = qa ** d - 2 * g * A ** d - g * d * A ** (da / 2) - 2 * (d + 1) * qa ** (da / 2) - (2 * g + 2) * d
        if G > 0:
            return d
        d += 1
        if d > 5000:
            return None


def realise(P, q, g):
    mods = S.moduli_upper(P)
    A = max(mods)
    if not A < flint.arb(q):
        return None
    D1 = D1_of(q, g, A)
    if D1 is None:
        return None
    Dm = max(D1, 80)
    s = S.psums(P, Dm)
    good = []
    for pt in parts(2 * g + 2):
        r = {}
        for d in pt:
            r[d] = r.get(d, 0) + 1
        if any(r[d] > nP1(q, d) for d in r):
            continue
        x = {}
        y = {}
        ok = True
        for n in range(1, Dm + 1):
            acc = -s[n]
            for d in range(1, n):
                if n % d == 0:
                    acc -= d * (x[d] + (-1) ** (n // d) * y[d])
            if acc % n:
                ok = False
                break
            delta = acc // n
            u = nP1(q, n) - r.get(n, 0)
            if (u - delta) % 2 or abs(delta) > u:
                ok = False
                break
            x[n] = (u + delta) // 2
            y[n] = (u - delta) // 2
        if ok:
            good.append(dict(S_degrees=pt, x1_3=[x[1], x[2], x[3]], y1_3=[y[1], y[2], y[3]], D1=D1))
    return good


def main():
    cases = [(5, 1), (7, 1), (9, 1), (11, 1), (13, 1), (25, 1), (3, 2), (5, 2), (7, 2), (9, 2), (3, 3)]
    out = []
    t0 = time.time()
    for q, g in cases:
        C = S.census(q, g)  # recomputes fakes (independent census); keep non-degenerate fakes only
        # census() keeps only a sample of fakes; re-enumerate fakes fully here:
        fakes = []

        def rec(c):
            k = len(c) - 1
            bnd = [math.comb(g, j) * (q + 1) ** j for j in range(g + 1)]
            if k == g:
                P = S.P_of(c, q)
                st, info = S.admissible(P, q, g)
                if st == 'yes':
                    rh, nreal = S.rh_exact(c, q)
                    if not rh:
                        fakes.append((c, P, nreal < g))
                return
            for ck in range(-bnd[k + 1], bnd[k + 1] + 1):
                cc = c + [ck]
                Pp = S.P_of(cc + [0] * (g - k - 1), q)
                s_, N_, B_ = S.Bvals(Pp, q, k + 1)
                if all(B_[d] >= 0 for d in range(1, k + 2)):
                    rec(cc)
        rec([1])
        nreal_ = 0
        nreal_nonreal = 0
        ex = []
        for c, P, nonreal in fakes:
            gd = realise(P, q, g)
            if gd:
                nreal_ += 1
                if nonreal:
                    nreal_nonreal += 1
                if len(ex) < 3:
                    ex.append(dict(c=c, P=P, nonreal=nonreal, sols=gd[:2]))
        rec_ = dict(q=q, g=g, fakes=len(fakes), realisable=nreal_, realisable_nonreal_x=nreal_nonreal,
                    examples=ex)
        print({k: v for k, v in rec_.items() if k != 'examples'}, flush=True)
        out.append(rec_)
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results',
                      'C5-function-field-transfer', 'skeptic_quadratic_indep.json')
    with open(fn, 'w') as f:
        json.dump(dict(results=out, runtime_s=round(time.time() - t0, 1), flint=flint.__version__), f,
                  indent=1, default=str)
    print('wrote', fn, hashlib.sha256(open(fn, 'rb').read()).hexdigest())


if __name__ == '__main__':
    main()
