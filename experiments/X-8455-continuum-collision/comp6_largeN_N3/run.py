#!/usr/bin/env python3
"""D6 — push finite double-root α_N to larger N for the N^{-3} constant."""
from __future__ import annotations
import hashlib, sys
from pathlib import Path
from mpmath import mp, mpf, nstr
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"shared"))
from collision import solve_finite
from jsonutil import dumps as json_dumps
OUT = Path(__file__).resolve().parent/"results"; OUT.mkdir(parents=True, exist_ok=True)
A_INF = mpf("0.975779528461603467680421342178")
C_PRED = mpf("0.1866219902712081")
# include prior D3 + new
PRIOR = {
 4:"0.9734385944090738626887126", 5:"0.9745642049361370336202833",
 6:"0.97506278881038202524629", 8:"0.9754669242022649946505486",
 10:"0.975615478563899622063933", 12:"0.9756828425723639821646444",
 14:"0.975717789951026039023817", 16:"0.9757377165721523329774872",
 18:"0.9757499057381845851823018", 20:"0.9757577790384711619878619",
}
def main():
    print("=== D6 larger-N double roots ===", flush=True)
    rows=[]
    for N,a in PRIOR.items():
        a=mpf(a); gap=A_INF-a; n3=gap*(N**3)
        rows.append({"N":N,"alpha":nstr(a,25),"source":"D3","N3_gap":nstr(n3,18),"ratio":nstr(n3/C_PRED,12)})
    for N in (24, 30, 40):
        # seed by asymptotic
        a0 = float(A_INF - C_PRED/(N**3))
        r0 = 2.1795
        print(f"solving N={N} seed_a={a0}", flush=True)
        sol = solve_finite(N, a0, r0, dps=40, maxsteps=50)
        a=sol["alpha"]; gap=A_INF-a; n3=gap*(N**3)
        row={"N":N,"alpha":sol["alpha_str"],"r":sol["r_str"],"R":sol["R"],"R_r":sol["R_r"],
             "source":"D6","N3_gap":nstr(n3,18),"ratio":nstr(n3/C_PRED,12)}
        rows.append(row)
        print(f"N={N} a={sol['alpha_str']} r={sol['r_str']} N3*gap={nstr(n3,15)} ratio={nstr(n3/C_PRED,12)}", flush=True)
    payload={"schema":"riemann.x8455.d6.v1","status":"EMPIRICAL_PROVISIONAL",
             "C_predicted":nstr(C_PRED,20),"rows":rows}
    text=json_dumps(payload,indent=2,sort_keys=True)+"\n"
    payload["content_sha256"]=hashlib.sha256(text.encode()).hexdigest()
    (OUT/"d6.json").write_text(json_dumps(payload,indent=2,sort_keys=True)+"\n")
    (OUT/"d6.txt").write_text("\n".join(f"N={r['N']} N3*gap={r['N3_gap']} ratio={r['ratio']}" for r in rows)+"\n")
    print("wrote", OUT/"d6.json", flush=True)
    return 0
if __name__=="__main__":
    raise SystemExit(main())
