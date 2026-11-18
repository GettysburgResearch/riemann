#!/usr/bin/env python3
"""Look up published corrections/errata/retractions for DOIs via Crossref's `updates:` filter,
plus basic metadata (is-referenced-by-count, container, issued date).
Usage: python3 crossref_updates.py DOIS.txt OUT.jsonl   (one DOI per line; resumable)"""
import json, sys, time, os, urllib.parse, urllib.request
UA = {"User-Agent": "riemann-observatory/0.1 (literature archive)"}
def get(url):
    for t in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return json.load(r)
        except Exception as e:
            if "404" in str(e):
                return None
            time.sleep(2 * (t + 1))
    return None
dois = [l.strip() for l in open(sys.argv[1]) if l.strip()]
done = set()
if os.path.exists(sys.argv[2]):
    done = {json.loads(l)["doi"] for l in open(sys.argv[2])}
with open(sys.argv[2], "a") as f:
    for d in dois:
        if d in done:
            continue
        meta = get("https://api.crossref.org/works/" + urllib.parse.quote(d))
        m = (meta or {}).get("message") or {}
        ups = get("https://api.crossref.org/works?" + urllib.parse.urlencode({"filter": f"updates:{d}", "rows": 20}))
        items = ((ups or {}).get("message") or {}).get("items") or []
        rec = {"doi": d, "found": bool(m), "title": (m.get("title") or [""])[0], "container": (m.get("container-title") or [""])[0],
               "issued": ((m.get("issued") or {}).get("date-parts") or [[None]])[0], "is_referenced_by_count": m.get("is-referenced-by-count"),
               "type": m.get("type"), "relation": m.get("relation") or {},
               "updates": [{"doi": it.get("DOI"), "title": (it.get("title") or [""])[0],
                            "update_type": [u.get("type") for u in it.get("update-to") or [] if (u.get("DOI") or "").lower() == d.lower()],
                            "issued": ((it.get("issued") or {}).get("date-parts") or [[None]])[0]} for it in items]}
        f.write(json.dumps(rec, ensure_ascii=False) + "\n"); f.flush()
        time.sleep(0.25)
