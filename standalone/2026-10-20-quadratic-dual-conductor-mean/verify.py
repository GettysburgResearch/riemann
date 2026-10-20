#!/usr/bin/env python3
"""Exact finite certificates, not an analytic theorem verifier.

Standard library only. The predecessor is authenticated before importing
its finite-field arithmetic. Deliberate errors must also fail under -O.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import itertools
import json
from math import lcm
from pathlib import Path
from typing import Any

BACKEND_SHA256 = "a56c35b9dece264ab1471da7aa9a8c314544e08d3d96df596162482d3955879b"
COUNTS: dict[str, int] = {}
STREAM = hashlib.sha256()


class CheckFailure(RuntimeError):
    pass


def need(ok: bool, tag: str, detail: str = "") -> None:
    if not ok:
        raise CheckFailure(tag + (": " + detail if detail else ""))
    COUNTS[tag] = COUNTS.get(tag, 0) + 1
    STREAM.update((tag + ":" + detail + "\n").encode())


class Poly:
    """Sparse exact polynomials in sigma, k=log_C(K), m=log_C(M)."""
    def __init__(self, terms: Any = 0):
        if isinstance(terms, Poly):
            self.t = dict(terms.t)
        elif isinstance(terms, dict):
            self.t = {e: F(v) for e, v in terms.items() if v}
        else:
            self.t = {(0, 0, 0): F(terms)} if terms else {}

    def __add__(self, other: Any) -> Poly:
        out = dict(self.t)
        for e, v in Poly(other).t.items():
            out[e] = out.get(e, F(0)) + v
        return Poly(out)

    __radd__ = __add__

    def __neg__(self) -> Poly:
        return Poly({e: -v for e, v in self.t.items()})

    def __sub__(self, other: Any) -> Poly:
        return self + (-Poly(other))

    def __rsub__(self, other: Any) -> Poly:
        return Poly(other) + (-self)

    def __mul__(self, other: Any) -> Poly:
        out: dict[tuple[int, int, int], F] = {}
        for e, v in self.t.items():
            for d, w in Poly(other).t.items():
                q = tuple(x+y for x, y in zip(e, d))
                out[q] = out.get(q, F(0)) + v*w
        return Poly(out)

    __rmul__ = __mul__

    def value(self, s: F, k: F = F(0), m: F = F(0)) -> F:
        return sum((v*s**a*k**b*m**c for (a,b,c),v in self.t.items()), F(0))

    def sub_m(self, new: Poly) -> Poly:
        out = Poly()
        for (a,b,c),v in self.t.items():
            term = Poly({(a,b,0): v})
            for _ in range(c):
                term = term * new
            out = out + term
        return out

    def sub_k(self, val: F) -> Poly:
        out = Poly()
        for (a,b,c),v in self.t.items():
            out = out + Poly({(a,0,c): v*val**b})
        return out

    def slope_k(self) -> Poly:
        need(all(b <= 1 for a,b,c in self.t), "affine_k")
        return Poly({(a,0,c): v for (a,b,c),v in self.t.items() if b})


def identity(a: Poly, b: Poly, name: str) -> None:
    need(not (a-b).t, "polynomial_identity", name)


def nonnegative(q: Poly, kl: F, kh: F | None, name: str) -> None:
    """Bilinear extrema on a rectangle; affine slopes for an infinite strip."""
    need(all(a <= 1 and b <= 1 and c == 0 for a,b,c in q.t), "bilinear_shape", name)
    for s in (F(4,9), F(1,2)):
        need(q.value(s,kl) >= 0, "closed_domain_nonnegative", f"{name}:s={s}:k={kl}")
        if kh is not None:
            need(q.value(s,kh) >= 0, "closed_domain_nonnegative", f"{name}:s={s}:k={kh}")
        else:
            need(q.slope_k().value(s) >= 0, "infinite_strip_slope", f"{name}:s={s}")


def scalar_checks(mutation: str | None) -> dict[str, Any]:
    s = Poly({(1,0,0): 1})
    k = Poly({(0,1,0): 1})
    m = Poly({(0,0,1): 1})
    h = [(1-F(3,2)*s)*k+2-F(7,4)*s,
         (1-F(12,11)*s)*k+2-F(20,11)*s,
         (1-s)*k+2-2*s]
    splits = [F(3,4)*k+F(7,8), F(6,11)*k+F(10,11), F(1,2)*k+1]
    if mutation == "wrong-split":
        splits[0] = F(3,4)*k+1
    domains = [(F(0),F(1,6)), (F(1,6),F(2)), (F(2),None)]
    resource = [1+(1-2*s)*m, (2-2*s)*m,
                F(5,6)+(F(4,3)-2*s)*m,
                F(1,3)+(F(11,6)-2*s)*m,
                (1-2*s)*k+3-4*s, k+2-2*s*m]
    for i, (split, domain) in enumerate(zip(splits,domains)):
        identity(resource[-1].sub_m(split), h[i], f"balanced-regime-{i}")
        for j, term in enumerate(resource):
            nonnegative(h[i]-term.sub_m(split), *domain, f"resource-{i}-{j}")
        for j in range(3):
            nonnegative(h[i]-h[j], *domain, f"envelope-{i}-{j}")
            nonnegative(splits[j]-split, *domain, f"minimum-split-{i}-{j}")
        nonnegative(split, *domain, f"legal-lower-length-{i}")
        nonnegative(F(1,2)*k+1-split, *domain, f"legal-upper-length-{i}")
    for join, i in [(F(1,6),0),(F(2),1)]:
        identity(splits[i].sub_k(join),splits[i+1].sub_k(join),f"split-join-{i}")
        identity(h[i].sub_k(join),h[i+1].sub_k(join),f"envelope-join-{i}")
    # A universal symbolic lower certificate for the supplied resource.
    for i,(term,w) in enumerate([(resource[2],F(3,2)*s),
                                  (resource[3],F(12,11)*s),
                                  (resource[1],s)]):
        identity(w*term+(1-w)*resource[-1],h[i],f"geometric-mean-{i}")
        nonnegative(w,F(0),F(0),f"weight-positive-{i}")
        nonnegative(1-w,F(0),F(0),f"weight-at-most-one-{i}")
    identity(resource[4]-h[0],-F(1,2)*s*k+1-F(9,4)*s,
             "dual-diagonal-ratio")
    # Exact fixed-conductor cancellation and complete cube resources.
    for a,b,name in [
        ((1-4*s)+2*s,1-2*s,"dual-diagonal-F0"),
        (2-4*s,2*(1-2*s),"dual-diagonal-F1"),
        ((2-4*s)+1,3-4*s,"dual-diagonal-C"),
        ((1-4*s)+4*s,Poly(1),"dual-length-F0"),
        ((2-4*s)+4*s,Poly(2),"dual-length-F1-and-C"),
        (F(1,2)-3*s-3*(F(1,2)-s),Poly(-1),"original-complete-cubes"),
        (3*s-F(5,2)-3*s,Poly(-F(5,2)),"dual-complete-cubes"),
    ]:
        identity(a,b,name)
    # Explicit ramanujan shortening cancellations in log variables.
    da, db = k, m
    identity(s*da+(3*s-F(3,2))*db-s*(da+3*db),-F(3,2)*db,
             "ramanujan-shortened-length")
    # Checks valid on the whole p interval, not a sampled grid.
    for label, poly in [
        ("mask-root-nonpositive", F(1,2)*(3*s-1)),
        ("powerful-unmarked-margin", 1-F(3,4)*s-F(1,2)),
        ("powerful-marked-nonnegative-margin", F(1,2)-s),
        ("pure-powerful-unmarked", 2-F(7,4)*s-(F(3,2)-s)),
        ("pure-powerful-marked", 2-2*s-(F(3,2)-s)),
    ]:
        nonnegative(poly,F(0),F(0),label)
    for i in range(3):
        a = h[i].slope_k()
        b = h[i].sub_k(F(0))
        nonnegative(1-s-a,F(0),F(0),f"fixed-level-mask-{i}")
        nonnegative(a,F(0),F(0),f"level-monotone-{i}")
        nonnegative(2-F(7,4)*s-b,F(0),F(0),f"unmarked-row-exponent-{i}")
        nonnegative(b-(2-2*s),F(0),F(0),f"marked-row-exponent-{i}")
    p = F(11,24)
    b0 = F(2)-F(7,4)*p
    marked_h = max(x.value(p,F(5,6))*F(3,10) for x in h)
    rms = (2*p*F(3,4)+F(1,2)+marked_h-F(3,10))/2
    euler_h = max(x.value(F(1,2),F(5,6))*F(3,10) for x in h)
    euler_rms = (F(3,4)+F(1,2)+euler_h-F(3,10))/2
    norm_corner = (2*p-1)+F(1,2)+max(x.value(p,F(1,2)) for x in h)
    benchmark = {
       "beta":"7/8", "p":str(p), "unmarked_conductor_exponent":str(b0),
       "gap_to_6_over_5":str(F(6,5)-b0), "normalized_X_equals_U":str(2*p-1+b0),
       "gain_against_generic_equal_length_sieve":str(F(7,6)-(2*p-1+b0)),
       "marked_RMS_example":str(rms), "Euler_only_RMS_example":str(euler_rms),
       "RMS_saving_against_comparable_Euler_baseline":str(euler_rms-rms),
       "normalized_marked_corner_cost":str(norm_corner)}
    expected = [b0==F(115,96), F(6,5)-b0==F(1,480),
                2*p-1+b0==F(107,96), rms==F(109,160),
                euler_rms==F(153,220), euler_rms-rms==F(5,352),
                norm_corner==F(11,6)]
    for i, ok in enumerate(expected):
        need(ok,"exact_benchmark",str(i))
    if mutation == "false-consumer":
        need(norm_corner <= F(6,5),"false_consumer_rejected")
    else:
        need(norm_corner > F(6,5),"consumer_gap_retained")
    return benchmark


def local_checks(backend: Any, mutation: str | None) -> dict[str, Any]:
    fields = []
    for p, quad in [(7,False),(13,False),(19,False),(31,False),(5,True)]:
        ff = backend.Field(p,quad)
        q = ff.q
        ring = backend.Roots(lcm(6,p))
        cs, ads = ring.order//6, ring.order//p
        gpsi = ring.mono_sum(cs*ff.log[a]+ads*ff.trace(a) for a in range(1,q))
        gtheta = ring.mono_sum(3*cs*ff.log[a]+ads*ff.trace(a) for a in range(1,q))
        for a in range(1,q):
            need((3*ff.log[a])%6 == ((1+2)*ff.log[a])%6,
                 "local_completion_and_dual",f"q={q}:a={a}")
        for v in range(q):
            power = 1 if mutation == "wrong-dual" else 3
            inner = ring.mono_sum(power*cs*ff.log[a]+ads*ff.trace(ff.mul(v,a))
                                  for a in range(1,q))
            got = ring.reduce(ring.mul(gpsi,inner))
            expected = ring.reduce([0]*ring.order) if v==0 else ring.reduce(
                ring.shift(ring.mul(gpsi,gtheta),-3*cs*ff.log[v]))
            need(got==expected,"quadratic_dual_transform",f"q={q}:v={v}")
            mass = ring.reduce(ring.mul(inner,ring.conjugate(inner)))
            need(mass == ((0 if v==0 else q),)+(0,)*(ring.degree-1),
                 "quadratic_dual_mass",f"q={q}:v={v}")
        fields.append(q)
    # Every finite valuation pattern, including the purely powerful case.
    # This exhaustive finite local alphabet is the input to an Euler-product proof.
    patterns = 0
    for vals in itertools.product(range(6), repeat=4):
        e = tuple(int(j==1) for j in vals)
        z = tuple(0 if j==1 else j for j in vals)
        f = tuple(int(j>=2) for j in vals)
        level = tuple(0 if j<2 else (1 if j==4 else 2) for j in vals)
        need(all(x+y==j and not(x and y) for x,y,j in zip(e,z,vals)),
             "unique_row_decomposition",str(vals))
        need(all(a<=b for a,b in zip(level,z)),"powerful_effective_level",str(vals))
        actual_residue = all(j in (0,4) for j in vals)
        predicted_residue = False if mutation=="omit-residue" and any(vals) else not any(e) and all(
            j==0 or (j+2)%6==0 for j in z)
        need(actual_residue==predicted_residue,"residue_fourth_power",str(vals))
        need(all((j>=2)==bool(v) for j,v in zip(z,f)),"primitive_powerful_modulus",str(vals))
        patterns += 1
    return {"fields":fields,"all_four_prime_valuation_patterns":patterns,
            "analytic_Euler_product_proof_required":True}


def load_backend(path: Path | None) -> Any:
    here = Path(__file__).resolve().parent
    candidates = ([path] if path else [
        here.parent/'2026-10-20-primitive-twist-type-i'/'verify.py',
        here.parent/'primitive-twist-type-i'/'verify.py'])
    found = next((p for p in candidates if p is not None and p.is_file()),None)
    if found is None:
        raise CheckFailure("authenticated predecessor verify.py not found")
    need(hashlib.sha256(found.read_bytes()).hexdigest()==BACKEND_SHA256,
         "predecessor_hash")
    spec = importlib.util.spec_from_file_location('authenticated_prior_finite_algebra',found)
    if spec is None or spec.loader is None:
        raise CheckFailure("cannot load authenticated predecessor")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_manifest() -> None:
    here = Path(__file__).resolve().parent
    path = here/'MANIFEST.json'
    if not path.exists():
        raise CheckFailure("required manifest not found")
    manifest = json.loads(path.read_text())
    actual = {p.name for p in here.iterdir() if p.is_file() and p.name!='MANIFEST.json'}
    if actual != set(manifest['files']):
        raise CheckFailure('manifest inventory')
    for name, expected in manifest['files'].items():
        fp = here/name
        if fp.parent != here or not fp.is_file():
            raise CheckFailure('manifest path: '+name)
        content = fp.read_bytes()
        if hashlib.sha256(content).hexdigest()!=expected['sha256']:
            raise CheckFailure('manifest digest: '+name)
        if len(content)!=expected['bytes']:
            raise CheckFailure('manifest length: '+name)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--predecessor',type=Path)
    ap.add_argument('--mutation',choices=['wrong-dual','wrong-split','omit-residue','false-consumer'])
    args = ap.parse_args()
    verify_manifest()
    backend = load_backend(args.predecessor)
    benchmarks = scalar_checks(args.mutation)
    local = local_checks(backend,args.mutation)
    # The inherited rational interval certificate, not a new floating optimizer.
    root = backend.root_checks()
    report = {
        'status':'PASS',
        'scope':'exact finite algebra, continuous scalar inequalities and row bookkeeping; not analytic certification',
        'checks':COUNTS,'check_stream_sha256':STREAM.hexdigest(),
        'benchmarks':benchmarks,'local':local,'inherited_root_certificate':root,
        'new_zero_free_boundary_proved':False,
        'independent_human_or_separate_agent_review':False,
        'upstream_analytic_proofs_rebuilt':False}
    print(json.dumps(report,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
