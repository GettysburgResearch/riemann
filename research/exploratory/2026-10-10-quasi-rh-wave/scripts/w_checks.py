# Note W bookkeeping checks: delta cap, primes-only counts, class-resolved row savings (variants of exponent_model.py)
import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exponent_model as em
from exponent_model import *
P=dict(DEFAULT)
# (3) cap delta at 3/4 (zero classes a>7/8 empty)
def Hmod_cap(b,l,P,dmax):
    lx,ly,h=geom(b,l); zsup=l/h
    delta=np.linspace(2*P['a0']-1,dmax,ND); x=np.linspace(0,.5,NX)
    R=Rstar_grid(delta,x,P,zsup); E=E0(delta[:,None],x[None,:],b,l,h,R,P)
    i,j=np.unravel_index(np.argmax(E),E.shape); return float(E[i,j]),(float(delta[i]),float(x[j]))
def Bach(b,l,P,hm):
    ok,c=feasible(b,l,P)
    if not ok: return np.inf
    return max(Blow(b,l,P),hm(b,l,P)[0],Hfloor(b,l,P),Hint(b,l,P))
from scipy.optimize import minimize
def opt(hm,P):
    best=(np.inf,None)
    for b in np.linspace(0.005,0.4,9):
        for l in np.linspace(0.10,0.33,13):
            v=Bach(b,l,P,hm)
            if v<best[0]: best=(v,(b,l))
    r=minimize(lambda p:Bach(p[0],p[1],P,hm),best[1],method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-10,maxiter=400))
    return r.fun,r.x
for dmax in [5/6,3/4,0.70,0.60,0.50,0.40]:
    B,x=opt(lambda b,l,P:Hmod_cap(b,l,P,dmax),P); print(f"(3) dmax={dmax:.3f}: B={B:.6f} b={x[0]:.4f} l={x[1]:.4f}")
# (4) primes-only detector: R = 1 - delta*k*z with capacity k z <= 1/2 (sextic sieve) -> R = 1-delta/2 ; ideal large sieve kz<=1 -> R=1-delta
def Hmod_R(b,l,P,Rf):
    lx,ly,h=geom(b,l); delta=np.linspace(2*P['a0']-1,P['alpha'],ND); x=np.linspace(0,.5,NX)
    R=Rf(delta)[:,None]+0*x[None,:]; E=E0(delta[:,None],x[None,:],b,l,h,R,P)
    i,j=np.unravel_index(np.argmax(E),E.shape); return float(E[i,j]),(float(delta[i]),float(x[j]))
for lab,Rf in [("primes-only sextic sieve R=1-d/2",lambda d:1-d/2),("primes-only ideal sieve R=1-d",lambda d:1-d),("R=1-2d/3 (no primes)",lambda d:1-2*d/3)]:
    B,x=opt(lambda b,l,P:Hmod_R(b,l,P,Rf),P); print(f"(4) {lab}: B={B:.6f} b={x[0]:.4f} l={x[1]:.4f}")
# floor power saving f applied to ALL classes with delta<delta1 (continuum) : R -> R - f for delta<=delta1, with paper R* else
def Hmod_f(b,l,P,f,d1):
    lx,ly,h=geom(b,l); zsup=l/h; delta=np.linspace(2*P['a0']-1,P['alpha'],ND); x=np.linspace(0,.5,NX)
    R=Rstar_grid(delta,x,P,zsup); R=np.where(delta[:,None]<=d1,R-f,R); E=E0(delta[:,None],x[None,:],b,l,h,R,P)
    i,j=np.unravel_index(np.argmax(E),E.shape); return float(E[i,j]),(float(delta[i]),float(x[j]))
def Hfloor_f(b,l,P,f):
    lx,ly,h=geom(b,l); return E0(2*P['a0']-1,0.5,b,l,h,1.0-f,P)
def Bach_f(b,l,P,f,d1):
    ok,c=feasible(b,l,P)
    if not ok: return np.inf
    return max(Blow(b,l,P),Hmod_f(b,l,P,f,d1)[0],Hfloor_f(b,l,P,f),Hint(b,l,P))
def opt_f(f,d1):
    best=(np.inf,None)
    for b in np.linspace(0.005,0.4,9):
        for l in np.linspace(0.10,0.33,13):
            v=Bach_f(b,l,P,f,d1)
            if v<best[0]: best=(v,(b,l))
    r=minimize(lambda p:Bach_f(p[0],p[1],P,f,d1),best[1],method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-10,maxiter=400))
    return r.fun,r.x
for f in [0.05,0.1,0.25,0.5]:
    for d1 in [0.05,0.2,0.4,5/6]:
        B,x=opt_f(f,d1); print(f"(5) row-saving f={f} on classes delta<={d1:.2f}: B={B:.6f} b={x[0]:.4f} l={x[1]:.4f}")
