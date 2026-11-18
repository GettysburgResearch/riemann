#!/usr/bin/env python3
"""Skeptic (independent) re-implementation of the Conrey-Li witnesses and the de Branges
necessary-condition scan, using mpmath only (NUMERICAL-NONRIGOROUS high precision) and the
closed form xi'(rho) = rho(rho-1) pi^{-rho/2} Gamma(rho/2) zeta'(rho) at a zero (zeta(rho)=0),
instead of the investigator's Arb power-series derivative.  Also tests the 'mechanism' identity
-Re{xi'(rho) xi(1+rho)} = -Xi'(gamma) Im xi(3/2 + i gamma).
Usage: python3 sk_conrey_li_mpmath.py K ZEROS_TSV out.json
"""
import sys, json, time, mpmath as mp

mp.mp.dps = 40

def xi(s):
    return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)

def xi_prime_at_zero(rho):
    return rho*(rho-1)*mp.pi**(-rho/2)*mp.gamma(rho/2)*mp.zeta(rho, derivative=1)

def xi4(s):
    return (4*mp.pi)**(-s/2)*mp.gamma((s+1)/2)*(mp.zeta(s, mp.mpf(1)/4)-mp.zeta(s, mp.mpf(3)/4))

def main():
    K = int(sys.argv[1]); path = sys.argv[2]; out = sys.argv[3]
    t0 = time.time()
    R = {"mpmath": mp.__version__, "dps": mp.mp.dps, "K": K}
    # 34th zero witness, recomputed from mpmath's own zetazero (independent of the TSV / flint)
    r34 = mp.zetazero(34)
    q = -mp.re(xi_prime_at_zero(r34)*xi(1+r34))
    R["CL_3.2"] = mp.nstr(q, 20)
    R["CL_3.4"] = mp.nstr(mp.re(xi(mp.mpc(1, 282))/xi(mp.mpc(2, 282))), 20)
    # chi_4 zero: refine with findroot from the C-L printed value
    L4 = lambda s: mp.zeta(s, mp.mpf(1)/4)-mp.zeta(s, mp.mpf(3)/4)
    r4 = mp.findroot(L4, mp.mpc("0.5", "67.6369208635460683980549"))
    d4 = mp.diff(xi4, r4)
    R["chi4_zero"] = mp.nstr(r4, 30)
    R["CL_chi4_3.7"] = mp.nstr(-mp.re(d4*xi4(1+r4)), 20)
    R["CL_chi4_3.8"] = mp.nstr(mp.re(xi4(mp.mpc(1, "8714.2"))/xi4(mp.mpc(2, "8714.2"))), 20)
    # scan
    neg = []; minrel = mp.inf; mech_bad = 0
    with open(path) as f:
        for line in f:
            n, mid, rad = line.split()[:3]
            n = int(n)
            if n > K: break
            g = mp.mpf(mid); rho = mp.mpc(0.5, g)
            a = xi_prime_at_zero(rho); b = xi(1+rho)
            p = a*b; val = -mp.re(p)
            minrel = min(minrel, abs(val)/abs(p))
            if val < 0: neg.append(n)
            # mechanism: Xi'(gamma) = i xi'(rho) must be real; -Xi' Im xi(3/2+i g) must equal val
            Xp = 1j*a
            mech = -mp.re(Xp)*mp.im(xi(mp.mpc(1.5, g)))
            if abs(mp.im(Xp)) > 1e-25*abs(Xp) or abs(mech-val) > 1e-20*abs(p):
                mech_bad += 1
    R["scan"] = {"num_negative": len(neg), "first": neg[:12], "min_|Re|/|prod|": mp.nstr(minrel, 5),
                 "mechanism_identity_failures": mech_bad}
    # Thm-2 grid
    gn = []
    t = mp.mpf(1)
    while t <= 1000:
        if mp.re(xi(mp.mpc(1, t))/xi(mp.mpc(2, t))) < 0: gn.append(float(t))
        t += mp.mpf(1)/4
    R["thm2_grid_neg"] = gn
    R["runtime_s"] = round(time.time()-t0, 1)
    json.dump(R, open(out, "w"), indent=1)
    print(json.dumps(R, indent=1))

main()
