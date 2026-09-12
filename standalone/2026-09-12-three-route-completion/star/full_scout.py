"""Bounded numerical exploration with all star weights and biases released.

Ordinary mpmath AD feeds a SciPy floating optimizer. No certification.
"""
import json
from pathlib import Path
import time
import numpy as np
from scipy.optimize import least_squares
import mpmath as mp
import scout as base

base.ACTIVE = list(range(19))
start = [float(x) for x in base.center] + [float(x/100) for x in base.center[:-1]]
cache_x, cache_value = None, None
calls = 0
t0 = time.monotonic()


def evaluate(x):
    global cache_x, cache_value, calls
    if cache_x is not None and np.array_equal(x, cache_x):
        return cache_value
    dual = []
    for i, val in enumerate(x):
        d = [mp.mpf(0)] * 19
        d[i] = mp.mpf(1)
        dual.append(base.Dual(str(val), d))
    result = base.graph(dual[:10], 0, biases=dual[10:])
    residual = np.array([float((result[r].value-base.target[r])/base.target[r]) for r in range(8)])
    jac = np.array([[float(v/base.target[r]) for v in result[r].deriv] for r in range(8)])
    calls += 1
    if calls % 25 == 0:
        print('evaluation', calls, 'max_relative_residual', max(abs(residual)),
              'elapsed', round(time.monotonic()-t0,1), flush=True)
    cache_x, cache_value = np.array(x), (residual, jac)
    return cache_value


answer = least_squares(lambda x:evaluate(x)[0], start, jac=lambda x:evaluate(x)[1],
                       bounds=([1e-14]*10+[0]*9,[10]*10+[1-1e-12]*9),
                       x_scale='jac',ftol=1e-14,xtol=1e-14,gtol=1e-14,max_nfev=600)
res, jac = evaluate(answer.x)
record = {'status':'ordinary numerical exploration; not a new theta certificate',
          'source':base.STAR,'target_source':base.ICR,
          'optimizer_message':answer.message,'nfev':answer.nfev,'evaluations':calls,
          'max_normalized_cumulant_residual':float(max(abs(res))),
          'residual_vector':list(map(float,res)),
          'weights':list(map(float,answer.x[:10])),
          'biases':list(map(float,answer.x[10:])),
          'elapsed_seconds':time.monotonic()-t0}
Path(__file__).with_name('full-scout-result.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2),flush=True)
