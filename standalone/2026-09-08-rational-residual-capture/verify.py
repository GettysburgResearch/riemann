#!/usr/bin/env python3
"""Bounded exact checks for RC1--RC5; not a machine proof of the analytic claims."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'REVIEW.md', 'SOURCES.json', 'VALIDATION.md',
         'verify.py', 'test_rejections.py', 'result.json', 'SHA256SUMS'}
PARENT = 'bcec690c1607e281bd6f741b68f5c50f556670c7'


def need(value, message):
    if not value:
        raise ValueError(message)


def pairs_hook(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def read_json(path):
    return json.loads(path.read_text(), object_pairs_hook=pairs_hook,
                      parse_float=lambda _: (_ for _ in ()).throw(ValueError('float forbidden')))


def strict_equal(a, b):
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(strict_equal(a[k], b[k]) for k in a)
    if isinstance(a, list):
        return len(a) == len(b) and all(strict_equal(x, y) for x, y in zip(a, b))
    return a == b


def digest_fractions(values):
    h = hashlib.sha256()
    for v in values:
        v = F(v)
        h.update((hex(v.numerator) + '/' + hex(v.denominator) + '\n').encode())
    return h.hexdigest()


def mu_trial(n):
    r, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            r = -r
            if n % p == 0:
                return 0
        p += 1
    return -r if n > 1 else r


def mu_sieve(N):
    out = [1]*(N+1)
    out[0] = 0
    prime = [True]*(N+1)
    for p in range(2, N+1):
        if prime[p]:
            for n in range(p, N+1, p):
                prime[n] = False
                out[n] *= -1
            for n in range(p*p, N+1, p*p):
                out[n] = 0
    return out


def jordan(N):
    out = [0]+[n*n for n in range(1, N+1)]
    for d in range(1, N+1):
        for k in range(2*d, N+1, d):
            out[k] -= out[d]
    return out


def balance(p):
    return sum((a/n for n, a in p.items()), F(0))


def value(p, j, b=F(1)):
    return b-sum((a*(j//n) for n, a in p.items()), F(0))


def period(p):
    return math.lcm(*(p.keys() or [1]))


def bilinear(p, q, b=F(1), c=F(1)):
    N = max(max(p, default=1), max(q, default=1))
    J = jordan(N)
    mean = (b+sum(p.values(), F(0))/2)*(c+sum(q.values(), F(0))/2)
    return mean+sum((J[d]*sum((a/n for n,a in p.items() if n%d==0), F(0))
                           *sum((a/n for n,a in q.items() if n%d==0), F(0))
                         for d in range(1,N+1)), F(0))/12


def moment(p, b=F(1)):
    return bilinear(p,p,b,b)


def C(N):
    return N*N*(1+2*(N-1).bit_length())


def finite_norm(p, H, b=F(1)):
    return sum((value(p,j,b)**2/F(j*(j+1)) for j in range(1,H)), F(0))


def centered(Y):
    p = {n:F(mu_trial(n)) for n in range(1,Y)}
    M, S = balance(p), sum(p.values(),F(0))
    cc = F(-2-S,F(3*Y-1,2)); bb = cc+M; aa = -cc-2*M
    for n in range(Y,2*Y):
        p[n] = aa*F(n,Y)
        p[2*n] = bb*F(2*n,Y)
    return {n:a for n,a in p.items() if a}, (aa,bb,cc)


def solve(A, b):
    """Exact Gaussian elimination; singular data are rejected."""
    a = [list(row)+[x] for row,x in zip(A,b)]
    n = len(b)
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j]), None)
        need(pivot is not None, 'singular finite matrix')
        a[j],a[pivot] = a[pivot],a[j]
        d = a[j][j]; a[j] = [v/d for v in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                d = a[i][j]
                a[i] = [x-d*y for x,y in zip(a[i],a[j])]
    return [row[-1] for row in a]


def decimal_out(q, places, lower):
    scale=10**places
    n=q.numerator*scale//q.denominator
    if not lower and F(n,scale) < q:
        n+=1
    sign='-' if n<0 else ''
    n=abs(n)
    return f'{sign}{n//scale}.{n%scale:0{places}d}'


def min_certificate(Y,N,H):
    """Global class: real p, prefix mu below Y, support <=N, p(1)=0 ONLY."""
    need(H>=N+1 and H+1>C(N), 'invalid positive comparison horizon')
    p={n:F(mu_trial(n)) for n in range(1,Y)}
    p[N]=-N*balance(p)
    need(balance(p)==0, 'reference balance')
    basis=[{n:F(1),N:F(-N,n)} for n in range(Y,N)]
    d=len(basis)
    G=[[F(0) for _ in range(d)] for _ in range(d)]
    L=[F(0)]*d; K=F(0)
    for j in range(1,H):
        w=F(1,j*(j+1)); r=value(p,j)
        q=[value(v,j,F(0)) for v in basis]
        K+=r*r*w
        for k in range(d):
            L[k]+=r*q[k]*w
            for ell in range(k+1):
                G[k][ell]+=q[k]*q[ell]*w
    for k in range(d):
        for ell in range(k):
            G[ell][k]=G[k][ell]
    GV=[[bilinear(v,w,F(0),F(0)) for w in basis] for v in basis]
    LV=[bilinear(p,v,F(1),F(0)) for v in basis]
    KV=moment(p)
    f=F(C(N),H*(H+1))
    minima=[]; digests=[]
    for coefficient in (F(1,H)-f,F(1,H),F(1,H)+f):
        A=[[G[i][j]+coefficient*GV[i][j] for j in range(d)] for i in range(d)]
        ll=[L[i]+coefficient*LV[i] for i in range(d)]
        x=solve(A,[-v for v in ll])
        need(all(ll[i]+sum((A[i][j]*x[j] for j in range(d)),F(0))==0
                 for i in range(d)), 'exact stationarity')
        val=K+coefficient*KV+sum((ll[i]*x[i] for i in range(d)),F(0))
        pp=dict(p)
        for xi,v in zip(x,basis):
            for n,a in v.items(): pp[n]=pp.get(n,F(0))+xi*a
        need(balance(pp)==0, 'minimum feasibility')
        need(all(pp.get(n,0)==mu_trial(n) for n in range(1,Y)), 'minimum prefix')
        # A second evaluation of the covariance part, not a numerical objective.
        v_direct=moment(pp)
        v_expanded=KV+2*sum((LV[i]*x[i] for i in range(d)),F(0))
        v_expanded+=sum((x[i]*GV[i][j]*x[j] for i in range(d) for j in range(d)),F(0))
        need(v_direct==v_expanded and v_direct>0, 'minimum period covariance')
        need(val>0, 'positive finite minimum')
        minima.append(val);digests.append(digest_fractions([val]+x))
    need(minima[0] <= minima[1] <= minima[2], 'ordered form minima')
    delta=F(C(N),H+1)
    need((1-delta)*minima[1] <= minima[0], 'uniform lower comparison')
    need(minima[2] <= (1+delta)*minima[1], 'uniform upper comparison')
    return {'Y':Y,'N':N,'H':H,'constraints':'actual prefix; p(1)=0; no derivative or p(0) constraint',
            'full_min_lower':decimal_out(minima[0],12,True),
            'full_min_upper':decimal_out(minima[2],12,False),
            'exact_solution_hashes_minus_center_plus':digests,
            'comparison_constant':C(N)}


def reconstruct():
    groups={}
    mus=mu_sieve(256)
    for n in range(1,257):
        need(mus[n]==mu_trial(n), 'Mobius primitive mismatch')
    groups['mobius_independent_factorization']=256
    J=jordan(128)
    for n in range(1,129):
        need(J[n]>0 and sum(J[d] for d in range(1,n+1) if n%d==0)==n*n,
             'Jordan convolution')
    groups['jordan_identity']=128
    for m in range(1,13):
        for n in range(1,13):
            q=math.lcm(m,n)
            av=sum((F(j%m,m)*F(j%n,n) for j in range(q)),F(0))/q
            target=F((m-1)*(n-1),4*m*n)+F(math.gcd(m,n)**2-1,12*m*n)
            need(av==target,'CRT covariance')
    groups['crt_covariance_pairs']=144
    samples=[({},F(0)),({},F(1)),({1:F(1),2:F(-2)},F(1)),
             ({1:F(1),2:F(-1),3:F(-1),4:F(-2,3)},F(1))]
    samples += [(centered(Y)[0],F(1)) for Y in range(2,6)]
    samples += [({n:F(1),2*n:F(-2)},F(0)) for n in range(2,6)]
    groupvals=[]
    for p,b in samples:
        need(balance(p)==0,'sample balance')
        q=period(p); vals=[value(p,j,b) for j in range(q)]; v=moment(p,b)
        need(v==sum((x*x for x in vals),F(0))/q,'period second moment')
        groupvals.append(v)
        for start in (-3,0,1,13):
            for length in (1,3,11):
                exact=sum((value(p,j,b)**2 for j in range(start,start+length)),F(0))
                need(abs(exact-length*v)<=C(max(2,max(p,default=1)))*v,
                     'bounded interval discrepancy')
        for H in (17,65,257):
            S=F(0); bound=F(0)
            for j in range(H,H+q):
                S+=value(p,j,b)**2-v
                bound=max(bound,abs(S))
            need(S==0,'period centered sum')
            need(bound<=C(max(2,max(p,default=1)))*v,'complete-tail periodic control')
    groups['full_period_second_moments']=len(samples)
    groups['block_discrepancy_panels']=len(samples)*12
    groups['independent_period_tail_brackets']=len(samples)*3
    c_hash=[]
    for Y in range(2,25):
        p,(a,b,c)=centered(Y);N=4*Y
        need(balance(p)==0 and sum(p.values())==-2, 'centered normalizations')
        need(max(p)<N and all(abs(x)<9 for x in p.values()), 'centered coefficients')
        need(abs(c)<=F(6,5) and abs(a)<=F(16,5) and abs(b)<=F(11,5),'centered parameters')
        need(all(p.get(n,0)==mu_trial(n) for n in range(1,Y)), 'native prefix')
        need(all(value(p,j)==0 for j in range(1,Y)), 'native horizon')
        v=moment(p);need(v<34*N,'centered covariance bound')
        f=F(1,N*N)+F(C(N),N*N*(N*N+1))
        need(v*f < F(68*(1+(N-1).bit_length()),N),'centered full tail rate')
        c_hash += [v,a,b,c]
    groups['native_centered_constructions']=23
    for H in (2,3,5,8,17,31):
        for c in (F(-3,2),F(1),F(7,5)):
            p={H:c,2*H:-4*c,4*H:4*c}
            need(balance(p)==0 and sum(p.values())==c, 'repair value jets')
            # derivative: coefficients of log(H) and log(2) vanish separately.
            need(c/H-4*c/(2*H)+4*c/(4*H)==0, 'repair log H jet')
            need(-4*c/(2*H)+8*c/(4*H)==0, 'repair log 2 jet')
            need(sum((a*a/n for n,a in p.items()),F(0))==13*c*c/H, 'repair coefficient cost')
            need(all(abs(value(p,j,F(0)))<=2*abs(c) for j in range(4*H)), 'repair floor bound')
    groups['safe_jet_preserving_center_repairs']=18
    for H in range(2,16):
        pp={n:F(mu_trial(n)) for n in range(1,H)}
        pp[H]=-H*balance(pp)
        need(balance(pp)==0 and finite_norm(pp,H)==0 and moment(pp)>0,
             'bare cutoff false-zero control')
    groups['bare_cutoff_false_zero_controls']=14
    for N in range(2,65):
        rr=math.isqrt(N)
        if rr*rr<N:rr+=1
        H=2*C(N)*rr
        need(H>=N+1 and F(4*C(N)**2,H*(H+1))<F(1,N), 'all-rank rational horizon')
        freqs=sorted({F(k,n) for n in range(1,N+1) for k in range(n)})
        need(len(freqs)<=N*N,'Farey count')
        gaps=[freqs[i+1]-freqs[i] for i in range(len(freqs)-1)]+[1+freqs[0]-freqs[-1]]
        need(min(gaps)>=F(1,N*N),'Farey circular spacing')
    groups['rational_frequency_and_horizon_cases']=63
    certificates=[min_certificate(Y,4*Y,4096) for Y in (2,3,4)]
    groups['actual_global_finite_minimum_brackets']=len(certificates)
    return {'status':'proposed component proof; independent review required',
            'RH_proved':False,'subpower_upper_bound_proved':False,
            'new_minimum_class':'p(1)=0 only; all real corrections Y,...,4Y',
            'parent_head':PARENT,'groups':groups,'bounded_panels':sum(groups.values()),
            'period_values_sha256':digest_fractions(groupvals),
            'centered_values_sha256':digest_fractions(c_hash),'certificates':certificates}


def integrity():
    need({p.name for p in ROOT.iterdir()}==FILES,'wrong packet inventory')
    need(all(p.is_file() and not p.is_symlink() for p in ROOT.iterdir()),'nonregular/symlink file')
    entries={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        sha,name=line.split('  ')
        need(name not in entries and name in FILES-{'SHA256SUMS'},'bad/duplicate manifest path')
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha,'checksum mismatch: '+name)
        entries[name]=sha
    need(set(entries)==FILES-{'SHA256SUMS'},'incomplete manifest')
    source=read_json(ROOT/'SOURCES.json')
    need(source['parent_head']==PARENT,'wrong locked parent')
    need(source['global_status']=='RH and subpower bound remain unproved','false global status')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write',action='store_true')
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    if args.write:
        (ROOT/'result.json').write_text(json.dumps(reconstruct(),sort_keys=True,indent=2)+'\n')
        return
    integrity()
    result=reconstruct()
    if args.check:
        need(strict_equal(result,read_json(args.check)),'result differs from reconstruction')
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
