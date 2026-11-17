# s6_theta_automorphy.py -- numerical test of the Kubota cubic theta function built from DR (5.6)-(5.8):
#   (i) periodicity under z -> z+1, z -> z+3 omega;  (ii) invariance under E=(0 -1;1 0) (SL_2(Z));
#   (iii) automorphy theta(gamma w) = chi(gamma) theta(w) on Gamma_1(3), discriminating
#        chi = (c/a)_3 [DR (5.4), used by paper2.tex l.3150-3152] from its conjugate (c/d)_3.
import sys, os, time, math, cmath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_theta import *

t0 = time.time()
R = float(sys.argv[1]) if len(sys.argv) > 1 else 8.5
th = FourierSeries(tau, 3, R, const=SIGMA)
print("theta terms:", len(th.mu), "R =", R, "build %.1fs" % (time.time() - t0))

def rel(a, b): return abs(a - b) / max(abs(a), abs(b))

# (i) periodicity
for (z, v) in [(0.13 + 0.21j, 0.4), (-0.31 + 0.07j, 0.35)]:
    f0 = th(z, v)
    print("period 1      : rel diff %.2e" % rel(f0, th(z + 1, v)))
    print("period 3omega : rel diff %.2e" % rel(f0, th(z + 3 * OMEGA, v)))
    print("shift omega (should NOT be invariant): rel diff %.2e" % rel(f0, th(z + OMEGA, v)))

# (ii) E-invariance, points on/near the unit sphere so both heights are large
E = ((0, -1), (1, 0))
for (z, v) in [(0.3 + 0.2j, math.sqrt(1 - 0.13)), (0.1 - 0.4j, 0.6), (0.45 + 0.1j, 0.5)]:
    z2, v2 = act(E, z, v)
    print("E-invariance at v=%.2f -> v'=%.2f : rel diff %.2e" % (v, v2, rel(th(z, v), th(z2, v2))))

# (iii) Gamma_1(3) automorphy
def make_gamma(a, c):
    # a = 1 mod 3, c = 0 mod 3, find d = 1 mod 3 with a d = 1 mod 3c, b=(ad-1)/c
    m = mul((3, 0), c)
    d = inv_mod(a, m)
    # adjust d to be = 1 mod 3 (automatic since a=1 mod 3 and 3|m)
    assert is_primary(d) or True
    b = exact_div(sub(mul(a, d), ONE), c)
    return a, b, c, d

cases = [((1, 3), (3, 0)), ((4, 3), (3, 0)), ((1, 3), (0, 3)), ((-2, 0), (3, 3)), ((4, 6), (-3, 0)), ((7, 3), (6, 3)),
         ((1, -3), (3, 6)), ((-5, -3), (3, 0))]
for a, c in cases:
    a, b, c, d = make_gamma(a, c)
    assert is_primary(a) and is_primary(d) and b[0] % 3 == 0 and b[1] % 3 == 0 and c[0] % 3 == 0 and c[1] % 3 == 0
    assert sub(mul(a, d), mul(b, c)) == ONE
    g = ((cv(a), cv(b)), (cv(c), cv(d)))
    ca = cubic_symbol(c, a); cd = cubic_symbol(c, d); bd = cubic_symbol(b, d)
    # point near the cusp -d/c with v chosen so both heights are comparable
    cc = cv(c); dd = cv(d)
    vv = 1.0 / abs(cc)
    for delta in (0.05 + 0.03j, -0.02 + 0.04j):
        z = -dd / cc + delta
        z2, v2 = act(g, z, vv)
        r = th(z2, v2) / th(z, vv)
        print("gamma a=%s b=%s c=%s d=%s  heights %.3f->%.3f  ratio=%s  |ratio|=%.12f  (c/a)_3=w^%d (c/d)_3=w^%d (b/d)_3=w^%d"
              % (a, b, c, d, vv, v2, np.round(r, 10), abs(r), ca, cd, bd))
        print("     |ratio-(c/a)| = %.2e   |ratio-(c/d)| = %.2e" % (abs(r - omega_pow(ca)), abs(r - omega_pow(cd))))
print("total %.1fs" % (time.time() - t0))
