import numpy as np, json, math, sys
NP = 10**7
out = {}

# ---- sieves: mu, eta (zeta^{1/2} coeffs), g (zeta^{-1/2} coeffs) to NP ----
sieve = np.ones(NP+1, dtype=bool); sieve[:2] = False
for p in range(2, int(NP**0.5)+1):
    if sieve[p]: sieve[p*p::p] = False
primes = np.nonzero(sieve)[0]

K = 25
eta_k = np.ones(K); g_k = np.ones(K)
for k in range(1, K):
    eta_k[k] = eta_k[k-1]*(2*k-1)/(2*k)      # eta(p^k)
    g_k[k]   = g_k[k-1]*(k-1.5)/k            # g(p^k) = [z^k](1-z)^{1/2}
eta = np.ones(NP+1); g = np.ones(NP+1); mu = np.ones(NP+1, dtype=np.int8)
eta[0]=g[0]=0; mu[0]=0
for p in primes:
    pl = int(p)
    eta[pl::pl] *= eta_k[1]; g[pl::pl] *= g_k[1]; mu[pl::pl] *= -1
    pk = pl*pl; k = 2
    while pk <= NP:
        eta[pk::pk] *= eta_k[k]/eta_k[k-1]
        g[pk::pk]   *= g_k[k]/g_k[k-1] if g_k[k-1]!=0 else 0.0
        if k == 2: mu[pk::pk] = 0
        pk *= pl; k += 1

# validation: g = mu * eta by direct convolution to 300
ok = True
for n in range(1, 301):
    s = sum(mu[d]*eta[n//d] for d in range(1, n+1) if n % d == 0)
    if abs(s - g[n]) > 1e-12: ok = False; break
out['sieve_check_g_eq_mu_conv_eta_n<=300'] = ok

nn = np.arange(NP+1, dtype=np.float64); nn[0] = 1
# m(u) = sum_{n<=u} mu(n)/n ; Q(T) = sum_{n<=T} m(n)^2 (~ int_1^T u m^2 du/u)
m_arr = np.cumsum(mu/nn)          # m_arr[u] = m(u)
Q = np.cumsum(m_arr**2)
Ts = [10**k for k in range(2, 8)]
out['m_samples'] = {str(T): float(m_arr[T]) for T in Ts}
out['sqrtU_m'] = {str(T): float(m_arr[T]*math.sqrt(T)) for T in Ts}
out['logmean_Q_over_logT'] = {str(T): float(Q[T]/math.log(T)) for T in Ts}
# dyadic blocks of int u m^2 du/u ~ sum_{block} m(n)^2
out['dyadic_m2'] = {str(j): float(Q[min(2**(j+1),NP)]-Q[2**j]) for j in range(7, 23)}

# M_{1/2}(x) vs Selberg-Delange -x/(2 sqrt(pi) log^{3/2} x)
Mg = np.cumsum(g)
out['M_half'] = {}
for T in Ts:
    pred = -T/(2*math.sqrt(math.pi)*math.log(T)**1.5)
    out['M_half'][str(T)] = {'meas': float(Mg[T]), 'pred': pred,
                             'ratio': float(Mg[T]/pred)}

# Sigma_N^{(g)}(gamma) partial sums vs prediction -N^{1/2-ig}/(sqrt(pi)(1-2ig)log^{3/2}N)
gammas = [1.0, 1.5, 2.0]
samples = [10**4, 10**5, 10**6, 3*10**6, 10**7]
ns = np.arange(1, NP+1, dtype=np.float64)
logn = np.log(ns)
base = g[1:] / np.sqrt(ns)
out['Sigma_g'] = {}
for ga in gammas:
    z = base * np.exp(-1j*ga*logn)
    cs = np.cumsum(z)
    res = {}
    for N in samples:
        S = cs[N-1]
        pred = -N**(0.5-1j*ga)/(math.sqrt(math.pi)*(1-2j*ga)*math.log(N)**1.5)
        res[str(N)] = {'absS': float(abs(S)), 'abspred': float(abs(pred)),
                       'ratio_re': float((S/pred).real), 'ratio_im': float((S/pred).imag)}
    out['Sigma_g'][str(ga)] = res
    del z, cs

# h_U partial sums, coupled U = floor(sqrt(N)), N in {1e5,1e6,1e7}
def h_arr(N, U):
    h = g[:N+1].copy()
    for d in range(1, U+1):
        if mu[d]:
            L = N//d
            h[d::d] -= float(mu[d])*eta[1:L+1]
    return h
out['Sigma_h'] = {}
for N in [10**5, 10**6, 10**7]:
    U = int(math.isqrt(N))
    h = h_arr(N, U)
    nsN = np.arange(1, N+1, dtype=np.float64)
    baseh = h[1:]/np.sqrt(nsN)
    lg = np.log(nsN)
    mU = float(m_arr[U])
    row = {'U': U, 'm(U)': mU, 'sqrtU_mU': mU*math.sqrt(U)}
    for ga in gammas:
        S = np.sum(baseh*np.exp(-1j*ga*lg))
        pred = -2*mU*N**(0.5-1j*ga)/((1-2j*ga)*math.sqrt(math.pi*math.log(N)))
        row[str(ga)] = {'absS': float(abs(S)), 'abspred': float(abs(pred)),
                        'ratio_re': float((S/pred).real), 'ratio_im': float((S/pred).imag)}
    out['Sigma_h'][str(N)] = row
    del h, baseh, lg

# I_w = int w(gamma)/(1+4 gamma^2) dgamma, w = |hatA_-(i gamma)|^2 ; and min w on [1,2]
def w_of(gam):
    s = 1j*gam
    v = (1-np.exp(-s*math.log(2)))*(1-math.sqrt(2)*np.exp(-s*math.log(2)))/s
    return np.abs(v)**2
gg = np.arange(0.0005, 400, 0.001)
Iw = 2*np.trapezoid(w_of(gg)/(1+4*gg**2), gg)   # even integrand
out['I_w'] = float(Iw)
g12 = np.arange(1, 2, 0.0001)
out['w_min_[1,2]'] = float(np.min(w_of(g12)))

# branch-mass prediction vs measured H rows
rows = json.load(open('/home/user/riemann/experiments/X-105053-assault/results.json'))['rows']
out['branch_vs_H'] = []
for r in rows:
    U, N = r['U'], r['N']
    mU = float(m_arr[U])
    pred = (2/math.pi**2)*Iw*mU*mU*N/math.log(N)
    out['branch_vs_H'].append({'X': r['X'], 'U': U, 'N': N, 'm(U)': mU,
        'H_meas': r['H_sweep'], 'H_branch_pred': pred,
        'ratio': r['H_sweep']/pred if pred != 0 else None})

json.dump(out, open('/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/progA2/laneP/num_results.json','w'), indent=1)
print('written')
