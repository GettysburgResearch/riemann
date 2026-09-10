#!/usr/bin/env python3
"""NIR26 finite arithmetic producer; no all-scale gain is certified."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

S = 1 << 128
MAX = 65535
PARENT = 'a1b4625f9775df1fdbd431b5198309a2fce9b038'

def need(ok, why):
    if not ok:
        raise ValueError(why)

def enc(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()

def digest(x):
    return hashlib.sha256(enc(x)).hexdigest()

def pair(x):
    x = F(x)
    return [x.numerator, x.denominator]

def enclosure(x):
    x = F(x) * S
    return [x.numerator // x.denominator, -(-x.numerator // x.denominator)]

def square(lo, hi):
    return [0 if lo <= 0 <= hi else min(lo*lo, hi*hi), max(lo*lo, hi*hi)]

def mu_sieve(N):
    mu, prime = [1]*(N+1), [True]*(N+1)
    mu[0] = 0
    for p in range(2, N+1):
        if prime[p]:
            for n in range(p, N+1, p):
                mu[n] = -mu[n]
                prime[n] = False
            for n in range(p*p, N+1, p*p):
                mu[n] = 0
    return mu

def state(Y, mu):
    M = 0
    m = E = u = Q = F(0)
    xs = []
    for k in range(1, Y+1):
        M += mu[k]
        m += F(mu[k], k)
        E += F(M*M, k*(k+1))
        u += F(M, k*(k+1))
        Q += m*m
        xs.append(m)
    c = {k:F(mu[k]) for k in range(1, Y+1) if mu[k]}
    c[Y+1] = -(Y+1)*m
    return c, xs, E, u, Q

def norm(c):
    positions = sorted(k for k,v in c.items() if v)
    total = value = F(0)
    for j,k in enumerate(positions):
        total += c[k]
        value += total*total*(F(1,k)-F(1,positions[j+1]) if j+1<len(positions) else F(1,k))
    return value

def raw(c, N):
    den = math.lcm(*(z.denominator for z in c.values()))
    C = {k:int(v*den) for k,v in c.items() if v}
    cc = [0]*(N+1)
    for r,a in C.items():
        for s,b in C.items():
            if r*s <= N:
                cc[r*s] += a*b
    out = [0]*(N+1)
    for k,a in C.items():
        if k<=N:
            out[k] += 2*den*a
    for d in range(1,N+1):
        if cc[d]:
            for k in range(d,N+1,d):
                out[k] -= cc[d]
    return out, den*den

def energy_panels(mu, cuts):
    M = ml = mh = el = eh = ul = uh = fl = fh = 0
    rows = []
    for k in range(1,max(cuts)+1):
        M += mu[k]
        ml += S*mu[k]//k
        mh += -(-S*mu[k]//k)
        a,b = square(ml,mh)
        fl += a//S; fh += -(-b//S)
        den = k*(k+1)
        el += S*M*M//den; eh += -(-S*M*M//den)
        ul += S*M//den; uh += -(-S*M//den)
        if k in cuts:
            a,b = square(ul,uh)
            g,h = (k+1)*a//S, -(-(k+1)*b//S)
            variance = [el+g,eh+h]
            need(max(fl,variance[0])<=min(fh,variance[1]),'energy identities have disjoint bounds')
            rows.append({'Y':k,'F':[fl,fh],'E':[el,eh],'u':[ul,uh],
                         'F_from_variance':variance,'A':[el+2*g,eh+2*h]})
    return rows

def build():
    mu = mu_sieve(MAX)
    isometry = []
    for N in range(1,13):
        for seed in range(4):
            c = {k:F((-1)**(k+seed)*(1+(k*seed)%3),1+(seed%2)) for k in range(1,N+1)}
            tail = sum((a/k for k,a in c.items()),F())
            value = tail*tail
            for k in range(1,N):
                tail -= c[k]/k; value += tail*tail
            need(value==norm(c),'whole norm/isometry')
            isometry.append([N,seed,pair(value)])
    projections = []; boundaries = []; constraints = 0
    for Y in range(1,25):
        c,x,E,u,Q = state(Y,mu); b=Y+1
        need(Q==E+b*u*u==norm(c),'native state')
        need(sum(x,F())==b*u,'mean')
        need(sum(((z-u)**2 for z in [F(),*x]),F())==E,'variance')
        for n in range(1,Y+1):
            need(sum((F(r*(n//r)-(r+1)*(n//(r+1)))*x[r-1] for r in range(1,n+1)),F())==1,'native divisor constraint')
            constraints += 1
        for j,alpha in ((b,F(-2,3)),(b+2,F(3,2))):
            a=c.copy();a[j]=a.get(j,F())+j*alpha;a[j+1]=a.get(j+1,F())-(j+1)*alpha
            need(norm(a)==Q+alpha*alpha,'orthogonal projection')
            projections.append([Y,j,pair(norm(a))])
        z,d = raw(c,b*b)
        e=F(mu[b])-c[b]
        need(F(mu[b*b])-F(z[b*b],d)==e*e,'first omitted coefficient')
        boundaries.append([Y,pair(e),pair(F(z[b*b],d)),mu[b*b]])
    ladder = []; pref=[0,1]
    for Y in (1,3,15,255):
        need(len(pref)==Y+1,'recursive scale')
        c,_,_,_,_=state(Y,pref); B=(Y+1)**2-1
        z,d=raw(c,B);need(all(a%d==0 for a in z),'integer reconstructed prefix')
        pref=[a//d for a in z]
        need(pref==mu[:B+1],'primitive Mobius comparison')
        ladder.append({'input':Y,'output':B,'coefficients':B,'sha256':digest(pref[1:])})
    kernel = []; kernel_entries = 0
    for Y in range(1,11):
        c,x,_,_,Q=state(Y,mu);b=Y+1;B=b*b-1
        H=[F(0)]
        for j in range(1,B+1):H.append(H[-1]+F(1,j))
        z,d=raw(c,B); q=F(); inc=F()
        for k in range(1,B+1):
            q += F(z[k],d*k)
            if k<b:continue
            form=F()
            for r in range(1,b):
                for s in range(1,b):
                    D=H[k//(r*s)]-H[k//((r+1)*s)]-H[k//(r*(s+1))]+H[k//((r+1)*(s+1))]
                    form += x[r-1]*x[s-1]*D;kernel_entries+=1
            need(q==-form,'mixed-difference arithmetic map')
            inc+=q*q;kernel.append([Y,k,pair(q)])
        need(Q+inc==state(B,mu)[-1],'complete quartic annulus')
    tails=[]
    for Y in (1,3,7):
        c,_,_,_,Q=state(Y,mu);R=257;z,d=raw(c,R-1)
        V=q=physical=innovation=F()
        for k in range(1,R):
            V+=F(z[k],d);q+=F(z[k],d*k)
            physical+=V*V/F(k*(k+1));innovation+=q*q
        K=2*abs(sum(c.values(),F()))+sum(map(abs,c.values()),F())**2
        p=[physical,physical+K*K/R];i=[innovation,innovation+4*K*K/(R-1)]
        need(max(p[0],i[0])<=min(p[1],i[1]),'whole-tail norm compatibility')
        tails.append({'Y':Y,'first_omitted_cell':R,'K':pair(K),
                      'physical':[enclosure(p[0])[0],enclosure(p[1])[1]],
                      'innovation':[enclosure(i[0])[0],enclosure(i[1])[1]],
                      'physical_tail':pair(K*K/R),'innovation_tail':pair(4*K*K/(R-1))})
    controls=[]
    for Y in (3,7,15,31,63):
        b=Y+1;c={Y:F(Y),b:F(-b)};z,d=raw(c,b*b-1);q=out=F()
        for k in range(1,b*b):
            q+=F(z[k],d*k)
            if k>=b:out+=q*q
        need(norm(c)==1 and out==2*Y+1,'localized unit-energy countermodel')
        controls.append([Y,pair(out)])
    fake=[]
    for b in (16,32,64,128):
        lower=0
        for k in range(b*b//2,b*b):
            V=2-2*b-k+2*b*(k//b)
            need(2*V>=k,'bounded-prefix barrier')
            lower+=S*V*V//(k*(k+1))
        need(lower>=S*b*b//16,'fake annulus bound')
        fake.append([b,b-1,lower])
    Ys=set(range(1,33))|{63,127,255}
    cuts=Ys|{(Y+1)**2-1 for Y in Ys}|{1,3,15,255,65535}
    energies=energy_panels(mu,cuts);by={r['Y']:r for r in energies};gains=[]
    for Y in sorted(Ys):
        B=(Y+1)**2-1;a=by[Y]['F'][0];bb=by[B]['F'][1]
        need((S+bb)**2*S<=4*(S+a)**3,'FINITE proposed gain test')
        gains.append([Y,B])
    body={'schema':'NIR26-v1','parent':PARENT,
          'scope':{'RH_proved':False,'all_scale_gain_proved':False,'finite_primitive_replay':True,
                   'whole_raw_tails_bounded':True,'projection_factor':1,'scale_endpoint':'(Y+1)^2-1'},
          'scale':S,'isometry':{'cases':len(isometry),'sha256':digest(isometry)},
          'projection':{'cases':len(projections),'sha256':digest(projections)},
          'constraints':constraints,'boundary':{'cases':len(boundaries),'sha256':digest(boundaries),'first':boundaries[:3]},
          'ladder':ladder,'kernel':{'panels':len(kernel),'entries':kernel_entries,'sha256':digest(kernel)},
          'raw_tails':tails,'localized_controls':controls,'bounded_fake_controls':fake,
          'energy':{'panels':len(energies),'sha256':digest(energies),
                    'ladder_rows':[by[n] for n in (1,3,15,255,65535)]},
          'FINITE_gain_tests':gains}
    return {'body':body,'sha256':digest(body)}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--output',type=Path)
    args=ap.parse_args();report=build()
    if args.check:need(enc(json.loads(args.check.read_text()))==enc(report),'canonical report differs')
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(enc(report)+b'\n')
    print('NIR PRODUCER PASS',report['sha256']);print('recursive endpoint',report['body']['ladder'][-1]['output'])
if __name__=='__main__':main()
