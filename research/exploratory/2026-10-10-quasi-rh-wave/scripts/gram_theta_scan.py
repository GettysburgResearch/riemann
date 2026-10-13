import sys; sys.path.insert(0, '.')
import numpy as np, exponent_model as em
# Scan theta for the Gram loss; also two structural variants of the low bound.
out = []
for th in [1/12, 1/18, 1/24, 1/36, 0.0]:
    P = dict(em.DEFAULT); P['theta'] = th
    B, b, l, det = em.optimise(P)
    out.append((th, B, b, l, det['active'], det['Hmod_class']))
    print(f"theta={th:.5f}  B={B:.6f}  b={b:.4f} l={l:.4f}  active={det['active']}  class={det['Hmod_class']}")
# Variant: sub-ball Gram where only the second term b - ly/2 survives (theta=0) but with ly lower bound b<=ly/2 (already in max)
# Variant 2: loss replaced by theta*b with b capped so that P_a^{1/6} ... (same as theta scan)
