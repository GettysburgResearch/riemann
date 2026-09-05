"""Optional NON_DIRECTED_HIGH_PRECISION regression, never a proof dependency."""
import argparse
import json
from pathlib import Path
import mpmath as mp
import source_moments as sm

mp.mp.dps = 70

def logarithm(u):
    s=(1+mp.sqrt(9+4*u))/2
    return mp.log(s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)/2)

def run():
    coefficients=mp.taylor(logarithm,0,6)
    moments,_=sm.source_moments()
    rows=[]
    for j,interval in enumerate(moments,1):
        value=(-1)**(j-1)*j*coefficients[j]
        lo=mp.mpf(interval.lo.numerator)/interval.lo.denominator
        hi=mp.mpf(interval.hi.numerator)/interval.hi.denominator
        rows.append({'moment':j,'inside_rational_interval':bool(lo<=value<=hi),
                     'value':mp.nstr(value,60)})
    if not all(row['inside_rational_interval'] for row in rows):
        raise RuntimeError('NONPROOF regression disagreement')
    return {'arithmetic':'NON_DIRECTED_HIGH_PRECISION_REGRESSION','dps':70,
            'mpmath_version':mp.__version__,'rows':rows,'proof_dependency':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args();result=run()
    text=json.dumps(result,indent=2)+'\n';path=Path(__file__).with_name('REGRESSION.json')
    if args.write:path.write_text(text)
    elif path.read_text()!=text:raise SystemExit('NONPROOF stored regression mismatch')
    print('PASS_NONPROOF_SOURCE_REGRESSION')
