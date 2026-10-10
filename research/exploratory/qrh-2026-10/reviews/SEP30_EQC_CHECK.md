# Sep 30 first-Poisson column coefficient, eq. (C): derivation and numerical replay

```text
Status: REVIEW (bounded; external, unreviewed manuscript). Closes item 1 of SEP30_INVMOMENT_REVIEW.md
  section 6. Verdict on eq. (C) (paper.tex 10279) and the identification at 10207-10245: VERIFIED,
  by hand derivation and by EMPIRICAL floating-point replay with exact residue symbols. No error,
  and no convention problem, was found. This is not a verdict on Lemma 17.2 or on Theorem 1.1.
Scope: paper.tex Section 17, proof of Lemma 17.2, first Poisson transformation, lines 10145-10295:
  eq:first-masked-data (10166), the masked Poisson root (10180-10186), the u_1-side factor list
  (10207-10225), the fixed-ray quotient G(u_1u_2^{-1})R(u_1u_2^{-1},P_T) (10227-10244), h~ = hf^2E and
  the exponent table (10246-10272), eq. (C) = eq:first-poisson-column (10279), and the m_1 = 1 case
  (10192-10202). Also eq:retained-cube-label (10316) and the slot-priority split used by (C).
  Not in scope: everything after 10295 (t'-inversion, Fourier separation, (D), second transform).
Exact sources or dependencies:
  [OAI] pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, standalone/2026-10-07-openai-quasi-riemann-
        import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex,
        SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed from git).
  Conventions used from [OAI]: 573-664 (primary generators, chi_c, gamma_j, alpha, e(z), zero
        extension), 843-1100 (Gamma, r, R, G, eq:signal, eq:G-quadratic-refinement, CRT for gamma_j),
        7285-7313 (a(n), Psi_k, product-form marks), 9722-9746 (Lemma 17.5), 9941-9997 (slot
        priority, block (A)). Lemma 17.5 itself is [O5] lem:poisson (R1 C4); its proof was re-read.
  Imported, not re-proved: cubic reciprocity (a/b)_3 = (b/a)_3 for coprime primary a, b ([OAI] cites
        DR eq. (1.4)); it is exercised numerically by A3 but not proved here.
  Reused code pattern: reviews/oct5_r1_checks.py (C6 replay design) and reviews/oct5_r2_iteration_
        check.py (part E symbol tables); neither was modified. a2/eis.py is imported only to
        cross-check the symbol tables (A0).
What was actually run: reviews/sep30_eqc_check.py (written for this note), as
  `nice -n 10 python3 -I sep30_eqc_check.py --out <scratch>/full.json` and with `--quick`.
  Script SHA-256 445f71c162c235940b0e48d49f6a6caae6554322935f46e172f0656cf50918c3.
  * Full run: 50/50 checks pass in about 63 s. Log SHA-256 a22a5d20...a722, JSON 27371c1b...dcca
    (scratch only). A second full run printed identical check lines.
  * Quick run: 46/46 checks pass.
  * An earlier version of the script failed 2/50: the replay controls in a degenerate third
    configuration, where E = 1 and the masks killed all but 36 tuples. That configuration was
    replaced by a non-degenerate one; no identity check ever failed.
  Residue symbols are exact integer tables. Gauss sums, Gamma, kernels and lattice sums are double
  precision: EMPIRICAL, not certified. Pointwise tolerance 1e-9 absolute (all compared values have
  modulus 0 or 1; observed max error 3e-15); replay tolerance 1e-9 relative.
Smallest remaining gap: (C) is now checked; it was the smallest unverified sub-claim inside the
  first Poisson transform. The next unverified arithmetic step is the mutual-gcd extension
  (10382-10398) and the factorization into B_{1,a}(t';y) P_a(y) (10481-10497). It is multiplicative
  bookkeeping and was read, not run. Outside Section 17, the Lemma 14.3 terminal branch outputs
  (target 1 of SEP30_VERIFICATION_MAP.md) remain the load-bearing unverified input.
```

RH remains unsolved. This note checks one arithmetic identity inside the proof of one lemma of an external manuscript that claims a fixed zero-free half-plane Re s > 7/8. The identity is correct, but that does not show the lemma, the 7/8 theorem, or anything about the critical line.

## 1. Verdict

**Verified.** Eq. (C) and the identification leading to it (10207-10245) are correct as written, with the manuscript's conventions:
* the primary generator m_1 = u_1u_2R_1 in e(x/m_1);
* the orientation chi_b(a) = R(a,b) chi_a(b);
* the second polynomial carried in conjugated form;
* nu_i read as nu times the Fourier modes of the displayed ray factor.

Three independent routes agree:
1. **A hand derivation (§3).** It reproduces every factor of (C) and also writes down the u-independent remainder, which the paper leaves undisplayed ("outer coefficients").
2. **A pointwise numerical identity (C1, C2).** Both sides were computed from the definitions on 900 random admissible tuples, 613 of them with nonzero value, and the maximum error was 3e-15. A second check (C2) does not use the explicit remainder at all: it shows that the remainder is independent of (u_1,u_2), over 6233 pairs in 12 outer families.
3. **An end-to-end replay of the first Poisson transform of block (A) at tiny scale (E).** The k-lattice sum agrees with the Poisson side written through (C) to relative error at most 2.5e-15. Measured against the h ≠ 0 (nonprincipal) part alone, which is 1.4e-4 to 5.7e-3 of the total, the error is at most 2.4e-12. This holds for 3 label configurations, each with a radial and a shifted Gaussian.

All 14 failing controls fail, and each has a minimal counterexample (§5). One further mutation was predicted to be harmless and is: the reciprocity orientation inside ξ, because the exponents there are even.

No error was found. Two remarks, neither of which is an error:
* **R1 (undisplayed remainder).** The u-independent factor (§3, step 7) depends on the frequency h through conj ψ_R(h), a character of h modulo R_1, which is built from moving primes of 𝔅. The paper's definition of e_σ (10520-10527) puts exactly these "finite Gauss, unit, reciprocity, and first-ray factors at the old outer ideals" into e_σ. They enter (D) only through |w_ω|, so this is harmless; its modulus is 0 or 1.
* **R2 (orientation-free ξ).** Every exponent of ξ is 0 or 4, so ξ(u) = Π χ_u(p)^{e_p} equals Π χ_p(u)^{e_p}: R(u,p)^4 = 1. The table therefore does not depend on the reciprocity orientation, but the u-side list before the table does (controls drop_RPT and drop_R12).

## 2. The statement, restated

Fix the raw data of block (A), eq:canonical-block (9984):
* f, a squarefree label;
* b_1, b_2, cube ideals, possibly with prime powers;
* n_1, n_2, squarefree columns;
* a(n) = ᾱ(n)γ_2(n)ν(n)ρ(n);
* the marks 𝔡.

Put 𝔅 = rad(b_1b_2), 𝔄_i = (n_i,𝔅), C = gcd(n_1/𝔄_1, n_2/𝔄_2) and u_i = n_i/(𝔄_iC). For p | 𝔅 define:
* a_ip = 1_{p|𝔄_i};
* π_p = v_p(b_1b_2) mod 2;
* t_p = a_1p − a_2p + 3π_p mod 6.

The derived data are:
* R_1 = Π_{t_p≠0} p and P_T = Π_{t_p≠0} p^{t_p};
* E = Π_{π_p=1} p^{a_1p+a_2p} and h~ = hf²E;
* ψ_1 = χ_{u_1} χ̄_{u_2} Π_{t_p≠0} χ_p^{t_p}, primitive modulo m_1 = u_1u_2R_1;
* ψ_R = Π_{t_p≠0} χ_p^{t_p}, modulo R_1;
* d_k | rad(C𝔅/R_1), the Lemma 17.5 divisor, and h ∈ 𝒪, the frequency.

Expanding the square and applying Lemma 17.5 to the k-sum produces, for each raw tuple, the product

  RAW = a(n_1) conj a(n_2) · χ_{n_1}(f)^4 conj χ_{n_2}(f)^4 · γ(ψ_1;m_1) ψ_1(d_k) conj ψ_1(h)

times the kernel, the β's, the marks and W's, and μ(d_k)/q_{d_k}. **The paper claims** (10207-10282) that

  RAW = Coef_1(u_1) · conj Coef_2(u_2) · G(u_1u_2^{-1}) R(u_1u_2^{-1}, P_T) · OUTER,

with:
* Coef_i(u) = μ(u)ν(u)ρ(u) conj χ_u(h~) χ_u(C)^4 χ_u(d_k) ξ(u), where ξ(u) = Π_{p|𝔅} χ_u(p)^{e_p} and e_p is the last column of the 8-row table (10262-10271);
* OUTER independent of u_1 and u_2.

Fourier expansion of the ray factor on the fixed ray group turns ν into ν_i. The slot-priority split turns the mark into 𝔡_i(u_i). The result is exactly (C).

## 3. Hand derivation

Each step names the script check that replays it.

1. **Masked data (B2).** For a prime p, χ_p^3 is real on units, so χ_{b_1}(k)^3 conj χ_{b_2}(k)^3 = Π_{p|𝔅} χ_p(k)^{3π_p}, with a zero at every p | 𝔅. Also χ_{n_1} conj χ_{n_2} = χ_{u_1} conj χ_{u_2} Π_{p|𝔅} χ_p^{a_1p−a_2p}, with zeros at C. Hence the k-character is ψ_1(k)·1_{(k, C𝔅/R_1)=1}. Every factor χ_p^{t_p} with t_p ≠ 0 is a nontrivial character of the residue field, so it is primitive, which gives eq:first-masked-data.
2. **Lemma 17.5 (E, and R1 C4 for Oct 5).** It gives the root (K γ(ψ_1;m_1)/√q_{m_1}) · μ(d_k)ψ_1(d_k)/q_{d_k} · conj ψ_1(h).
3. **CRT.** For pairwise coprime primary moduli, writing x = Σ (m/m_j) x_j gives γ(Πψ_j; Πm_j) = Π_j ψ_j(m/m_j) γ(ψ_j;m_j). Hence

   γ(ψ_1;m_1) = γ_1(u_1) χ_{u_1}(u_2R_1) · γ(χ̄_{u_2};u_2) χ̄_{u_2}(u_1R_1) · γ(ψ_R;R_1) ψ_R(u_1u_2).

4. **Sextic reciprocity (A3).** It gives χ_{u_1}(u_2) χ̄_{u_2}(u_1) = R(u_1,u_2). It also gives ψ_R(u_i) = Π χ_p(u_i)^{t_p} = R(u_i,P_T) χ_{u_i}(P_T), because R is a sign-valued bicharacter (A2). The root therefore factors as (C3)

   [γ_1(u_1) conj χ_{u_1}(h) χ_{u_1}(d_kR_1) χ_{u_1}(P_T)] R(u_1,P_T)
   × [γ(χ̄_{u_2};u_2) χ_{u_2}(h) conj χ_{u_2}(d_kR_1) χ_{u_2}(P_T)] R(u_2,P_T)
   × R(u_1,u_2) × [γ(ψ_R;R_1) ψ_R(d_k) conj ψ_R(h)].

   * The first bracket is the paper's u_1 list (10214-10222), up to the fixed-ray factor R(u_1,P_T).
   * The second bracket, conjugated, is the same list with t_p → −t_p (10222-10223).
   * The cross factor is R(u_1,u_2) (10223-10225).
5. **Columns (A6, C3).**
   * γ_2(n_i) = γ_2(𝔄_iC) γ_2(u_i) χ_{u_i}(𝔄_iC)^4. This is CRT with j = 2 plus χ_a(b)^2 = χ_b(a)^2, i.e. 10207-10212.
   * α, ν and ρ are multiplicative.
   * χ_{n_i}(f)^4 = χ_{𝔄_iC}(f)^4 χ_{u_i}(f)^4, and χ_u(f)^4 = conj χ_u(f²) including zeros (A8).
6. **Gauss signals (A4, A5, A7).**
   * Side 1: by eq:signal, ᾱ(u_1)γ_2(u_1)γ_1(u_1) = μ(u_1)G(u_1).
   * Side 2: γ(χ̄_u;u) = χ_u(−1) conj γ_1(u), so α(u_2) conj γ_2(u_2) γ(χ̄_{u_2};u_2) = μ(u_2)χ_{u_2}(−1) conj G(u_2). This is the paper's "raw second Gauss-signal factor", 10234-10236; G(u_2^{-1}) = χ_{u_2}(−1) conj G(u_2) is 10238-10239.
   * G(u^{-1}) = R(u,u) conj G(u) = χ_u(−1) conj G(u).
   * By eq:G-quadratic-refinement, G(u_1) χ_{u_2}(−1) conj G(u_2) R(u_1,u_2) = G(u_1u_2^{-1}).
   * R(u_1,P_T) R(u_2,P_T) = R(u_1u_2^{-1}, P_T).
7. **Local exponents at p | 𝔅 (B1).** Since u_i is prime to 𝔅, every χ_{u_i}(p) is a unit and the exponents add mod 6.
   * Side 1 collects 4a_1p from step 5, plus 1_{t≠0} from χ_{u_1}(R_1), plus t_p from χ_{u_1}(P_T). Moving conj χ_{u_1}(E) into h~ adds π_p(a_1p + a_2p).
   * Side 2, inside the conjugated polynomial, collects 4a_2p + 1_{t≠0}(1 − t_p) + π_p(a_1p + a_2p).
   * The table reduces both to e_p ∈ {0, 4}.

   What is left is independent of u_1 and u_2:

   OUTER = a(𝔄_1C) conj a(𝔄_2C) · χ_{𝔄_1C}(f)^4 conj χ_{𝔄_2C}(f)^4 · γ(ψ_R;R_1) ψ_R(d_k) conj ψ_R(h).

   This proves the claim of §2.
8. **Marks (C4).** Assign the slots first to b_i, 𝔄_i and C. Since u_i is prime to b_i𝔄_iC, each residual slot on u_i has its original coefficient, so the residual mark is a subcollection mark 𝔡_{I'}(u_i).
9. **Ray Fourier step (C5; 10240-10244).** The ray group of primary classes is (𝒪/4)^×, which has order 12. Its characters are χ_4^a 𝔯(·,y), for a ∈ ℤ/3 and y a square class. For each class of P_T, the function G(xy^{-1})R(xy^{-1},P_T) expands as Σ c θ_1(x) conj θ_2(y), with Σ|c| = 2 ≤ 12.

## 4. Numerical replay (sep30_eqc_check.py)

| part | what | size | result |
|---|---|---|---|
| A0 | symbol tables against the independent a2/eis.py | 3600 (p,u) | 0 mismatches |
| A1-A9 | Γ four-term formula against its definition; the 𝔯 table and bicharacter property; reciprocity on composite and prime-power pairs; G direct against the class function; eq:signal; G(vw); G(v^{-1}); χ_v(−1) = R(v,v); γ_2 CRT; γ(χ̄_u;u); χ_u(f)^4; the test twists | 280 to 3000 cases each | max err ≤ 3.2e-15 |
| B1-B4 | the table; eq:first-masked-data; m_1 = 1 ⇔ (n_1 = n_2 and b_1b_2 = □); eq:retained-cube-label | 12000 (tuple,k); 5184 combinations; 7500 (tuple,n) | exact / 1.4e-15 |
| C1 | RAW = CLAIM with the explicit OUTER | 900 tuples (613 nonzero, 287 zero on both sides) | 3.0e-15 |
| C2 | u-independence, no OUTER used | 6233 (u_1,u_2) pairs, 12 families | spread 3.3e-15 |
| C3 | intermediate u_1/u_2 lists, cross factor, a(n) split | 400 tuples | 3.1e-15 |
| C4 | mark split | 1200 sides | 0 |
| C5 | ray Fourier expansion | 4 classes of P_T | 8.7e-16 |
| D | 14 failing controls + 1 predicted-insensitive | 613 nonzero tuples | §5 |
| E | first-Poisson replay of block (A), 3 configs × {radial, shifted} Φ | 26244 raw tuples; about 4.35·10^5 k-points per run; 6 runs | rel err ≤ 2.5e-15; ≤ 2.4e-12 of the h ≠ 0 part |

**C1 coverage (nonzero tuples):**
* all 8 table rows;
* composite u_i (103 tuples);
* prime powers v_p(b_i) ≥ 2, up to 3 (441);
* inert primes of norm 25 and 121 (116);
* C ≠ 1 (231), d_k ≠ 1 (220), R_1 ≠ 1 (414), m_1 = 1 (23);
* ν ∈ {trivial, order 3, order 2, order 6};
* punctures ρ.

The zero cases include f meeting u_i, h meeting u_1u_2R_1, h = 0, and punctured columns. RAW and CLAIM vanish together in every one of them.

**E (replay) design.** This adapts R1 C6.
* The LHS is Σ_{k∈𝒪} Φ(k) |Σ_b β(b,f)χ_b(k)^3 Σ_n a(n)χ_n(k)χ_n(f)^4 𝔡(nb^3)W(q_n/X)|^2, summed directly over a lattice (K = 10^4, k = 0 included).
* The RHS sums, over all 26244 raw tuples (b_1,b_2,n_1,n_2), the Lemma 17.5 formula with the slot-priority split of the marks, every coefficient in the form Coef_1 conj Coef_2 G R OUTER, and the h-sum.
* The cube ideals are b ∈ {1, 7a, 7a², 7b, 7a·7b, 7a³}, where 7a and 7b are the two primes of norm 7. The 27 columns have norms in (58, 139): primes, the inert 121, and 7·13, 7·19.
* The three configurations are:
  * f = 1, ν of order 6, puncture at 73a, empty mark;
  * f = 13a, ν of order 3, two slot lists;
  * f = 7a, which meets b so that β is masked, trivial ν, puncture at 7b, one slot list.
* The radial Gaussian is the case of Lemma 17.5, where every ψ_1 nontrivial on units vanishes on both sides.
* The shifted Gaussian exp(−π|k−z_0|²/K) uses the general Poisson formula with ĝ(y) = e(−z_0y)(2/√3)K e^{−4πK|y|²/3}. It makes almost every tuple contribute.

In the table below, "tuples" counts the raw tuples that survive β, ρ, the marks and the
zero masks. "h≠0 share" is |LHS − (h = 0 part of RHS)|/LHS. The last column gives the
relative error of the RHS under the two replay controls.

| config | Φ | tuples | h≠0 share | LHS | RHS | rel err | err / h≠0 part | drop R(·,P_T) / drop E |
|---|---|---|---|---|---|---|---|---|
| f=1, empty mark, ν6, puncture 73a | radial | 24336 | 5.73e-03 | 1945759.0616877361 | 1945759.0616877312 − 6.8e-12i | 2.5e-15 | 4.4e-13 | 7.5e-03 / 3.0e-03 |
| same | shifted | 24336 | 2.29e-03 | 1939050.2012477932 | 1939050.2012477894 + 1.3e-10i | 1.9e-15 | 8.4e-13 | 8.4e-03 / 2.4e-04 |
| f=13a, two slot lists, χ_4 | radial | 2809 | 2.94e-03 | 70027.3170728111 | 70027.3170728111 + 7.9e-13i | 6.2e-16 | 2.1e-13 | 2.1e-04 / 2.2e-03 |
| same | shifted | 2809 | 3.35e-03 | 69998.7261691448 | 69998.7261691448 − 1.9e-14i | 2.1e-16 | 6.2e-14 | 7.6e-03 / 5.7e-03 |
| f=7b (meets b), one slot list, trivial ν, puncture 103a | radial | 7225 | 1.39e-04 | 348629.0818107656 | 348629.0818107657 − 4.3e-12i | 3.3e-16 | 2.4e-12 | 1.7e-03 / 1.7e-04 |
| same | shifted | 7225 | 2.56e-03 | 349477.0474990257 | 349477.0474990256 + 2.1e-11i | 3.4e-16 | 1.3e-13 | 1.8e-04 / 5.7e-05 |

* With the radial Φ, roughly 1/6 of the tuples have a nonvanishing h-sum, as expected. With the shifted Φ, almost all do.
* The radial and shifted LHS differ, so the dual (h ≠ 0) terms are genuinely exercised.

## 5. Failing controls (part D; minimal counterexamples by N(m_1)N(n_1)N(n_2))

| control | mutation | fails | minimal counterexample |
|---|---|---|---|
| conj_h | χ_u(h~) instead of conj χ_u(h~) | 325/613 | u_1=1, u_2=7a, 𝔅=1, f=103a·103b, h=26+45ω, ν=χ_4 |
| G_swap | G(u_2u_1^{-1}) instead of G(u_1u_2^{-1}) | 373/613 | u_1=1, u_2=7b, 𝔅=1, f=13a·13b, h=14+32ω, ν=ν6 |
| drop_RPT | R(u_1u_2^{-1},P_T) dropped | 97/613 | u_1=1, u_2=13a, 𝔅={7a} with row (π,a_1,a_2)=(1,1,1) (t=3), f=37a |
| drop_R12 | cross factor R(u_1,u_2) dropped | 82/613 | u_1=13a, u_2=7b, 𝔅=1, f=19a·79b, ν trivial |
| drop_chim1 | G(u_2^{-1}) → conj G(u_2) (χ_{u_2}(−1) dropped) | 172/613 | u_1=1, u_2=7b, 𝔅=1 |
| G_split | G(u_1) conj G(u_2) instead of G(u_1u_2^{-1}) | 140/613 | u_1=1, u_2=7b, 𝔅=1 |
| side2_plus | conjugated side keeps +t_p | 111/613 | u_1=1, u_2=37b, 𝔅={7a} with row (1,1,0) (t=4), f=1 |
| xi_2pi | table built with t = a_1 − a_2 + 2π | 239/613 | u_1=13a, u_2=1, 𝔅={7b} with row (1,1,0) |
| drop_E | E removed from h~ | 192/613 | u_1=13a, u_2=1, 𝔅={7b} with row (1,1,0) (E = 7b), f=103a, h=−1−ω |
| drop_f2 | f² removed from h~ | 254/613 | u_1=1, u_2=7a, 𝔅=1, f=103a·103b |
| drop_C4 | χ_u(C)^4 removed | 114/613 | u_1=1, u_2=7b, C=19b, h=−ω |
| drop_dk | χ_u(d_k) removed | 156/613 | u_1=61b, u_2=1, 𝔅={7a} with row (0,0,0), d_k=7a |
| drop_xi | ξ removed | 242/613 | u_1=13a, u_2=1, 𝔅={7b} with row (1,1,0) |
| drop_mu | μ(u) removed | 320/613 | u_1=1, u_2=7b, 𝔅=1 |

At each minimal counterexample, RAW and the mutated value are distinct sixth roots of unity, or distinct unit-modulus values. The full values are in the JSON.

**Predicted insensitive:** xi_orient replaces ξ(u) by Π χ_p(u)^{e_p}. It fails on 0/613, as predicted in remark R2.

**In the replay,** dropping R(·,P_T) or E moves the RHS off the LHS by relative 1e-4 to 1e-2 in every configuration. That is at least 10^9 times the agreement level.

## 6. What this does and does not establish

* It establishes that the first-Poisson column coefficient (C) is the correct reduction of the expanded block (A) under Lemma 17.5, CRT and sextic reciprocity, with the paper's conventions. That reduction includes the fixed-ray quotient, the table and h~ = hf²E. The numerical part is empirical: double-precision Gauss sums at norms ≤ 1.5·10^5, with exact symbols. The hand derivation is general.
* It does not check:
  * the subsequent t' extension (10382-10398) and the separated identity eq:inverse-first-separated, which was read only;
  * the weighted Cauchy step (D);
  * the second transform;
  * Lemma 14.3, the analytic common-density requirement, or the claim that the recursion closes.
* Cubic reciprocity, which eq:signal needs, is imported and is exercised only numerically.

## 7. Misreadings to avoid

* "(C) verified" is one identity inside the proof of Lemma 17.2. It is not a verification of Lemma 17.2, Proposition 19.2 or the 7/8 theorem.
* The script's tolerance passes are floating-point agreement, not certified computation.
* RH remains unsolved. Even if accepted, 7/8 is a fixed half-plane statement.
