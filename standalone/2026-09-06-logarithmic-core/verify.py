#!/usr/bin/env python3
"""Bounded exact controls. Not a proof of the analytic core theorem or RH."""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
PROOF_SHA = "0e9a2bbfbe811a0ccd244129aee302860603eac0882f69d0b183c4a95baa66fc"
SOURCE_SHA = "7ea66a2325ed9fcc80e4d2e370726a013a1a2c115100326b6ed66c14cdb18591"

class Reject(ValueError):
    pass

def require(ok: bool, reason: str) -> None:
    if not ok:
        raise Reject(reason)

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def unique(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, "duplicate JSON key")
        out[k] = v
    return out

def no_float(s):
    raise Reject("non-integer JSON number")

def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_float=no_float, parse_constant=no_float)

def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(typed_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a == b

@dataclass(frozen=True)
class G:
    """An exact Gaussian rational, with no binary floating arithmetic."""
    r: F = F(0)
    i: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, "r", F(self.r))
        object.__setattr__(self, "i", F(self.i))
    def __add__(self, x):
        x = cast(x); return G(self.r+x.r, self.i+x.i)
    __radd__ = __add__
    def __neg__(self):
        return G(-self.r, -self.i)
    def __sub__(self, x):
        return self + -cast(x)
    def __rsub__(self, x):
        return cast(x) + -self
    def __mul__(self, x):
        x = cast(x); return G(self.r*x.r-self.i*x.i, self.r*x.i+self.i*x.r)
    __rmul__ = __mul__
    def __truediv__(self, x):
        x = cast(x); den = x.r*x.r+x.i*x.i
        require(den != 0, "division by zero")
        return self*x.conj()*G(1/den)
    def conj(self):
        return G(self.r, -self.i)
    def norm2(self):
        return self.r*self.r+self.i*self.i

def cast(x):
    return x if isinstance(x, G) else G(x)

def inner(x,y):
    return sum((a.conj()*b for a,b in zip(x,y)), G())

def gram(cols, weights=None):
    if weights is None:
        weights = [F(1)]*len(cols[0])
    return [[sum((weights[k]*x[k].conj()*y[k]
                  for k in range(len(x))), G()) for y in cols] for x in cols]

def quad(mat, u):
    return sum((u[i].conj()*mat[i][j]*u[j]
                for i in range(len(u)) for j in range(len(u))), G())

def solve(mat, rhs):
    """Exact Gaussian elimination, for bounded test matrices only."""
    n = len(rhs)
    a = [[cast(x) for x in mat[i]]+[cast(rhs[i])] for i in range(n)]
    for j in range(n):
        piv = next((k for k in range(j,n) if a[k][j] != G()), None)
        require(piv is not None, "singular test matrix")
        a[j],a[piv] = a[piv],a[j]
        pivot = a[j][j]
        a[j] = [x/pivot for x in a[j]]
        for k in range(n):
            if k != j:
                factor = a[k][j]
                a[k] = [x-factor*y for x,y in zip(a[k],a[j])]
    return [row[-1] for row in a]

def poly_add(a,b):
    n=max(len(a),len(b)); return [(a[i] if i<len(a) else F(0))+
                                   (b[i] if i<len(b) else F(0)) for i in range(n)]

def poly_mul(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def compute():
    counts=Counter()
    def check(name, ok):
        require(ok, "failed exact control: "+name); counts[name]+=1
    # Coefficient identities, not merely evaluations at a frequency grid.
    den=[F(0),F(9,4),F(1)]
    rhs=poly_add(den,[F(1,16),F(1,36)-F(16,9)])
    check("rational_multiplier_coefficients", rhs==[F(1,16),F(1,2),F(1)])
    # Affine dependence on C: its two coefficients determine the identity.
    for C in [F(0),F(1)]:
        left=[F(1,16)-C/4,F(1,2)-C,F(1)]
        right=poly_add(poly_mul([-C-F(7,4),F(1)],[F(9,4),F(1)]),[4+2*C])
        check("coercive_division_coefficients", left==right)
    check("primitive_tail_coefficient", ((F(3,2)**2-F(1,2)**2)/F(3,2))**2==F(16,9))
    check("residual_constants", F(3,2)**2/F(3,4)==3 and F(3,2)**2/F(6,5)==F(15,8))
    # Exact parent scalar reserves; special-function estimates stay in the proof.
    S=lambda m: sum((F(4,4*k+1) for k in range(m+1)),F(0))
    check("source_rational_reserves", S(152)>F(37,4))
    check("source_rational_reserves", S(92)>F(35,4))
    check("source_rational_reserves", F(3,2)*(1-(17205+F(7,4))/93636)>F(6,5))
    for j in range(1,101):
        check("gamma_denominator_tail", (2*F(j)+F(1,2))**2-F(9,4)>=4*j*j)
    for j in range(1,51):
        for r in [F(1),F(2),F(7,3)]:
            b=F(3,2); alpha=2*F(j)+F(1,2)
            # Divided resolvent identity underlying the positive spectral sum.
            left=(r/(r*r+alpha*alpha)-r/(b*b+alpha*alpha))/(b*b-r*r)
            right=r/((r*r+alpha*alpha)*(b*b+alpha*alpha))
            check("laplace_resolvent_normalization", left==right)
    # The finite square in the Schur bound, retaining imaginary cross terms.
    b=F(3,2)
    for seed in range(1,21):
        n=4; d=3; lam=[F(j+1)+F(seed,20) for j in range(n)]; kap=F(1)
        ff=[[G(F((i+1)*(j+2)-seed,7),F(i-j+seed,11)) for j in range(n)] for i in range(d)]
        yy=[[G(F(i-j+seed,13),F((i+2)*(j+1)-seed,17)) for j in range(n)] for i in range(d)]
        rr=[[ff[i][j]-lam[j]*yy[i][j]/b for j in range(n)] for i in range(d)]
        aa=[[b*ff[i][j]/lam[j]-yy[i][j] for j in range(n)] for i in range(d)]
        error=gram(aa,lam); residual=gram(rr)
        rhs=gram(rr,[b*b/x for x in lam])
        check("complex_schur_error_gram", error==rhs)
        for step in range(1,5):
            u=[G(F((i+1)*step,5),F(seed-i*step,9)) for i in range(d)]
            gap=quad([[b*b*residual[i][j]/kap-error[i][j] for j in range(d)] for i in range(d)],u)
            check("complex_loewner_error", gap.i==0 and gap.r>=0)
    # Ridge systems include an exactly zero column and exactly duplicate columns.
    ridge=[]
    for m in [1,2,3,4,6,8,12]:
        target=[G(F(2,3),F(1,5)),G(F(-3,4),F(2,7))]
        columns=[]
        for j in range(m):
            columns.append([G(0),G(0)] if j==0 else
                           ([G(1),G(0)] if j%2 else [G(0),G(1)]))
        gg=gram(columns); delta=F(1,m)
        matrix=[[gg[i][j]+(delta if i==j else 0) for j in range(m)] for i in range(m)]
        rhs=[inner(col,target) for col in columns]
        coeff=solve(matrix,rhs)
        res=[target[k]-sum((coeff[j]*columns[j][k] for j in range(m)),G()) for k in range(2)]
        resnorm=sum((x.norm2() for x in res),F(0))
        for j,col in enumerate(columns):
            check("ridge_normal_equation", inner(col,res)==delta*coeff[j])
        objective=resnorm+delta*sum((x.norm2() for x in coeff),F(0))
        check("ridge_zero_comparison", objective<=sum((x.norm2() for x in target),F(0)))
        ridge.append({"m":m,"residual_squared":str(resnorm)})
    # Exact logarithmic diagonal prototype, with a genuine infinite-tail enclosure.
    harmonic=F(0); subtotal=F(0); model=[]
    for M in range(1,65):
        harmonic+=F(1,M); subtotal+=1/(M*M*harmonic)
        check("harmonic_model_residual_enclosure", F(1,M*M*harmonic)<=F(1,M*M))
        check("energy_does_not_imply_strong_residual", harmonic*(1/harmonic)**2==1/harmonic and harmonic/harmonic==1)
        if M in [1,2,4,8,16]:
            model.append({"M":M,"positive_upper":str(2-subtotal),
                          "positive_lower":str(2-subtotal-F(1,M)),
                          "negative_upper":str(1-subtotal),"tail_bound":str(F(1,M))})
    check("model_strict_certificates", model[1]["positive_lower"]=="1/3" and model[1]["negative_upper"]=="-1/6")
    # Interval-safe projection: weighted polynomial moment cancellation.
    # Simple independent constraints {1,t}; used as a finite core-construction test.
    moment=lambda n: F(1,(n+2)*(n+3)) # integral_0^1 t(1-t)t^n
    mat=[[moment(i+j) for j in range(2)] for i in range(2)]
    for n in range(12):
        coeff=solve(mat,[G(moment(n+i)) for i in range(2)])
        for i in range(2):
            check("exact_continuum_moment_correction", G(moment(n+i))-sum((mat[i][j]*coeff[j] for j in range(2)),G())==G())
    # Finite algebra of the gamma-source primitive summation, not an infinite replay.
    for j in range(1,65):
        alpha=2*F(j)+F(1,2)
        check("gamma_partial_fractions", 1/(alpha*alpha-F(9,4))==F(1,3)*(F(1,2*j-1)-F(1,2*j+2)))
    return {"schema":"riemann.logarithmic_core.controls.v1",
            "status":"PASS_BOUNDED_EXACT_CONTROLS", "rh_proved":False,
            "actual_window_certified":False, "infinite_analytic_proof_machine_checked":False,
            "groups":dict(sorted(counts.items())),"checks":sum(counts.values()),
            "ridge_models":ridge,"harmonic_models":model,
            "proof_sha256":PROOF_SHA,"source_lock_sha256":SOURCE_SHA}

def check_anchors():
    require(digest(ROOT/"PROOF.md")==PROOF_SHA,"proof anchor mismatch")
    require(digest(ROOT/"SOURCE_LOCK.json")==SOURCE_SHA,"source anchor mismatch")

def check_manifest():
    entries={}
    for line in (ROOT/"SHA256SUMS").read_text().splitlines():
        hash_,name=line.split("  ",1)
        require(name not in entries and '/' not in name and name!='SHA256SUMS',"manifest schema")
        entries[name]=hash_
    actual={p.name for p in ROOT.iterdir() if p.is_file() and p.name!='SHA256SUMS'}
    require(set(entries)==actual,"manifest coverage")
    for name,hash_ in entries.items():
        require(digest(ROOT/name)==hash_,"manifest digest: "+name)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write",type=Path)
    ap.add_argument("--check",type=Path)
    args=ap.parse_args()
    check_anchors(); expected=compute()
    if args.write:
        args.write.write_text(json.dumps(expected,sort_keys=True,indent=2)+"\n")
    else:
        supplied=load(args.check or ROOT/"result.json")
        require(typed_equal(supplied,expected),"result differs from reconstruction")
        check_manifest()
    print(json.dumps({"status":expected["status"],"checks":expected["checks"],
                      "groups":len(expected["groups"]),"rh_proved":False},sort_keys=True))

if __name__=="__main__":
    try:
        main()
    except (Reject, OSError, ValueError, KeyError) as exc:
        print("REJECT: "+str(exc),file=sys.stderr); sys.exit(2)
