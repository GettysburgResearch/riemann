"""C5 experiment E4: can a fake curve zeta be written as a 'quadratic-character-type' Euler product
over the places of P^1/F_q ?  (function-field analogue of a degree-1 Selberg-class element with
real coefficients)

Target object: L(T) = prod_{v in |P^1|} (1 - a_v T^{deg v})^{-1} with
   a_v in {+1,-1} for v outside a finite set S,  a_v = 0 for v in S,  sum_{v in S} deg v = 2g+2,
such that L(T) = P(T) (P a fake: (F1)-(F3) hold, RH fails).  Only the counts per degree matter:
   x_d = #{v: deg v = d, a_v=+1},  y_d = #{v: deg v=d, a_v=-1},  r_d = #{v in S: deg v = d},
   x_d + y_d + r_d = n_d(P^1),  and  P(T) = prod_d (1-T^d)^{-x_d} (1+T^d)^{-y_d}.
Since (1+T^d)^{-1} = (1-T^d)(1-T^{2d})^{-1}, writing P = prod (1-T^d)^{-c_d} (unique, c_d = B_d - n_d)
gives  x_d - y_d = c_d - y_{d/2} =: delta_d ,  x_d + y_d = u_d := n_d - r_d  (y_{d/2}=0, d odd).
So x_d, y_d are FORCED by (P, S): x_d = (u_d+delta_d)/2, y_d = (u_d-delta_d)/2.
Conditions: parity u_d = delta_d mod 2 for all d, and |delta_d| <= u_d for all d.
Report C5-L2: parity for all d  <=>  P(T)(1-T)(1-qT) = prod_{v in S}(1 - T^{deg v})  in F_2[T]
(a finite check).  |delta_d| <= u_d: exact for d <= D1, explicit monotone tail bound beyond D1
(requires max|alpha| < q, Arb upper bound).
"""
import json, os, sys, time, hashlib, platform, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flint, sympy
from ff_common import place_counts, mobius, divisors, max_modulus_upper, power_sums
from ff_fake_census import census

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results', 'C5-function-field-transfer')


def n_places_P1(q, d):
    if d == 1:
        return q + 1
    return sum(mobius(d // e) * q ** e for e in divisors(d)) // d


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield []
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest


def mod2_identity(P, q, parts):
    # left: P(T)(1-T)(1-qT) mod 2 ; right: prod (1 - T^d) mod 2
    left = [c % 2 for c in P]
    for fac in ([1, -1], [1, -q]):
        out = [0] * (len(left) + 1)
        for i, a in enumerate(left):
            out[i] += a * fac[0]
            out[i + 1] += a * fac[1]
        left = [c % 2 for c in out]
    right = [1]
    for d in parts:
        f = [1] + [0] * (d - 1) + [1]   # 1 - T^d = 1 + T^d mod 2
        out = [0] * (len(right) + d)
        for i, a in enumerate(right):
            out[i] += a
            out[i + d] += a
        right = [c % 2 for c in out]
    L = max(len(left), len(right))
    left += [0] * (L - len(left)); right += [0] * (L - len(right))
    return left == right


def tail_D1(q, g, A_up):
    """Smallest D1 such that G(d)/q^d is increasing for d>=D1 and G(D1)>0, where
    G(d) = q^d - 2g A^d - g d A^{d/2} - 2(d+1) q^{d/2} - (2g+2) d   (A = A_up < q)."""
    lnq = math.log(q)
    th = max(1.0 / math.log(q / math.sqrt(A_up)), 2.0 / lnq, 1.0 / lnq) + 1
    d = max(2, int(math.ceil(th)))
    Aa = flint.arb(A_up); qa = flint.arb(q)
    while True:
        G = qa ** d - 2 * g * Aa ** d - g * d * Aa ** (flint.arb(d) / 2) - 2 * (d + 1) * qa ** (flint.arb(d) / 2) - (2 * g + 2) * d
        if G > 0:
            return d
        d += 1
        if d > 5000:
            return None


def realize(P, q, g):
    A_up, _ = max_modulus_upper(P)
    if not A_up < q:
        return dict(status='A_not_below_q')
    D1 = tail_D1(q, g, A_up)
    if D1 is None:
        return dict(status='tail_cap')
    Dc = max(D1, 40)
    s, N, B = place_counts(P, q, Dc)
    found = []
    for parts in partitions(2 * g + 2):
        r = {}
        for d in parts:
            r[d] = r.get(d, 0) + 1
        if any(r[d] > n_places_P1(q, d) for d in r):
            continue
        if not mod2_identity(P, q, parts):
            continue
        x, y = {}, {}
        ok = True
        why = None
        for d in range(1, Dc + 1):
            nd = n_places_P1(q, d)
            c_d = B[d] - nd
            delta = c_d - (y.get(d // 2, 0) if d % 2 == 0 else 0)
            u = nd - r.get(d, 0)
            if (u - delta) % 2 != 0:
                ok = False; why = ('parity', d); break
            if abs(delta) > u:
                ok = False; why = ('size', d, delta, u); break
            x[d] = (u + delta) // 2; y[d] = (u - delta) // 2
        rec = dict(parts=parts, ok=ok, why=why, D1=D1)
        if ok:
            # reconstruction check mod T^{D1+1}
            M = 40
            ser = [1] + [0] * M
            def mul_series(a, b):
                out = [0] * (M + 1)
                for i, ai in enumerate(a):
                    if ai:
                        for j in range(0, M + 1 - i):
                            out[i + j] += ai * b[j]
                return out
            for d in range(1, M + 1):
                # (1-T^d)^{-x} = sum binom(x+k-1,k) T^{dk}; (1+T^d)^{-y} = sum (-1)^k binom(y+k-1,k) T^{dk}
                f = [0] * (M + 1); h = [0] * (M + 1)
                for k in range(0, M // d + 1):
                    f[d * k] = math.comb(x[d] + k - 1, k) if k else 1
                    h[d * k] = (-1) ** k * (math.comb(y[d] + k - 1, k) if k else 1)
                ser = mul_series(mul_series(ser, f), h)
            Ppad = list(P) + [0] * (M + 1 - len(P))
            rec['reconstruction_ok_mod_T^%d' % (M + 1)] = (ser[:M + 1] == Ppad[:M + 1])
            rec['x_1_6'] = [x[d] for d in range(1, 7)]
            rec['y_1_6'] = [y[d] for d in range(1, 7)]
            rec['n_P1_1_6'] = [n_places_P1(q, d) for d in range(1, 7)]
        found.append(rec)
    return dict(status='done', A_up=A_up, attempts=found,
                realizable=any(f['ok'] for f in found))


def main():
    cases = [(5, 1), (7, 1), (9, 1), (11, 1), (13, 1), (25, 1), (3, 2), (5, 2), (7, 2), (9, 2), (3, 3)]
    t0 = time.time()
    allres = []
    for q, g in cases:
        t1 = time.time()
        C = census(q, g, audit_rate=0.0)
        fakes = C['fakes']
        nreal = 0; examples = []
        tested = 0
        nonreal_realizable = 0
        for f in fakes:
            P = f['P_asc']
            res = realize(P, q, g)
            tested += 1
            if res.get('realizable'):
                nreal += 1
                if f['nonreal_x']:
                    nonreal_realizable += 1
                if len(examples) < 4 or (f['nonreal_x'] and nonreal_realizable <= 2):
                    good = [a for a in res['attempts'] if a['ok']]
                    examples.append(dict(P_asc=P, h_asc=f['h_asc'], nonreal_x=f['nonreal_x'],
                                         alpha_moduli_over_sqrtq=f['alpha_moduli_over_sqrtq'],
                                         ramification=good[0]['parts'], D1=good[0]['D1'],
                                         x_1_6=good[0]['x_1_6'], y_1_6=good[0]['y_1_6'],
                                         n_P1_1_6=good[0]['n_P1_1_6'],
                                         recon={k: v for k, v in good[0].items() if k.startswith('reconstruction')}))
        r = dict(q=q, g=g, fakes=len(fakes), tested=tested, realizable_as_quadratic_type=nreal,
                 realizable_with_nonreal_x=nonreal_realizable, examples=examples,
                 runtime_s=round(time.time() - t1, 1))
        print({k: v for k, v in r.items() if k != 'examples'}, flush=True)
        allres.append(r)
    meta = dict(script='ff_fake_quadratic.py', python=platform.python_version(), flint=flint.__version__,
                sympy=sympy.__version__, runtime_s=round(time.time() - t0, 1))
    fn = os.path.join(OUT, 'fake_quadratic.json')
    with open(fn, 'w') as fh:
        json.dump(dict(meta=meta, results=allres), fh, indent=1, default=str)
    print('wrote', fn, hashlib.sha256(open(fn, 'rb').read()).hexdigest())


if __name__ == '__main__':
    main()
