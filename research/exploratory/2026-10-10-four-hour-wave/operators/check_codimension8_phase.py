#!/usr/bin/env python3
"""Outward-ball phase-aware all-frequency codimension-eight primitive gap."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import flint
from flint import arb,ctx
from check_coercivity import require,log_rational_bounds
from check_codimension14 import atan_bounds


def certify():
    ctx.prec=160
    al,ah=atan_bounds(Q(1,5),16)
    bl,bh=atan_bounds(Q(1,239),8)
    pi_lo=16*al-4*bh
    pi_hi=16*ah-4*bl
    require(pi_lo>Q(31415,10000),'pi>3.1415')
    require(pi_hi<Q(3927,1250),'pi<3.1416')
    log2_lo,log2_hi=log_rational_bounds(Q(2))
    require(log2_hi<Q(1733,2500),'log2<.6932')
    h1024=sum((Q(1,j) for j in range(1,1025)),Q())
    require(h1024-10*log2_lo<Q(289,500),'gamma<.578')
    _,logpi_hi=log_rational_bounds(Q(3927,1250),64)
    require(logpi_hi<Q(1431,1250),'logpi<1.1448')
    require(Q(289,500)+Q(3927,2500)+3*Q(1733,2500)+Q(1431,1250)<Q(43,8),'Omega0>-43/8')
    require(Q(707,500)**2<2,'sqrt2>707/500')
    require(Q(1733,2500)/Q(707,500)<Q(491,1000),'q2<491/1000')
    scale=2**100
    log2=arb(2).log()
    q2=log2/arb(2).sqrt()
    alpha=Q(4,5)
    constant=244
    def gamma_lower(x):
        return Q(sum((scale*16*x)//((4*k+1)*((4*k+1)**2+4*x))
                     for k in range(257)),scale)
    def as_arb(x):
        return arb(x.numerator)/x.denominator
    def p(x):
        return (Q(x)+Q(1,4))**2/(Q(x)+Q(9,4))
    minimum=None
    mincell=None
    for left in range(4096):
        right=left+1
        phase=(arb(left).sqrt()*log2).union(arb(right).sqrt()*log2)
        cosphase=phase.cos()
        vlo=(as_arb(-Q(43,8)+gamma_lower(left))-2*q2*cosphase).lower()
        product=as_arb(p(right) if vlo<0 else p(left))*vlo
        margin=(product-as_arb(alpha*right)+constant).lower()
        require(margin>0,('phase-aware cell',left,str(margin)))
        if minimum is None or margin<minimum:
            minimum,mincell=margin,left
    tail_v=-Q(43,8)-Q(491,500)+gamma_lower(4096)
    require(tail_v>alpha,'tail V>.8')
    require(constant>Q(7,4)*tail_v,'tail supporting-line constant')
    kappa=Q(3,2)*(alpha-Q(constant,36)/Q(31415,10000)**2)
    require(kappa>Q(1,6),'five sine constraints yield kappa>1/6')
    return {
      'status':'DIRECTED_PHASE_COVERAGE_ACCEPT',
      'scope':'literal L=1 source primitive gap on complement dimension8; no effective sign',
      'arithmetic':'exact Fraction gamma floors and outward Arb cosine/root/log balls',
      'python_flint_version':flint.__version__,'precision_bits':ctx.prec,
      'supporting_line':{'alpha':str(alpha),'constant':constant},
      'removed_sine_modes':5,'complement_dimension':8,'gamma_last_index':256,
      'compact_cells':4096,'minimum_cell_margin':{'cell':mincell,'lower':minimum.str(45,more=True)},
      'tail_v_lower':str(tail_v),'kappa_lower':str(kappa),'reported_kappa':'1/6',
      'residual_coefficient':'27/2',
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'helper_sha256':{name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                       for name in ['check_coercivity.py','check_codimension14.py']},
      'classical_inputs':['Machin identity','gamma<H1024-log1024','digamma partial fractions'],
      'not_proved':['eight-dimensional effective sign','all windows','RH'],
    }

if __name__=='__main__':
    print(json.dumps(certify(),indent=2))
