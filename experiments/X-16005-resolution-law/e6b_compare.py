"""Quantitative comparison: O-16004's arithmetic run vs the pure-pole model."""
import mpmath as mp
from mpmath import mpf
import e6_zeta as E6
mp.mp.dps = 30
G = E6.gammas(90)
obs = {   # O-16004 section 2, cutoff c = 2000
 6:  ['14.1347251','21.0224296','25.0775916','33.0181','44.259'],
 8:  ['14.1347251','21.0220398','25.0111337','30.6382','36.818'],
 10: ['14.1347251','21.0220396','25.0108579','30.4313','33.123'],
}
print("O-16004 arithmetic run (c=2000) vs the synthetic pure-pole model, relative errors vs gamma_k")
print(f"{'N':>3} {'k':>3} {'margin':>7} {'gamma_k':>17} {'arithmetic w_k':>16} {'err(arith)':>12} {'err(model)':>12} {'ratio':>8}")
for N in (6, 8, 10):
    info, rec = E6.run(2000, N, G, 90)   # prints its own block; we reuse rec
    print()
    for k, w in enumerate(obs[N]):
        g = G[k]; w = mpf(w)
        ea = abs(w - g) / g
        rr = min(rec, key=lambda x: abs(x - g))
        em = abs(rr - g) / g
        rat = ea / em if em > 0 else mpf('inf')
        print(f"{N:>3} {k+1:>3} {N-2*(k+1):>7} {mp.nstr(g,14):>17} {mp.nstr(w,11):>16} "
              f"{mp.nstr(ea,4):>12} {mp.nstr(em,4):>12} {mp.nstr(rat,3):>8}")
    print()
