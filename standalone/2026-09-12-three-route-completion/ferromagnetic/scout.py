"""NON-DIRECTED exploration of the exact one-edge merger at the ICR26 seed."""
import json
import math
import subprocess
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 65
SHA = '0640c9c59be0bf20c18258460a7517fb09728e82'
PREFIX = 'standalone/2026-09-12-astra-interacting-cluster-realization/'

def old_json(name):
    return json.loads(subprocess.check_output(['git', 'show', SHA+':'+PREFIX+name], text=True))

def cumulants(moments):
    out = [mp.mpf(0)]*len(moments)
    for n in range(1, len(moments)):
        out[n] = moments[n]-sum(math.comb(n-1,j-1)*out[j]*moments[n-j] for j in range(1,n))
    return out

N=16
c=cumulants([mp.mpf(1) if k%2==0 else mp.mpf(0) for k in range(N+1)])
d=cumulants([mp.mpf(1)]+[mp.mpf(3)/5 if k%2==0 else mp.mpf(0) for k in range(1,N+1)])
ar=[d[2*k]/c[2*k] for k in range(1,9)]
pars=old_json('parameters.json')
x=[mp.mpf(v) for v in pars['centers']]
nu=pars['multiplicities']
target=old_json('result.json')
s=[mp.mpf(a+b)/mp.mpf(2)**321 for a,b in target['standardized_cumulant_ratios']]

def merged_moments(x,y,tau,maximum=16):
    a,b=mp.sqrt(y),mp.sqrt(x)
    out=[]
    for n in range(maximum+1):
        total=mp.mpf(0)
        for si,ti,ei in [(si,ti,ei) for si in [-1,1] for ti in [-1,1] for ei in [-1,1]]:
            weight=(mp.mpf(3)/10 if si==ti else mp.mpf(1)/5)/2*(1+tau*si*ei)
            total+=weight*(a*(si+ti)/2+b*ei)**n
        out.append(total)
    return out

def normalized_jet(variables,tau,owner):
    xx,yy=list(variables[:6]),variables[6]
    cc=cumulants(merged_moments(xx[owner],yy,tau))
    return [sum((nu[j]-(j==owner))*xx[j]**r for j in range(6))+cc[2*r]/c[2*r] for r in range(1,9)]

J=mp.matrix([[r*nu[j]*x[j]**(r-1) for j in range(6)]+[r*ar[r-1]*x[6]**(r-1)] for r in range(1,8)])
last=mp.matrix([[8*nu[j]*x[j]**7 for j in range(6)]+[8*ar[7]*x[6]**7]])
rows=[]
for j in range(6):
    deriv=mp.matrix([mp.diff(lambda t:normalized_jet(x,t,j)[k],0) for k in range(8)])
    dx=-mp.lu_solve(J,deriv[:7,:])
    derivative=c[16]*(deriv[7]+(last*dx)[0])
    rows.append({'owner_group':j,'compensated_standardized_moment16_derivative':mp.nstr(derivative,35),
                 'parameter_derivatives':[mp.nstr(v,25) for v in dx]})

result={'status':'non-directed-scout-not-a-certificate','source':SHA,'base_unmatched16':mp.nstr(c[16]*(normalized_jet(x,0,0)[7]-s[7]),35),'rows':rows}
Path(__file__).with_name('scout-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

if '--continue' in sys.argv:
    paths=[]
    for owner in [0,2]:
        previous=x[:]
        samples=[]
        ratios=['0.01','0.025','0.05','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','0.95','0.99'] if owner==0 else ['0.001','0.0025','0.005','0.01','0.025','0.05','0.1']
        for ratio in ratios:
            tau=mp.mpf(ratio)
            try:
                def equations(*v):
                    values=normalized_jet(v,tau,owner)
                    return tuple((values[k]-s[k])/s[k] for k in range(7))
                answer=mp.findroot(equations,tuple(previous),tol=mp.mpf('1e-40'),maxsteps=12)
                if any(abs(mp.im(t))>mp.mpf('1e-40') or mp.re(t)<=0 for t in answer):
                    raise ValueError('left positive domain')
                previous=[mp.re(t) for t in answer]
                error=c[16]*(normalized_jet(previous,tau,owner)[7]-s[7])
                samples.append({'tau':ratio,'error16':mp.nstr(error,25),'parameters':[mp.nstr(t,25) for t in previous]})
                print('PATH',owner,ratio,mp.nstr(error,20),flush=True)
            except (ValueError,ZeroDivisionError) as exc:
                samples.append({'tau':ratio,'failure':str(exc)[:160]})
                print('FAILED',owner,ratio,str(exc)[:100],flush=True)
                break
        paths.append({'owner_group':owner,'samples':samples})
    Path(__file__).with_name('continuation-scout.json').write_text(json.dumps({'status':'non-directed-scout-not-a-certificate','paths':paths},indent=2)+'\n')
