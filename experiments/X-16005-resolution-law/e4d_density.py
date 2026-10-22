"""E4d -- the density threshold.  E4b showed total failure for comb spacing S<1
(= the node spacing).  Is it a DENSITY effect or an EXTENT effect (source
reaching far beyond the budget reach)?  And does the critical S depend on N?"""
import mpmath as mp
from mpmath import mpf
import core

OFF = mpf('0.037')      # keeps comb elements off the integer nodes

def run(N, S, K):
    S = mpf(S)
    for tries in range(6):
        ps = [S/2 + OFF + S*k for k in range(K)]
        try:
            info = core.detect(N, ps, [mpf(1)]*K, extraprec=4000)
            break
        except ValueError:
            S = S * (1 + mpf('1e-4'))
    r = info['pos_roots']
    n6 = n3 = 0
    for k in range(min(N, K)):
        p = ps[k]
        rr = min(r, key=lambda x: abs(x-p))
        e = abs(rr-p)/p
        if e < mpf('1e-6'): n6 += 1
        if e < mpf('1e-3'): n3 += 1
    return n6, n3, r, ps

SS = ['0.6','0.7','0.8','0.9','1.0','1.1','1.2','1.3','1.5','1.8','2.2','3.0']
print("E4d-1  critical comb spacing vs N  (K chosen so the source extends to ~6N)")
print("       entries are  (#poles with rel.err<1e-6) / (#with rel.err<1e-3)")
print(f"{'N':>4} {'budget':>7} " + " ".join(f"S={s:>5}" for s in SS))
for N in (6, 10, 14):
    row = f"{N:>4} {N/2:>7} "
    for s in SS:
        K = int(mp.ceil(6*N/mpf(s)))+2
        n6, n3, r, ps = run(N, s, K)
        row += f" {str(n6)+'/'+str(n3):>7}"
    print(row)

print()
print("E4d-2  density vs extent:  N=10, S=0.9, vary K (source extent)")
for K in (11, 12, 15, 20, 30, 40, 69, 120):
    n6, n3, r, ps = run(10, '0.9', K)
    print(f"   K={K:>3} (source up to {mp.nstr(ps[-1],5):>7}):"
          f"  n(1e-6)={n6}  n(1e-3)={n3}   first roots: {[mp.nstr(x,7) for x in r[:6]]}")
print()
print("   control, same but S=1.85:")
for K in (11, 12, 15, 20, 30, 40, 69):
    n6, n3, r, ps = run(10, '1.85', K)
    print(f"   K={K:>3} (source up to {mp.nstr(ps[-1],5):>7}):  n(1e-6)={n6}  n(1e-3)={n3}"
          f"   first roots: {[mp.nstr(x,7) for x in r[:6]]}")
