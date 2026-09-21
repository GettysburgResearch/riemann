"""DCN26 native divisor closure and shifted-divisibility transport sectors."""
import argparse,hashlib,json
from pathlib import Path
from math import gcd
from arithmetic import sieve,divisors,near_candidates,require,canonical,strict_read
from exact import ZERO,S,BITS,rat,add,sub,scale,mul,log_int,intersect
CUTOFFS=(3,7,15,31,63,127,255)
WIDTHS=(0,1,3,7)

def logs_from_sieve(N,spf):
    logs=[ZERO]*(N+1)
    for n in range(2,N+1):
        p=spf[n]
        logs[n]=log_int(p) if p==n else add(logs[p],logs[n//p])
    return logs

def stage(Y):
    b=Y+1; X=b*b;N=X-1; H=max(WIDTHS)
    spf,mu,rad,core,primes=sieve(N+H)
    logs=logs_from_sieve(N,spf)
    A=[ZERO]*(N+1); repeat=[0]*(N+1)
    # Sparse, exact local collapse of Lambda_1*mu.
    for n in range(2,N+1):
        if mu[n]: A[n]=scale(logs[n],-mu[n])
    for p in primes:
        if p*p>N: break
        for r in range(1,N//(p*p)+1):
            if mu[r] and r%p:
                t=p*p*r;A[t]=scale(logs[p],-mu[r]);repeat[t]=p
    weights=[rat(X-max(b,n),X*max(b,n)) for n in range(N+1)]
    E=I=u0=u1=P=ZERO;M=0;running=ZERO
    for k in range(1,N+1):
        M+=mu[k];running=add(running,A[k])
        energy=rat(M*M,k*(k+1));mean=rat(M,k*(k+1))
        if k<b: E=add(E,energy);u0=add(u0,mean)
        else:
            I=add(I,energy);u1=add(u1,mean)
            P=add(P,scale(running,M,k*(k+1)))
    u=add(u0,u1)
    completed=add(add(E,I),scale(mul(u,u),2*X))
    comp_formula=ZERO; prior_matched=ZERO
    for n in range(2,N+1):
        if mu[n] and spf[n]!=n:
            comp_formula=add(comp_formula,mul(logs[n],weights[n]))
        if A[n]!=ZERO:
            prior_matched=add(prior_matched,scale(mul(A[n],weights[n]),mu[core[n]]))
    divs=divisors(N+H)
    diagonal=forward=reverse=ZERO; comp_pairs=0
    for s in range(1,N+1):
        diagonal=add(diagonal,scale(mul(A[s],weights[s]),mu[s]))
        for d in divs[s][:-1]:
            a=scale(A[s],mu[d]);c=scale(A[d],mu[s])
            forward=add(forward,mul(a,weights[s]));reverse=add(reverse,mul(c,weights[s]))
            if a!=ZERO or c!=ZERO: comp_pairs+=1
    require(intersect(add(diagonal,forward),ZERO),'complete forward divisor fibre')
    comp_direct=add(add(diagonal,forward),reverse)
    require(intersect(comp_direct,comp_formula),'comparable sector identity')
    require(comp_formula[0]>=0,'native comparable nonnegativity')
    # Additional disjoint, COMPLETE zero cubes with an outside-radical cofactor.
    fibres=terms=0
    for t in range(2,N+1):
        p=repeat[t]
        if not p: continue
        R=rad[t]
        for k in range(2,p+1):
            if not mu[k] or gcd(k,R)!=1: continue
            ms=[k*d for d in divs[R]]
            require(max(ms)<=t,'closed cube crosses kernel kink')
            require(sum(mu[m] for m in ms)==0,'closed cube not zero')
            require(all(t%m and m%t for m in ms),'cube/comparable overlap')
            fibres+=1;terms+=len(ms)
    bins=[ZERO]*(H+1); absolute=[ZERO]*(H+1); counts=[0]*(H+1); skipped=0
    for s in range(2,N+1):
        for d,r in near_candidates(s,H,divs):
            if r==0: continue  # comparable is handled as a complete sector
            a=scale(A[s],mu[d]); c=scale(A[d],mu[s])
            if a==ZERO and c==ZERO: continue
            k=d//gcd(d,rad[s])
            closed=bool(repeat[s] and mu[d] and 1<k<=repeat[s])
            if closed:
                require(c==ZERO,'unexpected reverse part in zero cube');skipped+=1;continue
            v=mul(add(a,c),weights[s]);bins[r]=add(bins[r],v)
            # Absolute original orientation contributions, not abs of their sum.
            av=(max(0,-a[1],a[0]),max(abs(a[0]),abs(a[1])))
            cv=(max(0,-c[1],c[0]),max(abs(c[0]),abs(c[1])))
            absolute[r]=add(absolute[r],mul(add(av,cv),weights[s]));counts[r]+=1
    harmonic=ZERO
    for n in range(1,N+H+1): harmonic=add(harmonic,rat(1,n))
    panels=[]
    for h in WIDTHS:
        signed=ab=ZERO; ct=0
        for r in range(1,h+1): signed=add(signed,bins[r]);ab=add(ab,absolute[r]);ct+=counts[r]
        bound=scale(mul(logs[N],mul(harmonic,harmonic)),8*h)
        require(ab[1]<=bound[0] if h else ab==ZERO,'near-transport absolute envelope')
        panels.append(dict(width=h,near=signed,near_absolute=ab,near_bound=bound,
            remaining=sub(sub(P,comp_formula),signed),pairs=ct))
    return dict(Y=Y,N=N,E=E,I=I,u_prefix=u0,u_annulus=u1,A_output=completed,P=P,
        prior_matched=prior_matched,comparable=comp_formula,comparable_direct=comp_direct,
        diagonal=diagonal,forward_proper=forward,reverse_proper=reverse,
        comparable_pairs=comp_pairs,zero_cubes=fibres,zero_cube_terms=terms,
        near_cube_pairs_removed=skipped,panels=panels)

def build():
    return dict(schema='DCN26-transport-1',bits=BITS,stages=[stage(y) for y in CUTOFFS],
        status='proposed component proofs; far incomparable negative part remains open')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path)
    args=ap.parse_args();out=build();s=canonical(out)
    if args.write: args.write.write_text(s+'\n')
    if args.check: require(s==canonical(strict_read(args.check)),'transport report differs')
    print('DCN26 transport OK',hashlib.sha256(s.encode()).hexdigest())
if __name__=='__main__': main()
