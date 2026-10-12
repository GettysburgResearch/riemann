"""Exact native norm37 unit-orbit and local kernel controls."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def need(ok,detail):
    if not ok:
        raise ArithmeticError(detail)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    here=Path(__file__).resolve()
    prior=here.with_name('PAIRED_FREQUENCY_COLLISION.md')
    prior_hash='d057fd4138a4f9c7fcb5455c51e8eabe04b707b8817d4a6ae3359cdfdb85df9a'
    need(hashlib.sha256(prior.read_bytes()).hexdigest()==prior_hash,
         'frozen local source kernel conventions')
    fields=controls=0
    for a,b,root in ((7,3,10),(4,-3,26)):
        need(a*a-a*b+b*b==37 and a%3==1 and b%3==0,
             'actual primary norm37 source prime')
        need((root*root+root+1)%37==0 and (a+b*root)%37==0,
             'actual source prime finite-field root')
        units=[(x+y*root)%37 for x,y in
               ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))]
        need(len(set(units))==6,'complete distinct native sixth units')
        for value in units:
            need(pow(value,6,37)==1,'norm37 native sextic unit symbol is principal')
            controls+=1
        need(pow(0,6,37)==0,'native nonunit symbol retains its zero')
        fields+=1
    q=37
    need(q<64,'actual second frequency phase is feasible')
    k11,k12,k22=F(1),F(3,4),F(1,2)
    need(k11*k22-k12*k12==-F(1,16),'unit-neutral local Euler determinant')
    f1,f2=1+F(1,q),F(3,4)+F(1,q)
    need((f1,f2)==(F(38,37),F(115,148)),'exact native local single factors')
    c11,c12,c22=k11/f1**2,k12/(f1*f2),k22/f2**2
    cd=c11*c22-c12*c12
    need((c11,c12,c22,cd)==(F(1369,1444),F(4107,4370),
                                F(10952,13225),-F(1874161,19096900)),
         'unit-neutral collision congruence remains indefinite')
    record=dict(status='PASS_EXACT_UNIT_NEUTRAL_LOCAL_KERNEL_CONTROLS',
                native_prime_norm=q,actual_primary_generators=[[7,3],[4,-3]],
                actual_prime_fields=fields,unit_symbol_controls=controls,
                local_unit_projector_leaves_kernel_unchanged=True,
                local_Euler_determinant='-1/16',
                local_collision_matrix=[[str(c11),str(c12)],[str(c12),str(c22)]],
                local_collision_determinant=str(cd),
                proof_sha256=hashlib.sha256(here.with_name('UNIT_NEUTRAL_LOCAL_KERNEL.md').read_bytes()).hexdigest(),
                checker_sha256=hashlib.sha256(here.read_bytes()).hexdigest(),
                source_local_kernel_sha256=prior_hash,
                complete_radial_trace_indefiniteness_proved=False,
                generalized_moment_obstruction_proved=False,rh_proved=False)
    args.output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(record['status'])


if __name__=='__main__':
    main()
