import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("fm", "floor_mollifier_cost.py")
# reuse functions without running the main loop: exec only the defs
src = open("floor_mollifier_cost.py").read().split("for label, (b, l) in")[0]
exec(src)
b, l = 1/8, 1/6
E0 = floor_proposal(b, l, 1, 0, 0, False)[0]
for ideal in [True, False]:
    best = (-1, None)
    for r in np.concatenate([np.linspace(1.0, 2.0, 41), np.linspace(2.0, 6.0, 41)]):
        for eta in np.linspace(0.0, 0.45, 91):
            _, new, parts = floor_proposal(b, l, r, eta, 10.0, ideal, True)   # f = infinity: ceiling independent of f
            g = E0 - new
            if g > best[0]: best = (g, (r, eta, {k: v-E0 for k, v in parts.items()}))
    print(f"counts={'ideal' if ideal else 'paper'}, f=infinity: max gain in floor Z-exponent = {best[0]:+.5f} at r={best[1][0]:.2f}, eta={best[1][1]:.3f}, pieces(rel. to floor)={ {k: round(v,4) for k,v in best[1][2].items()} }")
