#!/usr/bin/env python3
"""Final corpus selection (~1000 works) from triaged candidates.

Usage: python3 select_corpus.py WORKDIR TARGET
WORKDIR: candidates.jsonl, triage.jsonl (merged main + supplementary triage), l1_cands.txt (cand_ids read at L1, always kept).
Rules (methodology.md §4):
  1. keep every work read at Level 1 and every 'include' with relevance >= 4;
  2. keep verified expert seeds triaged include/borderline with relevance >= 3;
  3. fill with relevance-3 includes by selection score, enforcing family floors and stratum floors;
  4. borderline works may fill family floors for D, F, G, H only;
  5. dedupe by (normalized title, first-author surname); keep the original over translations/reprints;
  6. cap family-G 'low_quality' items (crank cap) at 25.
Writes WORKDIR/selection.json with ordered cand_ids and per-candidate notes for unselected includes.
"""
import json, os, re, sys, collections

FAM_FLOOR = {"A": 200, "B": 170, "C": 100, "D": 70, "E": 100, "F": 70, "G": 40, "H": 35}
ST_FLOOR = {"S1": 15, "S2": 90, "S3": 100, "S4": 150, "S5": 170, "S6": 150, "S7": 80}

def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())[:50]

def main(wd, target):
    C = {json.loads(l)["cand_id"]: json.loads(l) for l in open(os.path.join(wd, "candidates.jsonl"))}
    T = {json.loads(l)["cand_id"]: json.loads(l) for l in open(os.path.join(wd, "triage.jsonl"))}
    l1 = set(open(os.path.join(wd, "l1_cands.txt")).read().split()) if os.path.exists(os.path.join(wd, "l1_cands.txt")) else set()
    sel, seen, notes = [], {}, {}
    def key(c):
        return (norm(c.get("title")), norm(((c.get("authors") or [""])[0]).split(",")[0])[:12])
    def add(cid, why):
        c = C[cid]
        k = key(c)
        if k in seen:
            notes[cid] = f"duplicate of {seen[k]}"
            return False
        seen[k] = cid
        sel.append(cid)
        return True
    order = sorted(C, key=lambda x: -(C[x].get("score") or 0))
    for cid in order:
        if cid in l1:
            add(cid, "L1")
    for cid in order:
        t = T.get(cid)
        if t and t["decision"] == "include" and t["relevance"] >= 4 and cid not in sel:
            add(cid, "rel4+")
    for cid in order:
        t = T.get(cid)
        if t and C[cid].get("seed_ids") and t["decision"] in ("include", "borderline") and t["relevance"] >= 3 and cid not in sel:
            add(cid, "seed")
    def counts():
        fam = collections.Counter(f for cid in sel for f in set(T.get(cid, {}).get("families") or []))
        st = collections.Counter(C[cid]["stratum"] for cid in sel)
        return fam, st
    # family / stratum floors from relevance-3 includes (then borderline for D,F,G,H)
    pool3 = [cid for cid in order if T.get(cid) and T[cid]["decision"] == "include" and T[cid]["relevance"] == 3 and cid not in sel]
    for _ in range(3):
        fam, st = counts()
        for cid in pool3:
            if cid in sel:
                continue
            t, c = T[cid], C[cid]
            need = any(fam[f] < FAM_FLOOR.get(f, 0) for f in t["families"]) or st[c["stratum"]] < ST_FLOOR.get(c["stratum"], 0)
            if need and add(cid, "floor"):
                for f in set(t["families"]):
                    fam[f] += 1
                st[c["stratum"]] += 1
    fam, st = counts()
    for cid in order:
        t = T.get(cid)
        if t and t["decision"] == "borderline" and cid not in sel and any(f in ("D", "F", "G", "H") and fam[f] < FAM_FLOOR[f] for f in t["families"]):
            if add(cid, "borderline-floor"):
                for f in set(t["families"]):
                    fam[f] += 1
    # fill to target with remaining relevance-3 includes by score
    for cid in pool3:
        if len(sel) >= target:
            break
        if cid not in sel:
            add(cid, "fill")
    # crank cap
    g_low = [cid for cid in sel if T.get(cid, {}).get("work_type") == "failed_or_withdrawn_attempt"]
    for cid in g_low[25:]:
        sel.remove(cid)
        notes[cid] = "crank_cap"
    for cid in C:
        t = T.get(cid)
        if cid not in sel and cid not in notes and t:
            notes[cid] = ("rejected: " + t.get("reject_reason", "")) if t["decision"] == "reject" else f"not selected ({t['decision']}, relevance {t['relevance']}): below fill threshold"
    fam, st = counts()
    json.dump({"selected": sel, "notes": notes, "family_counts": dict(fam), "stratum_counts": dict(st)}, open(os.path.join(wd, "selection.json"), "w"), indent=0)
    print("selected", len(sel), "families", dict(sorted(fam.items())), "strata", dict(sorted(st.items())))

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 1000)
