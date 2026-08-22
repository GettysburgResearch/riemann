"""Exact-coefficient re-audit of flagged random trials + full exact random search.

Coordinates (floats) are promoted to exact Fractions; F and F' coefficients are
computed exactly; roots via mpmath.polyroots at high precision from the exact
coefficients. Parity check per gap: #real zeros of F' in a gap must be ODD
(F'/F: +inf -> -inf). Classification margin is recorded; ambiguous trials flagged.
"""
import numpy as np, mpmath as mp
from fractions import Fraction

mp.mp.dps = 60

def exact_poly(reals, pairs):
    c = [Fraction(1)]
    def mul(c, q):
        out = [Fraction(0)]*(len(c)+len(q)-1)
        for i, a in enumerate(c):
            for j, b in enumerate(q):
                out[i+j] += a*b
        return out
    for r in reals:
        c = mul(c, [Fraction(1), -Fraction(r)])
    for (x, y, m) in pairs:
        fx, fy = Fraction(x), Fraction(y)
        for _ in range(m):
            c = mul(c, [Fraction(1), -2*fx, fx*fx + fy*fy])
    return c

def deriv(c):
    n = len(c)-1
    return [c[i]*(n-i) for i in range(n)]

def roots_classified(c_exact, im_tol=mp.mpf('1e-30')):
    cs = [mp.mpf(f.numerator)/mp.mpf(f.denominator) for f in c_exact]
    rts = mp.polyroots(cs, maxsteps=500, extraprec=200)
    reals, pairs, min_im_gap = [], [], mp.inf
    for z in rts:
        aiy = abs(mp.im(z))
        if aiy < im_tol:
            reals.append(mp.re(z))
        else:
            min_im_gap = min(min_im_gap, aiy)
            if mp.im(z) > 0:
                pairs.append((mp.re(z), mp.im(z)))
    reals.sort()
    return reals, pairs, min_im_gap

def audit(reals, pairs, aw, bw, Aprime=4.0, label=""):
    """Full exact audit of one descent step. Returns dict; raises on parity anomaly."""
    F = exact_poly(reals, pairs)
    d1 = deriv(F)
    r1, p1, mig = roots_classified(d1)
    zs_all = sorted(reals)
    zs = []
    for r in zs_all:               # distinct real zeros for the gap structure
        if not zs or abs(r - zs[-1]) > 1e-12:
            zs.append(r)
    # window counts (rung 0 exact by construction; rung 1 from classified roots)
    Nr0 = sum(1 for r in zs_all if aw < r <= bw)
    Nc0 = sum(2*m for (x, y, m) in pairs if aw < x <= bw)
    Nr1 = sum(1 for r in r1 if aw < float(r) <= bw)
    Nc1 = sum(2 for (x, y) in p1 if aw < float(x) <= bw)
    N0, N1 = Nr0 + Nc0, Nr1 + Nc1
    # gaps
    gaps = [(zs[i], zs[i+1]) for i in range(len(zs)-1)
            if zs[i+1] > aw and zs[i] <= bw]
    W = 0.0; X = 0; ok = dict(rolle=True, parity=True, threshold=True, dipole=True)
    max_ratio = 0.0; rows = []
    for (a, b) in gaps:
        g = b - a
        n1 = sum(1 for r in r1 if a < float(r) < b)
        w = 0.0; nov = 0
        for (x, y, m) in pairs:
            if x - y < b and x + y > a:
                w += m*min(1.0, g*g/(4*y*y)); nov += 1
        extra = n1 - 1
        W += w; X += max(extra, 0)
        if n1 < 1: ok['rolle'] = False
        if n1 % 2 == 0: ok['parity'] = False
        if extra >= 1 and w < 1 - 1e-9: ok['threshold'] = False
        if extra > Aprime*w + 1e-9: ok['dipole'] = False
        if w > 0 and extra > 0: max_ratio = max(max_ratio, extra/w)
        if extra != 0 or w > 0:
            rows.append((round(a,4), round(b,4), n1, extra, round(w,4), nov))
    convR = Nr1 <= Nr0 + 1 + Aprime*W + 1e-9
    desc = (Nc0 - Nc1) <= (N0 - N1) + 1 + Aprime*W + 1e-9
    res = dict(label=label, N0=N0, Nr0=Nr0, Nc0=Nc0, N1=N1, Nr1=Nr1, Nc1=Nc1,
               W=round(W,4), X=X, ok=ok, convRolle=bool(convR), descent=bool(desc),
               max_ratio=round(max_ratio,4), min_im=float(mig) if mig != mp.inf else None,
               rows=rows)
    return res

def gen_trial_stream(seed, n):
    rng = np.random.default_rng(seed)
    for trial in range(n):
        nreal = rng.integers(6, 11)
        reals = np.sort(rng.uniform(0, 10, nreal))
        for i in range(1, len(reals)):
            reals[i] = max(reals[i], reals[i-1] + 0.05)
        reals = [-1.0] + list(map(float, reals)) + [float(reals[-1]) + 1.0]
        npair = rng.integers(1, 4)
        pairs = [(float(rng.uniform(reals[1], reals[-2])),
                  float(rng.uniform(0.05, 0.5)), 1) for _ in range(npair)]
        yield trial, reals, pairs

if __name__ == "__main__":
    # 1) re-audit the four flagged trials exactly
    flagged = {146, 173, 186, 351}
    for trial, reals, pairs in gen_trial_stream(7, 400):
        if trial in flagged:
            res = audit(reals, pairs, reals[1]+0.01, reals[-2]-0.01, label=f"trial{trial}")
            print(res['label'], "ok=", res['ok'], "convRolle=", res['convRolle'],
                  "descent=", res['descent'], "W=", res['W'], "X=", res['X'],
                  "max_ratio=", res['max_ratio'], "min|Im|=", res['min_im'])
            for row in res['rows']: print("   gap", row)
    # 2) full exact random search, fresh seed, 250 trials
    print("="*70)
    nbad = 0; worst = 0.0; nambig = 0
    for trial, reals, pairs in gen_trial_stream(123, 250):
        res = audit(reals, pairs, reals[1]+0.01, reals[-2]-0.01, label=f"s123t{trial}")
        if res['min_im'] is not None and res['min_im'] < 1e-12: nambig += 1
        worst = max(worst, res['max_ratio'])
        bad = [k for k, v in res['ok'].items() if not v] + \
              ([] if res['convRolle'] else ['convRolle']) + \
              ([] if res['descent'] else ['descent'])
        if bad:
            nbad += 1
            print("VIOLATION", res['label'], bad, res)
    print(f"exact search: 250 trials, violations={nbad}, worst extra/weight={worst}, ambiguous-classification trials={nambig}")
