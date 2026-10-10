import numpy as np
rng = np.random.default_rng(7)
viol = 0; checked = 0
for trial in range(300):
    nr = rng.integers(5, 15)
    reals = np.sort(rng.uniform(-20, 20, nr))
    pairs = [(rng.uniform(-15, 15), rng.uniform(0.05, 0.5)) for _ in range(rng.integers(0, 4))]
    p = np.poly1d([1.0])
    for t in reals: p = p * np.poly1d([1.0, -t])
    for (x, y) in pairs: p = p * np.poly1d([1.0, -2*x, x*x + y*y])
    dz = np.sort([w.real for w in np.roots(np.polyder(p)) if abs(w.imag) < 1e-9])
    for i in range(len(dz) - 1):
        u, up = dz[i], dz[i+1]
        if up - u < 1e-9: continue
        inside = [t for t in reals if u + 1e-9 < t < up - 1e-9]
        checked += 1
        if len(set(np.round(inside, 6))) > 1:
            viol += 1; print("VIOL:", u, up, inside)
print(f"gap-doubling D5.0: {checked} consecutive-deriv-zero intervals, violations={viol}")
