"""Rigorously enclose the completed quartic Artin logarithmic derivative at 1."""
from functools import cache
from flint import acb, arb
from check_zhao_cubic_fields_nov18 import run_gp
from check_zhao_quartic_fields_nov18 import polynomial

H=arb(1)/4
J=240


def gamma_factor(s,r):
    return (s/2).gamma()**(3-r)*((s+1)/2).gamma()**r


def boundary_constant(c,r,sigma):
    s=arb(sigma)
    return 2*c**sigma*gamma_factor(s,r)*s.zeta()**3*((s-arb(1)/2)**2/36).exp()


@cache
def base_kernel(r):
    out=[]
    for j in range(J+1):
        s=acb(8,j*H)
        gamma=gamma_factor(s,r)*((s-arb(1)/2)**2/36).exp()
        gamma*=H/(2*arb.pi())*(1 if j==0 else 2)
        out.append((s,gamma*(1/(s-1)+1/s),gamma*(1/(s-1)**2-1/s**2)))
    return out


@cache
def dirichlet_vector(n):
    w=acb(0,-H*arb(n).log()).exp()
    b=arb(1)/n**8
    v=[]
    z=acb(1)
    for j in range(J+1):
        if j%16==0:
            z=w**j
        v.append(b*z)
        z*=w
    return v


def quartic_weight(r,d,poly,tolerance="1e-6"):
    # Absolute errors in the completed function and derivative.
    target=arb(tolerance)
    c=arb(abs(d)).sqrt()/arb.pi()**(arb(3)/2)
    pi=arb.pi()
    strip=(6*pi.sqrt())*(boundary_constant(c,r,2)+boundary_constant(c,r,14))
    strip/=2*pi*((12*pi/H).exp()-1)
    T=J*H
    ends=boundary_constant(c,r,8)*36/T*(-T*T/36).exp()/(2*pi)
    tail_c=(2*c**8*gamma_factor(arb(8),r)*((arb(15)/2)**2/36).exp()
            *(arb(5)/4).zeta()**3*(H+6*pi.sqrt())/(2*pi))
    nmax=int(float((tail_c/target)**(arb(4)/27))*1.01)+2
    series=tail_c/nmax**(arb(27)/4)
    err=strip+ends+series
    if not err<2*target:
        raise ArithmeticError(f"Parameter bounds failed at {d}")
    (coeff,)=run_gp(f'F={polynomial(poly)};N={nmax};\n'
                     'print(dirdiv(dirzetak(nfinit(F),N),vector(N,i,1)));\n')
    if len(coeff)!=nmax or coeff[0]!=1:
        raise ArithmeticError("Missing exact Artin coefficients")
    values=[acb(0) for _ in range(J+1)]
    for n,a in enumerate(coeff,1):
        if a:
            for j,v in enumerate(dirichlet_vector(n)):
                values[j]+=a*v
    den,num=arb(0),arb(0)
    logc=c.log()
    for z,(s,k0,k1) in zip(values,base_kernel(r)):
        value=z*(s*logc).exp()
        den+=(value*k0).real
        num+=(value*k1).real
    den+=arb(0,err.upper())
    num+=arb(0,err.upper())
    if not den>0:
        raise ArithmeticError("Positive completed residue unresolved")
    return 2+arb.const_euler()-(4*pi).log()+2*(num/den-arb(1)/36)


def finish(report):
    decisions=[]
    for r,d,poly in report["unresolved"]:
        for tolerance in ("1e-6","1e-9","1e-12"):
            w=quartic_weight(r,d,poly,tolerance)
            if w<2 or w>2:
                break
        else:
            raise ArithmeticError(f"Unresolved quartic threshold at {poly}")
        if w<2:
            report["accepted"].append([r,d,poly])
        decisions.append([r,d,poly,str(w)])
    report["accepted"].sort()
    report["contour"]=decisions
    report["unresolved"]=[]
    return report


def canonicalize(report):
    polys=sorted({tuple(row[2]) for item in ("accepted","contour") for row in report[item]})
    canonical={}
    for start in range(0,len(polys),128):
        sub=polys[start:start+128]
        v=','.join(polynomial(c) for c in sub)
        rows=run_gp(f'V=[{v}];\nfor(i=1,#V,print(Vec(polredabs(V[i]))));\n')
        if len(rows)!=len(sub):
            raise ArithmeticError("Missing canonical defining polynomial")
        canonical.update(zip(sub,rows))
    for key in ("accepted","contour"):
        for row in report[key]:
            row[2]=canonical[tuple(row[2])]
        report[key].sort()
    return report


if __name__=="__main__":
    import argparse
    import json
    from pathlib import Path
    from flint import ctx
    from check_zhao_quartic_fields_nov18 import GROUPS
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--groups",nargs="+",choices=GROUPS,default=GROUPS)
    args=ap.parse_args()
    ctx.prec=160
    out={}
    for group in args.groups:
        report=json.loads((args.input_dir/f"quartic-{group}-screen.json").read_text())
        out[group]=canonicalize(finish(report))
        print(group,len(report["accepted"]),len(report["contour"]),flush=True)
    args.output.write_text(json.dumps(out,separators=(",",":"))+"\n")
