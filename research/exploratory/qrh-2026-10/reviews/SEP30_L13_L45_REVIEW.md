# Sep 30 manuscript: Lemmas 13.3 and 13.4 (common-support correlations) and Lemma 4.5 (smooth calculus)

```text
Status: REVIEW (bounded; external, unreviewed manuscript) + EXACT finite checks + FLOAT spot checks.
  Verdicts: Lemma 13.3 no wrong step found; Lemma 13.4 no wrong step found; Lemma 4.5 no wrong
  step found. Read as used, also no wrong step found: Lemma 13.2 (exact check added), Lemma 4.7
  (kernel-seminorms), Lemma 4.9 (logarithmic-control), and its inputs Lemmas 4.8 and 4.10.
Scope: "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (OpenAI, 30 Sep 2026).
  Line by line: Lemma 13.2 (l. 7055-7079); Lemma 13.3 (statement 7081-7132, proof 7134-7190);
  Lemma 13.4 (statement 7196-7210, proof 7212-7229); the Moebius-extension paragraph (7231-7247);
  Lemma 4.5 (1123-1210, proof 1212-1286); Lemma 4.7 (1347-1413); Lemma 4.8 (1425-1529);
  Lemma 4.9 (1531-1600); Lemma 4.10 (1602-1646). The uses were read only to check that each
  cited instance matches the statement: Prop 15.2 (8334-8420), Lemma 18.1 (13600-13760),
  Lemma 5.3 (2540-2578), Lemma 8.2 (4428-4456) and Sec. 17 (9645-9710). Those proofs are NOT
  reviewed here.
Exact sources or dependencies:
  [OAI] pr908 (31c706bb) standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, sha256
        42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 (re-hashed here).
        External and unreviewed; read as untrusted data.
  Code: reviews/sep30_l13_checks.py (new; sha256 d1587c070646425eded2887e68024964662bd16671afd05cf72ae81aafd5278d). It imports a2/eis.py unchanged
        (sha256 87ca11d98bf3ee130a6dab613b5f7efe444058320b7c22b005327686f2798e65), numpy, and
        sympy (for cyclotomic polynomials only).
  Prior notes: reviews/SEP30_VERIFICATION_MAP.md (target 5 and "next after these"),
        reviews/LEMMA18_1_COMMON_SUPPORT.md (its checks E and F were floating-point versions of
        part of A-C below).
What was actually run: nice -n 10 python3 -I sep30_l13_checks.py -> see Sec. 5 (one process,
  114 s): 33/33 PASS. Log: scratchpad l13/full_run.log.
Smallest remaining gap: none inside the scoped lemmas. What remains is outside scope:
  (i) whether each downstream invocation (Prop 15.2, Lemma 18.1, and the 40 users of Lemma 4.5)
      applies these lemmas inside their hypotheses with the claimed uniformity;
  (ii) the four-class reciprocity Lemma 4.4 as an analytic statement. Here it is only re-confirmed
      on the pairs used (check A5).
```

RH is unsolved. This note concerns three helper lemmas of an external, unreviewed proof of a
quasi-RH statement (`Re s > 7/8`). Parts A-D and X of the checks are exact computations, in
`Z[omega]` or in `Z[zeta_L]` modulo `Phi_L`, on finitely many small moduli. They show that the
displayed finite identities hold on those instances. They are not a proof for all moduli; the
proofs were read for that. Part S is floating point and EMPIRICAL.

## 1. Lemma 13.3 (`lem:full-correlation`), l. 7081-7190

**Setting.** `u, v` are primary moduli outside `S`. `F(u,v;j)` is the twisted congruence sum
(old-eq:2.11). `C = (u,v)`, `u = C n1`, `v = C n2`.

| claim (line) | step checked | result |
|---|---|---|
| Fourier form `F = (q_u q_v)^{-1/2} Σ_h G(u,h) conj G(v,h) e(−jh/uv)` (7090-7093; proof 7134-7140) | Expansion plus additive orthogonality. It uses `Σ_{h mod uv} e(hm/uv) = q_uv 1_{uv \| m}`, which holds because `O` is self-dual for `e(zy)`: the inverse different is `λ^{-1}O`. The normalization `(q_uq_v)^{-1/2} · (q_uq_v)^{-1/2} · q_uq_v = 1` is right. | correct; **D1** exact in `Z[ζ_L]`, 916 cases, control D1c |
| `F(u,v;0) = φ(u) 1_{u=v}` (7094-7095; 7140-7146) | Units force `u \| v` and `v \| u`. Primary generators give `u = v`; then `x ≡ y`. Includes `u = 1`. | correct; **A3** |
| `F = 0` unless `C \| j` (7099; 7148) | `vx − uy = C(n2x − n1y)`, and `uv = C² n1 n2`. | correct; **A1** |
| `F(Cn1,Cn2;Ck) = χ_{n1}(k) conj χ_{n2}(−k) R(n1,n2) L_C` (7100-7111; 7149-7158) | Reduction mod `n1` and `n2`. The unit factor is `conj χ_{n1}(n2) χ_{n2}(n1)`, which equals `R(n1,n2)` by Lemma 4.4 on coprime pairs. | correct; **A1** (21 configurations, 2,631,375 values of `j`); **A5**: symbol ratio = four-class `𝔯` |
| lift count (7159-7168) | At `p^c ∥ C` with `p ∤ n1n2`: no extra lift. If `v_p(n1) = d > 0`: each `y mod p^c` fixes a unique `x mod p^{c+d}`, and the reduction mod `p^c` is the `L_C` congruence. CRT gives the product. | correct; **A1, A2** (prime powers in the residuals, `C` meeting a residual) |
| local factor, `p ∤ n1n2` (7114-7121; 7170-7182) | `P^{c−1}` lifts per field solution. If `p \| k`: `A(n1/n2)(P−1)`. If `p ∤ k`: `y=(k/n1)t`, `x=(k/n2)(1+t)` reduces to `Σ_{z≠0,1} A(z)`, which is `−1` or `P−2`. `A = χ_p^c` is principal iff `6 \| c`, since `χ_p` has exact order 6 on `k_p^×`. | correct; **B1** (grid: split 7 for `c ≤ 3`, split 13 for `c ≤ 2`, inert 5 for `c ≤ 2`, inert 11 for `c = 1`; `Z/7^c` enumeration for `c = 4..7`), **B2** |
| one-sided factor `P^{c−1}(P−1)1_{6\|c}1_{p∤k}` (7122-7123; 7182-7185) | `x = k/n2` is forced; the `y`-sum is `P^{c−1} Σ conj A(y)`. | correct; **B1** (grid and enumeration, including `c = 6`) |
| `\|L_C\| ≤ q_C`; extension periodic mod `rad C` (7128-7131; 7185-7189) | Each local value depends only on `n_i mod p` and `k mod p`. Its modulus is `≤ P^{c−1}(P−1) < P^c`. | correct (with slack); **A4**, **B3** (genuine congruence sum periodic in both columns) |
| artificial extension is not the congruence sum (7123-7128) | the paper's own caveat | confirmed necessary: **X1** |

**Hypotheses and constants.**
* All constants are exact: no implied constants occur.
* "Primary" is used only for the zero-frequency step. "Outside `S`" is what makes `χ_p` sextic. The ramified prime `λ` (norm 3) and the inert prime `2` (norm 4) lie in `S`, and `χ` is undefined there. So the requested "ramified-type" case does not arise; the script prints this as N/A.
* The one-sided case ("`C` meets one residual") is the only asymmetric local type. It is covered by A and B.

**Verdict: no wrong step found.**

## 2. Lemma 13.4 (`lem:complete-support-correlation`), l. 7196-7247

**Setting.** `u = Da`, `v = Eb` are primary and outside `S`, with `(a,b) = 1` and `(ab, DE) = 1`.
`D` and `E` are arbitrary.

**Proof check.** `O/DEab = O/DE × O/a × O/b`, since the three factors are pairwise coprime.
* Mod `a`: `Da y ≡ 0`, so `x ≡ j/(Eb)`, which gives `χ_a(j) conj χ_a(Eb)`.
* Mod `b`: `y ≡ −j/(Da)`, which gives `conj χ_b(−j) χ_b(Da)`.
* On `DE`: the substitutions `x' = bx`, `y' = ay` are bijections. They turn the congruence into `Ex' − Dy' ≡ j (mod DE)` and contribute `conj χ_D(b) χ_E(a)`.
* The collected unit factor is `[χ_E(a)/χ_a(E)] · [χ_b(D)/χ_D(b)] · [χ_b(a)/χ_a(b)] = R(a,E) conj R(b,D) R(a,b)`. Since `R = ±1`, the conjugation is immaterial.
* The proof (7212-7229) says exactly this.

**The extension paragraph (7231-7247).** `F~` is the right side, extended to non-coprime `(a,b)`.
The identity `Σ_{(a,b)=1} c F = Σ c F~ Σ_{t|a,t|b} μ(t)` is the divisor-sum identity. The text
warns that `F~ ≠ F` off the locus; this is confirmed (**X2**: 27 differing values). The warning is
therefore needed, not decorative.

**Checks.** **C1**: 15 configurations and 1,139,157 values of `j`, every `j mod DEab`, with no
mismatch. The configurations cover:
* `D = E`, `D ≠ E` with a shared prime of unequal multiplicity, `D` or `E` equal to `1`, and `a` or `b` equal to `1`;
* prime-power `a`, `b`, and an inert `q5` in `D` or in `a`.

**C2**: each of `R(a,E)`, `R(b,D)`, `R(a,b)` equals −1 in some configuration, so dropping any
of them is detectable. **X3** is the Möbius insertion identity on a 5×5 array, checked exactly.
The configurations with unequal multiplicity at a shared prime, `(2,1)` and `(1,2)`, give
`F ≡ 0`. This is the forced vanishing for `6 ∤ min`, consistent with Lemma 18.1's text at
13722-13727.

**Verdict: no wrong step found.** The use in Lemma 18.1 (13686-13697) is on the genuine locus
`(a,b) = 1`, `(ab, D2E2) = 1` by construction, which matches the hypotheses. The one-sided and
unequal-multiplicity formulas quoted at 13699-13734 are special cases of Lemma 13.3; part B
covers them. Prop 15.2 (8378-8395) invokes Lemma 13.3 with `s_i` primary and prime to `S`, and
explicitly uses the artificial extension with the full Möbius sum inserted first. Both match the
statements. The rest of Prop 15.2 is not reviewed here.

## 3. Lemma 13.2 (`lem:prime-power-fourier`), l. 7055-7079 (dependency of 13.3)

The split `x = x0 + py` gives `P^{a−1} 1_{p^{a−1}|k}`. The remaining sum is either a nontrivial
Gauss sum (`6 ∤ a`) or a sum over units (`6 | a`). The proof is correct.

**D2** checks the formula exactly in `Z[ζ_L]` on 797 values of `(p^a, k)`:
* for `6 ∤ a`: `|S|² = P^{2a−1} 1_{v_p(k)=a−1}`, on split 7 (`a ≤ 3`), split 13 (`a ≤ 2`), inert 5 (`a ≤ 2`) and inert 11 (`a = 1`);
* for `a = 6`, `P = 7`: the integer value of `S`, using the coset criterion in `Z[ζ_{7^6}]`.

This replaces the earlier floating check (`lemma18_local.py`, 2e-16) with an exact one on these
instances. **No wrong step found.**

## 4. Lemma 4.5 (`lem:smooth-calculus`) and the lemmas read with it

| claim (line) | check | result |
|---|---|---|
| `‖w‖_{J,sep} ≪ p_{J+d+2}(w)` (1124-1127; 1213-1221) | Integrating `(1−Δ)^m` by parts bounds `(1+\|t\|²)^m \|ŵ\|` by `vol(Ω) C_{m,d} p_{2m}(w)`. Then `∫(1+\|t\|)^J(1+\|t\|²)^{−m}` is finite iff `2m > J+d`, and the least such `m` has `2m ≤ J+d+2`. | correct; **S2** (exact over `J < 30`, `d < 8`) |
| monomial separation formula (1128-1135) | Fourier inversion of `w_log` at `u_j = log c_j + Σ_ℓ a_{jℓ} log y_ℓ`; `ŵ ∈ L¹` | correct |
| Minkowski passage (1136-1139; 1222-1228) | displayed with `(2π)^{−d}`; it needs one common measure, which the text requires | correct |
| `eq:parameter-sobolev` (1141-1147; 1230-1235) | 1-D: FTC, averaging the base point over a length-3 interval, then Cauchy-Schwarz. This gives the explicit constant `sup_I\|F\|² ≤ (2/3)∫\|F\|² + 6∫\|F'\|²`. Iterating over coordinates gives the mixed `α ∈ {0,1}^d` terms with constant `≤ 6^d`. Summing over rows before the sup is legitimate, since every term is nonnegative. | correct; **S4** (max ratio 0.50) |
| covering costs (1148-1151; 1236-1247) | A log range of length `O(log Z)` gives `O(log Z)` unit boxes. Heights give `∫_{[−T1−1,T1+1]^{d_t}}(1+\|t\|)^H ≪ (1+T1)^{H+d_t}`. A scale derivative inserts `yW'` and a constant. | correct (the twist must be normalized, as the text says) |
| `eq:late-fourier-tail` (1153-1158; 1249-1250) | `(1+\|t\|)^{−N} ≤ T1^{−N}` on `\|t\| > T1`; the constant is exactly 1 | correct |
| Mellin twist shift (1159-1163) | definition | correct |
| `eq:pointwise-mellin-tail` (1164-1180; 1250-1263) | `F_σ(u) = e^{σu}W(e^u)`. `N` integrations by parts give `(−iT)^{−N}` and Leibniz gives `Σ C(N,j)σ^{N−j} D^jW`. `\|T\| < 1` is handled by the absolute integral. The boundary terms vanish for annular `W` (any `σ`) and for `W` smooth at 0 and Schwartz at ∞ (`σ > 0`). | correct; **S1** (rel. dev. 4.8e-12 on `W_G`, Mellin `e^{s²}`; controls `(iT)^{−N}` and no-binomial detected) |
| `eq:joint-gaussian-slice` (1181-1197; 1265-1272) | Uses `1+\|T\| ≤ (1+\|T+v\|)(1+\|v\|)` and `1+\|T\|+\|v\|+\|w\| ≤ 2(1+\|T+v\|)(1+\|v\|)(1+\|w\|)`. Both are exact, by `\|T\| ≤ \|T+v\| + \|v\|`. Then integrate the Gaussian in `T+v`. | correct; **S3** (the factor 2 is needed: 447 violations without it) |
| integrated tails, block-triangular map (1193-1199; 1273-1280) | a fixed invertible linear map changes polynomial weights by fixed factors | correct |
| tail bookkeeping (1201-1210) | the order `N + ⌈J⌉` in the pointwise bound gives `Z^B T1^{−N}` on a join at height `≍ T1` | correct |

**Uses spot-checked.**
* Lemma 5.3 (2576) applies the lemma with `j = J+d+2`.
* Lemma 8.2 (4450-4453) uses the pointwise bound with order `N+⌈J⌉+1`, one more than needed.
* Sec. 17 (9645-9710) states the common-measure requirement and the order of choices (`τ` before `N`) consistently with 1201-1210.

**Verdict on Lemma 4.5: no wrong step found.** It is standard, and its constants and derivative
orders are as stated.

**Lemma 4.7 (`kernel-seminorms`, 1347-1413).**
* The Fourier part holds with order `⌈A⌉+|β|`.
* The radial part: `r∂_r ↔ (ξ·∂_ξ)/2`. The paper says "finitely many" seminorms; `s_{⌈2A⌉+2j}` suffices, since `r = |ξ|²`.
* The Mellin part: `(x∂_x)^j` inserts `(−s)^j`, and more than `h+j+1` integrations by parts make the `t`-integral converge.
* The twist bound uses `(1+|v+ω|)^{h+j} ≤ (1+|v|)^{h+j}(1+|ω|)^{h+j}`.

No wrong step found.

**Lemma 4.9 (`logarithmic-control`, 1531-1600), with Lemma 4.8 (1425-1529) as input.**
* The radii are `R_j = 2−a−je`.
* Borel-Carathéodory goes from `R3` to `R4`: the gap `e` gives `|g| ≪_e log 𝒞`. This uses only an upper bound for `Re g` (Lemma 4.8 on `Re s ≥ a+3e ≥ 1/2`, Euler beyond 11/10) and `|g(2+it)| = O(1)`.
* Hadamard three circles uses `r0 = 49/100 < R6 < R4`, with `θ < 1` uniformly for `a ∈ [1/2,1]`. This gives `|g| ≪ (log 𝒞)^θ`, hence the `𝒞^ε` bound for `L^{±1}`.
* Cauchy from `R6` to `R8` gives `|g'| ≪ (log 𝒞)^θ`, which is stronger than the stated `log 𝒞`.
* The global clause needs `a = b ∈ [1/2,1]`. This holds because `β* ≥ 1/2` by definition (old-eq:1.1b, l. 378).

Lemma 4.8:
* On `Re s = −1/10`, the functional equation gives `(3Q)^{3/5}`, and Stirling gives `|t|^{1−2σ} = |t|^{6/5}`.
* The damped Phragmén-Lindelöf factor satisfies `|e^{δ(s−1/2)²}| ≤ e^{9δ/25}`.
* The theta and Poisson normalization `2/(√3 v)` and the exponent `4π|b−h/f|²/(3v)` were re-derived from the self-dual measure.

Lemma 4.10 is elementary and correct. **No wrong step found** in Lemmas 4.7-4.10 as read.

## 5. Mechanical checks (`sep30_l13_checks.py`)

```
   N/A: prime lambda has norm 3; (N-1)/6 = 0.3333333333333333 is not an integer, so it lies in S and chi is undefined
   N/A: prime 2 has norm 4; (N-1)/6 = 0.5 is not an integer, so it lies in S and chi is undefined
PASS A1 eq:correlation-lift (F = 0 unless C|j; chi_n1(k) conj chi_n2(-k) R(n1,n2) L_C) for every j, 21 configs   2631375 (u,v,j) values, 0 mismatches
PASS A2 L_C congruence sum = product of closed local factors (genuine locus, every k mod C)   1615 (C,k) values, 0 mismatches
PASS A3 F(u,v;0) = phi(u) 1_{u=v}
PASS A4 |L_C| <= q_C on every computed value
PASS A5 R(n1,n2) from symbols = four-class bicharacter r (eq:reciprocity-four-class)
PASS B1 eq:correlation-local + one-sided formula, local factor L_{p^c}: grid (split 7,13; inert 5,11) and Z/7^c enumeration (c=4..7, incl. 6|c)   291296 (n1,n2,k) cases, 0 mismatches
PASS B2 field-level sweep: modulus p, character chi_p^c, c=1..12 (principal branch at inert 5, 11)   0 mismatches
PASS B3 genuine L_{p^c} periodic modulo p in each column (n_i -> n_i + p), c<=3
PASS C1 eq:correlation-child-character, every j mod DEab, 15 configs   1139157 (config,j) values, 0 mismatches
PASS C2 the configurations realise each R-factor = -1 at least once   {'R(a,E)': [0, 3], 'R(b,D)': [0, 3], 'R(a,b)': [0, 3]}
PASS X1 at p | (n1,n2) the congruence sum is not the artificial value 0 (paper's own caveat, l. 7123-7131)   7 nonzero congruence-sum values where the extension is 0
PASS X2 F~_{D,E}(a,b;j) != F(Da,Eb;j) at some non-coprime (a,b) (paper: 'artificial', l. 7243)   27 differing (a,b,j) values
PASS X3 Moebius insertion: sum_{(a,b)=1} c F(Da,Eb;j) = sum c F~ sum_{t|a,b} mu(t) (exact)
PASS D1 Fourier form of F (Lemma 13.3, first display) exact in Z[zeta_L], 6 configs (split, inert)   916 (config,j) values, 0 failures
PASS D1c control: G(u,h) G(v,h) without conjugation is detected   7 failing j
PASS D2 Lemma 13.2 (eq:gauss-local) exact: |S|^2 = P^{2a-1} 1_{v=a-1} (6!|a) and S integer formula (a=6, P=7)   797 (p^a,k) values, 0 failures
PASS N control eq:correlation-local mutated 'minus1' is detected   206928 mismatches
PASS N control eq:correlation-local mutated 'orient' is detected   112176 mismatches
PASS N control eq:correlation-local mutated 'P2' is detected   23840 mismatches
PASS N control eq:correlation-local mutated 'onesided_no6' is detected   39504 mismatches
PASS N control eq:correlation-lift mutated 'dropR' is detected   12960 mismatches
PASS N control eq:correlation-lift mutated 'chi2_plus' is detected   18366 mismatches
PASS N control eq:correlation-lift mutated 'phi_q' is detected   1 mismatches
PASS N control eq:correlation-lift mutated 'orient' is detected   34224 mismatches
PASS N control eq:correlation-lift mutated 'minus1' is detected   33570 mismatches
PASS N control eq:correlation-child-character mutated 'drop_Rab' is detected   35100 mismatches
PASS N control eq:correlation-child-character mutated 'drop_RaE' is detected   42174 mismatches
PASS N control eq:correlation-child-character mutated 'chib_plus' is detected   50184 mismatches
PASS S1 eq:pointwise-mellin-tail IBP identity on W_G (sigma in {-1,.3,2}, T in {.7,1.5,3}, N<=5) [FLOAT]   max rel dev 4.8e-12
PASS S1c controls: (iT)^{-N} for odd N, and dropping the binomial weights, are detected [FLOAT]   rel dev 2.00, 174.70
PASS S2 smooth-calculus order: least m with 2m > J+d has 2m <= J+d+2 (J<30, d<8; exact)
PASS S3 joint-slice inequalities hold on 2e5 Cauchy samples; the factor 2 is needed (control) [FLOAT]   factor-1 violations: 447
PASS S4 1-D parameter-Sobolev with explicit constant (2/3, 6): max sup/rhs over 300 tests <= 1 [FLOAT]   max ratio 0.504
33/33 PASS   (114 s)
```

**Failing controls (part N).** Every mutation is detected by an exact mismatch:
* in `eq:correlation-local`: `−1→+1`, orientation `n1/n2→n2/n1`, `P−2→P−1`, and dropping `1_{6|c}` from the one-sided factor;
* in `eq:correlation-lift`: dropping `R`, `χ_{n2}(−k)→χ_{n2}(k)`, `φ(u)→q_u`, and the two local mutations;
* in `eq:correlation-child-character`: dropping `R(a,b)`, dropping `R(a,E)`, and `χ_b(−j)→χ_b(j)`.

**Part D1c** (no conjugation on `G(v,h)`) is also detected.

**Exactness.** All values in A, B, C and X are integer pairs in `Z[ω]`. D reduces integer
group-ring vectors modulo `Φ_L`, which sympy supplies. Only S uses floats, and its tolerances
are printed.

**Limits.**
* The configurations are small, with norms up to about `10^6` in `uv`.
* The principal branch `6 | c` is reached by enumeration only at `P = 7`, `c = 6`. At the inert primes it is reached only through the field-level sweep (B2) combined with the separately checked lift count `P^{c−1}`.
* No asymptotic or uniformity claim is tested.

## 6. Verdicts

| Lemma | Verdict | Notes |
|---|---|---|
| 13.3 full correlation | **no wrong step found** | all displayed identities exact on 21 global configurations (2,631,375 values of `j`) and 291,296 local `(n1,n2,k)` cases; `\|L_C\| ≤ q_C` has slack (`≤ P^{c−1}(P−1)` locally) |
| 13.4 complete-support correlation | **no wrong step found** | the off-locus warning (`F~ ≠ F`) is necessary (X2) |
| 13.2 prime-power sums (dependency) | **no wrong step found** | now exact-checked (D2) |
| 4.5 smooth calculus | **no wrong step found** | orders `J+d+2` and `N+⌈J⌉` are right; explicit Sobolev constant `6^d` |
| 4.7 kernel seminorms | **no wrong step found** | radial order `⌈2A⌉+2j` suffices |
| 4.9 logarithmic control (and 4.8, 4.10) | **no wrong step found** | log-derivative bound is in fact `(log 𝒞)^θ` |

**Status-map consequences.** In SEP30_VERIFICATION_MAP.md, Lemmas 13.3, 13.4 and 4.5 move from
U to R, with the verdict "no wrong step found" and the scope above. Lemmas 4.7 and 4.9 move from
U to R as well, for a bounded reading. Target 5's first unverified point is unchanged: the
analytic claim that one Fourier measure separates the kernels for all live labels in Lemma
18.1's bridges. That claim *uses* Lemma 4.5, which is now reviewed. The bridges themselves are
not reviewed here.
