"""C5 ADJUDICATOR: small numerical checks for OB-2(a) and OB-9 (NUMERICAL-NONRIGOROUS bookkeeping on
rigorous zero ordinates; the sum is evaluated in mpmath at 30 digits from the Arb midpoints, radii <= 1e-20).

OB-2(a): S(T) = sum_{|gamma|<T} 1/|rho| (both signs) vs (log T)^2/(2 pi) and (log(T/2pi))^2/(2 pi).
OB-9: what decay law the two quoted data points imply:
   Zhu 2608.24827 (abstract): unconditional variational upper bound lambda_min(2) <= 3.2e-283, empirical law
       -ln lambda_min(L) ~ 2 pi^2 N(T*)/ln N(T*), T* = 2 pi e^{2L}; RH-conditional bound lambda_min(L) <= exp(-L e^L).
   Andrews-Connes-La Gatta 2611.13129 (abstract): eps_lambda(1) ~ 1e-1618 at lambda^2 = 300; Fuchs rate e^{-4 pi lambda^2}.
"""
import sys, json, math, hashlib, time
import mpmath as mp

mp.mp.dps = 30
t0 = time.time()
files = sys.argv[1:3]
gam = []
for f in files:
    with open(f) as fh:
        for line in fh:
            n, mid, rad = line.split()
            gam.append(mp.mpf(mid))
gam.sort()
T = gam[-1] + mp.mpf('0.01')
S = 2 * mp.fsum(1 / mp.sqrt(mp.mpf('0.25') + g * g) for g in gam)
lead = mp.log(T)**2 / (2 * mp.pi)
lead2 = mp.log(T / (2 * mp.pi))**2 / (2 * mp.pi)
res = {'OB2a': {'n_zeros': len(gam), 'T': float(T), 'S_T': float(S), 'logT^2/2pi': float(lead),
                'log(T/2pi)^2/2pi': float(lead2), 'ratio_S_over_lead': float(S / lead), 'S_minus_lead2': float(S - lead2)}}


def N_count(t):
    lo, hi = 0, len(gam)
    while lo < hi:
        mid = (lo + hi) // 2
        if gam[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo


L = 2.0
Tstar = 2 * math.pi * math.exp(2 * L)
NT = N_count(Tstar)
zhu_emp = 2 * math.pi**2 * NT / math.log(NT)
zhu_obs = -math.log(3.2e-283)
lam2 = 300.0
acl_obs = 1618 * math.log(10)
res['OB9'] = {
    'Zhu_L2': {'T_star': Tstar, 'N_T_star': NT, 'empirical_law_-ln_lambda': zhu_emp, 'observed_-ln_upper_bound': zhu_obs,
               'c_in_exp(-c e^{2L})': zhu_obs / math.exp(2 * L), 'misquoted_law_L_e^L': L * math.exp(L),
               'exp(-L e^L)': math.exp(-L * math.exp(L)), 'Fuchs_4pi_e^{2L}': 4 * math.pi * math.exp(2 * L)},
    'ACLG_lambda2_300': {'L=log lambda': 0.5 * math.log(lam2), 'observed_-ln_eps': acl_obs, 'c_in_exp(-c lambda^2)': acl_obs / lam2,
                         'Fuchs_4pi_lambda^2': 4 * math.pi * lam2,
                         'misquoted_L_e^L': 0.5 * math.log(lam2) * math.sqrt(lam2)},
    'digits_needed_per_e^{2L}_if_c=4pi': 4 * math.pi / math.log(10)}
res['meta'] = {'script': 'adj_ob_numbers.py', 'mpmath': mp.__version__, 'runtime_s': round(time.time() - t0, 1),
               'inputs_sha256': [hashlib.sha256(open(f, 'rb').read()).hexdigest() for f in files]}
print(json.dumps(res, indent=1))
path = sys.argv[3]
json.dump(res, open(path, 'w'), indent=1)
print(path, hashlib.sha256(open(path, 'rb').read()).hexdigest())
