import time, sys
from flint import arb, ctx
ctx.prec = 192
for e in [13,14,15,16,17,18,20,22]:
    t = arb(10)**e
    t0=time.time()
    try:
        r = t.zeta_nzeros(); n = r.unique_fmpz()
        print("t=1e%-3d  N = %-24s  [%.1f s]" % (e, n, time.time()-t0), flush=True)
    except Exception as ex:
        print("t=1e%-3d  FAILED %s: %s  [%.1f s]" % (e, type(ex).__name__, ex, time.time()-t0), flush=True)
        break
    if time.time()-t0 > 900: print("  (stopping: too slow)"); break
