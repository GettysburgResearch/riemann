"""tables.py -- turn lab_core outputs into M2/Diag tables (exact integers in, ratios out).
Usage: python3 tables.py core_output.txt [more ...]  -> prints markdown tables and writes JSON next to stdout.
Ratio R(d;m) = sum_{deg u <= m} |A_u(d)|^2 / sum_{deg u <= m} #{n sqfree deg d, (n,u)=1}  (exact quotient of integers,
printed to 4 decimals). rho = m/d.  Also max_u |A_u(d)|^2 / q^d over rows of exact degree m.
"""
import sys, json
from fractions import Fraction
out = {}
for path in sys.argv[1:]:
    q = None; rows = {}
    for line in open(path):
        if line.startswith('#'):
            q = int(line.split()[1].split('=')[1]); continue
        t = line.split()
        d, k = int(t[0]), int(t[1])
        rows[(d, k)] = (int(t[2]), int(t[3]), int(t[4]), float(t[5]))
    dmax = max(d for d, _ in rows); mmax = max(k for _, k in rows)
    tab = {}
    print(f'\n## q = {q}: R(d; m) = M2/Diag (cumulative rows deg u <= m); in brackets rows of exact degree m')
    print('| d | ' + ' | '.join(f'm={m}' for m in range(2, mmax + 1)) + ' |')
    print('|---|' + '---|' * (mmax - 1))
    for d in range(2, dmax + 1):
        cells = []
        for m in range(2, mmax + 1):
            M = sum(rows[(d, k)][1] for k in range(m + 1)); Dg = sum(rows[(d, k)][2] for k in range(m + 1))
            Mk, Dk = rows[(d, m)][1], rows[(d, m)][2]
            R = M / Dg; Rk = Mk / Dk
            mx = rows[(d, m)][3] / q ** d
            tab[f'{d},{m}'] = dict(M2=str(M), Diag=str(Dg), ratio=R, ratio_exact_deg=Rk, max_over_qd=mx, rho=m / d)
            cells.append(f'{R:.3f} [{Rk:.3f}]')
        print(f'| {d} | ' + ' | '.join(cells) + ' |')
    print(f'\nmax_u |A_u(d)|^2 / q^d over rows of exact degree m (q={q}):')
    print('| d | ' + ' | '.join(f'm={m}' for m in range(2, mmax + 1)) + ' |')
    print('|---|' + '---|' * (mmax - 1))
    for d in range(2, dmax + 1, 2):
        print(f'| {d} | ' + ' | '.join(f"{tab[f'{d},{m}']['max_over_qd']:.3g}" for m in range(2, mmax + 1)) + ' |')
    out[str(q) + '_m' + str(mmax)] = tab
json.dump(out, open('/dev/stdout' if len(sys.argv) < 2 else sys.argv[1] + '.json', 'w'), indent=0)
