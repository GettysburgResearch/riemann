#!/usr/bin/env python3
"""Exact fourth-moment degree/singleton census on complete native column windows.
Requires NumPy. No floating-point arithmetic or asymptotic inference is used.
The inherited residue-table helper is authenticated before import.
"""
from pathlib import Path
import argparse
import collections
import hashlib
import importlib.util
import json
import numpy as np

HERE = Path(__file__).resolve().parent
HELPER = HERE.parent / "2026-10-13-native-matching-geometry" / "census_source.py"

def load_source():
    raw = HELPER.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    if blob != "2a074ccede483324392a729056ccbf43a1f26eac":
        raise ValueError("inherited arithmetic source mismatch")
    spec = importlib.util.spec_from_file_location("native_source", HELPER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

c = load_source()
def degree_gram(D,H,k=2):
    if type(D) is not int or type(H) is not int or D < 4 or H < 1:
        raise ValueError("positive integer D>=4 and H>=1 required")
    # A bounded implementation, not a resource-unbounded census promise.
    if D > 8192 or H > 20000:
        raise ValueError("tested implementation caps: D<=8192 and H<=20000")
    ps=c.prime_ideals(D); rr=c.element_rows(H); ideals=c.ideals_through(D,ps)
    cols=[(n,fac) for n,fac,_ in ideals if D<2*n and all(e==1 for _,e in fac)]
    maxdeg=max((len(fac) for _,fac in cols),default=0)
    if not cols or not rr: raise ValueError("empty fixture")
    if maxdeg*12 >= 2**15: raise OverflowError("phase exponent")
    if (D+2)*max(max(abs(a),abs(b)) for a,b in rr) >= 2**63:
        raise OverflowError("row residue arithmetic")
    if k!=2: raise ValueError("pilot k=2 only")
    if 12*max(1,len(rr))*max(1,len(cols))**4>=2**63:raise OverflowError("int64")
    coords=np.array(rr,dtype=np.int64)
    cps=[]
    for q,p,r,tab in ps:
        idx=(coords[:,0]+r*coords[:,1])%p if r is not None else (coords[:,0]%p)*p+coords[:,1]%p
        cps.append(np.array(tab,dtype=np.int8)[idx])
    roots=np.array(c.ROOTS,dtype=np.int64)
    C=np.zeros((6,maxdeg+1,len(rr),2),dtype=np.int64)
    for n,fac in cols:
        ex=np.zeros(len(rr),dtype=np.int16); mask=np.zeros(len(rr),dtype=bool)
        for j,e in fac:
            ex+=cps[j]%6;mask|=cps[j]==6
        ex%=6;ex[mask]=6
        C[((n-1)//6)%6,len(fac)]+=roots[ex]
    B=np.zeros((6,2*maxdeg+1,len(rr),2),dtype=np.int64)
    nonzero=[(a,j) for a in range(6) for j in range(maxdeg+1) if np.any(C[a,j])]
    for a,j in nonzero:
        x=C[a,j]
        for b,l in nonzero:
            y=C[b,l]
            B[(a+b)%6,j+l,:,0]+=x[:,0]*y[:,0]-x[:,1]*y[:,1]
            B[(a+b)%6,j+l,:,1]+=x[:,0]*y[:,1]+x[:,1]*y[:,0]-x[:,1]*y[:,1]
    outG=[]
    for a in range(6):
        X=B[a,:,:,0];Y=B[a,:,:,1]
        G=X@X.T-X@Y.T+Y@Y.T
        Gomega=Y@X.T-X@Y.T
        # Field conjugation reindexes the complete norm window and row ball.
        if np.any(Gomega): raise ValueError("complex Gram block")
        outG.append(G)
    # check distinct unit types vanish, all j,l
    for a in range(6):
        for b in range(a+1,6):
            X,Y=B[a,:,:,0],B[a,:,:,1]
            Z,T=B[b,:,:,0],B[b,:,:,1]
            if np.any(X@Z.T-X@T.T+Y@T.T) or np.any(Y@Z.T-X@T.T):raise ValueError("unit type failed")
    G=sum(outG)
    v=np.array([(-1)**j for j in range(2*maxdeg+1)],dtype=np.int64)
    mm=int(v@G@v);mp=int(G.sum())
    fourier=[int(np.trace(G,offset=l)) for l in range(len(G))]
    # d/dx sum_l>=1 2 R_l T_l(x) evaluated at x=-1: T'_l(-1)=(-1)^(l-1)l²
    deriv_minus1=2*sum(fourier[l]*(-1)**(l-1)*l*l for l in range(1,len(fourier)))
    return {"D":D,"H":H,"rows":len(rr),"columns":len(cols),"max_degree":maxdeg,
           "degree_gram":G.tolist(),"unit_blocks":[gg.tolist() for gg in outG],
           "M4_mobius":mm,"M4_unsigned":mp,"degree_diagonal":fourier[0],
           "fourier_positive":fourier,"d_dx_at_minus_one":deriv_minus1}, (ps,rr,cols,cps,B)

def no_singleton_gram(D,H,aux):
    if D > 1024:
        raise ValueError("full singleton resolution is capped at D<=1024")
    ps,rr,cols,cps,B=aux
    products=c.product_counts([fac for n,fac in cols],2)
    faces=sorted(products)
    mults=[products[f] for f in faces]
    supp=[sum(1<<j for j,e in fac) for fac in faces]
    singles=[sum(1<<j for j,e in fac if e==1) for fac in faces]
    degrees=[sum(e for j,e in fac) for fac in faces]
    types=[sum(e*((ps[j][0]-1)//6) for j,e in fac)%6 for fac in faces]
    idxsets=collections.defaultdict(set)
    bytype=collections.defaultdict(set)
    for i,fac in enumerate(faces):
        bytype[types[i]].add(i)
        for j,e in fac:idxsets[j].add(i)
    phases=[]
    for f in faces:
        a=np.zeros(len(rr),dtype=np.int16);z=np.zeros(len(rr),dtype=bool)
        for j,e in f:
            a+=(cps[j]%6)*e;z|=(cps[j]==6)
        a%=6;a[z]=6;phases.append(a.astype(np.int8))
    A=np.array(phases)
    lut=np.array([[0 if a==6 or b==6 else [2,1,-1,-2,-1,1][(a-b)%6]
                   for b in range(7)] for a in range(7)],dtype=np.int8)
    dim=max(degrees)+1
    twice=np.zeros((dim,dim),dtype=np.int64)
    principal=np.zeros_like(twice)
    validpairs=0
    for i,fac in enumerate(faces):
        needed=[j for j,e in fac if e==1]
        if needed:
            pool=min([idxsets[j] for j in needed],key=len)
        else:
            pool=bytype[types[i]]
        for j in pool:
            if j<i or types[i]!=types[j] or singles[i]&~supp[j] or singles[j]&~supp[i]:
                continue
            validpairs+=1
            ker=int(np.sum(lut[A[i],A[j]],dtype=np.int64))
            val=ker*mults[i]*mults[j]
            d,e=degrees[i],degrees[j]
            twice[d,e]+=val
            if i==j:principal[d,e]+=val
            else:twice[e,d]+=val
    if np.any(twice%2) or np.any(principal%2): raise ValueError("half integer totals")
    N=twice//2;P=principal//2
    vv=np.array([(-1)**i for i in range(dim)],dtype=np.int64)
    return {"no_singleton_degree_gram":N.tolist(),
            "principal_degree_gram":P.tolist(),
            "no_singleton_mobius":int(vv@N@vv),
            "no_singleton_unsigned":int(N.sum()),
            "principal_total":int(P.sum()),"qualifying_product_pairs":validpairs,
            "product_count":len(faces)}


def run_case(D, H, singleton=True):
    result, aux = degree_gram(D, H)
    ps, rows, columns, _, _ = aux
    # Independent full-moment assembly from the inherited original column loop.
    arrays, _ = c.native_arrays(D, rows, c.ideals_through(D, ps), ps)
    for source, label in (("mobius", "M4_mobius"),
                          ("squarefree_unsigned", "M4_unsigned")):
        total = sum((int(a)*int(a)-int(a)*int(b)+int(b)*int(b))**2
                    for a, b in arrays[source])
        if total != result[label]:
            raise ValueError("direct native moment reconstruction")
    if singleton:
        result.update(no_singleton_gram(D, H, aux))
        prefix = c.row_count_prefix(rows, H)
        reference = c.principal_fourth([f for n, f in columns], H, prefix, ps)
        if reference["principal_total"] != result["principal_total"]:
            raise ValueError("independent principal mask reconstruction")
        result["singleton_mobius"] = result["M4_mobius"] - result["no_singleton_mobius"]
        result["singleton_unsigned"] = result["M4_unsigned"] - result["no_singleton_unsigned"]
        result["remainder_nonprincipal"] = result["M4_mobius"] - result["principal_total"]
    return result

def suite():
    cases = [run_case(D, c.ceil_power_21_20(D), D<=1024)
             for D in (64,128,256,512,1024,2048,4096,8192)]
    # Retain the earlier exploratory sharp-height witness as well.
    pilot = run_case(512, 512, True)
    return {
        "status": "EXACT_FINITE_CENSUS_NOT_AN_ASYMPTOTIC_BOUND",
        "source_blob": "2a074ccede483324392a729056ccbf43a1f26eac",
        "scope": "All good squarefree ideals in D/2<Nn<=D; every nonzero element row in Nu<=H. Full fourth moments and unit/degree Grams through 8192; all-singleton versus no-singleton resolution only through 1024.",
        "cases": cases, "sharp_height_pilot": pilot}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--D", type=int)
    parser.add_argument("--H", type=int)
    parser.add_argument("--no-singletons", action="store_true",
                        help="omit the more expensive complete singleton resolution")
    args = parser.parse_args()
    if args.D is None:
        if args.H is not None:
            parser.error("--H requires --D")
        report = suite()
    else:
        height = args.H if args.H is not None else c.ceil_power_21_20(args.D)
        report = run_case(args.D, height, not args.no_singletons and args.D<=1024)
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))

if __name__ == "__main__":
    main()
