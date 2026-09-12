"""Nondirected single-group bias extension of the new STAR26 seed."""
import argparse
import json
from pathlib import Path
import mpmath as mp
import scout as base


def directions():
    active=[base.center[i] for i in base.ACTIVE]
    k=mp.mpf('.01')
    _,J,jet,_=base.evaluate(active,k)
    last=mp.matrix([jet[7].deriv])
    rows=[]
    h=mp.mpf('1e-20')
    for owner in range(9):
        plus=base.evaluate(active,k,owner,h)[2]
        minus=base.evaluate(active,k,owner,-h)[2]
        deriv=mp.matrix([(p.value-m.value)/(2*h) for p,m in zip(plus,minus)])
        rhs=mp.matrix([-deriv[r]/base.target[r] for r in range(7)])
        dx=mp.lu_solve(J,rhs)
        slope=base.FAIR[16]*(deriv[7]+(last*dx)[0])
        row={'owner':owner,'slope16':mp.nstr(slope,40),'parameter_slopes':[mp.nstr(x,30) for x in dx]}
        rows.append(row)
        print(owner,mp.nstr(slope,25),flush=True)
    return rows


def continue_owner(owner, grid):
    active=[base.center[i] for i in base.ACTIVE]
    rows=[]
    for value in grid:
        try:
            active,weights,error,norm=base.solve(active,mp.mpf('.01'),owner,mp.mpf(value))
            row={'extra_bias':value,'moment16_error':mp.nstr(error,40),
                 'normalized_residual':mp.nstr(norm,10),'weights':[mp.nstr(x,65) for x in weights]}
            print(owner,value,mp.nstr(error,25),flush=True)
        except (ValueError,ZeroDivisionError) as exc:
            row={'extra_bias':value,'failure':str(exc)}
            print(owner,value,str(exc),flush=True)
            rows.append(row)
            break
        rows.append(row)
    return rows


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--owner',type=int)
    p.add_argument('--grid',default='0,.001,.002,.005,.01,.02,.05,.1,.2,.3,.5,.7,.9')
    p.add_argument('--release-all',action='store_true')
    args=p.parse_args()
    if args.release_all:
        base.ACTIVE=list(range(10))
    if args.owner is None:
        result={'status':'nondirected scout','directions':directions()}
        name='bias-directions.json'
    else:
        result={'status':'nondirected scout','owner':args.owner,'rows':continue_owner(args.owner,args.grid.split(','))}
        name='bias-path-'+str(args.owner)+('-all' if args.release_all else '')+'.json'
    Path(__file__).with_name(name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
