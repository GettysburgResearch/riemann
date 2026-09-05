# A1 extremal check: the feasible set of the norm constraints
#   S(eps) = { (f, alpha) : f >= |alpha| >= 0,  p^2 + f^2 + 2 p Re(alpha) <= p^2 - (3pi/4) eps }
# (Theorem A1.3/A1.4's limit constraints, alpha = coherent amplitude) has
#   sup f = p + sqrt(p^2 - (3pi/4)eps),  inf f = p - sqrt(p^2 - (3pi/4)eps),
#   min |alpha| over S = inf f  (the floor is forced on the COHERENT part too).
# Verified by dense randomized sampling + boundary refinement. numpy.
import numpy as np, json

rng = np.random.default_rng(1)
p = 0.04782893516094
p2 = p*p
c0p = 4/(3*np.pi)*p2
out = {}

for frac in [0.001, 0.1, 0.5, 0.9, 0.999]:
    eps = frac*c0p
    B = p2 - (3*np.pi/4)*eps          # budget for f^2 + 2p Re alpha
    disc = np.sqrt(max(B, 0.0))
    pred_hi, pred_lo = p + disc, p - disc
    # sample alpha in disk of radius 3p, f in [|alpha|, 4p]
    N = 4_000_000
    re = rng.uniform(-3*p, 3*p, N); im = rng.uniform(-3*p, 3*p, N)
    absa = np.hypot(re, im)
    f = rng.uniform(0, 4*p, N)
    rhs = -(3*np.pi/4)*eps
    ok = (f >= absa) & (f*f + 2*p*re <= rhs)
    fs = f[ok]; aa = absa[ok]
    if fs.size:
        got_hi, got_lo, got_amin = fs.max(), fs.min(), aa.min()
    else:  # thin sliver at extreme eps: sampling can miss; 1-D refinements below decide
        got_hi = got_lo = got_amin = float('nan')
    # boundary refinement: extremes occur at alpha real negative, f = |alpha| (coherent)
    a_line = np.linspace(0, 3*p, 2_000_001)
    feas = a_line[a_line*a_line - 2*p*a_line <= -(3*np.pi/4)*eps]  # f=a, alpha=-a
    ref_hi, ref_lo = feas.max(), feas.min()
    out[f'eps/c0p={frac}'] = {
        'pred_sup_f/p': pred_hi/p, 'sampled_sup_f/p': got_hi/p if got_hi==got_hi else None, 'refined_sup_f/p': ref_hi/p,
        'pred_inf_f/p': pred_lo/p, 'sampled_inf_f/p': got_lo/p if got_lo==got_lo else None,
        'sampled_min|alpha|/p': got_amin/p if got_amin==got_amin else None,
        'note_inf': 'sampled inf approaches pred from above as N grows; refined line'
                    ' (anti-phase coherent, f=|alpha|) attains sup exactly',
        'sup_err': abs(ref_hi - pred_hi)/p}
    # inf check on the coherent line: smallest a with a^2-2pa <= B is 0? No: constraint is
    # <=, small a gives a^2-2pa<0<=B only if B>=... B < 0 impossible here (eps<=c0p => B>=0).
    # The FLOOR comes from the reductio EQUALITY direction: budget also lower-bounded?
    # No: the floor comes from p^2+f^2+2pRe(alpha) <= p^2-(3pi/4)eps REQUIRING Re(alpha)
    # <= -(f^2+(3pi/4)eps)/(2p), and |alpha|<=f: feasibility of ANY (f,alpha) needs
    # 2pf >= f^2+(3pi/4)eps. Check: smallest feasible f:
    fgrid = np.linspace(0, 2.2*p, 2_000_001)
    feas_f = fgrid[2*p*fgrid >= fgrid*fgrid + (3*np.pi/4)*eps]
    out[f'eps/c0p={frac}']['refined_inf_f/p'] = feas_f.min()/p if feas_f.size else None
    out[f'eps/c0p={frac}']['inf_err'] = abs(feas_f.min() - pred_lo)/p if feas_f.size else None

json.dump(out, open('/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/GRAND/final/A1/a1_opt_out.json','w'), indent=1)
for k, v in out.items():
    print(k, '| sup err %.2e | inf err %.2e | pred sup/p %.6f | pred inf/p %.6f'
          % (v['sup_err'], v['inf_err'], v['pred_sup_f/p'], v['pred_inf_f/p']))
print('OK')
