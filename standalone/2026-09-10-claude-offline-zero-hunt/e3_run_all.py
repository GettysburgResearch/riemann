"""Run E3 over several test-function families; collect certified verdicts."""
import sys, time
sys.path.insert(0, '.')
from e3_weil_form import run
from common import write_json

CONFIGS = [
    ("d0.25_N32",  32, 0.25,  1400),
    ("d0.25_N48",  48, 0.25,  1600),
    ("d0.125_N96", 96, 0.125, 2000),
    ("d0.5_N24",   24, 0.5,   1400),
]
out = {"configs": [], "any_RH_refuted": False}
for label, N, d, prec in CONFIGS:
    t0 = time.time()
    try:
        r = run(N, d, prec, False); r["label"] = label; r.pop("tau", None)
        out["configs"].append(r)
        out["any_RH_refuted"] = out["any_RH_refuted"] or r["RH_REFUTED"]
        mp = r["min_pivot"]
        print(f"{label}: A={r['A_support']:.3f} cutoff={r['prime_cutoff']} "
              f"LDLT={r['ldlt_status']} minPivot={mp['mid']:.4e}+/-{mp['rad']:.1e} "
              f"minEigFloat={r['float_eigenvalues_min5'][0]:.4e} "
              f"refuted={r['RH_REFUTED']} ({time.time()-t0:.0f}s)", flush=True)
    except Exception as e:
        print(f"{label}: FAILED {type(e).__name__}: {e}", flush=True)
        out["configs"].append({"label": label, "error": f"{type(e).__name__}: {e}"})
    write_json("results/e3_weil.json", out)
print("\nany certified RH refutation:", out["any_RH_refuted"])
