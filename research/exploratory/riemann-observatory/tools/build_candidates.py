#!/usr/bin/env python3
"""Score the pool and build the candidate bibliography for agent triage.

Usage: python3 build_candidates.py POOL_JSONL SEEDS_JSONL SEED_MATCHES_JSONL OUT_DIR
Writes OUT_DIR/candidates.jsonl (CAND-##### ids, score components) and OUT_DIR/triage_batches/batch_###.jsonl.
Score (documented in methodology.md §4):
  score = 2.0*rel + 2.5*cent + 3.0*seed + 0.4*multi_query + type_bonus
  rel  = relevance weight / 3.5 (query membership, max over queries)
  cent = within-stratum percentile of log(1+in-pool citations)
  seed = 1 if matched to a verified expert seed
"""
import json, math, os, sys, collections, re

QUOTA = {"S1": 60, "S2": 260, "S3": 380, "S4": 470, "S5": 600, "S6": 560, "S7": 420, "S?": 0}
MASK = "zbMATH Open Web Interface contents unavailable"

def main(pool_p, seeds_p, matches_p, out):
    pool = {json.loads(l)["key"]: json.loads(l) for l in open(pool_p)}
    seeds = {json.loads(l)["seed_id"]: json.loads(l) for l in open(seeds_p)} if os.path.exists(seeds_p) else {}
    matches = [json.loads(l) for l in open(matches_p)] if os.path.exists(matches_p) else []
    seed_of = collections.defaultdict(list)
    extra = []
    for m in matches:
        if m.get("status") != "verified":
            continue
        s = seeds[m["seed_id"]]
        key = m.get("pool_key") or (f"zb:{m['zbmath_id']}" if m.get("zbmath_id") else None)
        if key and key in pool:
            seed_of[key].append(m["seed_id"])
        elif m.get("arxiv") and f"ax:{m['arxiv']}" in pool:
            seed_of[f"ax:{m['arxiv']}"].append(m["seed_id"])
        else:  # verified outside pool: create a candidate from the seed + match metadata
            key = f"seed:{m['seed_id']}"
            pool[key] = {"key": key, "zbmath_id": m.get("zbmath_id"), "zbl": m.get("zbl"), "title": s["title"],
                         "title_original": s["title"], "authors": s["authors"], "year": str(s.get("year")),
                         "venue": s.get("venue") or m.get("venue", ""), "doi": m.get("doi") or s.get("doi", ""),
                         "arxiv": m.get("arxiv") or s.get("arxiv", ""), "doc_type": "seed", "msc": [], "keywords": [],
                         "language": "", "review": "", "queries": [], "in_pool_citations": 0,
                         "stratum": None, "rel_weight": 3.0, "n_queries": 0, "matched_via": m.get("source")}
            seed_of[key].append(m["seed_id"])
    # strata + centrality percentiles
    from build_pool import stratum
    by_st = collections.defaultdict(list)
    for p in pool.values():
        p["stratum"] = p.get("stratum") or stratum(p.get("year"))
        by_st[p["stratum"]].append(math.log1p(p.get("in_pool_citations", 0)))
    for st in by_st:
        by_st[st].sort()
    def pct(st, v):
        arr = by_st[st]
        import bisect
        return bisect.bisect_left(arr, v) / max(1, len(arr) - 1) if v > 0 else 0.0
    cands = []
    for k, p in pool.items():
        if MASK in (p.get("title") or "") or not p.get("title"):
            if not seed_of.get(k):
                continue
        rel = min(1.0, p.get("rel_weight", 0) / 3.5)
        cent = pct(p["stratum"], math.log1p(p.get("in_pool_citations", 0)))
        seed = 1.0 if seed_of.get(k) else 0.0
        tb = 0.5 if p.get("doc_type") == "b" else 0.0
        score = 2.0 * rel + 2.5 * cent + 3.0 * seed + 0.4 * (p.get("n_queries", 0) > 1) + tb
        p.update(score=round(score, 4), score_rel=round(rel, 3), score_cent=round(cent, 3), seed_ids=seed_of.get(k, []))
        cands.append(p)
    chosen = []
    for st, q in QUOTA.items():
        group = sorted([c for c in cands if c["stratum"] == st], key=lambda c: -c["score"])
        seeded = [c for c in group if c["seed_ids"]]
        rest = [c for c in group if not c["seed_ids"]][: max(0, q - len(seeded))]
        chosen += seeded + rest
    chosen.sort(key=lambda c: (c["stratum"], -c["score"]))
    os.makedirs(os.path.join(out, "triage_batches"), exist_ok=True)
    with open(os.path.join(out, "candidates.jsonl"), "w") as f:
        for i, c in enumerate(chosen, 1):
            c["cand_id"] = f"CAND-{i:05d}"
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    # triage batches: compact view
    def compact(c):
        seeds_txt = [{"fam": seeds[s].get("families"), "key": seeds[s].get("key_contribution", "")[:300]} for s in c["seed_ids"][:2]]
        return {"cand_id": c["cand_id"], "title": c["title"][:300], "title_original": (c.get("title_original") or "")[:200],
                "authors": c["authors"][:6], "year": c["year"], "venue": (c.get("venue") or "")[:150], "doc_type": c.get("doc_type"),
                "msc": c.get("msc", [])[:6], "keywords": c.get("keywords", [])[:10], "in_pool_citations": c.get("in_pool_citations", 0),
                "stratum": c["stratum"], "abstract": (c.get("arxiv_abstract") or "")[:1100], "zb_review": (c.get("review") or "")[:1100],
                "seed_notes": seeds_txt, "arxiv": c.get("arxiv", ""), "doi": c.get("doi", "")}
    B = 100
    for b in range(0, len(chosen), B):
        with open(os.path.join(out, "triage_batches", f"batch_{b // B + 1:03d}.jsonl"), "w") as f:
            for c in chosen[b:b + B]:
                f.write(json.dumps(compact(c), ensure_ascii=False) + "\n")
    print("pool", len(pool), "scored", len(cands), "chosen", len(chosen), collections.Counter(c["stratum"] for c in chosen),
          "seeded", sum(1 for c in chosen if c["seed_ids"]), "batches", math.ceil(len(chosen) / B))

if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main(*sys.argv[1:5])
