#!/usr/bin/env python3
"""Finite ordinary-high-precision Fourier checks, NOT interval certificates."""
import json
import mpmath as mp
from verify import rational_native, multiplicative_power

mp.mp.dps = 45
records=[]
for X,k,T,t0 in [(32,1,'0.75','0.3'),(32,3,'1.5','-0.2'),(64,2,'1.25','0.7')]:
    a=rational_native(X)
    a={n:v for n,v in enumerate(a) if X/2<n<=X and v}
    b=multiplicative_power(a,k)
    T=mp.mpf(T);t0=mp.mpf(t0)
    exact=mp.mpc(0)
    for n,c in b.items():
        for m,d in b.items():
            r=mp.log(mp.mpf(n)/m)
            exact += c*d*mp.exp(-T*T*r*r/2+1j*t0*r)
    # A harmless common phase X^(-it) avoids large carrier oscillations.
    def integrand(z):
        t=t0+T*z
        value=sum(c*mp.exp(1j*t*mp.log(mp.mpf(n)/X)) for n,c in a.items())
        return abs(value)**(2*k)*mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
    observed=mp.quad(integrand,[-20,-10,-5,-2,0,2,5,10,20])
    error=abs(exact-observed)
    if error>mp.mpf('1e-32'):raise RuntimeError((X,k,error))
    records.append({'X':X,'order':2*k,'T':str(T),'center':str(t0),
                    'kernel':mp.nstr(exact.real,24),'quadrature':mp.nstr(observed,24),
                    'absolute_error':mp.nstr(error,6)})
print(json.dumps({'scope':'Finite 45-digit non-directed quadrature; not certification or an infinite source evaluation.',
                  'records':records},indent=2,sort_keys=True))
