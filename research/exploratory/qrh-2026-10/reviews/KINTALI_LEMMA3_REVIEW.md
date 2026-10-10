# Bounded review: Kintali, Lemma 3 (weak reflection) and Appendix B; identities (4)-(6) / Appendix A

```text
Status: REVIEW (bounded; external manuscript)
Scope: Kintali Lemma 3, Appendix B, identities (4)-(6)/Appendix A as far as checked.
  Checked: Lemma 3 statement (pp. 8-9, eq. (12)); App. B in full (pp. 22-26: theta normalization,
  masks C_{p,j}, masked conjugate theta, rational cusps and multiplier (B.2), derivative and
  reflected local characters, B_p, Mellin normalization (B.3), kernel V#, |zeta_R| <= 1/81,
  cusp support and |d(mu)| bound); every Dunn-Radziwill (DR) input that App. B quotes; (3) and (4)
  on pp. 4-5 against T_{m,s,eta} in (2); (8) on p. 7 from table (A.4); A.3 table (A.4) compared
  symbol by symbol with the OpenAI table already checked in ../numerics.
  Not checked: App. A.2 "Fixed and moving phase cancellation" (p. 20), i.e. the factorization of
  K_eta(c,n,s,a;u) into the local restored summands; Lemma 4 beyond what the first review did.
Exact sources or dependencies:
  [K]  Kintali, "A Short Proof of the Quasi-Riemann Hypothesis" (7 Oct 2026), PDF sha256
       f7ddc46632e37466e85951ea67acbd3c2abc19c8259fac51be569b1f6bbbe8e5. Every formula used here was
       read from 300-dpi renderings (pdftoppm -r 300) of pp. 4, 5, 8, 9, 18-26, with overbars as printed.
  [DR] A. Dunn, M. Radziwill, "Bias in cubic Gauss sums: Patterson's conjecture", arXiv:2109.07463v3
       (source dated 14-15 May 2024); PDF sha256
       df888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0; TeX source output.tex sha256
       47d01be0662e77cf7a8c64c277945f3e54b9d8868ca5f67668647032aa4a2b66 (e-print tarball sha256
       1373df1737fb6b70a82a452fdf37658893ab4112f8c000f49bbdd12286f87577). Used: Sec. 1.2 and Sec. 2 (cubic
       symbol, cubic reciprocity, supplementary law, g(c), g~(c), twisted multiplicativity), Sec. 5.1
       eqs. (5.1)-(5.15), Sec. 5.2 eq. (5.16), Appendix A table (d_j column). Equation numbers were
       matched against the PDF.
  [OAI-num] ../numerics/README.md and check_local_euler.py / check_kintali_phase.py (prior repository
       checks of the OpenAI local table (7.10)-(7.16) and of Kintali (1), (A.1), (A.2)).
  [R1] ./KINTALI_REVIEW.md (first bounded review of [K]).
What was actually run (Python 3, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0, mpmath 1.3.0; nice -n 10,
  one process at a time):
  python3 -I kintali_lemma3_theta.py  OUT.json   18 s   (T0-T3, FLOATING_RECONNAISSANCE)
  python3 -I kintali_lemma3_finite.py OUT.json  185 s   (F1-F7, EXACT or FLOATING as labelled)
  Helper: kintali_lemma3_common.py (exact Z[omega] arithmetic, symbols by exact powmod).
  Script sha256: common 207ace21...b34a51, finite 18648148...edd1, theta f05022c3...c875.
  Output JSON is in the session scratchpad only (not committed); every number quoted below is from it.
Smallest remaining gap: App. A.2, p. 20 ("Fixed and moving phase cancellation"): the claim that the
  Poisson coefficient K_eta(c,n,s,a;u) equals the product over p of the restored summands on p. 21.
  This is the high-side identity (5)-(6); it is not used by Lemma 3. No error was found in it and it
  was not tested. For Lemma 3 itself the smallest untested statement is the end-to-end assembly of
  (12) for one actual completed row. Each ingredient was tested separately (below), but the
  assembled formula was not evaluated numerically.
```

RH is not touched by this paper or by this review. [K] claims a zero-free half-plane `Re s > 47/48`
for Hecke L-functions over Q(sqrt(-3)). Nothing below is a repository result. The verdict covers
only the steps listed under Scope.

## 0. Verdict

**No error found in Lemma 3 or Appendix B.** Every finite algebraic step of App. B was checked
with exact symbols, either exactly or in floating point. The DR inputs are quoted correctly. One
step was tested directly on the cubic theta function built from DR's printed coefficients: the
reflection of a single translate through a rational cusp, with Kintali's cusp choice and his
multiplier (B.2). It holds to about 1e-10 relative error at 78 cusps, covering all three
lambda-adic cases. Removing the conjugate on the multiplier breaks the identity, with deviation
sqrt(3). This matters because that conjugate is what makes the moving characters quadratic
(`chi_R(.)^3`), and so lets the quadratic large sieve apply.

The structural claims that [R1] had to assume for Lemma 4 hold. After the subdivision R mod M^2,
M = lambda^12 L^4, the R-dependence of (12) is only through:
* the scalar zeta_R, with |zeta_R| <= 1/81;
* the quadratic symbol chi_R(lambda^4 mu)^3;
* q_R inside the kernel argument.

The cusp coefficient d, the phase vartheta and the frozen factors B_p are independent of R.

First step **not verified**, as opposed to wrong: App. A.2, p. 20, the high-side phase
cancellation. See the header. It does not feed the low bound J << Z^{1/4+eps}.

## 1. External inputs from Dunn-Radziwill (arXiv:2109.07463v3) and how [K] uses them

| [K] quote (App. B) | DR source | quoted correctly? | numerical status |
|---|---|---|---|
| theta(z,v) = (3^{5/2}/2) v^{2/3} + sum t(mu) v K_{1/3}(4 pi abs(mu) v) ech(mu z), "[2, (5.6)-(5.8)]" | (5.6) sigma = 3^{5/2}/2; (5.7) tau(mu); (5.8) c, d primary, c squarefree | yes | T1, T2 |
| t(lambda^{-3} c b^3) = 3^{5/2} abs(b) conj(g~_3(c)) | (5.7), n = 0 line: conj(g(1,c)) abs(d/c) 3^{5/2}; g~(c) = g(c)/abs(c) (Sec. 2) | yes (bar present in the PDF) | T0 |
| coefficients are even, so conj(theta) has coefficients conj(t(mu)) | "tau is even" after (5.8); (5.16) | yes | — |
| theta(gw) = kappa(g) theta(w) on Gamma_2 = <SL2(Z), Gamma_1(3)>, kappa = (c/a)_3 on Gamma_1(3) (c != 0), 1 if c = 0 or on SL2(Z): "[2, (5.2)-(5.5)]" | (5.2), (5.4); the automorphy sentence after (5.5); extension to SL2(Z) per Patterson | yes | **T1: chi = (c/a)_3 matches (dev <= 4.4e-13, 14 elements, 9 with nontrivial chi); conj chi fails (dev 1.7)** |
| conj expansions at H = I, L(lambda), L(-lambda) are DR's j = 1, 19, 10, with d_H(mu) = conj(d_j^DR(-mu)): "[2, (5.9), (5.12), (5.16), App. A]" | (5.9) F_j = theta o gamma_j, gamma_10 = L(w), gamma_19 = L(w^2); (5.12); (5.16) conj F_j expansion; App. A: d_10 = w tau_2(w mu) ech(mu), d_19 = w^2 tau_1(w^2 mu) ech(mu) | yes | **T2: theta(L(lambda)w) = F_19(w) and theta(L(-lambda)w) = F_10(w) to 5e-15; the swapped assignment fails (0.12)** |
| support mu = u lambda^k n b^3, k >= -4; magnitudes 3^{k/6+8/3}, 3^{k/6+3}, and 9 at k = -4: "[2, (5.7), (5.13), (5.14), App. A]" | (5.7): k = 3n-4 (n >= 1) and k = 3n-3 (n >= 0); (5.13)-(5.14): k = -4 | yes; exact: 3^{n/2+2} = 3^{k/6+8/3}, 3^{n/2+5/2} = 3^{k/6+3} = 27·3^{k/6}, 9 <= 27·3^{-2/3} | — |

**Hypotheses.**
* [K] uses only DR Sec. 5.1-5.2 and the d_j column of DR App. A. These are Patterson's
  unconditional results (automorphy of the cubic theta function, its expansions at the cusps
  j = 1, 10, 19).
* [K] does **not** use DR's twisted Voronoi formula (Sec. 5.3-5.6). That formula assumes a twist
  periodic modulo r ≡ 1 (mod 3) and DR's cusp words E^3 W(r,b)^{-1}. [K] uses neither assumption.
* [K]'s masks are periodic modulo L, which is supported on S and divisible by 18, and modulo the
  moving primes. They enter only as finite Fourier sums of translates by lambda^2 h/L and
  lambda^2 h/p. These need nothing beyond automorphy on Gamma_2, together with the fact that
  translation by lambda^2 O = 3O has multiplier 1 (c = 0).
* [K]'s cusp normalization is his own. He reduces every cusp to H in {I, L(±lambda), E L(-u0)} so
  that g H^{-1} ∈ Gamma_1(3). The middle and last cases rest on two facts:
  - lambda - w^2 and -lambda - w lie in Z + 3O;
  - kappa(E) = 1.

  The first is checked by T2. The second is checked indirectly by the case-3 rows of T3.
* No GRH input of DR is used. DR's GRH enters only in their Sec. 6 onwards.
* DR's (5.4) multiplier together with the printed tau in (5.7) is consistent with the true
  automorphy (T1). The orientation question "kappa or conj kappa" is therefore settled
  numerically, not only by citation.

## 2. Step-by-step check of Appendix B

Labels: EXACT means exact integer, rational or sympy arithmetic. FLOATING means double precision
with exact symbols but floating exponentials or Bessel functions. It is not directed and not
certified.

| # | [K] step (page) | what was checked | result | label |
|---|---|---|---|---|
| B1 | g~_3(c) = chi_c(lambda)^{-2} gamma_2(c), p. 24, and abs(g~_3) = 1 | by hand (substitute d = lambda v, e(lambda z) = ech(z)); numerically for 105 squarefree primary c prime to 6, with N c <= 700, 1-2 prime factors | max dev 3.6e-15 | F1, FLOATING |
| B2 | C_{p,j}(h): four-case formula, abs(tau^-_{p,j}) = 1, and inversion sum_h C_{p,j}(h) e(hx/p) = chi_p(x)^j with zero at p \| x (including j = 0), p. 23 | split and inert primes with N <= 61, j = 0..5, every h and x | max dev 6.2e-15 (2682 coefficient cases) | F2, FLOATING |
| B3 | masked conj theta Theta_m: the coefficient at mu = lambda^{-3} c b^3 equals 3^{5/2} abs(b) gamma_2(c) nu(A) chi_A(m), and every other mu is killed (λ \| x, or x ≡ -1 mod 3), pp. 23-24 | by hand: translation multiplies the coefficient by e(lambda^3 mu h/p) = e(xh/p); combine with B1, B2 and the reciprocity display (sextic reciprocity (A.2), already EXACT-checked in [OAI-num] K4 including nonsquarefree arguments) | holds | reading + F1/F2 |
| B4 | fraction a/c reduced; g ≡ I, L(u0), (u0 -1; 1 0) (mod 3) in the three λ-cases; g H^{-1} ∈ Gamma_1(3), p. 24 | asserted in code for every constructed cusp (78 in T3, 168 in F5) | holds | T3/F5, EXACT |
| B5 | (B.2) kappa(g H^{-1}) = kappa_fix prod_{p\|r} chi_p(a)^2, with the explicit fixed factors (c_F/a)_3, (-u0/A0)_3 ((c_F/u0)/a)_3, (a/c_F)_3, p. 24 | by hand (all three derivations reproduced, including (delta/(1-a delta))_3 = 1 from a delta ≡ 1 mod 9 and mod delta); kappa computed directly from DR (5.4) by factorization, against the closed form; kappa_fix constant over four lifted frequency tuples per branch (test modulus lambda^8·4 in place of M) | 168/168 match, all three cases; 42/42 branches constant | F5, EXACT |
| B6 | z', v' of g^{-1}w; d/dz-bar z' = -(cv)^{-2}, d/dz-bar z-bar' = d/dz-bar v' = 0 at z = 0; the cusp constant is killed, p. 25 | by hand from DR (5.1) | holds | reading |
| B7 | **single-translate reflection**: d/dz-bar conj(theta)(a/c+z, v) at z = 0 equals conj kappa(k_g)·(-(cv)^{-2})·sum d_H(mu) 2 pi i mu v'K(4 pi abs(mu) v') ech(-delta mu/c), p. 25 (and the undifferentiated identity) | theta from DR (5.7); F_10, F_19 from DR's table; 78 cusps a/c from [K]'s recipe; every combination (case, j) ∈ {(1,1), (2,10), (2,19), (3,1), (3,10), (3,19)}; kappa codes 0/1/2 occur 36/25/17 times; q_c <= 63, heights 0.096-0.29 and dual heights >= 0.165 | max rel dev 1.2e-10 (derivative), 1.6e-11 (value); with kappa instead of conj kappa the deviation is >= 1.73 on all 42 nontrivial-kappa cusps | T3, FLOATING |
| B8 | additive CRT: ech(-delta mu/c) = vartheta(x) prod_p e(eps_p h_p^{-1} x/p), x = lambda^4 mu, f = lambda^3 c_F, eps_p = -(lambda^5 c_F^2 (r/p)^2)^{-1}, p. 25 | exact rational exponents mod 1, random c_F (S-supported, incl. lambda^k, -2, 4), 1-3 moving primes, random h, random x | 2400/2400 exact | F3, EXACT |
| B9 | vartheta and delta_F, r^{-1} mod f fixed in the sector | by hand: f \| M^2, and delta mod lambda^3 c_F is pinned by the CRT choices (≡ a^{-1} at c_F-primes and at λ if λ \| c_F, ≡ 0 mod lambda^{v(M)} ⊇ lambda^3 otherwise) | holds | reading |
| B10 | h_p sums: sum_{h≠0} C_{p,j}(h) conj(chi_p(a_h)^2) e(eps_p h^{-1} x/p) = K_j · B_p(x), with B_p as tabulated and chi_p(x)^3 at R-primes (j = 1); abs(K_j) = 1 and K_j independent of x; abs(B_p) <= q_p^{1/2}, p. 25 | 24 random (c_F, r, p) × j = 0..5, every x mod p | dev from constant·B_p <= 2.7e-15; abs(abs(K_j)-1) <= 5.8e-15 | F4, FLOATING |
| B11 | (B.3) constant 81/(8 pi) (27/(4 pi^2))^t; ∞-side coefficient 6 pi abs(cb^3) abs(b) gamma_2(c) conj(alpha(cb^3)), matching conj(alpha) in (3) | Bessel Mellin formula (mpmath, 4 values of w, <= 2.9e-13); constant algebra in sympy | ratio - 1 = 0 | F6, EXACT + FLOATING |
| B12 | dual moment: -(i/8 pi) conj(kappa alpha(c)^2)(4 pi^2)^t q_c^{-2t} prod Gamma(1-t ± 1/6) sum d_H alpha(mu) q_mu^{t-1/2} ech(..), p. 25; prefactor -i conj(alpha)^2/81 and kernel scale (2 pi)^4/27, p. 26 | sympy constant algebra; one numerical dual-moment integral (rel dev 1.6e-16) | ratio - 1 = 0 | F6 |
| B13 | V#: no poles in Re t >= 0 (first poles at -5/6, -7/6); Stirling gives (1+abs(t))^{4 sigma}; bounds (x d/dx)^j V# << min(1, x^{-A}) | by hand; V# evaluated on lines sigma = 0 and sigma = 1 at x ∈ {0.01, 0.1, 1, 10}: identical to 1e-17 (no poles crossed); real-valued | holds | F6, FLOATING |
| B14 | analytic continuation: Mellin moments of each differentiated translate are entire (exponential decay at both ends after the constant is killed); D_m(t) entire with e^{pi abs(Im t)} growth; the shift is justified by e^{t^2} | by hand | holds (standard Hecke argument) | reading |
| B15 | abs(zeta_R) <= 1/81: zeta_R = (-i/81) conj(alpha(c_cusp))^2 · conj kappa_fix · hat phi(h0) · prod K_j · prod (1 - q_p^{-1}) | assembled from B5, B10, B12; abs(hat phi) <= 1 since abs(phi) <= 1 | holds | reading |
| B16 | count O_{S,nu}(2^{omega(P)}): q_L values of h0 times at most 2^{omega(P)} active sets (a frozen prime is inactive only when j_p = 0) | by hand | holds | reading |
| B17 | support k >= -4, n squarefree, abs(d(mu)) <= 27·3^{k/6} q_b^{1/2}; convergence majorant sum_k 3^{-k(sigma+1/3)} sum q_n^{-sigma-1/2} sum q_b^{-3 sigma-1} for sigma > 1/2 (p. 26) | exact exponent arithmetic from (5.7), (5.13), (5.14); abs(g~(c)) = 1 for squarefree c including c = -2 (T0) | holds | EXACT |

T0 (plumbing; FLOATING) tested the following against direct sums:
* the prime cubic Gauss sums;
* twisted multiplicativity g(ab) = conj((a/b)_3) g(a) g(b);
* g(r, c) = conj((r/c)_3) g(c) for r ∈ {1, w^i lambda^2}.

These are used to build tau, tau_1 and tau_2. Over 380 composite cases the maximum relative
deviation is 9.2e-14.

Remarks (not errors):

* p. 25, "(B.2) ... Conjugating contributes chi_p(h_p)^{-2}". At frozen active primes as well as at
  R-primes, the companion scalars chi_p(lambda^2 c_F (r/p))^{-2}, chi_p(eps_p)^{...} and tau^-
  depend on R through r/p. As [K] says, they go into zeta_R and not into B_p. F4 confirms that
  they are independent of x.
* The "fixed ray subdivision" of Lemma 3 is the class of R mod M^2, with M = lambda^12 L^4. This
  is finite and S-dependent. It contains the classes mod 4 that Lemma 4's GL step needs to fix e(R).
* [K]'s M is much larger than needed. The argument only uses that a mod 9 c_F and b0 mod 9 are
  fixed. F5 reproduces constancy with lambda^8·4.

## 3. Identities (3), (4) and Appendix A (as far as checked)

* **(3) vs (2).**
  - T_{m,s,eta} in (2) carries gamma_2(c) conj(alpha(A)) conj(G(A)). The expansion on p. 5 is of
    conj(G(A)) = sum a_theta theta(A), with a_theta = abs(T)^{-1} sum conj(G(gamma)) conj(theta(gamma)).
  - The Mellin inversion of Phi = e^{t^2} = hat V_G is right: the substitution x = e^u gives
    hat V_G(t) = e^{t^2} exactly.
  - Together these give (1/2 pi i) ∫ Z^t Phi T dt = B_{m,sigma}(Z), with nu_sigma theta S-supported.
  - The bar on alpha in (3) is the one that ∂_{z̄} produces in B11.

  **Holds** (by hand).
* **(4).**
  - (q_m/(q_{b*} q_s X)) = (q_m/Q0)/(q_s/Y) and (q_{b*} q_s X)^{-1/2} = Q0^{-1/2}(q_s/Y)^{-1/2}.
  - Inserting Omega is harmless: Omega = 1 wherever W0·W1 ≠ 0.
  - Mellin inversion of W0 on Re = 0 then produces A_{m,sigma,v}(Y) exactly as displayed.

  **Holds** (by hand).
* **(5).**
  - The finite transform sum_{m mod s b* A} xi chi_A(m) q_s^{-1/2} g_{chi_s}(s,-m) e(Hm/(s b* A))
    = q_s^{1/2} F(s,A,H) is right. Write m = r + b* A l; orthogonality in l forces s | H - b* A d.
    No coprimality is used.
  - The dilation factors X/q_A and X q_H/q_A and the leftover X^{1/2}/(sqrt(q_{b*}) q_A) are
    right (by hand).
  - The derivation from these to the local Euler factors (A.2 "fixed and moving phase
    cancellation") was **not checked**.
* **(A.1), (A.2), Gauss-Jacobi.** Already checked in [OAI-num] (K1-K4: Gamma_q evaluation, G and
  R mod 36, G(p^3) = gamma_3(p), R(p,p) = chi_p(-1), sextic reciprocity including nonsquarefree
  arguments) and in the w5copg branch (gamma_2^3 = -alpha and the related identities). Not
  repeated.
* **(A.4) and the restored summand.** Read at 300 dpi. They agree symbol by symbol, overbars
  included, with the OpenAI table (7.6), (7.7), (7.10), (7.11), (7.12):
  - a_p = conj(alpha)^3 eta^3, b_p = conj(alpha)^2 eta^2 conj(chi_p(4));
  - (a_p conj(gamma_3))^l;
  - D = eta conj(chi_p(u)) Q^{-x};
  - the J_j column.

  [OAI-num] L1-L5 checked that table, by brute force in O/p^t and in sympy. [K]'s (6) has the
  matching denominator L^S(x, eta conj(psi_u)).
* **(8).** Derived from the j = 0 line of (A.4) at (x, w, z) = (s, 1, 1/6), u = 1 (rho = 1,
  V = W = t = Q^{-1}). Both H_p = (8) and [K]'s intermediate full factor
  P_p = (1+t)/(1-t) + (1+t)(R-D)/(1-R) hold identically. **F7, EXACT (sympy).**

## 4. What this does and does not establish

* It establishes that the reflection formula of Lemma 3 is correctly derived from published,
  unconditional inputs (Patterson's cubic theta function as tabulated by DR). It also establishes
  that every finite identity in that derivation holds on the tested ranges.
* All numerical checks are finite. The T/F floating checks are ordinary double precision and are
  **not certified**. They test identities whose proofs are given in [K] and were re-derived by
  hand here; they are not evidence for any infinite statement.
* Not done:
  - an end-to-end numerical evaluation of (12) for a concrete completed row. This needs L ~ 36,
    q_L ~ 1300 cusps and large q_{c_cusp}, and is too heavy for this budget;
  - App. A.2 phase cancellation;
  - App. A absolute-convergence majorants (read only);
  - Lemma 4 beyond [R1];
  - DR's and Patterson's derivations themselves, which were trusted and then numerically
    corroborated by T1 and T2.
* Combined with [R1], the low-bound chain (Lemma 3, then Lemma 4, then (14) and Sec. 3.3) now has
  no step that was read and found wrong. It still has these unexecuted or partial items:
  - the end-to-end evaluation of (12) above;
  - (14) and Sec. 3.3, which [R1] checked only at the level of exponents;
  - the GL large-sieve application, which [R1] checked against GL's hypotheses but did not
    re-prove.

  The high-bound identity (5)-(6) still has App. A.2 unverified. The density input still
  carries the citation repair noted in [R1].
