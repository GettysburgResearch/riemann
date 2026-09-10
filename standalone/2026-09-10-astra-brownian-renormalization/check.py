#!/usr/bin/env python3
"""Exact bounded algebra for BRN26. Not an analytic proof or zero certificate."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def ak(k: int) -> F:
    return F(1) if k == 0 else (1-F(1,2**(2*k-1)))/(2*k-1)


def convolution(a: list[F], b: list[F], k: int) -> F:
    return sum((F(math.comb(k,j))*a[j]*b[k-j] for j in range(k+1)),F(0))


def encode(value):
    if isinstance(value,F):
        return str(value.numerator)+'/'+str(value.denominator)
    if isinstance(value,list):
        return [encode(x) for x in value]
    if isinstance(value,dict):
        return {k:encode(v) for k,v in value.items()}
    return value


def canonical(value) -> str:
    return json.dumps(value,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n'


def reconstruct() -> dict:
    order,depth=16,12
    r=F(7,12)
    require(2*ak(2)==r,'variance contraction primitive')
    require(ak(3)/ak(2)==F(93,140),'tilted mean primitive')
    require(2*ak(3)==F(31,80),'third moment contraction')

    # Fixed moments: inverse sinh series, separately compared with the
    # distributional fixed-point recurrence.
    cc=[F(1)]
    for k in range(1,order+1):
        cc.append(-sum((F(6**j,math.factorial(2*j+1))*cc[k-j]
                        for j in range(1,k+1)),F(0)))
    fixed=[(-1)**k*math.factorial(k)*cc[k] for k in range(order+1)]
    for k in range(order+1):
        require(fixed[k]==ak(k)*convolution(fixed,fixed,k),'fixed sinh moment')
        require(fixed[k]<=math.factorial(k),'fixed moment majorant')
    require(fixed[1]==1 and fixed[2]==F(7,5),'fixed normalization')

    bm=[F(1)]
    for k in range(1,order+1):
        b=ak(k+2)/ak(2)
        bm.append(b/(1-b)*sum((F(math.comb(k,j))*bm[j]*fixed[k-j]
                               for j in range(k)),F(0)))
    cm=[convolution(bm,fixed,k) for k in range(order+1)]
    require(bm[1]==F(93,47) and cm[1]==F(140,47),'perpetuity means')
    tangent=[F(0),F(0)]+[F(k*(k-1),2)*bm[k-2] for k in range(2,order+1)]
    for k in range(2,order+1):
        require(r*tangent[k]==2*ak(k)*convolution(tangent,fixed,k),
                'linearized fixed-point eigenmode')

    lower=[F(1) for _ in range(order+1)]
    upper=[F(math.factorial(k)) for k in range(order+1)]
    B=[2*(F(math.factorial(k))-F(1,(k+1)*(k+2))) for k in range(order+1)]
    require(B[0]==1,'defect density mass')
    tables=[]
    companion_checks=0
    for n in range(depth+1):
        mix=[(a+b)/2 for a,b in zip(lower,upper)]
        C=[convolution(B,mix,k) for k in range(order+1)]
        zl=[convolution(lower,lower,k)/2**k for k in range(order+1)]
        zu=[convolution(upper,upper,k)/2**k for k in range(order+1)]
        require(lower[1]==upper[1]==1,'mean')
        require(lower[2]-1==F(2,5)*(1-r**n),'lower variance')
        require(upper[2]-1==F(2,5)+F(3,5)*r**n,'upper variance')
        for k in range(order+1):
            require(lower[k]<=math.factorial(k) and upper[k]<=math.factorial(k),
                    'finite positive moment bound')
            rhs=F(0) if k<2 else r**n*F(k*(k-1),2**k)*C[k-2]
            require(zu[k]-zl[k]==rhs,'exact full defect identity at integer moment')
            companion_checks+=1
        tables.append(encode({'n':n,'lower':lower,'upper':upper,'B':B,'C':C}))
        if n<depth:
            B=[ak(k+2)/ak(2)*convolution(B,mix,k) for k in range(order+1)]
            lower=[ak(k)*convolution(lower,lower,k) for k in range(order+1)]
            upper=[ak(k)*convolution(upper,upper,k) for k in range(order+1)]

    # Rational chord identity: its explicit nonnegative factorization is
    # separately derived from the two endpoint values.
    panels=[]
    a,b=F(1,4),F(1)
    for t in [F(0),F(1,8),F(1,2),F(1),F(3),F(17),F(100)]:
        for j in range(17):
            x=a+(b-a)*F(j,16)
            f=lambda z:z/(1+t*z)
            gap=f(x)-((b-x)*f(a)+(x-a)*f(b))/(b-a)
            fact=t*(x-a)*(b-x)/((1+t*x)*(1+t*a)*(1+t*b))
            require(gap==fact and fact>=0,'concave chord factorization')
            panels.append(encode([t,x,gap]))

    # Gamma integral remainder constants use exact factorial ratios.
    inverse=[]
    for p in range(1,17):
        k=(2*p-1).bit_length() # 2**k >= 2*p
        value=F(4**(k*p)*math.factorial(2**k-p-1),math.factorial(2**k-1))
        bound=F((8*p)**p)
        require(value<=bound,'complete inverse moment majorant')
        inverse.append(encode([p,k,value]))

    # Formal differential-dilation equation, coefficient by coefficient.
    dilation=0
    for row in tables:
        aa=[F(x) for x in row['upper']]
        for k in range(1,order+1):
            coeff=ak(k)*convolution(aa,aa,k)
            require((2*k-1)*coeff==(1-F(2,4**k))*convolution(aa,aa,k),
                    'differential-dilation coefficient')
            dilation+=1

    full=encode({'fixed':fixed,'fixed_B':bm,'fixed_C':cm,
                 'tables':tables,'chords':panels,'inverse_bounds':inverse})
    digest=hashlib.sha256(canonical(full).encode()).hexdigest()
    return {'packet':'BRN26','status':'BOUNDED_EXACT_ALGEBRA_ONLY','rh_proved':False,
            'all_band_phase_proved':False,
            'maximum_moment':order,'maximum_depth':depth,
            'fixed_moment_checks':order+1,'tangent_checks':order-1,
            'defect_moment_checks':companion_checks,
            'variance_checks':2*(depth+1),'chord_checks':len(panels),
            'inverse_bound_checks':len(inverse),'dilation_checks':dilation,
            'r':'7/12','b1':'93/140','mean_B_star':'93/47','mean_C_star':'140/47',
            'full_table_sha256':digest}


def reject_number(text):
    raise ValueError('noninteger JSON number rejected: '+text)


def pairs(items):
    out={}
    for k,v in items:
        require(k not in out,'duplicate JSON key')
        out[k]=v
    return out


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=reject_number,parse_constant=reject_number)


def self_test(expected: dict) -> int:
    with tempfile.TemporaryDirectory() as td:
        receipt=Path(td)/'result.json'
        cmd=[sys.executable,'-I','-S','-B']
        if sys.flags.optimize:
            cmd+=['-'+'O'*sys.flags.optimize]
        cmd += [str(Path(__file__).resolve()),'--check',str(receipt)]
        def run(text):
            receipt.write_text(text,encoding='utf-8')
            return subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                                  check=False).returncode
        require(run(canonical(expected))==0,'pristine CLI rejected')
        bad=[]
        for key,val in [('rh_proved',True),('r','7/13'),('defect_moment_checks',220),
                        ('maximum_depth',11),('full_table_sha256','0'*64),
                        ('all_band_phase_proved',0)]:
            altered=dict(expected);altered[key]=val;bad.append(canonical(altered))
        bad.append(canonical(expected).replace('"maximum_depth":12','"maximum_depth":12.0'))
        bad.append(canonical(expected).replace('"packet":"BRN26"','"packet":"BRN26","packet":"BRN26"'))
        for text in bad:
            require(run(text)!=0,'altered CLI receipt accepted')
    return len(bad)


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    group=ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--emit',type=Path)
    group.add_argument('--check',type=Path)
    ap.add_argument('--self-test',action='store_true')
    args=ap.parse_args()
    result=reconstruct()
    if args.emit:
        args.emit.write_text(canonical(result),encoding='utf-8')
    else:
        require(canonical(load(args.check))==canonical(result),'receipt differs from reconstruction')
    adverse=self_test(result) if args.self_test else 0
    print(canonical({'ok':True,'full_table_sha256':result['full_table_sha256'],
                     'actual_cli_refusals':adverse}),end='')

if __name__=='__main__':
    try:
        main()
    except (OSError,ValueError,TypeError,KeyError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        sys.exit(1)
