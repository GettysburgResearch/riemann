from numeric_probe import vals,B0,L0
import numpy as np
from scipy.optimize import minimize

d=.446;p=.5;v=5/6-d
R=lambda B,L:1-d+v*d*((1-p)*(1-2*p*B/L))/(v*(3-p-4*p/L)+d*(1-p)*(2-4*p/L))
base=R(B0,L0); grid=(np.linspace(0,1,9),np.linspace(0,.5,9),np.linspace(0,1,7))
def val(x):
 cross,A,D,k=x;return vals([cross,A,D,k/1000],grid)
def obj(x):
 cross,A,D,k=x;return (R(B0-cross*k/1000,L0-k/1000)-base)*1e7
for guess in [[.09,1.2,80,1],[.08,1.2,100,.5],[.07,1,100,.4],[.05,1,100,.1]]:
 q=minimize(obj,guess,method='SLSQP',bounds=[(.02,.0999),(.01,30),(.01,10000),(.001,3)],constraints=[{'type':'ineq','fun':lambda x:val(x)-1e-8}], options={'maxiter':300,'ftol':1e-11})
 print(q.success, q.x,'score',q.fun,'margin',min(val(q.x)),q.message,flush=True)
