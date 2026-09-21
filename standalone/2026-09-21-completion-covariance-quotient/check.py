#!/usr/bin/env python3
"""CQT32: exact finite source-completion and covariance checks.

Standard-library only. All accepting comparisons use integers/Fraction.
No assertions (checks remain active under python -O). This is not an
analytic proof, repository-wide validator, or independent implementation.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys
from typing import Mapping

Source = dict[int, F]
COUNTS: Counter[str] = Counter()

def check(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(f"check failed: {label}")
    COUNTS[label] += 1

def mobius(n: int) -> list[int]:
    if n < 1:
        raise ValueError("positive sieve endpoint required")
    mu = [1] * (n + 1)
    mu[0] = 0
    primes = []
    composite = bytearray(n + 1)
    for p in range(2, n + 1):
        if not composite[p]:
            primes.append(p)
            for j in range(p, n + 1, p):
                composite[j] = 1
                mu[j] = -mu[j]
            for j in range(p*p, n + 1, p*p):
                mu[j] = 0
    return mu

def prime_list(n: int) -> list[int]:
    sieve = bytearray(b'\1') * (n+1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\0' * (((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]

def cleaned(c: Mapping[int,F]) -> Source:
    return {n:F(a) for n,a in c.items() if a}

def add(c: Mapping[int,F], d: Mapping[int,F], scale: F = F(1)) -> Source:
    ans = dict(c)
    for n,a in d.items():
        ans[n] = ans.get(n,F(0)) + scale*a
    return cleaned(ans)

def primitive(c: Mapping[int,F], nmax: int | None = None) -> list[F]:
    end = max(c,default=0) if nmax is None else nmax
    ans = [F(0)]*(end+1)
    for n in range(1,end+1):
        ans[n] = ans[n-1] + c.get(n,F(0))/n
    return ans

def energy(c: Mapping[int,F]) -> F:
    x = primitive(c)
    if x[-1]:
        raise ValueError("energy requested for an unbalanced source")
    return sum((v*v for v in x), F(0))

def complete(y: int) -> Source:
    mu = mobius(y)                 # construction never requests mu past y
    c = {n:F(mu[n]) for n in range(1,y+1) if mu[n]}
    residual = sum((a/n for n,a in c.items()),F(0))
    n = y
    while residual:
        n += 1
        a = min(F(3),n*abs(residual)) * (-1 if residual>0 else 1)
        c[n] = a
        residual += a/n
        if n > 2*y:
            raise ValueError("cap-three completion exceeded proved support")
    return c

def U(c: Mapping[int,F], d: int) -> F:
    return sum((a/n for n,a in c.items() if n%d==0),F(0))

def convolution(c: Mapping[int,F], d: Mapping[int,F], limit: int | None=None) -> Source:
    z: Source = {}
    for a,ca in c.items():
        for b,cb in d.items():
            n=a*b
            if limit is None or n<=limit:
                z[n]=z.get(n,F(0))+ca*cb
    return cleaned(z)

def floor_coefficients(c: Mapping[int,F], d: Mapping[int,F], end: int) -> list[F]:
    """Coefficient of 1*c*d; independent of any future Mobius values."""
    z=convolution(c,d,end)
    out=[F(0)]*(end+1)
    for n,a in z.items():
        for k in range(n,end+1,n):
            out[k]+=a
    return out

def harmonic_output(c: Mapping[int,F], d: Mapping[int,F], end: int) -> list[F]:
    a=floor_coefficients(c,d,end)
    out=[F(0)]*(end+1)
    for n in range(1,end+1):
        out[n]=out[n-1]+a[n]/n
    return out

def three_point(y: int) -> tuple[Source, Source, list[int]]:
    c=complete(y)
    ps=[p for p in prime_list(y) if 4*p>3*(y+1)]
    h: Source={}
    for p in ps:
        h=add(h,{2*p-1:-F(2*p-1,2*p),2*p:F(2),2*p+1:-F(2*p+1,2*p)})
    return c,h,ps

def square_reservoir(y: int) -> tuple[Source,Source,int]:
    c=complete(y)
    r=isqrt(2*y)
    if r*r<2*y:
        r+=1
    h: Source={}
    for p in prime_list(2*y):
        if p<=r:
            continue
        residual=-U(c,p)
        if p<=y:
            t=y//p
            for k in range(t+1,2*t+1):
                if not residual:
                    break
                n=p*k
                a=min(F(8), n*abs(residual))*(1 if residual>0 else -1)
                h[n]=h.get(n,F(0))+a
                residual-=a/n
        elif residual:
            a=p*residual
            h[p]=h.get(p,F(0))+a
            residual=F(0)
        check(not residual,"square_assignment_capacity")
    # Snapshot only assigned terms; reservoirs are NOT recursively assigned.
    for n,a in list(h.items()):
        q=isqrt(n)
        if q*q<n:
            q+=1
        q*=q
        check(q!=n,"assigned_index_nonsquare")
        h[q]=h.get(q,F(0))-F(q,n)*a
    return c,cleaned(h),r

def solve(a: list[list[F]], b: list[F]) -> list[F]:
    """Exact Gaussian elimination; singular systems are rejected explicitly."""
    n=len(b)
    aug=[list(map(F,row))+[F(v)] for row,v in zip(a,b)]
    for j in range(n):
        p=next((i for i in range(j,n) if aug[i][j]),None)
        if p is None:
            raise ValueError("singular matrix")
        aug[j],aug[p]=aug[p],aug[j]
        v=aug[j][j]
        aug[j]=[x/v for x in aug[j]]
        for i in range(n):
            if i!=j:
                v=aug[i][j]
                aug[i]=[x-v*y for x,y in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]

def H_table(n: int) -> list[F]:
    h=[F(0)]*(n+1)
    for k in range(1,n+1):
        h[k]=h[k-1]+F(1,k)
    return h

def exact_str(x: F) -> str:
    return str(x)

def run() -> dict:
    COUNTS.clear()
    three=[]
    for y in (7,15,31,63):
        c,h,ps=three_point(y)
        d=add(c,h)
        bound=(y+1)**2-1
        check(all(d.get(n,F(0))==mobius(y)[n] for n in range(1,y+1)),"retained_prefix")
        check(U(d,1)==0,"reciprocal_balance")
        check(max(map(abs,d.values()))<=3,"retained_cap_three")
        expected=sum((F(1,2*p*p) for p in ps),F(0))
        check(energy(h)==expected,"three_point_exact_cost")
        check(energy(d)==energy(c)+expected,"three_point_total_energy")
        check(expected<=F(1,y),"three_point_cost_bound")
        z=convolution(d,d)
        for p in ps:
            check(U(d,p)==0,"three_point_U_p")
            for q in range(p,max(z)+1,2*p):
                if q%2:
                    check(U(z,q)==0,"all_affected_odd_denominators")
        for i,p in enumerate(ps):
            for r in ps[i+1:]:
                for q,v in ((p*r,0),(2*p*r,-F(2,p*r)),(4*p*r,F(2,p*r))):
                    check(U(z,q)==v,"replacement_amplitude")
        ac=floor_coefficients(c,c,bound)
        ad=floor_coefficients(d,d,bound)
        mu=mobius(bound)     # independent FUTURE source used only for checking
        mc=primitive(c,bound); md=primitive(d,bound)
        qc=harmonic_output(c,c,bound); qd=harmonic_output(d,d,bound)
        for n in range(1,bound+1):
            check(2*c.get(n,F(0))-ac[n]==mu[n],"original_native_coefficient")
            check(2*d.get(n,F(0))-ad[n]==mu[n],"modified_native_coefficient")
            check(qd[n]-qc[n]==2*(md[n]-mc[n]),"complete_output_difference")
        de=sum(((qd[k]-qc[k])**2 for k in range(y+1,bound+1)),F(0))
        check(de==4*expected,"whole_annulus_difference_energy")
        three.append({"Y":y,"protected_primes":ps,"J_h":exact_str(expected),"native_endpoint":bound})
    squares=[]
    for y in (7,15,31,63,127,255):
        c,h,r=square_reservoir(y); d=add(c,h); L=r*r
        check(U(h,1)==0,"square_balance")
        check(min(h,default=y+1)>y and max(h,default=y)<=L,"square_support")
        check(energy(h)<=F(64*(L-y)*(2*r-1)**2,y*y),"square_energy_bound")
        check(energy(h)<=3072,"square_absolute_energy_bound")
        check(energy(d)<=2*energy(c)+2*energy(h),"square_full_energy_paid")
        for p in prime_list(L):
            if p>r:
                check(U(d,p)==0,"square_all_protected_U")
        if y<=31:
            z=convolution(d,d)
            # With support <=R^2, pure rough types are p,p^2,pr only.
            ps=[p for p in prime_list(L) if p>r]
            for i,p in enumerate(ps):
                check(U(z,p)==0 and U(z,p*p)==0,"pure_rough_prime_and_square")
                for q in ps[i+1:]:
                    check(U(z,p*q)==0,"pure_rough_distinct_pair")
        squares.append({"Y":y,"R":r,"J_h":exact_str(energy(h)),"max_source_coefficient":exact_str(max(map(abs,d.values())))})
    graphs=[]
    for y in (7,15,31,63):
        c,h,R=square_reservoir(y); L=R*R
        ps=[p for p in prime_list(L) if p>R]
        coords=list(range(y+1,L))
        A=[[F(int(k%p==0)-int((k+1)%p==0)) for k in coords] for p in ps]
        G=[[sum((x*z for x,z in zip(row,col)),F(0)) for col in A] for row in A]
        u=[U(c,p) for p in ps]
        v=solve(G,u)
        opt=[-sum((v[i]*A[i][j] for i in range(len(ps))),F(0)) for j in range(len(coords))]
        for row,target in zip(A,u):
            check(sum((a*b for a,b in zip(row,opt)),F(0))==-target,"graph_feasibility")
        optimum=sum((x*x for x in opt),F(0))
        check(optimum==sum((a*b for a,b in zip(u,v)),F(0)),"graph_dual_cost")
        check(optimum<=energy(h),"graph_vs_square_reservoir")
        # KKT orthogonality and the exact Pythagorean minimum certificate.
        rs=primitive(h,L)
        diff=[rs[k]-x for k,x in zip(coords,opt)]
        check(sum((x*d for x,d in zip(opt,diff)),F(0))==0,"graph_KKT_orthogonality")
        check(energy(h)==optimum+sum((x*x for x in diff),F(0)),"graph_Pythagorean_certificate")
        rmap={k:x for k,x in zip(coords,opt)}
        hopt={n:n*(rmap.get(n,F(0))-rmap.get(n-1,F(0))) for n in range(y+1,L+1)}
        hopt=cleaned(hopt); copt=add(c,hopt)
        check(U(hopt,1)==0 and energy(hopt)==optimum,"graph_optimizer_realized")
        for p in ps:
            check(U(copt,p)==0,"graph_optimizer_amplitude")
        graphs.append({"Y":y,"L":L,"constraints":len(ps),"minimum_perturbation_energy":exact_str(optimum),
                       "square_reservoir_perturbation_energy":exact_str(energy(h)),
                       "optimized_full_source_energy":exact_str(energy(copt)),
                       "optimized_max_source_coefficient":exact_str(max(map(abs,copt.values())))})
    ward=[]
    for y in (3,7,15,31):
        c=complete(y); b=y+1; end=b*b
        h={b:F(b),b+1:F(-b-1)}
        qcc=harmonic_output(c,c,end)
        qch=harmonic_output(c,h,end)
        qhh=harmonic_output(h,h,end)
        mh=primitive(h,end)
        for k in range(end):
            check(qch[k]==mh[k],"mixed_completion_exact_identity")
            check(qhh[k]==0,"completion_Hessian_zero")
        check(qhh[end]==1,"strict_endpoint_nonzero_control")
        I=range(y+1,end)
        E0=sum((qcc[k]**2 for k in I),F(0))
        inner=sum((qcc[k]*mh[k] for k in I),F(0))
        Jh=sum((mh[k]**2 for k in I),F(0))
        for t in (F(-2),F(-1),F(0),F(1,2),F(2)):
            out=harmonic_output(add(c,h,t),add(c,h,t),end-1)
            E=sum((out[k]**2 for k in I),F(0))
            check(E==E0+4*t*inner+4*t*t*Jh,"full_covariance_polynomial")
        ward.append({"Y":y,"strict_native_endpoint":end-1,"first_nonzero_hh_endpoint":end})
    closure=[]
    for y in (15,31,63,127):
        _,_,ps=three_point(y); end=(y+1)**2-1
        # Accumulate balanced source-ray cross products, not a B_q subset.
        z: Source={}
        for i,p in enumerate(ps):
            rp={p:F(-1),2*p:F(2)}
            for r in ps[i+1:]:
                rr={r:F(-1),2*r:F(2)}
                z=add(z,convolution(rp,rr),F(2))
        co=[F(0)]*(end+1)
        for n,a in z.items():
            if n<=end:
                for k in range(n,end+1,n):
                    co[k]+=a
        out=[F(0)]*(end+1)
        for k in range(1,end+1):
            out[k]=out[k-1]+co[k]/k
        jumps: Source={}
        for i,p in enumerate(ps):
            for r in ps[i+1:]:
                jumps[p*r]=jumps.get(p*r,F(0))+F(2,p*r)
        accum=F(0)
        for k in range(1,end+1):
            accum+=jumps.get(k,F(0))
            check(out[k]==accum,"closed_ray_packet_native_identity")
        E=sum((v*v for v in out),F(0))
        closure.append({"Y":y,"pair_count":len(ps)*(len(ps)-1)//2,"whole_native_closed_packet_energy":exact_str(E),"last_value":exact_str(out[-1])})
    # Four individual closed packets, at points BEFORE, AT and AFTER onset.
    for p,r in ((11,13),(23,29),(29,31),(47,53)):
        rp={p:F(-1),2*p:F(2)}; rr={r:F(-1),2*r:F(2)}
        end=5*p*r; h=H_table(end)
        q=harmonic_output(rp,rr,end)
        for k in (0,p*r-1,p*r,2*p*r-1,2*p*r,4*p*r,5*p*r):
            expected=F(1,p*r)*(h[k//(p*r)]-2*h[k//(2*p*r)]+h[k//(4*p*r)])
            check(q[k]==expected,"closed_single_ray_full_harmonic_formula")
        # At k=pr-1 dropping the d=1,p,r attributed divisor terms is false.
        # For the early-interval expression, use k=max(p,r)+1<2min(p,r).
        k=max(p,r)+1
        incomplete=F(2,p*r)*(h[k]-2*h[k//2]+h[k//4]-2)
        check(incomplete!=0 and q[k]==0,"unclosed_denominator_false_zero_control")
    rectangular=[]
    for a,b in ((3,7),(7,15),(7,31),(15,31),(15,63)):
        c=complete(a); d=complete(b); end=(a+1)*(b+1)-1
        co=floor_coefficients(c,d,end)
        mu=mobius(end)
        for n in range(1,end+1):
            check(c.get(n,F(0))+d.get(n,F(0))-co[n]==mu[n],"rectangular_native_coefficient")
        rectangular.append({"A":a,"B":b,"endpoint":end,"source_lengths":[max(c),max(d)]})
    # Pointwise exact joint-budget optimization, with no coefficient cap.
    joint=[]
    for y,L,lam in ((7,15,F(1)),(15,31,F(4)),(31,63,F(7,2))):
        end=(y+1)**2-1
        mu=mobius(end)  # minimizer is diagnostic; not a source-only upper bound
        m=primitive({n:F(mu[n]) for n in range(1,end+1) if mu[n]},end)
        vals={k:F(2,1)*m[k]/(lam+4) for k in range(y+1,L)}
        d={n:F(mu[n]) for n in range(1,y+1) if mu[n]}
        prev=m[y]
        for n in range(y+1,L+1):
            cur=vals.get(n,F(0)); d[n]=n*(cur-prev); prev=cur
        d=cleaned(d)
        q=harmonic_output(d,d,end); md=primitive(d,end)
        actual=sum((q[k]**2+lam*md[k]**2 for k in range(y+1,end+1)),F(0))
        target=lam/(lam+4)*sum((m[k]**2 for k in range(y+1,L)),F(0))+sum((m[k]**2 for k in range(L,end+1)),F(0))
        check(actual==target,"joint_budget_exact_minimum")
        joint.append({"Y":y,"L":L,"lambda":str(lam),"minimum":str(actual)})
    return {"schema":1,"packet":"CQT32","status":"finite_exact_checks_only_RH_open",
        "construction_uses_future_mobius":False,
        "joint_optimizer_is_future_dependent_diagnostic":True,
        "full_repo_validator_run":False,"independent_review":False,
        "three_point":three,"square_reservoir":squares,"graph":graphs,
        "completion_covariance":ward,"closed_packets":closure,
        "rectangular":rectangular,"joint_budget":joint,
        "counts":dict(sorted(COUNTS.items())),"total_counted_predicates":sum(COUNTS.values())}

def no_duplicate_keys(pairs):
    obj={}
    for key,value in pairs:
        if key in obj:
            raise ValueError(f"duplicate JSON key: {key}")
        obj[key]=value
    return obj

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--write',type=Path)
    group.add_argument('--check',type=Path)
    args=parser.parse_args()
    result=run()
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.write:
        args.write.write_text(text,encoding='utf-8')
    if args.check:
        supplied=json.loads(args.check.read_text(encoding='utf-8'),object_pairs_hook=no_duplicate_keys)
        if supplied!=result:
            raise ValueError("report mismatch (including scope fields)")
    print(json.dumps({"status":"PASS","count":result['total_counted_predicates'],
          "sha256":hashlib.sha256(text.encode()).hexdigest()},sort_keys=True))
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (ValueError,OSError,json.JSONDecodeError) as exc:
        print(f"REFUSED: {exc}",file=sys.stderr)
        raise SystemExit(2)
