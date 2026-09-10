#!/usr/bin/env python3
"""DPG26 bounded exact controls; not a machine proof of the infinite theorems."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import sys

FILES = {
    'PROOF.md', 'README.md', 'REVIEW_AND_SOURCES.md', 'VALIDATION.md',
    'SOURCE_LOCK.json', 'check.py', 'test_check.py', 'verification.json',
    'SHA256SUMS',
}
SOURCE = {
    'repository': 'GettysburgResearch/riemann',
    'base': 'c07aa6adcb1e8afa8bac4c5d6f921a822629b236',
    'graph_pr': 790,
    'graph_commit': '6b309554bf1e2f83a83325cd54038f5a0b9b0014',
    'graph_path': 'standalone/2026-09-05-astra-theta-count-closure/divisor-cusp-pass10/PROOF.md',
    'graph_blob': '2e7d67973881dc440868abd3e46bb65f379b2b31',
    'graph_bytes': 15233,
    'parent_code_executed': False,
    'infinite_theorems_machine_checked': False,
}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def canonical(x: object) -> bytes:
    return (json.dumps(x, sort_keys=True, indent=2, ensure_ascii=True) + '\n').encode()


def strict_json(path: Path) -> object:
    def pairs(items):
        ans = {}
        for k, v in items:
            require(k not in ans, 'duplicate JSON key: ' + k)
            ans[k] = v
        return ans
    def no_float(_):
        raise ValueError('noninteger JSON number forbidden')
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_float=no_float, parse_constant=no_float)


def authenticate(root: Path) -> None:
    entries = list(root.iterdir())
    require({p.name for p in entries} == FILES, 'incorrect flat inventory')
    require(all(p.is_file() and not p.is_symlink() for p in entries), 'nonregular or symlink input')
    manifest = {}
    for line in (root / 'SHA256SUMS').read_text().splitlines():
        require(len(line) >= 67 and line[64:66] == '  ', 'manifest syntax')
        h, name = line[:64], line[66:]
        require(name not in manifest, 'duplicate manifest path')
        require(len(h) == 64 and all(c in '0123456789abcdef' for c in h), 'manifest hash')
        manifest[name] = h
    require(set(manifest) == FILES - {'SHA256SUMS'}, 'manifest coverage')
    for name, h in manifest.items():
        require(hashlib.sha256((root / name).read_bytes()).hexdigest() == h, 'changed bytes: ' + name)
    require(canonical(strict_json(root / 'SOURCE_LOCK.json')) == canonical(SOURCE), 'source lock mismatch')


def factors(n: int) -> dict[int, int]:
    require(type(n) is int and n >= 1, 'positive integer required')
    ans = {}; d = 2
    while d*d <= n:
        while n % d == 0:
            ans[d] = ans.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: ans[n] = ans.get(n, 0) + 1
    return ans


def sieve_factors(limit: int) -> list[dict[int, int]]:
    ans = [{} for _ in range(limit + 1)]
    for p in range(2, limit + 1):
        if not ans[p]:
            for n in range(p, limit + 1, p):
                k = n; e = 0
                while k % p == 0: e += 1; k //= p
                ans[n][p] = e
    return ans


def divisors(n: int) -> set[int]:
    ds = {1}
    for p, e in factors(n).items():
        ds = {d*p**j for d in ds for j in range(e+1)}
    return ds


def valid_support(s: list[int]) -> None:
    require(len(s) > 0 and all(type(n) is int and n > 0 for n in s), 'empty or malformed support')
    require(s == sorted(set(s)), 'support duplicates/order')
    require(all(divisors(n) <= set(s) for n in s), 'support not divisor closed')


def log_series(x: F, terms: int = 32) -> tuple[F, F]:
    require(1 <= x <= 2, 'log range')
    z = (x-1)/(x+1); z2 = z*z; power = z; lower = F(0)
    for j in range(terms):
        lower += 2*power/(2*j+1); power *= z2
    return lower, lower + 2*power/((2*terms+1)*(1-z2))


def log_bounds(p: int) -> tuple[F, F]:
    k = p.bit_length()-1
    a, b = log_series(F(2)); c, d = log_series(F(p, 2**k))
    lo, hi = k*a+c, k*b+d
    scale = 2**24
    return F((lo*scale).__floor__(), scale), F((hi*scale).__ceil__(), scale)


def parents(s: list[int], largest: bool = False) -> dict[int, int]:
    ans = {}
    for a in s:
        if a == 1: continue
        fs = factors(a); p = max(fs) if largest else min(fs)
        ans[a] = a//p**fs[p]
    return ans


def paths(s: list[int], par: dict[int, int]) -> dict[int, list[int]]:
    out = {}
    for n in s:
        a = n; trail = []
        while a > 1:
            require(a in par and par[a] < a, 'broken tree')
            trail.append(a); a = par[a]
        out[n] = trail
    return out


def source_matrix(s: list[int], weights: dict[int, F]) -> list[list[F]]:
    """All ordered-by-size prime-power edges, exact stiffness in f coordinates."""
    idx = {a:i for i,a in enumerate(s)}; d = len(s)
    out = [[F(0) for _ in s] for _ in s]
    for a in s:
        for p,e in factors(a).items():
            for k in range(1,e+1):
                b = a//p**k; i,j = idx[a],idx[b]; c = weights[p]/a
                out[i][i] += c; out[j][j] += c
                out[i][j] -= c; out[j][i] -= c
    return out


def pair_matrix(s: list[int], weights: dict[int,F]) -> list[list[F]]:
    """Independent pair enumeration plus native divisor/birth diagonal."""
    out = [[F(0) for _ in s] for _ in s]
    for i,a in enumerate(s):
        out[i][i] = sum((e*weights[p]/a for p,e in factors(a).items()),F(0))
        for j,b in enumerate(s):
            if b > a and b % a == 0:
                fs = factors(b//a)
                if len(fs)==1:
                    p = next(iter(fs)); c = weights[p]/b
                    out[i][i] += c; out[i][j] = -c; out[j][i] = -c
    return out


def quadratic(k, f):
    return sum((f[i]*k[i][j]*f[j] for i in range(len(f)) for j in range(len(f))),F(0))


def positive_ldl(k: list[list[F]]) -> dict:
    """Exact LDL pivots, no tolerance or float acceptance."""
    n = len(k); l = [[F(0) for _ in range(n)] for _ in range(n)]; d = []
    for j in range(n):
        v = k[j][j]-sum((l[j][i]**2*d[i] for i in range(j)),F(0))
        require(v > 0, 'nonpositive LDL pivot')
        d.append(v); l[j][j]=1
        for i in range(j+1,n):
            l[i][j]=(k[i][j]-sum((l[i][a]*l[j][a]*d[a] for a in range(j)),F(0)))/v
    return {'positive_pivots': n,
            'minimum_pivot_floor_2pow24': (min(d)*2**24).__floor__() if d else 0,
            'max_denominator_bits': max((x.denominator.bit_length() for x in d), default=0)}


def support_panel(s: list[int], dense: bool) -> dict:
    valid_support(s)
    primes = sorted({p for n in s for p in factors(n)})
    weights = {p:log_bounds(p)[0] for p in primes}
    z = {}; mass = F(1)
    for p in primes: z[p]=mass; mass *= F(p,p-1)
    r = max(map(lambda n:len(factors(n)), s))
    kappa = max((z[p]/weights[p] for p in primes),default=F(0))
    if r: require(kappa < 24, 'finite rational Euler load exceeds bound')
    par = parents(s); trails = paths(s,par)
    for n in s: require(len(trails[n]) == len(factors(n)), 'omega path length')
    for a in s[1:]:
        p=min(factors(a))
        desc={n for n in s if a in trails[n]}
        predicted={n for n in s if n%a==0 and all(q<p for q in factors(n//a))}
        require(desc==predicted, 'descendant identity')
        require(sum((F(1,n) for n in desc),F(0)) <= z[p]/a, 'Euler mass bound')
    k=source_matrix(s,weights); require(k==pair_matrix(s,weights),'source edge/diagonal reconstruction')
    require(all(sum(row)==0 for row in k),'ground null vector')
    f=[F((7*n*n+3*n)%19-9, (n%5)+1) for n in s]
    weighted_mean=sum((x/n for x,n in zip(f,s)),F(0))/sum((F(1,n) for n in s),F(0))
    residual=sum(((x-weighted_mean)**2/n for x,n in zip(f,s)),F(0))
    anchored=sum(((x-f[0])**2/n for x,n in zip(f,s)),F(0))
    lookup=dict(zip(s,f)); et=sum((weights[min(factors(a))]/a*(lookup[a]-lookup[par[a]])**2 for a in s[1:]),F(0))
    require(residual<=anchored<=r*kappa*et<=r*kappa*quadratic(k,f),'Poincare chain')
    # Arbitrary tree data, integration, and weighted-centering decoder.
    delta={a:F((a*13)%17-8,11) for a in s[1:]}; ff={1:F(0)}
    for a in s[1:]: ff[a]=ff[par[a]]+delta[a]
    center=sum((ff[a]/a for a in s),F(0))/sum((F(1,a) for a in s),F(0))
    decoded={a:ff[a]-center for a in s}
    require(all(decoded[a]-decoded[par[a]]==delta[a] for a in s[1:]), 'decoder edge fidelity')
    ene=sum((weights[min(factors(a))]/a*delta[a]**2 for a in s[1:]),F(0))
    require(sum((decoded[a]**2/a for a in s),F(0))<=r*kappa*ene,'decoder bound')
    result={'vertices':len(s),'maximum_integer':max(s),'distinct_prime_depth':r,
            'support_sha256':hashlib.sha256(canonical(s)).hexdigest(),
            'edges':sum(sum(factors(a).values()) for a in s),
            'tree_edges':len(s)-1,'dense_lower_certificate':None}
    if dense and r:
        gamma=F(1,24*r)
        fixed235=set(primes)<={2,3,5}
        if fixed235: gamma=F(1,6)
        lower=[[k[i][j]-(gamma/F(s[i]) if i==j else 0) for j in range(1,len(s))] for i in range(1,len(s))]
        result['dense_lower_certificate']={'gap':str(gamma),**positive_ldl(lower)}
    return result


def local_generator(p:int,m:int):
    q=F(1,p)
    return [[sum((q**(a-e) if a>e else F(1) for a in range(m+1) if a!=e),F(0)) if e==j else
             -(q**(j-e) if j>e else F(1)) for j in range(m+1)] for e in range(m+1)]


def matvec(a,x):
    return [sum((r[j]*x[j] for j in range(len(x))),F(0)) for r in a]


def wavelet(p:int,m:int,j:int):
    if j==0: return [F(1)]*(m+1),F(0)
    q=F(1,p); a=sum((q**l for l in range(1,m-j+2)),F(0))
    return [F(0) if e<j-1 else -a if e==j-1 else F(1) for e in range(m+1)],j+a


def spectrum_panel(p:int,m:int):
    l=local_generator(p,m); q=F(1,p); basis=[]; vals=[]
    for j in range(m+1):
        u,eig=wavelet(p,m,j); basis.append(u); vals.append(str(eig))
        require(matvec(l,u)==[eig*x for x in u],'one-prime eigen equation')
        if j:
            aa=sum((q**k for k in range(1,m-j+2)),F(0))
            require(sum((q**e*u[e]**2 for e in range(m+1)),F(0))==q**(j-1)*aa*(1+aa),'wavelet norm')
    for i in range(m+1):
        for j in range(i): require(sum((q**e*basis[i][e]*basis[j][e] for e in range(m+1)),F(0))==0,'wavelet orthogonality')
    return {'prime':p,'max_exponent':m,'eigenvalues_divided_by_log_prime':vals}


def reconstruct() -> dict:
    groups={}
    sf=sieve_factors(1024)
    require(all(sf[n]==factors(n) for n in range(1,1025)),'primitive factorization mismatch')
    groups['primitive_factorization']={'integers':1024}
    for p in (2,3,5):
        lo,hi=log_bounds(p)
        require(hi>lo and hi-lo<=F(1,2**23),'directed logarithm enclosure width')
    require(log_bounds(2)[0]>F(1,2) and log_bounds(3)[0]>1 and log_bounds(5)[0]>F(3,2),'fixed-prime margins')
    groups['logarithm_bounds']={str(p):[str(x) for x in log_bounds(p)] for p in (2,3,5,7,31,127)}
    panels=[list(range(1,n+1)) for n in [1,2,3,4,5,6,8,10,12,16,20,24,32]]
    panels += [sorted(divisors(60)|divisors(84)),sorted(divisors(360)),
               [n for n in range(1,65) if all(p not in {2,3,5} for p in factors(n))],
               [n for n in range(1,49) if all(e==1 for e in factors(n).values())],
               sorted({2**a*3**b for a in range(6) for b in range(4)}),
               [2**a for a in range(9)]]
    groups['divisor_closed_graphs']=[support_panel(s,len(s)<=32) for s in panels]
    groups['prime_power_spectra']=[spectrum_panel(p,m) for p in (2,3,5,7,11) for m in range(1,9)]
    # Whole two-prime tensor, separate FORMAL coefficients of log 2 and log 3.
    coords=list(product(range(3),range(2))); l2=local_generator(2,2); l3=local_generator(3,1)
    tensor=[]
    for j2,j3 in coords:
        u2,e2=wavelet(2,2,j2); u3,e3=wavelet(3,1,j3)
        f={(a,b):u2[a]*u3[b] for a,b in coords}
        for a,b in coords:
            require(sum((l2[a][k]*f[k,b] for k in range(3)),F(0))==e2*f[a,b],'tensor log2 component')
            require(sum((l3[b][k]*f[a,k] for k in range(2)),F(0))==e3*f[a,b],'tensor log3 component')
        tensor.append([str(e2),str(e3)])
    groups['tensor_spectrum']={'support':[2**a*3**b for a,b in coords], 'formal_log2_log3_eigenvalues':tensor}
    # Explicit finite ancestors show why reversing the tree changes its load.
    reverse=[]
    for n in (8,16,32,64):
        s=list(range(1,n+1)); a=paths(s,parents(s,True)); desc={k for k in s if 2 in a[k]}
        require(desc=={2*m for m in range(1,n//2+1,2)},'greatest-prime direction control')
        reverse.append({'N':n,'harmonic_load':str(sum((F(1,k) for k in desc),F(0)))})
    groups['direction_and_closure_controls']=reverse
    try: valid_support([1,6])
    except ValueError: pass
    else: raise ValueError('nonclosed support accepted')
    # No prime-power ratio: the retained induced energy is zero but variance 1/7.
    require(len(factors(6))==2,'nonclosed ratio')
    variance=F(1,6)-F(1,6)**2/(1+F(1,6)); require(variance==F(1,7),'nonclosed variance')
    groups['nonclosed_counterexample']={'support':[1,6],'energy':'0','weighted_variance':str(variance)}
    # Rational Schur controls in a spectral basis, not actual Weil matrices.
    schur=[]
    for t in (F(0),F(1,2),F(3,4)):
        gamma=F(1,48); aa=gamma*(1-t); bb=2*gamma
        b1,b2=F(1,100),F(-1,200); cost=b1*b1/aa+b2*b2/bb
        require(cost<= (b1*b1+b2*b2)/aa,'Schur cost ceiling')
        for sign in (-1,0,1):
            k00=cost+sign*F(1,1000); x,y,z=F(3,7),F(-2,5),F(1,11)
            lhs=k00*x*x+2*x*(b1*y+b2*z)+aa*y*y+bb*z*z
            rhs=(k00-cost)*x*x+aa*(y+b1*x/aa)**2+bb*(z+b2*x/bb)**2
            require(lhs==rhs,'Schur completed square')
        schur.append({'theta':str(t),'correction':str(cost)})
    groups['schur_controls']=schur
    return {'schema':'DPG26-exact-1','rh_proved':False,'global_gap_constant_proved':False,
            'gap_denominator_factor':24,'distinct_factor_depth':'omega',
            'all_prime_powers_retained':True,'groups':groups,
            'scope':{'factorization_limit':1024,'graph_panels':len(panels),
                     'local_spectral_panels':40,'tensor_panels':1,
                     'infinite_claims':'paper proofs; not finite-test consequences'}}


def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument('--write',action='store_true'); args=parser.parse_args()
    root=Path(__file__).absolute().parent
    if args.write:
        require(not (root/'verification.json').is_symlink(), 'symlink output')
        (root/'verification.json').write_bytes(canonical(reconstruct()))
        print('WROTE_DPG26_BOUNDED_RESULT'); return 0
    authenticate(root)
    expected=reconstruct(); observed=strict_json(root/'verification.json')
    require(canonical(expected)==canonical(observed),'primitive reconstruction mismatch')
    print('PASS_DPG26_BOUNDED_EXACT_CONTROLS')
    print(json.dumps(expected['scope'],sort_keys=True))
    return 0

if __name__=='__main__':
    try: sys.exit(main())
    except (ValueError,OSError,KeyError,TypeError,ZeroDivisionError) as exc:
        print('REJECT_DPG26: '+str(exc),file=sys.stderr); sys.exit(1)
