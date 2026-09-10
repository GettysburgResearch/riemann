# Descent efficiency of a shifted Gram mesh (fast version): mesh points theta(t_j) = delta + j*pi found by
# float Newton on the Riemann-Siegel theta asymptotic; signs of Z from mpmath.siegelz.
import mpmath as mp, sys, math
mp.mp.dps = 15
T0 = float(sys.argv[1]); NMESH = int(sys.argv[2]); NOFF = int(sys.argv[3])
def theta(t):  return t/2*math.log(t/(2*math.pi)) - t/2 - math.pi/8 + 1/(48*t) + 7/(5760*t**3)
def thetap(t): return 0.5*math.log(t/(2*math.pi)) - 1/(48*t*t)
def mesh(delta):
    pts = []; n = math.ceil((theta(T0) - delta)/math.pi); x = T0
    for j in range(NMESH):
        target = delta + (n+j)*math.pi
        for _ in range(30):
            dx = (theta(x) - target)/thetap(x); x -= dx
            if abs(dx) < 1e-11: break
        pts.append(x); x = x + math.pi/thetap(x)
    return pts
# sanity: compare asymptotic theta with mpmath at T0
print("T0=%g: theta asymptotic %.10f vs mpmath %.10f" % (T0, theta(T0), float(mp.siegeltheta(T0))))
print("mesh points per offset: %d; delta = mesh phase (theta mod pi); delta=0 Gram points; delta=1/2 zeros of the leading RS term" % NMESH)
print("%9s %8s %8s %9s" % ("delta/pi", "eff", "V/M", "minU/(M+1)"))
for k in range(NOFF):
    delta = k*math.pi/NOFF
    pts = mesh(delta)
    signs = [1 if mp.siegelz(x) > 0 else -1 for x in pts]
    M = len(pts) - 1
    changes = sum(1 for i in range(M) if signs[i] != signs[i+1])
    r = 1; Up = 1
    for i in range(M):
        if signs[i] == signs[i+1]: r = -r
        if r > 0: Up += 1
    Um = (M+1) - Up
    print("%9.4f %8.3f %8.3f %9.3f" % (delta/math.pi, changes/M, (M-changes)/M, min(Up,Um)/(M+1)), flush=True)
