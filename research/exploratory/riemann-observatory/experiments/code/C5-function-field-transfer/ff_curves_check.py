"""C5 experiment E2 (validation): genuine curves vs. the Toeplitz/Weil-bound criteria.

For a few smooth projective hyperelliptic curves y^2 = f(x) (deg f = 2g+1, odd p) over F_p:
  * brute-force N_r = #C(F_{p^r}) for r = 1..rmax (F_{p^r} implemented as F_p[t]/(irreducible)),
  * reconstruct P(T) from N_1..N_g (Newton identities + functional equation),
  * check that the predicted N_r (r = g+1..rmax) agree with brute force (code-path validation),
  * decide RH exactly (Sturm, ff_common.rh_exact) and confirm the Toeplitz matrices T_N have no
    certified negative direction (they are PSD of rank <= 2g by THEOREM C5-T1/T2),
  * check B_d >= 0 for all d (ff_common.positivity_all_degrees).
"""
import json, os, sys, time, hashlib, platform, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flint, sympy, numpy as np
from ff_common import power_sums, rh_exact, positivity_all_degrees, toeplitz_negative_witness, h_from_P

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results', 'C5-function-field-transfer')


def polymod(a, m, p):
    a = [c % p for c in a]
    while len(a) >= len(m):
        if a[-1] == 0:
            a.pop(); continue
        c = a[-1]; sh = len(a) - len(m)
        for i, mc in enumerate(m):
            a[sh + i] = (a[sh + i] - c * mc) % p
        a.pop()
    while a and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b, m, p):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return polymod(out, m, p)


def ppow(a, e, m, p):
    r = [1]
    while e:
        if e & 1:
            r = pmul(r, a, m, p)
        a = pmul(a, a, m, p); e >>= 1
    return r


def irreducible(p, r):
    """Monic irreducible polynomial of degree r over F_p (ascending coeffs), via sympy."""
    x = sympy.symbols('x')
    import itertools
    for tail in itertools.product(range(p), repeat=r):
        coeffs = list(tail) + [1]
        P = sympy.Poly(list(reversed(coeffs)), x, modulus=p)
        if P.is_irreducible:
            return coeffs
    raise ValueError


def count_points(fcoef, p, r):
    """#C(F_{p^r}) for y^2 = f(x), deg f odd (one point at infinity)."""
    if r == 1:
        m = [0, 1]  # dummy: work in F_p directly
        elems = [[a] if a else [] for a in range(p)]
        q = p
    else:
        m = irreducible(p, r)
        q = p ** r
        import itertools
        elems = []
        for t in itertools.product(range(p), repeat=r):
            e = list(t)
            while e and e[-1] == 0:
                e.pop()
            elems.append(e)
    half = (q - 1) // 2
    N = 1
    for xe in elems:
        val = []
        for c in reversed(fcoef):          # Horner: val = val*x + c
            val = pmul(val, xe, m, p) if val else []
            if c % p:
                val = list(val) if val else [0]
                val[0] = (val[0] + c) % p
                val = polymod(val, m, p)
        if not val:
            N += 1
        else:
            chi = ppow(val, half, m, p)
            N += 2 if chi == [1] else 0
    return N


def P_from_counts(Ns, q, g):
    s = [2 * g] + [q ** k + 1 - Ns[k - 1] for k in range(1, g + 1)]
    # Newton: e_k from s_1..s_k ; P(T) = sum (-1)^k e_k T^k
    e = [1]
    for k in range(1, g + 1):
        acc = 0
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * s[i]
        assert acc % k == 0
        e.append(acc // k)
    P = [(-1) ** k * e[k] for k in range(g + 1)]
    # functional equation: p_{2g-k} = q^{g-k} p_k
    full = P + [q ** (g - k) * P[k] for k in range(g - 1, -1, -1)]
    return full


def main():
    curves = [
        dict(name='E: y^2=x^3+x+1 / F_5', f=[1, 1, 0, 1], p=5, g=1, rmax=4),
        dict(name='E: y^2=x^3+2x+3 / F_7', f=[3, 2, 0, 1], p=7, g=1, rmax=4),
        dict(name='NEGATIVE CONTROL (singular mod 3) y^2=x^5+x+1 / F_3', f=[1, 1, 0, 0, 0, 1], p=3, g=2, rmax=5),
        dict(name='C2: y^2=x^5-x+1 / F_3', f=[1, -1, 0, 0, 0, 1], p=3, g=2, rmax=5),
        dict(name='C2: y^2=x^5+2x^2+1 / F_5', f=[1, 0, 2, 0, 0, 1], p=5, g=2, rmax=4),
        dict(name='C3: y^2=x^7+x+2 / F_3', f=[2, 1, 0, 0, 0, 0, 0, 1], p=3, g=3, rmax=5),
    ]
    out = []
    t0 = time.time()
    for c in curves:
        p, g = c['p'], c['g']
        # smoothness: f squarefree mod p (deg f = 2g+1 odd => smooth at infinity)
        x = sympy.symbols('x')
        F = sympy.Poly(list(reversed(c['f'])), x, modulus=p)
        sqf = sympy.gcd(F, F.diff(x)).degree() == 0
        Ns = [count_points(c['f'], p, r) for r in range(1, c['rmax'] + 1)]
        P = P_from_counts(Ns, p, g)
        s = power_sums(P, c['rmax'])
        pred = [p ** k + 1 - s[k] for k in range(1, c['rmax'] + 1)]
        R = flint.fmpz_poly(list(reversed(P)))
        rh_balls = [abs(z) for z, m in R.complex_roots() for _ in range(m)]
        mod_ok = all((z - flint.arb(p).sqrt()).contains(0) for z in rh_balls)
        hcoef = h_from_P(P, p)
        rh = rh_exact(hcoef, p)
        pos = positivity_all_degrees(P, p, g)
        Nw, val = toeplitz_negative_witness(P, p, g, Nmax=40)
        rec = dict(name=c['name'], smooth=sqf, N_bruteforce=Ns, P_asc=P, N_predicted=pred,
                   prediction_matches=(pred == Ns), h_asc=hcoef,
                   rh_exact=rh, arb_moduli_contain_sqrtq=mod_ok, positivity=pos['status'],
                   toeplitz_negative_witness_N_le_40=Nw)
        print(rec, flush=True)
        out.append(rec)
    meta = dict(script='ff_curves_check.py', python=platform.python_version(), flint=flint.__version__,
                sympy=sympy.__version__, numpy=np.__version__, runtime_s=round(time.time() - t0, 1))
    fn = os.path.join(OUT, 'curves_check.json')
    with open(fn, 'w') as f:
        json.dump(dict(meta=meta, curves=out), f, indent=1, default=str)
    print('wrote', fn, hashlib.sha256(open(fn, 'rb').read()).hexdigest())


if __name__ == '__main__':
    main()
