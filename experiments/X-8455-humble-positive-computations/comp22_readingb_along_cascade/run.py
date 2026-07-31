#!/usr/bin/env python3
"""C22 — opposite-sign Reading-B screen along the Φ cascade.

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Walk α through precursor and deficit jumps; record whether B_p isotropic cone
is nontrivial. Invitation: does Reading B open exactly when Loewner goes negative,
or earlier at the p±2 flip?
"""

from __future__ import annotations

import hashlib
import random
import sys
from fractions import Fraction as F
from pathlib import Path

from mpmath import mp, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from phi_xi import Fwin, Phi  # noqa: E402
from linalg_q import quadratic  # noqa: E402
from jsonutil import dumps as json_dumps  # noqa: E402

mp.dps = 35
OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)


def Bp(p):
    n = len(p)
    return [[(F(1) / p[i] if i == j else F(0)) - F(1) for j in range(n)] for i in range(n)]


def cone_screen(p, trials=250, seed=22):
    random.seed(seed)
    n = len(p)
    pos = neg = 0
    for _ in range(trials):
        x = [F(random.randint(-7, 7)) for _ in range(n)]
        if p[-1] == 0:
            continue
        x[-1] = -sum(x[i] * p[i] for i in range(n - 1)) / p[-1]
        if all(v == 0 for v in x):
            continue
        q = quadratic(Bp(p), x)
        if q > 0:
            pos += 1
        elif q < 0:
            neg += 1
        if pos and neg:
            break
    return {"has_pos": pos > 0, "has_neg": neg > 0, "nontrivial": pos > 0 and neg > 0, "pos": pos, "neg": neg}


def main():
    print("=== C22 Reading-B along cascade ===", flush=True)
    rows = []
    for N in (4, 6):
        for alpha in [1.02, 1.00, 0.9975, 0.995, 0.99, 0.98, 0.975, 0.97, 0.96]:
            nodes = list(range(-N, N + 1))
            vals = [((-1) ** j) * Fwin(alpha, j, Phi) for j in nodes]
            p = [F(nstr(v, 24, strip_zeros=False)) for v in vals]
            s = sum(p)
            pn = [v / s for v in p]
            scr = cone_screen(pn)
            # deficit light
            import sympy as sp

            ssym = sp.symbols("s")
            P = 0
            for i, lam in enumerate(nodes):
                term = 1
                for mu in nodes:
                    if mu != lam:
                        term *= mu - ssym
                P += sp.Rational(p[i]) * term
            P = sp.Poly(sp.expand(P), ssym)
            deg = int(P.degree())
            g = sp.gcd(P, P.diff())
            nre = int(sp.Poly(P.quo(g), ssym).count_roots())
            row = {
                "alpha": alpha,
                "N": N,
                "deficit": deg - nre,
                "p2": float(vals[nodes.index(2)]),
                "cone": scr,
            }
            rows.append(row)
            print(row, flush=True)

    payload = {
        "schema": "riemann.x8455.comp22.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Random rational isotropic probes; not L-15109 thresholds.",
        "rows": rows,
        "suggested_questions_for_other_agents": [
            "Does cone.nontrivial ever become true on the pass side of the deficit jump?",
            "If cone stays one-sided through α*, Reading B may still be open while Sturm passes.",
        ],
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "comp22.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "comp22.txt").write_text(
        "\n".join(
            f"N={r['N']} a={r['alpha']} def={r['deficit']} nontrivial={r['cone']['nontrivial']} p2={r['p2']:.3e}"
            for r in rows
        )
        + "\n"
    )
    print("wrote", OUT / "comp22.json", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
