"""C5 ADJUDICATOR: numerical check (NUMERICAL-NONRIGOROUS, IEEE double) of the fibre identity
WITHOUT RH, for fake zeta functions with off-circle normalized roots:

  W(u) := sum_rho m_rho uhat(gamma_rho) conj(uhat(conj(gamma_rho)))
        = h * int_0^h sum_{k,l} t_{k-l} u(t+kh) conj(u(t+lh)) dt,      h = log q,

where rho = 1/2 + i gamma runs over the zeros of P(q^{-s}) (gamma in gamma_j + 2 pi Z / h,
e^{i gamma_j h} = beta_j = alpha_j / sqrt q), t_n = sum_j m_j beta_j^n, uhat(z) = int u(x) e^{izx} dx.
(The proof is in FINAL.md, C5-ADJ-W; this script only illustrates it.)

Test functions: u(x) = sum_i c_i B((x - x_i)/w), B the centred cardinal B-spline of order M (C^{M-2},
compact support); uhat(z) = w * sinc(wz/2)^M * sum_i c_i e^{i z x_i}. The zero sum is truncated at
|n| <= NMAX (tail < 1e-30 relative for the parameters used). Fibre integral: composite Gauss-Legendre.

Also: the negative direction for the hidden fake q=3, g=3 (h(x)=x^3-10x-7), window a=2.9 > (g-1/2)log 3.
"""
import json, sys, time, hashlib, platform
import numpy as np
from scipy.interpolate import BSpline
import scipy

t0 = time.time()
rng = np.random.default_rng(20261117)
M = 8
NMAX = 4000


def Bspline_centered(M):
    knots = np.arange(M + 1) - M / 2.0
    return BSpline.basis_element(knots, extrapolate=False)


Bc = Bspline_centered(M)


def Bval(x):
    y = Bc(x)
    return np.nan_to_num(y, nan=0.0)


def Bhat(xi):
    # Fourier transform of centred cardinal B-spline of order M: (sin(xi/2)/(xi/2))^M
    xi = np.asarray(xi, dtype=complex)
    out = np.ones_like(xi)
    nz = np.abs(xi) > 1e-12
    out[nz] = (np.sin(xi[nz] / 2) / (xi[nz] / 2))**M
    return out


def make_u(cs, xs, w):
    def u(x):
        x = np.asarray(x, dtype=float)
        acc = np.zeros_like(x, dtype=complex)
        for c, x0 in zip(cs, xs):
            acc += c * Bval((x - x0) / w)
        return acc
    def uhat(z):
        z = np.asarray(z, dtype=complex)
        s = np.zeros_like(z)
        for c, x0 in zip(cs, xs):
            s += c * np.exp(1j * z * x0)
        return w * Bhat(w * z) * s
    return u, uhat


def zeros_data(P, q):
    # P(T) = prod (1 - alpha T)  =>  alpha are the roots of T^n P(1/T) = sum_j P[j] T^{n-j}
    alphas = np.roots(np.array(P, dtype=float))  # np.roots takes descending coeffs: P[0] T^n + ... + P[n]
    h = np.log(q)
    betas = alphas / np.sqrt(q)
    gammas = -1j * np.log(betas) / h
    return betas, gammas, h


def W_zero_side(uhat, gammas, h):
    n = np.arange(-NMAX, NMAX + 1)
    tot = 0.0 + 0.0j
    for g in gammas:
        z1 = g + 2 * np.pi * n / h
        z2 = np.conj(g) + 2 * np.pi * n / h
        tot += np.sum(uhat(z1) * np.conj(uhat(z2)))
    return tot


def W_fibre_side(u, betas, h, a, nsub=4000, order=24):
    kmin = int(np.floor(-a / h)) - 1
    kmax = int(np.ceil(a / h)) + 1
    ks = np.arange(kmin, kmax + 1)
    K = len(ks)
    tn = {d: np.sum(betas**d).real for d in range(-K, K + 1)}
    Tm = np.array([[tn[k - l] for l in range(K)] for k in range(K)])
    xg, wg = np.polynomial.legendre.leggauss(order)
    edges = np.linspace(0, h, nsub + 1)
    tot = 0.0 + 0.0j
    for i in range(nsub):
        lo, hi = edges[i], edges[i + 1]
        tt = (hi - lo) / 2 * xg + (hi + lo) / 2
        U = np.array([u(tt + k * h) for k in ks])  # K x order
        quad = np.einsum('ki,kl,li->i', U, Tm, np.conj(U))
        tot += (hi - lo) / 2 * np.sum(wg * quad)
    return h * tot, Tm


out = {'meta': {'script': 'adj_window_fibre.py', 'python': platform.python_version(), 'numpy': np.__version__,
                'scipy': scipy.__version__, 'M': M, 'NMAX': NMAX, 'arithmetic': 'IEEE double (non-rigorous)'}}
tests = []
cases = [('hidden_fake_q3_g3', 3, [1, 0, -1, -7, -3, 0, 27]),
         ('complex_quadruple_q5_g2', 5, [1, -6, 20, -30, 25]),
         ('g1_fake_q9', 9, [1, -7, 9]),
         ('RH_true_curve_q5_y2=x3+x+1', 5, [1, 3, 5])]
for name, q, P in cases:
    betas, gammas, h = zeros_data(P, q)
    for trial in range(3):
        a = 3.0
        w = 0.12
        nb = 9
        xs = rng.uniform(-a + 0.6, a - 0.6, nb)
        cs = rng.normal(size=nb) + (1j * rng.normal(size=nb) if trial == 2 else 0)
        u, uhat = make_u(cs, xs, w)
        Wz = W_zero_side(uhat, gammas, h)
        Wf, _ = W_fibre_side(u, betas, h, a)
        rel = abs(Wz - Wf) / max(abs(Wf), 1e-300)
        tests.append({'case': name, 'q': q, 'P_asc': P, 'max_abs_beta': float(np.max(np.abs(betas))),
                      'trial': trial, 'complex_coeffs': trial == 2, 'W_zero_side': [Wz.real, Wz.imag],
                      'W_fibre_side': [Wf.real, Wf.imag], 'rel_diff': rel})
        print(name, trial, 'zero-side', Wz, 'fibre', Wf, 'rel', rel)
out['identity_tests'] = tests

# negative direction for the hidden fake, window a = 2.9 > (g - 1/2) h = 2.7465
q, P = 3, [1, 0, -1, -7, -3, 0, 27]
betas, gammas, h = zeros_data(P, q)
t = {d: np.sum(betas**d).real for d in range(-8, 9)}
T6 = np.array([[t[k - l] for l in range(6)] for k in range(6)])
T5 = T6[:5, :5]
ev6, V6 = np.linalg.eigh(T6)
ev5 = np.linalg.eigvalsh(T5)
v = V6[:, 0]
a = 2.9
# need t* + k0 h > -a and t* + (k0+5) h < a with phi support radius rho = 2w (M=8 -> support [-4w,4w])
w = 0.012
rho = 4 * w
k0 = -3
lo = -a - k0 * h + rho
hi = a - (k0 + 5) * h - rho
tstar = (lo + hi) / 2
assert lo < hi and 0 < tstar - rho and tstar + rho < h, (lo, hi, tstar)
xs = [tstar + (k0 + k) * h for k in range(6)]
u, uhat = make_u(list(v), xs, w)
Wz = W_zero_side(uhat, gammas, h)
normsq = w * np.sum(Bval(np.linspace(-M / 2, M / 2, 200001))**2) * (M / 200000)  # int phi^2 (Riemann sum)
pred = h * normsq * ev6[0]
out['negative_direction'] = {'a': a, 'threshold_(g-1/2)h': 2.5 * h, 'eig_T6': ev6.tolist(), 'eig_T5': ev5.tolist(),
                             'support': [xs[0] - rho, xs[-1] + rho], 'W_zero_side': [Wz.real, Wz.imag],
                             'predicted_h_intphi2_lambda_min': pred}
print('negative direction: W =', Wz, 'predicted', pred, 'support', xs[0] - rho, xs[-1] + rho,
      'lambda_min(T5)=', ev5[0], 'lambda_min(T6)=', ev6[0])
out['meta']['runtime_s'] = round(time.time() - t0, 1)
path = sys.argv[1]
json.dump(out, open(path, 'w'), indent=1)
print('runtime', out['meta']['runtime_s'], path, hashlib.sha256(open(path, 'rb').read()).hexdigest())
