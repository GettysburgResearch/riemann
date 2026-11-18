"""Summarise detect_*.json: L* vs Nyquist L_N=(1/2)log(T/2pi) and flat-growth L_flat; prints a table."""
import sys, json, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from detect_lib import kappa_cross
kc = kappa_cross()
for path in sys.argv[1:]:
    d = json.load(open(path))
    print('#', path.split('/')[-1], 'kappa_cross=%.4f' % kc)
    print('%10s %6s %7s %7s %7s %7s %7s %7s %s' % ('T0', 'delta', 'kappa', 'L_N', 'L_flat', 'L_pred', 'L*', 'L*-Lpr', 'regime'))
    for r in d['results']:
        for x in r['rows']:
            LN, Lf, Ls = x['L_nyquist'], x['L_flat'], x['L_star']
            Lp = min(LN, Lf)
            reg = 'growth' if x['kappa'] > kc else 'nyquist'
            print('%10.2f %6.3f %7.3f %7.4f %7.4f %7.4f %7s %7s %s' % (r['T0'], x['delta'], x['kappa'], LN, Lf, Lp,
                  'None' if Ls is None else '%.4f' % Ls, 'None' if Ls is None else '%+.4f' % (Ls - Lp), reg))
