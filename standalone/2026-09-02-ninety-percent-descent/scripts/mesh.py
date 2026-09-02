# Reverse-Rolle descent efficiency: for K in KS, find the real zeros c_j of Xi^{(K)} in a height window,
# compute residue signs rho_j = Xi(c_j)/Xi^{(K+1)}(c_j), and count how many consecutive same-sign pairs
# (each certifies a real zero of Xi between c_j and c_{j+1}).  Local Taylor expansions of Xi(t)=xi(1/2+it)
# are obtained from Cauchy circles (trapezoid rule, spectrally accurate) at high precision.
import mpmath as mp, sys, json, time
mp.mp.dps = int(sys.argv[4]) if len(sys.argv) > 4 else 80
T0 = mp.mpf(sys.argv[1]); T1 = mp.mpf(sys.argv[2]); KS = [int(k) for k in sys.argv[3].split(',')]
N = 192; KMAX = 72; r = mp.mpf('1.0'); half = mp.mpf('0.62'); step = mp.mpf('1.2')
def xi(s): return mp.mpf('0.5')*s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)
def taylor_at(t):
    # c_k = (1/N) sum_j Xi(t + r e^{i phi_j}) e^{-i k phi_j} / r^k  -> Taylor coefficients of Xi(t+z)
    vals = []
    for j in range(N):
        phi = 2*mp.pi*j/N
        z = r*mp.expj(phi)
        vals.append(xi(mp.mpf('0.5') + 1j*(t+z)))
    cs = []
    for k in range(KMAX+1):
        s = mp.mpc(0)
        for j in range(N):
            s += vals[j]*mp.expj(-2*mp.pi*j*k/N)
        cs.append((s/N)/r**k)
    return [c.real for c in cs]   # Xi(t+z) is real for real z; imaginary parts are roundoff
def deriv_poly(cs, K):
    # coefficients of Xi^{(K)}(t+z) = sum_{k>=K} c_k k!/(k-K)! z^{k-K}
    return [cs[k]*mp.factorial(k)/mp.factorial(k-K) for k in range(K, KMAX+1)]
def peval(p, z):
    s = mp.mpf(0)
    for a in reversed(p): s = s*z + a
    return s
def zeros_in(p, lo, hi, ngrid=400):
    zs = []; xs = [lo + (hi-lo)*i/ngrid for i in range(ngrid+1)]; vs = [peval(p, x) for x in xs]
    for i in range(ngrid):
        if vs[i] == 0: zs.append(xs[i])
        elif vs[i]*vs[i+1] < 0:
            a, b = xs[i], xs[i+1]; fa = vs[i]
            for _ in range(60):
                m = (a+b)/2; fm = peval(p, m)
                if fa*fm <= 0: b = m
                else: a = m; fa = fm
            zs.append((a+b)/2)
    return zs
t0 = time.time()
centers = []; t = T0 + half
while t - half < T1:
    centers.append(t); t += step
results = {K: [] for K in KS}; zeros0 = []; grams = []
for tc in centers:
    cs = taylor_at(tc)
    for K in KS:
        pK = deriv_poly(cs, K); pK1 = deriv_poly(cs, K+1); p0 = deriv_poly(cs, 0)
        lo, hi = -half, half
        for z in zeros_in(pK, lo, hi):
            c = tc + z
            if any(abs(c - prev[0]) < mp.mpf('1e-9') for prev in results[K][-3:]): continue
            rho = peval(p0, z)/peval(pK1, z)
            results[K].append((c, rho))
    p0 = deriv_poly(cs, 0)
    for z in zeros_in(p0, -half, half):
        c = tc + z
        if not any(abs(c - prev) < mp.mpf('1e-9') for prev in zeros0[-3:]): zeros0.append(c)
    print("window centre %s done, %.0fs" % (mp.nstr(tc, 8), time.time()-t0), flush=True)
# Gram points in range and the sign of Xi there
def theta(t): return mp.siegeltheta(t)
n = int(mp.ceil(theta(T0)/mp.pi)); x0 = T0
while True:
    g = mp.findroot(lambda x: theta(x) - n*mp.pi, x0)
    if g > T1: break
    if g >= T0: grams.append((g, mp.sign(xi(mp.mpf('0.5')+1j*g).real)))
    n += 1; x0 = g + 2*mp.pi/mp.log(g/(2*mp.pi))
out = {'T0': float(T0), 'T1': float(T1), 'zeros_of_Xi': [float(z) for z in zeros0], 'gram': [(float(g), int(s)) for g, s in grams]}
print("\n=== window [%s, %s]: %d zeros of Xi; %d Gram points" % (mp.nstr(T0,6), mp.nstr(T1,6), len(zeros0), len(grams)))
if len(grams) > 1:
    alt = sum(1 for i in range(len(grams)-1) if grams[i][1]*grams[i+1][1] < 0)
    print("Gram mesh: sign changes of Xi between consecutive Gram points: %d of %d intervals (%.1f%%)" % (alt, len(grams)-1, 100*alt/(len(grams)-1)))
    out['gram_sign_changes'] = alt
for K in KS:
    R = results[K]; R.sort(key=lambda x: x[0])
    M = len(R); Up = sum(1 for c, rho in R if rho > 0); Um = M - Up
    V = sum(1 for i in range(M-1) if R[i][1]*R[i+1][1] < 0)
    inside = sum(1 for z in zeros0 if R[0][0] <= z <= R[-1][0]) if M else 0
    lt = mp.log(mp.mpf(T0)/(2*mp.pi)); phi = mp.pi/2 + mp.atan(mp.pi/(2*lt)); kphi = mp.fmod(K*phi, mp.pi)
    print("K=%2d: mesh M=%d  U+=%d U-=%d  min/M=%.3f  same-sign edges=%d of %d (%.1f%%)  true zeros of Xi inside mesh span=%d  ratio detected/true=%.3f  K*phi mod pi=%.3f" %
          (K, M, Up, Um, min(Up,Um)/M if M else 0, M-1-V, M-1, 100*(M-1-V)/(M-1) if M > 1 else 0, inside, (M-1-V)/inside if inside else 0, float(kphi)))
    out[str(K)] = {'mesh': [(float(c), float(mp.sign(rho))) for c, rho in R], 'M': M, 'Up': Up, 'Um': Um, 'V': V, 'true_inside': inside}
json.dump(out, open('mesh_%s_%s.json' % (sys.argv[1], sys.argv[2]), 'w'))
print("total %.0fs" % (time.time()-t0))
