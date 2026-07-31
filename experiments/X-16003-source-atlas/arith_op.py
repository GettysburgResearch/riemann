"""Does the ARITHMETIC Weil form obey the orthogonal-polynomial law?

The law (checked exactly on synthetic rational-Herglotz sources in mech2.py):
    t* = min { ||P||^2_{L^2(nu)} : P monic, deg 2N },  nu = sum_mu (a_mu/Omega(mu)^2) delta_mu
and P_xi is the monic degree-2N orthogonal polynomial of nu.

psi_W is NOT literally a pole sum -- it is entire, an integral over [0,L].  So the law
cannot hold exactly.  The question is how well the zeta-zero measure
    nu_zeta = sum_gamma Omega(gamma*Delta)^{-2} ( delta_{gamma Delta} + delta_{-gamma Delta} )
approximates the true inner product.  Two tests:

 (T1) orthogonality residual of the ARITHMETIC P_xi against nu_zeta.  If psi_W behaved
      exactly like sum_rho 1/(s-rho) this would be ~0.
 (T2) the exact, representation-free statement:  t* = xi^T Q_W xi = min over monic P.
      Verify, and verify the claimed minimality against random monic competitors.
"""
import sys; sys.path.insert(0, '.')
from mpmath import mp, mpf, nstr, matrix, lu_solve, polyroots
import x0001

mp.dps = 60

GAM = ['14.134725141734693790', '21.022039638771554993', '25.010857580145688763',
       '30.424876125859513210', '32.935061587739189691', '37.586178158825671257',
       '40.918719012147495187', '43.327073280914999519', '48.005150881167159727',
       '49.773832477672302182', '52.970321477714460644', '56.446247697063394805',
       '59.347044002602353080', '60.831778524609809844', '65.112544048081606661',
       '67.079810529494173714', '69.546401711173979253', '72.067157674481907582',
       '75.704690699083933168', '77.144840068874805373', '79.337375020249367922',
       '82.910380854086030183', '84.735492980517050106', '87.425274613125229406',
       '88.809111207634465424', '92.491899270558484296', '94.651344040519886967',
       '95.870634228245309758', '98.831194218193692233', '101.31785100573139122']


def build_P(xis, nodes):
    n = len(nodes)
    Om = [mpf(1)]
    for k in nodes:
        Om = [(Om[i - 1] if i > 0 else mpf(0)) * (-1) + (Om[i] * k if i < len(Om) else mpf(0))
              for i in range(len(Om) + 1)]
    P = [mpf(0)] * n
    for a, lj in enumerate(nodes):
        Omd = Om[::-1]; acc = mpf(0); Qd = []
        for i in range(len(Omd) - 1):
            acc = Omd[i] + acc * lj; Qd.append(acc)
        Qj = [-c for c in Qd[::-1]]
        for i in range(len(Qj)):
            P[i] += xis[a] * Qj[i]
    return P, Om


def peval(P, s):
    acc = mpf(0) * s
    for c in reversed(P):
        acc = acc * s + c
    return acc


print(f"{'cut':>6} {'N':>3} {'t*':>16} {'xi^T Q xi':>16} {'rel':>10} "
      f"{'||P||^2_nuzeta':>16} {'orth resid':>11} {'min over 400 random monic':>26}")
print("-" * 116)
for cut, N in [('500', 6), ('2000', 6), ('2000', 8), ('2000', 10)]:
    A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=60)
    dim = A.rows
    nodes = [mpf(k) for k in range(-N, N + 1)]
    eta = matrix([1] * dim)
    x = lu_solve(A, eta)
    denom = sum(x[i] for i in range(dim))
    tstar = 1 / denom
    xi = [x[i] * tstar for i in range(dim)]
    q = sum(xi[i] * sum(A[i, j] * xi[j] for j in range(dim)) for i in range(dim))
    P, Om = build_P(xi, nodes)
    L = mp.log(mpf(cut)); Delta = L / (2 * mp.pi)
    atoms = []
    for g in GAM:
        m = mpf(g) * Delta
        for mm in (m, -m):
            atoms.append((mm, 1 / peval(Om, mm) ** 2))
    n2 = sum(w * peval(P, m) ** 2 for m, w in atoms)
    res = []
    for k in range(2 * N):
        s = sum(w * peval(P, m) * m ** k for m, w in atoms)
        nrm = sum(abs(w) * abs(peval(P, m)) * abs(m) ** k for m, w in atoms)
        res.append(abs(s) / nrm if nrm > 0 else mpf(0))
    # (T2) minimality: random monic degree-2N competitors, value of x^T Q x
    import random
    random.seed(5)
    best = None
    for _ in range(400):
        y = [xi[i] + mpf(random.gauss(0, 1)) * abs(xi[i] if xi[i] != 0 else 1) * mpf(10) ** (-2)
             for i in range(dim)]
        s = sum(y)
        y = [v / s for v in y]              # renormalise to eta^T y = 1 (monic)
        v = sum(y[i] * sum(A[i, j] * y[j] for j in range(dim)) for i in range(dim))
        best = v if best is None or v < best else best
    print(f"{cut:>6} {N:>3} {nstr(tstar,10):>16} {nstr(q,10):>16} "
          f"{nstr(abs(q-tstar)/abs(tstar),3):>10} {nstr(n2,10):>16} {nstr(max(res),3):>11} "
          f"{nstr(best,10):>26}")

print()
print("nu_zeta mass fractions by zero index (why only the low zeros are resolved):")
for cut, N in [('2000', 6), ('2000', 10)]:
    A, _ = x0001.build_cutoff_free_matrix(cut, N, dps=60)
    nodes = [mpf(k) for k in range(-N, N + 1)]
    _, Om = build_P([mpf(0)] * (2 * N + 1), nodes)
    L = mp.log(mpf(cut)); Delta = L / (2 * mp.pi)
    w = [1 / peval(Om, mpf(g) * Delta) ** 2 for g in GAM[:8]]
    tot = sum(w)
    print(f"  cut={cut} N={N}: " + "  ".join(f"g{i+1}:{nstr(v/tot,3)}" for i, v in enumerate(w)))
