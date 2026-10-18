"""Exact rational coefficient/arithmetic controls for THETA_GROWTH.md.

The complete analytic inequalities are proved in prose; these controls check
the rational constants and polynomial identities used for the infinite tail.
"""
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:raise ValueError(message)

def shift(poly,a):
    out=[F(0)]*len(poly)
    for j,c in enumerate(poly):
        for k in range(j+1):out[k]+=c*comb(j,k)*a**(j-k)
    return out

def main():
    e3=sum(F(3**j,factorial(j)) for j in range(9));require(e3>20,'e^3 rational lower sum')
    require(shift([F(-171),F(144),F(-31),F(2)],F(7))==[F(4),F(4),F(11),F(2)],'first-term curvature polynomial')
    require(F(4)-F(4,9)==F(32,9),'negative-shift quadratic minimum')
    N=F(4);C=36*N*N*(N-1)**2+3*N*(N-1)*(12*(N-1)**2+16*(N-1)+F(32,3));require(C==11184,'exact first ratio second-derivative coefficient')
    require((F(4,3))**8<10 and F(10,20**7)<F(1,2),'complete index tail ratio')
    tail=F(2*87*3**8,20**8);require(tail<F(1,1000),'all n>=3 tail bound')
    require(F(11184,20**3)+F(1,1000)<F(7,5),'complete ratio curvature upper bound')
    require(19-F(7,5)==F(88,5),'final logconcavity constant')
    out={'status':'EXACT_GROWTH_CONSTANT_CONTROLS_PASS','e3_lower_sum':str(e3),'n2_second_derivative_coefficient':11184,'n_ge3_tail_upper':str(tail),
        'strong_logconcavity_constant':'88/5','theta_gaussian_coefficient':'5/176',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    txt=json.dumps(out,sort_keys=True,separators=(',',':'))+'\n';(ROOT/'growth_controls.json').write_text(txt)
    print('GROWTH_CONSTANT_CONTROLS_PASS',hashlib.sha256(txt.encode()).hexdigest())

if __name__=='__main__':main()
