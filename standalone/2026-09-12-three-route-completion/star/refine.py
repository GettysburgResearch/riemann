"""High-precision minimum-norm Newton attempts on the nineteen-parameter star.
This is ordinary numerical exploration; positivity and residual checks are not
interval root existence proofs.
"""
import json
from pathlib import Path
import mpmath as mp
import scout as base

base.ACTIVE=list(range(19))


def evaluate(values):
    variables=[]
    for i,v in enumerate(values):
        d=[mp.mpf(0)]*19
        d[i]=mp.mpf(1)
        variables.append(base.Dual(v,d))
    jet=base.graph(variables[:10],0,biases=variables[10:])
    return (mp.matrix([(jet[r].value-base.target[r])/base.target[r] for r in range(8)]),
            mp.matrix([[d/base.target[r] for d in jet[r].deriv] for r in range(8)]))


def solve(values,scaling):
    values=mp.matrix(values)
    history=[]
    status='iteration budget'
    for it in range(50):
        residual,jac=evaluate(values)
        norm=max(abs(x) for x in residual)
        history.append({'iteration':it,'maximum_relative_residual':mp.nstr(norm,20)})
        if norm<mp.mpf('1e-45'):
            status='numerical root; not certified'
            break
        D=mp.diag([mp.mpf(1) if scaling=='unit' else max(v,mp.mpf('1e-6')) for v in values])
        jj=jac*D
        step=D*jj.T*mp.lu_solve(jj*jj.T,-residual)
        accepted=False
        for j in range(30):
            candidate=values+mp.mpf(2)**(-j)*step
            if min(candidate)<=0 or max(candidate[10:])>=1:
                continue
            if max(abs(x) for x in evaluate(candidate)[0])<norm:
                values=candidate
                accepted=True
                break
        if not accepted:
            status='positive-domain line search stalled'
            break
    print(scaling,status,history[-1],flush=True)
    return {'status':status,'scaling':scaling,'history':history,
            'weights':[mp.nstr(v,65) for v in values[:10]],
            'biases':[mp.nstr(v,65) for v in values[10:]]}


if __name__=='__main__':
    previous=json.loads(Path(__file__).with_name('full-scout-result.json').read_text())
    source=[mp.mpf(str(v)) for v in previous['weights']+previous['biases']]
    results=[solve(source,mode) for mode in ['unit','relative']]
    Path(__file__).with_name('refine-result.json').write_text(json.dumps(
        {'status':'nondirected exploration only','source':base.STAR,
         'target_source':base.ICR,'attempts':results},indent=2)+'\n',encoding='utf-8')
