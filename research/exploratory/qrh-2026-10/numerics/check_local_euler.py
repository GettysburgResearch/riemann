"""
check_local_euler.py -- finite checks of Lemma 7.1 ("The complete local identity")
of the OpenAI QRH manuscript (30 Sep 2026, Section 7.2, eqs. (7.6)-(7.17)).

Status: FLOATING_RECONNAISSANCE (parts A, B, D) + EXACT symbolic algebra (part C).
A finite check is not a proof of the lemma.

Formulas were transcribed from the rendered PDF (pdftoppm at 250-400 dpi), NOT
from pdftotext: the text extraction drops every overbar, and the identity is
sensitive to them (see the ablations in part B).

  (7.6)  Q = N p, j = v_p(u), rho = chi_p(u/p^j) in mu_6, omega_p = chi_p(-1),
         a_p = conj(alpha(p))^3 eta(p)^3,  b_p = conj(alpha(p))^2 eta(p)^2 conj(chi_p(4)),
         V = Q^{-6z},  R = a_p^2 Q^{4-6x-6z},  W_loc = rho Q^{-w}.
  lifts  g_{chi^r}(p^t, p^{j'}) = Q^{t-1} G_r 1[j'=t-1]            (6 !| r)
                                = Q^t 1[j'>=t] - Q^{t-1} 1[j'>=t-1]  (6 | r)
  (7.7)  C_p(t,k,j') = sum_{d mod p^k, p^{j'} = p^t d (mod p^k)} chi_p^k(d) g_{chi_p^t}(p^t, (p^{j'}-p^t d)/p^k)
  (7.8)  C_p = 1 (t=k=0); 1[j'=0] (t=0<k); g_{chi^t}(p^t,p^{j'}) (t>0=k);
               omega_p^{-1} G_1 g_{chi^{t-1}}(p^t, p^{j'-1}) (t>0, k=1, j'>=1); 0 otherwise.
  (7.10) P_p = sum_{e0 in {0,1}; l,k,m >= 0} (-1)^{e0} gamma_1^{-e0} eta^{e0} (a_p conj(gamma_3))^l
               rho^{k-t} omega_p^{tk - e0 l - l(l-1)/2} C_p(t,k,j+6m) Q^{-(x+1/2)e0-(1+3x)l-wk-6zm},
         t = e0 + 3l;  P_p^* = same sum restricted to t > 0.
  (7.11) P_p^* = (1-R)^{-1} { [R(1-Q^{-1}) - eta (Q-1) Q^{-x-w} V^{1[j<=1]}]/(1-V) + J_j },
         P_p   = 1/(1-V) + 1[j=0] W_loc/(1-W_loc) + P_p^*, with the J_j table.
  (7.12) H_p = P_p (1-V)(1-W)/(1-D),  W = chi_p(u) Q^{-w},  D = eta conj(chi_p(u)) Q^{-x}
  (7.17) H_p - 1 = [D(V+W-VW) - VW + (1-V)(1-W) E_p]/(1-D),  E_p = P_p^* + D.

Parts
  A  brute force (7.7) and the Gauss lifts against (7.8), from first principles in O/p^t
  B  truncated series (7.10) (with (7.8), the lifts, and the ACTUAL Gauss sums G_r of the
     prime) against the closed form (7.11); random j, rho in mu_6, eta, x, w, z.
     Ablations: drop each overbar in turn; replace the Gauss sums by random unit phases.
  C  sympy: the table (7.16) sums to (7.11) for every j; (7.17) is an identity.
  D  size of H_p - 1 at the corners of regions (7.14), (7.15), from the closed form.

Run:  python3 -I check_local_euler.py results/local_euler.json
"""

import cmath
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import eisenstein as E  # noqa: E402  (verbatim copy of w5copg eisenstein.py)

ZETA = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]


# ---------------------------------------------------------------------------
# first-principles Gauss sums modulo prime powers
# ---------------------------------------------------------------------------
def residues(M):
    """Complete residue system of O/M as int64 arrays (x, y): x + y w."""
    N = E.norm(M)
    g = math.gcd(M[0], M[1])
    xs = np.arange(N // g, dtype=np.int64)
    ys = np.arange(g, dtype=np.int64)
    X, Y = np.meshgrid(xs, ys, indexing="ij")
    return X.ravel(), Y.ravel()


def exact_div(z, m):
    c, d = E.mul(z, E.conj(m))
    n = E.norm(m)
    assert c % n == 0 and d % n == 0, (z, m)
    return (c // n, d // n)


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def char_values(P, x, y, r):
    """chi_p(v)^r with the paper's zero convention (r = 0 mod 6 -> 1[(v,p)=1])."""
    c = P.codes(x, y).astype(np.int64)
    out = np.zeros(len(x), dtype=np.complex128)
    nz = c != E.ZERO
    out[nz] = np.exp(1j * math.pi / 3 * ((r * c[nz]) % 6))
    return out


def gauss(P, r, M, yel, res=None):
    """g_{chi_p^r}(M, y) = sum_{v mod M} chi_p(v)^r e(y v / M), M a power of p."""
    if res is None:
        res = residues(M)
    vx, vy = res
    yel = E.reduce_mod(yel, M)
    ya, yb = yel
    # w = y * v
    wa = ya * vx - yb * vy
    wb = ya * vy + yb * vx - yb * vy
    ca, cb = E.conj(M)
    N = E.norm(M)
    coord = (wa * cb + wb * ca - wb * cb) % N      # omega-coordinate of w conj(M)
    add = np.exp(2j * math.pi * coord / N)
    return complex(np.sum(char_values(P, vx, vy, r) * add))


def C_brute(P, t, k, jp, cache):
    pi = P.gen
    if t == 0 and k == 0:
        return 1.0 + 0j
    pij = E.power(pi, jp)
    pit = E.power(pi, t)
    if k == 0:
        return gauss(P, t, pit, pij, cache.setdefault(t, residues(pit)))
    Mk = E.power(pi, k)
    dx, dy = cache.setdefault(("k", k), residues(Mk))
    total = 0j
    chis = char_values(P, dx, dy, k)
    for i in range(len(dx)):
        d = (int(dx[i]), int(dy[i]))
        diff = sub(pij, E.mul(pit, d))
        if not E.divides_exact(Mk, diff):
            continue
        if chis[i] == 0:
            continue
        if t == 0:
            gs = 1.0
        else:
            gs = gauss(P, t, pit, exact_div(diff, Mk), cache.setdefault(t, residues(pit)))
        total += chis[i] * gs
    return total


# ---------------------------------------------------------------------------
# (7.8) and the lifts, as lists of (coefficient, power of Q)
# ---------------------------------------------------------------------------
def lift_terms(r, t, jp, G):
    """g_{chi^r}(p^t, p^{j'}) = sum c * Q^e (t >= 1)."""
    if r % 6:
        return [(G[r % 6], t - 1)] if jp == t - 1 else []
    out = []
    if jp >= t:
        out.append((1.0, t))
    if jp >= t - 1:
        out.append((-1.0, t - 1))
    return out


def C_terms(t, k, jp, G, omega_p):
    if t == 0 and k == 0:
        return [(1.0, 0)]
    if t == 0:
        return [(1.0, 0)] if jp == 0 else []
    if k == 0:
        return lift_terms(t, t, jp, G)
    if k == 1 and jp >= 1:
        return [(c * G[1] / omega_p, e) for c, e in lift_terms(t - 1, t, jp - 1, G)]
    return []


def terms_value(terms, Q):
    return sum(c * Q ** e for c, e in terms)


# ---------------------------------------------------------------------------
# the series (7.10) and the closed form (7.11)
# ---------------------------------------------------------------------------
def series(Q, G, omega_p, alpha, eta, rho, j, x, w, z, flip=None, L=60, K=400):
    """Truncated (7.10).  Returns (P_p, P_p^*).  flip: name of an overbar to drop."""
    flip = flip or set()
    sq = math.sqrt(Q)
    gam = {r: G[r] / sq for r in range(1, 6)}
    a_p = (alpha if "a_p" in flip else alpha.conjugate()) ** 3 * eta ** 3
    g3 = gam[3] if "gamma3" in flip else gam[3].conjugate()
    lQ = math.log(Q)
    P = 0j
    Pst = 0j
    Mmax = L // 2 + 25
    for e0 in (0, 1):
        for l in range(L):
            t = e0 + 3 * l
            kmax = K if t == 0 else 2
            for k in range(kmax):
                mrange = range(Mmax) if (t > 0 or k == 0) else (0,)   # t=0<k needs j'=0
                for m in mrange:
                    jp = j + 6 * m
                    terms = C_terms(t, k, jp, G, omega_p)
                    if not terms:
                        continue
                    coeff = ((-1) ** e0 * gam[1] ** (-e0) * eta ** e0 * (a_p * g3) ** l
                             * rho ** (k - t) * omega_p ** (t * k - e0 * l - l * (l - 1) // 2))
                    s = -(x + 0.5) * e0 - (1 + 3 * x) * l - w * k - 6 * z * m
                    val = sum(c * cmath.exp(lQ * (e + s)) for c, e in terms) * coeff
                    P += val
                    if t > 0:
                        Pst += val
    return P, Pst


def closed_form(Q, alpha, chi4, eta, rho, j, x, w, z, flip=None):
    flip = flip or set()
    a_p = (alpha if "a_p" in flip else alpha.conjugate()) ** 3 * eta ** 3
    c4 = chi4 if "b_p" in flip else chi4.conjugate()
    b_p = alpha.conjugate() ** 2 * eta ** 2 * c4
    V = Q ** (-6 * z)
    R = a_p ** 2 * Q ** (4 - 6 * x - 6 * z)
    Wl = rho * Q ** (-w)
    J = {0: -eta / rho * Q ** (-x) + Wl * R,
         1: eta * Q ** (-x - w),
         2: a_p * rho ** -3 * Q ** (1.5 - 3 * x),
         3: -eta * b_p * rho ** -2 * Q ** (2 - 3 * x - w) + b_p ** 2 * rho ** -4 * Q ** (2 - 4 * x),
         4: -eta * a_p * rho ** -3 * Q ** (2.5 - 4 * x - w),
         5: -a_p ** 2 * Q ** (3 - 6 * x)}
    Pst = ((R * (1 - 1 / Q) - eta * (Q - 1) * Q ** (-x - w) * V ** (1 if j <= 1 else 0)) / (1 - V)
           + J[j]) / (1 - R)
    P = 1 / (1 - V) + (Wl / (1 - Wl) if j == 0 else 0) + Pst
    return P, Pst


def prime_data(P):
    """Actual G_r = g_{chi^r}(p, 1), r = 1..5, omega_p, alpha, chi_p(4)."""
    res = residues(P.gen)
    G = {r: gauss(P, r, P.gen, (1, 0), res) for r in range(1, 6)}
    G[0] = -1.0
    code_m1 = int(P.codes(np.array([-1]), np.array([0]))[0])
    code_4 = int(P.codes(np.array([4]), np.array([0]))[0])
    omega_p = ZETA[code_m1].real
    assert abs(ZETA[code_m1] - omega_p) < 1e-12
    alpha = E.to_complex(P.gen) / math.sqrt(P.N)
    return G, round(omega_p), alpha, ZETA[code_4]


# ---------------------------------------------------------------------------
def part_A(primes, out):
    print("== Part A: brute force (7.7) vs (7.8), and Gauss lifts ==", flush=True)
    plan = {7: 4, 13: 3, 19: 3, 25: 2, 31: 2}
    kmax = {7: 3, 13: 2, 19: 2, 25: 2, 31: 2}
    worst_C = 0.0
    worst_lift = 0.0
    nC = nL = 0
    nonzero = 0
    for P in primes:
        if P.N not in plan:
            continue
        T = plan[P.N]
        G, omega_p, alpha, chi4 = prime_data(P)
        cache = {}
        # lifts
        for r in range(6):
            for t in range(1, T + 1):
                for jp in range(0, t + 2):
                    b = gauss(P, r, E.power(P.gen, t), E.power(P.gen, jp),
                              cache.setdefault(t, residues(E.power(P.gen, t))))
                    f = terms_value(lift_terms(r, t, jp, G), P.N)
                    worst_lift = max(worst_lift, abs(b - f) / P.N ** (t - 0.5))
                    nL += 1
        for t in range(0, T + 1):
            for k in range(0, kmax[P.N] + 1):
                for jp in range(0, t + 3):
                    b = C_brute(P, t, k, jp, cache)
                    f = terms_value(C_terms(t, k, jp, G, omega_p), P.N)
                    worst_C = max(worst_C, abs(b - f) / max(1.0, P.N ** max(t - 0.5, 0)))
                    nC += 1
                    nonzero += abs(f) > 1e-9
        print(f"  p={P.gen} N={P.N} {P.kind}: t<={T}, k<={kmax[P.N]} done", flush=True)
    out["A"] = dict(cases_C=nC, nonzero_C=nonzero, max_rel_dev_C=worst_C,
                    cases_lift=nL, max_rel_dev_lift=worst_lift,
                    primes={str(k): f"t<={v}, k<={kmax[k]}, j'<=t+2" for k, v in plan.items()})
    print(f"  (7.8): {nC} cases ({nonzero} nonzero), max rel dev {worst_C:.2e}")
    print(f"  lifts: {nL} cases, max rel dev {worst_lift:.2e}")


def part_B(primes, out, rng):
    print("== Part B: series (7.10) vs closed form (7.11) ==", flush=True)
    test_primes = [P for P in primes if P.N <= 400]
    regions = {"x=1.2,w=1.1,z=0.4": (1.2, 1.1, 0.4),
               "x=0.8,w=0.3,z=0.15": (0.8, 0.3, 0.15)}
    data = {P.gen: prime_data(P) for P in test_primes}
    res = {}
    for name, (xr, wr, zr) in regions.items():
        worst = {"P": 0.0, "Pstar": 0.0}
        n = 0
        for P in test_primes:
            G, omega_p, alpha, chi4 = data[P.gen]
            for j in range(6):
                for _ in range(3):
                    rho = ZETA[rng.integers(6)]
                    eta = cmath.exp(2j * math.pi * rng.random())
                    x = complex(xr, rng.normal() * 5)
                    w = complex(wr, rng.normal() * 5)
                    z = complex(zr, rng.normal() * 5)
                    Ps, Pss = series(P.N, G, omega_p, alpha, eta, rho, j, x, w, z)
                    Pc, Pcs = closed_form(P.N, alpha, chi4, eta, rho, j, x, w, z)
                    worst["P"] = max(worst["P"], abs(Ps - Pc) / max(1, abs(Pc)))
                    worst["Pstar"] = max(worst["Pstar"], abs(Pss - Pcs) / max(1e-300, abs(Pcs)))
                    n += 1
        res[name] = dict(cases=n, max_rel_dev_P=worst["P"], max_rel_dev_Pstar=worst["Pstar"])
        print(f"  {name}: {n} cases over {len(test_primes)} primes (N<=400), "
              f"max rel dev P {worst['P']:.2e}, P* {worst['Pstar']:.2e}", flush=True)
    out["B"] = dict(primes_tested=len(test_primes),
                    split=sum(P.kind == "split" for P in test_primes),
                    inert=sum(P.kind == "inert" for P in test_primes),
                    eta="random unit-modulus (not only roots of unity)",
                    rho="random sixth root of unity", runs=res)

    # ablations: which overbars / which Gauss-sum identities are load-bearing
    print("  ablations (x=1.2,w=1.1,z=0.4; P* relative deviation, max over cases):")
    abl = {}
    xr, wr, zr = regions["x=1.2,w=1.1,z=0.4"]
    variants = {
        "drop bar on gamma_3 in (7.10)": dict(series={"gamma3"}),
        "drop bar on alpha in a_p (both sides)": dict(series={"a_p"}, closed={"a_p"}),
        "drop bar on chi_p(4) in b_p": dict(closed={"b_p"}),
        "random Gauss phases (|G_r| = sqrt Q, Lemma 4.2 violated)": dict(random=True),
    }
    for vname, v in variants.items():
        worst = 0.0
        per_j = {}
        for P in test_primes[:12]:
            G, omega_p, alpha, chi4 = data[P.gen]
            if v.get("random"):
                G = dict(G)
                for r in range(1, 6):
                    G[r] = math.sqrt(P.N) * cmath.exp(2j * math.pi * rng.random())
            for j in range(6):
                rho = ZETA[rng.integers(6)]
                eta = cmath.exp(2j * math.pi * rng.random())
                x, w, z = complex(xr, 1.3), complex(wr, -0.7), complex(zr, 2.1)
                _, Pss = series(P.N, G, omega_p, alpha, eta, rho, j, x, w, z, flip=v.get("series"))
                _, Pcs = closed_form(P.N, alpha, chi4, eta, rho, j, x, w, z, flip=v.get("closed"))
                d = abs(Pss - Pcs) / abs(Pcs)
                per_j[j] = max(per_j.get(j, 0.0), d)
                worst = max(worst, d)
        abl[vname] = dict(max_rel_dev_Pstar=worst, per_j={str(k): v for k, v in per_j.items()})
        print(f"    {vname}: {worst:.2e}  per j: " +
              " ".join(f"{k}:{per_j[k]:.1e}" for k in sorted(per_j)))
    out["B"]["ablations"] = abl


def part_C(out):
    print("== Part C: sympy, table (7.16) -> (7.11), and (7.17) ==", flush=True)
    import sympy as sp
    R, V, Q, eta, rho, a, b, Wl, X, Y, Z = sp.symbols("R V Q eta rho a b W_loc X Y Z")
    # X = Q^{-x}, Y = Q^{-w}, Z := Q^{1/2}; monomials Q^{c - n x - w} written via X, Y, Z
    r, m = sp.symbols("r m", integer=True, nonnegative=True)
    results = {}
    for j in range(6):
        # rows of (7.16) after division by R^r, summed over m, as functions of r
        rows = []
        rows.append(sp.Sum(R * (1 - 1 / Q) * V ** (m - r - 1), (m, r + 1, sp.oo)))
        if j == 5:
            rows.append(-a ** 2 * Z ** 6 * X ** 6)
        if j == 0:
            rows.append(Wl * R)
            rows.append(-eta / rho * X)
        if j == 1:
            rows.append(eta * X * Y)
        lo = r + (1 if j <= 1 else 0)
        rows.append(sp.Sum(-eta * (Q - 1) * X * Y * V ** (m - r), (m, lo, sp.oo)))
        if j == 2:
            rows.append(a / rho ** 3 * Z ** 3 * X ** 3)
        if j == 3:
            rows.append(-eta * b / rho ** 2 * Z ** 4 * X ** 3 * Y)
            rows.append(b ** 2 / rho ** 4 * Z ** 4 * X ** 4)
        if j == 4:
            rows.append(-eta * a / rho ** 3 * Z ** 5 * X ** 4 * Y)
        inner = sp.simplify(sum(sp.simplify(x.doit()) if isinstance(x, sp.Sum) else x
                                for x in rows))
        inner = sp.piecewise_fold(inner)
        inner = inner.args[0][0] if isinstance(inner, sp.Piecewise) else inner
        total = sp.simplify(sp.Sum(R ** r * inner, (r, 0, sp.oo)).doit())
        total = total.args[0][0] if isinstance(total, sp.Piecewise) else total
        Jj = {0: -eta / rho * X + Wl * R, 1: eta * X * Y, 2: a / rho ** 3 * Z ** 3 * X ** 3,
              3: -eta * b / rho ** 2 * Z ** 4 * X ** 3 * Y + b ** 2 / rho ** 4 * Z ** 4 * X ** 4,
              4: -eta * a / rho ** 3 * Z ** 5 * X ** 4 * Y, 5: -a ** 2 * Z ** 6 * X ** 6}[j]
        closed = ((R * (1 - 1 / Q) - eta * (Q - 1) * X * Y * V ** (1 if j <= 1 else 0)) / (1 - V)
                  + Jj) / (1 - R)
        diff = sp.simplify(sp.together(total - closed))
        results[str(j)] = str(diff)
        print(f"  j={j}: sum(table) - (7.11) = {diff}")
    # (7.17)
    W, D, Ps = sp.symbols("W D Pstar")
    Pp = 1 / (1 - V) + W / (1 - W) + Ps
    Hp = Pp * (1 - V) * (1 - W) / (1 - D)
    rhs = (D * (V + W - V * W) - V * W + (1 - V) * (1 - W) * (Ps + D)) / (1 - D)
    d717 = sp.simplify(Hp - 1 - rhs)
    # j > 0 case: W = D = 0, P_p = 1/(1-V) + P*
    d717b = sp.simplify((1 / (1 - V) + Ps) * (1 - V) - 1 - (1 - V) * Ps)
    print(f"  (7.17) j=0: difference = {d717};  j>0 (W=D=0): {d717b}")
    out["C"] = dict(table_to_closed_form=results, eq_7_17=str(d717), eq_7_17_ramified=str(d717b))


def part_D(out, rng):
    """Probe the stated decay of H_p - 1 at region corners (closed form; phases sampled)."""
    print("== Part D: |H_p - 1| at region corners (closed form) ==", flush=True)
    corners = {
        "(7.15) x=7/8,z=33/200,w=19/20": (7 / 8, 33 / 200, 19 / 20, 363 / 200, 33 / 40),
        "(7.14) x=51/100,z=17/50,w=53/100 (eps0=1/25)": (51 / 100, 17 / 50, 53 / 100, 1 + 1 / 50, 1 / 50),
    }
    res = {}
    for name, (xr, zr, wr, e_good, e_ram) in corners.items():
        rows = []
        for Q in [7, 13, 25, 97, 1009, 10007, 100003, 1000003]:
            best_good = best_ram = 0.0
            for _ in range(400):
                eta = cmath.exp(2j * math.pi * rng.random())
                alpha = cmath.exp(2j * math.pi * rng.random())
                chi4 = ZETA[2 * rng.integers(3)]
                rho = ZETA[rng.integers(6)]
                x, w, z = complex(xr, 0), complex(wr, 0), complex(zr, 0)
                # good prime (j = 0): W = W_loc = rho Q^{-w}, D = eta conj(rho) Q^{-x}
                P, _ = closed_form(Q, alpha, chi4, eta, rho, 0, x, w, z)
                V = Q ** (-6 * z)
                W = rho * Q ** (-w)
                D = eta * rho.conjugate() * Q ** (-x)
                Hg = P * (1 - V) * (1 - W) / (1 - D)
                best_good = max(best_good, abs(Hg - 1))
                for j in range(1, 6):
                    P, _ = closed_form(Q, alpha, chi4, eta, rho, j, x, w, z)
                    best_ram = max(best_ram, abs(P * (1 - V) - 1))
            row = dict(Q=Q, max_abs_Hm1_good=best_good, max_abs_Hm1_ramified=best_ram)
            if e_good:
                row[f"scaled_good(Q^{e_good:.4g})"] = best_good * Q ** e_good
                row[f"scaled_ram(Q^{e_ram:.4g})"] = best_ram * Q ** e_ram
            rows.append(row)
            print("  " + name + " " + " ".join(f"{k}={v:.3g}" for k, v in row.items()))
        res[name] = rows
    out["D"] = res


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else "local_euler.json"
    t0 = time.time()
    rng = np.random.default_rng(20261010)
    primes = E.prime_ideals(400)
    out = {"label": "FLOATING_RECONNAISSANCE (A,B,D) / EXACT symbolic (C)",
           "source": "OpenAI QRH manuscript 30 Sep 2026, Sec. 7.2, eqs (7.6)-(7.17); "
                     "formulas read from rendered PDF (overbars), not pdftotext"}
    part_A(primes, out)
    part_B(primes, out, rng)
    part_C(out)
    part_D(out, rng)
    out["runtime_s"] = time.time() - t0
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"done in {out['runtime_s']:.1f} s -> {out_path}")


if __name__ == "__main__":
    main()
