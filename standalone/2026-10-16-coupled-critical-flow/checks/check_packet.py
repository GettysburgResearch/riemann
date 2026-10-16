#!/usr/bin/env python3
"""Exact finite checks, not an analytic or RH certificate. Standard library only.

The arithmetic helper is an unchanged #936 source. The field fixtures include
all allowed 0/1/m columns of a NAMED THREE-PRIME SEMIGROUP, not all field ideals.
No assertions are used as acceptance gates; python -O must give identical output.
"""
from __future__ import annotations
import hashlib
import itertools
import json
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
import eisenstein_source as E

counts = defaultdict(int)
negative_controls = []
ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))


def check(ok, label):
    counts[label] += 1
    if not ok:
        raise RuntimeError(f"{label}: failed check {counts[label]}")


def neg_control(ok, name):
    check(ok, "negative_controls")
    negative_controls.append(name)


def add(a, b): return E.add(a, b)
def mul(a, b): return E.mul(a, b)
def cj(a): return E.conj(a)
def sc(a, c): return E.scale(a, c)
def real(a): return a[0] + a[1] / 2

def series_mul(a, b, length):
    out = [ZERO] * length
    for i, x in enumerate(a):
        if x == ZERO: continue
        for j, y in enumerate(b[:length-i]):
            if y != ZERO: out[i+j] = add(out[i+j], mul(x, y))
    return out


def inverse(a, length):
    check(a[0] == ONE, "series_unit_setup")
    out = [ONE] + [ZERO] * (length-1)
    for n in range(1, length):
        s = ZERO
        for j in range(1, min(n+1, len(a))):
            s = add(s, mul(a[j], out[n-j]))
        out[n] = sc(s, -1)
    return out


def series_checks():
    local_cases = 0
    phases = [ONE, E.ROOTS[1], E.ROOTS[2], E.ROOTS[3], ZERO]
    for q, m, a, b in itertools.product((2, 3, 7, 25), (2, 4, 6, 8), phases, phases):
        length = 2*m+3
        r, h = Q(1, q), Q(q**(m//2-1))
        F = [ONE] + [ZERO]*(length-1)
        F[1], F[m] = sc(a, -(1-r)), sc(b, -h)
        first = [ONE, sc(a, -1)] + [ZERO]*(length-2)
        powerful = [ONE] + [ZERO]*(length-1)
        powerful[m] = sc(b, -h)
        den = series_mul(first, powerful, length)
        u = series_mul(F, inverse(den, length), length)
        ui = series_mul(den, inverse(F, length), length)
        j = series_mul(F, inverse(first, length), length)
        ji = series_mul(first, inverse(F, length), length)
        for lhs, rhs in (
            (series_mul(den, u, length), F),
            (series_mul(u, ui, length), [ONE]+[ZERO]*(length-1)),
            (series_mul(powerful, u, length), j),
            (series_mul(inverse(powerful, length), ui, length), ji),
            (series_mul(j, first, length), F)):
            for x, y in zip(lhs, rhs): check(x == y, "local_series_coefficients")
        check(j[m] == add(sc(E.power(a, m), r), sc(b, -h)), "critical_leading_coefficients")
        check(ji[m] == add(sc(b, h), sc(E.power(a, m), -r*(1-r)**(m-1))), "critical_leading_coefficients")
        local_cases += 1
    mass_cases = 0
    for z, m in itertools.product((2, 3, 5, 7, 11), (2, 4, 6, 8, 12)):
        q, t = z*z, Q(1, z)
        r, h = Q(1, q), Q(q**(m//2-1))
        check(h*t**m == r, "critical_mass_identities")
        den1, den2 = (1-t)*(1-r), 1-(1-r)*t-h*t**m
        check(den1 == den2 and den1 > 0, "critical_mass_identities")
        bound = 1+2*r*t/den1
        plus = 1+t*(r+h*t**m)/((1-t)*(1-h*t**m))
        minus = 1+t*(r+h*t**m)/(1-(1-r)*t-h*t**m)
        check(plus == minus == bound, "critical_mass_identities")
        check(bound <= 1+16*t**3, "critical_mass_identities")
        mass_cases += 1
    x=Q(37,50)
    neg_control(1-x/2-4*x**6<0 and x**7<Q(1,8), "omit_norm_two_gate_for_3_over_7")
    q,m=7,6
    r,h=Q(1,q),Q(q*q)
    jm=r-h
    neg_control(jm != 0, "impose_extra_coprimality_in_j_times_mobius")
    neg_control(h*Q(1,q)**3==Q(1,q) and h*Q(1,q)**3!=Q(1,q*q), "pretend_powerful_critical_mass_is_summable")
    neg_control(h != q**3, "replace_coupled_q_squared_by_old_q_cubed")
    return {"local_phase_series_cases": local_cases, "rational_critical_mass_cases": mass_cases,
            "series_orders": "through degree 2m+2; m=2,4,6,8"}


def pclean(p): return {e:a for e,a in p.items() if a!=ZERO}

def pmul(p, q):
    out={}
    for e,a in p.items():
        for f,b in q.items():
            ef=tuple(x+y for x,y in zip(e,f))
            out[ef]=add(out.get(ef,ZERO),mul(a,b))
    return pclean(out)


def ppow(p, k, dim):
    out={(0,)*dim:ONE}
    for _ in range(k): out=pmul(out,p)
    return out


def pconj(p): return {e:cj(a) for e,a in p.items()}

def moments(n):
    out=[1,0]
    for j in range(2,n+1): out.append(out[-1]+out[-2])
    return out


def expectation(p):
    if not p: return ZERO
    ms=moments(max(max(e,default=0) for e in p))
    out=ZERO
    for e,a in p.items():
        w=1
        for j in e:w*=ms[j]
        out=add(out,sc(a,w))
    return out


def moment(p,k,dim):
    pk=ppow(p,k,dim)
    v=expectation(pmul(pk,pconj(pk)))
    check(v[1]==0 and v[0]>=0,"positive_reference_checks")
    return v[0]


def split(p, idx):
    u,v={},{}
    for e,a in p.items():
        check(e[idx] in (0,1),"multiaffine_setup")
        f=list(e);f[idx]=0;f=tuple(f)
        dest=v if e[idx] else u
        dest[f]=add(dest.get(f,ZERO),a)
    return pclean(u),pclean(v)


def restore(p,idx):
    out={}
    for e,a in p.items():
        f=list(e);f[idx]=0;f=tuple(f)
        out[f]=add(out.get(f,ZERO),a)
    return pclean(out)


def injection(u,v,k,dim):
    uu=pmul(u,pconj(u))
    integrand=pmul(ppow(uu,k-1,dim),pmul(u,pconj(v)))
    return 2*k*real(expectation(integrand))

# Independent exact atom assembly in Q(sqrt(5)), with zeta_6 coefficients.

def qadd(a,b):return (a[0]+b[0],a[1]+b[1])
def qmul(a,b):return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qscale(a,b):return(a[0]*b,a[1]*b)
def qpow(a,n):
    out=(Q(1),Q(0))
    for _ in range(n):out=qmul(out,a)
    return out


def atom_moment(p,k,dim):
    atoms=((Q(1,2),Q(1,2)),(Q(1,2),Q(-1,2)))
    probs=((Q(1,2),Q(-1,10)),(Q(1,2),Q(1,10)))
    total=(Q(0),Q(0))
    for choices in itertools.product((0,1),repeat=dim):
        prob=(Q(1),Q(0));A=(Q(0),Q(0));B=(Q(0),Q(0))
        for c in choices:prob=qmul(prob,probs[c])
        for e,a in p.items():
            mon=(Q(1),Q(0))
            for j,c in zip(e,choices):mon=qmul(mon,qpow(atoms[c],j))
            A=qadd(A,qscale(mon,a[0]));B=qadd(B,qscale(mon,a[1]))
        norm=qadd(qadd(qmul(A,A),qmul(A,B)),qmul(B,B))
        total=qadd(total,qmul(prob,qpow(norm,k)))
    check(total[1]==0,"atom_irrational_part_cancellation")
    return total[0]


def coupled_columns(primes,m,cap):
    cols=[]
    for exps in itertools.product((0,1,m),repeat=len(primes)):
        n=1
        for e,p in zip(exps,primes):n*=E.en(p)**e
        if n<=cap:cols.append((exps,n))
    return cols


def poly_columns(cols,primes,m,u,excluded=()):
    out={};records=[]
    symbols=[E.prime_character(p,u) for p in primes]
    for es,n in cols:
        a=ONE;occ=[]
        for j,(e,p,symbol) in enumerate(zip(es,primes,symbols)):
            occ.append(int(e>0))
            if e==0:continue
            q=E.en(p)
            if symbol is None or j in excluded:a=ZERO;break
            phase=E.ROOTS[(symbol*e)%6]
            factor=Q(-(q-1),q) if e==1 else Q(-q**(m//2-1))
            a=mul(a,sc(phase,factor))
        if a!=ZERO:
            occ=tuple(occ)
            out[occ]=add(out.get(occ,ZERO),a)
            records.append((es,n,a))
    return pclean(out),records


def cofactor_check(primes,m,u,cap,idx,whole):
    # Assemble both cofactor scales directly, not by splitting occupancy code.
    q=E.en(primes[idx]);symbol=E.prime_character(primes[idx],u)
    dim=len(primes);direct={};parts=[]
    for branch in (1,m):
        part={}
        if symbol is not None:
            exterior=sc(E.ROOTS[(symbol*branch)%6],Q(-(q-1),q) if branch==1 else Q(-q**(m//2-1)))
            for es in itertools.product((0,1,m),repeat=dim):
                if es[idx]:continue
                n=1
                for e,p in zip(es,primes):n*=E.en(p)**e
                if n*q**branch>cap:continue
                pol,_=poly_columns([(es,n)],primes,m,u)
                for occ,a in pol.items():part[occ]=add(part.get(occ,ZERO),mul(exterior,a))
        parts.append(pclean(part))
        for e,a in part.items():direct[e]=add(direct.get(e,ZERO),a)
    _,v=split(whole,idx)
    check(pclean(direct)==v,"direct_two_scale_cofactor")
    return parts


def arithmetic_checks():
    primes=((-3,-1),(-3,-2),(5,0)) # norms 7,7,25; two conjugates and one inert.
    check([E.en(p) for p in primes]==[7,7,25],"primitive_setup")
    rows=E.elements(13)
    check(len(rows)==54,"primitive_setup")
    dim=3; totals=[]; channel_witness=None;case_count=0; atom_cases=0
    for m in (2,4,6,8):
        cap=25**m
        cols=coupled_columns(primes,m,cap)
        G=I=D=Native=Q(0)
        for ri,u in enumerate(rows):
            p,records=poly_columns(cols,primes,m,u)
            start=moment(p,2,dim)
            if m==6:
                check(atom_moment(p,2,dim)==start,"direct_atom_reference_agreement");atom_cases+=1
            for idx in range(dim):
                parts=cofactor_check(primes,m,u,cap,idx,p)
                _,v=split(p,idx)
                full=moment(v,2,dim)
                separate=moment(parts[0],2,dim)+moment(parts[1],2,dim)
                if channel_witness is None and full!=separate:
                    channel_witness={"m":m,"row":u,"prime_index":idx,
                                     "coupled_energy":str(full),"separate_energy":str(separate)}
            current=p;ii=dd=Q(0)
            for idx in range(dim):
                U,V=split(current,idx)
                inj=injection(U,V,2,dim);comp=moment(V,2,dim)
                after=restore(current,idx)
                check(moment(after,2,dim)-moment(current,2,dim)==inj-comp,"quartic_restoration_steps")
                if m==6 and ri<7:
                    i6=injection(U,V,3,dim)
                    rem=moment(current,3,dim)-moment(after,3,dim)+i6
                    check(rem>=Q(8,5)*moment(V,3,dim),"sixth_compensation_lower_bound")
                ii+=inj;dd+=comp;current=after
            val=ZERO
            for a in p.values():val=add(val,a)
            native=E.norm(val)**2
            check(start+ii-dd==native,"complete_quartic_flow")
            G+=start;I+=ii;D+=dd;Native+=native;case_count+=1
        totals.append({"m":m,"cap":cap,"semigroup_columns":len(cols),"rows":len(rows),
                       "G":str(G),"I":str(I),"D":str(D),"native_M4":str(Native)})
    neg_control(channel_witness is not None,"separate_the_two_channel_compensations")
    # A single local source gives exact distinctions between multiplier schemes.
    same={(0,):ONE,(1,):(-Q(6,7)-Q(49),Q(0))}
    exponent={(0,):ONE,(1,):(-Q(6,7),Q(0)),(6,):(-Q(49),Q(0))}
    independent={(0,0):ONE,(1,0):(-Q(6,7),Q(0)),(0,1):(-Q(49),Q(0))}
    neg_control(moment(same,2,1)!=moment(exponent,2,1),"use_Z_to_m_instead_of_one_occupancy_multiplier")
    neg_control(moment(same,2,1)!=moment(independent,2,2),"randomize_prime_and_powerful_branches_independently")
    p=primes[0];check(E.prime_character(p,p) is None,"literal_nonunit_setup")
    masked,_=poly_columns([((6,0,0),7**6)],primes,6,p)
    neg_control(masked=={} and Q(49)!=0,"erase_neutral_sixth_power_nonunit_zero")
    q,m=7,6;scale=q**m
    true=Q(q**m,scale);wrong=Q(q**2,scale)
    neg_control(Q(1,2)<=true<=1 and not (Q(1,2)<=wrong<=1),"rescale_powerful_cofactor_by_q_squared")
    # Same literal family with an extra prime exclusion, on all rows.
    ex_count=0
    for u in rows:
        cols=coupled_columns(primes,6,25**6)
        p,_=poly_columns(cols,primes,6,u,excluded=(0,))
        check(all(e[0]==0 for e in p),"moving_exclusion")
        U,V=split(p,0);check(not V and U==p,"moving_exclusion");ex_count+=1
    return {"fixture":"three-prime semigroup only; hard norm cap, not the Gaussian",
            "prime_generators":primes,"prime_norms":[7,7,25],"row_norm_cap":13,
            "full_row_count":54,"quartic_row_cases":case_count,"additional_exclusion_rows":ex_count,
            "direct_atom_cases":atom_cases,"flow_totals":totals,"cross_channel_witness":channel_witness}


def main():
    local=series_checks();arith=arithmetic_checks()
    for m in range(2,65):
        alpha=Q(m,2*(m+1));delta=Q(1,101)
        check(Q(1,3)<=alpha<Q(1,2),"rational_exponent_bookkeeping")
        check(Q(m,2)-1-(m+1)*(alpha+delta)==-1-(m+1)*delta,"rational_exponent_bookkeeping")
    for s,v in itertools.product((Q(1,2),Q(31,32),Q(2)),(Q(-3),Q(0),Q(7,5))):
        c=Q(5,6)
        check(-v*v/4+(s-c)*v==-(v-2*(s-c))**2/4+(s-c)**2,"gaussian_square_completion")
    helper=Path(__file__).with_name('eisenstein_source.py').read_bytes()
    expected='64d21a7f400f5bf5654fd67735743ff1befab067'
    blob=hashlib.sha1(b'blob '+str(len(helper)).encode()+b'\0'+helper).hexdigest()
    check(blob==expected,"primitive_helper_git_blob")
    print(json.dumps({"status":"PASS","scope":"finite algebra and arithmetic fixtures only; no asymptotic certification",
                      "local":local,"arithmetic":arith,"helper_blob":blob,
                      "predicates_by_category":dict(sorted(counts.items())),"total_predicates":sum(counts.values()),
                      "negative_controls":negative_controls},sort_keys=True,indent=2))

if __name__=='__main__':main()
