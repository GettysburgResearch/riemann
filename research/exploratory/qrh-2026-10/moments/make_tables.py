"""
make_tables.py -- markdown tables from results/moments.json, results/diag.json
(and results/balanced.json if present).  EMPIRICAL post-processing only.

Usage: python3 -I make_tables.py [results_dir] > results/tables.md
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RD = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "results")
CLS = ("sixth", "cube", "square", "generic")


def load(name):
    p = os.path.join(RD, name)
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def Ek(d, k):
    """Diagonal E_k(D) with source tag and relative standard error."""
    if k == 1:
        return d["E1"], "ex", 0.0
    if k == 2 and "E2_exact" in d:
        return d["E2_exact"], "ex", 0.0
    if k == 3 and "E3_exact" in d:
        return d["E3_exact"], "ex", 0.0
    m, s = d["mc"][str(k)]
    return m, "mc", s / m


def fit(xs, ys):
    n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx


def main():
    mo = load("moments.json")
    dg = load("diag.json")
    dd = {r["D"]: r for r in dg["results"]}
    res = [r for r in mo["results"] if r["D"] in dd]
    labels = []
    for r in res:
        for h in r["per_H"]:
            if h["label"] not in labels:
                labels.append(h["label"])
    print("## Diagonal constants\n")
    print("E_k(D) = sum_r c_k(r)^2 prod_{p|r}(1-1/Np) (ex = exact grouping, mc = 10^6-sample random model, "
          "relative s.e. in brackets); Gaussian reference k! E_1^k.\n")
    print("| D | #n | E_1/D | E_2/(2E_1^2) | E_3/(6E_1^3) | E_4/(24E_1^4) (mc) | |A_1|/sqrt(E_1) |")
    print("|---|---|---|---|---|---|---|")
    for r in res:
        d = dd[r["D"]]
        e1 = d["E1"]
        e2, t2, s2 = Ek(d, 2)
        e3, t3, s3 = Ek(d, 3)
        e4, _, s4 = Ek(d, 4)
        a1 = math.hypot(*r["A1"])
        print(f"| {r['D']} | {r['n_count']} | {e1/r['D']:.4f} | {e2/(2*e1**2):.4f} ({t2}) | "
              f"{e3/(6*e1**3):.4f} ({t3}{'' if t3=='ex' else f' {s3:.1%}'}) | {e4/(24*e1**4):.3f} ({s4:.1%}) | {a1/math.sqrt(e1):.3f} |")
    for k in (1, 2, 3):
        print(f"\n## Ratio M_{2*k}(D,H) / diag_{2*k}(D,H),  diag = L0(H) E_{k}(D)\n")
        print("| D | " + " | ".join(labels) + " |")
        print("|---|" + "---|" * len(labels))
        for r in res:
            d = dd[r["D"]]
            e, tag, se = Ek(d, k)
            cells = []
            hm = {h["label"]: h for h in r["per_H"]}
            for lab in labels:
                if lab in hm:
                    h = hm[lab]
                    cells.append(f"{h['M'][str(k)] / (h['n_u'] * e):.4f}")
                else:
                    cells.append("")
            print(f"| {r['D']} | " + " | ".join(cells) + f" |{' (E mc, s.e. %.1f%%)' % (100*se) if tag == 'mc' else ''}")
    for k in (2, 3):
        print(f"\n## Gaussian-normalised per-row moment: M_{2*k} / (L0(H) {math.factorial(k)} E_1^{k})\n")
        print("| D | " + " | ".join(labels) + " |")
        print("|---|" + "---|" * len(labels))
        for r in res:
            d = dd[r["D"]]
            hm = {h["label"]: h for h in r["per_H"]}
            cells = [f"{hm[l]['M'][str(k)] / (hm[l]['n_u'] * math.factorial(k) * d['E1']**k):.4f}" if l in hm else ""
                     for l in labels]
            print(f"| {r['D']} | " + " | ".join(cells) + " |")
    print("\n## Fitted exponents in D (least squares over the listed D range)\n")
    print("alpha_k: slope of log M_{2k}(D, H(D)); target k+h with H = D^h. "
          "beta_k: slope of log(M_{2k}/diag_{2k}).\n")
    print("| H | D range | " + " | ".join(f"alpha_{k} - (k+h) | beta_{k}" for k in (1, 2, 3)) + " |")
    print("|---|---|" + "---|---|" * 3)
    for lab in labels:
        h = 2.0 if lab == "H=D^2" else 1 + float(lab.split("=")[1])
        allrows = [(r, {x["label"]: x for x in r["per_H"]}[lab]) for r in res
                   if lab in {x["label"] for x in r["per_H"]}]
        for dmin in (0, 4000):
            rows = [(r, x) for r, x in allrows if r["D"] >= dmin]
            if len(rows) < 3:
                continue
            xs = [math.log(r["D"]) for r, _ in rows]
            cells = []
            for k in (1, 2, 3):
                ys = [math.log(x["M"][str(k)]) for _, x in rows]
                yr = [math.log(x["M"][str(k)] / (x["n_u"] * Ek(dd[r["D"]], k)[0])) for r, x in rows]
                cells.append(f"{fit(xs, ys) - (k + h):+.3f} | {fit(xs, yr):+.3f}")
            print(f"| {lab} | {rows[0][0]['D']}-{rows[-1][0]['D']} | " + " | ".join(cells) + " |")
    print("\n## Row-class decomposition\n")
    print("share = class contribution / M_{2k}; per-row = (class mean of |A_u|^{2k}) / (generic-row mean); "
          "max = max |A_u|^2 / E_1 in the class.\n")
    print("| D | H | class | #u | share k=1 | share k=2 | share k=3 | per-row k=1 | per-row k=2 | per-row k=3 | max |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for r in res:
        if r["D"] not in (1000, 4000, 5657, 16000, 32000, 64000):
            continue
        d = dd[r["D"]]
        for h in r["per_H"]:
            if h["label"] not in ("theta=0.1", "theta=0.25", "H=D^2", "theta=0.5"):
                continue
            g = h["by_class"]["generic"]
            for c in CLS + ("rational",):
                bc = h["by_class"][c]
                if bc["n_u"] == 0:
                    continue
                sh = [bc["M"][str(k)] / h["M"][str(k)] for k in (1, 2, 3)]
                pr = [(bc["M"][str(k)] / bc["n_u"]) / (g["M"][str(k)] / g["n_u"]) for k in (1, 2, 3)]
                print(f"| {r['D']} | {h['label']} | {c} | {bc['n_u']} | " + " | ".join(f"{x:.2e}" for x in sh)
                      + " | " + " | ".join(f"{x:.3f}" for x in pr) + f" | {bc['max_abs2']/d['E1']:.2f} |")
    bal = load("balanced.json")
    if bal:
        print("\n## Balanced-divisor mean square (PR 910, eq. 3.5) on the actual sextic symbols\n")
        print(f"(brute-force check of the column construction: max error {bal['brute_check_err']:.1e})\n")
        print("| D | X | N(c) | #cols r | theta | sum_u |B|^2 / (H X^2) | / diag | E|B|^4/(E|B|^2)^2 |")
        print("|---|---|---|---|---|---|---|---|")
        for r in bal["results"]:
            for q in r["per_H"]:
                print(f"| {r['D']} | {r['X']:.0f} | {r['Nc']} | {r['n_columns']} | {q['theta']:g} | "
                      f"{q['ms_over_HX2']:.4f} | {q['ms_over_diag']:.4f} | {q['m4_over_m2sq']:.3f} |")


if __name__ == "__main__":
    main()
