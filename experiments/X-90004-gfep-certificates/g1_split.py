"""PRONG G1: decompose binding cut value Sigma(p*) = S(p*) [window self-source]
+ far inflow [Moebius tail transported]; which side carries the fluctuation?
Also: total window flux identity check (H2 tie)."""
import sys, math
import numpy as np
sys.path.insert(0, "/home/user/riemann/experiments/X-90002-stress-test-artifacts")
sys.path.insert(0, "/home/user/riemann/experiments/X-90004-gfep-certificates")
from gfep import mobius_sieve, critical_r
from smallX_band2 import full_G
from g1_scan import sigma_from_G

X = 10**4
mu = mobius_sieve(X); r = critical_r(X, mu); G = full_G(X, r)
S = np.zeros(X + 2); mm = np.arange(2, X + 1); S[2:X + 1] = mm * r[2:X + 1]

print(f"{'n':>5} {'p*':>5} {'fam':>12} {'sqrt(n)Sig':>10} {'self=sqrt(n)S(p*)':>17} "
      f"{'inflow':>9} {'self/Sig':>8}")
selfs, infl, sigs = [], [], []
for n in range(8, X // 10 + 1, 7):
    p, sig = sigma_from_G(X, n, r, G)
    j = int(np.argmin(sig)); ps = int(p[j])
    fam = "bottom" if ps == n else ("top" if ps == 2 * n - 1 else
          ("int_odd" if ps % 2 else "int_even"))
    sq = math.sqrt(n)
    a = sig[j] * sq; b = S[ps] * sq; c = a - b
    selfs.append(b); infl.append(c); sigs.append(a)
    if n % 49 < 7:
        print(f"{n:>5} {ps:>5} {fam:>12} {a:>10.4f} {b:>17.4f} {c:>9.4f} {b/a:>8.3f}")
selfs = np.array(selfs); infl = np.array(infl); sigs = np.array(sigs)
print(f"\nfluctuation split (std over n-scan, X={X}):")
print(f"  std sqrt(n)Sigma(p*) = {np.std(sigs):.4f}")
print(f"  std self-source part = {np.std(selfs):.4f}   std inflow part = {np.std(infl):.4f}")
print(f"  corr(Sigma, self) = {np.corrcoef(sigs, selfs)[0,1]:.3f}   "
      f"corr(Sigma, inflow) = {np.corrcoef(sigs, infl)[0,1]:.3f}")

# interior-even exception audit
n = 106
p, sig = sigma_from_G(X, n, r, G)
j = int(np.argmin(sig))
print(f"\n[exception audit] X={X} n=106: p*={int(p[j])} theta={p[j]/n:.4f} "
      f"sqrt(n)Sig={sig[j]*math.sqrt(n):.4f}; runner-ups:")
order = np.argsort(sig)[:5]
for k in order:
    print(f"    p={int(p[k])} ({'odd' if p[k]%2 else 'even'}) sqrt(n)Sig={sig[k]*math.sqrt(n):.4f}")

# total-flux vs tail-sum identity: sum_p Sigma(p) = sum_{m>=n} S(m) - leak - stopped-below
for n in (50, 100, 300, 700):
    p, sig = sigma_from_G(X, n, r, G)
    tot = float(np.sum(sig))
    tail = float(np.sum(S[n:X + 1]))
    print(f"n={n:>4}: sum_p Sigma={tot:+.5f}  sum_(m>=n) S(m)={tail:+.5f}  "
          f"captured={tot/tail if tail else float('nan'):.3f}")
