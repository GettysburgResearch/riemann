"""Optional nondirected center producer. Only certify20.py proves a root.

The starting seed and active coordinates are finite witness data. This script
reconstructs the original theta intervals, then applies ordinary Decimal
Newton iterations to their midpoints. No optimizer or cached theta target is
used. Its output must still pass the separate directed certificate.
"""
from pathlib import Path
from decimal import Decimal as D, getcontext
import argparse, json
import theta_source
from connected_blocks import jet, COUNTS
from tree_core import linear_solve

ROOT=Path(__file__).resolve().parent
ACTIVE=[6,0,15,21,3,27,9,12,4,42]

def produce():
    getcontext().prec=100
    src=theta_source.reconstruct()
    target=[D(sum(x))/D(2*2**src['bits']) for x in src['standardized_cumulant_ratios']]
    seed=json.loads((ROOT/'seed20.json').read_text())
    z=[D(x) for x in seed['parameters']]
    z[1]=D(0);z[2]=D(1)
    for iteration in range(15):
        values,jacobian,_=jet(z,active=ACTIVE,eta=D('1e-10'))
        step=linear_solve(jacobian,[target[i]-values[i] for i in range(10)])
        for j,x in zip(ACTIVE,step):z[j]+=x
        print('DECIMAL_CORRECTION',iteration,max(abs(x) for x in step),flush=True)
        if max(abs(x) for x in step)<D('1e-85'):break
    else:raise ArithmeticError('nondirected producer did not settle')
    if not all(z[i]>z[i+1]>0 and D('.5')<z[i+2]<1 for i in range(3,len(z),3)):
        raise ValueError('producer left positive model domain')
    return {'schema':'T20D.parameters.v1','status':'rational-center-input-not-certificate',
            'active':ACTIVE,'centers':[str(x) for x in z],
            'counts':list(COUNTS),'hub_correlation':'1/10000000000',
            'radius':'1/1000000000000000000000000000000','single_blocks':[0],
            'dimer_blocks':list(range(1,len(COUNTS)))}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--emit',type=Path,required=True);a=p.parse_args()
    a.emit.write_text(json.dumps(produce(),indent=2)+'\n')
    print('NONDIRECTED_CENTER_WRITTEN',flush=True)
