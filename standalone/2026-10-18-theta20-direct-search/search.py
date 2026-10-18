"""Bounded dense ferromagnetic search. No solver outcome is a proof certificate."""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from models import MomentModel
ROOT=Path(__file__).resolve().parent

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--initial',type=Path,default=ROOT/'records'/'compound0.json')
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--steps',type=int,default=100)
    ap.add_argument('--hidden',type=int,default=3)
    args=ap.parse_args()
    if not 1<=args.steps<=10000:ap.error('--steps must lie between 1 and 10000')
    if args.output.exists():ap.error('refusing to overwrite an existing record')
    z=np.asarray(json.loads(args.initial.read_text())['z'])
    recurrence=list(map(float,json.loads((ROOT/'target.json').read_text())['an']))
    model=MomentModel([1]*12,recurrence,gaussian=True,hidden=args.hidden)
    if not model.admissibility(z)['passes_parameter_sign_conditions']:
        ap.error('input is outside the nonnegative parameter class')
    lo=np.r_[np.full(13,1e-5),np.full(model.count-13,1e-10)]
    hi=np.r_[np.full(13,1.5),np.full(model.count-13,3.)]
    out=least_squares(lambda q:model.evaluate(q)[0],z,jac=lambda q:model.evaluate(q)[1],
                      bounds=(lo,hi),max_nfev=args.steps,gtol=1e-14,ftol=1e-14,
                      xtol=1e-14,x_scale='jac')
    result={'status':'NUMERICAL_EXPLORATION_ONLY','err':float(np.linalg.norm(out.fun)),
            'z':out.x.tolist(),'residuals':out.fun.tolist(),'evaluations':out.nfev,
            'solver_message':out.message,**model.admissibility(out.x)}
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('z','residuals')},indent=2))
if __name__=='__main__':main()
