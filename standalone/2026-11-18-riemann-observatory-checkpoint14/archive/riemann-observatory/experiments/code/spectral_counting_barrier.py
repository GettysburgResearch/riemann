"""Exact rational checks of the finite-channel spectral-counting lemma.
Run: python experiments/code/spectral_counting_barrier.py
Only decoupled loops are computed; the coupled result is proved in the note.
No zeta-zero computation and no RH inference occur here.
"""
from fractions import Fraction as F
from math import floor, pi, log
import json
from pathlib import Path

def count(K, loops):
    # l_j=2*pi*r_j, eigenvalues (n+c_j)/r_j, n integer.
    return sum(floor(r*K-c)-floor(-c) for r,c in loops)

def main():
    loops=[(F(3,2),F(0)),(F(5,7),F(1,3)),(F(7,9),F(5,8))]
    E=len(loops); rate=sum(r for r,c in loops)
    samples=[]
    for K in [F(1),F(10),F(100),F(1000),F(10_000)]:
        Ns=[count(m*K,loops) for m in [1,2,4]]
        D=Ns[2]-3*Ns[1]+2*Ns[0]
        errors=[abs(F(n)-rate*m*K) for n,m in zip(Ns,[1,2,4])]
        assert all(err < E for err in errors)
        assert abs(D) < 3*E
        samples.append({'K':str(K),'counts_K_2K_4K':Ns,'exact_discrepancies':[str(e) for e in errors],'dyadic_curvature':D,'RVM_main_term_curvature_float':float(K)*log(2)/pi})
    result={'status':'exact_rational_sanity_checks_passed','scope':'decoupled_loop_examples_only','edge_count':E,'total_length_over_2pi':str(rate),'samples':samples,'warning':'Floating RVM curvature values illustrate an analytically derived asymptotic; they are not rigorous zeta-zero counts.'}
    out=Path(__file__).resolve().parents[1]/'results'/'spectral_counting_barrier.json'
    out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
