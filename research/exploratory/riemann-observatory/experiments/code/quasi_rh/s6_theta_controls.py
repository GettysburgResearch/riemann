# s6_theta_controls.py -- negative controls for s6_theta_automorphy.py:
#   (A) replace conj g(.,c) by g(.,c) in DR (5.7)  -> automorphy with (c/a)_3 should fail;
#   (B) set tau = 0 when (c,d) != 1                 -> automorphy should fail at the size of the
#       non-coprime terms (tests that DR (5.8) imposes no coprimality, as paper2.tex l.362-366 uses);
#   and the positive test again with a larger truncation radius.
import sys, os, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s6_theta as T
from s6_theta import *

def tau_noconj(m, sh=3):
    return np.conj(tau(m, sh)) * 1.0 if False else _tau_variant(m, sh, conjflag=False)
def _tau_variant(m, sh, conjflag=True, coprime_only=False):
    dec = decompose(m, sh)
    if dec is None: return 0j
    u, M, c, d = dec
    if coprime_only and norm(gcd_(c, d)) != 1: return 0j
    t = tau(m, sh)
    if conjflag: return t
    # undo the conjugation of the Gauss sum: t = phase * conj(g) * mod  ->  phase * g * mod
    if abs(t) == 0: return t
    ratio = math.sqrt(norm(d) / norm(c)); n_ = None
    if M % 3 == 2:
        n_ = (M + 4) // 3
        if u in ((1, 0), (-1, 0)): g = gauss(LAM2, c); ph = 1
        elif u in ((0, 1), (0, -1)): g = gauss(mul(OM, LAM2), c); ph = E9 ** (-1)
        else: g = gauss(mul(OM2, LAM2), c); ph = E9
        return ph * g * ratio * 3 ** (n_ / 2 + 2)
    n_ = (M + 3) // 3
    return gauss(ONE, c) * ratio * 3 ** (n_ / 2 + 2.5)
def gcd_(x, y):
    from s6_zw import egcd
    g, _, _ = egcd(x, y); return g

t0 = time.time()
R = 9.5
th = FourierSeries(tau, 3, R, const=SIGMA)
thA = FourierSeries(lambda m, s: _tau_variant(m, s, conjflag=False), 3, R, const=SIGMA)
thB = FourierSeries(lambda m, s: _tau_variant(m, s, coprime_only=True), 3, R, const=SIGMA)
print("terms", len(th.mu), "build %.1fs" % (time.time() - t0))

def make_gamma(a, c):
    m = mul((3, 0), c); d = inv_mod(a, m); b = exact_div(sub(mul(a, d), ONE), c)
    return a, b, c, d
cases = [((1, 3), (3, 0)), ((-2, 0), (3, 3)), ((4, 6), (-3, 0)), ((7, 3), (6, 3)), ((1, -3), (3, 6)), ((-5, -3), (3, 0)),
         ((4, 9), (6, 3)), ((-8, -3), (3, 6)), ((10, 3), (0, 3))]
worst = {'theta': [], 'A': [], 'B': []}
for a, c in cases:
    a, b, c, d = make_gamma(a, c)
    g = ((cv(a), cv(b)), (cv(c), cv(d)))
    ka = omega_pow(cubic_symbol(c, a)); kd = omega_pow(cubic_symbol(c, d))
    vv = 1.0 / abs(cv(c))
    for delta in (0.04 + 0.03j, -0.02 + 0.035j):
        z = -cv(d) / cv(c) + delta
        z2, v2 = act(g, z, vv)
        for name, F in (('theta', th), ('A', thA), ('B', thB)):
            r = F(z2, v2) / F(z, vv)
            worst[name].append((abs(r - ka), abs(r - kd), cubic_symbol(c, a), round(v2, 3)))
for name in worst:
    print(name, "max |ratio-(c/a)_3| = %.2e ; max |ratio-(c/d)_3| = %.2e" % (max(x[0] for x in worst[name]), max(x[1] for x in worst[name])))
print("positive test detail (|ratio-(c/a)|, |ratio-(c/d)|, (c/a) exponent, height of gamma w):")
for x in worst['theta']: print("   %.1e  %.1e  %d  %.3f" % x)
print("total %.1fs" % (time.time() - t0))
