import subprocess, sys, time
for label, n in [('t~1e14', 467888702914984), ('t~1e15', 5045354828589536), ('t~1e16', 54171670468359120)]:
    for prec in (128, 192):
        code = ('import time\nfrom platt_ctypes import platt_zeros\n'
                't0=time.time()\n'
                'got, balls = platt_zeros(%d, 100, %d)\n'
                'dt=time.time()-t0\n'
                'print("%s prec=%d -> %%3d isolated [%%.1f s%%s]" %% (got, dt, (", %%.3f s/zero"%%(dt/got)) if got else ""), flush=True)\n'
                'if got: print("   first:", balls[0][:50], flush=True)\n') % (n, prec, label, prec)
        r = subprocess.run([sys.executable,'-u','-c',code], capture_output=True, text=True, timeout=3000, cwd='/home/user/riemann/experiments/X-5604-exact-slab-discrepancy')
        print(r.stdout.strip() if r.stdout.strip() else '%s prec=%d rc=%d %s' % (label, prec, r.returncode, (r.stderr or '')[-150:]), flush=True)
        if 'isolated' in r.stdout and ' 0 isolated' not in r.stdout:
            break
