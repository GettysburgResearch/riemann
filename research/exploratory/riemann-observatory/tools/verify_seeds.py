#!/usr/bin/env python3
"""Level-0 verification of expert seed works.

Each seed (title, authors, year) is matched, in order, against
  1. the harvested pool (pool.jsonl) by normalized-title similarity + surname + year window,
  2. the zbMATH Open API (ti: + au: query),
  3. Crossref (query.bibliographic),
  4. arXiv (ti: query) for post-1991 works.
A seed is VERIFIED only if a record with similar title (token-set Jaccard >= 0.6, or containment >= 0.85),
a matching first-author surname, and |year difference| <= 2 is found.
Usage: python3 verify_seeds.py SEEDS_JSONL POOL_JSONL OUT_JSONL
"""
import json, re, sys, time, unicodedata, urllib.parse, urllib.request, os

UA = {"User-Agent": "riemann-observatory/0.1 (literature archive; mailto not provided)"}

def norm(t):
    t = unicodedata.normalize("NFKD", t or "").encode("ascii", "ignore").decode().lower()
    t = re.sub(r"\\[a-z]+", " ", t)
    return re.sub(r"[^a-z0-9]+", " ", t).strip()

STOP = set("the of a an and on in for to with its der die das und von zur uber ueber sur la le les des du de et une un".split())

def toks(t):
    return {w for w in norm(t).split() if w not in STOP and len(w) > 1}

def sim(a, b):
    A, B = toks(a), toks(b)
    if not A or not B:
        return 0.0
    j = len(A & B) / len(A | B)
    c = len(A & B) / min(len(A), len(B))
    return max(j, 0.0 if min(len(A), len(B)) < 3 else (c if c >= 0.85 else 0))

def surname(a):
    a = norm(a.split(",")[0] if "," in a else a.split()[-1] if a.split() else a)
    return a.split()[-1] if a else ""

def year_ok(y1, y2, w=2):
    try:
        return abs(int(y1) - int(y2)) <= w
    except Exception:
        return False

def get_json(url, tries=3):
    for t in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 * (t + 1))
    return None

def match_pool(seed, index):
    sn = surname(seed["authors"][0]) if seed.get("authors") else ""
    best = None
    for p in index.get(sn, []):
        if not year_ok(seed.get("year"), p.get("year"), 3):
            continue
        s = max(sim(seed["title"], p.get("title", "")), sim(seed["title"], p.get("title_original", "")),
                sim(seed.get("title_en") or "", p.get("title", "")))
        if s >= 0.6 and (best is None or s > best[0]):
            best = (s, p)
    return best

def match_zbmath(seed):
    sn = surname(seed["authors"][0]) if seed.get("authors") else ""
    words = [w for w in norm(seed["title"]).split() if w not in STOP][:6]
    if not words:
        return None
    q = "ti:" + " ".join(words) + (f" & au:{sn}" if sn else "")
    url = "https://api.zbmath.org/v1/document/_search?" + urllib.parse.urlencode({"search_string": q, "results_per_page": 10})
    d = get_json(url)
    for r in (d or {}).get("result") or []:
        t = (r.get("title") or {})
        title = t.get("title") or ""
        s = max(sim(seed["title"], title), sim(seed["title"], t.get("original") or ""), sim(seed.get("title_en") or "", title))
        auth = [a.get("name", "") for a in (r.get("contributors") or {}).get("authors", [])]
        if s >= 0.6 and year_ok(seed.get("year"), r.get("year")) and (not sn or any(sn == surname(a) for a in auth)):
            links = r.get("links") or []
            return {"source": "zbmath_api", "zbmath_id": r["id"], "zbl": r.get("identifier"), "matched_title": title,
                    "year": r.get("year"), "doi": next((l["identifier"] for l in links if l.get("type") == "doi"), ""),
                    "arxiv": next((l["identifier"] for l in links if l.get("type") == "arxiv"), ""), "score": round(s, 2),
                    "raw": r}
    return None

def match_crossref(seed):
    sn = surname(seed["authors"][0]) if seed.get("authors") else ""
    q = f"{seed['title']} {sn} {seed.get('year', '')}"
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": q, "rows": 5})
    d = get_json(url)
    for it in ((d or {}).get("message") or {}).get("items", []):
        title = (it.get("title") or [""])[0]
        y = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        fams = [norm(a.get("family", "")) for a in it.get("author") or []]
        s = sim(seed["title"], title)
        if s >= 0.6 and year_ok(seed.get("year"), y) and (not sn or sn in fams or not fams):
            return {"source": "crossref", "doi": it.get("DOI"), "matched_title": title, "year": y,
                    "venue": (it.get("container-title") or [""])[0], "score": round(s, 2),
                    "is_referenced_by_count": it.get("is-referenced-by-count")}
    return None

def match_arxiv(seed):
    words = [w for w in norm(seed["title"]).split() if w not in STOP][:7]
    q = " AND ".join(f"ti:{w}" for w in words)
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "max_results": 5})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
            xml = r.read().decode()
    except Exception:
        return None
    time.sleep(3.2)
    for m in re.finditer(r"<entry>(.*?)</entry>", xml, re.S):
        e = m.group(1)
        title = " ".join(re.search(r"<title>(.*?)</title>", e, re.S).group(1).split())
        aid = re.search(r"<id>http://arxiv.org/abs/(.*?)</id>", e).group(1)
        pub = re.search(r"<published>(\d{4})", e).group(1)
        s = sim(seed["title"], title)
        if s >= 0.6 and year_ok(seed.get("year"), pub, 3):
            return {"source": "arxiv_api", "arxiv": re.sub(r"v\d+$", "", aid), "matched_title": title, "year": pub, "score": round(s, 2)}
    return None

def main(seeds_path, pool_path, out_path):
    pool = [json.loads(l) for l in open(pool_path)]
    index = {}
    for p in pool:
        for a in p.get("authors") or []:
            index.setdefault(surname(a), []).append(p)
    seeds = [json.loads(l) for l in open(seeds_path)]
    done = set()
    if os.path.exists(out_path):
        done = {json.loads(l)["seed_id"] for l in open(out_path)}
    with open(out_path, "a") as f:
        for s in seeds:
            if s["seed_id"] in done:
                continue
            res = {"seed_id": s["seed_id"], "status": "unverified"}
            m = match_pool(s, index)
            if m:
                res.update(status="verified", source="pool", pool_key=m[1]["key"], score=round(m[0], 2), matched_title=m[1]["title"])
            else:
                z = match_zbmath(s); time.sleep(0.3)
                if z:
                    res.update(status="verified", **{k: v for k, v in z.items()})
                else:
                    c = match_crossref(s); time.sleep(0.3)
                    if c:
                        res.update(status="verified", **c)
                    elif str(s.get("year", "0")).isdigit() and int(s.get("year", 0)) >= 1991:
                        a = match_arxiv(s)
                        if a:
                            res.update(status="verified", **a)
            f.write(json.dumps(res, ensure_ascii=False) + "\n"); f.flush()

if __name__ == "__main__":
    main(*sys.argv[1:4])
