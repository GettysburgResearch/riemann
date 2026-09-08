#!/usr/bin/env python3
"""Exact finite controls for FW-1--FW-3; not a proof of RH or infinite analysis."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
EXPECTED_SOURCE = {
    "repository": "GettysburgResearch/riemann",
    "publication_base": "2c3184545bafb4f5d873d2fa0ffc2c335a25d048",
    "parents": [
        {"commit": "2c3184545bafb4f5d873d2fa0ffc2c335a25d048", "path": "local-window-positivity/PROOF.md", "git_blob": "8d7120ef2edc0ac033a4814eb61917652fc57ba8"},
        {"commit": "dc4bb9dbb49876732eb656339e79ee4ec43b157f", "path": "arithmetic-cutoff-inertia/PROOF.md", "git_blob": "122097298b4d35f21cca930423711faf748355f7"},
        {"commit": "39c13367f4b3956631ea1e00fac6c3005fc32057", "path": "cross-route-hardy-laguerre/BRIDGE.md", "git_blob": "81d7d5db7a25f5875a08c10235fdb514d67cc744"},
    ],
}
COUNT = 0

def need(ok: bool, message: str) -> None:
    global COUNT
    COUNT += 1
    if not ok:
        raise ValueError(message)

def ceil_fraction(x: F) -> int:
    return -((-x.numerator) // x.denominator)

def pair(x: F) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}

def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    obj: dict[str, object] = {}
    for k, v in pairs:
        if k in obj:
            raise ValueError("duplicate JSON key: " + k)
        obj[k] = v
    return obj

def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)

def same(a: object, b: object) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    return a == b

def atanh_log(x: F, terms: int = 80) -> tuple[F, F]:
    """Enclose log(x), 1 <= x <= 2, with the exact positive series tail."""
    if not F(1) <= x <= F(2) or terms < 1:
        raise ValueError("log domain/terms")
    y = (x - 1) / (x + 1)
    s = 2 * sum((y ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
    rem = 2 * y ** (2*terms+1) / ((2*terms+1) * (1-y*y))
    return s, s + rem

def log_int(n: int) -> tuple[F, F]:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    k = n.bit_length() - 1
    lo, hi = atanh_log(F(n, 2**k))
    l2, u2 = atanh_log(F(2))
    return lo + k*l2, hi + k*u2

def sqrt_int(n: int, digits: int = 40) -> tuple[F, F]:
    if type(n) is not int or n < 1:
        raise ValueError("positive integer required")
    d = 10**digits
    k = isqrt(n*d*d)
    return F(k, d), F(k+1, d)

def round_out(lo: F, hi: F, digits: int = 30) -> dict[str, object]:
    d = 10**digits
    lower = lo.numerator*d // lo.denominator
    upper = ceil_fraction(hi*d)
    return {"lower": lower, "upper": upper, "denominator": d}

def gamma_sum(m: int) -> F:
    return sum((F(4, 4*k+1) for k in range(m+1)), F(0))

def gamma_constant(m: int) -> int:
    return (m+1)*(2*m+1)

def polynomial_derivative(p: list[F]) -> list[F]:
    return [i*p[i] for i in range(1, len(p))] or [F(0)]

def polynomial_add(p: list[F], q: list[F]) -> list[F]:
    ans = [F(0)]*max(len(p), len(q))
    for i, x in enumerate(p): ans[i] += x
    for i, x in enumerate(q): ans[i] += x
    while len(ans)>1 and ans[-1] == 0: ans.pop()
    return ans

def polynomial_scale(p: list[F], q: F) -> list[F]:
    return [q*x for x in p]

def polynomial_mul(p: list[F], q: list[F]) -> list[F]:
    ans = [F(0)]*(len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q): ans[i+j] += x*y
    return ans

def polynomial_value(p: list[F], x: F) -> F:
    return sum((v*x**i for i,v in enumerate(p)), F(0))

def build() -> dict[str, object]:
    global COUNT
    COUNT = 0
    need(same(read_json(HERE/"SOURCE_LOCK.json"), EXPECTED_SOURCE), "source lock mismatch")
    # Direct source bounds for the L=1 example; all arithmetic below is rational.
    l2, u2 = log_int(2)
    l3, u3 = log_int(3)
    s2, t2 = sqrt_int(2)
    s3, t3 = sqrt_int(3)
    need(l2 > F(2,3) and u2 < F(7,10), "log 2 enclosure")
    need(s2*s2 <= 2 < t2*t2 and s3*s3 <= 3 < t3*t3, "sqrt enclosure")
    qlo, qhi = l2/t2+l3/t3, u2/s2+u3/s3
    need(qhi < F(9,8), "actual Q3 upper bound")
    need(u2/s2 < F(1,2), "actual Q2 upper bound")
    need(sum((F(1,factorial(j)) for j in range(4)), F(0))+F(5,96) < 3,
         "e < 3 by geometric tail")
    need(sum((F(6,5)**j/factorial(j) for j in range(7)), F(0)) > F(22,7),
         "exp(6/5) > 22/7")
    need(1+F(11,7)+F(21,10)+F(6,5) == F(411,70) < 6,
         "Omega zero lower bound arithmetic")
    s152 = gamma_sum(152)
    need(s152 > F(37,4), "gamma reservoir m=152")
    need(gamma_constant(152) == 46665, "C152")
    need(9*102**2 > 2*46665+F(7,2), "K=101 for L=1")
    need(gamma_sum(43) > 8, "m=43 for Q2")
    # Independent finite verification of the gamma split and lower envelope.
    for m,q in [(16,F(0)), (43,F(1,2)), (152,F(9,8))]:
        S = gamma_sum(m)
        C = gamma_constant(m)
        need(C == sum(4*k+1 for k in range(m+1)), "gamma C summation")
        for x in [F(0),F(1,16),F(1,4),F(1),F(4),F(25),F(10000)]:
            inc = sum((F(2)/(2*k+F(1,2))*x/((2*k+F(1,2))**2+x)
                       for k in range(m+1)),F(0))
            dec = sum((2*(2*k+F(1,2))/((2*k+F(1,2))**2+x)
                       for k in range(m+1)),F(0))
            need(inc == S-dec, "gamma partial-fraction identity")
            need(-6+inc-2*q >= 1-F(C)/(x+F(1,4)), "rational barrier fixture")
    # Exact multiplier division, with no floating-point comparison.
    for C in [0,1,561,3828,46665,1000000]:
        for x in [F(0),F(1,4),F(1),F(9,4),F(123,7),F(10000)]:
            lhs = ((x+F(1,4))**2-C*(x+F(1,4)))/(x+F(9,4))
            rhs = x-C-F(7,4)+F(4+2*C)/(x+F(9,4))
            need(lhs == rhs, "differential multiplier division")
            need(rhs >= x-C-F(7,4), "positive rational remainder")
    # Explicit m selector uses the analytic integral/log bound in the proof.
    selectors=[]
    for q in [F(0),F(1,2),F(9,8),F(16,5),F(10)]:
        r=ceil_fraction(F(5,2)+3*q)
        m=5*2**r
        need(4+F(2,3)*(r+2) >= 7+2*q, "explicit reservoir selector")
        for L in [F(1,20),F(1,2),F(1),F(2),F(10)]:
            K=ceil_fraction(F(2*(m+2),3)*L)
            need(F(9*(K+1)**2)/(L*L) > 2*gamma_constant(m)+F(7,2),
                 "sine cutoff criterion")
        selectors.append({"qbar":pair(q),"r":r,"m":m})
    # Polynomial endpoint and exponential-moment cancellation identities.
    for L in [F(1,2),F(1),F(3)]:
        phi=polynomial_mul([F(0),F(0),F(1)], [L*L,-2*L,F(1)])
        for extra in [[F(1)],[F(1),F(-2),F(3)]]:
            p=polynomial_mul(phi,extra)
            dp=polynomial_derivative(p)
            ddp=polynomial_derivative(dp)
            h=polynomial_add(ddp,polynomial_scale(p,-F(1,4)))
            need(polynomial_value(p,F(0))==polynomial_value(p,L)==0,
                 "primitive endpoint values")
            need(polynomial_value(dp,F(0))==polynomial_value(dp,L)==0,
                 "primitive endpoint derivatives")
            for c in [F(1,2),-F(1,2)]:
                primitive=polynomial_add(dp,polynomial_scale(p,-c))
                weighted_derivative=polynomial_add(polynomial_derivative(primitive),
                                                    polynomial_scale(primitive,c))
                need(weighted_derivative==h,"exponential moment cancellation identity")
    # A concrete infinite family of admissible high-frequency primitive tests.
    # L=pi/10, frequencies 10k, 10(k+2), 10(k+4); same parity removes endpoints.
    mode_examples=[]
    for k in range(9,31):
        omega=[F(10*(k+2*i)) for i in range(3)]
        v=[w/(w*w+F(9,4)) for w in omega]
        a=[omega[1]*v[2]-omega[2]*v[1],
           omega[2]*v[0]-omega[0]*v[2],
           omega[0]*v[1]-omega[1]*v[0]]
        a=[x/a[0] for x in a]
        need(sum((x*w for x,w in zip(a,omega)),F(0))==0,"sine endpoint cancellation")
        need(sum((x*w/(w*w+F(9,4)) for x,w in zip(a,omega)),F(0))==0,
             "cosh tail moment cancellation")
        n0=sum((x*x for x in a),F(0))
        n1=sum((x*x*w*w for x,w in zip(a,omega)),F(0))
        need(n1 >= 8100*n0, "primitive spectral lower bound")
        need(n1-(3828+F(7,4))*n0 >= n1/2, "actual-source coercivity margin")
        if k==9:
            mode_examples.append({"k":k,"omega":[pair(w) for w in omega],
                                  "coefficients":[pair(x) for x in a],
                                  "norm_ratio":pair(n1/n0)})
    # Exact indefinite rank-two tail, and low/high coupling non-implication.
    for u,v in [(F(1),F(0)),(F(0),F(1)),(F(3,2),F(-2,3))]:
        need(-((u+v)/2)**2+((u-v)/2)**2 == -u*v,"tail cosh/sinh split")
    need(1*1-2*2 == -3 and 1-2-2+1 == -2,"coupling countercontrol")
    hashes={p:hashlib.sha256((HERE/p).read_bytes()).hexdigest()
            for p in ["PROOF.md","SOURCE_LOCK.json","verify.py"]}
    return {
        "status":"EXACT_FINITE_CONTROLS_ONLY",
        "analytic_proof_machine_checked":False,
        "rh_proved":False,
        "check_count":COUNT,
        "actual_Q3_interval":round_out(qlo,qhi),
        "actual_Q3_upper":pair(F(9,8)),
        "gamma_sum_152_margin":pair(s152-F(37,4)),
        "unit_window":{"X":3,"m":152,"C_m":46665,"K":101,
                       "nonpositive_dimension_upper_bound":104},
        "selectors":selectors,
        "three_mode_example":mode_examples,
        "source_hashes":hashes,
    }

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args=parser.parse_args()
    try:
        result=build()
        if args.check is not None and not same(read_json(args.check),result):
            raise ValueError("saved result mismatch (including exact JSON types and source hashes)")
        output=json.dumps(result,sort_keys=True,indent=2)+"\n"
        if args.write is not None: args.write.write_text(output,encoding="utf-8")
        sys.stdout.write(output)
        return 0
    except (ValueError,TypeError,OSError,ZeroDivisionError) as exc:
        print("REFUSED: "+str(exc),file=sys.stderr)
        return 2

if __name__=="__main__":
    raise SystemExit(main())
