#!/usr/bin/env python3
"""Fetch zbMATH records by document id (backward citation expansion).
Usage: python3 fetch_zbmath_ids.py IDS_TSV OUT_JSONL [THREADS]   (IDS_TSV: id<TAB>count per line)"""
import json, sys, time, urllib.request, concurrent.futures, os
def get(i):
    for t in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://api.zbmath.org/v1/document/{i}", headers={"User-Agent": "riemann-observatory/0.1"}), timeout=90) as r:
                return json.load(r)["result"]
        except Exception:
            time.sleep(3 * (t + 1))
    return None
ids = [l.split("\t")[0] for l in open(sys.argv[1]) if l.strip()]
done = set()
if os.path.exists(sys.argv[2]):
    done = {str(json.loads(l)["id"]) for l in open(sys.argv[2])}
ids = [i for i in ids if i not in done]
with open(sys.argv[2], "a") as f, concurrent.futures.ThreadPoolExecutor(int(sys.argv[3]) if len(sys.argv) > 3 else 3) as ex:
    for r in ex.map(get, ids):
        if r:
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
print("fetched", len(ids))
