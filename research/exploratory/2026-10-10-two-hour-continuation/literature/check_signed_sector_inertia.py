"""Exact native signed-sector kernels and bound imported compact witnesses."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt,prod
from pathlib import Path
import argparse
import hashlib
import json
import re


def need(ok,why):
    if not ok:
        raise ArithmeticError(why)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def conjugate(z):
    return z[0]-z[1],-z[1]


def norm(z):
    return z[0]*z[0]-z[0]*z[1]+z[1]*z[1]


def ball_bounds(text):
    match=re.fullmatch(r'\[([0-9.e+\-]+) \+/- ([0-9.e+\-]+)\]',text)
    need(match is not None,'exact printed midpoint-radius ball shape')
    midpoint,radius=map(F,match.groups())
    need(radius>=0,'nonnegative printed radius')
    return midpoint-radius,midpoint+radius


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    here=Path(__file__).resolve()
    directory=here.parent
    guards={
        'FULL_SIGNED_COMPACT_WITNESS.md':'1c0a1718080e6f763a3531f9f9a8f8fcd31868c48d241290406fe4cef61644ca',
        'check_full_signed_compact.py':'ace0ec9a10deef974d3cae842590bc46c2d048e65dfa5b14b659cbc7c380dc50',
        'FOURIER_COMPACT_BALANCED_TRACE.md':'480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120',
        'check_fourier_compact_trace.py':'dddf8f7c12fe022e54e19d9994da6092fd7a3a7e9da1d1d67b6daf6f5c27c598',
        'FULL_SIGNED_COMPACT_WITNESS_INDEPENDENT_REVIEW.md':'5084650971b3af4d5dbb30ed169ecc5f30a4ce463f064edb6bcca3d5ce13d008',
        'independent-full-signed-compact-normal.json':'46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93',
        'independent-full-signed-compact-optimized.json':'46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93',
        'independent-fourier-compact-trace-normal.json':'fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8',
        'independent-fourier-compact-trace-optimized.json':'fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8'}
    for path,expected in guards.items():
        need(sha(directory/path)==expected,'frozen imported compact-source binding '+path)
    C=json.loads((directory/'independent-full-signed-compact-normal.json').read_text())
    L=json.loads((directory/'independent-fourier-compact-trace-normal.json').read_text())
    need(C['tuple_count']==4096 and C['critical_tuple_count']==3696,
         'complete physical critical tuple inventory')
    need(C['D']==30 and C['H']==40,'literal physical scales')
    need(C['proof_sha256']==guards['FULL_SIGNED_COMPACT_WITNESS.md']
         and C['checker_sha256']==guards['check_full_signed_compact.py'],
         'full receipt direct source binding')
    need(L['Schwartz_mollifier_radius']=='1e-12','paid genuine Schwartz radius')
    full_lower,_=ball_bounds(C['full_signed_R2_ball'])
    lead_lower,_=ball_bounds(L['leading_remainder_ball'])
    _,lead_error=ball_bounds(L['smooth_error_bound'])
    # sqrt7 > 2645/1000, so this rational quantity exceeds the full
    # analytic Schwartz budget 3696*2*40*34693*90*delta/sqrt7.
    need(F(2645,1000)**2<7,'strict rational square-root lower bound')
    full_error=F(3696*2*40*34693*90*1000,2645*10**12)
    need(full_error<F(7,20) and full_lower-full_error>8852,
         'complete genuine Schwartz full signed form stays above8852')
    need(lead_error<F(1,1000) and lead_lower-lead_error>3916,
         'complete genuine Schwartz leading form stays above3916')

    # Exact auxiliary spatial disk, independently reconstructed from all
    # actual source prime fields. It is not the compact Fourier source.
    fields=[]
    for q in (7,13,19,31):
        for root in (r for r in range(q) if (r*r+r+1)%q==0):
            generator=next(g for g in range(2,q)
                           if len({pow(g,j,q) for j in range(q-1)})==q-1)
            logs={pow(generator,j,q):j for j in range(q-1)}
            beta=(1+root)%q
            need(logs[beta]%((q-1)//6)==0,'native sixth-root embedding')
            c=logs[beta]//((q-1)//6)
            inverse=pow(c,-1,6)
            table={x:logs[x]*inverse%6 for x in range(1,q)}
            fields.append((q,root,table))
    need(len(fields)==8,'all distinct actual prime ideals')
    H=40
    bound=isqrt(4*H//3)
    rows=[(a,b) for a,b in product(range(-bound,bound+1),repeat=2)
          if 0<norm((a,b))<=H]
    need(len(rows)==150,'complete auxiliary Eisenstein lattice disk')
    symbols=[[None if (a+b*root)%q==0 else table[(a+b*root)%q]
              for q,root,table in fields] for a,b in rows]
    pairs=list(product(range(8),repeat=2))
    pair_symbols=[]
    for p,q in pairs:
        pair_symbols.append([None if row[p] is None or row[q] is None
                             else (row[p]+row[q])%6 for row in symbols])
    units=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]

    def critical(alpha,beta):
        counts=Counter(alpha+beta)
        left=Counter(alpha)
        singles=[p for p,e in counts.items() if e==1]
        same_twice=[p for p,e in counts.items() if e==2 and left[p] in (0,2)]
        g1=prod(fields[p][0] for p in singles)
        g2=prod(fields[p][0] for p in same_twice)
        return bool(singles) and g1*g1*g2>H*H

    matrix=[]
    critical_count=0
    for i,alpha in enumerate(pairs):
        values=[]
        for j,beta in enumerate(pairs):
            if not critical(alpha,beta):
                values.append((0,0))
                continue
            critical_count+=1
            a=b=0
            for v,w in zip(pair_symbols[i],pair_symbols[j]):
                if v is not None and w is not None:
                    x,y=units[(v-w)%6]
                    a+=x;b+=y
            values.append((a,b))
        matrix.append(values)
    need(critical_count==3696,'exact source singleton/conductor critical cutoff')
    need(all(matrix[i][i]==(0,0) for i in range(64)),'every critical diagonal removed')
    need(all(matrix[i][j]==conjugate(matrix[j][i]) for i in range(64) for j in range(64)),
         'complete auxiliary signed kernel Hermitian')
    full=(sum(z[0] for row in matrix for z in row),sum(z[1] for row in matrix for z in row))
    need(full==(1176,0),'independent exact full signed disk witness')
    lead_indices=[i for i,pair in enumerate(pairs) if pair[0]!=pair[1]]
    lead_values=[matrix[i][j] for i in lead_indices for j in lead_indices
                 if len(set(pairs[i]+pairs[j]))==4]
    need(len(lead_indices)==56 and len(lead_values)==1680,'complete ordered leading face')
    leading=(sum(z[0] for z in lead_values),sum(z[1] for z in lead_values))
    need(leading==(456,0),'independent exact leading disk witness')
    witness=next((i,j,matrix[i][j]) for i in range(64) for j in range(i+1,64)
                 if matrix[i][j]!=(0,0))
    i,j,z=witness
    determinant=-norm(z)
    need(determinant<0,'exact native principal two-by-two indefinite witness')
    record=dict(status='PASS_EXACT_SIGNED_SECTOR_KERNEL_INERTIA_CONTROLS',
                source_prime_fields=8,auxiliary_spatial_rows=150,
                full_pair_space_dimension=64,critical_entries=critical_count,
                leading_pair_space_dimension=56,leading_entries=1680,
                exact_full_disk_form=list(full),exact_leading_disk_form=list(leading),
                exact_full_kernel_diagonal_zero=True,exact_full_kernel_Hermitian=True,
                exact_auxiliary_negative_minor={'pair_indices':[i,j],
                    'off_diagonal_Eisenstein_coefficients':list(z),'determinant':determinant},
                actual_Schwartz_full_form_lower_bound=8852,
                actual_Schwartz_leading_form_lower_bound=3916,
                actual_full_minimum_eigenvalue_strict_upper_bound='-2213/1008',
                actual_leading_minimum_eigenvalue_strict_upper_bound='-979/770',
                complete_full_Schwartz_error_rational_upper_bound=str(full_error),
                imported_compact_source_sha256=guards,
                proof_sha256=sha(directory/'SIGNED_SECTOR_KERNEL_INERTIA.md'),
                checker_sha256=sha(here),
                complete_actual_Schwartz_kernel_numerically_recomputed=False,
                negative_eigenvector_source_factorization_claimed=False,
                full_moment_indefinite=False,generalized_moment_obstruction_proved=False,
                asymptotic_generalized_moment_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':
    main()
