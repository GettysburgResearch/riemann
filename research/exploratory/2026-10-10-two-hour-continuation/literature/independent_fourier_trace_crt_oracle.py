"""Independent complete-period CRT/Gauss/cubic oracle for one actual conductor."""
from collections import Counter
from itertools import combinations
from math import gcd
from pathlib import Path
import argparse
import hashlib
import json
from flint import arb, acb, ctx


def need(ok, label):
    if not ok:
        raise ArithmeticError(label)


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def conj(x):
    a, b = x
    return a-b, -b


units = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    base = Path('/workspace/riemann/research/exploratory/2026-10-10-two-hour-continuation/literature')
    bindings = {'FOURIER_COMPACT_BALANCED_TRACE.md':
                '480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120',
                'check_fourier_compact_trace.py':
                'dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598'}
    for file, expected in bindings.items():
        need(hashlib.sha256((base/file).read_bytes()).hexdigest()==expected,
             'frozen companion packet')
    fields=[]
    # Residue roots/discrete logarithms, independent of producer Euler-symbol lookup.
    for q in (7,13):
        for root in (r for r in range(q) if (r*r+r+1)%q==0):
            generator=next(g for g in range(2,q)
                           if len({pow(g,j,q) for j in range(q-1)})==q-1)
            logs={pow(generator,j,q):j for j in range(q-1)}
            beta=(1+root)%q
            c=logs[beta]//((q-1)//6)
            need(logs[beta]%((q-1)//6)==0 and gcd(c,6)==1,
                 'source sixth-unit embedding via discrete logarithms')
            inv=pow(c,-1,6)
            table=[None]+[logs[x]*inv%6 for x in range(1,q)]
            candidates=[(a,b) for a in range(-q,q+1) for b in range(-q,q+1)
                        if norm((a,b))==q and a%3==1 and b%3==0
                        and (a+b*root)%q==0]
            need(len(candidates)==1,'unique primary generator reconstructed from root')
            fields.append({'q':q,'root':root,'table':table,'pi':candidates[0],
                           'charge':((q-1)//6)%6})
    conductor=(1,0)
    for field in fields:
        conductor=mul(conductor,field['pi'])
    need(conductor==(91,0) and norm(conductor)==8281,'actual complete CRT period')
    omega=acb(-arb(1)/2,arb(3).sqrt()/2)
    zeta=[acb(a)+b*omega for a,b in units]
    for field in fields:
        q=field['q']; b=field['pi'][1]
        gamma=acb(0)
        for x in range(1,q):
            # Literal e(x/pi); no arbitrary additive finite-field character.
            gamma+=zeta[field['table'][x]]*acb(0,-2*arb.pi()*b*x/q).exp()
        field['gamma']=gamma/arb(q).sqrt()

    allocations=[]
    for left in combinations(range(4),2):
        signs=[1 if i in left else -1 for i in range(4)]
        if sum(s*f['charge'] for s,f in zip(signs,fields))%6==0:
            allocations.append(signs)
    need(len(allocations)==4,'four neutral allocations in this conductor')
    char_sums=[(0,0) for _ in allocations]
    covariance=[[ (0,0) for _ in allocations] for _ in allocations]
    gauss_counts=[Counter() for _ in allocations]
    active=0
    for a in range(91):
        for b in range(91):
            es=[f['table'][(a+b*f['root'])%f['q']] for f in fields]
            if None in es:
                continue
            active+=1
            phases=[sum(s*e for s,e in zip(signs,es))%6 for signs in allocations]
            for i,e in enumerate(phases):
                x,y=units[e]
                xx,yy=char_sums[i]
                char_sums[i]=(xx+x,yy+y)
                gauss_counts[i][(b,e)]+=1
                for j,ee in enumerate(phases):
                    x,y=units[(e-ee)%6]
                    xx,yy=covariance[i][j]
                    covariance[i][j]=(xx+x,yy+y)
    need(active==5184 and char_sums==[(0,0)]*4,'complete-period first means and masks')
    for i in range(4):
        for j in range(4):
            need(covariance[i][j]==((5184,0) if i==j else (0,0)),
                 'complete-period exact cubic quotient orthogonality')
    gaps=[]
    for signs,counts in zip(allocations,gauss_counts):
        direct=acb(0)
        for (b,e),count in sorted(counts.items()):
            direct+=count*zeta[e]*acb(0,2*arb.pi()*b/91).exp()
        direct/=91
        crt=acb(1)
        for i,(sign,field) in enumerate(zip(signs,fields)):
            other=(1,0)
            for j,f in enumerate(fields):
                if i!=j:other=mul(other,f['pi'])
            v=(other[0]+other[1]*field['root'])%field['q']
            need(v!=0,'actual coprime CRT complement')
            phase=field['gamma']*zeta[field['table'][v]]
            crt*=phase if sign==1 else (-1)**field['charge']*phase.conjugate()
        gap=direct-crt
        need(gap.real.contains(0) and gap.imag.contains(0)
             and gap.abs_upper()<arb('1e-45'),'direct complete Gauss sum equals source CRT')
        need(direct.abs_lower()>arb('0.999999999999'),'primitive complete Gauss norm')
        gaps.append(gap.abs_upper().str(25,more=True))
    record={'status':'PASS_INDEPENDENT_COMPLETE_PERIOD_FOURIER_TRACE_CRT_ORACLE',
            'oracle_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'frozen_packet':bindings,'precision_bits':192,
            'fields':[{'q':f['q'],'root':f['root'],'primary_generator':f['pi']} for f in fields],
            'complete_residue_period':8281,'conductor':conductor,
            'active_residue_classes':active,'neutral_allocations':4,
            'exact_first_character_means':char_sums,
            'exact_cubic_covariance':covariance,
            'direct_complete_gauss_CRT_overlap_checks':4,
            'gauss_difference_absolute_upper_bounds':gaps,
            'asymptotic_trace_bound_proved':False,'full_R2_lower_bound_proved':False,
            'rh_proved':False}
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':main()
