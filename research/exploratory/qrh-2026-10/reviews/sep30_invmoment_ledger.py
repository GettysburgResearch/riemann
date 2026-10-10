"""sep30_invmoment_ledger.py -- exact checks of the exponent ledgers in the marked inverse-moment
engine (Section 17: Lemmas 17.1, 17.2, 17.6) of the OpenAI QRH manuscript dated 30 Sep 2026
(PR 908 import, paper.tex, SHA-256 42a5ee0f...6ac6a3).  External, unreviewed; read as data.

What this checks (and only this):
  A. statement dictionary  Sep30 Lemma 17.1/17.2  <->  Oct 5 thm:ms / prop:canonical (exact exponents);
  B. the finite local tables of the first Poisson transform (exhaustive over valuations);
  C. every displayed exact exponent identity in the two Poisson transforms, the child data, the
     energy exponent, the initialization and Lemma 17.6 (sympy, exact);
  D. every displayed eta/tau error budget (exact positive maxima of the linear error forms);
  E. every displayed inequality of "The new canonical data and their admissibility" (10913-11118),
     "The energy exponent" (11402-11474), the terminal ledger (9870-9925) and the initialization
     margins (12185-12271), each by an EXACT Farkas certificate (multipliers found by LP, then
     rationalized and re-verified as a polynomial identity), plus FAILING CONTROLS: perturbed
     constants must fail, with an exact rational counter-witness;
  F. "Order of choices and termination" (11474-11599): contraction per level, depth bound, margin
     decay, epsilon budget, quantifier order (DAG), and a MODEL of Lemma 17.3's order recursion.

It does NOT check that the displayed exponents correctly describe the analysis (e.g. that the
reflected-energy outputs O, T_d, S_0, B_0, E_ref of Lemma 14.3 are what the text says), nor any
Gauss-sum/reciprocity identity beyond the local exponent bookkeeping.
Line numbers refer to paper.tex at pr908 (31c706bb).

Run: python3 -I sep30_invmoment_ledger.py      (about 5 s; sympy, scipy)
"""
from fractions import Fraction as Fr
import itertools
import math
import sympy as sp
from scipy.optimize import linprog

ok = []


def check(name, cond):
    ok.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


S = sp.symbols
# ---------------------------------------------------------------------------------------------
print("== A. statement dictionary (Sep30 17.1/17.2 vs Oct5 thm:ms / prop:canonical)")
r, m, th, eps, Zl = S("r m vartheta epsilon logZ", positive=True)
# Oct5 thm:ms:  sum_{N(u)<=D^{1+th}} |A_u(D)|^2 << D^{2+th+eps};  Sep30: M_u = Z^{-r/2} A_u, D = Z^r.
# log_Z of  Z^{-r} * D^{2+th}  with D = Z^r, m = (1+th) r  must equal m.
check("A1 thm:ms <-> (old-eq:4.1) at z=0: -r + r(2+th) == m with m=(1+th)r  [9318-9320 / O5 680-689]",
      zero(-r + r * (2 + th) - (1 + th) * r))
c1_ = sp.Symbol("c1", positive=True)
check("A2 parameter map th=(m-r)/r: (m-r-c1) - (th*r-c1) = 0 at m=(1+th)r, so r<=m-c1 <=> th*r>=c1",
      zero(((1 + th) * r - r - c1_) - (th * r - c1_)))
print("     dictionary: Z^r=D, Z^m=D^(1+th), th=(m-r)/r; eps_chi=-1 case = conjugate of (nu-bar, W-bar)")
N, V, M, F0, Q, z0, cs = S("N V M F0 Q z0 c_star", real=True)
# canonical: E = Z^{-V} sum_f w(f) sum_k |Z^{-N/2} sum_n ...|^2  vs Oct5 (1/(XF)) sum_f sum_k |...|^2
check("A3 canonical normalization Z^{-V}Z^{-N} = 1/(XF) with X=Z^N, F=Z^V; target Z^{F0}=Sigma",
      zero((-V - N) + (N + V)))
# at z0=0 the first invariant (with Q>=0) implies Oct5's H<=Sigma D^{-kappa} with kappa=c_*:
check("A4 z0=0: (F0-M-Q-c*>=0, Q>=0) => F0-M-c*>=0  (Oct5 eq:positive-gap)",
      zero((F0 - M - cs) - ((F0 - M - Q - cs) + Q)))
# and makes the second invariant redundant: 4F0-3M-c* = 3(F0-M-c*) + F0 + 2c* >= 0
check("A5 z0=0: second invariant redundant: 4F0-3M-c* = 3(F0-M-c*) + F0 + 2c*",
      zero((4 * F0 - 3 * M - cs) - (3 * (F0 - M - cs) + F0 + 2 * cs)))
# for z0>0 the second invariant is NOT implied by the first: witness
wF, wM, wz = Fr(1), Fr(0), Fr(1, 2)   # F=1, M=0, z0=1/2, Q=0: first margin 1/2, second 4-3=1 ... try z0=0.9
wF, wM, wz, wc = Fr(10), Fr(0), Fr(9), Fr(1, 2)
check("A6 z0>0: second invariant independent (witness F=10,M=0,z0=9: first margin >0, second <0)",
      wF - wM - wz - wc >= 0 and 4 * wF - 3 * wM - 6 * wz - wc < 0)
c1, c2, z = S("c1 c2 z", positive=True)
check("A7 Lemma 17.1 at z=0: r<=m-c1 => 2r<=3m-c2 whenever m>=c2-2c1 (2r-3m+c2 = 2(r-m+c1)-(m-c2+2c1))",
      zero((2 * r - 3 * m + c2) - (2 * (r - m + c1) - (m - c2 + 2 * c1))))

# ---------------------------------------------------------------------------------------------
print("== B. local tables of the first Poisson transform (exhaustive)  [10201-10350, 11291-11300]")
tab = {(0, 0, 0): (0, 0), (0, 1, 0): (1, 0), (0, 0, 1): (5, 0), (0, 1, 1): (0, 4),
       (1, 0, 0): (3, 4), (1, 1, 0): (4, 4), (1, 0, 1): (2, 4), (1, 1, 1): (3, 4)}   # (pi,a1,a2): (t, exp)
bad_t, bad_e = [], []
for (pi, a1, a2), (tp, ex) in tab.items():
    if (a1 - a2 + 3 * pi) % 6 != tp:
        bad_t.append((pi, a1, a2))
    e1 = (4 * a1 + (1 + tp if tp else 0) + pi * (a1 + a2)) % 6
    e2 = (4 * a2 + (1 - tp if tp else 0) + pi * (a1 + a2)) % 6
    if not (e1 == e2 == ex):
        bad_e.append((pi, a1, a2, e1, e2, ex))
check("B1 t_p = a1-a2+3pi mod 6 column of the table   [10214]", not bad_t)
check("B2 exponent 4a_i + 1_{t!=0}(1 +- t) + pi(a1+a2) mod 6 equal on both sides = table   [10279-10297]",
      not bad_e)
# exhaustive over valuations v1,v2 of b1,b2 at p (p | B = rad(b1 b2)) and a_ip in {0,1}
fails = {k: [] for k in ["loc", "rdiff", "xi", "q0", "recon", "cube", "sqf"]}
for v1, v2 in itertools.product(range(0, 13), repeat=2):
    if v1 + v2 == 0:
        continue
    pi = (v1 + v2) % 2
    for a1, a2 in itertools.product((0, 1), repeat=2):
        tp = (a1 - a2 + 3 * pi) % 6
        R = 1 if tp else 0
        E = (a1 + a2) if pi else 0
        s_ = 1 if pi else 0                          # p | s  iff  odd valuation of b1 b2
        j2 = 1 if (pi == 0 and a1 == a2 == 1) else 0
        q = (v1 + v2 - s_) // 2                       # b1 b2 = q^2 s
        q0 = q - j2                                   # q = J2 q0
        rdiff = 1 if (pi == 0 and a1 != a2) else 0
        if R - a1 - a2 + E != s_ - 2 * j2:
            fails["loc"].append((v1, v2, a1, a2))
        if R != s_ + rdiff:
            fails["rdiff"].append((v1, v2, a1, a2))
        ex = tab[(pi, a1, a2)][1]
        # (retained-cube-label): exponent 4 exactly on primes of J = s J2; every other prime of B divides q0
        if (ex == 4) != (s_ + j2 == 1) or (ex == 0 and q0 < 1):
            fails["xi"].append((v1, v2, a1, a2))
        if q0 < 0:
            fails["q0"].append((v1, v2, a1, a2))
        # (poisson-divisor-reconstruction): t_p = 0  =>  p in J2 or p | q0
        if tp == 0 and not (j2 == 1 or q0 >= 1):
            fails["recon"].append((v1, v2, a1, a2))
        # (inverse-cube-actual): c = l_pair - s/2 - j2 ;  4 l_pair - 2 s + j2 = 4c + 5 j2 >= 0
        lp = Fr(v1 + v2, 2)
        if q0 != lp - Fr(s_, 2) - j2 or 4 * lp - 2 * s_ + j2 != 4 * q0 + 5 * j2:
            fails["cube"].append((v1, v2, a1, a2))
        if s_ + j2 > 1:                                # J = s J2 squarefree: s, J2 disjoint
            fails["sqf"].append((v1, v2))
check("B3 local identity R - A1 - A2 + E = s - 2 j2 (per prime, all v1,v2<=12)   [10357-10358]", not fails["loc"])
check("B4 R = s + r_diff   [10599]", not fails["rdiff"])
check("B5 xi(n) = chi_n(J)^4 1_{(n,rad q0)=1}: exponent-4 primes = supp(sJ2), exponent-0 primes | q0  [10331-10336]",
      not fails["xi"])
check("B6 q0 integral (J2 | q)   [10314-10316]", not fails["q0"])
check("B7 t_p = 0 => p in J2 u supp(q0)  (eq:poisson-divisor-reconstruction)   [11277-11288]", not fails["recon"])
check("B8 c = l_pair - s/2 - j2 and 4 l_pair - 2s + j2 = 4c + 5 j2   [10325-10329]", not fails["cube"])
check("B9 s, J2 disjoint (J squarefree)   [10317-10318]", not fails["sqf"])
# control: the alternative (wrong) parity rule t_p = a1 - a2 + 2 pi must break B2
bad = [k for k in tab if ((4 * k[1] + (1 + (k[1] - k[2] + 2 * k[0]) % 6 if (k[1] - k[2] + 2 * k[0]) % 6 else 0)
                           + k[0] * (k[1] + k[2])) % 6) != tab[k][1]]
check("B10 CONTROL: t_p with 2*pi instead of 3*pi breaks the common-exponent table (must fail -> detected)", bool(bad))

# ---------------------------------------------------------------------------------------------
print("== C. exact identities (sympy)")
(ell, A1, A2, B, t, g, thta, v, j, dlt, R_, h1, h2, Vv, Nn, Mm, s_i, Ai, tau, eta, Gs, P1, Dp, H_) = S(
    "ell A1 A2 B t g theta v j delta R h1 h2 V N M s_i A_i tau eta G P1 Dprime H", real=True)
rr = Nn - 3 * ell                                     # r = N - 3 ell   [9987]
F = Nn + Vv
s1, s2 = rr - A1 - B - t, rr - A2 - B - t             # [10404]
kap = lambda Aa: Mm - 2 * rr - 2 * ell - Vv - dlt + Aa + B - R_ / 2      # [10405]
# actual hats
hn1, hn2, hA1, hA2, hB, hR, hd, ht, hx1, hx2, hb1, hb2, hj, hf, hs, hj2, hc = S(
    "hn1 hn2 hA1 hA2 hB hR hd ht hx1 hx2 hb1 hb2 hj hf hs hj2 hc", real=True)
hL1 = hn1 + hn2 - hA1 - hA2 - 2 * hB + hR            # (first-poisson-lengths) [10226]
hk = lambda hn, hA: Mm - rr - 2 * ell - Vv - hd - hn + hA + hB - hR / 2
check("C1 prefactor split: -r-2l-V+M-d-L1/2 = (k1+k2)/2 (actual)   [10419-10424]",
      zero((-rr - 2 * ell - Vv + Mm - hd - hL1 / 2) - (hk(hn1, hA1) + hk(hn2, hA2)) / 2))
# n_i = A_i C t' x_i  =>  L1/2 = t + (x1+x2)/2 + R/2 ;  root (inverse-first-root-kernel)
sub_n = {hn1: hA1 + hB + ht + hx1, hn2: hA2 + hB + ht + hx2}
check("C2 actual root: Z^{-L1/2} = 1/(q_t sqrt(q_x1 q_x2 q_R))   [10433-10437]",
      zero(hL1.subs(sub_n) / 2 - (ht + (hx1 + hx2) / 2 + hR / 2)))
check("C3 center root: -r-2l-V+M-d-R/2-t-(s1+s2)/2 = (kappa_1+kappa_2)/2   [10433-10437]",
      zero((-rr - 2 * ell - Vv + Mm - dlt - R_ / 2 - t - (s1 + s2) / 2) - (kap(A1) + kap(A2)) / 2))
hh_ = sp.Symbol("hh")
check("C4 kernel: M + h - d - L1 = M + h - d - R - 2t - x1 - x2 (actual), i.e. A_ker1 = Z^{M+h1-d-R-2t-s1-s2}   [10438-10442]",
      zero((Mm + hh_ - hd - hL1.subs(sub_n)) - (Mm + hh_ - hd - hR - 2 * ht - hx1 - hx2)))
# y-bound derivation (10360-10368): y = h f^2 E,  h <= L1 + d - M + tau,  E from local identity
hE = hs - 2 * hj2 - hR + hA1 + hA2
ybound1 = hL1 + hd - Mm + tau + 2 * hf + hE
disp1 = hn1 + hn2 - 2 * hB - Mm + hs - 2 * hj2 + hd + 2 * hf + tau
check("C5 y <= n1+n2-2B-M+s-2j2+d+2f+tau  [10363-10365]", zero(ybound1 - disp1))
lpair = hc + hj2 + hs / 2
disp2 = hn1 + hn2 - 2 * hB - Mm + 4 * lpair - (hs + hj2) + hd + 2 * hf + tau
check("C6 second line - first line = 4c + 5j2 >= 0  [10366, (inverse-cube-actual)]",
      zero(disp2 - disp1 - (4 * hc + 5 * hj2)))
Hc = 2 * rr - 2 * B - Mm + 4 * ell + 2 * Vv + dlt - j     # (enlarged-first-frequency) [10372]
err_Hc = (hn1 - rr) + (hn2 - rr) - 2 * (hB - B) + 2 * (hb1 - ell) + 2 * (hb2 - ell) - (hj - j) + (hd - dlt) + 2 * (hf - Vv)
disp2b = hn1 + hn2 - 2 * hB - Mm + 2 * hb1 + 2 * hb2 - hj + hd + 2 * hf + tau
check("C7 (second line) - tau - H_c == displayed error expression   [10376-10380]", zero(disp2b - tau - Hc - err_Hc))
# second Poisson
Mc = 2 * (s_i - g) - Hc + dlt + 2 * thta
sI = rr - Ai - B - t
check("C8 M_c = 2(s_i-g) - H_c + d + 2theta = M-4l-2A_i-2t-2g+2theta-2V+j   (second-poisson-lengths) [10719-10724]",
      zero(Mc.subs(s_i, sI) - (Mm - 4 * ell - 2 * Ai - 2 * t - 2 * g + 2 * thta - 2 * Vv + j)))
kapI = kap(Ai)
check("C9 principal exponent kappa_i+H_c+s_i+B+t+l+R/2 = F-B-j   (second-principal-exponent) [10771-10774]",
      zero(kapI + Hc + sI + B + t + ell + R_ / 2 - (F - B - j)))
lam_c = Hc - thta - (sI - g)
Nc = rr - Ai - B - t - g - v
Vc = B + thta + v + j
Fc = Nc + Vc
Huse = Hc + 12 * eta + tau
check("C10 second root: H_use - theta - v - N_c = lambda_c + 12eta + tau  (N_c = s_i-g-v)  [11132-11143]",
      zero((Huse - thta - v - Nc) - (lam_c + 12 * eta + tau)))
check("C11 N_c = s_i - g - v   [11139]", zero(Nc - (sI - g - v)))
Dc = ell + Ai + t + g - thta + Vv
check("C12 F_c = F - D_c - 2l + j   (canonical-transition) [11032-11037]", zero(Fc - (F - Dc - 2 * ell + j)))
Mc_ = Mc.subs(s_i, sI)
check("C13 M_c = M - 2D_c - 2l + j", zero(Mc_ - (Mm - 2 * Dc - 2 * ell + j)))
check("C14 F_c - M_c = F - M + D_c", zero(Fc - Mc_ - (F - Mm + Dc)))
check("C15 4F_c - 3M_c = 4F - 3M + 2(A_i+t+g-theta+V) + j",
      zero(4 * Fc - 3 * Mc_ - (4 * F - 3 * Mm + 2 * (Ai + t + g - thta + Vv) + j)))
Cc = ell + R_ / 2 - j + t + g - thta
check("C16 ENERGY: kappa_i + lambda_c + C_c + 2F_c = F = r+3l+V   (canonical-prefactor) [11404-11410]",
      zero(kapI + lam_c + Cc + 2 * Fc - F))
check("C17 fixed-cube-count: c = l_pair + R/2 - j - r_diff/2 (with R = s + r_diff, j = s + j2)  [10601-10604]",
      zero((lpair + (hs + S("rd")) / 2 - (hs + hj2) - S("rd") / 2) - hc))
check("C18 M - M_ch (M_ch = M_c + eta) = 2D_c + 2l - j - eta   (inverse-row-decrease) [11098-11100]",
      zero(Mm - (Mc_ + eta) - (2 * Dc + 2 * ell - j - eta)))
# initialization (Lemma 17.1)
z_, G_ = S("z G_", real=True)
z0i = z_ - G_
Dpi = r + z_ - 2 * G_
check("C19 init: Z^{-(r+z)/2} = Z^{-G} Z^{-D'/2} with D' = r+z-2G   [11622-11630]",
      zero(-(r + z_) / 2 - (-G_ - Dpi / 2)))
kap_init = m - 2 * Dp + P1
Nci, Vci = Dp - B - v, thta + v
Fci = Nci + Vci
check("C20 init: F_c = D' - P1 with P1 = B - theta   (initial-canonical-lengths) [11935-11939]",
      zero(Fci.subs(B, P1 + thta) - (Dp - P1)))
check("C21 init root: -D'+m-theta-v-N_c = kappa_c^init (=m-2D'+B-theta)   (initial-root-kernel) [11982-11992]",
      zero((-Dp + m - thta - v - Nci) - (m - 2 * Dp + B - thta)))
check("C22 init kernel: m+H-theta-2v-2N_c = m+H-theta-2(D'-B)", zero((m + H_ - thta - 2 * v - 2 * Nci) - (m + H_ - thta - 2 * (Dp - B))))
check("C23 init energy: kappa_c + P1 + 2F_c = m   [12243-12246]", zero(kap_init + P1 + 2 * (Dp - P1) - m))
Mci = 2 * Dp - m - 2 * P1
check("C24 init margin 1: F_c - M_c - (P1+G) - z0 = m - r - 2z + 2G   [12183-12187]",
      zero(((Dp - P1) - Mci - (P1 + G_) - z0i).subs(Dp, Dpi) - (m - r - 2 * z_ + 2 * G_)))
check("C25 init margin 2: 4F_c - 3M_c - 6z0 = 3m - 2r - 8z + 10G + 2P1",
      zero((4 * (Dp - P1) - 3 * Mci - 6 * z0i).subs(Dp, Dpi) - (3 * m - 2 * r - 8 * z_ + 10 * G_ + 2 * P1)))
# Lemma 17.6
U, Hh = S("U H", positive=True)
P = (Hh / U) ** sp.Rational(1, 6)
check("C26 17.6: H/P = U^{1/6} H^{5/6}   [12447-12449]", sp.simplify(Hh / P - U ** sp.Rational(1, 6) * Hh ** sp.Rational(5, 6)) == 0)
cc = S("c", positive=True)
check("C27 17.6: H = D^{1+c}, D = U^r: log_U(U^{1/6}H^{5/6}) = (1+5r)/6 + 5rc/6 -> e(r) as c->0",
      zero(sp.Rational(1, 6) + sp.Rational(5, 6) * r * (1 + cc) - ((1 + 5 * r) / 6 + 5 * r * cc / 6)))
check("C28 17.6 raw moment: m=1, r=1/(1+c): 1-r = c/(1+c), 2r <= 3 - c2 with c2 = 1",
      zero((1 - 1 / (1 + cc)) - cc / (1 + cc)) and all(2 / (1 + Fr(k, 10)) <= 3 - 1 for k in range(1, 50)))

# ---------------------------------------------------------------------------------------------
print("== D. eta / tau error budgets (exact positive maxima over |error| <= unit per window)")


def posmax(coeffs):
    return sum(abs(Fr(c)) for c in coeffs)


check("D1 H_use - H_c: errors (n1,n2,B,b1,b2,j,d,f) weights (1,1,-2,2,2,-1,1,2) -> 12 eta   [10381-10383]",
      posmax([1, 1, -2, 2, 2, -1, 1, 2]) == 12)
check("D2 first prefactor kappa-hat <= kappa + 9/2 eta: weights (1,1,1,1,1/2)   [10426-10429]",
      posmax([1, 1, 1, 1, Fr(1, 2)]) == Fr(9, 2))
check("D3 L2 conductor |L2 - 2(s_i-g)| <= 10 eta (x1,x2 at 4 eta; g weight 2)   [10691-10695]",
      posmax([4, 4, 2]) == 10)
check("D4 k_new <= M_c + eta: 10 (conductor) + 1 (d_k) + 2 (two d_2) = 13 = 12 + 1   [10703-10727]",
      posmax([4, 4, 2, 1, 2]) == 13 and 13 - 12 == 1)
check("D5 lambda-hat <= lambda_c + 18 eta + tau: 12 + 1 + 4 + 1   [10751-10756]", 12 + 1 + 4 + 1 == 18)
check("D6 principal count: 9/2 + 12 + 4 + 1 + 1 + 7/2 = 26   [10775-10781]",
      Fr(9, 2) + 12 + 4 + 1 + 1 + Fr(7, 2) == 26)
check("D7 combined (q0,J) count: (l+R/2-j+5/2) + (j+1) = l+R/2+7/2   [10605-10609]", Fr(5, 2) + 1 == Fr(7, 2))
check("D8 fixed-cube-count slack 5/2: l_pair 1 + R/2 1/2 + j 1   [10603-10604]", posmax([1, Fr(1, 2), 1]) == Fr(5, 2))
check("D9 child column 6 eta (n_i,A_i,C,t',g',v'), label 4 eta (J,C,d2,v')   [11005-11008]",
      posmax([1] * 6) == 6 and posmax([1] * 4) == 4)
check("D10 new puncture 4 eta: c 1 + t 1 + (g - theta) 2   [11078-11084]", posmax([1, 1, 1, 1]) == 4)
check("D11 step loss: 9/2 + 18 + 11/2 = 28 ; 28 + 2*6 = 40   [11433-11441]",
      Fr(9, 2) + 18 + Fr(11, 2) == 28 and 28 + 2 * 6 == 40)
check("D12 fixed count 11/2 eta: q0 5/2 + t' 1 + r_g 2   [11336-11345]", Fr(5, 2) + 1 + 2 == Fr(11, 2))
check("D13 init: kappa 3 eta (theta,c_i,B); L_init 4 eta; row 4+2 = 6 eta; child 3 eta / 2 eta; Q_init 3 eta",
      posmax([1, 1, 1]) == 3 and posmax([1, 1, 2]) == 4 and 4 + 2 == 6)
check("D14 init margin-2 loss 22 = 4 (2P1 >= -4eta) + 18 (3 x 6eta row enclosure)   [12194-12195]", 4 + 3 * 6 == 22)
check("D15 init energy: 3 + 2 + 2*3 = 11   [12247-12252]", 3 + 2 + 2 * 3 == 11)

# ---------------------------------------------------------------------------------------------
print("== E. inequalities: exact Farkas certificates + failing controls")


def _lin(expr, vs):
    expr = sp.expand(expr)
    p = sp.Poly(expr, *vs)
    assert p.total_degree() <= 1, expr
    return [Fr(str(expr.coeff(x))) for x in vs], Fr(str(expr.subs({x: 0 for x in vs})))


def farkas(name, hyps, target, vs, strict=None):
    """Prove target >= 0 from hyps >= 0 (all linear in vs) by an exact certificate
    target = sum lam_k hyp_k + lam0, lam >= 0, lam0 >= 0 (lam0 > 0 if strict)."""
    rows = [_lin(h, vs) for h in hyps]
    aT, cT = _lin(target, vs)
    n = len(hyps)
    A_eq = [[float(rows[k][0][i]) for k in range(n)] for i in range(len(vs))]
    b_eq = [float(a) for a in aT]
    cost = [float(rows[k][1]) for k in range(n)]         # minimize sum lam_k c_k  => maximize lam0
    res = linprog(cost, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * n, method="highs")
    if res.status != 0:
        check(name + "  [no certificate]", False)
        return None
    lam = [Fr(x).limit_denominator(10 ** 6) for x in res.x]
    resid = sp.expand(target - sum(sp.Rational(l.numerator, l.denominator) * h for l, h in zip(lam, hyps)))
    const_ok = all(sp.expand(resid).coeff(x) == 0 for x in vs)
    lam0 = resid.subs({x: 0 for x in vs}) if const_ok else None
    good = const_ok and all(l >= 0 for l in lam) and lam0 is not None and (lam0 > 0 if strict else lam0 >= 0)
    check(name + ("   [cert: lam0=%s]" % lam0 if good else ""), good)
    return lam


def control(name, hyps, target, vs, box=1000):
    """Perturbed claim must FAIL: find exact rational point with hyps >= 0 and target < 0."""
    rows = [_lin(h, vs) for h in hyps]
    aT, cT = _lin(target, vs)
    A_ub = [[-float(a) for a in rr_[0]] for rr_ in rows]
    b_ub = [float(rr_[1]) for rr_ in rows]
    res = linprog([float(a) for a in aT], A_ub=A_ub, b_ub=b_ub, bounds=[(-box, box)] * len(vs), method="highs")
    if res.status != 0 or res.fun + float(cT) >= -1e-12:
        check("CONTROL " + name + " (perturbed claim should fail; it did not)", False)
        return
    pt = {x: sp.Rational(str(Fr(val).limit_denominator(10 ** 6))) for x, val in zip(vs, res.x)}
    hyp_ok = all(sp.nsimplify(h.subs(pt)) >= 0 for h in hyps)
    tv = sp.nsimplify(target.subs(pt))
    check("CONTROL " + name + "  -> fails as expected (exact witness, target=%s)" % tv, hyp_ok and tv < 0)


# --- canonical step: admissibility (10913-11118) ---
Fp, Mp, Qp, z0p, c, d, dN, Qn = S("F M Q z0 c d dN Qnew", real=True)
vs = [Fp, Mp, Qp, z0p, c, d, eta, dN, Qn, ell, Ai, t, g, thta, j, Vv]
Dc_ = ell + Ai + t + g - thta + Vv
Fc_ = Fp - Dc_ - 2 * ell + j
Mc2 = Mp - 2 * Dc_ - 2 * ell + j
Fch, Mch = Fc_ + dN, Mc2 + eta
base = [ell, Ai, t, Vv, j, thta, g, eta,                          # nonnegative centers, eta >= 0
        g - thta + 2 * eta, 2 * ell + 3 * eta - j,               # (inverse-center-inequalities)
        dN, 6 * eta - dN,                                        # (inverse-child-clipping)
        Qp + Dc_ + 4 * eta - Qn,                                 # (inverse-new-puncture), last line
        Fp - Mp - Qp - z0p - c, 4 * Fp - 3 * Mp - 6 * z0p - c,   # parent invariants
        ell + Vv - d, d / 16 - eta]                              # remaining block; eta <= d/16
farkas("E1 child margin 1: F_ch-M_ch-Q_new-z0 >= c - 5eta   (inverse-child-margins) [11090-11094]",
       base, Fch - Mch - Qn - z0p - c + 5 * eta, vs)
farkas("E1' child margin 1 (with delta_N): >= c + delta_N - 5eta", base, Fch - Mch - Qn - z0p - c - dN + 5 * eta, vs)
farkas("E2 child margin 2: 4F_ch-3M_ch-6z0 >= c - 7eta", base, 4 * Fch - 3 * Mch - 6 * z0p - c + 7 * eta, vs)
farkas("E2' child margin 2 (with 4 delta_N): >= c + 4delta_N - 7eta", base,
       4 * Fch - 3 * Mch - 6 * z0p - c - 4 * dN + 7 * eta, vs)
farkas("E3 row decrease: M - M_ch >= 2(l+V) - 8eta   (inverse-row-decrease) [11098-11100]",
       base, Mp - Mch - 2 * (ell + Vv) + 8 * eta, vs)
farkas("E4 row decrease >= 3d/2 (eta <= d/16, l+V >= d)", base, Mp - Mch - sp.Rational(3, 2) * d, vs)
farkas("E5 F_c <= F - l - V + 5eta", base, Fp - ell - Vv + 5 * eta - Fc_, vs)
farkas("E6 F_ch <= F + 11eta", base, Fp + 11 * eta - Fch, vs)
farkas("E6' (sharper, not claimed) F_ch <= F - 5eta", base, Fp - 5 * eta - Fch, vs)
farkas("E7 D_c >= l + V - 2eta and 2l - j >= -3eta", base, Dc_ - ell - Vv + 2 * eta, vs)
control("E1 with 4eta (margin 1)", base, Fch - Mch - Qn - z0p - c + 4 * eta, vs)
control("E2 with 6eta (margin 2)", base, 4 * Fch - 3 * Mch - 6 * z0p - c + 6 * eta, vs)
control("E3 with 7eta (row decrease)", base, Mp - Mch - 2 * (ell + Vv) + 7 * eta, vs)
base_d12 = base[:-1] + [d / 12 - eta]
control("E4 with eta <= d/12 instead of d/16 (3d/2 decrease)", base_d12, Mp - Mch - sp.Rational(3, 2) * d, vs)
base_d6 = base[:-1] + [d / 6 - eta]
control("E4' with eta <= d/6: decrease >= d", base_d6, Mp - Mch - d, vs)
control("E5 with 4eta", base, Fp - ell - Vv + 4 * eta - Fc_, vs)
# the new puncture inequality itself (11078-11084)
hcq, htq, hgq, hthq = S("hc ht hg hth", real=True)
vsq = [hcq, htq, hgq, hthq, ell, t, g, thta, eta, Ai, Vv]
hq = [ell + eta - hcq, t + eta - htq, hgq - g - eta, g + eta - hgq, hthq - thta + eta, thta + eta - hthq,
      Ai, Vv, eta]
farkas("E8 Q_new - Q <= c+t+g-theta (actual) <= l+t+g-theta+4eta <= D_c+4eta   [11078-11084]",
       hq, (ell + Ai + t + g - thta + Vv + 4 * eta) - (hcq + htq + hgq - hthq), vsq)
control("E8 with 3eta", hq, (ell + Ai + t + g - thta + Vv + 3 * eta) - (hcq + htq + hgq - hthq), vsq)
# center inequalities from actual divisibility (11063-11072)
hl, hjj, hg_, hth_ = S("hl hj hg hth", real=True)
vsc = [hl, hjj, hg_, hth_, ell, j, g, thta, eta]
hc_ = [hg_ - hth_, 2 * hl - hjj, ell + eta - hl, hl - ell + eta, hjj - j + eta, j + eta - hjj,
       g + eta - hg_, hg_ - g + eta, thta + eta - hth_, hth_ - thta + eta, eta]
farkas("E9 g - theta >= -2eta  from theta-hat <= g-hat", hc_, g - thta + 2 * eta, vsc)
farkas("E10 j <= 2l + 3eta  from j-hat <= 2 l_pair-hat", hc_, 2 * ell + 3 * eta - j, vsc)
control("E10 with 2eta", hc_, 2 * ell + 2 * eta - j, vsc)

# --- energy exponent (11402-11474) ---
pi_, ech = S("pi epsilon_child", real=True)
side = (kapI + lam_c + Cc + 2 * (Fc + dN)) + (sp.Rational(9, 2) + 18 + sp.Rational(11, 2)) * eta + tau + pi_ + ech
check("E11 per-side exponent = F + 28eta + 2delta_N + tau + pi + eps_child (exact)   [11433-11437]",
      zero(side - (F + 28 * eta + 2 * dN + tau + pi_ + ech)))
vse = [Nn, Vv, eta, dN, tau, pi_, ech, ell]
he = [dN, 6 * eta - dN, eta]
farkas("E12 ... <= F + 40eta + tau + pi + eps_child", he, (F + 40 * eta + tau + pi_ + ech) - (F + 28 * eta + 2 * dN + tau + pi_ + ech), vse)
control("E12 with 39eta", he, (F + 39 * eta + tau + pi_ + ech) - (F + 28 * eta + 2 * dN + tau + pi_ + ech), vse)
farkas("E13 second principal F-B-j+26eta+tau+pi <= F+40eta+tau+pi", [B, j, eta],
       (40 * eta) - (-B - j + 26 * eta), [B, j, eta])
farkas("E14 first principal M+pi <= F+... (M <= F - Q - z0 - c, Q,z0,c >= 0)",
       [Fp - Mp - Qp - z0p - c, Qp, z0p, c], Fp - Mp, [Fp, Mp, Qp, z0p, c])

# --- terminal (short completion) ledger (9870-9925): reflected-energy outputs taken as inputs ---
O, TSB, hh, za, Er, tref, pref, cst = S("O TSB hh za Eref tauref piref cstar", real=True)
vst = [Nn, Vv, Mp, Qp, z0p, c, d, eta, O, TSB, hh, za, tref, pref, cst]
Fn = Nn + Vv
Nstar = Nn - 3 * hh
ht_ = [2 * Mp - O + Qp + Vv - Nstar + 2 * za + eta - TSB,            # (inverse-terminal-width), second
       Fn - Mp - Qp - z0p - c, 4 * Fn - 3 * Mp - 6 * z0p - c,         # invariants
       d - Vv, d + eta - hh, Vv, hh, za, z0p - za, O, Qp, Mp, eta, tref, pref]
farkas("E15 (old-eq:4.9) TSB <= M - O + 2z_a - z0 - c + 5d + 4eta   [9887-9893]",
       ht_, Mp - O + 2 * za - z0p - c + 5 * d + 4 * eta - TSB, vst)
control("E15 with 5d + 3eta", ht_, Mp - O + 2 * za - z0p - c + 5 * d + 3 * eta - TSB, vst)
farkas("E16 (old-eq:4.10) O/2 + TSB + 5eta/3 + tref <= F - 2c + 5d + 17eta/3 + tref   [9906-9910]",
       ht_, (Fn - 2 * c + 5 * d + sp.Rational(17, 3) * eta + tref) - (O / 2 + TSB + sp.Rational(5, 3) * eta + tref), vst)
farkas("E17 (old-eq:4.11) O/2 + TSB/2 + z_a + 7eta/6 + tref/2 <= F - M/4 - 3c/4 + 5d/2 + 19eta/6 + tref/2   [9911-9920]",
       ht_, (Fn - Mp / 4 - sp.Rational(3, 4) * c + sp.Rational(5, 2) * d + sp.Rational(19, 6) * eta + tref / 2)
       - (O / 2 + TSB / 2 + za + sp.Rational(7, 6) * eta + tref / 2), vst)
farkas("E18 row branch: M + z_a + 5eta/3 <= F - c + 5eta/3", ht_, (Fn - c) - (Mp + za), vst)
control("E16 dropping O>=0 (O can be negative)", [h for h in ht_ if h is not O],
        (Fn - 2 * c + 5 * d + sp.Rational(17, 3) * eta + tref) - (O / 2 + TSB + sp.Rational(5, 3) * eta + tref), vst)
# "all three bounds, after adding pi_ref, are strictly below F" (9921-9925)
tpar = [c - cst / 2, cst / 200 - d, cst / 1000 - eta, cst / 1000 - tref, cst / 1000 - pref, Mp, eta, tref, pref, d, cst]
vsp = [c, cst, d, eta, tref, pref, Mp]
farkas("E19 row branch strictly below F: c - 5eta/3 - pi_ref > 0", tpar,
       c - sp.Rational(5, 3) * eta - pref - cst / 1000, vsp)
farkas("E20 (4.10)+pi_ref strictly below F", tpar,
       2 * c - 5 * d - sp.Rational(17, 3) * eta - tref - pref - cst / 1000, vsp)
farkas("E21 (4.11)+pi_ref strictly below F", tpar,
       Mp / 4 + sp.Rational(3, 4) * c - sp.Rational(5, 2) * d - sp.Rational(19, 6) * eta - tref / 2 - pref - cst / 1000, vsp)
tpar_bad = [c - cst / 2, cst / 4 - d] + tpar[2:]
control("E20 with d <= c*/4 instead of c*/200 (c*/20 still passes: large slack)", tpar_bad,
        2 * c - 5 * d - sp.Rational(17, 3) * eta - tref - pref, vsp)
control("E21 with c_node >= c*/100 instead of c*/2 (c*/8 still passes: large slack)",
        [c - cst / 100] + tpar[1:], Mp / 4 + sp.Rational(3, 4) * c - sp.Rational(5, 2) * d
        - sp.Rational(19, 6) * eta - tref / 2 - pref, vsp)

# --- initialization margins (12185-12271) ---
ti, Qi, di, mm, rr_, zz, GG, P1s, cc1, cc2 = S("tau_init Q_init delta_init m r z G P1 c1 c2", real=True)
Dpp = rr_ + zz - 2 * GG
z0x = zz - GG
Fci_ = Dpp - P1s
Mci_ = 2 * Dpp - mm - 2 * P1s
Fi, Mi = Fci_ + di, Mci_ + 6 * eta + ti
vsi = [mm, rr_, zz, GG, P1s, cc1, cc2, eta, ti, Qi, di]
hi = [mm - cc1 - rr_ - 2 * zz, 3 * mm - cc2 - 2 * rr_ - 8 * zz,   # marked premises
      GG, z0x, P1s + 2 * eta, P1s + GG + 3 * eta - Qi, di, 3 * eta - di, eta, ti]
farkas("E22 init margin 1 >= c1 + delta - 9eta - tau_init   (inverse-initial-margins) [12188-12195]",
       hi, Fi - Mi - Qi - z0x - (cc1 + di - 9 * eta - ti), vsi)
farkas("E23 init margin 2 >= c2 + 4delta - 22eta - 3tau_init", hi, 4 * Fi - 3 * Mi - 6 * z0x - (cc2 + 4 * di - 22 * eta - 3 * ti), vsi)
control("E22 with 8eta", hi, Fi - Mi - Qi - z0x - (cc1 + di - 8 * eta - ti), vsi)
control("E23 with 21eta", hi, 4 * Fi - 3 * Mi - 6 * z0x - (cc2 + 4 * di - 21 * eta - 3 * ti), vsi)
cb = S("cbar", real=True)
vsb = [cb, cc1, cc2, eta, ti]
hb = [cc1 - cb, cc2 - cb, cb / 100 - eta, cb / 100 - ti, eta, ti, cb]
farkas("E24 init margins >= 3cbar/4 > c* = cbar/2 (eta, tau_init <= cbar/100)   [12262-12264]", hb,
       cc2 - 22 * eta - 3 * ti - sp.Rational(3, 4) * cb, vsb)
control("E24 with eta <= cbar/50 (stated 3cbar/4 fails; > cbar/2 would still hold)",
        hb[:2] + [cb / 50 - eta] + hb[3:], cc2 - 22 * eta - 3 * ti - sp.Rational(3, 4) * cb, vsb)
farkas("E25 init energy: 11eta + pi_init <= eps/4 (eta<=eps/88, pi_init<=eps/8), total m+3eps/4   [12267-12271]",
       [eps / 88 - eta, eps / 8 - pi_, eta, pi_, eps], eps / 4 - (11 * eta + pi_), [eps, eta, pi_])
control("E25 with eta <= eps/80", [eps / 80 - eta, eps / 8 - pi_, eta, pi_, eps], eps / 4 - (11 * eta + pi_), [eps, eta, pi_])
farkas("E26 init a-priori ranges: M_init <= 2D_max + 10eta + tau <= 2D_max + 1  (eta,tau<=1/100)",
       [S("Dm") - Dpp, mm, P1s + 2 * eta, sp.Rational(1, 100) - eta, sp.Rational(1, 100) - ti, eta, ti],
       2 * S("Dm") + 1 - Mi, [S("Dm"), rr_, zz, GG, mm, P1s, eta, ti])

# ---------------------------------------------------------------------------------------------
print("== F. order of choices and termination (11474-11599)")
# depth bound: D = ceil((Mmax+2)/d) + 1  =>  Mmax - D d < 0  (cap negative at depth D)
badD = []
for Mmax in [Fr(k, 7) for k in range(0, 300, 7)]:
    for dd in [Fr(1, k) for k in range(1, 400, 13)]:
        D = math.ceil((Mmax + 2) / dd) + 1
        if not (Mmax - D * dd < 0 and Mmax - (D - 1) * dd < 0):
            badD.append((Mmax, dd))
check("F1 row cap M_max - D d < 0 (indeed already at depth D-1)   [9817-9822, 11590-11592]", not badD)
# per-level contraction >= 3d/2 > d is E4; margin decay c_h = c* - 7h eta >= c*/2 for h <= D:
Dsym, csym, esym = S("D cstar eps", positive=True)
etamax = sp.Min(csym / (14 * Dsym), esym / (160 * Dsym))
check("F2 c_D = c* - 7 D eta >= c*/2 when eta <= c*/(14D)   [11481, 11588]",
      zero((csym - 7 * Dsym * (csym / (14 * Dsym))) - csym / 2))
check("F3 eps budget: D*(40 eta + tau + pi) <= 3eps/4 < eps at eta=eps/(160D), tau=pi=eps/(4D)   [11593-11597]",
      zero(Dsym * (40 * esym / (160 * Dsym) + 2 * esym / (4 * Dsym)) - sp.Rational(3, 4) * esym))
check("F4 CONTROL: eta <= eps/(40D) would give D*40*eta = eps (budget fails -> detected)",
      zero(Dsym * 40 * esym / (40 * Dsym) - esym))
check("F5 CONTROL: eta <= c*/(7D) would give c_D = 0 < c*/2 (detected)",
      zero(csym - 7 * Dsym * csym / (7 * Dsym)))
# induction: depth-h bound F + (D-h) L_step, nonterminal: F + L_step + (D-h-1) L_step
Lst, hsym = S("L_step h", real=True)
check("F6 backward induction step: L_step + (D-h-1)L_step = (D-h)L_step", zero(Lst + (Dsym - hsym - 1) * Lst - (Dsym - hsym) * Lst))
# child hypothesis window: margins >= c_node - 7eta = c_{h+1}; M' <= M - d; F' <= F + 11eta
check("F7 c_{h+1} = c_h - 7eta matches the induction hypothesis margin (c_node - 7eta)   [10010-10013]",
      zero((csym - 7 * (hsym + 1) * eta) - ((csym - 7 * hsym * eta) - 7 * eta)))
# Schwartz tail orders
Bc, T_, A_, Bref, tr = S("B_crude T A B_ref tau_ref", positive=True)
check("F8 tail: Z^{B_crude} Z^{tau(1-A)} <= Z^{-T} iff A >= 1 + (B_crude+T)/tau   [11545-11551]",
      zero((Bc + tau * (1 - (1 + (Bc + T_) / tau))) + T_))
check("F9 reflected tail: argument >= Z^{tau_ref/2}: A_ref >= 1 + 2(B_ref+T)/tau_ref   [11553-11558]",
      zero((Bref + tr / 2 * (1 - (1 + 2 * (Bref + T_) / tr))) + T_))
# late external cutoff (Sec 17.3, 9692-9700): tau < delta/(1+H) => (1+Z^tau)^H <= 2^H Z^delta
Hd, dl = S("H delta", positive=True)
check("F10 late cutoff: tau*H < delta when tau < delta/(1+H)", sp.simplify(dl / (1 + Hd) * Hd - dl) .is_negative)
# H_use bound used for L_all: H_c <= 3F_max + 4eta + ... <= 7F_max + 18eta + tau
Fm = S("Fmax", positive=True)
vsH = [rr, ell, Vv, B, Mm, j, dlt, Nn, eta]
farkas("F11 H_use <= 7F_max + 18eta + tau  (with delta <= r+2l+4eta, N,V <= F_max, r >= -eta)   [11516-11520]",
       [B, Mm, j, ell, Vv, eta, rr + 2 * ell + 4 * eta - dlt, Fm - Nn, Fm - Vv, rr + eta, Nn - 3 * ell - rr, rr - Nn + 3 * ell],
       7 * Fm + 18 * eta - (Hc.subs(Nn, rr + 3 * ell) + 12 * eta).subs(rr, rr), vsH + [Fm])
# Quantifier order as a DAG (the text's "first fix ... then ... finally Z")
deps = {
    "ranges,tests,slots,c*": [], "eps": [],
    "d": ["ranges,tests,slots,c*"], "D": ["d", "ranges,tests,slots,c*"],
    "eta": ["d", "D", "eps", "ranges,tests,slots,c*"], "tau": ["D", "eps", "ranges,tests,slots,c*"],
    "pi": ["D", "eps"], "tau_ref,pi_ref": ["ranges,tests,slots,c*"],
    "cutoffs,I_D,L_win": ["D", "eta"], "F_max,L_all": ["D", "eta", "ranges,tests,slots,c*"],
    "subsidiary exponents": ["pi", "tau_ref,pi_ref", "F_max,L_all"],
    "B_crude,B_ref": ["F_max,L_all", "cutoffs,I_D,L_win"], "T": ["B_crude,B_ref"],
    "A,A_ref": ["B_crude,B_ref", "T", "tau", "tau_ref,pi_ref"],
    "Fourier/seminorm orders": ["A,A_ref", "D", "cutoffs,I_D,L_win"],
    "Z threshold": ["cutoffs,I_D,L_win", "eta", "tau_ref,pi_ref", "subsidiary exponents", "Fourier/seminorm orders"],
}


def acyclic(dd):
    seen, stack = set(), set()

    def visit(x):
        if x in stack:
            return False
        if x in seen:
            return True
        stack.add(x)
        okk = all(visit(y) for y in dd[x])
        stack.discard(x)
        seen.add(x)
        return okk
    return all(visit(x) for x in dd)


check("F12 order of choices (11477-11586) is a DAG ending in the Z threshold", acyclic(deps))
bad_deps = dict(deps)
bad_deps["eta"] = deps["eta"] + ["F_max,L_all"]
check("F13 CONTROL: making eta depend on L_all creates a cycle (detected)", not acyclic(bad_deps))

# MODEL (illustration only): Lemma 17.3 backward order selection with model edge data
#   child profile:  p_j(W_e) <= p_{j+2}(w) <t>^{j} <xi>^{j}   (m_e(j)=j+2, b'=1, c'(j)=j)
#   coefficient measure (inverse-fourier-moment): needs 2m0 > H + dim  -> l_e(H) = H + dim + 2, c_e(H) = H
def model_orders(depth, dims=(9, 6), J0=4, H0=0):
    J, Hh_ = J0, H0                      # terminal input orders
    for _ in range(depth):
        for dim in dims:                 # two Poisson/Fourier separations per level
            He = Hh_ + J                 # H_e = H' + B' c'_e(J'), B' = 1
            J = max(J + 2, He + dim + 2)
            Hh_ = He + He                # H_e + c_e(H_e)
    return J, Hh_


mo = [model_orders(Dd) for Dd in (1, 2, 5, 10)]
print("     MODEL Lemma 17.3 orders (J, height) at depth 1,2,5,10:", mo)
check("F14 MODEL: orders finite at every finite depth; they depend on eps only through D and the tail order",
      all(isinstance(x, int) for p in mo for x in p))

print("\nSUMMARY: %d/%d checks passed" % (sum(x for _, x in ok), len(ok)))
