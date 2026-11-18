#!/usr/bin/env python3
"""Skeptic: check the identity -Re{xi'(rho) xi(1+rho)} = -Xi'(gamma) Im xi(3/2+i gamma) and the alternation of
sign Xi'(gamma_n), n <= 200, with mpmath zetazero and mp.diff (full derivative). NUMERICAL-NONRIGOROUS.
(Supersedes the 'mechanism_identity_failures' field of sk_conrey_li_K2000.json, which is a tolerance artefact:
there xi' was taken from the closed form valid only at an exact zero, with 25-digit TSV ordinates.)"""
import json, sys, mpmath as mp
mp.mp.dps = 40
def xi(s): return s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
wi = 0; wd = 0; sg = []
for n in range(1, 201):
    rho = mp.mpc(0.5, mp.zetazero(n).imag)
    a = mp.diff(xi, rho); Xp = 1j*a; b = xi(1+rho)
    wi = max(wi, abs(mp.im(Xp))/abs(Xp)); wd = max(wd, abs(-mp.re(a*b) + mp.re(Xp)*mp.im(b))/abs(a*b))
    sg.append(1 if mp.re(Xp) > 0 else -1)
res = {"n_max": 200, "max_|Im Xi'|/|Xi'|": mp.nstr(wi, 3), "max_rel_identity_residual": mp.nstr(wd, 3),
       "Xi'_signs_alternate": all(sg[i] == -sg[i+1] for i in range(len(sg)-1))}
json.dump(res, open(sys.argv[1], "w"), indent=1); print(res)
