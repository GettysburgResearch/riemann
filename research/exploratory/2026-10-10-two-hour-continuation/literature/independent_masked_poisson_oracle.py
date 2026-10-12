"""Independent Gaussian direct/Poisson control of an actual masked critical group."""
from collections import Counter
from math import isqrt, gcd
from pathlib import Path
import argparse
import hashlib
import json
from flint import arb, acb, ctx


def need(ok, label):
    if not ok:raise ArithmeticError(label)


def norm(z):
    a,b=z
    return a*a-a*b+b*b


def make_field(q,root):
    generator=next(g for g in range(2,q)
                   if len({pow(g,j,q) for j in range(q-1)})==q-1)
    logs={pow(generator,j,q):j for j in range(q-1)}
    c=logs[(1+root)%q]//((q-1)//6)
    need(logs[(1+root)%q]%((q-1)//6)==0 and gcd(c,6)==1,'native unit embedding')
    inv=pow(c,-1,6)
    return [None]+[logs[x]*inv%6 for x in range(1,q)]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=192
    source=Path('/workspace/.riemann-research/sources/qrh11-12.tex')
    source_hash='d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d'
    need(hashlib.sha256(source.read_bytes()).hexdigest()==source_hash,'frozen literal source')
    roots=[r for r in range(7) if (r*r+r+1)%7==0]
    need(roots==[2,4],'two independent prime fields over7')
    tables=[make_field(7,r) for r in roots]
    mask_root=3
    need((mask_root*mask_root+mask_root+1)%13==0,'actual mask prime over13')
    candidates=[(a,b) for a in range(-13,14) for b in range(-13,14)
                if norm((a,b))==13 and a%3==1 and b%3==0
                and (a+b*mask_root)%13==0]
    need(candidates==[(4,3)],'source primary mask generator reconstructed')
    d=candidates[0]
    def phase(z):
        a,b=z
        values=[table[(a+b*r)%7] for table,r in zip(tables,roots)]
        return None if None in values else (values[0]-values[1])%6
    units=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
    omega=acb(-arb(1)/2,arb(3).sqrt()/2)
    zeta=[acb(a)+b*omega for a,b in units]
    gauss=acb(0)
    for a in range(7):
        for b in range(7):
            e=phase((a,b))
            if e is not None:
                gauss+=zeta[e]*acb(0,2*arb.pi()*b/7).exp()
    gauss/=7
    need(gauss.abs_lower()>arb('0.999999999999')
         and (gauss*gauss.conjugate()).real.contains(1),'direct49-class primitive Gauss norm')
    chi_d=zeta[phase(d)]
    need(phase(d)==3,'nontrivial source chi(d) phase exercised')
    N=1024
    counts=Counter(); masked=Counter(); total_rows=0; deleted=0
    amax=isqrt(4*N//3)
    for a in range(-amax,amax+1):
        t=isqrt(4*N-3*a*a)
        for b in range(-(-(a-t)//2),(a+t)//2+1):
            z=(a,b);n=norm(z)
            if n==0:continue
            need(0<n<=N,'complete exact norm inequalities')
            total_rows+=1
            e=phase(z)
            if e is None:continue
            counts[n,e]+=1
            if (a+b*mask_root)%13:
                masked[n,e]+=1
            else:deleted+=1
    def summed(counter,lam,conjugated=False):
        out=acb(0)
        for (n,e),number in sorted(counter.items()):
            out+=number*zeta[(-e if conjugated else e)%6]*(-lam*n).exp()
        return out
    def tail(lam):
        # c_n<=# {0<Nu<=n}<=16n for every integer n>=1.
        # The complete geometric derivative bounds the whole omitted lattice.
        x=(-lam).exp()
        return 16*x**(N+1)*((N+1)/(1-x)+x/(1-x)**2)
    H=arb(40); c=2/arb(3).sqrt()
    lam0=arb.pi()*c/H
    lam1=arb.pi()*c*H/49
    lam13=lam1/13
    direct=summed(masked,lam0)
    dual1=summed(counts,lam1,True)
    dual13=summed(counts,lam13,True)
    poisson=H*gauss/7*(dual1-chi_d*dual13/13)
    complete_tail=tail(lam0)+H/7*(tail(lam1)+tail(lam13)/13)
    gap=(direct-poisson).abs_upper()
    need(gap<complete_tail+arb('1e-48'),'independent primal/Poisson complete tail overlap')
    need(complete_tail<arb('1e-34'),'explicit whole Gaussian tail is small')
    wrong_phase=H*gauss/7*(dual1-dual13/13)
    wrong_norm=H*gauss/7*(dual1-chi_d*dual13)
    need((wrong_phase-poisson).abs_lower()>arb('1e-6'),'chi(d) omission rejected')
    need((wrong_norm-poisson).abs_lower()>arb('1e-6'),'Nd amplitude omission rejected')
    need(deleted>0,'principal nonunit mask actually exercised')
    record={'status':'PASS_INDEPENDENT_MASKED_GAUSSIAN_PRIMAL_POISSON_ORACLE',
            'oracle_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_sha256':source_hash,'precision_bits':192,'H':40,
            'primitive_modulus_generator':[7,0],'primitive_norm':49,
            'local_exponents':[1,5],'mask_generator':d,'mask_norm':13,
            'source_chi_mask_generator_exponent':phase(d),
            'complete_truncated_lattice_norm':N,'complete_truncated_rows':total_rows,
            'principal_zero_rows_exercised':deleted,
            'direct_masked_gaussian_ball':direct.str(50,more=True),
            'primitive_masked_Poisson_ball':poisson.str(50,more=True),
            'difference_absolute_upper':gap.str(40,more=True),
            'whole_omitted_Gaussian_tail_upper':complete_tail.str(40,more=True),
            'wrong_chi_d_difference_lower':(wrong_phase-poisson).abs_lower().str(40,more=True),
            'wrong_Nd_amplitude_difference_lower':(wrong_norm-poisson).abs_lower().str(40,more=True),
            'full_compact_R2_independently_recomputed':False,
            'asymptotic_moment_proved':False,'rh_proved':False}
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':main()
