import time
from flint import acb, ctx
ctx.prec = 128
n0 = 43124192297104          # index just below t = 1e13 + 0.5 (from our N(a))
for num in (1, 4, 16):
    t0=time.time()
    try:
        zs = acb.zeta_zeros(n0+1, num)
        dt=time.time()-t0
        print("num=%-4d  %.1f s  (%.2f s/zero)   first im = %s" %
              (num, dt, dt/num, zs[0].imag.str(18, radius=True)), flush=True)
    except Exception as e:
        print("num=%-4d FAILED %s" % (num, e), flush=True); break
