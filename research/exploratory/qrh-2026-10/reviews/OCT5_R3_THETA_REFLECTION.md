# R3 review: cubic theta reflection in OpenAI, "The Quasi-Riemann Hypothesis" (Oct 5 2026, 11/12)

```text
Status: REVIEW (bounded; external manuscript)
Scope: paper2.tex lines 1632-2214 (Section sec:reflection: realization, theta transformation,
  Prop lem:reflection, Lemmas lem:reflection-uniformity, lem:theta-bounds, lem:quadratic,
  lem:squarefree-completed, proof of Prop prop:R) and lines 2874-3479 (App. app:fixed-ray).
  Outline cross-references: lines 351-424 (eq:intro-theta-coefficients, eq:intro-quadratic-twist).
Exact sources or dependencies:
  pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6; file
    standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex,
    sha256 d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d (3988 lines).
  Dunn-Radziwill, arXiv:2109.07463v3 (revised 14 May 2024): e-print (TeX, gz) sha256
    1373df1737fb6b70a82a452fdf37658893ab4112f8c000f49bbdd12286f87577; PDF sha256
    df888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0. Read: Sec. 1.2, 2, 5.1-5.3,
    Prop. 5.2 statement, Appendix A table. Equation numbers were taken from the PDF.
  Goldmakher-Louvel, arXiv:1112.1642, current e-print sha256
    12183c3c2d1ff5cdffb02f30664e0add43cbea91ee497df11dcbfad056ff4947: Definition 1, Thm 1.1, Cor 1.2
    (statements only).
  Repository: research/exploratory/qrh-2026-10/a2/eis.py (sha256 87ca11d9...2798e65), read before use.
What was actually run: the line-by-line reading below, and
  python3 -I reviews/oct5_r3_theta_checks.py OUT.json 22000 (31 s, one process; Python 3.13,
  numpy 2.5.3, scipy 1.18.1, mpmath 1.3.0, sympy 1.14.0). Script sha256
  504d84f340b31fd5866c548530d713c25227183c73df21d7f3d0e78669c3b16e. The JSON output (sha256
  2760e3dd...4ec98f) was written to the session scratchpad and is not committed; rerun to reproduce.
  Labels: EXACT = residue symbols as integer exponents; FLOAT = ordinary double precision (not
  directed, not certified); mpmath at 30 digits for the Mellin check.
Smallest remaining gap: no wrong step was found. The first steps that were not independently
  verified are: (i) lines 2112-2141, the use of Lemma lem:smooth (app:weights, line 3491) to separate
  the k_0-dependent weight. This is outside R3 and was not read. (ii) Inside R3, lines 3395-3418:
  the Phragmen-Lindelof and contour-shift justification was checked by reading only. (iii) Lines
  1903-1912: the GL hypotheses, including the claim that classes mod 24 fix the quadratic
  reciprocity factors. These were checked against the GL statement only; the GL proof was not read.
  No end-to-end numerical evaluation of both sides of eq:reflection was run (see Section 6).
```

RH remains unsolved. This review covers only the one new automorphic input of the 11/12 argument
(the completed mean square, Prop. prop:R). It does not check the reduction to zero-free regions
(Sec. 3), the Poisson step (Sec. 4), the cube-removal iteration (Sec. 5 and 7, the R2 scope), or
Lemma lem:arithmetic. A correct Prop. prop:R does not by itself establish the paper's theorem.

## 0. Verdict

| # | Item (paper2.tex lines) | Verdict | Evidence |
|---|---|---|---|
| 1 | Theta normalization eq:cubic-theta-definition (1650) vs DR (5.6)-(5.8) | **quoted correctly** (cosmetic: DR (5.6) is only sigma = 3^{5/2}/2; the expansion is the unnumbered display before it) | DR PDF p. 18; check A: theta(Ew)=theta(w) to 1e-17, theta(w+1)=theta(w); theta(w+omega)!=theta(w) (control) |
| 2 | Kubota multiplier convention kappa(g)=(c/a)_3, theta(gw)=kappa(g)theta(w) (3155-3158; DR (5.4), (5.11)) | **correct** | check A: 12 elements of Gamma_1(3) with (c/a)_3 != 1, error <= 1.7e-13; the conjugate convention fails by sqrt3 (FLOAT) |
| 3 | eq:intro-theta-coefficients (363): c_theta(nb^3) = 3^{5/2}\|b\| conj(chi_n(lambda)^2) gamma_2(n), incl. (n,b) != 1 | **correct** | derivation in Section 2; check G: 434 cases, rel. error <= 2.7e-15 |
| 4 | Lemma lem:theta-realization (1686-1718) | **correct** | read; finite Fourier identity, constant term cancels since phi(0)=0 |
| 5 | eq:ray-fourier (2992) | **correct** | check C: max error 5e-16, 14 primes, j=0..5 |
| 6 | Cusp reps gamma_0, gamma_+ = gamma_10, gamma_- = gamma_19 (1762, 3082-3084) and eq:cusp-fourier-coefficients (3108) | **quoted correctly** from DR (5.13), (5.14) and App. A table rows 10, 19 | check B: theta(gamma_10 w), theta(gamma_19 w) match the t_+, t_- series to 5e-15; swapped labels fail (0.05-0.32) |
| 7 | Reduction of theta(Hw) to theta(gamma_sigma w) with multiplier 1 (3076-3102) | **correct** | hand: H gamma_sigma^{-1} in SL_2(Z) Gamma_1(3) with trivial character; check F: 22 cases, <= 9e-15 |
| 8 | g_1 = gH^{-1} == I mod 3 and eq:ray-multiplier (3175-3200) | **correct** | hand (Section 3); check D: 700 random instances built with the paper's congruences (M = lambda^12), 700/700 agree EXACT; 445 of them discriminate kappa from conj kappa |
| 9 | Translate identity eq:theta-cusp-automorphy (3161) with the chosen g, H, sigma | **correct** | check E: 44 translates a/c with c = c_0 p (all three cases), max rel. error 1.1e-8; 31 have kappa != 1 and the conjugate fails by sqrt3 |
| 10 | eq:ray-additive-crt (3219); psi fixed by delta'_0 and r^{-1} mod D_0 | **correct** | hand (Section 3) |
| 11 | eq:ray-local-transform and omega_{p,j}, j = 0..5 (3232-3275); eq:theta-local-factors (1735) | **correct** | check C: 14 primes (12 split with N <= 43; inert 5, 11), j=0..5, random sigma_p, epsilon_p, all x mod p; max error 2.0e-14 |
| 12 | **B_{p,1} = chi_p^3 (quadratic)**; eq:intro-quadratic-twist (409), eq:residual-quadratic-factor (2002) | **correct** | exponent -j-2 from chi_p(h)^{-j} (Fourier) and chi_p(a)^{-2} (conj kappa); check C; corroborated by DR Prop. 5.2 (j=4 gives Ramanujan sums) |
| 13 | Archimedean part: eq:bessel-mellin, eq:ray-mellin, eq:theta-mellin-functional-equation, eq:dual-cusp-mellin-series, C = -i/81, gamma quotient and scale (2pi)^4/27 in eq:theta-weight (3284-3433) | **correct** | hand derivation (Section 4); check H (mpmath): Bessel-Mellin 4e-31, assembled scalar/scale 1e-16 |
| 14 | No Kubota pole: T(s,Psi) is entire (3355-3370, 3408) | **correct**; see Section 5 (coordinator question) | hand; DR Prop. 5.2 ("if l != 0 ... entire") |
| 15 | Contour shifts and Phragmen-Lindelof (3395-3418) | standard; **checked by reading only** | - |
| 16 | lem:theta-bounds support and coefficient bound (1859-1870, 3121-3135) | **correct** | hand from DR (5.7), (5.13), (5.14); equality at m = 3k-3 |
| 17 | lem:theta-bounds weight decay min(x^{1/4}, x^{-A}) (1873, 3452-3478) | **correct** | hand: first numerator pole at t = -5/6, Stirling |
| 18 | lem:reflection-uniformity (1847-1857, 3438-3450) | **correct** | hand (Section 3, item U) |
| 19 | lem:quadratic vs GL Thm 1.1 / Cor 1.2 (1886-1913) | **statement matches**; hypotheses plausible; GL proof not read | GL TeX read |
| 20 | lem:squarefree-completed bookkeeping (1923-2187) | **correct as far as read**; depends on Lemma lem:smooth and eq:integral-mean-square (not checked) | read line by line (Section 7) |
| 21 | Prop. prop:R from squarefree rows (2189-2214) | **correct** | read |

## 1. Citations against Dunn-Radziwill v3 (checklist item 1)

All equation numbers below were read from the v3 PDF. Its equations are numbered by section.

| paper2 cites | DR v3 content | status |
|---|---|---|
| [DR, Sec. 5.1, (5.6)] for theta (lines 362, 1647) | (5.6) is only sigma := 3^{5/2}/2. The Fourier expansion theta(w) = sigma v^{2/3} + sum tau(mu) v K_{1/3}(4 pi\|mu\|v) e-check(mu z) is the unnumbered display just before it. | content identical; pointer imprecise (cosmetic) |
| [DR (5.7)-(5.8)], Patterson Thm 8.1 (lines 368, 1660) | (5.7) the four-line formula for tau; (5.8) c,d == 1 mod 3, mu^2(c)=1 | correct |
| [DR (5.9), (5.15)] for cusp expansions (line 1768) | (5.9) F_j(w) := theta(gamma_j w); (5.15) F_j = sigma v^{2/3} + F_j^* for j <= 9, F_j^* for j >= 10 | correct (no constant term at gamma_10, gamma_19, as paper2 has) |
| [DR (5.13), (5.14)] tau_1, tau_2 (line 3105) | (5.13), (5.14) | correct; check B confirms numerically |
| gamma_0, gamma_+, gamma_- = gamma_1, gamma_10, gamma_19 (line 3036) | DR p. 18: gamma_10 = [[1,0],[omega,1]], gamma_19 = [[1,0],[omega^2,1]] | correct |
| t_- = omega^2 tau_1(omega^2 l) e-check(l), t_+ = omega tau_2(omega l) e-check(l) | App. A table: d_19 = omega^2 tau_1(omega^2 mu) e-check(mu), d_10 = omega tau_2(omega mu) e-check(mu) | correct |
| d_sigma(l) = conj t_sigma(-l) (eq:conjugate-cusp-coefficients) | DR (5.16): coefficient of conj F_j is conj d_j(-mu) | correct |
| Kubota character [DR (5.4), (5.6)] (line 3154) | (5.4) chi(gamma) = (c/a)_3; (5.5) the alternative (b/d)_3; (5.6) is sigma | (5.6) should be (5.5) or (5.11) (cosmetic) |
| supplementary law [DR (1.5)] (line 2936) | (1.5) (omega/d)_3 = omega^{alpha_2}, (lambda/d)_3 = omega^{-alpha_3} | correct |
| [DR, Corollary 5.1], [DR Lemma 5.4, Prop. 5.3], [DR Props. 5.1-5.2] | exist with matching content (twisted theta functional equation; Mellin/residue; Voronoi) | consistent |

The bibliography lists DR as Ann. of Math. 200 (2024) 967-1057. I did not check the journal
version; everything above refers to arXiv v3.

## 2. Realization by the cubic theta function (lines 1639-1718)

* **Coefficient formula (line 363).** The coefficient of conj theta at l is conj tau(-l) = conj tau(l),
  since tau is even. For l = lambda^{-3} n b^3 the fourth line of (5.7) applies (n = 0, sign +),
  giving 3^{5/2} \|b\| g~(n) with g~(n) = \|n\|^{-1} sum_x (x/n)_3 e-check(x/n). Moreover
  e(z) = e-check(z/lambda), and x -> lambda x gives gamma_2(n) = (lambda/n)_3 g~(n) =
  chi_n(lambda)^2 g~(n). Together these give the stated formula. Check G confirms it numerically,
  including b sharing primes with n.
* **eq:T-theta.** c_theta(nb^3) phi_k(nb^3) = 3^{5/2}\|b\| gamma_2(n) Psi_k(n) Psi_k(b)^3, using
  chi_{nb^3}(lambda)^2 = chi_n(lambda)^2. With V_*(y) = sqrt(y) W(y) the powers of N(b) match
  (\|b\|^3/\|b\|^2 = \|b\|). Correct.
* **eq:theta-twist-translates.** This is finite Fourier inversion. Multiplying the l-th mode by
  e(lambda^3 l h/q) = e-check(lambda^2 l h/q) is the translation z -> z + lambda^2 h/q. The constant
  terms cancel because sum_h phi^(h) = phi(0) = 0. Correct.

## 3. The theta transformation (lines 1722-1857; 2874-3275, 3438-3450)

**Finite Fourier step (2906-3025).** C_{p,j} in eq:ray-fourier is correct; check C confirms it
directly. Every additive character of O/q has the form e(hx/q), since the inverse different is
lambda^{-1}O. Active primes stay in the reduced denominator because v_p(lambda^2 h_p/p) = -1. So
c = c_0 r up to a unit. Correct.

**Matrices (3039-3075).** With q | c_0 the congruence a delta' == 1 mod q^{v_q(M c_0)} gives
v_q(b_g) >= v_q(M). With q | M, q not dividing c_0, delta' == 0 gives b_g == -c^{-1}. Hence:

* if 3 | c, then H = I and g == I mod 3 (a primary, delta' == a^{-1} == 1 mod 3);
* if v_lambda(c) = 1, then gH^{-1} = [[a - u_0 b_g, b_g],[c - u_0 delta', delta']] == I, using u_0 == c mod 3;
* if (c,lambda) = 1, then gH^{-1} = [[-b_g, a + u_0 b_g],[-delta', c + u_0 delta']] == I, using u_0 == a and c == 1 mod 3.

All three cases were also asserted in checks D and E.

**Cusp choice (3076-3102).**

* [[1,0],[lambda,1]] = [[1,0],[2+3omega,1]] gamma_19. The left factor is [[1,0],[2,1]][[1,0],[3omega,1]], which lies in SL_2(Z) Gamma_1(3) with trivial character.
* [[1,0],[-lambda,1]] is in Gamma_2 gamma_10.
* For H = T^{u_0}E, reduce u_0 mod Z+3O to {0, omega, -omega}. Then:
  * gamma_2 E gamma_19^{-1} = [[-1,-1],[1,0]] and gamma_3 E gamma_10^{-1} = [[0,-1],[1,0]], both in SL_2(Z);
  * so u_0 == omega gives sigma = "-" and u_0 == -omega gives sigma = "+".

The paper's sentence "translating by omega or -omega, then applying inversion" describes the matrix
product T^{u_0}E, which acts on w by inversion first. Only the wording is ambiguous; the labels are
right, and check F confirms them.

**Multiplier (3149-3200).** By hand:

* **3 | c.** (c/a)_3 = (c_0/a)_3 (r/a)_3 = (c_0/a)_3 (a/r)_3 by cubic reciprocity, since r and a are primary.
* **v_lambda(c) = 1.** a(c - u_0 delta') == -u_0 mod A, with A = a - u_0 b_g. Reciprocity gives
  (a/A)_3 = (A/a)_3 = (-u_0 b_g/a)_3 = ((u_0/c)/a)_3, using b_g c == -1 mod a. Hence
  kappa = (-u_0/A)_3 ((c_0/u_0)/a)_3 (a/r)_3, as stated.
* **(c,lambda) = 1.** kappa = (-delta'/-b_g)_3 = (delta'/-b_g)_3. With 1 - a delta' == 1 mod 9,
  (delta'/(-b_g c))_3 = 1, so kappa = conj (delta'/c)_3 = (a/c)_3 = (a/c_0)_3 (a/r)_3.

All residues other than (a/r)_3 are fixed by a mod M c_0 (since c_0 | L | M and h_p == 0 mod M^2)
and by the supplementary laws. So kappa = kappa_0 prod_{p|r} chi_p(a)^2. Check D confirms the
three-case formula EXACTLY on 700 instances (85, 261 and 354 in the three cases).

**Additive CRT (3219).** e-check(-delta' l/c) = e(-delta' lambda^4 l/(D_0 r)) with D_0 = lambda^3 c_0.
Partial fractions mod O give psi(lambda^4 l) = e(-delta'_0 r^{-1} lambda^4 l/D_0). The p-factor is
e(-delta'(lambda^3 c/p)^{-1} lambda^4 l/p). Since delta' == a^{-1} == (sigma_p h_p)^{-1} mod p, the
p-factor equals e(epsilon_p h_p^{-1} lambda^4 l/p). delta' mod D_0 is fixed by the congruences
(v_lambda(M) = 12 >= 3), and r^{-1} mod D_0 is fixed because D_0 | M^2. Correct.

**Local transform and the quadratic twist (checklist item 2).** For j != 0, 4 and h != 0:

C_{p,j}(h) chi_p(a)^{-2} = N(p)^{-1/2} chi_p(-1)^j gamma_j(p) chi_p(sigma_p)^{-2} chi_p(h)^{-j-2}.

Summing against e(epsilon_p h^{-1} x/p) gives
chi_p(sigma_p)^{-2} chi_p(-1)^j gamma_j gamma_{j+2} chi_p(epsilon_p)^{-j-2} chi_p(x)^{-j-2},
with zero extension at p | x. So B_{p,j} = chi_p^{-j-2}, and **B_{p,1} = chi_p^{-3} = chi_p^3 is
quadratic.**

* For j = 4 the character is trivial and gives the Ramanujan factor -1 + N(p) 1_{p|x}.
* For active j = 0 one gets N(p)^{-1/2} chi_p(x)^{-2}.

All six cases and omega_{p,j} hold EXACTLY in check C. The sign of the exponent is the load-bearing
point: with the conjugate multiplier convention, j = 1 would give chi_p^{+1} (sextic) and the
quadratic large sieve would not apply. Checks A, D and E show that the convention used,
theta(g w) = (c/a)_3 theta(w), is the one under which DR's tau, tau_1 and tau_2 define an automorphic
function. The convention is also independently consistent with DR Prop. 5.2: twisting g~(c) by
conj((c/r)_3) = chi_r^4 produces Ramanujan sums b_r^dagger and no character, which matches j = 4.

**Uniformity (item U; checklist item 3; 1847-1857, 3438-3450).** Every p | k_0 has j_p = 1 and
is active, so r = k_0 prod_{A_fix} p. Fixing k_0 mod M^2 (a modulus supported on S) fixes:

* r mod M^2, hence a mod M c_0 and the normalizing unit;
* H and sigma, hence d = d_sigma;
* kappa_0, delta'_0 and r^{-1} mod D_0, hence psi.

c_0 depends on h_0 only. The transformed weight V_*^sharp does not depend on k_0 at all. k_0 enters
only through the scale N(c)^2 = N(c_*)^2 N(k_0)^2, through the unimodular scalar C, and through
chi_{k_0}(.)^3. Correct as stated.

## 4. Archimedean part and the angular Grossencharacter (checklist item 4)

The factor conj alpha(nb^3) is not periodic, so it cannot be absorbed into phi. The paper produces
it with the operator d/d(z-bar) at z = 0 (3307-3343): each mode gains 2 pi i conj(l), and the
Bessel-Mellin integral removes \|l\|. For l = lambda^{-3} n b^3 one has
conj alpha(lambda^{-3}) = -i and \|l\|^{-2s} = 27^s N(n)^{-s} N(b)^{-3s}, which gives eq:ray-mellin
with constant 3^{5/2}/4 and (27/(2pi)^2)^s. This is DR's l = -1 operator (DR (5.43), Cor. 5.1),
used in the same way.

The change of variables (3347-3354), the factor -(cv)^{-2} with N(c)/c^2 = conj alpha(c)^2, and the
substitution v -> 1/(N(c)v) give eq:theta-mellin-functional-equation with -conj kappa conj alpha(c)^2
N(c)^{1-2s}. The dual series (3389) follows from d/dz. Composing everything with s = 1/2 - t gives:

* the scalar -i/(3^{5/2} 27^{1/2}) = -i/81;
* the gamma quotient Gamma(5/6+t)Gamma(7/6+t)/(Gamma(5/6-t)Gamma(7/6-t));
* the argument ((2pi)^4 N(l) X/(27 N(c)^2))^{-t}.

These match eq:theta-weight and eq:reflection. Check H recomputes the composition in mpmath and the
DLMF 10.43.19 integral. It also checks that the gamma quotient has modulus 1 on Re t = 0.

**V^sharp decay.** The numerator poles are at t = -5/6 - k and -7/6 - k, and 1/Gamma is entire.
Shifting to Re t = -1/4 gives x^{1/4}; shifting to Re t = A gives x^{-A}. Each x d/dx contributes a
factor -t. Stirling gives \|quotient\| ~ \|Im t\|^{4 Re t}, and that growth is absorbed by
integrating the Mellin transform of V_* by parts. eq:theta-weight-decay is correct, with constants
depending on ||V_*||_{C^J(I)}.

A remark, not an error: the decay begins only at x ~ (bandwidth of V_*^)^4/(2pi)^4·27. For a
compactly supported bump on [1,2] this is x ~ 10^4 or more. The bound is uniform because W is fixed
in Prop. prop:R. Any later use with varying W must carry the C^J norms, and the paper's statements
do carry them.

## 5. Coordinator question: where is the Patterson/Kubota residue cancelled?

Prop. prop:R (1317-1333) has no "+X" or X^{5/6}-type main term. That is justified as follows:
**T(s,Psi) is entire, and the reason is the d/d(z-bar) derivative.**

1. Theta_Psi has no constant term at infinity, since phi(0) = 0 (line 2978).
2. J(s) = int_0^infty d/d(z-bar) Theta_Psi(z,v)\|_{z=0} v^{2s-1} dv (3311-3314). For v -> 0, each
   translate is rewritten at its own cusp (3355-3368). By eq:theta-cusp-coordinates, at z = 0 we
   have d v'/d(z-bar) = 0 and d conj(z')/d(z-bar) = 0. So the chain rule leaves only
   -(cv)^{-2} d_{z'} F. The constant mode sigma v'^{2/3}, present at sigma = 0 cusps (and absent at
   gamma_10, gamma_19 by DR (5.15)), is therefore annihilated. The integrand decays like
   exp(-c/(N(c)v)) as v -> 0 and exponentially as v -> infty, so J is entire.
3. The pole would come from that constant mode. Without the derivative, the int v'^{2/3} v^{2s-1} dv
   piece with v' = 1/(N(c)v) is exactly the Kubota residue (the l = 0 case of DR Prop. 5.1/5.2). DR
   Prop. 5.2 states the same dichotomy: for l != 0 the completed series is entire, and only l = 0
   has the simple pole at 5/6. Here l = -1.
4. T(s,Psi) = J(s) / [(3^{5/2}/4)(27/(2pi)^2)^s Gamma(s+1/3)Gamma(s+2/3)] is entire, because 1/Gamma
   is entire. The b-factor L(3s - 1/2, conj alpha^3 Psi^3) involves a Grossencharacter of nontrivial
   infinity type, so cube completion introduces no zeta pole either. Line 3408 ("No poles are
   crossed") is therefore justified, and T(X;Psi) equals the dual sums with no residual term.
5. Empirical consistency (not evidence for the asymptotic claim): numerics/README.md, row P, found
   no X^{5/6} term in sum gamma_2(c) alpha(c)^k for k in {+-1, +-2, 3} up to X = 2·10^5, and found
   one for k = 0.

Conclusion: the absence of a main term is proved in the paper (3355-3370, 3408). It is correct by my
reading and consistent with DR. This is not a gap in Prop. prop:R. The cancellation needs the full
angular twist conj alpha(nb^3) = conj alpha(n) conj alpha(b)^3 exactly as in eq:T. A version of T
without conj alpha(n) would have the l = 0 pole.

## 6. Coefficient bounds, quadratic large sieve

* **eq:theta-support / eq:theta-coefficient-bound.** \|g(u lambda^2, c)\| = \|c\| for squarefree
  c == 1 mod 3.
  * For m = 3k-4: 3^{k/2+2} = 3^{m/6+8/3} <= 27·3^{m/6}.
  * For m = 3k-3: 3^{k/2+5/2} = 27·3^{m/6} (equality).
  * For m = -4: 9 <= 27·3^{-2/3} ≈ 12.98.
  * The actual support is m in {-4, -3, -1, 0, 2, 3, ...}; "m >= -4" is a valid superset.
* **lem:quadratic.** GL Thm 1.1 (TeX read) gives the bound
  sum*_{N a <= M} \| sum*_{N b <= N} lambda_b chi_b(a) \|^2 << (MN)^eps (M+N) sum \|lambda_b\|^2
  for a quadratic Hecke family with respect to c. paper2 puts the family index outside. The bound is
  symmetric, so transposition suffices.
  * The modified character x -> (x/k)_2 kappa_lambda(x)^{e_k} is trivial on units: (omega/k)_2 = 1,
    (-1/k)_2 = (-1)^{e_k} and kappa_lambda(-1) = -1. It equals (x/k)_2 on primary x and has
    conductor k lambda^{e_k}.
  * In one class, e_{k_1} = e_{k_2}, so the product character has conductor k_1 k_2 (GL property 3).
  * Reciprocity with a class function (GL property 2) is the cube of sextic reciprocity, since
    R^3 = R. Sextic reciprocity was verified numerically in numerics/README.md K4, but not here.
  * The S-part n_S of n contributes chi_k(n_S)^3, which is constant on fixed classes of k.
  * Verdict: statement-level match. GL's proof was not read.

**Why no end-to-end numerical test of eq:reflection.** I attempted to size one: a toy with
S = {lambda}, L = 9, P = {p} and N(p) = 7. It is dominated by translates with N(c) = 63. Because
V^sharp decays only beyond the bandwidth^4 scale noted in Section 4, the dual sum would need
N(lambda^4 l) up to about 10^6 for any smooth weight that keeps the primal side short. That was out
of budget. All factors were checked separately instead: translate identity (E), local assembly (C,
D), Mellin bookkeeping (H). The only unchecked link between them is the standard contour argument.

## 7. Squarefree rows and Prop. prop:R (lines 1915-2214)

Checked by reading.

* **eq:theta-row-twist.** j_p == v_p(k) + 4 v_p(g) mod 6. The fourth power at g carries no
  reciprocity sign because R^4 = 1. Psi_0 contains R(n, prod p^{v_p(k)}), which is fixed on ray
  classes.
* **eq:residual-quadratic-factor.** chi_p(n b^3)^3 = chi_p(nb)^3, including zero extension.
* **Unique representation.** l = u lambda^m n b^3 is unique, since off lambda the exponents are
  0 or 1 mod 3. |A_{u,m}| <= 27, from the coefficient bound together with \|psi\| = \|alpha\| = 1.
* **j = 4 identity and reindexing (2036-2062).** -q^{-1/2} + q^{1/2} 1_{p|n} + q^{1/2} 1_{p∤n, p|b}.
  The substitutions n = pn', b = pb' give scales q^2 Y -> qY and Y/q with the stated q-powers.
* **Cost table (2066-2091).**
  * p | t, p not in S: then p | g, so j_p = 1 + 4v_p(g) is odd and the cost is N(p)^2.
  * p | g, p ∤ t: j_p = 0 needs v_p(g) >= 3 (cost N(p)); j_p = 4 has cost <= N(p); j_p = 2 needs
    v_p(g) >= 2 (cost N(p)^2).
  * Hence a^2 Y << H_0^2 N(t)^2 N(g)/X.
* **Dyadic sums.**
  * sum_{U,B} sqrt(U)(1 + UB^3/Z)^{-2} << sqrt(Z): sum over B <= Z^{1/3} of sqrt(Z) B^{-3/2}, plus
    Z^2 B^{-6} for larger B.
  * U <= 81 Y z_* since m >= -4.
  * The m-sum is geometric: 3^{-m/3} · 3^{-m/2}.
  * Triangle inequality in l^2(k_0) with pointwise bounded c_{iota,m}(k_0).
  * Final bound: H_0 + a^2 Y <= H + H^2 N(g)/X.
* **Not checked.** Lemma lem:smooth and eq:integral-mean-square (app:weights) are used at
  2112-2141. They belong to another scope.
* **Prop. prop:R.** k = u_0 s v^2 is unique with s squarefree. chi_n(v^2) = chi_n(v^8) gives
  T(X; u_0 s v^2, f) = T(X; u_0 s, f v^2), and N(g) <= H N(f) <= D^{2C_0}. Summing gives
  sum_v N(v)^{-2} = zeta_K(2). Correct.

## 8. Minor points (non-fatal)

1. Lines 362 and 1647: "(5.6)" should point at the unnumbered theta expansion in DR Sec. 5.1;
   (5.6) is only sigma. Line 3154: "(5.4), (5.6)" should read (5.4), (5.5) or (5.11).
2. Line 3099: "translating by omega or -omega, then applying inversion" means the matrix
   T^{±omega}E, which applies inversion first. The labels -, + are correct (check F).
3. lem:theta-bounds: m ranges over a proper subset of m >= -4, as described in Section 6.
4. Lines 1903-1910: "Classes modulo 24O fix the supplementary characters and reciprocity factors."
   This is plausible: R and G descend mod 4 (numerics K2'), and kappa_lambda is defined mod lambda.
   It was not re-verified here for the quadratic family.

## 9. Not done

* Patterson 1977 Thm 8.1 / Table III was not read. DR's transcription was tested for automorphy
  instead: E, T, 12 Gamma_1(3) elements, gamma_10, gamma_19, and 44 translates. These are finite
  floating checks, not a proof.
* GL's proof; Lemma lem:smooth; Sec. 3-5 and 7 of paper2 (other scopes).
* No end-to-end numerical evaluation of eq:reflection (see Section 6).
* The other review files in this directory written in parallel this session (for example
  KINTALI_LEMMA3_REVIEW.md) were not consulted. Kintali's App. B uses the same DR inputs, so
  checks A, B, E and F apply to those inputs as well, but not to his own algebra.

## Reproduction

```
cd research/exploratory/qrh-2026-10/reviews
python3 -I oct5_r3_theta_checks.py /path/to/out.json 22000     # ~31 s, single process
```

| check | what | result |
|---|---|---|
| gauss | prime Gauss sums (numpy) vs direct; composite via twisted multiplicativity vs direct; g~(p)^3 = -p/\|p\| | 1.6e-14; 8.1e-14 (65 composites); 1.2e-14 |
| G | eq:intro-theta-coefficients | 434 cases, 2.7e-15 |
| H | Bessel-Mellin; assembled scalar -i/81 and scale | 4e-31; 1e-16 |
| C | eq:ray-fourier; eq:ray-local-transform j=0..5; gamma_2^3 = -alpha; gamma_4 = conj gamma_2 | 5e-16; 2.0e-14; 4e-15; 1.2e-15 |
| D | eq:ray-multiplier vs (c_1/a_1)_3 | 700/700 EXACT |
| A | E-, T-, 3omega-invariance; Gamma_1(3) multiplier | 1e-17, 0, 4e-16; 1.7e-13 (conj: 1.73) |
| B | gamma_10, gamma_19 expansions | <= 5.3e-15 (swapped: >= 0.049) |
| F | H -> gamma_sigma | 22 cases, 9e-15 |
| E | translate identity, all three denominator cases | 44 cases, 1.1e-8 (conj kappa: 1.73) |
