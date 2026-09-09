#!/usr/bin/env python3
"""Optional fixed-point numerical regression, NEVER a proof or acceptance input."""
import json
import platform
from pathlib import Path
import mpmath as mp

mp.mp.dps = 50

def primes(n):
    a = [True] * (n + 1)
    a[0:2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if a[p]:
            a[p*p:n+1:p] = [False] * len(range(p*p, n+1, p))
    return [p for p in range(2, n+1) if a[p]]

rows = []
for x in (101, 1009, 10007):
    ps = [p for p in primes(x) if p != 67]
    L = mp.log(x)
    for t in (mp.mpf('0.4'), mp.mpf('1.1'), mp.mpf('3')):
        s = 1 + 1j*t
        P = mp.fprod(1-mp.power(p,-s) for p in ps)
        D = 1/(mp.zeta(s)*(1-mp.power(67,-s)))
        z = (s-1)*L
        C = mp.exp(-mp.e1(z))
        Ein = mp.quad(lambda u: z if u == 0 else (1-mp.exp(-z*u))/u, [0,1])
        entire = mp.exp(mp.euler)*z*mp.exp(-Ein)
        rows.append({
            'X':x, 't':str(t),
            'raw_error':mp.nstr(abs(P-D),22),
            'completed_error':mp.nstr(abs(P*C-D),22),
            'two_correction_forms_difference':mp.nstr(abs(C-entire),8)
        })
result = {
    'classification':'NON_DIRECTED_HIGH_PRECISION_NON_PROOF',
    'digits':50, 'python':platform.python_version(), 'mpmath':mp.__version__,
    'rows':rows,
    'scope':'Nine fixed arithmetic points. No global norm, PNT rate, zero-free region, or RH certificate.'
}
print(json.dumps(result,sort_keys=True,indent=2))
