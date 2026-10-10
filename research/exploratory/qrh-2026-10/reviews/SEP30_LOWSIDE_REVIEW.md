# Bounded review of the low-side chain of the 30 Sep 2026 OpenAI 7/8 manuscript

```text
Status: EXPLORATORY bounded review (one agent, about 75 minutes). Verdict: NO WRONG STEP FOUND in
  Cor 14.1, Lemma 14.2, Lemma 14.3 (with its completed-moment corollary), Prop 15.2 and Prop 15.3,
  at the level stated in the verdict table. This is not certification, not an integration record,
  and says nothing about RH.
Scope: [OAI] TeX 7249-8649: Cor 14.1 (7361-7441), the phase prose (7443-7483), Lemma 14.2
  (7510-7655), Lemma 14.3 (7747-7993), completed moment (7995-8056), Prop 15.2 (8340-8557),
  Prop 15.3 (8564-8649). Lemma 15.1 (8111-8332) was re-checked at the exponent level only (PR 910
  already reviewed it). Inputs read and checked as invoked, not reviewed in full: Prop 5.1 statement
  and its local-factor paragraphs (1676-1881, 1995-2060, 2200-2279), Lemmas 5.3-5.5 and 5.7
  (2536-2813, 2956-3137), Lemmas 13.2-13.4 (7055-7229), Sec. 6 probe and low separation (3349-3480),
  Sec. 12 geometry and compensated probe (6810-6916).
Exact sources or dependencies:
  [OAI] paper.tex at pr908 (31c706bb), standalone/2026-10-07-openai-quasi-riemann-import/upstream/
        preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, SHA-256
        42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here; the
        scratchpad copy sep30.tex is byte-identical). External, unreviewed, read as untrusted data.
  [HB]  D. R. Heath-Brown, Kummer's conjecture for cubic Gauss sums, Israel J. Math. 120 (2000)
        97-124, Theorem 2. The original was NOT re-read (no open copy found). Its statement was
        checked against the verbatim restatement in [DR] (Theorem "cubicHBloc", Sec. 9 of the source;
        source SHA-256 47d01be0662e77cf...).
  [GL]  L. Goldmakher, B. Louvel, A quadratic large sieve inequality over number fields,
        arXiv:1112.1642v2 (TeX source, SHA-256 620b50748e958877...): Definition 1, Theorem 1.1.
  [DR]  A. Dunn, M. Radziwill, Bias in cubic Gauss sums: Patterson's conjecture, arXiv:2109.07463
        (TeX source as above): Patterson's coefficients eq. (cubiccoeff), the quoted cubic sieve.
  Repository: SEP30_VERIFICATION_MAP.md (target 1), THRESHOLD_CALCULUS.md, BILINEAR_B2.md,
        reviews/PR910_REPLAY.md, scripts/energy_lp.py, a2/eis.py (imported read-only,
        SHA-256 87ca11d9...e65, unmodified).
What was actually run (nice -n 10; both scripts exit 0 under python3 and python3 -O):
  - reviews/sep30_lowside_ledger.py (new; SHA-256 42c173ba...4004): 54 exact-rational / sympy
    checks, 0 failures. They re-derive every displayed exponent identity of the chain, the Lemma 14.2
    block bound on 20000 exact rational dyad configurations, the zero-excess locus, and the
    sensitivities.
  - reviews/sep30_lowside_eis.py (new; SHA-256 3784f6b1...cee): 22 checks, 0 failures, about 5 s.
    Exact symbols in Z[omega] (Gauss sums in floating point). It checks Prop 5.1's local Fourier
    table and the active zero-exponent local sum on 15 primes, the zero-preserving symbol identities
    of Lemmas 5.5/14.2/14.3 (3000 random cases each), and the pair phase on 506 prime pairs. It
    brute-forces Lemma 13.3 on 14 modulus pairs (5232 frequencies) and counts the Gram bound's
    exceptional frequencies for K <= 60000.
Smallest remaining gap: Cor 14.1 imports Prop 5.1's branch-compatibility clause (TeX 1843-1849,
  proof 2253-2262). The clause says an absent good prime and an inactive zero-exponent prime give the
  same c_F, c, d, vartheta, kappa_F and kernel, and that the cusp data depend on the local set only
  through h_0 and r mod M_ref^2. Its local half is now checked mechanically. Its global theta half
  is Prop 5.1's own proof, which has not been reviewed at this source.
```

RH is unsolved. This file reviews one block of an external, unreviewed proof of a zero-free half-plane `Re s > 7/8`. It is a bounded agent review: "no wrong step found" means only that the steps listed below were re-derived or checked and nothing failed. It does not mean the chain is certified.

## 1. Verdict table

| Node (TeX) | What was checked | How | Verdict |
|---|---|---|---|
| Cor 14.1 (7361-7441) | Expansion `1_{q\|A} = 1 - chi_q(A)^0`. Combination absent + inactive = `1 - (1 - q^-1) = q^-1`. Active coefficient `-omega_{q,0} = tau+_{q,2} chi_q(eps_q)^-2`. `\|zeta_Q\| <= 1/81`. Vanishing when a marked prime is a base prime. | Hand re-derivation; ledger §1. The local Fourier coefficients of `1_{p\|x}` are `1/q` at every frequency; the Prop 5.1 local table and the active `j=0` local sum were checked numerically (dev `<= 3e-16`). | **No wrong step found.** Conditional on Prop 5.1 item 3 (branch compatibility), which is imported and is the first unverified step. |
| Phase prose (7443-7483) | `chi_p(sigma_p)^-2 omega_{p,j} ∝ chi_p(c/p)^{2j+2}` for all j. Pair phase `(q/p)_3^{j_p+j_q+2}`. Row `j=1` against a mark `j=0` gives 1; against a moving `j=4` it gives `(q/p)_3`. Moving columns `chi_R(nb^3)^3 = chi_R(nb)^3` and `chi_P(nb^3)^-2 = chi_P(n)^-2 1_{(P,b)=1}`. | Exponents mod 6 for all `j`; actual symbols on 506 ordered prime pairs × 36 exponent pairs; 3000 random column cases. | **No wrong step found.** |
| Lemma 14.2 (7510-7655) | Möbius removal of `1_{(P,k)=1}` and the rowwise divisor Cauchy. Factorisations of `beta_D`, `a_D` and `a_{D,r}`, and the zero-preserving identity at 7612-7613. Application of Lemma 5.5 with row length `K/q_D`. Cubic sieve with rows `j = c'm` and columns `P'`. Count `T^2 (C/r_0)(G/C) r_0 = B`. Final bound `B(K+NB)(N+L+(NL)^{2/3})`. | Hand; ledger §2: block exponent `<=` claim on 20000 exact configurations (0 violations); Lemma 5.5 count identity; eis checks of the zero masks. | **No wrong step found.** Imported hypotheses match (§3). |
| Lemma 14.3 (7747-7993) | Kernel argument `q_mu X/q_c^2 = Y y_n y_b^3 y_R^-2 prod y_i^-2`, exponent `v+3l_b+e_lambda-T_d`. Per-tuple coefficient (4.5) from `\|d(mu)\| <= 27 3^{k/6}\|b\|` and the `B_p` sizes. Outside factor `-v-2l_b-2e_lambda/3-S_0-B_0`. Identity `v+z_a-u = max(v,z_a,2(v+z_a)/3)`. Assembly of `E_ref` (4.6). Kernel saving `-(T_d-y)_+/2`. Powerful count `O/2`. The two independence hypotheses of Lemma 14.2. | Sympy identities; 625-point exact grid for the `u` identity; independence checked by reading against Cor 14.1 and the phase prose. | **No wrong step found.** Size bound (4.3) matches Patterson's coefficients as restated in [DR] (§3.3). |
| Completed moment (7995-8056) | Table of `2A_0-N_0-S_0-4B_0` coefficients `(2,1,1,1,-2,0)`. Width charge `T_d-S_0-B_0 = 2H+(2A_0-N_0-S_0-4B_0)+2z_a-N_*`. Both branch bounds (branch 2 slack `= 3l_b + (5/3)(e_lambda+eta) >= 0`). Note that `z_a = u = 0` here: the step "drop the nonpositive terms" would be false for `z_a > u`, and the text restricts to empty slot lists at 8034. | Ledger §3. | **No wrong step found** (unmarked case only, as stated). |
| Lemma 15.1, exponents only (8235-8325) | Identity (5.3). `T_d - (H-3d)` formula. Branch-2 energy `M' + (d-1/6-2Delta_H+theta_N)/4`. 'Otherwise' inequality `s+l_b+2e/3+(T-y)_+/2 >= T/4` (20000 exact points). `E_B(M-2d, l-d) = M'` on `[0,1/6]`. | Ledger §4. | Agrees with PR910_REPLAY. |
| Prop 15.2 (8340-8557) | Rewriting `A_m = Y'^{-3/2} sum c W r^{-1+i nu} g`. Prefactor `Q/Y'^3`. Kernel argument `q_C q_k/P_a`. Diagonal `Q/Y'`. Nonexceptional vanishing argument. Periodic Poisson bound (eq. gram-periodic-poisson). Count `C_0 D_0 K_R`. Nonexceptional total `(Q/Y')(P_a^2/Y') R^{2-B}`. Exceptional count `O(K_R^{1/6} q_C^eps)` and total `(Q/Y') P_a^{1/6}`. Dyadic sum `<<(1+log(2+Lambda))/Lambda`. | Ledger §5 (log-form identities; the dyadic sum in floating point, ratio `<= 3.45`); Lemma 13.3 brute force (max dev `1.8e-14`, including `C` meeting one residual modulus and an inert prime); exceptional count: brute force equals the structure `(k) = a_1^6 e` exactly at K = 100, 1000, 10^4, 6·10^4, for C = 1 and C = pi_7. | **No wrong step found.** |
| Prop 15.3 (8564-8649) | `P_a = q_{b*}^-1 Z^{1/8}` independent of d. Length inequalities `3/16, 5/16, 1/12, M' >= 1/2`. `P_a^2/Y' << P_a^{1/6}`. CS output `[Z^{M'}/Y']^{1/2} P_a^{1/12} = r_J X'^{1/2} P_a^{1/12}`. Tuple count `Z^d`, coefficient `Z^{-3d/2}`, `f(d) = -d`. `C_II(7/8) = 3/16`. | Ledger §6 in exact rationals on 17 values of d. | **No wrong step found.** The supremum `3/16` is attained only at `d = 0`, with zero excess. |

## 2. Line-by-line notes

### 2.1 Cor 14.1 and the phase separation

* **(7418-7432).** `1_{q|A} = 1 - chi_q(A)^0` holds by the zero convention `chi_p(x)^0 = 1_{p∤x}` (1674). Expanding the product over `Q` gives finitely many completed sums. Each has local set `P_0 ∪ S'` with `j_q = 0` on `S' ⊂ Q`, so Prop 5.1 applies to each: its marked primes are good, hence prime to `L`.
* **Summing the branches at one prime q.**
  * The absent branch has coefficient `+1`.
  * The inactive branch has coefficient `−(1 − q^{-1})`. It has the same kernel as the absent branch, by Prop 5.1 item 3.
  * The active branch has coefficient `−omega_{q,0}` and local factor `B_q = q^{-1/2} chi_q^{-2}`.
  * The inactive total `q^{-1}` is the mean of `1_{q|x}`; `eis` confirms that every Fourier coefficient of `1_{p|x}` equals `1/q`.
* **(1828, 2022-2025, 2241-2245).** The table value `C_{p,0}(h) = 1 − q^{-1}` or `−q^{-1}`, and the active sum `−q^{-1/2} tau+_{p,2} chi_p(eps x)^{-2}`, were checked numerically. The check includes `p | x`.
* **(7436-7440).** If a marked prime is a base local prime, the mark forces `q | nb³`, and the zero-extended base factor `chi_q(nb³)^{j_q}` then vanishes, including for `j_q = 0`. Correct.
* **(2271-2276, 7446-7452).**
  * We have `eps_p = −lambda^{-5}(c/p)^{-2} mod p` and `sigma_p = lambda² c/p`. The exponent of `chi_p(c/p)` is therefore `−2 + 2(j+2) = 2j+2` for `j ≠ 0, 4`; `−2 + 4 = 2` for `j = 0`; and `−2 ≡ 10` for `j = 4`.
  * The pair phase then follows from `chi_p² = (·/p)_3` and cubic reciprocity.
  * The cancellation that makes the row/tuple split possible is the `j=1`/`j=0` case: `chi_p(q)^4 chi_q(p)^2 = (q/p)_3^3 = 1`.
  * All other cross terms are row scalars, tuple scalars or frozen, as stated. The same holds for `alpha-bar(c)²`, which is multiplicative, and for `kappa_F`, which is fixed once the classes of `R` and `P` modulo `M_ref²` are fixed separately.

### 2.2 Lemma 14.2

* **(7546-7570).** For fixed `k`, the sum over `D | (P,k)` has at most `d(k)` terms, so rowwise Cauchy is legitimate. In each `D`-summand:
  * `chi_k = chi_D chi_{k'}`, `chi_P = chi_D chi_{P'}` and `1_{(P,b)=1} = 1_{(D,b)=1} 1_{(P',b)=1}`;
  * the factor `q_D^{-1}` comes from `q_P^{-1/2}`;
  * no `(P',k')` mask remains.
* **(7577-7590).** For fixed `D`, the coefficient `beta_D · gamma_D` (where `gamma_D` is the inner `P'`-sum) is independent of `k'`. This is the only hypothesis of Lemma 5.5.
* **Lemma 5.5 itself (2731-2812).**
  * The zero mask `chi_k(nb)^3 = chi_k(mh)^3 1_{(k,ct)=1}` holds and was checked on 3000 random cases.
  * The `S`-parts of `m,h` are split off before the sieve, so the sieve is applied only to good indices, which is what [GL] needs (§3.2).
  * The count `(C/r_0)(N/C)(G/C)(C/r_0) · r_0 · T · T = NB/r_0` was checked in the ledger.
* **(7612-7615).** `chi_{P'}(rc'm)^{-2} 1_{(P',rc'ht²)=1} = chi_{P'}(r)^{-2} chi_{P'}(c'm)^{-2} 1_{(P',ht)=1}`. The character zeros supply `(P',rc')=1` (checked).
* **(7622-7651).**
  * Discarding `|beta_D|² ≤ 1` is allowed in this positive sum.
  * The rows `j = c'm` are squarefree and primary and may contain the prime 2, which HB allows (§3.1).
  * The kernel `chi_{P'}(j)^{-2} = conj((j/P')_3)`. Since the bound `U+V+(UV)^{2/3}` is symmetric, duality (or cubic reciprocity) gives HB's orientation.
  * `Sum_{P'} q_{P'}^{-1} = O(1)` on a dyad.
  * The ledger confirms that every block is bounded by the final display. The proof replaces `D_0, r_0` by 1 and uses `NG/C² ≤ NB`.

### 2.3 Lemma 14.3 and the completed moment

* **(7851-7868).** The kernel-argument identity is exact; sympy reproduces `T_d = 2H+2A_0+2z_a−N_*−N_0−3B_0`.
* **Coefficient (4.5).** Write `mu = u lambda^k (N_F n)(B_F b)^3`. Then `|d(mu)|/sqrt(q_mu) ≤ 27·3^{-k/3} q_{N_F n}^{-1/2} q_{B_F b}^{-1}`. Combine this with the `B_p` sizes:
  * divisibility terms contribute `q^{1/2}`;
  * small Ramanujan or active zero-mask terms contribute `q^{-1/2}`;
  * active marks contribute `q^{-1/2}`.

  This gives `−v/2 − l_b − e_lambda/3 − (S_0+B_0+z_a)/2` exactly.
* **(7969-7982).** Lemma 14.2 is applied with `(K,N,B,L) = (Z^H, Z^v, Z^{l_b}, Z^{z_a})`. Together with the outside squared factor and `m_ker² = Z^{-(D)_+/2}`, it reproduces `E_ref − O/2`. The powerful count `x²y³` gives `O/2`.
* **Independence hypotheses (7952-7967).** These are the load-bearing structural claim. They follow from §2.1 once the classes of `R` and `P` modulo `M_ref²` are fixed separately. Rows and tuples are then partitioned into finitely many fixed classes, which costs only a triangle inequality.
* **(8034-8046).** Branch 1 drops `−l_b − 2e_lambda/3 − ...`. This is valid only because `z_a = u = 0` there; for marked rows `z_a − u ≥ 0` is not droppable. The text restricts to the unmarked case, and Lemma 15.1 handles the marked case separately (8267-8311).
* **Kernel bound.** `V#(x) ≪ x^{1/4}` for small `x` is conservative: `R(t)` has no poles for `Re t > −5/6`. It is only used as an upper bound.

### 2.4 Prop 15.2

* **Setup.**
  * Poisson in `m` over `O` with period `s_1 s_2`, and the complete transform `q_{s1} q_{s2} F(s_1, s_2; j)`, give the prefactor `Q/Y'^3`.
  * The dual frequency `j = Ck` (Lemma 13.3) puts the kernel argument at `q_k Q/(q_C q_{n1} q_{n2}) ≍ q_C q_k/P_a`.
  * The `k = 0` term forces `s_1 = s_2` and gives `phi(s)`.
* **Nonexceptional frequencies.**
  * For fixed `C, d, k`, every factor of the coefficient other than `chi_{m1}(k)` is periodic modulo `l_fixed · rad C`: `c_sigma`, `R`, `L_C^{ext}` and the `m_2` factor.
  * The factor `chi_{m1}(k) = kappa(m1) R(k_good,m1) Π chi_p(m1)^{e_p}` (8407-8417) contributes a nonprincipal `chi_p(m1)^{e_p}` at some `p ∤ C l_fixed`.
  * By CRT the complete mean over `m_1` vanishes. Four-dimensional Poisson then gives `q_C N² min{1, (Q_r/N)^A}`.
* **Exceptional frequencies.**
  * These are `(k) = a_1^6 e`, with `e` sixth-power-free on `S ∪ supp C`. Nothing restricts `a_1` at `S` or `C`; an earlier draft of our count got this wrong, and the brute force caught it.
  * The trivial bound is `q_C N²` per frequency. The `K_R^{1/6}` count gives `(Q/Y') P_a^{1/6}`.
  * The brute-force count of nonzero `k` with `q_k ≤ K` equals the structural count exactly (C = 1: 66, 132, 216, 294; C = pi_7: 102, 246, 504, 762).
* **Lemma 13.3 (input).** The lift formula `F(Cn_1,Cn_2;Ck) = chi_{n1}(k) conj chi_{n2}(−k) R(n_1,n_2) L_C` matches brute force on 14 modulus pairs. Here `R(n_1,n_2) = conj chi_{n1}(n_2) chi_{n2}(n_1)`. The pairs include `C` meeting exactly one residual modulus (local factor 0 when `6 ∤ c`) and the inert prime 5. Also confirmed: `F(u,v;0) = phi(u) 1_{u=v}`, and `F = 0` unless `C | j`. The `6 | c` branch (`P − 2`) was **not** exercised, because it needs `p^6`.

### 2.5 Prop 15.3: where the zero excess sits

The ledger rebuilds the J-summand exponent from the black-box outputs at general d. These are Lemma 15.1's `Z^{E_B(M',l')}`, Prop 15.2's `(Q/Y')·max(1, P_a^{1/6}, P_a²/Y')`, the `Z^d` tuples and the coefficient `Z^{-3d/2}`. The result is exactly `lx/2 + b/12 − d`, so the supremum `3/16 = C_II(7/8)` is attained only at `d = 0`. At `d = 0`:

* **Row norm.** It is the large-sieve diagonal `Z^{M}`: branch 1 of Lemma 15.1, `E_ref ≤ O/2 + H ≤ M' − O/2`. This is the quadratic sieve's `K` (row-count) term.
* **Cubic sieve.** The hybrid branch is **not** binding at `d = 0`: `E_B` branches are `(5/6, 19/24, 5/6)`, slack `1/24 − d/4`. Heath-Brown's `(NL)^{2/3}` term binds only at `d = 1/6`, where the J-summand has slack `1/6`.
* **Gram norm.** It is set by the exceptional term `P_a^{1/6} = Z^{1/48}`. The other terms have slack: `P_a²/Y'` by `1/4`, and `1` by `1/48`.

**Sensitivity.** These are exact in the ledger.
* A fixed loss `Z^eta` in either factor norm at `d = 0` moves the boundary `sigma_0 = 1 − lx/2 − h/6 + theta_low` by `eta/2`.
* Raising the exceptional-count slope from `1/6` to `1/6 + delta` moves it by `delta/16`.
* Without the sixth-power structure (all frequencies exceptional), `theta_low = 23/96` and the boundary would be `89/96`.

So the two load-bearing exact inputs at the binding point are the quadratic sieve's diagonal and the `K^{1/6}` exceptional count. Both were checked above. The cubic sieve has `1/24` of row-norm slack there.

## 3. Imported theorems: hypotheses against use

### 3.1 Heath-Brown's cubic large sieve [HB, Thm 2]

Quoted at TeX 7491-7499. It was compared with [DR]'s verbatim restatement:

* the outer sum is over squarefree `a ≡ 1 (3)` with `N(a) ≤ A`;
* the coefficients `beta_b` are supported on squarefree `b ≡ 1 (3)` with `N(b) ≤ B`;
* the bound is `(A + B + (AB)^{2/3})(AB)^eps Σ|beta_b|²`.

The manuscript's statement matches. It is used once, at 7631-7639, with:

* rows `j = c'm`: squarefree primary of norm `≪ N/r_0`, possibly divisible by the inert prime 2, which HB allows;
* columns `P'`: squarefree good primes of norm `≍ L/D_0`, with bounded coefficients.

The orientation is immaterial by duality, since the bound is symmetric, and also by cubic reciprocity. [DR] note (via the duality principle and cubic reciprocity) that `B(A,B) = B(B,A)`. **Hypotheses satisfied.** The original paper was not re-read; this is the only imported statement checked only through a secondary primary-literature quotation.

### 3.2 Goldmakher–Louvel [GL, Def. 1, Thm 1.1]

* **What the theorem says.** Consider a quadratic Hecke family `{chi_a}` indexed by squarefree ideals in `I(c)`, satisfying:
  * (1) order divides 2;
  * (2) reciprocity `chi_a(b) = chi_b(a) C([a],[b])`;
  * (3) `chi_a conj(chi_b)` is primitive modulo `ab` when `[a] = [b]`.

  Then `Σ*_{Na≤M} |Σ*_{Nb≤N} lambda_b chi_b(a)|² ≪ (MN)^eps (M+N) Σ|lambda_b|²`.
* **Manuscript use (2650-2672).**
  * The family is `vartheta_a`, the quadratic symbol at the primary generator. Its conductor is exactly `a lambda^{e(a)}` (the `±1` primary adjustment is a character modulo `lambda`; `omega` is a square) and its infinity type is trivial.
  * Property (3) holds within a fixed class modulo 4, and reciprocity is the fixed bicharacter `R`. The displayed orientation follows by duality.
  * Lemma 5.5 applies the sieve only to good rows `k'` and good columns `j`, with the `S`-parts split off first.
* **Verdict: hypotheses satisfied.** This was checked at the level of the argument, not mechanically.

### 3.3 Patterson / Dunn–Radziwiłł theta coefficients

Lemma 14.3 uses the support and size statement (4.3), `|d(mu)| ≤ 27·3^{k/6}|b|` on `mu = u lambda^k n b³`. For the cusp at infinity, [DR] eq. (cubiccoeff), citing Patterson Thm 8.1, gives:

* `|tau(mu)| = |d| 3^{n/2+2}` for `mu = ±lambda^{3n−4} c d³`;
* `|tau(mu)| = |d| 3^{n/2+5/2}` for `mu = ±lambda^{3n−3} c d³`.

With `|g(·,c)| = |c|` for squarefree `c`, these are `≤ 27·3^{k/6}|d|`. This is consistent. The other two cusp functions were not checked, and neither were the cusp-expansion identities of Prop 5.1. Both are imported, and their analog was reviewed in [O5] R3.

## 4. What was not verified (in reading order of the chain)

1. **Prop 5.1 item 3, branch compatibility (1843-1849; proof 2253-2262).** This is the first unverified step. Cor 14.1 is finite inclusion-exclusion *given* this clause. The local factors are verified (§2.1). The global claim is not: that `c_F, d, vartheta, kappa_F` and the kernel depend on the local set only through `h_0` and the active radical `r mod M_ref²`, which is part of the theta cusp transform. Prop 5.1 has 786 lines and no review at this source.
2. **Lemma 4.5 (smooth calculus)** and the single-density Minkowski separation (Lemma 5.3, eq. reflection-common-minkowski). They were read and are consistent, but Lemma 4.5 itself was not reviewed. They are used in Lemma 14.3 (7916-7927) and Lemma 15.1.
3. **The vanishing of nonexceptional complete means in Prop 15.2.** It was checked by reading. It rests on the reciprocity decomposition of `chi_m(k)` and Lemma 4.1 (fixed numerators give ray characters), which are unreviewed. It was not brute-forced.
4. **Lemma 13.3's `6 | c` local branch.** It was not exercised numerically.
5. **The analytic transfer in Lemma 15.1.** It is not re-proved here; PR 910 checked it at the exponent and adapter level.
6. **[HB]'s original text.** It was not consulted (§3.1).

## 5. Reproduction

```text
cd research/exploratory/qrh-2026-10/reviews
nice -n 10 python3 sep30_lowside_ledger.py   # 54 PASS, exit 0 (sympy); also under -O
nice -n 10 python3 sep30_lowside_eis.py      # 22 PASS, exit 0, ~5 s; imports ../a2/eis.py read-only
```

The ledger's floating-point items are the dyadic-sum ratio and nothing else. In the eis script, the Gauss-sum and correlation checks are floating point, with tolerances `1e-9` and `1e-6` against deviations of at most `2e-14`. The symbol, zero-mask, pair-phase and counting checks are exact.
