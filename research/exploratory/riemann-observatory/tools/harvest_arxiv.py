#!/usr/bin/env python3
"""Harvest arXiv metadata (Atom API) for the Riemann Observatory candidate pool.
Usage: python3 harvest_arxiv.py OUTDIR    (polite: 3.5 s between requests)
"""
import json, os, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
API = "https://export.arxiv.org/api/query"
NS = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
QUERIES = {
    "rh_abs": 'abs:"Riemann hypothesis"',
    "rh_ti": 'ti:"Riemann hypothesis"',
    "zeta_zeros": 'abs:"zeros of the Riemann zeta"',
    "zeta_zeros2": 'abs:"zeros of zeta" AND cat:math.NT',
    "critical_line": 'abs:"critical line" AND cat:math.NT',
    "zero_density": 'abs:"zero density" OR abs:"zero-density"',
    "zero_free": 'abs:"zero-free region"',
    "debruijn_newman": 'abs:"de Bruijn-Newman" OR abs:"de Bruijn--Newman"',
    "li_criterion": 'abs:"Li coefficients" OR abs:"Li criterion" OR abs:"Keiper-Li"',
    "nyman_beurling": 'abs:"Nyman" AND abs:"Beurling"',
    "robin": 'abs:"Robin inequality" OR abs:"Robin\'s inequality" OR abs:"colossally abundant"',
    "weil_explicit": 'abs:"Weil explicit formula" OR abs:"Weil positivity" OR abs:"Weil\'s positivity"',
    "hilbert_polya": 'abs:"Hilbert-Polya" OR abs:"Polya-Hilbert" OR abs:"Hilbert--Polya"',
    "berry_keating": 'abs:"Berry-Keating" OR abs:"xp Hamiltonian"',
    "de_branges": 'abs:"de Branges" AND abs:zeta',
    "pair_corr": 'abs:"pair correlation" AND abs:zeta',
    "moments_zeta": 'abs:"moments of the Riemann zeta" OR abs:"moments of zeta"',
    "random_matrix_zeta": 'abs:"random matrix" AND abs:"zeta function" AND cat:math.NT',
    "jensen_poly": 'abs:"Jensen polynomials" OR abs:"Turan inequalities" AND abs:zeta',
    "explicit_formula": 'abs:"explicit formula" AND cat:math.NT',
    "mollifier": 'abs:mollifier AND abs:zeta',
    "selberg_class": 'abs:"Selberg class"',
    "grh": 'abs:"generalized Riemann hypothesis" AND cat:math.NT',
    "large_values_dirichlet": 'abs:"large values" AND abs:"Dirichlet polynomial"',
    "verification_zeros": 'abs:"verification of the Riemann hypothesis" OR abs:"Riemann hypothesis is true up to"',
    "connes_rh": 'abs:Connes AND abs:"Riemann hypothesis"',
    "function_field_rh": 'abs:"Riemann hypothesis" AND abs:"function field"',
    "mertens_conj": 'abs:"Mertens conjecture" OR abs:"Mertens function"',
    "universality_zeta": 'abs:universality AND abs:"Riemann zeta"',
    "zeta_extreme": 'abs:"extreme values" AND abs:zeta',
}
def fetch(q, start, n=500, tries=6):
    url = API + "?" + urllib.parse.urlencode({"search_query": q, "start": start, "max_results": n,
                                              "sortBy": "submittedDate", "sortOrder": "ascending"})
    for t in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "riemann-observatory/0.1"}), timeout=120) as r:
                return r.read()
        except Exception as e:
            err = e; time.sleep(10 * (t + 1))
    raise RuntimeError(f"{q} {start}: {err}")
def parse(xml):
    root = ET.fromstring(xml)
    tot = int(root.find("{http://a9.com/-/spec/opensearch/1.1/}totalResults").text)
    out = []
    for e in root.findall("a:entry", NS):
        g = lambda tag: (e.find(tag, NS).text or "").strip() if e.find(tag, NS) is not None else ""
        aid = g("a:id").rsplit("/abs/", 1)[-1]
        out.append({"arxiv_id": aid, "title": " ".join(g("a:title").split()), "summary": " ".join(g("a:summary").split()),
                    "published": g("a:published"), "updated": g("a:updated"),
                    "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
                    "doi": g("arxiv:doi"), "journal_ref": g("arxiv:journal_ref"), "comment": g("arxiv:comment"),
                    "primary_category": (e.find("arxiv:primary_category", NS).attrib.get("term") if e.find("arxiv:primary_category", NS) is not None else ""),
                    "categories": [c.attrib.get("term") for c in e.findall("a:category", NS)]})
    return tot, out
def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    for name, q in QUERIES.items():
        path = os.path.join(outdir, name + ".jsonl")
        if os.path.exists(path + ".done"): continue
        start, tot, rows = 0, None, []
        while True:
            tot, out = parse(fetch(q, start))
            rows += out
            time.sleep(3.5)
            if not out or len(rows) >= tot or start > 4000: break
            start += len(out)
        with open(path, "w") as f:
            for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
        json.dump({"query": q, "total": tot, "written": len(rows), "harvested_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, open(path + ".done", "w"))
        print(name, tot, len(rows), flush=True)
if __name__ == "__main__":
    main(sys.argv[1])
