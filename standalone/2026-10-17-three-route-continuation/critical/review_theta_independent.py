#!/usr/bin/env python3
"""Independent exact replay of the displayed row formulas.

This does not import verify_theta.py. It uses direct coefficient formulas and
an elementary interval majorant, not that checker's Bernstein conversion.
Imported analytic inputs are outside its coverage.
"""
from fractions import Fraction as Q
from collections import Counter
import json

def require(condition, message):
    if not condition:
        raise ValueError(message)

A=Q(2243,5000); H=1-A; TH=A/2; Z0=Q(2,5); EMAX=Q(1,1000000)
thresholds=[Q(i,10000) for i in range(6728,9401)]

def g(s):
    q=2*s-1
    if s<=Q(11,12):
        return (9*q*(7-6*q)-10)/(6*q*(10-6*q)-10)
    return (1-q)*(8*q-5)/(1-6*(1-q)**2)

def domain(x,y,z):
    return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
            6*x+6*z-5,x-Q(1,2),3*x-2,3*x+y-Q(5,2)]

rows=[]
# (name, method, x0, x1, y0, y1, nu0, nu1)
rows.append(('good','mean',thresholds[0],1,Q(1,2),0,1,0))
for j,(lo,hi) in enumerate(zip(thresholds,thresholds[1:])):
    if lo<Q(69,100): method='mean'; y0=Q(1,2); y1=0
    elif lo<Q(86,100): method='interpolated'; y0=max(1-hi,Q(5,2)-3*hi); y1=1
    else: method='convexity'; y0=1-hi; y1=1
    rows.append((f'middle-{j}',method,hi,1,y0,y1,g(lo),1))
rows.append(('last','convexity',1,1,0,1,g(thresholds[-1]),1))

worst=None
method_counts=Counter()
for name,method,x0,x1,y0,y1,n0,n1 in rows:
    method_counts[method]+=1
    x0,x1,y0,y1,n0,n1=map(Q,(x0,x1,y0,y1,n0,n1))
    if method=='mean':
        R=[(n0+1)/2-Z0,n1/2,Q(0)]
    elif method=='interpolated':
        R=[Q(1,2)+n0*(1-y0)-Z0,n1*(1-y0)-n0*y1,-n1*y1]
        require(0<y0 and y0+y1*EMAX<Q(1,2), name+' interpolation range')
    else:
        R=[n0+(1-y0)/2-Z0,n1-y1/2,Q(0)]
    R=list(map(Q,R))
    c0=A/2+x0-1+H*Z0+A*(y0-1)+H*R[0]
    c1=x1+A*y1+R[0]+H*R[1]
    c2=R[1]+H*R[2]
    c3=R[2]
    coeffs=(c0,c1,c2,c3)
    # Direct upper bound on the full e interval; no endpoint sampling shortcut.
    # growth-theta-4e <= (c0-theta)+sum max(ck,0)e^k,
    # with k=1 coefficient c1-4.
    upper=c0-TH+max(c1-4,0)*EMAX+max(c2,0)*EMAX**2+max(c3,0)*EMAX**3
    require(upper<0, name+' full-interval budget')
    lower_R=R[0]+min(R[1],0)*EMAX+min(R[2],0)*EMAX**2
    require(lower_R>0,name+' positive U exponent')
    # Every domain inequality is affine in e; zero at e=0 is permitted only
    # when its slope is strictly positive, since the interval excludes zero.
    for label,(vx0,vx1,vy0,vy1) in [('xi-stage',(x0,x1,1,1)),('w-stage',(x0,x1,y0,y1))]:
        values0=domain(vx0,vy0,Z0)
        values1=domain(vx0+vx1*EMAX,vy0+vy1*EMAX,Z0)
        for k,(left,right) in enumerate(zip(values0,values1)):
            require(left>=0 and right>0,f'{name}/{label}/{k} domain')
    if name.startswith('middle'):
        margin=TH-c0
        require(margin>0,name+' constant margin')
        if worst is None or margin<worst['margin']:
            worst={'name':name,'margin':margin,'coefficients':coeffs}

require(len(rows)==2674,'class count')
require(method_counts=={'mean':173,'interpolated':1700,'convexity':801},'method counts')
require(worst['margin']==Q(20321474869,416197180000000),'worst exact margin')
require(Q(5,6)-A/3==Q(3419,5000),'Mellin shift')
require(Q(5,6)+A/6==Q(9081,10000),'boundary')
small=H*Z0+Q(1,1000)*(Q(5,4)-Z0)
require(small==Q(22141,100000)<TH,'small-norm budget')
require(H*Z0+Q(1,100)*(Q(5,4)-Z0)>TH,'old-cutoff negative control')
large=A/2+3+3*A+H-10
require(large==-Q(9757,2000),'large-norm budget')
require(Q(2)+2*Q(14,25)-Q(6000,1000)<-1,'horizontal-tail coarse exponent')
print(json.dumps({'status':'PASS','row_count':len(rows), 'method_counts':dict(method_counts),
    'minimum_margin':str(worst['margin']), 'worst_row':worst['name'],
    'worst_polynomial':[str(x) for x in worst['coefficients']],
    'coverage':'direct rational row exponents and affine domains on the full stated e interval; no imported analytic theorem'},indent=2))
