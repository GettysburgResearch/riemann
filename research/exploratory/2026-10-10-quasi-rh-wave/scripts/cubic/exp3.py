"""Experiment 3: direct-side Gram term.  A_m = Y^{-3/2} sum_{s primary odd squarefree, Y/2 < N s <= Y} c(s) g(s,-m)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eis, numpy as np, time, pickle
Qmax = int(sys.argv[1]) if len(sys.argv) > 1 else 250000
Ys = [int(v) for v in sys.argv[2].split(',')] if len(sys.argv) > 2 else [500, 1000, 2000]
t0 = time.time()
mx, my, mN = eis.all_elements(Qmax)          # all nonzero m, sorted by norm
nm = len(mx)
print('m count', nm, flush=True)
lines = ['## Experiment 3: Gram term.  m over all nonzero Eisenstein integers N m <= Q; s primary, odd, squarefree, Y/2 < N s <= Y.',
         'S(Q) = sum_{N m <= Q} |A_m|^2, A_m = Y^{-3/2} sum_s c(s) g(s,-m) (g unnormalized sextic Gauss sum, |g| = sqrt N s).',
         'diag(Q) = Y^{-3} sum_s |c(s)|^2 N(s) #{N m <= Q : (m,s)=1}.  P_a = Y^2/Q.  Ratio = S/diag (1 = pure diagonal).']
res = {}
rng = np.random.default_rng(1)
for Y in Ys:
    prs = eis.primary_primes(Y, exclude_two=True)
    lookup = {}
    for pr in prs: lookup.setdefault(pr['p'], []).append(pr)
    for pr in prs: pr['g1'] = eis.gauss_prime(pr, 1)
    sx, sy, sN = eis.primary_elements(Y, coprime_to_2=True)
    sel = sN > Y/2
    sx, sy, sN = sx[sel], sy[sel], sN[sel]
    spf = eis.spf_sieve(Y)
    cache = {}
    def table(pr):
        key = id(pr)
        if key not in cache:
            cache[key] = eis.sextic_vec(pr, mx, my)
        return cache[key]
    # per-s data
    s_list = []
    for i in range(len(sx)):
        el = (int(sx[i]), int(sy[i]))
        fac = eis.factor_primary(el, int(sN[i]), spf, lookup)
        if any(e > 1 for _, e in fac): continue
        g = 1.0
        for a in range(len(fac)):
            g *= fac[a][0]['g1']
            for b in range(a+1, len(fac)):
                pa, pb = fac[a][0], fac[b][0]
                g *= eis.symbol_val(pb['el'], pa, 1) * eis.symbol_val(pa['el'], pb, 1)
        s_list.append(dict(el=el, N=int(sN[i]), fac=[pr for pr, _ in fac], g=g * np.sqrt(sN[i]), nf=len(fac)))
    ns = len(s_list)
    print('Y', Y, '#s', ns, 'primes among s', sum(s['nf']==1 for s in s_list), time.time()-t0, flush=True)
    # coefficient variants
    ray = np.array([eis.ray9(s['el'][0], s['el'][1]) for s in s_list])
    variants = {
        'c=1 (all sqfree s)': np.ones(ns),
        'c=random sign': rng.choice([-1.0, 1.0], ns),
        'c=random phase': np.exp(2j*np.pi*rng.random(ns)),
        'c=1 on primes only': np.array([1.0 if s['nf']==1 else 0.0 for s in s_list]),
        'c=random sign on primes': np.array([1.0 if s['nf']==1 else 0.0 for s in s_list]) * rng.choice([-1.0, 1.0], ns),
        'c=1_{s=1 mod 9} (ray class)': ((ray[:,0]==0)&(ray[:,1]==0)).astype(float),
        'c=1_{s=1 mod 9} * random sign': ((ray[:,0]==0)&(ray[:,1]==0)).astype(float) * rng.choice([-1.0, 1.0], ns),
        'c=xi9(1,0)(s) (nonprincipal ray char)': np.array([eis.xi9(s['el'][0], s['el'][1], 1, 0) for s in s_list]),
        'c=conj g(s)/|g(s)| (Gauss phase removed)': np.array([np.conj(s['g'])/abs(s['g']) for s in s_list]),
    }
    # A_m for each variant: accumulate over s
    A = {k: np.zeros(nm, np.complex128) for k in variants}
    diagw = {k: np.zeros(nm) for k in variants}      # per-m diagonal weight sum_s |c|^2 N(s) 1_{(m,s)=1}
    for s in s_list:
        ex = np.zeros(nm, np.int64); zero = np.zeros(nm, bool)
        for pr in s['fac']:
            T = table(pr).astype(np.int64)
            zero |= (T < 0); ex += np.where(T < 0, 0, T)
        chi_conj = np.where(zero, 0, eis.ZETA6 ** ((-ex) % 6))   # conj chi_s(m)
        term = chi_conj * s['g']
        for k, c in variants.items():
            if c[s_list.index(s)] != 0:
                A[k] += c[s_list.index(s)] * term
                diagw[k] += abs(c[s_list.index(s)])**2 * s['N'] * (~zero)
    print('A_m done', time.time()-t0, flush=True)
    Pas = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 729, 1024, 2048, 4096]
    lines.append(''); lines.append('### Y = %d, #s = %d (%d primes).  Columns: P_a, Q, S/(Q/Y), S/diag' % (Y, ns, sum(s['nf']==1 for s in s_list)))
    hdr = '| variant | ' + ' | '.join('P_a=%d' % P for P in Pas if Y*Y/P <= Qmax) + ' | slope of S/diag vs P_a (P_a>=4) |'
    lines.append(hdr); lines.append('|---|' + '---|'*(hdr.count('|')-2))
    for k in variants:
        A2 = np.abs(A[k])**2 / Y**3
        cum = np.cumsum(A2); cumd = np.cumsum(diagw[k]) / Y**3
        row = []; pv = []; rv = []
        for P in Pas:
            Q = Y*Y/P
            if Q > Qmax: continue
            i = np.searchsorted(mN, Q, side='right') - 1
            S = cum[i]; D = cumd[i]
            row.append('%.3f / %.3f' % (S/(Q/Y), S/D))
            if P >= 4: pv.append(P); rv.append(S/D)
            res[(Y, k, P)] = (S, D, Q)
        sl, se = eis.fit_exponent(np.array(pv, float), np.array(rv)) if len(pv) > 2 else (np.nan, np.nan)
        lines.append('| %s | ' % k + ' | '.join(row) + ' | %.3f +- %.3f |' % (sl, se))
        print(lines[-1], flush=True)
    # shell profile of |A_m|^2 for c=1: mean over dyadic shells of N m
    A2 = np.abs(A['c=1 (all sqfree s)'])**2 / Y**3; A2r = np.abs(A['c=random sign'])**2 / Y**3
    d1 = diagw['c=1 (all sqfree s)'] / Y**3
    A2c = np.abs(A['c=1_{s=1 mod 9} (ray class)'])**2 / Y**3; d1c = diagw['c=1_{s=1 mod 9} (ray class)'] / Y**3
    lines.append('Shell profile: N m in (Q/2, Q], mean |A_m|^2 / mean diag weight  [c=1 ; random sign ; ray class s=1 mod 9]:')
    for Q in [125, 250, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 250000]:
        if Q > Qmax: continue
        lo = np.searchsorted(mN, Q/2, side='right'); hi = np.searchsorted(mN, Q, side='right')
        lines.append('  Q=%7d  P_a=%7.1f  ratio c=1: %.3f   random sign: %.3f   ray class: %.3f   (n=%d)' % (Q, Y*Y/Q, A2[lo:hi].mean()/d1[lo:hi].mean(), A2r[lo:hi].mean()/d1[lo:hi].mean(), A2c[lo:hi].mean()/max(d1c[lo:hi].mean(),1e-30), hi-lo))
    print('\n'.join(lines[-12:]), flush=True)
    cache.clear()
open('/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/exp/exp3_out.md', 'w').write('\n'.join(lines))
pickle.dump(res, open('/tmp/claude-0/-home-user/53c3997b-234a-5832-95c7-2c9489662fb1/scratchpad/exp/exp3.pkl', 'wb'))
print('\n'.join(lines)); print('total', time.time()-t0)
