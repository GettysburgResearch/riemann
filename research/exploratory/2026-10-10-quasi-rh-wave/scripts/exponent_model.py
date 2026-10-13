#!/usr/bin/env python3
"""
Exponent-comparison model for the cubic-theta "common signal" argument
(OpenAI QRH manuscript 30 Sep 2026, Secs 15-20; Liu arXiv:2610.12234 Parts II-III).

All quantities are logarithmic exponents in base Z.  Balanced geometry:
    lx=(1-b-l)/2, ly=(1+b-l)/2, h=1-lx+l=(1+b+3l)/2, M=lx+ly=1-l.
Signal exponent C(s) = s - 5/6 + lx/3 + l/6  (= s-(4+b)/6 balanced).
Direct (low) bound  Llow = lx/2 + max(0, theta*b, b-ly/2) + k(M,l)/2,
    k(M,l) = max(0,(1+3l-2M)/4, M+l-1, (3l-1)/2)      [Liu Lemma 22.1, Prop 22.2]
Comparison boundary  Blow = Llow + 5/6 - lx/3 - l/6   (= 11/12 - l/4 + b(theta-1/12) + penalties).

Nonprincipal row U=Z^d, class delta=2a-1, amplitude ratio x=gbar/delta, count exponent R:
    E0(d) = a + h(z0-1/6) - a*ly - l/2 + x*delta*l + d*(R + delta/2 - z0);  need B >= E0(d).  [(18.4),(20.4)]
Counts (Prop 19.2 / Liu Prop 18.1, Sec 23): detector t in [1,3/2], r in [t-1/2,1], m=t-r<=1/2,
    FI(r) = r + 2x*min(cM(1-r), zsup)       (inverse moment, Lemma 17.1: r+2z<=1 -> cM=1/2)
    FS(r) = 2m + 2x*min(ck(1-2m), zsup)     (plain 4th moment, Lemma 18.1: 2m+6*kappa*z<=1 -> ck=1/(6kappa)=2/9)
    Rshort(t) = 1 - delta*min_r max(FI,FS);  Rlong(t) = 1-alpha+(alpha-delta)t  (Lemma 17.6, alpha=5/6)
    R*(delta,x) = min_t max(Rshort,Rlong).   Uncapped closed form (Liu 18.2) used as a check.
Side constraints: floor class (a0=51/100, R=1), intermediate rows (d=1/2, R=76/75-2delta/3),
    small rows ly/2 - h(z0-1/6) - 2dmin > 0, supply l/h > 7/37, lx>l, ly>l, b>0, 1-3l>0.
"""
import numpy as np
from scipy.optimize import minimize
import json

DEFAULT = dict(alpha=5/6, ck=2/9, cM=1/2, theta=1/12, z0=17/50, a0=51/100, supply=7/37,
               dmin=1/100, use_cap=True, reflected=True)

NT = 101; T = np.linspace(1.0, 1.5, NT)

def geom(b, l):
    lx = (1 - b - l) / 2; ly = (1 + b - l) / 2; return lx, ly, 1 - lx + l

def Blow(b, l, P):
    lx, ly, h = geom(b, l); M = lx + ly
    gram = max(0.0, P['theta'] * b, (b - ly / 2) if P['reflected'] else 0.0)
    k = max(0.0, (1 + 3 * l - 2 * M) / 4, M + l - 1, (3 * l - 1) / 2) if P['reflected'] else 0.0
    return lx / 2 + gram + k / 2 + 5 / 6 - lx / 3 - l / 6

# ---------------------------------------------------------------- vectorised counts
def Fshort(x, t, P, zsup):
    """min over r in [max(t-1/2,1/2),1] of max(FI,FS); x,t broadcastable arrays."""
    cM, ck = P['cM'], P['ck']; cap = zsup if P['use_cap'] else 1e9
    x = np.asarray(x, float); t = np.asarray(t, float)
    rlo = np.maximum(t - 0.5, 0.5); rhi = np.ones_like(t)
    # affine pieces: FI = min(A1,A2), FS = min(S1,S2) with
    # A1 = 2x cM + (1-2x cM) r ; A2 = r + 2x cap
    # S1 = 2x ck + (2-4x ck)(t-r) ; S2 = 2(t-r) + 2x cap
    def FI(r): return np.minimum(2*x*cM + (1-2*x*cM)*r, r + 2*x*cap)
    def FS(r): m = t - r; return np.minimum(2*x*ck + (2-4*x*ck)*m, 2*m + 2*x*cap)
    cands = [rlo, rhi]
    # breakpoints of FI: A1=A2 -> r = 1 - cap/cM ; of FS: S1=S2 -> m = (1-cap/ck)/2 -> r = t - (1-cap/ck)/2
    cands.append(np.broadcast_to(1 - cap / cM, np.broadcast(x, t).shape))
    cands.append(t - (1 - cap / ck) / 2 + 0 * x)
    # crossings of each FI piece with each FS piece (affine in r): a0+a1 r = s0 + s1 (t-r)
    A = [(2*x*cM, 1-2*x*cM), (2*x*cap + 0*t, 1 + 0*x)]
    S = [(2*x*ck, 2-4*x*ck), (2*x*cap + 0*t, 2 + 0*x)]
    for a0, a1 in A:
        for s0, s1 in S:
            den = a1 + s1
            r = (s0 + s1 * t - a0) / np.where(np.abs(den) < 1e-15, 1e-15, den)
            cands.append(r + 0 * x + 0 * t)
    best = None
    for r in cands:
        r = np.clip(np.broadcast_to(r, np.broadcast(x, t).shape), rlo, rhi)
        v = np.maximum(FI(r), FS(r))
        best = v if best is None else np.minimum(best, v)
    return best

def Rstar_grid(delta, x, P, zsup):
    """delta: (nd,), x: (nx,) -> R*(delta,x) array (nd,nx) with t optimised on grid + linear refinement."""
    d = delta[:, None, None]; xx = x[None, :, None]; tt = T[None, None, :]
    Fs = Fshort(xx, tt, P, zsup)                    # (1,nx,nt) -> broadcast
    Rs = 1 - d * Fs                                  # (nd,nx,nt)
    # long witness r in [1,t]: count 1-alpha+(alpha-delta) r; worst r = t if alpha>=delta else r = 1
    Rl = 1 - P['alpha'] + (P['alpha'] - d) * np.where(P['alpha'] >= d, tt, 1.0)      # (nd,1,nt)
    diff = Rs - Rl
    # find first t where diff <= 0 ; Rs piecewise linear non-increasing, Rl increasing
    neg = diff <= 0
    idx = np.argmax(neg, axis=2)                     # first index with diff<=0 (0 if none/at start)
    none = ~neg.any(axis=2)
    R = np.empty((len(delta), len(x)))
    # cases
    i0 = idx == 0
    R[i0] = np.maximum(Rs[..., 0], np.broadcast_to(Rl[..., 0], Rs[..., 0].shape))[i0]
    R[none] = np.maximum(Rs[..., -1], np.broadcast_to(Rl[..., -1], Rs[..., -1].shape))[none]
    mid = (~i0) & (~none)
    ii = np.where(mid)
    k = idx[ii]
    d1 = diff[ii[0], ii[1], k - 1]; d2 = diff[ii[0], ii[1], k]
    w = d1 / (d1 - d2)
    t_star = T[k - 1] + w * (T[k] - T[k - 1])
    R[mid] = 1 - P['alpha'] + (P['alpha'] - delta[ii[0]]) * np.where(P['alpha'] >= delta[ii[0]], t_star, 1.0)
    # delta = alpha endpoint: R = 1 - alpha
    R[np.abs(delta - P['alpha']) < 1e-12, :] = 1 - P['alpha']
    return R

def Rstar_closed(delta, x, alpha=5/6):
    Dx = 3 - 17*x/9; Px = (2 - 8*x/9)*(1 - x); J = (alpha - delta)*Dx + delta*Px
    return 1 - delta + (alpha - delta)*delta*Px/(2*J)

# ---------------------------------------------------------------- exponents / constraints
def E0(delta, x, b, l, d, R, P):
    lx, ly, h = geom(b, l); a = (1 + delta) / 2; z0 = P['z0']
    return a + h*(z0 - 1/6) - a*ly - l/2 + x*delta*l + d*(R + delta/2 - z0)

ND, NX = 81, 41
def Hmod(b, l, P, delta_lo=None):
    lx, ly, h = geom(b, l); zsup = l / h
    d0 = (2*P['a0'] - 1) if delta_lo is None else delta_lo
    delta = np.linspace(d0, P['alpha'], ND); x = np.linspace(0, .5, NX)
    R = Rstar_grid(delta, x, P, zsup)
    E = E0(delta[:, None], x[None, :], b, l, h, R, P)
    i, j = np.unravel_index(np.argmax(E), E.shape)
    # local refinement around (delta_i, x_j)
    dlo, dhi = delta[max(i-1, 0)], delta[min(i+1, ND-1)]; xlo, xhi = x[max(j-1, 0)], x[min(j+1, NX-1)]
    dd = np.linspace(dlo, dhi, 41); xx = np.linspace(xlo, xhi, 41)
    R2 = Rstar_grid(dd, xx, P, zsup); E2 = E0(dd[:, None], xx[None, :], b, l, h, R2, P)
    i2, j2 = np.unravel_index(np.argmax(E2), E2.shape)
    return float(E2[i2, j2]), (float(dd[i2]), float(xx[j2]))

def Hfloor(b, l, P):
    lx, ly, h = geom(b, l); return E0(2*P['a0'] - 1, 0.5, b, l, h, 1.0, P)

def Hint(b, l, P):
    f = lambda dl: E0(dl, 0.5, b, l, 0.5, 76/75 - 2*dl/3, P)
    return max(f(2*P['a0'] - 1), f(P['alpha']))

def feasible(b, l, P):
    lx, ly, h = geom(b, l)
    c = dict(b_pos=b > 0, lx_gt_l=lx > l, ly_gt_l=ly > l, one_minus_3l=1 - 3*l > 0,
             supply=l/h > P['supply'], small_rows=ly/2 - h*(P['z0'] - 1/6) - 2*P['dmin'] > 0)
    return all(c.values()), c

def Bachievable(b, l, P, detail=False):
    ok, c = feasible(b, l, P)
    if not ok:
        return (np.inf, dict(infeasible=[k for k, v in c.items() if not v])) if detail else np.inf
    bl = Blow(b, l, P); hm, cls = Hmod(b, l, P); hf = Hfloor(b, l, P); hi = Hint(b, l, P)
    parts = dict(Blow=bl, Hmod=hm, Hfloor=hf, Hint=hi); B = max(parts.values())
    if detail:
        d = dict(parts); d['Hmod_class'] = cls; d['active'] = [k for k, v in parts.items() if v > B - 1e-7]
        return B, d
    return B

def optimise(P):
    best = (np.inf, None)
    for b in np.linspace(0.005, 0.4, 9):
        for l in np.linspace(0.10, 0.33, 13):
            v = Bachievable(b, l, P)
            if v < best[0]: best = (v, (b, l))
    r = minimize(lambda p: Bachievable(p[0], p[1], P), best[1], method='Nelder-Mead',
                 options=dict(xatol=1e-8, fatol=1e-11, maxiter=600))
    B, det = Bachievable(r.x[0], r.x[1], P, detail=True)
    return B, float(r.x[0]), float(r.x[1]), det

# ---------------------------------------------------------------- checks
def check_certificate():
    P = dict(DEFAULT); b, l = 1/8, 1/6; lx, ly, h = geom(b, l)
    delta = np.linspace(0, 5/6, 301); x = np.linspace(0, .5, 76)
    Rc = Rstar_closed(delta[:, None], x[None, :]); Rn = Rstar_grid(delta, x, P, l/h)
    Ec = E0(delta[:, None], x[None, :], b, l, h, Rc, P) - 7/8
    i, j = np.unravel_index(np.argmax(Ec), Ec.shape)
    print(f"[check i] b=1/8 l=1/6: lx={lx:.6f} ly={ly:.6f} h={h:.6f} Blow={Blow(b,l,P):.6f} (7/8)")
    print(f"   min(-E*) closed-form R* on [0,5/6]x[0,1/2] = {-Ec[i,j]:.6e}  target 49/440640={49/440640:.6e}  at delta={delta[i]:.4f}, x={x[j]:.4f}")
    print(f"   max|R*_closed - R*_numeric(capped, t-grid)| = {np.max(np.abs(Rc-Rn)):.2e}")
    print(f"   floor E(h)={Hfloor(b,l,P)-7/8:+.6f} (paper -7/1200={-7/1200:+.6f}); intermediate E(1/2)={Hint(b,l,P)-7/8:+.6f} (paper <= -49/14400={-49/14400:+.6f})")
    print(f"   small-row margin={ly/2-h*(17/50-1/6)-2/100:.6f} (paper 63/800={63/800:.6f}); supply l/h={l/h:.5f} > 7/37={7/37:.5f}")
    B, det = Bachievable(b, l, P, detail=True)
    print(f"   model B at (1/8,1/6) = {B:.9f}; parts={ {k:(round(v,7) if isinstance(v,float) else v) for k,v in det.items()} }")

def check_liu():
    P = dict(DEFAULT); r9 = np.sqrt(921)
    dc = (49 - r9)/48; lnew = (33 + 8*r9)/1653; bnew = -4/29 + 230*r9/26709; Bnew = (1507 - 2*r9)/1653
    print(f"[check ii] Liu: delta_c={dc:.9f} l_new={lnew:.9f} b_new={bnew:.9f} B_new={Bnew:.12f}; R*(dc,1/2)={Rstar_closed(dc,.5):.9f} (=2/3)")
    B, det = Bachievable(bnew, lnew, P, detail=True)
    print(f"   model at (b_new,l_new): B={B:.12f} parts={ {k:(round(v,9) if isinstance(v,float) else v) for k,v in det.items()} }")
    Bo, bo, lo, deto = optimise(P)
    print(f"   model optimum: B={Bo:.12f} at b={bo:.9f} l={lo:.9f}; active={deto['active']}; tight class={deto['Hmod_class']}; B_opt-B_new={Bo-Bnew:+.2e}")
    return Bo, bo, lo, deto

def sensitivity(B0):
    base = dict(DEFAULT)
    dials = [('alpha (amplification slope)', 'alpha', 5/6, [1.0, 2/3, 1/2, 0.0]),
             ('ck=1/(6kappa) (plain capacity)', 'ck', 2/9, [1/(6*0.7), 1/3, 1.0]),
             ('cM (inverse capacity)', 'cM', 1/2, [0.75, 1.0]),
             ('theta (Gram loss, b/12)', 'theta', 1/12, [1/24, 0.0]),
             ('z0 (Mellin real part)', 'z0', 17/50, [0.30, 0.25]),
             ('a0 (detector floor)', 'a0', 51/100, [0.505, 0.5]),
             ('supply (7/37)', 'supply', 7/37, [0.15, 0.10])]
    print("\n[sensitivity]  base B0=%.9f" % B0)
    print("%-34s %9s %9s %13s %11s %-22s %s" % ("dial", "current", "hypoth.", "B(hyp)", "dB/ddial", "active", "tight class (delta,x); b,l"))
    out = []
    for name, key, cur, hyps in dials:
        eps = 2e-3 * max(abs(cur), 0.1)
        Pp = dict(base); Pp[key] = cur + eps; Pm = dict(base); Pm[key] = cur - eps
        der = (optimise(Pp)[0] - optimise(Pm)[0]) / (2*eps)
        for hyp in hyps:
            Ph = dict(base); Ph[key] = hyp
            Bh, bh, lh, dh = optimise(Ph)
            print("%-34s %9.5f %9.5f %13.9f %+11.5f %-22s %s; b=%.4f l=%.4f" % (name, cur, hyp, Bh, der, ",".join(dh['active']), np.round(dh['Hmod_class'], 4), bh, lh))
            out.append((name, cur, hyp, Bh, der, dh['active'], dh['Hmod_class'], bh, lh))
    return out

def best_conceivable():
    print("\n[best conceivable]")
    for lab, upd in [("alpha=0 only (Lindelof-on-average inverse)", dict(alpha=0.0)),
                     ("cM=1, ck=1 only", dict(cM=1.0, ck=1.0)),
                     ("alpha=0, cM=1, ck=1", dict(alpha=0.0, cM=1.0, ck=1.0)),
                     ("alpha=0, cM=1, ck=1, a0=1/2", dict(alpha=0.0, cM=1.0, ck=1.0, a0=0.5)),
                     ("alpha=0, cM=1, ck=1, a0=1/2, supply=0", dict(alpha=0.0, cM=1.0, ck=1.0, a0=0.5, supply=0.0)),
                     ("theta=0 only", dict(theta=0.0)),
                     ("theta=0, alpha=0, cM=1, ck=1", dict(alpha=0.0, cM=1.0, ck=1.0, theta=0.0)),
                     ("theta=0, alpha=0, cM=1, ck=1, a0=1/2", dict(alpha=0.0, cM=1.0, ck=1.0, theta=0.0, a0=0.5)),
                     ("... + supply=0", dict(alpha=0.0, cM=1.0, ck=1.0, theta=0.0, a0=0.5, supply=0.0)),
                     ("... + no reflected/Gram-2nd penalty", dict(alpha=0.0, cM=1.0, ck=1.0, theta=0.0, a0=0.5, supply=0.0, reflected=False))]:
        P = dict(DEFAULT); P.update(upd)
        B, b, l, det = optimise(P)
        print(f"   {lab:42s}: B={B:.9f} at b={b:.5f} l={l:.5f} active={det['active']} class={np.round(det['Hmod_class'],4)} Blow={det['Blow']:.5f} Hfloor={det['Hfloor']:.5f} Hmod={det['Hmod']:.5f} Hint={det['Hint']:.5f}")

def three_quarters():
    print("\n[3/4] B(l)=11/12-l/4 hits 3/4 at l=2/3. Obstructions along l (b=0.001):")
    P = dict(DEFAULT)
    for l in [1/6, 0.2, 0.25, 1/3, 0.5, 2/3]:
        b = 1e-3; lx, ly, h = geom(b, l)
        print(f"   l={l:.4f}: B(l)={11/12-l/4:.4f} Blow(refl.pen.)={Blow(b,l,P):.4f} floor E0-B(l)={Hfloor(b,l,P)-(11/12-l/4):+.4f} lx-l={lx-l:+.4f} l/h={l/h:.4f} l<=lx/2+b/12? {l<=lx/2+b/12}")
    print("   Floor identity (balanced, delta->0, R=1): raw floor-row exponent = l, signal = lx/2+b/12 = C_b(B)")
    print("   => l <= 1/4 - b/6 - l/4  <=>  l <= 1/5 - 2b/15  =>  B = 11/12 - l/4 >= 13/15 + b/30 = 0.8667 + b/30.")

if __name__ == '__main__':
    import time, sys; t0 = time.time()
    part = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if part in ('check', 'all'):
        check_certificate(); Bo, bo, lo, deto = check_liu(); print(f"[time {time.time()-t0:.1f}s]")
    if part in ('sens', 'all'):
        rows = sensitivity(0.874957); print(f"[time {time.time()-t0:.1f}s]")
    if part in ('best', 'all'):
        best_conceivable(); three_quarters(); print(f"[time {time.time()-t0:.1f}s]")
    if part == 'time':
        P = dict(DEFAULT); t1 = time.time(); B = Bachievable(0.12, 0.167, P, detail=True); print(B, time.time()-t1)
