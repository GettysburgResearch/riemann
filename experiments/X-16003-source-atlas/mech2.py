"""The CvS finite gate, decoded.

Setup: nodes lam_{-N}..lam_N (2N+1 of them), Omega(s) = prod_k (lam_k - s),
ell(s)_j = 1/(lam_j - s), and for a coefficient vector x the CvS interpolation
polynomial P_x(s) = sum_j x_j prod_{k != j}(lam_k - s).

Three exact facts, each checked below:

 (A)  P_x(s) = Omega(s) <x, ell(s)>                                       [one line]
 (B)  the coefficient of s^{2N} in P_x is exactly eta^T x
      => the CvS normalisation eta^T x = 1 says exactly "P_x is MONIC of degree 2N"
 (C)  for Q positive definite,   t* = 1/(eta^T Q^{-1} eta) = min { x^T Q x : eta^T x = 1 }
      and the minimiser is the CvS kernel vector xi = Q^{-1} eta / (eta^T Q^{-1} eta).

Combine with L-16004 (psi(x) = sum_mu a_mu/(mu-x)  =>  Q = sum_mu a_mu ell(mu) ell(mu)^T):

      x^T Q x = sum_mu a_mu <ell(mu),x>^2 = sum_mu a_mu P_x(mu)^2 / Omega(mu)^2

so, writing  d nu = sum_mu ( a_mu / Omega(mu)^2 ) delta_mu ,

      t*(N) = min { || P ||^2_{L^2(nu)} : P monic, deg P = 2N }

and the CvS kernel polynomial P_xi is THE MONIC DEGREE-2N ORTHOGONAL POLYNOMIAL of the
discrete measure nu supported on the POLES of the source.

Consequences, all classical once stated that way:
  * P_xi has 2N real simple roots inside the convex hull of the poles  (= CvS Thm 5.6 here)
  * its roots are the 2N-point GAUSS QUADRATURE NODES for nu
  * if #poles = 2N+1 - 1 = 2N then nu has 2N atoms and P_xi vanishes at ALL of them exactly
  * the weight Omega(mu)^{-2} ~ mu^{-2(2N+1)} is why only the LOWEST poles are resolved
  * t* -> 0 monotonically in N: orthogonal-polynomial norms decrease.

This script tests (A),(B),(C) and then the orthogonality claim directly.
HIGH-PRECISION FLOAT (mpmath) throughout; the orthogonality residuals are the evidence.
"""
from mpmath import mp, mpf, nstr, matrix, lu_solve, polyroots

mp.dps = 80


def loewner_from_poles(poles, weights, nodes):
    """EXACT L-16004 assembly: Q = sum_mu a_mu ell(mu) ell(mu)^T over mu in +-poles."""
    n = len(nodes)
    Q = matrix(n, n)
    allp = [(m, a) for m, a in zip(poles, weights)] + [(-m, a) for m, a in zip(poles, weights)]
    for m, a in allp:
        ell = [1 / (nodes[j] - m) for j in range(n)]
        for i in range(n):
            for j in range(n):
                Q[i, j] += a * ell[i] * ell[j]
    return Q, allp


def loewner_from_divided_differences(poles, weights, nodes):
    """Independent build straight from CvS Prop 4.1, to check L-16004."""
    def psi(x):
        return sum(a * (1 / (m - x) + 1 / (-m - x)) for m, a in zip(poles, weights))
    def dpsi(x):
        return sum(a * (1 / (m - x) ** 2 + 1 / (-m - x) ** 2) for m, a in zip(poles, weights))
    n = len(nodes)
    Q = matrix(n, n)
    for i in range(n):
        for j in range(n):
            Q[i, j] = dpsi(nodes[i]) if i == j else (psi(nodes[i]) - psi(nodes[j])) / (nodes[i] - nodes[j])
    return Q


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


def report(name, poles, weights, N):
    nodes = [mpf(k) for k in range(-N, N + 1)]
    dim = 2 * N + 1
    Q, allp = loewner_from_poles(poles, weights, nodes)
    Qd = loewner_from_divided_differences(poles, weights, nodes)
    l4 = max(abs(Q[i, j] - Qd[i, j]) for i in range(dim) for j in range(dim))
    sc = max(abs(Q[i, j]) for i in range(dim) for j in range(dim))
    eta = matrix([1] * dim)
    x = lu_solve(Q, eta)
    denom = sum(x[i] for i in range(dim))
    tstar = 1 / denom
    xi = [x[i] * tstar for i in range(dim)]
    P, Om = build_P(xi, nodes)
    print(f"### {name}   N={N}  dim={dim}  #pole pairs={len(poles)}  (#atoms {len(allp)} vs deg {2*N})")
    print(f"  L-16004 check: |Loewner(psi) - sum a ell ell^T|_max / scale = {nstr(l4/sc,4)}")
    # (B) leading coefficient == eta^T xi == 1
    print(f"  (B) leading coeff of P_xi (should be eta^T xi = 1): {nstr(P[2*N], 12)}")
    # (C) variational value
    q = sum(xi[i] * sum(Q[i, j] * xi[j] for j in range(dim)) for i in range(dim))
    print(f"  (C) t* = {nstr(tstar,12)}   xi^T Q xi = {nstr(q,12)}   rel.diff {nstr(abs(q-tstar)/abs(tstar),4)}")
    # the measure nu on the poles
    nu = [(m, a / peval(Om, m) ** 2) for m, a in allp]
    tot = sum(w for _, w in nu)
    # orthogonality of P_xi to all lower degrees in L^2(nu)
    res = []
    for k in range(2 * N):
        s = sum(w * peval(P, m) * m ** k for m, w in nu)
        nrm = sum(abs(w) * abs(peval(P, m)) * abs(m) ** k for m, w in nu)
        res.append(abs(s) / nrm if nrm > 0 else mpf(0))
    print(f"  ORTHOGONALITY  max_k |<P_xi, s^k>_nu| / (abs-sum)  for k=0..{2*N-1}: {nstr(max(res),4)}")
    # and the norm equals t*
    n2 = sum(w * peval(P, m) ** 2 for m, w in nu)
    print(f"  ||P_xi||^2_nu = {nstr(n2,12)}   vs t* = {nstr(tstar,12)}   rel.diff {nstr(abs(n2-tstar)/abs(tstar),4)}")
    # mass distribution of nu -- why only low poles are seen
    mm = sorted(set(abs(m) for m, _ in allp))
    print(f"  nu mass fractions by |pole| : "
          f"{[(nstr(m,6), nstr(sum(w for mu,w in nu if abs(mu)==m)/tot, 3)) for m in mm[:6]]}")
    rts = polyroots(P[::-1], maxsteps=600, extraprec=6000)
    rr = sorted([mp.re(r) for r in rts if abs(mp.im(r)) < mpf(10) ** (-25) * max(1, abs(mp.re(r)))])
    pos = [v for v in rr if v > 0]
    print(f"  #real roots {len(rr)}/{2*N};  positive roots {[nstr(v,10) for v in pos[:7]]}")
    print(f"  true poles (+)                  {[nstr(m,10) for m in poles[:7]]}")
    print()


print("=" * 104)
print("EXACTLY-DETERMINED REGIME  (#atoms = 2N):  P_xi should vanish at EVERY pole, exactly")
print("=" * 104)
report("6 pole pairs, unit weights", [mpf(v) for v in [11, 19, 27, 35, 43, 51]], [mpf(1)] * 6, N=6)

print("=" * 104)
print("OVER-DETERMINED REGIME  (#atoms >> 2N):  this is the regime the arithmetic form is in.")
print("P_xi should become the degree-2N ORTHOGONAL POLYNOMIAL of nu, i.e. Gauss nodes for nu.")
print("=" * 104)
G = [mpf(v) for v in ['14.134725141734693', '21.022039638771555', '25.010857580145688',
                      '30.424876125859513', '32.935061587739190', '37.586178158825671',
                      '40.918719012147495', '43.327073280914999', '48.005150881167159',
                      '49.773832477672302', '52.970321477714460', '56.446247697063394',
                      '59.347044002602353', '60.831778524609809', '65.112544048081606',
                      '67.079810529494173', '69.546401711173979', '72.067157674481907',
                      '75.704690699083933', '77.144840068874805']]
for N in (3, 4, 6):
    report(f"the first 20 zeta ordinates as poles (Delta=1), unit weights", G, [mpf(1)] * len(G), N=N)
