#!/usr/bin/env python3
"""D4 — N³(α_∞ − α_N) law from D3 (and C41 comparison).

Agent: cursor-grok-8455
Status: EMPIRICAL / EXPLORATORY

Review prediction:
  α_∞ − α_N  ~  0.1866219902712081 / N³
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "shared"))
from jsonutil import dumps as json_dumps  # noqa: E402

OUT = Path(__file__).resolve().parent / "results"
OUT.mkdir(parents=True, exist_ok=True)

A_INF = mpf("0.975779528461603467680421342178")
C_PRED = mpf("0.1866219902712081")
D3 = ROOT / "comp3_finite_RR" / "results" / "d3.json"

# fallback C41 odd-eig α_def if D3 not ready
C41_FALLBACK = {
    4: "0.9734385944092645",
    5: "0.9745642049359158",
    6: "0.9750627888059245",
    8: "0.9754669242082166",
    10: "0.9756154785668478",
    12: "0.9756828425684942",
    14: "0.9757177899479865",
    16: "0.9757377163767813",
    18: "0.9757499055266381",
    20: "0.975757779300213",
}


def main():
    print("=== D4 N^3 law ===", flush=True)
    mp.dps = 50
    source = "fallback_C41_odd_eig"
    alphas = dict(C41_FALLBACK)
    if D3.exists():
        d3 = json.loads(D3.read_text())
        alphas = {int(r["N"]): r["alpha_str"] for r in d3["rows"]}
        source = "D3_finite_RR"

    rows = []
    for N in sorted(alphas):
        a = mpf(alphas[N])
        gap = A_INF - a
        n3g = gap * (N ** 3)
        rows.append(
            {
                "N": N,
                "alpha": nstr(a, 25),
                "gap": nstr(gap, 20),
                "N3_gap": nstr(n3g, 20),
                "N3_gap_over_Cpred": nstr(n3g / C_PRED, 20),
                "abs_diff_to_Cpred": nstr(abs(n3g - C_PRED), 20),
            }
        )
        print(
            f"N={N} gap={nstr(gap,12)} N3*gap={nstr(n3g,15)} "
            f"ratio/C={nstr(n3g/C_PRED,12)}",
            flush=True,
        )

    # fit constant from largest N's
    big = [mpf(r["N3_gap"]) for r in rows if r["N"] >= 10]
    mean_big = sum(big) / len(big)
    payload = {
        "schema": "riemann.x8455.d4.v1",
        "status": "EMPIRICAL_PROVISIONAL",
        "disclaimer": "Uses discovery alpha_N; asymptotic constant is analytic prediction.",
        "source_alphas": source,
        "alpha_infinity": nstr(A_INF, 30),
        "C_predicted": nstr(C_PRED, 20),
        "rows": rows,
        "mean_N3_gap_Nge10": nstr(mean_big, 20),
        "note": "Ratio N3_gap/Cpred should approach 1 as N→∞ if the linearization is sharp.",
    }
    text = json_dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["content_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    (OUT / "d4.json").write_text(json_dumps(payload, indent=2, sort_keys=True) + "\n")
    (OUT / "d4.txt").write_text(
        "\n".join(f"N={r['N']} N3*gap={r['N3_gap']} ratio={r['N3_gap_over_Cpred']}" for r in rows) + "\n"
    )
    print("mean_Nge10", nstr(mean_big, 15), "Cpred", nstr(C_PRED, 15), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
