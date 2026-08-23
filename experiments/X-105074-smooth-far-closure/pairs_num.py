# A2 pairs_num.py -- far-pinch candidate pairs from verified zero tables.
# Far pinch condition (FAR.md 4.4 / F-4): pole z_p(rho)=a-rho collides with branch
# z_b(rho') = rho'-a  iff  rho + rho' = 2a = 3/2 + 3s, i.e.
#   beta + beta' = 3/2 + 3h  and  gamma + gamma' = 3t in [gamma_1 - 3 r_0, gamma_1 + 3 r_0].
# Pole-side zero has gamma < 0 (conjugate), branch-side gamma' > 0:
# candidate pairs: gamma'_k - gamma_j in [gamma_1 - 3 r_0, gamma_1 + 3 r_0], both from tables.
# All tabulated zeros are on the line: beta = beta' = 1/2, so beta+beta' = 1 and the
# "pinch defect" (3/2 + 3h) - (beta+beta') >= 1/2 for every h > 0: NO pinch possible.
# Re s' = (beta+beta'-3/2)/3 = -1/6: distance 1/6 LEFT of Omega^+ = {Re s > 0}.
import json
from mpmath import mp, zetazero
mp.dps = 20
gamma1 = float(zetazero(1).imag)
r0 = 1.0
N = 60
gams = [float(zetazero(k).imag) for k in range(1, N + 1)]
pairs = []
for j, gj in enumerate(gams, 1):          # pole-side zero at -gj (conjugate)
    for k, gk in enumerate(gams, 1):      # branch-side zero at +gk
        dgap = gk - gj                    # = gamma' - |gamma|
        if abs(dgap - gamma1) <= 3 * r0:
            s_im = (gk - gj) / 3.0        # Im s' = (gamma+gamma')/3 with gamma=-gj
            pairs.append(dict(j=j, k=k, gamma_pole=-gj, gamma_branch=gk,
                              beta_sum=1.0, pinch_defect_at_h0=0.5,
                              Re_sprime=-1.0 / 6.0, Im_sprime=s_im,
                              dist_to_window_Im=abs(s_im - gamma1 / 3.0)))
pairs.sort(key=lambda p: (p["gamma_branch"], p["j"]))
first20 = pairs[:20]
out = dict(gamma1=gamma1, r0=r0, n_zeros_used=N, height_max=gams[-1],
           n_candidate_pairs=len(pairs),
           note=("every tabulated pair has beta+beta'=1 (all on line); pinch needs "
                 "beta+beta' = 3/2+3h: defect >= 1/2 for all h>0. Re s' = -1/6 < 0: "
                 "outside Omega^+ by absolute distance 1/6. No pair below height "
                 f"{gams[-1]:.2f} (in particular none below 60) can pinch."),
           first20=first20)
with open(__file__.replace("pairs_num.py", "pairs_num_out.json"), "w") as f:
    json.dump(out, f, indent=1)
print("gamma1 =", gamma1)
print("zeros used:", N, "up to height", round(gams[-1], 3))
print("candidate pairs (|gamma'-|gamma|-gamma1| <= 3):", len(pairs))
print("first 20 (j,k, gamma_pole, gamma_branch, Im s', dist to window):")
for p in first20:
    print(f"  ({p['j']:2d},{p['k']:2d})  {p['gamma_pole']:9.4f} {p['gamma_branch']:9.4f}"
          f"  Im s'={p['Im_sprime']:7.4f}  d={p['dist_to_window_Im']:6.4f}")
print("ALL pairs: beta+beta' = 1, pinch defect at h->0+ is 1/2 > 0; Re s' = -1/6.")
