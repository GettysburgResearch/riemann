# A1 verification: constants, arctan pole mass, algebraic identities, model saturation,
# supersession comparisons, pinch line-mass constant. mpmath, dps 30.
import json
from mpmath import mp, mpf, mpc, pi, sqrt, atan, quad, log, exp, cos, sin, gamma as G

mp.dps = 30
out = {}

p = mpf('0.04782893516094')          # |c_B|, L-105072(b)
p2 = p*p
c0p = (4/(3*pi))*p2                  # c_0'
out['p'] = str(p); out['p2'] = str(p2); out['c0p'] = str(c0p)
out['c0p_matches_9.71e-4'] = abs(c0p - mpf('9.7089e-4')) < mpf('1e-8')

# KEY ALGEBRA: (3pi/4) c0' = p^2 exactly
out['key_algebra_(3pi/4)c0p_minus_p2'] = str((3*pi/4)*c0p - p2)   # should be 0 to dps

# Old numbers
old_target = (2/(3*pi))*p2
old_ceiling = (sqrt(2)+1)**2 * p2
out['old_target_over_p2'] = str(old_target/p2)                    # 0.212207
out['old_ceiling_over_p2'] = str(old_ceiling/p2)                  # 5.828427
out['old_gap'] = str(old_ceiling/old_target)                      # 27.4645

# New numbers
out['new_ceiling_C0_over_p2'] = str(mpf(4))
out['new_threshold_over_p2'] = str(mpf(1))
out['new_gap'] = str(mpf(4))
out['threshold_weakening_3pi/2'] = str(3*pi/2)                    # 4.712389
out['gap_vs_old_target_range'] = [str(p2/old_target), str(4*p2/old_target)]  # [4.712,18.85]
out['sqrt_3pi'] = str(sqrt(3*pi))                                 # 3.0700 (eps_1 admissible)
out['old_eps1_beta_slope_sqrt(3pi/2)'] = str(sqrt(3*pi/2))        # 2.1708
out['old_beta_threshold_sqrt(2/(3pi))'] = str(sqrt(2/(3*pi)))     # 0.46066

# Lemma A1.2(i): exact arctan pole window mass, quad vs closed form
def pole_mass(h, r0):
    integ = quad(lambda tau: h/(h*h + tau*tau), [-r0, 0, r0])
    return integ/pi   # h||P||^2 / p^2  (since |P|^2 = p^2/(pi(h^2+tau^2)))
arctan_checks = {}
for h in [mpf('1e-2'), mpf('1e-3'), mpf('1e-4')]:
    for r0 in [mpf('0.15'), mpf('0.5'), mpf('1.0')]:
        closed = (2/pi)*atan(r0/h)
        num = pole_mass(h, r0)
        expans = 1 - (2/pi)*(h/r0)
        arctan_checks[f'h={float(h)},r0={float(r0)}'] = {
            'closed': str(closed), 'quad_err': str(abs(num-closed)),
            'expansion_err': str(abs(closed-expans))}
out['arctan_pole_mass'] = arctan_checks

# Theorem A1.3: roots of f^2 - 2 p f + (3pi/4) eps = 0 are p(1 -+ sqrt(1-eps/c0'))
eps_grid = [c0p*mpf(q) for q in ['0.001','0.1','0.5','0.9','1.0']]
roots_check = {}
for eps in eps_grid:
    disc = p2 - (3*pi/4)*eps
    lo = p - sqrt(disc); hi = p + sqrt(disc)
    lo2 = p*(1 - sqrt(1 - eps/c0p)); hi2 = p*(1 + sqrt(1 - eps/c0p))
    # check they are roots
    q_lo = lo*lo - 2*p*lo + (3*pi/4)*eps
    q_hi = hi*hi - 2*p*hi + (3*pi/4)*eps
    roots_check[f'eps/c0p={float(eps/c0p)}'] = {
        'floor_over_p': str(lo/p), 'ceil_over_p': str(hi/p),
        'form_match': str(max(abs(lo-lo2), abs(hi-hi2))),
        'root_residuals': [str(q_lo), str(q_hi)],
        'C(eps)_over_p2': str((hi/p)**2),
        'a_min_over_p': str(lo/p)}
out['A13_roots'] = roots_check

# Theorem A1.6 model saturation: theta* = -sqrt(1-eps/c0'); A_model = theta^2 c0' = c0'-eps;
# f_model = (1-theta)p = ceiling; sharp-F1 saturation (1-theta)^2(2/pi) vs (1+|theta|)^2(2/pi).
model_check = {}
for eps in eps_grid:
    th = -sqrt(1 - eps/c0p)
    A_model = th*th*c0p
    f_model = (1-th)*p
    Ceps = p*(1 + sqrt(1 - eps/c0p))
    lineside_cost = (1-th)**2 * (2/pi)          # x p^2 log(1/h)
    lineside_budget = (sqrt((mpf(3)/2)*A_model) + sqrt(2/pi)*p)**2 / p2
    model_check[f'eps/c0p={float(eps/c0p)}'] = {
        'A_model_eq_c0p_minus_eps': str(abs(A_model - (c0p-eps))),
        'f_model_eq_C(eps)': str(abs(f_model - Ceps)),
        'sharpF1_saturation_gap': str(abs(lineside_cost - lineside_budget))}
out['A16_model_saturation'] = model_check

# Pinch damped line mass: int_1^inf (2Re[c_B pi^{-1/2} x^{-1/2} e^{i g1 x/3}])^2 e^{-2hx} dx
# = (2 p^2/pi) log(1/h) (1+o(1)) + O(1). Numeric check (numpy trapezoid, oscillatory).
import numpy as np
g1 = 14.134725141734693
pf = float(p)
line_checks = {}
for h in [1e-2, 1e-3]:
    X = 40.0/h
    n = int(min(3e7, X*200))
    x = np.linspace(1.0, X, n)
    fld = 2*np.real(pf*np.pi**-0.5 * x**-0.5 * np.exp(1j*g1*x/3))
    mass = np.trapezoid(fld*fld*np.exp(-2*h*x), x)
    pred_main = (2*pf*pf/np.pi)*np.log(1/(2*h))  # Gamma(0,2h) ~ log(1/2h) - gamma_E
    pred_full = (2*pf*pf/np.pi)*(np.log(1/(2*h)) - 0.5772156649)
    line_checks[f'h={h}'] = {'measured': mass, 'pred_(2p^2/pi)log(1/2h)': pred_main,
                             'pred_minus_gammaE': pred_full,
                             'ratio_meas/pred_full': mass/pred_full}
out['pinch_line_mass'] = line_checks

# Supersession table: constants at beta grid (old formula valid only beta<0.46066)
tab = {}
for b in ['0.081','0.115','0.3','0.46','0.8','0.99']:
    b_ = mpf(b)
    new_c = (1-b_)**2
    old_c = (1 - b_*sqrt(3*pi/2))**2 if b_ < sqrt(2/(3*pi)) else None
    tab[b] = {'new_(1-beta)^2': str(new_c),
              'old_(1-2.171beta)^2': (str(old_c) if old_c is not None else 'INADMISSIBLE')}
out['supersession_table'] = tab

# Measured beta from FAR.md 5.2 ratios (mass/p^2 = ratio since pinch mass = p^2)
out['beta_measured_range'] = [str(sqrt(mpf('0.0065'))), str(sqrt(mpf('0.0133')))]

with open('/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/final/A1/a1_verify_out.json','w') as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1)[:4000])
print('...OK')
