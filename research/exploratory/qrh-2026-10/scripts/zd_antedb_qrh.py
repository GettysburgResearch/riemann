"""zd_antedb_qrh.py -- QRH-IMPORT inserted into the ANTEDB zero-density machinery.

Status: CONDITIONAL on QRH-IMPORT (external, unreviewed) / reconnaissance.

Usage (sandboxed; ANTEDB is downloaded, read, and only imported from its own path):
    python -I zd_antedb_qrh.py <path to expdb/blueprint/src/python> [part ...]
parts: mu  (exact mu envelope with and without the QRH point (7/8, 0))
       zd  (Corollary 11.7 zero-density runs with and without QRH zeta-large-value data)
       best (aggregate ANTEDB best-known A(sigma) table at sample sigma)
Default: all parts.

QRH-IMPORT enters ONLY as zeta-type information:
  mu(7/8) = 0 (Titchmarsh 14.2 argument + continuity of mu), hence by ANTEDB Cor. lvz-mu
  LV_zeta(sigma, tau) = -infinity for sigma > 7/8, and, redundantly, the zeta large-value
  regions of every vertex of the QRH-convexified mu envelope.
It does NOT enter general large-value estimates LV(sigma, tau) (arbitrary coefficients) or
exponent pairs / beta bounds (general phases): QRH says nothing about those objects.
All arithmetic below is exact (fractions.Fraction); ANTEDB uses exact cdd polytopes.
"""

import sys
import time
from fractions import Fraction as F

EXPDB = sys.argv[1]
PARTS = sys.argv[2:] or ["mu", "zd", "best"]
sys.path.insert(0, EXPDB)

import literature as L  # noqa: E402  (ANTEDB module; read before running)
import large_values as lv  # noqa: E402
import zeta_large_values as zlv  # noqa: E402
import zero_density_estimate as zd  # noqa: E402
import bound_beta as bbeta  # noqa: E402
import exponent_pair as ep  # noqa: E402
from bound_mu import classical_bound_mu  # noqa: E402  (label only; year needed by ANTEDB)
from hypotheses import Hypothesis_Set  # noqa: E402
from functions import Interval  # noqa: E402
from reference import Reference  # noqa: E402

QRH_EDGE = F(7, 8)

# Compatibility shim (sympy 1.14): ANTEDB's RationalFunction.max/min compares candidate
# functions against a +-oo default; sympy.real_roots then raises on expressions containing
# oo. Crossing points of an infinite default can never change the max/min, so we return
# no roots for such expressions (cells are only refined by the finite functions). Counted.
import sympy as _sp  # noqa: E402
_orig_real_roots = _sp.real_roots
SHIM_EVENTS = [0]


def _real_roots_shim(expr, *a, **k):
    e = _sp.sympify(expr)
    if e.has(_sp.oo, -_sp.oo, _sp.zoo, _sp.nan):
        SHIM_EVENTS[0] += 1
        return []
    roots = _orig_real_roots(e, *a, **k)
    # Irrational crossing points (e.g. involving sqrt(609)) make later sympy comparisons
    # undecidable; replace them by 40-digit rational approximations (cell boundaries only).
    out = []
    for r in roots:
        if r.is_Rational:
            out.append(r)
        else:
            SHIM_EVENTS[0] += 1
            out.append(_sp.Rational(str(_sp.N(r, 40))))
    return out


_sp.real_roots = _real_roots_shim


# ---------------------------------------------------------------- mu envelope (exact)
def lower_hull(points):
    pts = sorted(set(points))
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            # keep only strictly convex (lower) turns
            if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) <= 0:
                hull.pop()
            else:
                break
        hull.append(p)
    return hull


def hull_eval(hull, s):
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        if x1 <= s <= x2:
            return y1 + (y2 - y1) * (s - x1) / (x2 - x1)
    raise ValueError(s)


def mu_points_unconditional():
    pts = [(F(0), F(1, 2)), (F(1), F(0))]
    for h in L.literature.list_hypotheses(hypothesis_type="Upper bound on mu"):
        s, m = F(h.data.sigma), F(h.data.mu)
        pts.append((s, m))
    for h in L.literature.list_hypotheses(hypothesis_type="Exponent pair"):
        k, l = F(h.data.k), F(h.data.l)
        pts.append((l - k, k))  # mu(l - k) <= k
    # functional equation mu(1 - s) <= mu(s) + s - 1/2, and mu(s) for s >= 1/2 from s <= 1/2
    pts += [(1 - s, m + s - F(1, 2)) for (s, m) in pts if s > F(1, 2)]
    pts += [(1 - s, m - (F(1, 2) - s)) for (s, m) in pts if s < F(1, 2)]
    return [(s, m) for (s, m) in pts if F(0) <= s <= F(1)]


def part_mu():
    print("=" * 78)
    print("PART mu: exact lower convex envelope of literature mu-points (ANTEDB data)")
    pts = mu_points_unconditional()
    unc = [p for p in lower_hull(pts) if p[0] >= F(1, 2)]
    unc = lower_hull([(F(1, 2), hull_eval(lower_hull(pts), F(1, 2)))] + unc)
    qrh = lower_hull(unc + [(QRH_EDGE, F(0))])
    print("unconditional envelope vertices on [1/2,1]:", len(unc))
    print("QRH envelope vertices on [1/2,1]:", [(str(a), str(b)) for a, b in qrh])
    print(f"{'sigma':>8} {'mu_unc':>12} {'mu_QRH':>12} {'(26/63)(7/8-s)':>16}")
    for s in [F(1, 2), F(11, 20), F(3, 5), F(13, 20), F(7, 10), F(3, 4), F(4, 5), F(17, 20), F(7, 8), F(9, 10)]:
        mu_u, mu_q = hull_eval(unc, s), hull_eval(qrh, s)
        lin = max(F(26, 63) * (QRH_EDGE - s), F(0))
        print(f"{float(s):8.4f} {float(mu_u):12.6f} {float(mu_q):12.6f} {float(lin):16.6f}")
    # tangent point and tau*: sup over alpha < 7/8 of (7/8 - alpha) / mu_unc(alpha)
    best = max(((QRH_EDGE - a) / m, a, m) for (a, m) in unc if a < QRH_EDGE and m > 0)
    print(f"tangent from (7/8,0) touches unconditional envelope at alpha* = {best[1]} "
          f"(mu = {best[2]}), tau* = {best[0]} = {float(best[0]):.6f}")
    # sup-norm exponent of zeta sums: sigma_max(tau) = min_alpha alpha + tau*mu(alpha)
    print(f"{'tau':>6} {'sigma_max_unc':>14} {'sigma_max_QRH':>14} {'min(unc,7/8)':>13}")
    for tau in [F(1), F(3, 2), F(2), F(9, 4), F(12, 5), F(5, 2), F(3), F(4), F(6)]:
        su = min(a + tau * m for (a, m) in unc)
        sq = min(a + tau * m for (a, m) in qrh)
        assert sq == min(su, QRH_EDGE), "envelope lemma violated"
        print(f"{float(tau):6.3f} {float(su):14.6f} {float(sq):14.6f} {float(min(su, QRH_EDGE)):13.6f}")
    print("CHECK: sigma_max_QRH(tau) == min(sigma_max_unc(tau), 7/8) at all sampled tau: PASS")
    return unc, qrh


# ---------------------------------------------------------------- zero-density runs
def base_hypotheses(kind):
    hs = Hypothesis_Set()
    hs.add_hypothesis(lv.large_value_estimate_L2)
    for k in range(2, 6):
        hs.add_hypothesis(lv.raise_to_power_hypothesis(k))
    if kind == "classical":
        return hs
    names = ["Huxley large value estimate", "Heath-Brown large value estimate",
             "Guth--Maynard large value estimate", "Bourgain optimized large value estimate"]
    names += [f"Jutila large value estimate with k = {k}" for k in (1, 2, 3)]
    for n in names:
        hs.add_hypothesis(L.literature.find_hypothesis(name=n))
    hs.add_hypothesis(L.literature.find_hypothesis(keywords="Heath-Brown (1978) zeta large value estimate"))
    # beta bounds from two strong exponent pairs (zeta sums via beta_to_zlv)
    pairs = Hypothesis_Set()
    for (k, l) in [(F(3, 40), F(31, 40)), (F(13, 84), F(55, 84))]:
        pairs.add_hypothesis(ep.derived_exp_pair(k, l, "literature pair", set()))
    hs.add_hypotheses(bbeta.exponent_pairs_to_beta_bounds(pairs))
    return hs


def mu_zlv_hyps(points, label):
    hs = Hypothesis_Set()
    for (s, m) in points:
        if F(1, 2) <= s <= 1:
            hs.add_hypothesis(classical_bound_mu(s, m))  # INSERTED: 'label' says which
    return zlv.mu_to_zlv(hs)


def run(kind, sigma_iv, extra, tau0=F(3)):
    hs = base_hypotheses(kind)
    hs.add_hypotheses(extra)
    t = time.time()
    out = zd.lv_zlv_to_zd(hs, sigma_iv, tau0)
    return [(h.data.interval, h.data) for h in out], time.time() - t


def sample_A(pieces, s):
    # derived estimates from lv_zlv_to_zd store A(sigma)(1 - sigma)
    vals = [float(z.at(s)) for iv, z in pieces if iv.contains(s)]
    return min(vals) / float(1 - s) if vals else None


def part_zd(unc, qrh):
    print("=" * 78)
    print("PART zd: ANTEDB Corollary 11.7 (lv_zlv_to_zd), tau0 = 3, with/without QRH zeta data")
    unc_mu_zlv = mu_zlv_hyps(unc, "unconditional mu envelope vertex")
    qrh_mu_zlv = mu_zlv_hyps(qrh, "QRH-IMPORT mu envelope vertex (incl. mu(7/8)=0)")
    intervals = [Interval(F(1, 2) + F(1, 100), F(7, 10)), Interval(F(7, 10), F(4, 5)),
                 Interval(F(4, 5), QRH_EDGE)]
    # sigma > 7/8 is not run: there the QRH zeta region is {rho = 0} only, which ANTEDB's
    # region clipping treats as empty (ValueError in as_disjoint_union); QRH gives N = 0 anyway.
    for kind in ["classical", "literature"]:
        for iv in intervals:
            try:
                a, ta = run(kind, iv, unc_mu_zlv)
                b, tb = run(kind, iv, qrh_mu_zlv)
            except Exception as exc:  # report and continue (ANTEDB/sympy compatibility)
                print(f"[{kind}] sigma in [{iv.x0}, {iv.x1}]  FAILED: {type(exc).__name__}: {str(exc)[:120]}")
                continue
            n = 24
            diffs, rows = 0, []
            for i in range(1, n):
                s = iv.x0 + (iv.x1 - iv.x0) * F(i, n)
                Aa, Ab = sample_A(a, s), sample_A(b, s)
                rows.append((s, Aa, Ab))
                if Aa is None or Ab is None or abs(float(Aa) - float(Ab)) > 1e-12:
                    diffs += 1
            print(f"[{kind}] sigma in [{iv.x0}, {iv.x1}]  ({ta:.0f}s / {tb:.0f}s, shim events {SHIM_EVENTS[0]})  "
                  f"sampled points where QRH changes the derived A: {diffs}/{n - 1}")
            for (s, Aa, Ab) in rows[:: max(1, (n - 1) // 6)]:
                fa = "None" if Aa is None else f"{float(Aa):.5f}"
                fb = "None" if Ab is None else f"{float(Ab):.5f}"
                print(f"    sigma={float(s):.4f}  A_unc={fa}  A_QRH={fb}")


def part_best():
    print("=" * 78)
    print("PART best: ANTEDB aggregate of literature + Tao-Trudgian-Yang (best known A)")
    hs = Hypothesis_Set()
    hs.add_hypotheses(L.literature)
    ref = Reference.make("Tao--Trudgian--Yang", 2024)
    zd.add_zero_density(hs, "2/(9*x - 6)", Interval("[17/22, 38/49]"), ref)
    zd.add_zero_density(hs, "9/(8*(2*x - 1))", Interval("[38/49, 4/5]"), ref)
    zd.add_zero_density(hs, "3/(10 * x - 7)", Interval("[701/1000, 1]"), ref)
    hs.add_hypotheses(zd.bourgain_ep_to_zd())
    import sympy
    x = sympy.Symbol("x")
    zdh = hs.list_hypotheses(hypothesis_type="Zero density estimate")
    grid = [F(11, 20), F(3, 5), F(13, 20), F(7, 10), F(3, 4), F(19, 25), F(77, 100), F(7, 9),
            F(25, 32), F(4, 5), F(33, 40), F(17, 20), F(87, 100), F(7, 8), F(9, 10), F(19, 20)]
    for s in grid:
        best_val, best_src = None, "-"
        for h in zdh:
            if not h.data.interval.contains(s):
                continue
            try:
                v = float(sympy.sympify(h.data.expr).subs(x, sympy.Rational(s.numerator, s.denominator)))
            except Exception:
                try:
                    v = float(h.data.at(s))
                except Exception:
                    continue
            if best_val is None or v < best_val - 1e-15:
                best_val, best_src = v, f"{h.name}: {h.data.expr}"
        qrh = "0 (QRH: no zeros)" if s > QRH_EDGE else "unchanged"
        print(f"sigma={float(s):.5f}  A_best={best_val:.5f}  [{best_src}]  QRH: {qrh}")


if __name__ == "__main__":
    unc, qrh = part_mu() if ("mu" in PARTS or "zd" in PARTS) else (None, None)
    if "zd" in PARTS:
        part_zd(unc, qrh)
    if "best" in PARTS:
        part_best()
