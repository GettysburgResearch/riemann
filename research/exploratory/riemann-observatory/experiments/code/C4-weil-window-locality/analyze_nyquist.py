"""Nyquist-regime analysis of detect_*.json: fit L*(delta) = a + b ln(1/delta) over delta <= 0.2 and
locate the local-floor collapse L_c(T) (first grid L with lam0 < 1e-3 * lam0 at L_N, and its log-slope)."""
import sys, json, math
import numpy as np
rows = []
for path in sys.argv[1:]:
    d = json.load(open(path))
    for r in d['results']:
        LN = r['rows'][0]['L_nyquist']
        xs = [(x['delta'], x['L_star']) for x in r['rows'] if x['delta'] <= 0.2 and x['L_star'] is not None]
        if len(xs) >= 3:
            X = np.array([math.log(1 / a) for a, _ in xs]); Y = np.array([b for _, b in xs])
            b, a = np.polyfit(X, Y, 1)
        else:
            a = b = float('nan')
        fl = r['floor']
        Ls = np.array([f[0] for f in fl]); l0 = np.array([f[2] for f in fl])
        iN = int(np.argmin(abs(Ls - LN)))
        ref = abs(l0[iN])
        Lc = next((L for L, l in zip(Ls, l0) if L > LN - 0.3 and l < 1e-3 * ref), None)
        # log-slope of lam0 just after collapse (two grid points with lam0 > 1e-9)
        sl = float('nan')
        if Lc is not None:
            i = int(np.where(Ls == Lc)[0][0])
            j = i + 1
            if j < len(Ls) and l0[j] > 1e-9 and l0[i] > 1e-9:
                sl = (math.log(l0[i]) - math.log(l0[j])) / (Ls[j] - Ls[i])
        rows.append((r['T0'], LN, a, b, Lc, sl, a + b * math.log(1 / 0.01) - LN))
print('%10s %7s %8s %8s %7s %9s %9s' % ('T0', 'L_N', 'a', 'b', 'L_c', 'dln/dL', 'off(.01)'))
for T0, LN, a, b, Lc, sl, off in rows:
    print('%10.1f %7.4f %8.4f %8.4f %7s %9.2f %9.4f' % (T0, LN, a, b, 'None' if Lc is None else '%.2f' % Lc, sl, off))
