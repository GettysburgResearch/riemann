"""Experiment 2: floor-row cross-row cancellation with finite Dirichlet polynomials of sextic symbols."""
import eis, numpy as np, time, sys, pickle
U = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
t0 = time.time()
x, y, N = eis.primary_elements(U)
keep = ~((x % 64 == 0) & (y % 64 == 0))         # sixth-power-free (2^6 = 64 is the only sixth power <= 1e5 besides 1)
x, y, N = x[keep], y[keep], N[keep]
nu = len(x)
N0max = int(np.sqrt(U)) + 1
prs = eis.primary_primes(N0max, exclude_two=True)   # odd primary primes, N <= sqrt U
lookup = {}
for pr in prs: lookup.setdefault(pr['p'], []).append(pr)
E = np.stack([eis.sextic_vec(pr, x, y) for pr in prs]).astype(np.int8)   # (#primes, nu)
print('u:', nu, 'primes:', len(prs), 'tables', time.time()-t0, flush=True)
# moduli n: primary odd N <= N0max
nx, ny, nN = eis.primary_elements(N0max, coprime_to_2=True)
spf = eis.spf_sieve(N0max)
pidx = {id(pr): i for i, pr in enumerate(prs)}
CH = np.zeros((len(nx), nu), np.complex64)
mu = np.zeros(len(nx)); 
for j in range(len(nx)):
    fac = eis.factor_primary((int(nx[j]), int(ny[j])), int(nN[j]), spf, lookup)
    ex = np.zeros(nu, np.int64); zero = np.zeros(nu, bool)
    for pr, e in fac:
        Ej = E[pidx[id(pr)]].astype(np.int64)
        zero |= (Ej < 0); ex += e * np.where(Ej < 0, 0, Ej)
    CH[j] = np.where(zero, 0, eis.ZETA6 ** (ex % 6))
    mu[j] = 0 if any(e > 1 for _, e in fac) else (-1)**len(fac)
print('moduli:', len(nx), 'symbols done', time.time()-t0, flush=True)
# ray characters on u and on moduli n
xi_u = {'xi9(1,0)': eis.xi9(x, y, 1, 0), 'xi9(0,1)': eis.xi9(x, y, 0, 1), 'xi9(1,1)': eis.xi9(x, y, 1, 1)}
lam = lookup[7][0]
kl = eis.sextic_vec(lam, x, y).astype(np.int64)
xi_u['(u/lam)_6'] = np.where(kl >= 0, eis.ZETA6 ** (kl % 6), 0)
xi_u['none'] = np.ones(nu)
eta_n = {'eta=1': np.ones(len(nx)), 'eta=xi9(1,0)': eis.xi9(nx, ny, 1, 0)}
Ug = np.exp(np.linspace(np.log(1000), np.log(U), 97))
lines = ['## Experiment 2: U up to %d, #u (primary, 6th-power-free) = %d, moduli odd primary N n <= sqrt U (%d of them)' % (U, nu, len(nx)),
         'R(U) = sum_{N u <= U} xi(u) D1(u) D2(u), D1 = sum_{N n <= sqrt U} chi_n(u) N(n)^{-w}, D2 = sum_{N m <= sqrt U} mu(m) eta(m) chi_m(u) N(m)^{-x}, w = x = 1/2 + i t.',
         'T(U) = sum_u |D1 D2| (trivial bound).  Fits on 21 log-spaced U in [1000, %d].' % U,
         '| t | xi | eta | Mobius | slope |R| (97 pts) | slope rms(8 windows) | slope T | rms/U^{1/2} (top window) | rms/U^{2/3} | |R(U)|/T(U) | T(U) |',
         '|---|---|---|---|---|---|---|---|---|---|---|']
res = {}
for t in (0.0,):
    w = 0.5 + 1j*t
    for xname, xi in xi_u.items():
        for ename, eta in eta_n.items():
            for mob in (True, False):
                if not mob and ename != 'eta=1': continue
                if (xname == 'none' and (ename != 'eta=1' or not mob)) or (t != 0.0 and (ename != 'eta=1' or not mob)): continue
                Rs = []; Ts = []
                for Uv in Ug:
                    N0 = int(np.sqrt(Uv)); sn = nN <= N0; su = N <= Uv
                    c1 = (nN[sn] ** (-w)).astype(np.complex64)
                    c2 = ((mu[sn] if mob else 1.0) * eta[sn] * nN[sn] ** (-w)).astype(np.complex64)
                    D1 = c1 @ CH[sn][:, su]; D2 = c2 @ CH[sn][:, su]
                    prod = D1 * D2
                    Rs.append(np.sum(xi[su] * prod)); Ts.append(np.sum(np.abs(prod)))
                Rs = np.array(Rs); Ts = np.array(Ts)
                sl, se = eis.fit_exponent(Ug, np.abs(Rs)); slT, seT = eis.fit_exponent(Ug, Ts)
                nw = 8; w_ = len(Ug)//nw
                Uw = np.array([np.exp(np.mean(np.log(Ug[i*w_:(i+1)*w_]))) for i in range(nw)])
                Rw = np.array([np.sqrt(np.mean(np.abs(Rs[i*w_:(i+1)*w_])**2)) for i in range(nw)])
                slw, sew = eis.fit_exponent(Uw, Rw)
                # ratio tests: mean of |R|/U^a over grid for a = 1/2, 2/3 (constancy check via slope of log(|R|/U^a))
                res[(t, xname, ename, mob)] = dict(Ug=Ug, R=Rs, T=Ts, slope=sl, se=se)
                lines.append('| %.0f | %s | %s | %s | %.3f +- %.3f | %.3f +- %.3f | %.3f +- %.3f | %.3f | %.3f | %.4f | %.1f |' % (t, xname, ename, 'mu' if mob else 'plain', sl, se, slw, sew, slT, seT, Rw[-1]/np.sqrt(Uw[-1]), Rw[-1]/Uw[-1]**(2/3), abs(Rs[-1])/Ts[-1], Ts[-1]))
                print(lines[-1], time.time()-t0, flush=True)
# detail trace for the main case
r = res[(0.0, 'xi9(1,0)', 'eta=1', True)]
lines.append(''); lines.append('Trace (t=0, xi9(1,0), eta=1, Mobius): U, |R(U)|, |R|/U^{1/2}, T(U)/U:')
for k in range(0, len(Ug), 8):
    lines.append('  U=%8.0f  |R|=%8.2f  |R|/sqrtU=%.3f  T/U=%.3f' % (Ug[k], abs(r['R'][k]), abs(r['R'][k])/np.sqrt(Ug[k]), r['T'][k]/Ug[k]))
r = res[(0.0, 'none', 'eta=1', True)]
lines.append('Trace (t=0, xi=none, eta=1, Mobius): U, Re R(U), |R|/U:')
for k in range(0, len(Ug), 8):
    lines.append('  U=%8.0f  Re R=%9.2f  |R|/U=%.4f' % (Ug[k], r['R'][k].real, abs(r['R'][k])/Ug[k]))
open('/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/exp/exp2c_out.md', 'w').write('\n'.join(lines))
pickle.dump(res, open('/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/exp/exp2c.pkl', 'wb'))
print('\n'.join(lines)); print('total', time.time()-t0)
