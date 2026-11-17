# C2-countermodel-zoo: independent skeptic review

```text
Status:       SKEPTIC REVIEW of an EXPLORATORY campaign (Riemann Observatory). RH is open. Nothing in this
              review or in the reviewed campaign proves or disproves RH.
Scope:        All 33 investigator claims C2-00 ... C2-32 (REPORT.md, code under
              experiments/code/C2-countermodel-zoo/, outputs under experiments/results/C2-countermodel-zoo/).
Exact sources / dependencies:
              Independent replay code: experiments/code/C2-countermodel-zoo/skeptic/*.py
              Outputs: experiments/results/C2-countermodel-zoo/skeptic/*.json (SHA256SUMS in that folder).
              Python 3.13, python-flint 0.9.0 (Arb), mpmath 1.3.0, numpy 2.5.3, scipy 1.18.1, sympy 1.14.0.
              The Li replay uses the 100000 certified zeta ordinates in the session scratchpad
              (zeros_1_50000.tsv, zeros_50001_100000.tsv, 100000 lines checked).
What was actually run: see section 4 (16 scripts, about 75 CPU-minutes, at most 2 cores, no single run
              over 15 min).
Smallest remaining gap: listed per claim. The protocol's stated blind spot (C2-00(i), C2-31) is wrong
              as written. See finding F1.
```

The investigator's input hashes in `experiments/results/C2-countermodel-zoo/SHA256SUMS` were re-verified: all 12 files match.

Independence. Wherever possible I re-implemented the computation instead of re-running the investigator's scripts. The changes were:

- a different zero certificate: a rigorous argument principle in Arb instead of the Krawczyk test;
- different evaluation routes:
  - the L-function form of Davenport-Heilbronn instead of the Hurwitz form;
  - the Chowla-Selberg K-Bessel expansion and the Riemann theta integral for Epstein, instead of genus theory;
  - heat-flow convolution of xi for H_t, instead of the Phi-integral;
  - Polya moments of Phi, and theta moments, for Taylor coefficients, instead of Arb power series;
- exact Li sums with no interpolation.

## 1. Main findings

**F1. A countermodel family is missing, and the stated "blind spot" is wrong.** This affects C2-00(i), C2-25 and C2-31. Let

    F_c(s) = zeta(s) (1 + c 2^{-s} + 2*4^{-s}) = zeta(s) (1 + a 2^{-s}) (1 + b 2^{-s}),   ab = 2, a + b = c > 0.

The properties of F_c are elementary. They were checked in `skeptic/sk_local_factor.py`, where the functional-equation defect is below 3e-30 and |F| < 3e-31 at the predicted zeros.

- F_c is an ordinary Dirichlet series over N, with a_1 = 1 and real, nonnegative, multiplicative coefficients.
- It has an Euler product over the rational primes. The factor at p = 2 is D_c(s)/(1-2^{-s}), and the factor at odd p is (1-p^{-s})^{-1}.
- It has a simple pole at s = 1 and order 1.
- It satisfies a self-dual degree-1 functional equation with Gamma_R(s) and conductor 4. This is because 2^s D_c(s) = 2^s + c + 2^{1-s} is symmetric under s -> 1-s.
- Its zeros include the full vertical progressions Re s = log_2 a and Re s = 1 - log_2 a:
  - for c = 3 (integer coefficients 1, 3, 2), they lie on Re s = 0 and Re s = 1;
  - for c = 2(2^{-1/4} + 2^{-3/4}), they lie on Re s = 1/4 and 3/4, strictly inside the strip. Examples are 0.25 + 4.532i and 0.75 + 4.532i.

So F_c is RH-false while having every property that C2-00(i) says no known RH-false function has: an ordinary Dirichlet series over N, an Euler product over the rational primes, and a self-dual functional equation. C2-00(i) adds that such a function "would be a counterexample to GRH for the Selberg class". That is false. F_c lies outside the Selberg class only because its local factor at 2 has |alpha| = 2^{3/4} (resp. 2) > 1, which violates the Euler-product axiom b(p^k) << p^{k theta} with theta < 1/2. Ramanujan a_n << n^eps still holds, since a_n <= 6.

Consequences:

- The protocol must add "the Selberg-class local condition (theta < 1/2, or |alpha_p| <= 1)" as an input that every valid proof must use. "Uses the Euler product" alone is not enough.
- The blind spot is the full Selberg class, not "Euler product + FE + Dirichlet series".
- Every member of this family has Lambda_F(2^k) < 0 for some k. For example, F_3 has Lambda(4) = -4 log 2. So von Mangoldt positivity does exclude the family, and the matrix's "explicit formula" column should record this.

This construction is folklore for the extended Selberg class (Kaczorowski-Perelli). I did not locate a specific citation, so I do not claim it is new.

**F2. The "uniform in d" Jensen statement for xi~ is conditional on RH.** This affects C2-17 and C2-28. Craven-Csordas-Smith (zbMATH 0625.30036, review read) applies to real entire functions of order < 2 with finitely many non-real zeros. The non-real zeros of F~(X) are X0 and conj X0, together with the images of any off-line zeros of zeta. So "F~ has exactly two non-real zeros" holds iff RH holds. The conclusion "J^{d,n} is hyperbolic for all d once n >= n0" for xi~ is therefore CONDITIONAL (on RH, or at least on finitely many off-line zeta zeros). It is not THEOREM.

The existential statement "some RH-false function has the (non-uniform) GORZ property" is still unconditionally true, by a case split. If RH is false, zeta itself is such a function, since GORZ proved the property for it unconditionally. If RH is true, xi~ works.

Repair: replace xi by an unconditionally Laguerre-Polya base, for example H_{0.2}. H_t has only real zeros for t >= Lambda, and Lambda <= 0.2 (Polymath 15). Then H_{0.2}(sqrt X)(X - X0)(X - conj X0) has exactly two non-real zeros unconditionally.

**F3. The Li-coefficient table in C2-16 is numerically wrong (the identity is fine).** I recomputed lambda_n(xi) exactly for every n, from the same 100000 zeros and the same smooth tail (`skeptic/sk_li.py`). The investigator's code instead interpolates lambda_n(xi) linearly on a 60-point geometric grid and scans n with stride n//2000. The first n with lambda_n(xi~) < 0 is:

| (beta, gamma0) | claimed | recomputed | note |
|---|---|---|---|
| (0.6, 14) | 20857 | **20855** | lambda_n(xi~) > 0 for n <= 20854, not for n <= 20856 as C2-28 states |
| (0.75, 14) | 7395 | **7477** | at n = 7395 the exact value is **+1.88**; the interpolated value is -2.17 |
| (0.6, 30) | 112929 | **112538** | |
| (0.75, 30) | 41098 | **40908** | |

The quoted scales "980, 393, 4501, 1801, 11905, 50000" are half of what both the code and the stated formula (1/2)log(...) give: 1962.6, 785.2, 9002.6, 3601.2, 23808 and 100003. The code's JSON has the right values, and these equal gamma0^2/delta to within 0.2%, consistent with the "T^2/delta" conclusion. All of this remains NUMERICAL-NONRIGOROUS. The margin at n = 7395 is thin (7.6e-5 relative). The estimated smooth-tail model error is about 0.02.

**F4. Epstein zeros with Re s > 1 occur much lower than "3.6e6".** This affects C2-10, C2-30 (SP-8) and matrix row M2. I rigorously certified zeros of Z_{x^2+5y^2} with Re s > 1 in six further squares, each of half-width 1e-3 and with left edge > 1:

| t | sigma | runtime |
|---|---|---|
| 1193.94640 | 1.0110493 | 0.7 s |
| 4108.10828 | 1.0150707 | 1.4 s |
| 148065.8475 | 1.0045451 | 37 s |
| 272795.9566 | 1.0323639 | 64 s |
| 506416.4994 | 1.0115418 | 119 s |
| 939506.1826 | 1.0145417 | 227 s |

The method is the Taylor-form argument principle with winding number 1 (`skeptic/sk_ep_cert.py`, `sk_ep_cert.json`). The four candidates at 1.48e5 to 9.4e5 already appear in the investigator's own screen log, but were never polished. The two lowest were found by my screen (`sk_ep_low.py`, NUMERICAL-NONRIGOROUS screen, then a rigorous certificate).

SP-8's "Epstein zeros with sigma>1 were first found near 3.6e6" is therefore misleading. The lowest certified zero with sigma > 1 is at t ~ 1194. That it is the lowest is only screen evidence for t <= 4200. The investigator's three high zeros are not wrong: I independently re-certified the one at 3587891.15067 (858 s).

**F5. The C2-14 premise is a published theorem.** This affects C2-14 and C2-29. The zbMATH review of Csordas-Varga, Constr. Approx. 4 (1988), Zbl 0696.30007, states: "Of primary importance is the result that log Phi(sqrt t) is strictly concave on 0 < t < infinity." The premise of C2-14 is therefore a theorem. The investigator lists this paper as "searched", yet calls the premise "checked numerically only" and leaves it as an open question.

C2-14 and the Turan part of SP-6 become THEOREM, given IMPORTED Csordas-Varga 1988 and the moment lemma. One caveat remains. For m = 1 the moment lemma is needed at p = -1/2, so the source must cover p in (-1, inf). Borell 1973 / Karlin-Proschan-Barlow were not opened. A numerical stress test with 400 random log-concave functions found no violation; the minimum ratio was 1.032.

**F6. Completeness is now rigorous, which upgrades C2-04 and C2-09.** I counted all zeros in a box by a rigorous argument principle and compared with Arb-certified sign changes on the critical line (`sk_dh_count.py`, `sk_ep_count.py`). Off-line zeros come in pairs (rho, 1 - conj rho). With the investigator's certified zeros, the count closes exactly:

- Davenport-Heilbronn, box [-0.6, 1.6] x [1, 300]: N_box = 214, sign changes = 204, difference 10 = 2 x 5.
- Epstein x^2+5y^2, box [-0.7, 1.7] x [1, 200]: N_box = 253, sign changes = 183, difference 70 = 2 x 35.

The boxes contain every zero in their t-range, by the right edges C2-05 and C2-11 and the functional equation. So for 1 <= t <= 300 (DH) and 1 <= t <= 200 (Epstein) the off-line zeros are exactly the certified ones, including the strip 1/2 < sigma < 0.52 that the investigator did not cover. All other zeros are simple and lie on the line.

Boxes with |t| <= 1 contain no zeros (`sk_lowbox.json`). Hence 85.70 (DH) and 15.67 (Epstein) are rigorously the lowest off-line zeros.

**F7. Side finding on the prior art cited in C2-12 (Betermin-Samaj-Travenec, arXiv:2110.09368).** I read their abstract, section 1 and section 4 at L1. Their Conjecture 1.1 says that the unique solution of zeta2(1/2, Delta) = 0 on (0,1) is exactly Delta = e^gamma/(4 pi). This is false by an exponentially small amount.

Chowla-Selberg at s = 1/2 gives, exactly,

    Z_{x^2+k^2y^2}(1/2) = 2 gamma + 2 log(k/(4 pi)) + 8 sum_{N>=1} d(N) K_0(2 pi N k).

At k = 4 pi e^{-gamma} this equals 8 sum d(N) K_0(...) = 8.3917e-20 > 0. Two independent evaluations agree: the closed form and Riemann's theta integral (`sk_bst_threshold.py`). The true threshold is Delta*_c = 0.141733239663887191395..., against e^gamma/(4 pi) = 0.141733239663887191389.... They differ in the 21st decimal, a relative gap of 4.2e-20. BST report agreement to "at least 22 decimal digits".

The same formula and the monotonicity of the left side in k >= 1 show that "real off-line zeros exist for every k > 4 pi e^{-gamma}" is a THEOREM for rectangular forms. It is not "NN/CONJ" as matrix row M2b says. The exact threshold equation is probably already in Bateman-Grosswald 1964, which was not accessed. Prior-art search for this side finding was limited to the arXiv API and found no follow-up.

## 2. Per-claim verdicts (summary)

| id | verdict | key independent evidence |
|---|---|---|
| C2-00 | upheld with corrections | (i) refuted by F1; (ii) now rigorous for DH t<=300 and Epstein t<=200 (F6); (iii) premise is a theorem (F5) |
| C2-01 | upheld | proof re-derived (Brouwer existence; uniqueness via 0 in conv f'(D) inside B) |
| C2-02 | upheld | L-form chi values, coefficients and FE replayed (Arb + mpmath; FE defect < 2e-29 at 4 random points) |
| C2-03 | upheld | all 5 zeros re-certified with a rigorous winding number (L-form, squares of half-width 0.01, left edges >= 0.564) |
| C2-04 | upheld (upgraded to rigorous) | count 214 = 204 + 2x5 |
| C2-05 | upheld | independent sieve and tail: S_upper(1.13514) = 2.5502 < 2.5880, S_lower(1.11464) = 2.5915 |
| C2-06 | upheld | min |f| on sigma=1, t<=4000 replayed: 0.1839 at t = 240.4 (grid 0.04; sigma=1.05 not replayed) |
| C2-07 | upheld | Liu-Wu read (L1); independent witness = my rigorous winding certificates |
| C2-08 | upheld | Chowla-Selberg vs genus formulas at complex s: relative agreement 1e-40 |
| C2-09 | upheld (completeness upgraded) | count 253 = 183 + 2x35; 4 zeros replayed via Chowla-Selberg |
| C2-10 | upheld with corrections | 3.6e6 zero re-certified; much lower zeros with sigma>1 exist (F4) |
| C2-11 | upheld | S_upper(1.17816) = 2.9079 < pi with P = 1e8 |
| C2-12 | upheld | Chowla-Selberg replay: Z(1/2), Z(0.99) to 20 digits; root inside the enclosure; prior-art note F7 |
| C2-13 | upheld | heat-flow convolution of xi: both zeros reproduced to 18 digits, winding 1 |
| C2-14 | upheld with corrections | premise = Csordas-Varga 1988 theorem (F5) |
| C2-15 | upheld | elementary, re-derived |
| C2-16 | upheld with corrections | table wrong (F3) |
| C2-17 | downgraded | CCS part conditional on RH (F2); numerics replayed |
| C2-18 | upheld (Epstein part replayed; DH part not checked) | theta-moment coefficients: Turan k<=80, all J^{d,n} with d,n<=40 hyperbolic |
| C2-19 | upheld | Broucke-Debruyne-Vindas 2004.11501 p.1 and Broucke 2507.13780 sect. 4 read |
| C2-20 | upheld | zbMATH 1121.11061 abstract; BDR 2309.01567 Thms 1.1 and 1.3 read |
| C2-21 | upheld | proof re-derived; Mellin identity by x-domain quadrature (<= 6e-13); A replayed |
| C2-22 | upheld | Newton-step screen to 2e6 finds only this zero; rigorous winding certificate |
| C2-23 | upheld | standard results (reviewer knowledge; sources not opened) |
| C2-24 | upheld | elementary logic |
| C2-25 | upheld with corrections | S1 does not imply RH, correct; Epstein clause ill-formed; "must use the Euler product" overstated (F1) |
| C2-26 | upheld with corrections | BDR Thm 1.3 boundary confirmed; "must use" overstated |
| C2-27 | upheld with corrections | Ihara: poles and lambda = q^s + q^{1-s}, not s(1-s); Selberg: trivial zeros and s = 1 |
| C2-28 | downgraded | uniform-in-d conditional (F2); Li range should be n <= 20854 (F3) |
| C2-29 | upheld with corrections | Turan part unconditional (F5) |
| C2-30 | upheld with corrections | SP-8 Epstein sigma>1 height wrong (F4); "decides" should be "establishes" |
| C2-31 | downgraded | hitting-set conclusion is a non sequitur; blind-spot sentence refuted by F1 |
| C2-32 | upheld | crosscheck_mpmath.json read: max ratio 3.03e-15 (zeta_19) |

## 3. Details by claim

**C2-01 (Krawczyk).** I re-derived the proof.

- For z in D, f(z) = f(z0) + (z - z0)A_z with A_z = int_0^1 f'(z0 + u(z - z0)) du. Then A_z lies in conv f'(D), which is inside the rectangle B.
- So g(z) = z - Y f(z) lies in K, and Brouwer gives a fixed point.
- Y = 0 would give K = D, which is not inside int D.
- Uniqueness: two zeros force 0 in B, so 1 lies in 1 - YB, and K would contain a translate of D.

The code matches the theorem. The ball is acb(arb(x, r), arb(y, r)), the "off-line" test is a certified Arb comparison, and the refinement squares only shrink the enclosure. No issue found.

**C2-02 / C2-03 (DH zeros).**

- python-flint dirichlet_char(5,2) has values (1, i, -i, -1), which I checked.
- The L-form reproduces a_n = (1, kappa, -kappa, -1).
- All five zeros were re-certified by the rigorous argument principle on [x-0.01, x+0.01] x [y-0.01, y+0.01], with winding [1 +- 3e-15] (`sk_dh.json`, 3.2 s).
- The Spira comparison was reproduced from the JSON.

**C2-04.** See F6. Status: NUMERICAL-RIGOROUS for 1 <= t <= 300 and the whole half-strip sigma > 1/2. This relies on the investigator's 5 Krawczyk certificates and my count.

**C2-05.** The proof was checked line by line:

- f = 0 iff R = -(1+i kappa)/(1-i kappa) = e^{i(pi + 2 alpha)};
- the local factors are correct;
- the Mobius disc has centre (1+r^2)/(1-r^2), radius 2r/(1-r^2) and maximum argument 2 arctan r;
- target pi - 2 alpha = 2.588018;
- the partial-summation tail with Rosser-Schoenfeld is valid (the mod-5 restriction is not used, which is conservative).

My independent recomputation (`sk_edges.py`) gives S_upper(1.13514) = 2.55020. Even the root of S_upper with P = 1e8 is 1.13086, so the stated edge is valid but not optimal.

Additional remark. The maximal-argument configuration u = +-i r has |factor| = 1 exactly. By Kronecker/Bohr, the supremum of Re rho is therefore exactly the root of S(sigma) = pi - 2 alpha. That root lies in [1.11464, 1.13086] rigorously and is about 1.1204 by the PNT heuristic. This is presumably the Bombieri-Ghosh "solution of a certain equation" (zbMATH 1247.11116, sect. 5-6, review read).

**C2-06.** Replayed on sigma = 1 only (`sk_dh_sigma1.py`): min |f| = 0.18393 at t ~ 240.40, followed by 0.1852 at 2442.5 and 0.1892 at 3059.5. The sigma = 1.05 value was not replayed. The heuristic is fine as a heuristic. Note that "needs at least 20 primes to align" is a lower bound on the number of contributing primes; it does not mean that the first 20 primes specifically must align.

**C2-07 (Liu-Wu).** I read arXiv:2503.24275 (Thm 3.1, Thm 3.2, sect. IV). Their Thm 3.1 has two steps:

- it derives the strict inequality (8)/(9) from (7) after dividing by |f(1-s)|^2;
- it then evaluates (9) at a common zero, where that division is 0/0, to reach "0 > 0".

Their Table 1 then classifies certified zeros as "approximate zeros" because |f(s)|/|f(1-s)| differs from |X(s)| at numerically tiny values, which is again 0/0. The investigator's diagnosis is correct.

My winding-number certificates are a rigorous witness, produced by different code and a different method. A holomorphic function with winding number 1 on a contour has an actual zero inside. So the methodology sect. 6 requirement of an independent witness is now met. Classification: verified_error. The structured claim's "(also 2010.03521)" is supported: the 2020 abstract presents the same off-line "puzzles".

**C2-08.** See section 1 and `sk_epstein_cs.json`. The Chowla-Selberg expansion was derived here from Poisson summation in m. It matches 4 zeta beta for x^2+y^2 to 4e-41, and both genus formulas at s = 0.3+11.7i, 0.8+40.1i, 0.65+3.3i and 3 to <= 2.3e-40. This is much stronger than the investigator's single real point s = 3.

**C2-09.**

- Four zeros, including the lowest and t = 198.6, were replayed with Chowla-Selberg (|Z(mid)| ~ 1e-18 to 1e-19 with 21-digit midpoints, |Z| ~ 4e-6 at distance 1e-6).
- Completeness is rigorous (F6).
- The investigator's three uniqueness radii of 1e-5 are fine.

**C2-10.** See F4. The claim as stated (three certified zeros) is upheld. The surrounding narrative ("first found near 3.6e6"; matrix M2 "3 certified with sigma>1 at t~3.6e6-5.0e6") should list the lower zeros.

**C2-11.**

- Local factors re-derived: R's p-factor is ((1-p^-s)/(1+p^-s))^2 exactly for p = 3, 7 mod 20, it is (1-2^-s)/(1+2^-s) at p = 2, and it is trivial otherwise.
- Bound re-computed: S_upper(1.17816) = 2.9079 with P = 1e8 (the investigator used 2.9505 with P = 1e7).
- The necessary condition still holds at 1.12806. With P = 1e8 it holds up to at least 1.1302. The PNT-heuristic edge is about 1.1339.

**C2-12.** Upheld independently: Z_57(1/2) = 0.13543410369903428667 and Z_57(0.99) = -40.106266343797945279, both from Chowla-Selberg; the root 0.654651202577622799100319554317 lies inside the stated enclosure; the sign scan on (0,1) gives exactly two sign changes, at 0.35 and 0.655. For the prior art, see F7. Since sqrt 57 > 4 pi e^{-gamma} > k*, the existence of the real zero also follows from the theorem in F7.

**C2-13.**

- The heat-flow identity H_t(z) = (4 pi |t|)^{-1/2} int H_0(z-x) e^{-x^2/(4|t|)} dx (Fourier transform of e^{tu^2}, t < 0) was evaluated with mpmath's zeta.
- It reproduces both certified zeros to 18 digits and gives winding 1 on circles of radius 0.05 (`sk_dbn.json`, 200 s).
- The rigorous Arb tail bounds in dbn_Ht.py were checked by hand: (i) the n > 6 truncation, (ii) u > 1 by convexity of the exponent, and (iii) e^{tu^2} <= 1 for t <= 0. They are valid.

**C2-14.** See F5. The algebra checks: b_m = (1/2) int v^{m-1/2} Phi(sqrt v) e^{tv} dv, and Gamma(m+1/2)^2/(Gamma(m-1/2)Gamma(m+3/2)) = (2m-1)/(2m+1). Csordas-Norfolk-Varga 1988 (zbMATH 0663.65017) needed a different (Jensen-type) inequality to prove Lambda > -50. This fits the fact that all Turan inequalities hold for every t, which suggests the t < 0 extension is known to those authors. Not verified.

**C2-15.** Upheld. P(1-s) = P(s) because Q is invariant under rho -> 1-rho, and N(T) gains rho0 and 1 - conj rho0.

**C2-16.** The identity is upheld (log xi~ = log xi + log P, and Li's formula for a polynomial). The table: see F3.

**C2-17.** See F2. The numerics were replayed from an independent coefficient source: Polya moments b_m of Phi, giving xi(1/2+w) = 8 sum 4^m b_m w^{2m}/(2m)! (`sk_jensen.py`, mpmath dps 110, sympy Sturm counts).

- Turan holds for k = 1..80 for xi and for the quadruples (0.6,14), (0.9,5) and (0.6,5).
- J^{d,0} is hyperbolic for all d <= 40 for (0.6,14) and (0.6,5).
- For (0.9,5), J^{d,0} is hyperbolic for d <= 39 and has exactly 2 non-real roots at d = 40. So the smallest non-hyperbolic degree is exactly 40.
- The d <= 240 claims were not replayed.

Minor points. The "d,n <= 40" table actually stops at d + n <= 79. Also, odd_coeff_max_abs = 0.0 in synthetic_xi.json is float underflow, not exact zeros.

**C2-18.** The Epstein part was replayed from Riemann-theta moments (`sk_jensen_epstein.py`), with no L-functions. The check xi_Q(1/2) = 0.859144101273273233 agrees with C2-12's Z_Q(1/2) to 18 digits. The results match the investigator's: Turan holds for k = 1..80, and every J^{d,n} with d, n <= 40 and d + n <= 79 is hyperbolic (FLINT root isolation of 60-digit-rounded polynomials, NUMERICAL-NONRIGOROUS; 106 s). The DH part was not replayed.

**C2-19 / C2-20.** Upheld at the investigator's access level.

- BDV 2004.11501 p.1 confirms "given 1/2 < theta < 1 ... N(x) = rho x + O(x^theta) ... pi(x) = Li(x) + Omega_pm(x exp(-c sqrt log x))", with de la Vallee Poussin zero-free region realized.
- Broucke 2507.13780 sect. 4 confirms G(z) = 1 - (e^{-z} - e^{-2z})/z and log G = -int g x^{-z-1}, with g >= 0 supported on [e, inf).
- Zhang (zbMATH 1121.11061) is confirmed verbatim.
- BDR Thm 1.1 (any alpha in [0,1), beta in [1/2,1)) and Thm 1.3 (assuming RH: [1/2, beta] for beta < 1/2, and [alpha, beta] for 1/2 < alpha < 2/3, 2 alpha/(alpha+2) <= beta < 1/2) are confirmed.

One inconsistency: matrix row M5c restricts to beta in [1/2, alpha]. That is the RH-false range, which is right for that purpose, but it differs from C2-20's wording.

**C2-21.** I re-derived the proof:

- Frullani gives int_1^inf x^{-s}(1-1/x) dx/log x = log(s/(s-1));
- the cut part gives E1((s-rho)L);
- exp(-E1(w)) = e^gamma w e^{-Ein(w)};
- positivity holds for all x >= x0 because h(x) = 1 - 1/x - 2x^{beta-1} has h' > 0;
- (d): dN0 = delta_1 + dx, so N0(x) = x, and N(x) = x int_{[1,x]} y^{-1} dG(y) = G(1)x + O(x^sigma) for sigma > beta, because the signed measure G = exp*(m) has finite sigma-moment for sigma > beta.

Numerics replayed in `sk_beurling.json`. This is a continuous "Euler product" (zeta = exp int x^{-s} dPi). It is not a product over discrete primes, and the wording should say so.

**C2-22.** My screen used a Newton step delta = -F/F' at every grid point (dt = 0.05) on sigma = 1, for t <= 2e6. Unlike a |F| < 0.03 threshold, this cannot miss a zero within about 0.08 of the line. It finds exactly one zero with Re > 1, the stated one. That zero is certified by my winding method on a square with left edge 1.00055 (`sk_zeta19.json`). Platt-Trudgian Thm 1.1 was read (arXiv 1507.01340, L1). It confirms the cited statement, and its Table 1 points to Spira 1968 Table III and to van de Lune-te Riele for earlier N = 19 zeros.

**C2-23.** Standard results, not re-checked in sources. A phrasing nuance: every compact surface has the Selberg zeta zero s = 1 (from lambda_0 = 0) and topological trivial zeros. So "RH-false" must mean extra real zeros in (1/2, 1).

**C2-25.** Each item of S1 holds for DH, and Karatsuba 1990 gives the T(log T)^{1/2-eps} count. There are two problems:

1. The Epstein sentence "adding a_n >= 0, a pole, ... degree 2" is logically ill-formed. S1 contains "entire", "degree 1", "|a_n| <= 1" and "a_1 = 1", which Epstein violates (a_1 = r_Q(1) = 2, and r_Q is unbounded). The correct form is "replacing (entire, degree 1, |a_n| <= 1) by (pole, degree 2, 0 <= a_n << n^eps)".
2. "A valid proof must use multiplicativity / the Euler product" does not follow from the meta-lemma. A proof must use some property each witness lacks, and DH also lacks positivity, a pole and conductor 1. By F1, even the Euler product is not sufficient: the local theta < 1/2 condition (or Lambda_F >= 0, or conductor 1 with Hamburger) is needed as well.

**C2-26.** BDR's boundary is confirmed. "A valid proof must use a functional equation or the integrality of primes and integers" is a protocol heuristic, not a theorem. Another property the witnesses lack could also serve.

**C2-27.** The Ihara zeta "RH" concerns the poles of Z(u), with adjacency eigenvalues lambda = q^s + q^{1-s}, not s(1-s) = lambda. The Selberg zeta has non-spectral trivial zeros, so "zeros equal to spectrum" needs the word "nontrivial". The logic is otherwise fine.

**C2-28.** See F2 and F3. The structural part is CONDITIONAL. The Li range should be n <= 20854.

**C2-29.** Upheld. Rodgers-Tao gives that H_{-eps} has non-real zeros for every eps > 0. Phi > 0 holds (Polya). With F5 the Turan part needs no condition.

**C2-30.** SP-7 is upheld (Turan; Montgomery 1983; Platt-Trudgian). SP-8:

- "no finite zero census decides RH" should be "can establish RH", since a census can refute it;
- the heights 15.67 and 85.7 are now rigorously the lowest (F6);
- the zeta_19 height of 6.0e5 is the lowest with sigma > 1 up to 2e6 on screen evidence;
- the Epstein sigma > 1 height is wrong (F4).

SP-9 is upheld at the investigator's access level (Rezvyakova 2411.18492 abstract read).

**C2-31.** Downgraded from THEOREM to protocol heuristic. The matrix has 13 columns, and each member lacks several of them. For example, DH lacks multiplicativity, the Euler product, coefficient positivity and Lambda-positivity. So the hitting-set argument only shows that a proof must hit each member's set of missing properties. It does not show that a proof must use the Euler product. The sentence "the Selberg-class axioms contain all three, and no RH-false member satisfying them is known" conflates "has all three properties" with "is in the Selberg class". F1 refutes it.

**C2-32.** crosscheck_mpmath.json was read. The ratios are <= 3.03e-15 (zeta_19); DH is about 1e-22 and Epstein about 1e-23.

## 4. Computations run by the skeptic (code: experiments/code/C2-countermodel-zoo/skeptic/)

| script | purpose | runtime | output |
|---|---|---|---|
| sk_wind.py | rigorous argument principle (ball segments; Taylor-form variant) | library | |
| sk_dh.py | DH L-form checks and 5 winding certificates | 3 s | sk_dh.json |
| sk_dh_count.py | DH rigorous count, t <= 300 | 104 s | sk_dh_count_T300.json |
| sk_edges.py | DH and Epstein right edges, independent sieve to 1e8 | 13 s | sk_edges.json |
| sk_epstein_cs.py | Chowla-Selberg evaluation; genus formulas; C2-12 replay | 17 s | sk_epstein_cs.json |
| sk_ep_probe.py, sk_ep_newton.py, sk_ep_screen.py, sk_ep_low.py | Epstein sigma>1 screens (NN), printed only | <= 10 min each | in text above |
| sk_ep_cert.py | Taylor-form winding certificates for 7 Epstein zeros with Re > 1 | 0.7 s to 858 s | sk_ep_cert.json, *.log |
| sk_ep_count.py | Epstein rigorous count, t <= 200 | 99 s | sk_ep_count_T200.json |
| (inline) | boxes with abs(t) <= 1 | 20 s | sk_lowbox.json |
| sk_dh_sigma1.py | C2-06 replay (NN), printed only | about 9 min | in text above |
| sk_zeta19.py | zeta_19 Newton-step screen and certificate | 30 s | sk_zeta19.json |
| sk_dbn.py | H_t heat-flow replay (NN) | 200 s | sk_dbn.json |
| sk_li.py, sk_li_check.py, sk_li_margin.py | exact Li sums (NN) | 90 s + 60 s + 60 s | sk_li.json, sk_li_margin.json |
| sk_jensen.py | Turan/Jensen from Polya moments (NN) | 563 s | sk_jensen.json |
| sk_jensen_epstein.py | Turan/Jensen for xi_Q from theta moments (NN); the first sympy-Sturm version was killed at 15 min and replaced by FLINT root isolation | 106 s | sk_jensen_epstein.json |
| sk_bst_threshold.py | F7 | 5 s | sk_bst_threshold.json |
| sk_local_factor.py | F1 | 2 s | sk_local_factor.json |
| sk_beurling.py | C2-21 replay (NN) | 5 s | sk_beurling.json |

## 5. Negative knowledge from this review

- The ball-segment argument principle (Arb L-functions on a ball) is far too slow at t >= 1e5. At t ~ 1.5e5 it ran more than 12 minutes without finishing one square, because of Arb overestimation on balls of radius 1e-3 at large height. I replaced it with a Taylor (mean-value) form: f(c), f'(c) at points, plus one series bound on |f''| over the square. That form needs 32 point evaluations per square.
- My first heat-flow run integrated over a window centred at Re z instead of at 0, the centre of the Gaussian. This produced a spurious offset of 5e-7 in the t = -20 zero. It was corrected and rerun, and only the corrected output is kept.
- At t ~ 6e5, complex128 evaluation of zeta_19 has a residual floor of about 1e-10. A Newton acceptance threshold of 1e-10 silently rejected the true zero, and 1e-8 is needed.
- A heredoc script was accidentally created in the repository root by a backgrounded `cd`. It was moved into the skeptic folder; nothing outside the observatory was modified.
- The investigator's Li scan has two problems: linear interpolation of lambda_n(xi), and a stride of n//2000. Both produce wrong "first n" values, and the error can be a whole envelope period (about 88 in n for gamma0 = 14).

## 6. Recommended actions

1. Add a member M10 "zeta x self-reciprocal local factor" (F1) and rewrite C2-00(i) and C2-31.
2. Relabel C2-17 and C2-28 (structural part) as CONDITIONAL on RH, or rebase them on H_{0.2}.
3. Replace the C2-16 table and the C2-28 Li range with the recomputed values.
4. Update SP-8 and matrix row M2 with the sigma > 1 zeros at t ~ 1194, 4108, and so on.
5. Relabel C2-14 as THEOREM (Csordas-Varga 1988 plus the moment lemma), after confirming that the lemma's range includes p = -1/2.
6. Upgrade C2-04 and C2-09 completeness to NUMERICAL-RIGOROUS, citing the counts in F6.
7. Correct the M2b label ("THEOREM for rectangular forms; BST Conjecture 1.1 is false by 4e-20").
