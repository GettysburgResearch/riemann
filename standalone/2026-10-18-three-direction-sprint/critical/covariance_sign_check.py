"""Directed complete finite covariance signs; no asymptotic assertion.

All ideal coverage, factorization, character phases, conductor cutoffs and
integer phase bins are exact. Only transcendental profile/height values and
their finite sums use outward Arb/acb enclosures.
"""
from pathlib import Path
import argparse, hashlib, json, math, sys, time
import numpy as np


def need(v, msg):
    if not v: raise ArithmeticError(msg)


UNITS=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))


def mul(a,b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1]


def norm(a): return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]


def quotient(a,p):
    q=norm(p); x,y=mul(a,(p[0]-p[1],-p[1]))
    return None if x%q or y%q else (x//q,y//q)


def primitive(cap):
    bound=math.isqrt(2*cap)
    ideals=sorted(((a,b) for b in range(-bound,bound+1) if b%3==0
                   for a in range(-bound,bound+1) if a%3==1
                   and 0<norm((a,b))<=cap and math.gcd(norm((a,b)),6)==1),
                  key=lambda z:(norm(z),z))
    ns=[norm(a) for a in ideals]
    # Independent HNF inventory, from omega stability of its two lattice columns.
    hnf={}
    for c in range(1,math.isqrt(cap)+1):
        for a in range(1,cap//(c*c)+1):
            if math.gcd(c*c*a,6)!=1: continue
            for b in range(a):
                if (b*b-b+1)%a==0:
                    hnf.setdefault(c*c*a,[]).append((c*a,c*b,c))
    def member(t,z):
        a,b,c=t; x,y=z
        return y%c==0 and (x-b*(y//c))%a==0
    covered=set()
    for a in ideals:
        matches=[t for t in hnf[norm(a)] if member(t,a) and member(t,(-a[1],a[0]-a[1]))]
        need(len(matches)==1,'primary ideal has no unique HNF')
        need(matches[0] not in covered,'duplicate primary ideal')
        covered.add(matches[0])
    need(len(covered)==sum(map(len,hnf.values())),'incomplete ideal inventory')
    spf=list(range(cap+1))
    for p in range(2,math.isqrt(cap)+1):
        if spf[p]==p:
            for x in range(p*p,cap+1,p): spf[x]=p
    index={a:i for i,a in enumerate(ideals)}
    by_p={}; primes=[]
    for i,q in enumerate(ns):
        r=math.isqrt(q)
        p=q if q>1 and spf[q]==q else r if r*r==q and r>1 and spf[r]==r and r%3==2 else None
        if p is not None:
            primes.append(i); by_p.setdefault(p,[]).append(i)
    parents=[None]*len(ideals); factors=[{} for a in ideals]; mu=[1]*len(ideals)
    for i,a in enumerate(ideals):
        if i==0: continue
        for pi in by_p[spf[ns[i]]]:
            rem=quotient(a,ideals[pi])
            if rem is not None:
                ri=index[rem]; need(ri<i,'factorization did not shorten')
                parents[i]=pi,ri; f=factors[ri].copy(); f[pi]=f.get(pi,0)+1
                factors[i]=f; mu[i]=0 if max(f.values())>1 else (-1)**len(f)
                need(math.prod(ns[j]**e for j,e in f.items())==ns[i],'factor norm mismatch')
                break
        else: raise ArithmeticError('missing prime ideal factor')
    return ideals,ns,parents,factors,mu,primes


def powmodvec(a,k,p):
    r=np.ones_like(a)
    while k:
        if k&1: r=r*a%p
        a=a*a%p; k//=2
    return r


def prime_phases(alpha,rows):
    q=norm(alpha); p=math.isqrt(q)
    if p*p!=q:
        p=q; root=(-alpha[0]*pow(alpha[1],-1,p))%p
        value=powmodvec((rows[:,0]+rows[:,1]*root)%p,(p-1)//6,p)
        out=np.full(len(rows),6,dtype=np.int8)
        for k,(a,b) in enumerate(UNITS): out[value==(a+b*root)%p]=k
        need(np.all((value==0)|(out!=6)),'split prime phase failure')
        return out
    a=rows[:,0]%p; b=rows[:,1]%p
    ra=np.ones(len(rows),dtype=np.int64); rb=np.zeros_like(ra); k=(q-1)//6
    while k:
        if k&1: ra,rb=(ra*a-rb*b)%p,(ra*b+rb*a-rb*b)%p
        a,b=(a*a-b*b)%p,(2*a*b-b*b)%p; k//=2
    out=np.full(len(rows),6,dtype=np.int8)
    for k,(a,b) in enumerate(UNITS): out[(ra==a%p)&(rb==b%p)]=k
    need(np.all(((ra==0)&(rb==0))|(out!=6)),'inert prime phase failure')
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dependency-dir',type=Path,required=True)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args();sys.path.insert(0,str(args.dependency_dir.resolve()))
    import flint
    from flint import arb,acb,ctx,fmpq
    need(flint.__version__=='0.9.0','pinned flint0.9.0 required')
    need(args.bits>=160,'insufficient precision');ctx.prec=args.bits
    start=time.monotonic(); U=1024;D=1024;N=32;cap=2048
    ideals,ns,parents,factors,mu,primes=primitive(cap)
    ri=[i for i,q in enumerate(ns) if U<q<2*U and max(factors[i].values(),default=0)<6]
    rows=np.array([ideals[i] for i in ri],dtype=np.int64)
    codes=np.empty((len(ideals),len(ri)),dtype=np.int8);codes[0]=0
    for i in range(1,len(ideals)):
        pi,qi=parents[i]
        if qi==0: codes[i]=prime_phases(ideals[i],rows)
        else: codes[i]=np.where((codes[pi]==6)|(codes[qi]==6),6,(codes[pi]+codes[qi])%6)
    def A(q,den=1): return arb(fmpq(int(q),int(den)))
    def bump(q,scale):
        if not scale<q<2*scale: return arb(0)
        x=A(q,scale)-1
        return (4-1/(x*(1-x))).exp()
    roots=[acb(A(2*a-b,2),A(b,2)*arb(3).sqrt()) for a,b in UNITS]+[acb(0)]
    roww=[bump(ns[i],U) for i in ri]
    di=[i for i,q in enumerate(ns) if D<q<2*D and mu[i]]
    ni=[i for i,q in enumerate(ns) if N<q<2*N]
    pindex={}; prods=[]; ff=[]; pc=[]; records=[]
    for d in di:
        for n in ni:
            aa=mul(ideals[d],ideals[n]); raw=np.where((codes[d]==6)|(codes[n]==6),6,(codes[d]+codes[n])%6)
            if aa not in pindex:
                pindex[aa]=len(prods);prods.append(aa);pc.append(raw)
                f=factors[d].copy()
                for p,e in factors[n].items(): f[p]=f.get(p,0)+e
                ff.append(f)
            j=pindex[aa];need(np.array_equal(pc[j],raw),'product character mismatch')
            records.append((d,n,j))
    pc=np.array(pc,dtype=np.int8); length=len(prods)
    need(max(e for f in ff for e in f.values()) < 6,
         'radical matrix requires nonzero single-column exponents modulo six')
    rad=np.array([math.prod(ns[p] for p in f) for f in ff],dtype=np.int64)
    need(int(max(rad))**2 < 2**63,'conductor integer overflow')
    conductors=np.outer(rad,rad)
    incidence={}
    for j,f in enumerate(ff):
        for p,e in f.items(): incidence.setdefault(p,{}).setdefault(e%6,[]).append(j)
    for p,exps in incidence.items():
        both=[j for rr in exps.values() for j in rr]; idx=np.ix_(both,both)
        need(np.all(conductors[idx]%ns[p]==0),'radical conductor division')
        conductors[idx]//=ns[p]
        for same in exps.values():
            idx=np.ix_(same,same)
            need(np.all(conductors[idx]%ns[p]==0),'equal-exponent conductor division')
            conductors[idx]//=ns[p]
    cutoff=1
    while (cutoff+1)**8<=U**9: cutoff+=1
    selected=list(zip(*np.where(np.triu(conductors<=cutoff))))
    # Every selected integer conductor is independently checked from valuations.
    pairhash=hashlib.sha256()
    for i,j in selected:
        exact=math.prod(ns[p] for p in ff[i].keys()|ff[j].keys() if (ff[i].get(p,0)-ff[j].get(p,0))%6)
        need(exact==int(conductors[i,j]) and exact**8<=U**9,'pair conductor error')
        pairhash.update(f'{i},{j},{exact}\n'.encode())
    # All remaining matrix entries are excluded by exact integer comparison,
    # not by logarithmic floating conductor classification.
    normgroups=sorted(set(ns[i] for i in ri)); groupindex={q:i for i,q in enumerate(normgroups)}
    group=np.array([groupindex[ns[i]] for i in ri],dtype=np.int64)
    weighted_roots=[bump(q,U)*r for q in normgroups for r in roots[:6]]
    kernels=[]
    for i,j in selected:
        good=(pc[i]!=6)&(pc[j]!=6)
        ph=(pc[i,good].astype(np.int64)-pc[j,good])%6
        counts=np.bincount(6*group[good]+ph,minlength=6*len(normgroups))
        value=acb(0)
        for k in np.flatnonzero(counts): value+=int(counts[k])*weighted_roots[k]
        kernels.append(value)
    runs=[]
    for height in (0,10):
        ad={i:mu[i]*bump(ns[i],D)/A(ns[i]).sqrt()*acb(0,-height*A(ns[i]).log()).exp() for i in di}
        bn={i:bump(ns[i],N)/A(ns[i]).sqrt()*acb(0,-height*A(ns[i]).log()).exp() for i in ni}
        coeff=[acb(0) for a in prods]; perprod=[[] for a in prods]
        for d,n,j in records:
            val=ad[d]*bn[n];coeff[j]+=val;perprod[j].append((d,n,val))
        direct=arb(0);ed=arb(0);en=arb(0);over=arb(0)
        for r,w in enumerate(roww):
            md=sum((ad[d]*roots[int(codes[d,r])] for d in di),acb(0))
            sn=sum((bn[n]*roots[int(codes[n,r])] for n in ni),acb(0))
            sd=sum((abs(ad[d])**2 for d in di if codes[d,r]!=6),arb(0))
            ss=sum((abs(bn[n])**2 for n in ni if codes[n,r]!=6),arb(0))
            direct+=w*abs(md*sn)**2;ed+=w*sd*abs(sn)**2
            en+=w*ss*abs(md)**2;over+=w*sd*ss
        total=direct-ed-en+over
        small=arb(0)
        for (i,j),kernel in zip(selected,kernels):
            form=coeff[i]*coeff[j].conjugate()
            for d,n,z in perprod[i]:
                for dd,nn,zz in perprod[j]:
                    if d==dd: form-=z*zz.conjugate()
                    if n==nn: form-=z*zz.conjugate()
                    if d==dd and n==nn: form+=z*zz.conjugate()
            small+=(1 if i==j else 2)*(form*kernel).real
        high=total-small
        need(high<0 if height==0 else high>0,'expected complete high-conductor sign failed')
        runs.append({'height':height,'E':str(direct),'ED':str(ed),'EN':str(en),'EDN':str(over),
                     'complete_both_different':str(total),'complete_C_at_most_U_9_8':str(small),
                     'complete_C_greater_U_9_8':str(high),'sign':-1 if height==0 else 1})
    result={'status':'PASS','scope':'Complete finite original mixed covariance signs only; no asymptotic refutation or exponent bound.',
            'arithmetic':'Exact integer ideals/phases/conductors; outward Arb/acb transcendental profiles and finite sums.',
            'python_flint':flint.__version__,'bits':args.bits,'U':U,'D':D,'N':N,
            'profile':'W(x)=exp(4-1/((x-1)(2-x))) for 1<x<2, else0',
            'common_height_factor':'(Na)^(-it) in both original input factors',
            'complete_good_ideal_inventory':len(ideals),'complete_sixthfree_physical_rows':len(ri),
            'inverse_terms':len(di),'plain_terms':len(ni),'original_input_pairs':len(records),
            'collapsed_products':length,'exact_cutoff':cutoff,'upper_triangular_selected_pairs':len(selected),
            'pair_conductor_stream_sha256':pairhash.hexdigest(),
            'character_stream_sha256':hashlib.sha256(codes.tobytes()).hexdigest(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':runs,
            'not_proved':['asymptotic one-sign failure','complete U^(6/5) mean','RH','new zero-free region']}
    if args.check:
        need(result==json.loads(args.check.read_text(encoding='utf-8')),
             'fresh primitive covariance replay differs from saved record')
    if args.output:
        args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','runs':runs,'seconds':time.monotonic()-start},indent=2))


if __name__=='__main__': main()
