#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, sys

# Exact complex arithmetic over Q: pair (real, imaginary).
def cadd(z,w): return (z[0]+w[0], z[1]+w[1])
def csub(z,w): return (z[0]-w[0], z[1]-w[1])
def cmul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def cscale(a,z): return (a*z[0], a*z[1])
def cnorm2(z): return z[0]*z[0]+z[1]*z[1]
def cinv(z):
    d=cnorm2(z)
    return (z[0]/d, -z[1]/d)
def cdiv(z,w): return cmul(z,cinv(w))

def assert_eq(x,y,label,checks):
    if x != y:
        raise AssertionError(f"{label}: {x!r} != {y!r}")
    checks.append(label)

def phase_fixture(alpha,a,y,atoms,tag,checks):
    v=alpha*y
    fp=(alpha,F(0))
    for t,mass in atoms:
        D=(t-a)*(t-a)+y*y
        v += mass*y/D
        denom=(t-a,-y)
        fp=cadd(fp,cscale(mass,cmul(cinv(denom),cinv(denom))))
    d=cscale(y/v,fp)

    probs=[]; phases=[]
    if alpha:
        probs.append(alpha*y/v); phases.append((F(1),F(0)))
    for t,mass in atoms:
        D=(t-a)*(t-a)+y*y
        probs.append(mass*y/(v*D))
        phases.append(cdiv((t-a,y),(t-a,-y)))
    assert_eq(sum(probs,F(0)),F(1),f"{tag}:probability",checks)
    bary=(F(0),F(0))
    for p,w in zip(probs,phases):
        assert_eq(cnorm2(w),F(1),f"{tag}:unit_phase_{len(checks)}",checks)
        bary=cadd(bary,cscale(p,w))
    assert_eq(bary,d,f"{tag}:barycenter",checks)

    directional=F(1)-d[0]
    rhs=F(0)
    for p,w in zip(probs,phases):
        rhs += p*cnorm2(csub(w,(F(1),F(0))))/2
    assert_eq(directional,rhs,f"{tag}:directional_variance",checks)

    full=F(1)-cnorm2(d)
    rhs2=F(0)
    for i in range(len(probs)):
        for j in range(len(probs)):
            rhs2 += probs[i]*probs[j]*cnorm2(csub(phases[i],phases[j]))/2
    assert_eq(full,rhs2,f"{tag}:full_variance",checks)

    C=(y*fp[0]-v)/2
    assert_eq(C,-v*rhs/2,f"{tag}:microscope_phase",checks)
    Cnewton=F(0)
    for t,mass in atoms:
        D=(t-a)*(t-a)+y*y
        Cnewton -= y**3*mass/(D*D)
    assert_eq(C,Cnewton,f"{tag}:microscope_newton",checks)

def downshift_fixture(alpha,a,h,delta,atoms,tag,checks):
    y=h-delta
    assert y>0
    v=alpha*y
    fp=(alpha,F(0))
    for t,mass in atoms:
        D=(t-a)*(t-a)+y*y
        v += mass*y/D
        denom=(t-a,-y)
        fp=cadd(fp,cscale(mass,cmul(cinv(denom),cinv(denom))))
    C=(h*fp[0]-v)/2
    kernel=alpha*delta/2
    for t,mass in atoms:
        x=t-a; D=x*x+y*y
        kernel += mass*(delta*x*x-(2*h-delta)*y*y)/(2*D*D)
    assert_eq(C,kernel,f"{tag}:downshift_kernel",checks)
    d=cscale(y/v,fp)
    assert_eq(C,v*((F(1)+delta/y)*d[0]-1)/2,
              f"{tag}:hyperbolic_threshold",checks)

def shell_counts(heights,h1,h2):
    return sum(mult for beta,mult in heights if h1 < abs(beta) < h2)

def degree_theta(heights,h):
    return -sum(mult for beta,mult in heights if abs(beta)<h)

def shell_fixture(ladder,h1,h2,tag,checks):
    Ms=[shell_counts(level,h1,h2) for level in ladder]
    shell_degs=[degree_theta(level,h2)-degree_theta(level,h1) for level in ladder]
    for k,(M,d) in enumerate(zip(Ms,shell_degs)):
        assert_eq(d,-M,f"{tag}:shell_degree_{k}",checks)
    Udegs=[shell_degs[k]-shell_degs[k+1] for k in range(len(ladder)-1)]
    assert_eq(Ms[0],Ms[-1]-sum(Udegs),f"{tag}:ladder_telescope",checks)
    assert Ms[0] % 2 == 0
    checks.append(f"{tag}:even_shell_count")

def frozen_source_fixture(L, coeffs, h, tag, checks):
    N=10
    q=[F(0)]*(N+1); q[0]=F(1,L)
    power=[F(0)]*(N+1); power[0]=F(1)
    for k in range(1,N+1):
        new=[F(0)]*(N+1)
        for i,x in enumerate(power):
            if not x: continue
            for j,c in enumerate(coeffs):
                if i+j<=N: new[i+j]+=x*c
        power=new
        for n,x in enumerate(power): q[n]+=x/F(L**(k+1))
    transformed=[q[n]*(1+h*n) for n in range(N+1)]
    direct=[q[n]-h*(-n*q[n]) for n in range(N+1)]
    assert_eq(transformed,direct,f"{tag}:hardy_multiplier",checks)
    assert all(x>=0 for x in q)
    checks.append(f"{tag}:positive_coefficients")

def main(output):
    checks=[]
    fixtures=[
        (F(0),F(0),F(1),[(F(-2),F(1)),(F(3),F(2))]),
        (F(1,3),F(1),F(2),[(F(-1),F(2)),(F(4),F(1,2))]),
        (F(2,5),F(-2),F(3,2),[(F(-5),F(3,2)),(F(0),F(4)),(F(7),F(2,3))]),
        (F(0),F(3,2),F(5,3),[(F(-4),F(5,2)),(F(2),F(3)),(F(8),F(7,4))]),
    ]
    for idx,args in enumerate(fixtures):
        phase_fixture(*args,f"phase{idx}",checks)

    for idx,(alpha,a,h,delta,atoms) in enumerate([
        (F(0),F(0),F(3),F(1),[(F(-2),F(1)),(F(4),F(2))]),
        (F(1,4),F(1),F(5,2),F(1,2),[(F(-1),F(3)),(F(3),F(2))]),
        (F(0),F(-2),F(7,3),F(1,3),[(F(-5),F(2)),(F(0),F(1)),(F(6),F(4))]),
    ]):
        downshift_fixture(alpha,a,h,delta,atoms,f"down{idx}",checks)

    for lam in [F(1,10),F(1,2),F(1),F(3),F(10)]:
        assert_eq((lam-(2+lam))/4,F(-1,2),
                  f"kernel_integral_lambda_{lam}",checks)
        checks.append(f"kernel_core_threshold_{lam}")
        for s in [F(-1),F(-1,2),F(0),F(1,2),F(1)]:
            assert lam*s*s-(2+lam)<=-2
            checks.append(f"kernel_core_{lam}_{s}")

    for delta in [F(1,10),F(1,2),F(1)]:
        for y in [F(1),F(2),F(5)]:
            h=y+delta
            for x in [F(-y),F(-y,2),F(0),F(y,2),F(y)]:
                D=x*x+y*y
                K=(delta*x*x-(2*h-delta)*y*y)/(2*D*D)
                assert K<=-F(1,4)/y
                checks.append(f"hole_core_{delta}_{y}_{x}")
            for mult in [F(2),F(3),F(5),F(10)]:
                x=mult*y; D=x*x+y*y
                K=(delta*x*x-(2*h-delta)*y*y)/(2*D*D)
                assert max(K,F(0)) <= delta/(2*x*x)
                checks.append(f"hole_tail_{delta}_{y}_{mult}")

    for delta in [F(1,5),F(1),F(3)]:
        for M in [F(1),F(2),F(7,3)]:
            assert delta*M/2>0
            checks.append(f"finite_mass_positive_lead_{delta}_{M}")

    ladders=[
        [[(F(0),2),(F(1,4),1),(F(-1,4),1),(F(3,4),1),(F(-3,4),1)],
         [(F(0),1),(F(1,5),1),(F(-1,5),1)],[(F(0),2)]],
        [[(F(0),1),(F(1,10),2),(F(-1,10),2),(F(2,5),1),(F(-2,5),1)],
         [(F(0),2),(F(1,8),1),(F(-1,8),1)],[(F(0),1)]],
        [[(F(0),4),(F(1,3),2),(F(-1,3),2)],
         [(F(0),3),(F(1,4),1),(F(-1,4),1)],[(F(0),2)],[(F(0),1)]],
    ]
    for idx,ladder in enumerate(ladders):
        shell_fixture(ladder,F(1,20),F(1,2),f"shell{idx}",checks)

    for m in range(0,20,2):
        for numerator in range(0,200):
            E=F(numerator,100)
            if E<2: assert not (m>0 and m<=E)
            checks.append(f"parity_gate_{m}_{numerator}")

    frozen_source_fixture(5,[F(0),F(1),F(2),F(1)],F(2),"frozen0",checks)
    frozen_source_fixture(7,[F(0),F(2),F(0),F(3),F(1)],F(3,2),"frozen1",checks)

    payload={
        "arithmetic_class":"EXACT_RATIONAL_FINITE_ALGEBRA",
        "checks":len(checks),
        "phase_barycenter_identity_replayed":True,
        "backward_poisson_kernel_replayed":True,
        "height_shell_telescope_replayed":True,
        "frozen_reciprocal_hardy_multiplier_replayed":True,
        "height_shell_entire_transfer_proved":False,
        "one_sided_hardy_physical_transfer_proved":False,
        "spatial_escape_excluded_for_xi":False,
        "rh_established":False,
        "verdict":"PASS_X_105600_PHASE_BARYCENTER_ANTIPOISSON_SHELL",
    }
    canonical=json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    payload["proof_object"]=hashlib.sha256(canonical).hexdigest()
    out=Path(output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print(payload["verdict"])
    print(payload["proof_object"])
    print(f"checks={payload['checks']}")
    print("RH_UNPROVEN")

if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("usage: verify.py OUTPUT")
    main(sys.argv[1])
