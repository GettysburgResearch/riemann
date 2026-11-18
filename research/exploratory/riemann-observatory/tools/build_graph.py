#!/usr/bin/env python3
"""Build graphs/knowledge_graph.jsonl from archive data (schema: graphs/graph_schema.md).

Usage: python3 build_graph.py ARCHIVE_ROOT CITATION_EDGES_TSV
Sources: corpus/bibliography.jsonl, theorems/{theorems,proof_dependencies}.jsonl, frontiers/ledger.jsonl,
connections/{repository_bridge,connections}.jsonl, audits/findings.jsonl (if present), and zbMATH citation
edges (citing_zbmath_id<TAB>cited_zbmath_id) restricted to the selected corpus.
"""
import json, os, re, sys, collections

CRITERIA = {
    "CRIT:li": ("Li / Keiper-Li criterion", ["li coefficient", "keiper", "li's criterion", "li criterion"]),
    "CRIT:weil": ("Weil explicit-formula positivity", ["weil positivity", "weil's positivity", "weil quadratic", "weil functional", "weil criterion"]),
    "CRIT:nyman-beurling": ("Nyman-Beurling / Baez-Duarte criterion", ["nyman", "beurling", "baez-duarte", "báez-duarte"]),
    "CRIT:robin": ("Robin's inequality", ["robin"]),
    "CRIT:lagarias": ("Lagarias harmonic-number inequality", ["harmonic number", "lagarias' inequality", "lagarias inequality"]),
    "CRIT:nicolas": ("Nicolas' Euler-phi criterion", ["nicolas"]),
    "CRIT:mertens": ("Mertens-function growth criterion", ["mertens"]),
    "CRIT:riesz": ("Riesz criterion", ["riesz"]),
    "CRIT:hardy-littlewood": ("Hardy-Littlewood criterion", ["hardy-littlewood criterion"]),
    "CRIT:de-bruijn-newman": ("de Bruijn-Newman constant Lambda <= 0", ["de bruijn-newman", "newman"]),
    "CRIT:jensen": ("Jensen-polynomial hyperbolicity / Laguerre-Polya", ["jensen polynomial", "laguerre-p", "turan inequalit", "turán inequalit"]),
    "CRIT:franel-landau": ("Franel-Landau Farey criterion", ["farey"]),
    "CRIT:redheffer": ("Redheffer matrix criterion", ["redheffer"]),
    "CRIT:speiser": ("Speiser zeta' criterion", ["speiser"]),
    "CRIT:de-branges": ("de Branges / Hermite-Biehler formulation", ["de branges", "hermite-biehler"]),
    "CRIT:hilbert-polya": ("Hilbert-Polya spectral realization", ["hilbert-p", "polya-hilbert", "self-adjoint operator"]),
    "CRIT:sondow-dumitrescu": ("Monotonicity of |xi| (Sondow-Dumitrescu)", ["sondow", "monotonicity of |xi", "modulus of xi"]),
}

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:60]

def jl(p):
    return [json.loads(l) for l in open(p)] if os.path.exists(p) else []

def main(root, cit):
    nodes, edges = {}, []
    def node(i, t, label, **props):
        if i not in nodes:
            nodes[i] = {"kind": "node", "id": i, "type": t, "label": label, "props": props}
        return i
    def edge(src, dst, t, status, evidence=None, confidence="medium"):
        edges.append({"kind": "edge", "id": f"E-{len(edges) + 1:06d}", "src": src, "dst": dst, "type": t, "status": status,
                      "evidence": evidence or {}, "confidence": confidence})
    bib = jl(os.path.join(root, "corpus", "bibliography.jsonl"))
    zb2p = {}
    for b in bib:
        p = node(b["paper_id"], "paper", f"{(b.get('authors') or ['?'])[0].split(',')[0]} {b.get('year')}: {(b.get('title') or '')[:120]}",
                 year=b.get("year"), stratum=b.get("stratum"), families=b.get("families"), audit_level=b.get("audit_level"),
                 doi=b.get("doi"), arxiv=b.get("arxiv"), zbl=b.get("zbl"))
        if b.get("zbmath_id"):
            zb2p[str(b["zbmath_id"])] = p
        for a in (b.get("authors") or [])[:12]:
            aid = node("AUTH:" + slug(a), "author", a)
            edge(p, aid, "authored_by", "established", {"source": "index metadata"}, "high")
        text = ((b.get("title") or "") + " ").lower()
        for cid, (lab, kws) in CRITERIA.items():
            if any(k in text for k in kws):
                node(cid, "criterion", lab)
                edge(p, cid, "about_structure", "reported", {"basis": "title keyword match"}, "low")
    # citations among selected works
    n_cit = 0
    if os.path.exists(cit):
        for line in open(cit):
            a, b2 = line.strip().split("\t")
            if a in zb2p and b2 in zb2p and a != b2:
                edge(zb2p[a], zb2p[b2], "cites", "citation_only", {"source": "zbMATH resolved references"}, "high")
                n_cit += 1
    # theorems
    for t in jl(os.path.join(root, "theorems", "theorems.jsonl")):
        k = "lemma" if t.get("kind") == "lemma" else ("theorem" if "conj" not in (t.get("kind") or "") else "conjecture")
        tid = node(t["thm_id"], k, (t.get("statement") or "")[:200], scope=t.get("scope"), conditional_on=t.get("conditional_on"), location=t.get("location"))
        edge(t["paper_id"], tid, "proves" if k != "conjecture" else "suggests_route_to", "established" if t.get("evidence_level") == "fulltext_read" else "reported",
             {"paper": t["paper_id"], "location": t.get("location"), "evidence_level": t.get("evidence_level")}, "high" if t.get("evidence_level") == "fulltext_read" else "medium")
        for c in t.get("conditional_on") or []:
            if c and len(c) < 120:
                cid = node("COND:" + slug(c), "conjecture", c)
                edge(tid, cid, "conditional_on", "established", {"paper": t["paper_id"], "location": t.get("location")}, "medium")
    for d in jl(os.path.join(root, "theorems", "proof_dependencies.jsonl")):
        src = node(f"LOC:{d['paper_id']}:{slug(d.get('from'))}", "lemma", f"{d['paper_id']} {d.get('from')}")
        dst = node(f"LOC:{d['paper_id']}:{slug(d.get('to'))}", "lemma", f"{d['paper_id']} {d.get('to')}")
        rel = d.get("relation") or "uses"
        rel = rel if rel in ("uses", "requires", "special_case_of", "generalizes", "equivalent_to") else "uses"
        edge(src, dst, rel, "established", {"paper": d["paper_id"], "source": "L1 dependency extraction"}, "medium")
    # ledger
    for r in jl(os.path.join(root, "frontiers", "ledger.jsonl")):
        lid = node(r["led_id"], "ledger_record", f"{r.get('quantity')}: {r.get('value')}"[:200], area=r.get("area"), status=r.get("status"),
                   verification=(r.get("verification") or {}).get("verdict"))
        v = (r.get("verification") or {}).get("verdict") or ""
        st = "established" if v.startswith("confirmed") else ("reported" if v in ("", "unverifiable", None) else "reported")
        src = r.get("source") or {}
        sid = node("SRC:" + slug(f"{src.get('authors')} {src.get('year')} {src.get('title')}"), "paper", f"{src.get('authors')} {src.get('year')}: {src.get('title')}"[:200], arxiv=src.get("arxiv"), doi=src.get("doi"))
        edge(sid, lid, "improves_record", st, {"location": r.get("location"), "evidence_level": r.get("evidence_level"), "verifier": v}, "high" if v.startswith("confirmed") else "medium")
    # bridge
    for b in jl(os.path.join(root, "connections", "repository_bridge.jsonl")):
        bid = node(b["brg_id"], {"prior_art": "connection", "obstruction": "obstruction", "tool": "technique"}[b["kind"]],
                   (b.get("literature_result") or b.get("obstruction") or b.get("tool") or "")[:200], programme=b.get("programme"))
        prog = node("REPO:" + b["programme"], "structure", f"host-repository programme {b['programme']}")
        v = (b.get("verification") or {}).get("verdict")
        t = {"prior_art": "special_case_of", "obstruction": "obstructs", "tool": "suggests_route_to"}[b["kind"]]
        edge(bid, prog, t, "established" if v in ("confirmed", "confirmed_with_correction") else ("speculative" if b["kind"] == "tool" else "reported"),
             {"citation": b.get("citation"), "relation": b.get("relation"), "verifier": v}, "medium")
    # connections & findings (if present)
    for c in jl(os.path.join(root, "connections", "connections.jsonl")):
        cid = node(c["con_id"], "connection", c.get("title", "")[:200], kind=c.get("kind"), status=c.get("status"))
        for s in c.get("source_papers", []):
            edge(cid, s, "suggests_route_to", "speculative" if c.get("status") != "tested_refuted" else "refuted", {"verifier": c.get("verification")}, "low")
    for f in jl(os.path.join(root, "audits", "findings.jsonl")):
        fid = node(f["finding_id"], "finding", f.get("claim", "")[:200], classification=f.get("classification"), status=f.get("status"))
        if f.get("paper_id"):
            edge(fid, f["paper_id"], "repairs_gap_in" if f.get("classification") in ("verified_error", "suspected_gap") else "about_structure",
                 "established" if f.get("status") == "verified" else "reported", {"location": f.get("location")}, "medium")
    os.makedirs(os.path.join(root, "graphs"), exist_ok=True)
    with open(os.path.join(root, "graphs", "knowledge_graph.jsonl"), "w") as fh:
        for n in nodes.values():
            fh.write(json.dumps(n, ensure_ascii=False) + "\n")
        for e in edges:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    print("nodes", len(nodes), collections.Counter(n["type"] for n in nodes.values()))
    print("edges", len(edges), collections.Counter(e["type"] for e in edges), "citations", n_cit)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
