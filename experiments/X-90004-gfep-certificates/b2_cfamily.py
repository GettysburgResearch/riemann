import numpy as np
from b2_core import H, J, Jp, Hc, E, Ec

rng = np.random.default_rng(7)

# (1) c-monotonicity: finite-difference d/dc H_c vs claimed identity (theta^{3/2}/c^2) J'(theta/c)
print("== c-derivative identity check ==")
bad = 0; worst = 0.0
for _ in range(4000):
    th = rng.uniform(1e-4, 0.90)
    c = rng.uniform(min(th * 1.02, 0.99), 0.995)
    u = th / c
    # avoid knots of u and th
    if abs(u - 1 / round(1 / u)) < 1e-4 or abs(1/u - round(1/u)) < 1e-3: continue
    h = 1e-7 * c
    fd = (Hc(np.array([th]), c + h)[0] - Hc(np.array([th]), c - h)[0]) / (2 * h)
    idd = th ** 1.5 / c ** 2 * Jp(np.array([u]))[0]
    err = abs(fd - idd) / max(1.0, abs(idd))
    worst = max(worst, err)
    if fd < -1e-9: bad += 1
print(f"max rel err fd-vs-identity: {worst:.2e}; negative-derivative violations: {bad}")

# (2) pointwise ordering: c <= c' => H_c <= H_c' <= 0
print("== pointwise ordering in c ==")
ths = rng.uniform(1e-4, 0.999, 300)
cs = np.sort(rng.uniform(0.02, 0.999, 60))
M = np.array([Hc(ths, c) for c in cs])  # rows: c increasing
d = np.diff(M, axis=0)
print("min over c-increments of H_{c+} - H_{c-}:", d.min(), " (>= 0 expected); max H_c:", M.max())

# (3) PSD max-kernel:  G_ij = -H_{max(ci,cj)}(theta)  should be PSD (f(max), f nonincreasing >= 0)
#     and -H_{min} should generically NOT be PSD.
print("== max-kernel PSD test ==")
for theta in (0.03, 0.1408, 0.4, 0.75):
    for trial in range(3):
        cs = np.sort(rng.uniform(theta + 1e-3, 0.999, 40))
        CM = np.maximum.outer(cs, cs)
        Cm = np.minimum.outer(cs, cs)
        Gmax = np.array([[-Hc(np.array([theta]), CM[i, j])[0] for j in range(len(cs))] for i in range(len(cs))])
        Gmin = np.array([[-Hc(np.array([theta]), Cm[i, j])[0] for j in range(len(cs))] for i in range(len(cs))])
        emax = np.linalg.eigvalsh(Gmax).min()
        emin = np.linalg.eigvalsh(Gmin).min()
        print(f"theta={theta}: min eig(-H_max)={emax:.3e}  min eig(-H_min)={emin:.3e}")

# (4) the induced quadratic form on E_c differences: sum_i x_i E_{c_i} integrated against
#     nondecreasing weights stays in the cone iff coefficients respect ordering; check the
#     two-parameter closure element sqrt(th)(J(th/a)-J(th/b)), a<=b, is <=0... sign:
print("== two-parameter family sign ==")
a, b = 0.3, 0.7
ths = rng.uniform(1e-4, 0.999, 2000)
v = np.sqrt(ths) * (J(np.minimum(ths / a, 1.0)) - J(np.minimum(ths / b, 1.0)))
print("max of sqrt(th)(J(th/a)-J(th/b)) for a<b:", v.max(), "(<=0 expected: th/a>=th/b, J nondecr)")
