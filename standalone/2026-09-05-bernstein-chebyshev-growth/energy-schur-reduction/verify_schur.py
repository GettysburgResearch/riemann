#!/usr/bin/env python3
"""Exact finite controls for ES-1--ES-5. Does NOT certify the actual S_L sign."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
PARENT = 'ddeca90f7aa6facd77841d38207aabe38d7a8f53'
PINS = {
    '../finite-window-coercivity/PROOF.md': '35d8d38a77bee896b0b2e729b095ccdef5d7a50f',
    '../local-window-positivity/PROOF.md': '8d7120ef2edc0ac033a4814eb61917652fc57ba8',
    '../cross-route-hardy-laguerre/BRIDGE.md': '81d7d5db7a25f5875a08c10235fdb514d67cc744',
}

class Rejected(ValueError):
    pass

class Counter:
    def __init__(self) -> None:
        self.groups: dict[str, int] = {}
    def check(self, group: str, condition: bool) -> None:
        if not condition:
            raise Rejected('control failed: ' + group)
        self.groups[group] = self.groups.get(group, 0) + 1


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def no_duplicate(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    obj: dict[str, Any] = {}
    for k, v in pairs:
        if k in obj:
            raise Rejected('duplicate JSON key: ' + k)
        obj[k] = v
    return obj

def load(path: Path) -> Any:
    return json.loads(path.read_text(), object_pairs_hook=no_duplicate,
                      parse_constant=lambda s: (_ for _ in ()).throw(Rejected('nonfinite JSON')))

def encode(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + '\n'

def authentic() -> dict[str, str]:
    lock = load(ROOT / 'SOURCE_LOCK.json')
    expected = {'publication_parent': PARENT, 'parent_blobs': PINS}
    if encode(lock) != encode(expected):
        raise Rejected('source lock mismatch')
    for path, sha in PINS.items():
        if git_blob((ROOT / path).read_bytes()) != sha:
            raise Rejected('parent blob mismatch: ' + path)
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in ('PROOF.md', 'SOURCE_LOCK.json', 'verify_schur.py')}

# Small exact polynomial package, coefficients in ascending powers.
def trim(p: list[F]) -> list[F]:
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p or [F(0)]
def add(p: list[F], q: list[F]) -> list[F]:
    n = max(len(p), len(q))
    return trim([(p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0)) for i in range(n)])
def scale(p: list[F], c: F) -> list[F]:
    return trim([c*x for x in p])
def mul(p: list[F], q: list[F]) -> list[F]:
    r = [F(0)] * (len(p)+len(q)-1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)
def deriv(p: list[F]) -> list[F]:
    return trim([F(i)*p[i] for i in range(1, len(p))])
def anti(p: list[F]) -> list[F]:
    return [F(0)] + [x/F(i+1) for i, x in enumerate(p)]
def val(p: list[F], x: F) -> F:
    y = F(0)
    for a in reversed(p):
        y = y*x+a
    return y
def integ(p: list[F], a: F=F(0), b: F=F(1)) -> F:
    q = anti(p)
    return val(q,b)-val(q,a)
def shift(p: list[F], d: F) -> list[F]:
    """p(t-d)."""
    out = [F(0)]*len(p)
    for j, x in enumerate(p):
        for k in range(j+1):
            out[k] += x*comb(j,k)*(-d)**(j-k)
    return trim(out)
def abs_kernel(z: list[F], d: F, a: F, b: F) -> list[F]:
    """Integral |t-u-d|z(u)du, for t on a segment not crossing d or d+1."""
    mid = (a+b)/2-d
    m0, m1 = integ(z), integ(mul([F(0),F(1)],z))
    if mid <= 0:
        return [m1+d*m0, -m0]
    if mid >= 1:
        return [-(m1+d*m0), m0]
    p = [F(0),F(0)] + [2*x/F((j+1)*(j+2)) for j,x in enumerate(z)]
    return add(shift(p,d), [m1+d*m0,-m0])
def kernel_segments(z: list[F], terms: list[tuple[F,F]]) -> list[tuple[F,F,list[F]]]:
    breaks = sorted({F(0),F(1)} | {r for _,d in terms for r in (d,d+1) if 0<r<1})
    out = []
    for a,b in zip(breaks,breaks[1:]):
        # A constant kernel as well as shifted absolute-value cusps.
        k = [integ(z)]
        for weight, d in terms:
            k = add(k,scale(abs_kernel(z,d,a,b),weight))
        out.append((a,b,k))
    return out

def polynomial_controls(c: Counter) -> None:
    bump = [F(0),F(0),F(1),F(-2),F(1)] # t^2(1-t)^2, clamped
    kernels = [[(F(1),F(0))], [(F(-1),F(0)),(F(1,3),F(1,2)),(F(1,3),F(-1,2))],
               [(F(2),F(1,4)),(F(2),F(-1,4)),(F(-3,2),F(0))]]
    for order in range(5):
        phi = [F(0)]*order + bump
        v = add(deriv(deriv(phi)),scale(phi,F(-1,4)))
        c.check('clamped_endpoint_algebra', all(val(phi,x)==0 and val(deriv(phi),x)==0 for x in (F(0),F(1))))
        for z in ([F(1)],[F(0),F(1)],[F(2),F(-3),F(1)]):
            for terms in kernels:
                lhs = rhs = F(0)
                cumulative = F(0)
                prior = None
                for a,b,k in kernel_segments(z,terms):
                    if prior is not None:
                        c.check('cusp_continuity',val(prior,a)==val(k,a))
                    j = anti(k)
                    j[0] += cumulative-val(j,a)
                    f = add(scale(deriv(k),F(-1)),scale(j,F(1,4)))
                    lhs += integ(mul(v,k),a,b)
                    rhs += integ(mul(deriv(phi),f),a,b)
                    cumulative = val(j,b)
                    prior = k
                c.check('weak_residual_identity',lhs==rhs)
    # Independent exact projection away from the constant residual direction.
    for n in range(1,7):
        p = [F(0)]*n+[F(1)]
        centered = add(p,[-integ(p)])
        c.check('residual_projection',integ(centered)==0)
        c.check('residual_projection',integ(mul(centered,centered)) <= integ(mul(p,p)))

# Exact dense matrix controls, all small and explicitly synthetic.
def zeros(n: int, m: int) -> list[list[F]]:
    return [[F(0) for _ in range(m)] for _ in range(n)]
def trans(A: list[list[F]]) -> list[list[F]]:
    return list(map(list,zip(*A)))
def mm(A: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    return [[sum((a*b for a,b in zip(row,col)),F(0)) for col in zip(*B)] for row in A]
def ma(A: list[list[F]], B: list[list[F]], sign: int=1) -> list[list[F]]:
    return [[x+sign*y for x,y in zip(a,b)] for a,b in zip(A,B)]
def inverse(A: list[list[F]]) -> list[list[F]]:
    n=len(A)
    C=[row[:] + [F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next((k for k in range(j,n) if C[k][j]),None)
        if k is None:
            raise Rejected('singular exact matrix')
        C[j],C[k]=C[k],C[j]
        pivot=C[j][j]
        C[j]=[v/pivot for v in C[j]]
        for k in range(n):
            if k!=j:
                t=C[k][j]
                C[k]=[x-t*y for x,y in zip(C[k],C[j])]
    return [r[n:] for r in C]
def determinant(A: list[list[F]]) -> F:
    n=len(A)
    if n==0:return F(1)
    out=F(0)
    for perm in itertools.permutations(range(n)):
        prod=F(1)
        for i in range(n):prod*=A[i][perm[i]]
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        out+=(-1)**inv*prod
    return out
def psd(A: list[list[F]]) -> bool:
    n=len(A)
    if A!=trans(A):return False
    for r in range(1,n+1):
        for inds in itertools.combinations(range(n),r):
            if determinant([[A[i][j] for j in inds] for i in inds])<0:return False
    return True
def quad(A: list[list[F]], x: list[F]) -> F:
    return mm([x],mm(A,trans([x])))[0][0]

def matrix_controls(c: Counter) -> dict[str, Any]:
    last={}
    for n in (3,5,7):
        U=[[F(((i+1)*(j+2))%7-3,10) for j in range(2)] for i in range(n)]
        H=mm(U,trans(U))
        for i in range(n):H[i][i]+=1+F(i,3)
        Hi=inverse(H)
        B=[[F(((i+2)*(j+3))%11-5,13) for j in range(3)] for i in range(n)]
        exact=mm(Hi,B)
        for diag in ([F(1,5),F(1,3),F(2,7)], [F(-1,8),F(1,4),F(1,2)], [F(0),F(0),F(1,2)]):
            S=zeros(3,3)
            for i in range(3):S[i][i]=diag[i]
            C=ma(S,mm(trans(B),exact))
            prev=C
            for m in range(n+1):
                trial=zeros(n,3)
                if m:
                    active=mm(inverse([r[:m] for r in H[:m]]), B[:m])
                    trial[:m]=active
                residual=ma(B,mm(H,trial),-1)
                Um=ma(ma(ma(C,mm(trans(B),trial),-1),mm(trans(trial),B),-1),mm(trans(trial),mm(H,trial)))
                error=mm(trans(residual),mm(Hi,residual))
                c.check('schur_exact_remainder',ma(Um,S,-1)==error)
                c.check('schur_upper_direction',psd(error))
                c.check('galerkin_monotonicity',psd(ma(prev,Um,-1)))
                crude=mm(trans(residual),residual)
                c.check('residual_lower_bound',psd(ma(crude,error,-1))) # H>=I
                if m==n:c.check('complete_finite_elimination',Um==S)
                for x in ([F(1),F(-2),F(3)],[F(-1,2),F(1,3),F(2,5)]):
                    c.check('complex_polarization_parts',quad(ma(Um,S,-1),x)==quad(error,x))
                prev=Um
            # Non-Galerkin trial: the enclosure does not require exact minimizers.
            trial=[[F(i-j,17) for j in range(3)] for i in range(n)]
            R=ma(B,mm(H,trial),-1)
            Q=ma(ma(ma(C,mm(trans(B),trial),-1),mm(trans(trial),B),-1),mm(trans(trial),mm(H,trial)))
            c.check('arbitrary_trial_identity',ma(Q,S,-1)==mm(trans(R),mm(Hi,R)))
            c.check('arbitrary_trial_enclosure',psd(ma(mm(trans(R),R),ma(Q,S,-1),-1)))
            last={'n':n,'signed_schur_diagonal':[str(x) for x in diag]}
    # Simple counterexample: two positive diagonal restrictions, negative coupled form.
    A=[[F(1),F(2)],[F(2),F(1)]]
    c.check('positive_blocks_not_positive_form',A[0][0]>0 and A[1][1]>0 and quad(A,[F(1),F(-1)])<0)
    # The residual lower bound can both accept and correctly reject.
    c.check('certificate_positive_control',psd([[F(1,2)-3*F(1,20),F(0)],[F(0),F(1,3)-3*F(1,100)]]))
    c.check('certificate_negative_control',not psd([[F(1,20)-3*F(1,2)]]))
    return last

def compact_controls(c: Counter) -> dict[str, Any]:
    values={}
    for C in (F(1,2),F(1,3),F(1,4)):
        S=C-F(1,3)
        for M in range(1,13):
            partial=sum((F(1,4)**j for j in range(1,M+1)),F(0))
            SM=C-partial
            c.check('compact_energy_completion',SM-S==F(1,3)*F(1,4)**M)
            # Ordinary inverse would need a vector with norm squared M.
            c.check('ordinary_inverse_divergence',sum(F(1) for _ in range(M))==M)
            # If b_j=2^-j instead, completing M coordinates gives C-M.
            bad=sum((F(1,4)**j*F(2)**(2*j)-2*F(1,2)**j*F(2)**j for j in range(1,M+1)),F(0))+C
            c.check('unbounded_coupling_control',bad==C-M)
        values[str(C)]={'limiting_schur':str(S),'first':str(C-F(1,4)),
                        'second':str(C-F(1,4)-F(1,16))}
    return values

def scalar_source_controls(c: Counter) -> None:
    def log_bounds(x: F, N: int=24) -> tuple[F,F]:
        y=(x-1)/(x+1)
        low=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
        high=low+2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
        return low, high
    ln2low=log_bounds(F(2),3)[0]
    H32=sum((F(1,j) for j in range(1,33)),F(0))
    c.check('actual_scalar_barrier',H32-5*ln2low<F(3,5))
    c.check('actual_scalar_barrier',F(3,5)+F(11,7)+F(21,10)+F(6,5)<F(11,2))
    low2,low3=F(1414213,1000000),F(1732050,1000000)
    c.check('actual_scalar_barrier',low2*low2<2)
    c.check('actual_scalar_barrier',low3*low3<3)
    q_upper=log_bounds(F(2))[1]/low2+log_bounds(F(3))[1]/low3
    c.check('actual_scalar_barrier',q_upper<F(9,8))
    s92=sum((F(4,4*k+1) for k in range(93)),F(0))
    c.check('actual_scalar_barrier',s92>F(35,4))
    c.check('actual_scalar_barrier',F(35,4)==1+F(11,2)+2*F(9,8))
    C=93*185
    c.check('actual_scalar_barrier',C==17205)
    c.check('actual_scalar_barrier',9*102**2==93636)
    c.check('actual_scalar_barrier',F(3,2)*(1-(C+F(7,4))/F(93636))>=F(6,5))
    c.check('actual_scalar_barrier',F(3,2)**2/F(6,5)==F(15,8))
    c.check('actual_scalar_barrier',F(3,2)**2/F(3,4)==3)

def reconstruct() -> dict[str, Any]:
    hashes=authentic()
    c=Counter()
    scalar_source_controls(c)
    polynomial_controls(c)
    matrices=matrix_controls(c)
    compact=compact_controls(c)
    return {'format_version':1,'arithmetic':'EXACT_RATIONAL',
            'component_proofs_machine_checked':False,
            'actual_schur_sign_computed':False,'rh_proved':False,
            'parent':PARENT,'source_sha256':hashes,'checks':sum(c.groups.values()),
            'groups':c.groups,'last_matrix_fixture':matrices,'compact_controls':compact}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',type=Path)
    p.add_argument('--write',type=Path)
    args=p.parse_args()
    if args.check and args.write:
        p.error('use --check OR --write')
    try:
        result=reconstruct()
        text=encode(result)
        if args.check and encode(load(args.check))!=text:
            raise Rejected('saved result mismatch')
        if args.write:args.write.write_text(text)
        print(text,end='')
        return 0
    except (Rejected,OSError,ValueError,TypeError) as exc:
        print('REFUSED: '+str(exc))
        return 2
if __name__=='__main__':
    raise SystemExit(main())
