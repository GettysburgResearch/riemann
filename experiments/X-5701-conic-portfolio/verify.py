#!/usr/bin/env python3
"""Exact rational checker for affine and PSD-Gram conic portfolios."""
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path

SCHEMA = "riemann.conic-portfolio.v1"
GOOD = {"PROVED", "INDEPENDENTLY_VERIFIED", "SYNTHETIC_CONTROL"}

class Error(ValueError): pass

def Q(x, name="value"):
    if isinstance(x, bool): raise Error(f"{name}: boolean")
    if isinstance(x, int): return Fraction(x)
    if isinstance(x, str):
        try: return Fraction(x)
        except (ValueError, ZeroDivisionError) as exc: raise Error(f"{name}: bad rational") from exc
    raise Error(f"{name}: rational required")

def T(x): return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def features(raw):
    if not isinstance(raw, list) or not raw: raise Error("features required")
    c, r = {}, {}
    for i, f in enumerate(raw):
        if not isinstance(f, dict): raise Error("feature object required")
        k = f.get("id")
        if not isinstance(k, str) or not k or k in c: raise Error("bad feature id")
        c[k], r[k] = Q(f.get("center"), f"features[{i}].center"), Q(f.get("radius"), f"features[{i}].radius")
        if r[k] < 0: raise Error("negative radius")
    return c, r

def manifest(p, used_features, used_gates):
    fs = p.get("feature_manifest")
    if not isinstance(fs, list) or len(fs) != len(set(fs)) or set(fs) != used_features: raise Error("feature manifest mismatch")
    gs = p.get("logical_gates")
    if not isinstance(gs, list): raise Error("logical_gates required")
    found, states = set(), []
    for g in gs:
        if not isinstance(g, dict): raise Error("gate object required")
        gid, state, evidence = g.get("id"), g.get("state"), g.get("evidence")
        if not isinstance(gid, str) or not gid or gid in found: raise Error("bad gate id")
        if state not in GOOD: raise Error(f"gate {gid!r} blocking")
        if not isinstance(evidence, str) or not evidence: raise Error("gate evidence required")
        found.add(gid); states.append(state)
    if found != used_gates: raise Error("gate manifest mismatch")
    return {"logical_gate_count": len(states), "logical_manifest_closed": all(s != "SYNTHETIC_CONTROL" for s in states), "synthetic_gate_count": states.count("SYNTHETIC_CONTROL")}

def upper_box(b, a, c, r): return b + sum((v*c[k] + abs(v)*r[k] for k,v in a.items()), Fraction())

def claimed(p, u):
    if "claimed_robust_upper" in p and Q(p["claimed_robust_upper"], "claimed_robust_upper") != u: raise Error("false claimed endpoint")

def result(kind, u, m, d):
    return {"schema": SCHEMA, "kind": kind, "status": "CERTIFIED_QUANTITATIVE_CONIC_SEPARATION" if u < 0 else "NOT_CERTIFIED", "robust_upper": T(u), "strict_score_moat": T(-u) if u < 0 else "0", "manifest": m, "details": d, "interpretation": "Exact quantitative separation only; RH implications and primitive enclosure soundness are external proof obligations."}

def affine(p):
    c, r = features(p.get("features")); raw_rows, weights = p.get("rows"), p.get("weights")
    if not isinstance(raw_rows, list) or not raw_rows or not isinstance(weights, dict) or not weights: raise Error("rows/weights required")
    rows = {}
    for i, row in enumerate(raw_rows):
        if not isinstance(row, dict): raise Error("row object required")
        rid, cr, gr = row.get("id"), row.get("coefficients"), row.get("gate_ids")
        if not isinstance(rid, str) or not rid or rid in rows or not isinstance(cr, dict) or not isinstance(gr, list) or not gr: raise Error("bad row")
        a = {}
        for k, x in cr.items():
            if k not in c: raise Error("unknown feature")
            a[k] = Q(x, f"rows[{i}].{k}")
            if a[k] == 0: raise Error("explicit zero coefficient")
        rows[rid] = Q(row.get("constant"), f"rows[{i}].constant"), a, set(gr)
    b, a, gates, indiv = Fraction(), {k:Fraction() for k in c}, set(), {}
    for rid, x in weights.items():
        if rid not in rows: raise Error("unknown row")
        w = Q(x, f"weights.{rid}")
        if w <= 0: raise Error("weights must be positive")
        bi, ai, gi = rows[rid]; b += w*bi; gates |= gi; indiv[rid] = T(upper_box(bi, ai, c, r))
        for k, v in ai.items(): a[k] += w*v
    a = {k:v for k,v in a.items() if v}; u = upper_box(b, a, c, r); claimed(p,u)
    l1 = sum((abs(v) for v in a.values()), Fraction())
    repair = "INFINITE_IN_DECLARED_FEATURE_SPACE" if u < 0 and l1 == 0 else (T((-u)/l1) if u < 0 else "0")
    return result("affine-box-portfolio", u, manifest(p,set(c),gates), {"combined_constant":T(b), "combined_coefficients":{k:T(v) for k,v in sorted(a.items())}, "individual_robust_uppers":indiv, "linfinity_feature_repair_lower":repair})

def matrix(raw, name):
    if not isinstance(raw, list) or not raw: raise Error(f"{name}: matrix required")
    A = [[Q(x,name) for x in row] if isinstance(row,list) else [] for row in raw]; n=len(A)
    if any(len(row)!=n for row in A) or any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)): raise Error(f"{name}: nonsymmetric square matrix")
    return A

def quad(A,v): return sum((v[i]*A[i][j]*v[j] for i in range(len(v)) for j in range(len(v))), Fraction())

def psd(p):
    B = matrix(p.get("base_matrix"),"base_matrix"); raw_F, terms, gid = p.get("feature_matrices"), p.get("gram_terms"), p.get("gate_id")
    if not isinstance(raw_F,dict) or not isinstance(terms,list) or not terms or not isinstance(gid,str) or not gid: raise Error("matrix fields required")
    F = {k:matrix(v,f"feature_matrices.{k}") for k,v in raw_F.items()}; n=len(B)
    if any(len(A)!=n for A in F.values()): raise Error("matrix dimension mismatch")
    c,r = features(p.get("features"))
    if set(c)!=set(F): raise Error("feature table/pencil mismatch")
    b,a,indiv,seen = Fraction(),{k:Fraction() for k in c},{},set()
    for i,t in enumerate(terms):
        if not isinstance(t,dict): raise Error("Gram term object required")
        tid,w,vr=t.get("id"),Q(t.get("weight"),f"gram_terms[{i}].weight"),t.get("vector")
        if not isinstance(tid,str) or not tid or tid in seen or w<=0 or not isinstance(vr,list) or len(vr)!=n: raise Error("bad Gram term")
        v=[Q(x,f"gram_terms[{i}].vector") for x in vr]
        if not any(v): raise Error("zero Gram vector")
        seen.add(tid); bi=quad(B,v); ai={k:quad(A,v) for k,A in F.items()}; b+=w*bi; indiv[tid]=T(upper_box(bi,ai,c,r))
        for k,x in ai.items(): a[k]+=w*x
    a={k:v for k,v in a.items() if v}; u=upper_box(b,a,c,r); claimed(p,u)
    return result("psd-gram-box",u,manifest(p,set(c),{gid}),{"combined_constant":T(b),"combined_coefficients":{k:T(v) for k,v in sorted(a.items())},"individual_robust_uppers":indiv})

def verify(p):
    if not isinstance(p,dict) or p.get("schema")!=SCHEMA: raise Error("wrong schema")
    if p.get("kind")=="affine-box-portfolio": return affine(p)
    if p.get("kind")=="psd-gram-box": return psd(p)
    raise Error("unsupported kind")

def controls():
    g=[{"id":"synthetic","state":"SYNTHETIC_CONTROL","evidence":"built-in exact control"}]
    a={"schema":SCHEMA,"kind":"affine-box-portfolio","features":[{"id":"u","center":"0","radius":"1"}],"rows":[{"id":"q1","constant":"-2/5","coefficients":{"u":"1"},"gate_ids":["synthetic"]},{"id":"q2","constant":"-2/5","coefficients":{"u":"-1"},"gate_ids":["synthetic"]}],"weights":{"q1":"1","q2":"1"},"feature_manifest":["u"],"logical_gates":g,"claimed_robust_upper":"-4/5"}
    p={"schema":SCHEMA,"kind":"psd-gram-box","base_matrix":[["-1/2","0"],["0","-1/2"]],"feature_matrices":{"u":[["1","0"],["0","-1"]]},"features":[{"id":"u","center":"0","radius":"1"}],"gram_terms":[{"id":"e1","weight":"1","vector":["1","0"]},{"id":"e2","weight":"1","vector":["0","1"]}],"gate_id":"synthetic","feature_manifest":["u"],"logical_gates":g,"claimed_robust_upper":"-1"}
    return a,p

def self_test():
    a,p=controls(); A,P=verify(a),verify(p)
    assert A["robust_upper"]=="-4/5" and A["details"]["individual_robust_uppers"]=={"q1":"3/5","q2":"3/5"}
    assert P["robust_upper"]=="-1" and P["details"]["individual_robust_uppers"]=={"e1":"1/2","e2":"1/2"}
    bad=json.loads(json.dumps(a)); bad["weights"]["q2"]="-1"
    try: verify(bad)
    except Error: pass
    else: raise AssertionError("negative weight accepted")

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("certificate",nargs="?",type=Path); ap.add_argument("--self-test",action="store_true"); args=ap.parse_args()
    if args.self_test: self_test(); print("3 exact conic controls passed"); return
    if args.certificate is None: ap.error("certificate required unless --self-test")
    try: print(json.dumps(verify(json.loads(args.certificate.read_text(encoding="utf-8"))),indent=2,sort_keys=True))
    except (OSError,json.JSONDecodeError,Error) as exc: raise SystemExit(f"REJECTED: {exc}") from exc

if __name__=="__main__": main()
