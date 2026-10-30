"""Floating-point exploration only: this is not an interval certificate."""
import json, math
import numpy as np
from scipy.special import ive, gammaln
from scipy.optimize import root
from numpy.polynomial.legendre import leggauss

def phi(t):
    t=np.asarray(t); y=np.exp(2*np.abs(t)); ans=np.zeros_like(y)
    for n in range(1,15):
        x=np.pi*n*n*y
        ans+=(4*x*x-6*x)*np.exp(np.abs(t)/2-x)
    return ans

def kernel(a,M,t):
    t=np.asarray(t); nn=np.arange(-M,M+1)
    ww=phi(np.arcsinh(nn/a)/2)
    cc=ive(np.abs(nn),a)*ww
    xx=a*(1-np.cosh(2*t[:,None]))+2*t[:,None]*nn[None,:]
    with np.errstate(divide='ignore'):
        logs=np.log(cc)[None,:]+xx
    mx=np.max(logs,axis=1)
    return np.exp(mx)*np.sum(np.exp(logs-mx[:,None]),axis=1)

nodes,weights=leggauss(900)
t=1.5*(nodes+1); weights=1.5*weights
out={'status':'ordinary floating point diagnostics; no certified zero counts', 'rows':[]}
for a in [.25,.5,1,2,5,10,20,50]:
    M=max(16,int(10*a))
    kval=kernel(a,M,t)
    mass=2*np.dot(weights,kval)
    def F(z): return 2*np.dot(weights*kval,np.cos(z*t))/mass
    def RF(z):
        v=F(z[0]+1j*z[1]); return [v.real,v.imag]
    found=[]
    for x in np.linspace(1,28,15):
        for y in [0,.3,1,2]:
            sol=root(RF,[x,y],tol=1e-9)
            xx,yy=sol.x
            if sol.success and abs(F(xx+1j*yy))<1e-9 and 0<xx<32 and abs(yy)<5:
                if not any(abs(xx-q[0])+abs(yy-q[1])<1e-4 for q in found): found.append([float(xx),float(yy)])
    # necessary coefficient gate, central versus leading coefficient
    c0=ive(0,a)*float(phi(0)); cM=ive(M,a)*float(phi(np.arcsinh(M/a)/2))
    log_gate=math.log(c0)-math.log(cM)-float(gammaln(2*M+1)-2*gammaln(M+1)) if cM>0 else None
    err=float(np.max(np.abs(kernel(a,M,np.linspace(0,1,201))-phi(np.linspace(0,1,201)))))
    row={'a':a,'M':M,'mass':float(mass),'kernel_max_abs_error_on_201_grid_0_1':err,'located_roots':sorted(found),'unit_circle_coefficient_log_violation':log_gate}
    out['rows'].append(row)
    print(a,M,'err',err,'roots',sorted(found),'loggate',log_gate,flush=True)
from pathlib import Path
with (Path(__file__).resolve().parent / 'SKELLAM_DIAGNOSTIC.json').open('w') as f: json.dump(out,f,indent=2)
