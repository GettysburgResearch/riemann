#!/usr/bin/env python3
"""Extract completed agent results from a workflow journal.jsonl.
Usage: python3 journal_extract.py JOURNAL OUT_JSONL   -> lines {label, phase, result}"""
import json, sys
started = {}
out = []
for line in open(sys.argv[1]):
    j = json.loads(line)
    if j.get("type") == "started":
        started[j.get("key")] = j
        continue
    res = None
    for k in ("result", "value", "output", "returnValue"):
        if k in j:
            res = j[k]; break
    if res is None:
        continue
    meta = started.get(j.get("key"), {})
    out.append({"label": j.get("label") or meta.get("label"), "phase": j.get("phase") or meta.get("phase"), "type": j.get("type"), "result": res})
with open(sys.argv[2], "w") as f:
    for o in out:
        f.write(json.dumps(o, ensure_ascii=False) + "\n")
print(len(out), "results;", sorted({o["label"] for o in out if o["label"]})[:50])
