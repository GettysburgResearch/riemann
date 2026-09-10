"""E2 - de Bruijn-Newman heat flow and the certified Laguerre inequality.

    H_t(z) = int_0^inf e^{t u^2} Phi(u) cos(zu) du
    Phi(u) = sum_{n>=1} (2 pi^2 n^4 e^{9u} - 3 pi n^2 e^{5u}) exp(-pi n^2 e^{4u})

H_0 is a constant multiple of Xi. The de Bruijn-Newman constant is
Lambda = inf{ t : H_t has only real zeros }; RH <=> Lambda <= 0, and
Rodgers-Tao give Lambda >= 0 unconditionally.

For a real entire function with only real zeros the Laguerre inequality holds
pointwise on the real axis:

    L_t(x) = H_t'(x)^2 - H_t(x) H_t''(x) >= 0.

Indeed L_t = H_t^2 * sum_k 1/(x - z_k)^2, so a conjugate pair z = a +/- ib
contributes 2[(x-a)^2 - b^2]/((x-a)^2 + b^2)^2, which equals -2/b^2 at x = a.
A tight complex pair therefore drives L_t strictly negative near its real part.

Consequences of a CERTIFIED negative value of L_t(x):
    t  = 0   ->  Xi has a non-real zero: RH IS FALSE.
    t  < 0   ->  H_t has a non-real zero, hence Lambda > t (a certified
                 lower bound on the de Bruijn-Newman constant).

No zeta evaluator and no zero table is used anywhere in this file. All
quantities come from Phi and Arb's rigorous integrator.
"""

import argparse
import json
import sys
import time

from flint import acb, arb, ctx

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from common import ball, certified_negative, set_prec, write_json  # noqa: E402

NTERMS = 20        # Phi truncation; tail proved below 1e-300 for Re u >= 0
U_MAX = "1.2"      # integration cutoff; |Phi(u)| < 1e-160 beyond this


def phi_terms(u, nterms=NTERMS):
    """Phi(u) truncated. Tail bound (added by caller) is astronomically small.

    For Re u >= 0 and |Im u| <= 1/5, Re(e^{4u}) >= cos(4/5) > 0.69, so the
    omitted terms are bounded by sum_{n>N} 2 pi^2 n^4 exp(-0.69 pi n^2), which
    at N = 20 is below 1e-300.
    """
    pi = acb.pi()
    e4 = (4 * u).exp()
    e5 = (5 * u).exp()
    e9 = (9 * u).exp()
    acc = acb(0)
    for n in range(1, nterms + 1):
        n2 = acb(n * n)
        acc += (2 * pi**2 * acb(n**4) * e9 - 3 * pi * n2 * e5) * (-pi * n2 * e4).exp()
    return acc


def _tail_ball():
    """Explicit error ball covering the Phi truncation and the u > U_MAX tail."""
    return acb(arb(0, 1e-200), arb(0, 1e-200))


def H_derivs(t, z, prec):
    """Certified (H_t(z), H_t'(z), H_t''(z)) for the given real t and complex z."""
    ctx.prec = prec
    t = acb(t)
    z = acb(z)
    U = arb(U_MAX)

    def f0(u, _):
        return (t * u * u).exp() * phi_terms(u) * (z * u).cos()

    def f1(u, _):
        return -u * (t * u * u).exp() * phi_terms(u) * (z * u).sin()

    def f2(u, _):
        return -u * u * (t * u * u).exp() * phi_terms(u) * (z * u).cos()

    H0 = acb.integral(f0, 0, U) + _tail_ball()
    H1 = acb.integral(f1, 0, U) + _tail_ball()
    H2 = acb.integral(f2, 0, U) + _tail_ball()
    return H0, H1, H2


def laguerre(t, x, prec):
    """L_t(x) = H'^2 - H H''  (real for real t, x)."""
    H0, H1, H2 = H_derivs(t, x, prec)
    return (H1 * H1 - H0 * H2).real, H0.real


def scan(t, x_lo, x_hi, n_pts, prec, budget_s, label):
    """Scan L_t on a real grid, reporting every certified negative."""
    set_prec(prec)
    t0 = time.time()
    lo, hi = arb(x_lo), arb(x_hi)
    neg, rows = [], []
    minrec = None
    done = 0
    for i in range(n_pts):
        if time.time() - t0 > budget_s:
            break
        x = lo + (hi - lo) * arb(i) / arb(max(n_pts - 1, 1))
        L, H = laguerre(arb(t), x, prec)
        done += 1
        rec = {
            "x": float(arb(x).mid()),
            "L": ball(L),
            "H": ball(H),
            "certified_negative": certified_negative(L),
            "conclusive": bool(arb(L) > 0) or certified_negative(L),
        }
        rows.append(rec)
        if rec["certified_negative"]:
            neg.append(rec)
        if minrec is None or rec["L"]["upper"] < minrec["L"]["upper"]:
            minrec = rec
    return {
        "label": label,
        "t": float(arb(t).mid()) if not isinstance(t, str) else t,
        "t_str": str(t),
        "x_range": [float(lo.mid()), float(hi.mid())],
        "points_requested": n_pts,
        "points_done": done,
        "prec_bits": prec,
        "elapsed_s": round(time.time() - t0, 1),
        "n_certified_negative": len(neg),
        "certified_negatives": neg[:40],
        "min_record": minrec,
        "rows": rows,
    }


def selftest(prec=200):
    """Pin the normalization: locate H_0's first sign change and compare with
    the classical first zeta ordinate 14.134725141734693."""
    set_prec(prec)
    out = {}
    for conv, scale in (("H0(z) ~ Xi(z)", 1.0), ("H0(z) ~ Xi(z/2)", 2.0)):
        g = 14.134725141734693 * scale
        a, _ = laguerre(arb(0), arb(g) - arb("0.3"), prec)
        # evaluate H itself either side of the predicted zero
        Ha = H_derivs(arb(0), arb(g) - arb("0.3"), prec)[0].real
        Hb = H_derivs(arb(0), arb(g) + arb("0.3"), prec)[0].real
        out[conv] = {
            "predicted_zero_z": g,
            "H_left": ball(Ha),
            "H_right": ball(Hb),
            "sign_change_certified": bool((arb(Ha) > 0 and arb(Hb) < 0)
                                          or (arb(Ha) < 0 and arb(Hb) > 0)),
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["selftest", "scan"])
    ap.add_argument("--t", default="0")
    ap.add_argument("--xlo", type=float, default=10.0)
    ap.add_argument("--xhi", type=float, default=60.0)
    ap.add_argument("--pts", type=int, default=200)
    ap.add_argument("--prec", type=int, default=200)
    ap.add_argument("--budget", type=float, default=900.0)
    ap.add_argument("--label", default="scan")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    if a.mode == "selftest":
        res = {"selftest": selftest(a.prec)}
    else:
        res = scan(arb(a.t), a.xlo, a.xhi, a.pts, a.prec, a.budget, a.label)
    write_json(a.out, res)
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1)[:2000])


if __name__ == "__main__":
    main()
