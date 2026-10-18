#!/usr/bin/env python3
"""Power-sum producer for Gaussian times a real-root Fourier polynomial.

F(z)=exp(-a*z*z)*prod(1-b_j*z*z), a>=0,b_j>0. Matching even
cumulants of degree4+ becomes a finite positive power-sum problem. Optional
inverse Fourier density diagnostics are separate and never assumed.
"""
from decimal import Decimal as D,getcontext
from pathlib import Path
from math import factorial,log,pi
import argparse,json
import numpy as np
import search_full as s


def targets(degree):
    ss=s.get_target(degree);unit=s.unit_cumulants(degree)
    return [D((-1)**(r+1)*r*unit[2*r])*ss[r-1]/factorial(2*r)
            for r in range(2,degree//2+1)]


def guessed_nodes(n):
    # Deliberately rough root guesses, used solely as optimizer initialization.
    rough=[14.13,21.02,25.01,30.42,32.94,37.59,40.92,43.33,48.01,49.77,
           52.97,56.45,59.35,60.83,65.11,67.08,69.55,72.07,75.70,77.14]
    guess_file=s.ROOT/'initial_zero_guesses.json'
    if guess_file.exists():
        rough=list(map(float,json.loads(guess_file.read_text())['values']))
    while len(rough)<n:
        k=len(rough)+1;t=rough[-1]+3
        for _ in range(20):
            f=t/(2*pi)*(log(t/(2*pi))-1)+.875-(k-.5)
            t-=f/(log(t/(2*pi))/(2*pi))
        rough.append(t)
    src=json.loads((s.ROOT/'theta26_source.json').read_text())
    v=D(sum(src['variance']))/(D(2)**(src['bits']+1))
    return [1/(v*D(str(t))**2) for t in rough[:n]]


def value(b,m):
    return [sum(x**r for x in b) for r in range(2,m+2)]


def solve(b,target,maxiter=150):
    m=len(target);history=[]
    for k in range(maxiter):
        val=value(b,m);residual=[y-x for x,y in zip(val,target)]
        error=max(abs(x/y) for x,y in zip(residual,target))
        if error<D('1e-90'):return b,True,history
        jac=[[r*x**(r-1) for x in b] for r in range(2,m+2)]
        scale=list(b)
        rows=[[a*q for a,q in zip(row,scale)]for row in jac]
        gram=[[sum(a*c for a,c in zip(row,other))for other in rows]for row in rows]
        lag=s.linear_solve(gram,residual)
        delta=[q*sum(row[j]*u for row,u in zip(rows,lag))for j,q in enumerate(scale)]
        damping=D(1)
        while damping>D('1e-14'):
            trial=[x+damping*y for x,y in zip(b,delta)]
            if min(trial)>0 and sum(trial)<D('.5'):
                newvalue=value(trial,m)
                newerror=max(abs((x-y)/y)for x,y in zip(newvalue,target))
                if newerror<error:break
            damping/=2
        else:return b,False,history
        b=trial
        history.append({'iteration':k,'error':str(newerror),'damping':str(damping)})
        if k%10==0:print('POWER_NEWTON',k,newerror,damping,flush=True)
    return b,False,history


def density_polynomial(a,b):
    # u=x²/(4a); inverse density is normalized Gaussian times P(u).
    # Multiplication by 1-b*z² corresponds to P + (b/a)L(P), where
    # L(P)=uP''+(.5-2u)P'+(u-.5)P.
    c=[D(1)]
    for beta in b:
        old=c+[D(0)];c=[D(0)]*(len(c)+1)
        for k in range(len(c)):
            c[k]=old[k]*(1-(beta/a)*(2*k+D('.5')))
            if k+1<len(old):c[k]+=(beta/a)*(k+1)*(k+D('.5'))*old[k+1]
            if k:c[k]+=(beta/a)*old[k-1]
    return c


def positivity_diagnostic(c):
    # Only an empirical diagnostic. Complex coefficient/root conditioning is
    # recorded; no root exclusion or positivity theorem is inferred here.
    if all(x>=0 for x in c):
        return {'all_coefficients_positive':all(x>0 for x in c),
                'constant_coefficient':str(c[0]),'approximate_minimum_scaled':1.,
                'candidate_minimum_u':0.,'approximate_positive_critical_points':[],
                'diagnostic_method':'nonnegative ordinary-Decimal coefficients; no root solver'}
    coef=np.array([float(x/max(abs(y)for y in c))for x in c])
    try:
        critical=np.polynomial.polynomial.polyroots(np.array([i*coef[i] for i in range(1,len(coef))]))
    except np.linalg.LinAlgError:
        return {'all_coefficients_positive':False,'constant_coefficient':str(c[0]),
                'approximate_minimum_scaled':None,'diagnostic_method':'root diagnostic failed; positivity unresolved'}
    candidates=[0.]+[float(x.real) for x in critical if abs(x.imag)<1e-5 and x.real>0]
    vals=[np.polynomial.polynomial.polyval(x,coef)for x in candidates]
    return {'all_coefficients_positive':all(x>0 for x in c),
            'constant_coefficient':str(c[0]),
            'approximate_minimum_scaled':min(vals),
            'candidate_minimum_u':candidates[int(np.argmin(vals))],
            'approximate_positive_critical_points':candidates}


def main():
    p=argparse.ArgumentParser();p.add_argument('--degree',type=int,default=22)
    p.add_argument('--nodes',type=int,nargs='+',default=[10,11,12,14,16,20,24,32])
    p.add_argument('--progressive',action='store_true')
    p.add_argument('--without-density',action='store_true',
                   help='omit the optional, non-certifying inverse-density diagnostic')
    p.add_argument('--output',type=Path,
                   help='write exploratory results here instead of the default local record')
    args=p.parse_args();getcontext().prec=140
    target=targets(args.degree);records=[]
    for count in args.nodes:
        print('POLYNOMIAL_FAMILY',args.degree,count,flush=True)
        if args.progressive:
            b=guessed_nodes(count);history=[];ok=False
            for m in range(1,len(target)+1):
                b,ok,local=solve(b,target[:m])
                history.extend(dict(stage=m,**r)for r in local)
                print('POWER_STAGE',m,ok,flush=True)
                if not ok:break
        else:
            b,ok,history=solve(guessed_nodes(count),target)
        a=D('.5')-sum(b)
        record={'nodes':count,'settled':ok,'a':str(a),'b':[str(x)for x in b],
                'target':[str(x)for x in target],'history':history}
        if not args.without_density:
            coeff=density_polynomial(a,b)
            diagnostic=positivity_diagnostic(coeff)
            record.update(density_polynomial_coefficients=[str(x)for x in coeff],
                          positivity_diagnostic=diagnostic)
        print('POLYNOMIAL_RESULT',count,ok,'A',a,flush=True)
        records.append(record)
        label='progressive' if args.progressive else 'direct'
        output=args.output or (s.ROOT/f'gaussian_polynomial{args.degree}_{label}.json')
        output.write_text(json.dumps({
            'status':'EMPIRICAL_POWER_SUM_PRODUCER_NOT_CERTIFICATE',
            'degree':args.degree,'precision':140,'records':records},indent=2)+'\n')


if __name__=='__main__':main()
