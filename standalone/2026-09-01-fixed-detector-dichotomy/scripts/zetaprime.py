# Compute zeta'(rho) at the first N zeros rho = 1/2 + i*gamma (gamma from Odlyzko's table, 9 decimals).
import mpmath as mp, sys, time
mp.mp.dps = 20
N = int(sys.argv[1]); out = sys.argv[2]
gammas = [float(l.strip()) for l in open('../zeros1.txt') if l.strip()][:N]
t0 = time.time()
with open(out, 'w') as f:
    f.write("# n gamma re_zetaprime im_zetaprime\n")
    for n, g in enumerate(gammas, 1):
        d = mp.zeta(mp.mpc(0.5, g), derivative=1)
        f.write("%d %.9f %.12e %.12e\n" % (n, g, float(d.real), float(d.imag)))
        if n % 2000 == 0:
            f.flush(); print(n, "done, %.0fs" % (time.time()-t0), flush=True)
print("finished", N, "%.0fs" % (time.time()-t0))
