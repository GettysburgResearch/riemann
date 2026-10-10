"""Exact Eisenstein sextic diagnostics; not a proof of asymptotic moments."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

O = tuple[int, int]
ROOT_O: tuple[O, ...] = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ROOT_C: tuple[O, ...] = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

def norm(z: O) -> int:
    a,b=z; return a*a-a*b+b*b

def mul(x: O,y: O) -> O:
    a,b=x;c,d=y;return a*c-b*d,a*d+b*c-b*d

def conj(z: O) -> O:
    a,b=z;return a-b,-b

def sub(x: O,y: O) -> O:
    return x[0]-y[0], x[1]-y[1]

def quotient(x: O,p: O) -> O | None:
    a,b=mul(x,conj(p));q=norm(p)
    return (a//q,b//q) if a%q==0 and b%q==0 else None

def residue(x: O,p: O) -> O:
    a,b=mul(x,conj(p));q=norm(p)
    return sub(x,mul(p,(a//q,b//q)))

def powmod(x: O,e: int,p: O) -> O:
    r=(1,0);x=residue(x,p)
    while e:
        if e&1:r=residue(mul(r,x),p)
        x=residue(mul(x,x),p);e//=2
    return residue(r,p)

def isprime(n: int) -> bool:
    if n<2:return False
    return all(n%d for d in range(2,math.isqrt(n)+1))

def lattice(limit: int) -> list[O]:
    R=2*math.isqrt(limit)+3
    return sorted(((a,b) for a in range(-R,R+1) for b in range(-R,R+1)
                   if 0<norm((a,b))<=limit),key=lambda z:(norm(z),z))

def primary_ideals(limit: int) -> list[O]:
    return [z for z in lattice(limit) if z[0]%3==1 and z[1]%3==0
            and (z[0]%2 or z[1]%2)]

def prime_elements(limit: int) -> list[O]:
    out=[]
    for z in primary_ideals(limit):
        q=norm(z);r=math.isqrt(q)
        if isprime(q) or (r*r==q and isprime(r) and r%3==2):out.append(z)
    return out

def factor(z: O,primes: list[O]) -> tuple[tuple[int,...],bool]:
    f=[];sf=True;left=z
    for j,p in enumerate(primes):
        if norm(p)>norm(left):break
        e=0
        while (v:=quotient(left,p)) is not None:
            left=v;e+=1
        if e:
            f.extend([j]*e)
            sf &= e==1
    if norm(left)!=1:raise ValueError(f'unfactored ideal {z}: {left}')
    return tuple(f), sf

def symbol_prime(u: O,p: O) -> int:
    if quotient(u,p) is not None:return -1
    z=powmod(u,(norm(p)-1)//6,p)
    roots={residue(r,p):e for e,r in enumerate(ROOT_O)}
    if len(roots)!=6 or z not in roots:raise ValueError('invalid sixth root')
    return roots[z]

def independent_symbol_prime(u: O,p: O) -> int:
    """Independent quotient-field coordinates: F_p or F_p[omega]."""
    q=norm(p)
    if isprime(q):
        w=(-p[0]*pow(p[1],-1,q))%q
        if (w*w+w+1)%q:raise ValueError('bad split-field embedding')
        a=(u[0]+u[1]*w)%q
        if a==0:return -1
        v=pow(a,(q-1)//6,q);r=(1+w)%q
        return {pow(r,j,q):j for j in range(6)}[v]
    ell=math.isqrt(q)
    if ell*ell!=q or not isprime(ell) or ell%3!=2:
        raise ValueError('not an inert prime ideal')
    def mm(x,y):
        a,b=x;c,d=y
        return (a*c-b*d)%ell,(a*d+b*c-b*d)%ell
    x=(u[0]%ell,u[1]%ell)
    if x==(0,0):return -1
    r=(1,0);e=(q-1)//6
    while e:
        if e&1:r=mm(r,x)
        x=mm(x,x);e//=2
    return {(a%ell,b%ell):j for j,(a,b) in enumerate(ROOT_O)}[r]

def c_mul(z: O,w: O) -> O:
    a,b=z;c,d=w;return a*c-b*d,a*d+b*c+b*d

def c_norm(z: O) -> int:
    a,b=z;return a*a+a*b+b*b

def fjson(x: Fraction | int) -> dict:
    f=Fraction(x)
    return {'numerator':str(f.numerator),'denominator':str(f.denominator)}

class Guards:
    def __init__(self):self.counts={}
    def check(self,ok: bool,label: str):
        if not ok:raise AssertionError(label)
        self.counts[label]=self.counts.get(label,0)+1

def run(D: int=48,H: int=48) -> dict:
    if not (4<=D<=96 and 4<=H<=96):raise ValueError('diagnostic range: 4 <= D,H <= 96')
    G=Guards();rows=lattice(2*H-1);pr=prime_elements(D);pn=[norm(p) for p in pr]
    cols=[]
    for z in primary_ideals(D):
        f,sf=factor(z,pr)
        zz=(1,0)
        for j in f:zz=mul(zz,pr[j])
        G.check(zz==z,'native_primary_factor_reconstruction')
        if sf:cols.append((z,norm(z),frozenset(f),(-1)**len(f)))
    phases=[[symbol_prime(u,p) for u in rows] for p in pr]
    # Residue arithmetic, genuine zero extensions and unit characters.
    for j,p in enumerate(pr):
        q=norm(p)
        for idx,u in enumerate(rows):
            e=phases[j][idx]
            G.check(e==independent_symbol_prime(u,p),'native_independent_quotient_field')
            G.check((e==-1)==(quotient(u,p) is not None),'native_prime_zero_mask')
            G.check(symbol_prime(mul(u,ROOT_O[1]),p)==(-1 if e<0 else (e+(q-1)//6)%6),
                    'native_unit_covariance')
        for u in rows[:min(19,len(rows))]:
            for v in rows[:min(19,len(rows))]:
                a=symbol_prime(u,p);b=symbol_prime(v,p)
                G.check(symbol_prime(mul(u,v),p)==(-1 if min(a,b)<0 else (a+b)%6),
                        'native_residue_multiplicativity')
    @lru_cache(None)
    def phase(f: frozenset[int]) -> tuple[int,...]:
        return tuple(-1 if any(phases[j][i]<0 for j in f)
                     else sum(phases[j][i] for j in f)%6 for i in range(len(rows)))
    weights=[(2*H-norm(u))**8 for u in rows];rowden=(2*H)**8
    # Product columns and all balanced allocations, for the box n/X in (1/2,1].
    allocations: dict[frozenset[int],list[tuple[int,int]]] = {}
    for _,n,f,_ in cols:
        for _,m,g,_ in cols:
            if f.isdisjoint(g):allocations.setdefault(f|g,[]).append((n,m))
    products=sorted(allocations,key=lambda f:(math.prod(pn[j] for j in f),tuple(sorted(f))))
    ps=[phase(f) for f in products];sgn=[(-1)**len(f) for f in products]
    Nr=[math.prod(pn[j] for j in f) for f in products]
    L=math.lcm(*range(1,D+1))**3
    scale=[L//m**3-L//(m+1)**3 for m in range(1,D)]
    W=[[sum(n<=m<2*n and v<=m<2*v for n,v in allocations[f])
        for f in products] for m in range(1,D)]
    active=[i for i in range(len(products)) if any(w[i] for w in W)]
    products=[products[i] for i in active];ps=[ps[i] for i in active]
    sgn=[sgn[i] for i in active];Nr=[Nr[i] for i in active]
    W=[[w[i] for i in active] for w in W]
    size=len(products)
    gram=[[sum(scale[m]*W[m][i]*W[m][j] for m in range(D-1))
           for j in range(size)] for i in range(size)]
    gram_tail=[[sum(scale[m]*W[m][i]*W[m][j] for m in range(max(1,D//2)-1,D-1))
                for j in range(size)] for i in range(size)]
    total_direct=0;tail_direct=0;moment={k:0 for k in [1,2,3,4]}
    for m in range(1,D):
        for ri,u in enumerate(rows):
            a=b=0;ba=bb=0
            for _,n,f,mu in cols:
                if n<=m<2*n:
                    e=phase(f)[ri]
                    if e>=0:
                        x,y=ROOT_C[e];a+=mu*x;b+=mu*y
            for j in range(size):
                e=ps[j][ri]
                if e>=0:
                    x,y=ROOT_C[e];v=sgn[j]*W[m-1][j];ba+=v*x;bb+=v*y
            # Independently enumerate the original ordered coprime pair sum.
            ia=ib=0
            active_cols=[c for c in cols if c[1]<=m<2*c[1]]
            for _,n,f,mu in active_cols:
                for _,nn,g,mv in active_cols:
                    if f.isdisjoint(g):
                        e=phase(f|g)[ri]
                        if e>=0:
                            x,y=ROOT_C[e];ia+=mu*mv*x;ib+=mu*mv*y
            G.check((ba,bb)==(ia,ib),'native_balanced_product_identity')
            G.check(c_norm((a,b))>=0 and c_norm((ba,bb))>=0,'native_nonnegative_norms')
            contribution=scale[m-1]*weights[ri]*c_norm((ba,bb))
            total_direct+=contribution
            if m>=max(1,D//2):tail_direct+=contribution
            for k in moment:moment[k]+=scale[m-1]*weights[ri]*c_norm((a,b))**k
    diag=0;off=0;tail_diag=0;tail_off=0;bands={};surviving=0;unitzeros=0;maskzeros=0
    for i,f in enumerate(products):
        for j in range(i,size):
            gij=gram[i][j]
            if not gij:continue
            x=y=0
            for ri in range(len(rows)):
                a=ps[i][ri];b=ps[j][ri]
                if min(a,b)>=0:
                    v,w=ROOT_C[(a-b)%6];x+=weights[ri]*v;y+=weights[ri]*w
            if i==j:
                G.check(y==0 and x>=0,'native_diagonal_kernel')
                diag+=gij*x;tail_diag+=gram_tail[i][j]*x;continue
            q=math.prod(pn[t] for t in f^products[j])
            G.check(q>1,'native_offdiagonal_nonprincipal_conductor')
            label_i=sum((pn[t]-1)//6 for t in f)%6
            label_j=sum((pn[t]-1)//6 for t in products[j])%6
            G.check(label_i==(Nr[i]-1)//6%6 and label_j==(Nr[j]-1)//6%6,
                    'native_unit_label_norm_congruence')
            if label_i!=label_j:
                G.check(x==0 and y==0,'native_radial_block_zero');unitzeros+=1
            term=sgn[i]*sgn[j]*gij*(2*x+y);off+=term
            tail_term=sgn[i]*sgn[j]*gram_tail[i][j]*(2*x+y);tail_off+=tail_term
            if term:surviving+=1
            key=str(q.bit_length()-1)
            d=bands.setdefault(key,{'signed':0,'tail_signed':0,'absolute_real_pairs':0,'pairs':0,'nonzero_pairs':0})
            d['signed']+=term;d['tail_signed']+=tail_term;d['absolute_real_pairs']+=abs(term);d['pairs']+=1
            d['nonzero_pairs']+=int(term!=0)
            # Exact mask identity, checked at every genuine row.
            common=f & products[j];left=f-products[j];right=products[j]-f
            pf=phase(left);pg=phase(right);pc=phase(common)
            for ri in range(len(rows)):
                actual=-1 if min(ps[i][ri],ps[j][ri])<0 else (ps[i][ri]-ps[j][ri])%6
                expected=-1 if min(pf[ri],pg[ri],pc[ri])<0 else (pf[ri]-pg[ri])%6
                G.check(actual==expected,'native_common_mask_identity')
                if actual<0:maskzeros+=1
    G.check(total_direct==diag+off,'native_full_integrated_covariance_identity')
    G.check(tail_direct==tail_diag+tail_off,'native_annular_covariance_identity')
    den=3*L*rowden
    bandout={key:{'norm_range':f'[{2**int(key)}, {2**(int(key)+1)})',
                  'signed':fjson(Fraction(v['signed'],den)),
                  'annular_signed':fjson(Fraction(v['tail_signed'],den)),
                  'absolute_real_pairs':fjson(Fraction(v['absolute_real_pairs'],den)),
                  'pairs':v['pairs'],'nonzero_pairs':v['nonzero_pairs']}
             for key,v in sorted(bands.items(),key=lambda kv:int(kv[0]))}
    # Explicit negative controls are executable, not assertions.
    rejected=[]
    if not any(pn[t] and phases[t][i]<0 for t in range(len(pr)) for i in range(len(rows))):
        raise RuntimeError('zero-mask rejection fixture absent')
    try:
        t,i=next((t,i) for t in range(len(pr)) for i in range(len(rows)) if phases[t][i]<0)
        G.check(phases[t][i]==0,'reject_removed_zero_mask')
    except AssertionError:rejected.append('removed_zero_mask')
    else:raise RuntimeError('bad zero mask accepted')
    try:G.check(total_direct==diag+off+1,'reject_forged_covariance')
    except AssertionError:rejected.append('forged_covariance')
    else:raise RuntimeError('bad covariance accepted')
    if off==0:raise RuntimeError('diagonal-only rejection fixture absent')
    try:G.check(total_direct==diag,'reject_discarded_offdiagonal')
    except AssertionError:rejected.append('discarded_offdiagonal')
    else:raise RuntimeError('bad diagonal-only formula accepted')
    # Rational frontier identities are tested independently of the arithmetic sample.
    for dd in range(1,8):
        delta=Fraction(dd,16)
        q=1/(1-delta)
        G.check(q*(1-delta)==1 and 1<q<2,'rational_conductor_cutoff')
        G.check(-2*delta+1+delta==1-delta,'rational_first_join')
        G.check(2*(1-delta)==1+2*(Fraction(1,2)-delta),'rational_second_join')
    primitive={'rows':rows,'primes':pr,'inputs':[(z,n,sorted(f),mu) for z,n,f,mu in cols]}
    primitive_hash=hashlib.sha256(json.dumps(primitive,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'schema':1,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'primitive_inventory_sha256':primitive_hash,'status':'exact finite actual-Eisenstein diagnostic; not asymptotic certification',
      'D':D,'H':H,'field':'Q(sqrt(-3))','target':'principal',
      'excluded_prime_support':[2,3],'column_window':'1_(1/2,1]',
      'scale_exponent':3,'row_window':'(1-Nu/(2H))_+^8',
      'rows':len(rows),'squarefree_input_ideals':len(cols),'good_prime_ideals':len(pr),
      'product_columns':size,'unit_forced_zero_pairs':unitzeros,'nonzero_offdiagonal_pairs':surviving,
      'common_mask_zero_instances':maskzeros,'total_balanced_integral':fjson(Fraction(total_direct,den)),
      'diagonal':fjson(Fraction(diag,den)),'signed_offdiagonal':fjson(Fraction(off,den)),
      'signed_over_diagonal':fjson(Fraction(off,diag)),
      'annular_scale_range':[max(1,D//2),D],
      'annular_total':fjson(Fraction(tail_direct,den)),
      'annular_diagonal':fjson(Fraction(tail_diag,den)),
      'annular_signed_offdiagonal':fjson(Fraction(tail_off,den)),
      'annular_signed_over_diagonal':fjson(Fraction(tail_off,tail_diag)),
      'moment_integrals_common_X_minus_3_weight':{str(k):fjson(Fraction(v,den)) for k,v in moment.items()},
      'conductor_bands':bandout,'successful_checks':G.counts,
      'total_successful_checks':sum(G.counts.values()),'negative_controls_rejected':rejected}

def main() -> None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--D',type=int,default=48)
    p.add_argument('--H',type=int,default=48);g=p.add_mutually_exclusive_group()
    g.add_argument('--write',type=Path);g.add_argument('--check',type=Path)
    a=p.parse_args();out=run(a.D,a.H);text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if a.write:a.write.write_text(text,encoding='utf-8')
    if a.check:
        supplied=json.loads(a.check.read_text(encoding='utf-8'))
        if supplied!=out:raise SystemExit('REJECT: complete primitive reconstruction mismatch')
    print(text,end='')
if __name__=='__main__':main()
