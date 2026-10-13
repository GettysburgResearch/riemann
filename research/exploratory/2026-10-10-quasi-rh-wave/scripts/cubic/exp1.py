"""Experiment 1: Patterson bias of cubic Gauss sums gamma_2(c) over primary squarefree c, and twisted sums."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eis, numpy as np, time, pickle
X = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
t0 = time.time()
prs = eis.primary_primes(X)          # primary primes N <= X incl. inert (and -2)
lookup = {}
for pr in prs: lookup.setdefault(pr['p'], []).append(pr)
for pr in prs:
    pr['g2'] = eis.gauss_prime(pr, 2)
    pr['g1'] = eis.gauss_prime(pr, 1) if pr['p'] != 2 else 0.0
    pr.pop('K', None)                  # free memory
print('primes:', len(prs), 'gauss sums done', time.time()-t0, flush=True)

x, y, N = eis.primary_elements(X)
spf = eis.spf_sieve(X)
n = len(x)
gam2 = np.zeros(n, complex); gam1 = np.zeros(n, complex); sqf = np.zeros(n, bool); isprime = np.zeros(n, bool); odd = np.zeros(n, bool)
for i in range(n):
    el = (int(x[i]), int(y[i]))
    fac = eis.factor_primary(el, int(N[i]), spf, lookup)
    if any(e > 1 for _, e in fac): continue
    sqf[i] = True; isprime[i] = (len(fac) == 1)
    odd[i] = all(pr['p'] != 2 for pr, _ in fac)
    g2 = 1.0; g1 = 1.0
    for a in range(len(fac)):
        g2 *= fac[a][0]['g2']; g1 *= fac[a][0]['g1']
        for b in range(a+1, len(fac)):
            pa, pb = fac[a][0], fac[b][0]
            g2 *= eis.symbol_val(pb['el'], pa, 2) * eis.symbol_val(pa['el'], pb, 2)
            if odd[i]:
                g1 *= eis.symbol_val(pb['el'], pa, 1) * eis.symbol_val(pa['el'], pb, 1)
    gam2[i] = g2; gam1[i] = g1 if odd[i] else 0.0
print('elements:', n, 'squarefree:', sqf.sum(), 'primes:', isprime.sum(), 'factored', time.time()-t0, flush=True)

# twist characters
lam = lookup[7][0]; print('lambda =', lam['el'])
k_lam = np.array([eis.sextic_scalar((int(x[i]), int(y[i])), lam) for i in range(n)])
def lam_char(order):
    j = 6 // order
    return np.where(k_lam >= 0, eis.ZETA6 ** ((j * k_lam) % 6), 0.0)
twists = {
    'none': np.ones(n, complex),
    'xi9(1,0)': eis.xi9(x, y, 1, 0), 'xi9(0,1)': eis.xi9(x, y, 0, 1), 'xi9(1,1)': eis.xi9(x, y, 1, 1), 'xi9(1,2)': eis.xi9(x, y, 1, 2),
    '(c/lam)_6': lam_char(6), '(c/lam)_3 [=(lam/c)_3, cubic]': lam_char(3), 'conj (c/lam)_3': np.conj(lam_char(3)), '(c/lam)_2': lam_char(2),
    'alpha(c)^6 [inf order]': ((x + y*eis.OMEGA)/np.sqrt(N))**6,
}
Xg = np.exp(np.linspace(np.log(2000), np.log(X), 25))
res = {}
lines = []
lines.append('## Experiment 1: X = %d, #primary c = %d, #squarefree = %d, #prime = %d' % (X, n, sqf.sum(), isprime.sum()))
lines.append('Fits of log|S(X)| vs log X on 25 log-spaced points in [2000, %d]; "rms" = rms of |S(x)| over x in (X/2, X].' % X)
lines.append('| series | twist | slope(|S|) +- se | slope(rms) +- se | |S(X)|/X^{5/6} | |S(X)|/X^{1/2} |')
lines.append('|---|---|---|---|---|---|')
for series, (coef, mask) in {'gamma_2 squarefree': (gam2, sqf), 'gamma_2 primes only': (gam2, isprime), 'gamma_1 (sextic) squarefree odd': (gam1, sqf & odd)}.items():
    for tname, tw in twists.items():
        if series.startswith('gamma_1') and 'lam' in tname: continue
        a = np.where(mask, coef * tw, 0)
        S = np.cumsum(a)
        idx = np.searchsorted(N, Xg, side='right') - 1
        SX = np.abs(S[idx])
        rms = np.array([eis.rms_window(N, S, Xv) for Xv in Xg])
        sl, se = eis.fit_exponent(Xg, SX + 1e-12)
        sl2, se2 = eis.fit_exponent(Xg, rms)
        res[(series, tname)] = dict(Xg=Xg, SX=SX, rms=rms, slope=sl, se=se, slope_rms=sl2, se_rms=se2)
        lines.append('| %s | %s | %.3f +- %.3f | %.3f +- %.3f | %.3f | %.3f |' % (series, tname, sl, se, sl2, se2, SX[-1]/X**(5/6), SX[-1]/X**0.5))
        if series == 'gamma_2 squarefree' or (series == 'gamma_2 primes only' and tname == 'none'):
            print(series, tname, 'S(X)=', np.round(S[idx[-1]], 3), 'slope', round(sl,3), '+-', round(se,3), 'rms slope', round(sl2,3), flush=True)
# Also exponent of the squarefree Patterson sum in sub-ranges and sign of the real part
S = np.cumsum(np.where(sqf, gam2, 0))
idx = np.searchsorted(N, Xg, side='right') - 1
lines.append('')
lines.append('Patterson sum S(X) = sum_{Nc<=X, c sqfree primary} gamma_2(c) at grid points (X, Re S, Im S, |S|/X^{5/6}):')
for k in range(0, len(Xg), 3):
    lines.append('  X=%8.0f  Re=%9.2f  Im=%9.2f  |S|/X^{5/6}=%.4f' % (Xg[k], S[idx[k]].real, S[idx[k]].imag, abs(S[idx[k]])/Xg[k]**(5/6)))
# local slope on [X/10, X]
for lo in (2000, 10000):
    m = Xg >= lo
    sl, se = eis.fit_exponent(Xg[m], np.abs(S[idx[m]]))
    lines.append('  slope on [%d, %d]: %.3f +- %.3f' % (lo, X, sl, se))
# Comparison: count of terms, trivial bound
lines.append('trivial bound sum |gamma_2| = #squarefree = %d = %.3f X; Dunn-Radziwill constant for primes: (2pi)^{2/3}/(5 Gamma(2/3)) = %.4f' % (sqf.sum(), sqf.sum()/X, (2*np.pi)**(2/3)/(5*1.3541179394264)))
Sp = np.cumsum(np.where(isprime, gam2, 0))
lines.append('primes: S_p(X)*log X / X^{5/6} at X = %d: %.4f (Re %.4f, Im %.4f)' % (X, abs(Sp[-1])*np.log(X)/X**(5/6), Sp[-1].real*np.log(X)/X**(5/6), Sp[-1].imag*np.log(X)/X**(5/6)))
open('/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/exp/exp1_out.md', 'w').write('\n'.join(lines))
pickle.dump(dict(x=x, y=y, N=N, gam2=gam2, gam1=gam1, sqf=sqf, isprime=isprime, res=res), open('/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/exp/exp1.pkl', 'wb'))
print('\n'.join(lines)); print('total time', time.time()-t0)
