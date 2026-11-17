"""C5 ADJUDICATOR: numerical illustration (NUMERICAL-NONRIGOROUS, IEEE double) of C5-ADJ-MODEL:

For Z = Z0 u {T+i delta, T-i delta, -T+i delta, -T-i delta} with Z0 = (pi/L) Z (real ordinates),
the zero-side Weil form W_Z(u) = sum_{gamma in Z} uhat(gamma) conj(uhat(conj gamma)) satisfies
W_Z(u) >= 2L (1 - 8 delta^2 L^2 e^{2 L delta}) ||u||^2 on L^2(-L, L)  (proof in FINAL.md).

We compute the minimum of W_Z(u)/||u||^2 over a B-spline subspace of L^2(-L,L) (generalized eigenproblem)
for several (L, T, delta), and compare with the proven lower bound. Truncation |n| <= NMAX of the lattice sum.
"""
import sys, json, time, hashlib, platform
import numpy as np
import scipy
from scipy.interpolate import BSpline
from scipy.linalg import eigh

t0 = time.time()
M = 6
NMAX = 20000


def bhat(xi, w):
    xi = np.asarray(xi, dtype=complex) * w
    out = np.ones_like(xi)
    nz = np.abs(xi) > 1e-12
    out[nz] = (np.sin(xi[nz] / 2) / (xi[nz] / 2))**M
    return w * out


def basis(L, nb):
    w = 2 * L / (nb + M)  # support of each spline: M*w; centres spread inside (-L, L)
    cs = np.linspace(-L + M * w / 2 * 1.0001, L - M * w / 2 * 1.0001, nb)
    return w, cs


def gram_L2(w, cs):
    # <phi_i, phi_j> = (1/2pi) int phihat_i conj(phihat_j) dxi, computed on a fine grid (non-rigorous)
    xi = np.linspace(-400 / w, 400 / w, 400001)
    dx = xi[1] - xi[0]
    B = bhat(xi, w)
    E = np.exp(1j * np.outer(cs, xi))
    F = E * B
    G = (F @ np.conj(F).T) * dx / (2 * np.pi)
    return G.real


def form_matrix(w, cs, gammas):
    # W(u) = sum_gamma uhat(gamma) conj(uhat(conj gamma)), u = sum c_i phi_i  -> c^H Mx c with
    # Mx[i,j] = sum_gamma conj(phihat_i(conj gamma)) phihat_j(gamma)
    g = np.asarray(gammas, dtype=complex)
    Fj = bhat(g, w) * np.exp(1j * np.outer(cs, g))              # phihat_j(gamma)
    Fi = bhat(np.conj(g), w) * np.exp(1j * np.outer(cs, np.conj(g)))  # phihat_i(conj gamma)
    Mx = np.conj(Fi) @ Fj.T
    return 0.5 * (Mx + np.conj(Mx).T)


rows = []
for L in [0.5, 1.0, 2.0]:
    w, cs = basis(L, 24)
    G = gram_L2(w, cs)
    n = np.arange(-NMAX, NMAX + 1)
    lattice = np.pi * n / L
    M0 = form_matrix(w, cs, lattice)
    lam0 = eigh(M0, G, eigvals_only=True)[0]
    for T in [7.3, 50.0]:
        for delta in [0.25 / L, 1.0 / L, 3.0 / L]:
            quad = [T + 1j * delta, T - 1j * delta, -T + 1j * delta, -T - 1j * delta]
            Mq = form_matrix(w, cs, quad)
            lam = eigh(M0 + Mq, G, eigvals_only=True)[0]
            bound = 2 * L * (1 - 8 * delta**2 * L**2 * np.exp(2 * L * delta))
            rows.append({'L': L, 'T': T, 'delta': delta, 'lambda_min_Z0_over_2L': lam0 / (2 * L),
                         'lambda_min_Z': lam, 'proven_lower_bound': bound, 'bound_holds': bool(lam >= bound - 1e-8)})
            print(f'L={L} T={T} delta={delta:.3f}  min W_Z/||u||^2 = {lam:.6f}   bound = {bound:.6f}   (Z0 alone: {lam0:.6f} vs 2L={2*L})')
out = {'meta': {'script': 'adj_model_window.py', 'python': platform.python_version(), 'numpy': np.__version__,
                'scipy': scipy.__version__, 'M': M, 'NMAX': NMAX, 'basis_size': 24,
                'runtime_s': round(time.time() - t0, 1), 'arithmetic': 'IEEE double (non-rigorous)'}, 'rows': rows}
path = sys.argv[1]
json.dump(out, open(path, 'w'), indent=1)
print(path, hashlib.sha256(open(path, 'rb').read()).hexdigest())
