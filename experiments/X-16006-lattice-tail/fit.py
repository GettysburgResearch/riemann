"""Subtlety (3): could L-16005's OWN measurement window (alpha=1, j=4..12) tell
j^-1 from j^-2?  Least-squares fit of log|E_j| against log j, plus the spread of
j|E_j| and j^2|E_j| over that exact window and over wider ones."""
import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, log, nstr
from math import log as flog

d = json.load(open('/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail/full.json'))


def fit(js, absE):
    n = len(js)
    x = [flog(j) for j in js]; y = [flog(v) for v in absE]
    mx = sum(x)/n; my = sum(y)/n
    num = sum((xi-mx)*(yi-my) for xi, yi in zip(x, y))
    den = sum((xi-mx)**2 for xi in x)
    return -num/den


print("### L-16005's EXACT measurement window: alpha=1, j = 4,6,8,10,12")
rows = {r['j']: r for r in d['1.0']['rows']}
W = [4, 6, 8, 10, 12]
jE = [rows[j]['absE']*j for j in W]
j2E = [rows[j]['absE']*j*j for j in W]
print("   |E_j|      :", "  ".join(f"{rows[j]['absE']:.4g}" for j in W))
print("   j *|E_j|   :", "  ".join(f"{v:.4g}" for v in jE),
      f"   max/min = {max(jE)/min(jE):.3f}   spread about mean = "
      f"{100*(max(jE)-min(jE))/(sum(jE)/len(jE)):.0f}%")
print("   j^2*|E_j|  :", "  ".join(f"{v:.4g}" for v in j2E),
      f"   max/min = {max(j2E)/min(j2E):.3f}   spread about mean = "
      f"{100*(max(j2E)-min(j2E))/(sum(j2E)/len(j2E)):.0f}%")
print(f"   least-squares exponent p in |E_j| ~ j^-p over this window: p = "
      f"{fit(W, [rows[j]['absE'] for j in W]):.4f}")
print(f"   (L-16005 quotes exactly these j|E_j| as 0.0084, 0.0060, 0.0046, 0.0037, 0.0031)")
print()
print("### fitted exponent p over several windows / alphas")
print(f"{'alpha':>6} {'window':>14} {'p (LSQ)':>10} {'spread j|E|':>13} {'spread j^2|E|':>15}")
print('-'*64)
for astr in ['1.0', '0.7', '0.5', '0.4']:
    rr = {r['j']: r for r in d[astr]['rows']}
    for w in [(4, 12), (4, 20), (10, 20), (20, 40), (30, 40)]:
        js = [j for j in range(w[0], w[1]+1)]
        aE = [rr[j]['absE'] for j in js]
        p = fit(js, aE)
        s1 = [rr[j]['absE']*j for j in js]; s2 = [rr[j]['absE']*j*j for j in js]
        print(f"{astr:>6} {f'j={w[0]}..{w[1]}':>14} {p:>10.4f} {max(s1)/min(s1):>13.3f} "
              f"{max(s2)/min(s2):>15.3f}")
print()
print("### ratio of measured |E_j| to L-16005's (iv) table values, alpha=1  (reproduction check)")
ref = {1: 7.33e-3, 2: 5.22e-3, 3: 3.32e-3, 4: 2.10e-3, 6: 9.95e-4, 10: 3.67e-4, 12: 2.56e-4}
for j, v in ref.items():
    print(f"   j={j:>2}: L-16005 {v:.3g}   this work {rows[j]['absE']:.6g}   ratio {rows[j]['absE']/v:.5f}")
