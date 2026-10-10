# Corrected cost/benefit of note M's "mollified first moment on the floor rows".
# Floor contour moved to Re x = a0 + eta (x only; w stays on 1-a0-6e, so cost is Z^eta, coefficient 1),
# mollifier length U^r, off-diagonal saving U^{-f}.  Floor sum = (all rows) - (non-floor rows);
# the non-floor rows of class delta re-enter with |M_r| ~ U^{r((delta-delta0)/2 - eta)_+}.
import numpy as np
a0, d0, z0, alpha = 51/100, 1/50, 17/50, 5/6

def geom(b, l):
    return (1-b-l)/2, (1+b-l)/2, (1+b+3*l)/2            # lx, ly, h

def Rstar(delta, x):                                     # Liu/paper count, closed form (note A)
    Dx = 3 - 17*x/9; Px = (2 - 8*x/9)*(1 - x); J = (alpha-delta)*Dx + delta*Px
    return 1 - delta + (alpha-delta)*delta*Px/(2*J)

def E_bin(b, l, delta, x, ideal):                        # (20.4) at d=h: paper's bin exponent, class delta
    lx, ly, h = geom(b, l); C0 = -1/4 + 5*l/4 + b/6
    R = 1 - delta if ideal else Rstar(delta, x)
    return C0 + delta*(1/2 + l) + x*delta*l - h*(1 - R)

def floor_proposal(b, l, r, eta, f, ideal, pl_numerator=True):
    lx, ly, h = geom(b, l); C0 = -1/4 + 5*l/4 + b/6
    E_floor = C0 + 3*d0/4                                 # (20.5)
    main  = E_floor + eta - f*h                           # off-diagonal of the mollified moment
    trunc = E_floor + eta - r*eta*h                       # truncation error, bounded row by row
    ds = np.linspace(d0, alpha, 120); xs = np.linspace(0, .5, 11)
    D, X = np.meshgrid(ds, xs, indexing='ij')
    Ebin = E_bin(b, l, D, X, ideal)
    numer = -h*(D-d0)/4 if pl_numerator else 0.0         # U^{(delta+delta0)/4} vs crude U^{delta/2}
    Delta = -(D-d0)*(1-ly)/2 + eta + numer + h*r*np.maximum((D-d0)/2 - eta, 0)
    nonfloor = (Ebin + Delta).max()
    new = max(main, trunc, nonfloor)
    return E_floor, new, dict(main=main, trunc=trunc, nonfloor=nonfloor, binmax=Ebin.max())

def best_gain(b, l, f, ideal, pl=True):
    best = (-1, None)
    for r in np.linspace(0.5, 2.0, 31):
        for eta in np.linspace(0.0, 0.45, 46):
            E0, new, parts = floor_proposal(b, l, r, eta, f, ideal, pl)
            g = E0 - new
            if g > best[0]: best = (g, (r, eta, parts))
    return best

for label, (b, l) in [("paper (1/8,1/6)", (1/8, 1/6)), ("Liu (0.1232,0.166838)", (0.1232, 0.166838))]:
    lx, ly, h = geom(b, l)
    print(f"\n=== {label}: lx={lx:.4f} ly={ly:.4f} h={h:.4f}  1/h={1/h:.4f}  a-coef in (10.15) at d=h = 1-ly+h = {1-ly+h:.4f}")
    print(f"    non-floor subtraction slope per unit (delta-delta0): rh/2-(1-ly)/2-h/4 = {h/2:.4f} r - {(1-ly)/2+h/4:.4f}; zero at r={((1-ly)/2+h/4)/(h/2):.4f}")
    E0 = floor_proposal(b, l, 1, 0, 0, False)[0]
    print(f"    floor exponent (20.5): {E0:.5f}; paper's worst bin: {E_bin(b,l,np.linspace(d0,alpha,120)[:,None],np.linspace(0,.5,11)[None,:],False).max():.2e}")
    # r <= 1: sign of the net change for every eta
    for r in [0.5, 1.0, 1/h - 1e-9]:
        worst = min(floor_proposal(b, l, r, eta, 10.0, True)[1] - E0 for eta in np.linspace(0.001, .4, 100))
        print(f"    r={r:.3f}: min over eta of (new-old) even with f=infinity: {worst:+.4f}  (>0 means the proposal loses)")
    for ideal in [False, True]:
        for pl in [True, False]:
            print(f"  counts={'ideal' if ideal else 'paper'}, numerator={'PL-interp' if pl else 'crude U^(delta/2)'}:")
            for f in [0.05, 0.13, 0.2, 0.3, 0.5]:
                g, (r, eta, parts) = best_gain(b, l, f, ideal, pl)
                print(f"    f={f:.2f}: best gain in floor exponent {g:+.4f} at r={r:.2f}, eta={eta:.3f}; "
                      f"pieces main={parts['main']-E0:+.4f} trunc={parts['trunc']-E0:+.4f} nonfloor={parts['nonfloor']-E0:+.4f}  (dB ~ -0.26*gain = {-0.26*max(g,0):+.4f})")
