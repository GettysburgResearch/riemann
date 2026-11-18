# Level-2 audit (support for Lemma 4.1): App. A.1, l.2793-2800.  Fourier transform, w.r.t. the paper's
# normalisation hat f(y) = (2/sqrt3) int f(z) e(-zy) dx dy, of f(z) = e(z^2/c) exp(-pi eta |z|^2); claimed
#   hat f(y) = |c|/(2 sqrt(r)) exp(-pi eta N(c)|y|^2/(4r)) e(-c y^2/(4r)),   r = 1 + 3 N(c) eta^2/16.
# Run: python3 -I s4_chirp_ft_check.py
import math, cmath, numpy as np
SQ3 = math.sqrt(3); OM = complex(-0.5, SQ3 / 2)
def e(z): return np.exp(4j * np.pi * np.imag(z) / SQ3)
worst = 0
for (ca, cb), eta, y in [((1, 3), 0.6, 0.4 - 0.3j), ((3, 1), 0.35, 1.2 + 0.1j), ((5, 2), 0.25, -0.7 + 0.9j), ((-1, 0), 0.5, 0.3 + 0.2j)]:
    c = ca + cb * OM; Nc = abs(c) ** 2
    L = 9 / math.sqrt(eta); n = 1601
    xs = np.linspace(-L, L, n); X, Y = np.meshgrid(xs, xs); Z = X + 1j * Y
    F = e(Z * Z / c) * np.exp(-np.pi * eta * np.abs(Z) ** 2) * e(-Z * y)
    h = xs[1] - xs[0]
    num = (2 / SQ3) * np.sum(F) * h * h
    r = 1 + 3 * Nc * eta ** 2 / 16
    cl = abs(c) / (2 * math.sqrt(r)) * math.exp(-math.pi * eta * Nc * abs(y) ** 2 / (4 * r)) * e(-c * y * y / (4 * r))
    err = abs(num - cl) / abs(cl); worst = max(worst, err)
    print("c=%s eta=%g y=%s  quadrature=%s  closed=%s  relerr=%.1e" % (c, eta, y, np.round(num, 10), np.round(cl, 10), err))
print("worst relative error:", worst)
