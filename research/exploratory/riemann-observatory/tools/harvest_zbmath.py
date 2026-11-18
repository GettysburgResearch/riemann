#!/usr/bin/env python3
"""Harvest zbMATH Open records for the Riemann Observatory candidate pool.

Usage: python3 harvest_zbmath.py OUTDIR
Writes one JSONL file per query (raw zbMATH API records) and a manifest.
Only public zbMATH Open API endpoints are used (https://api.zbmath.org/v1).
"""
import json, os, sys, time, urllib.parse, urllib.request

API = "https://api.zbmath.org/v1/document/_search"
QUERIES = {
    # core RH / zeta zero material
    "msc_11M26": "cc:11M26",
    "msc_11M06": "cc:11M06",
    "msc_11M50": "cc:11M50",
    "msc_11M45": "cc:11M45",
    "msc_11M20": "cc:11M20",
    "msc_11Y35": "cc:11Y35",
    "msc_11M36": "cc:11M36",
    "msc_11N05": "cc:11N05",
    "msc_11N56_rh": "cc:11N56 & any:\"Riemann\"",
    "kw_RH_any": "any:\"Riemann hypothesis\"",
    "kw_zeta_zeros": "any:\"zeros of the Riemann zeta\"",
    "kw_deBranges": "any:\"de Branges\" & any:zeta",
    "kw_trace_formula_zeta": "any:\"trace formula\" & any:\"Riemann zeta\"",
    "kw_li_criterion": "any:\"Li coefficients\"",
    "kw_nyman": "any:\"Nyman\" | any:\"Baez-Duarte\"",
    "kw_robin": "any:\"Robin inequality\" | any:\"Robin's inequality\" | any:\"colossally abundant\"",
    "kw_weil_positivity": "any:\"Weil positivity\" | any:\"Weil's explicit formula\" | any:\"explicit formula\" & cc:11M",
    "kw_debruijn_newman": "any:\"de Bruijn-Newman\" | any:\"Newman's conjecture\"",
    "kw_pair_correlation": "any:\"pair correlation\" & cc:11M",
    "kw_zero_density": "any:\"zero density\" | any:\"zero-density\"",
    "kw_zero_free": "any:\"zero-free region\" | any:\"zero free region\"",
    "kw_moments_zeta": "any:\"moments of the Riemann zeta\" | any:\"mean value\" & cc:11M06",
    "kw_hilbert_polya": "any:\"Hilbert-Polya\" | any:\"Hilbert-Pólya\" | any:\"Polya-Hilbert\"",
    "kw_laguerre_polya_xi": "any:\"Laguerre-Polya\" & any:zeta | any:\"Jensen polynomials\" & any:zeta",
    "kw_function_field_rh": "any:\"Riemann hypothesis for curves\" | any:\"Weil conjectures\"",
    "kw_selberg_class": "any:\"Selberg class\"",
    "kw_GRH": "any:\"generalized Riemann hypothesis\"",
}

def fetch(q, page, per=100, tries=5):
    params = urllib.parse.urlencode({"search_string": q, "results_per_page": per, "page": page})
    url = API + "?" + params
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "riemann-observatory-harvester/0.1"})
            with urllib.request.urlopen(req, timeout=90) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(3 * (t + 1))
            err = e
    raise RuntimeError(f"failed {q} p{page}: {err}")

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    manifest = {}
    for name, q in QUERIES.items():
        path = os.path.join(outdir, name + ".jsonl")
        if os.path.exists(path + ".done"):
            manifest[name] = json.load(open(path + ".done"))
            continue
        page, n_written, total = 0, 0, None
        with open(path, "w") as f:
            while True:
                d = fetch(q, page)
                total = d["status"]["nr_total_results"]
                res = d.get("result") or []
                for r in res:
                    f.write(json.dumps(r, ensure_ascii=False) + "\n")
                n_written += len(res)
                if not res or n_written >= (total or 0):
                    break
                page += 1
                time.sleep(0.4)
        info = {"query": q, "total": total, "written": n_written,
                "harvested_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        json.dump(info, open(path + ".done", "w"))
        manifest[name] = info
        print(name, info, flush=True)
    json.dump(manifest, open(os.path.join(outdir, "MANIFEST.json"), "w"), indent=1)

if __name__ == "__main__":
    main(sys.argv[1])
