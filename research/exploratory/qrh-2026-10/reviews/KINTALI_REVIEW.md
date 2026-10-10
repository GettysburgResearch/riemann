# Bounded review: Kintali, "A Short Proof of the Quasi-Riemann Hypothesis" (7 Oct 2026)

```text
Status: REVIEW (bounded; external manuscript)
Scope: [K] Sec. 4.1 (Lemma 5, global reciprocal bound (15), Lemma 6, density display, (16)),
  Lemma 2 (conductor and multiplicity), Sec. 4.3-4.4 (exponents (22)-(23), monotonicity in d,
  v = 4000, Lemma 7 arithmetic), Sec. 5.1 constants; the GL hypotheses and orientation for (11) and
  the bookkeeping in Lemma 4, spot-checked only. Not checked: Sec. 2.2-2.3 constructions (2), (4),
  (5)-(6); Appendix A (table (A.4), local factor (8)); Lemma 3 and Appendix B (the cusp and
  multiplier computations); (14); Sec. 4.2 monomial table (17)-(21); tail bounds.
Exact sources or dependencies:
  [K] PDF sha256 f7ddc46632e37466e85951ea67acbd3c2abc19c8259fac51be569b1f6bbbe8e5
  [K ref 4] T. Khale, C. O'Kuhn, A. Panidapu, A. Sun, S. Zhang, "A Bombieri-Vinogradov theorem for
     primes in short intervals and small sectors", J. Number Theory 229 (2021) 142-167 (journal and volume confirmed via NSF PAR record; page range as cited by [K], unconfirmed),
     arXiv:2008.09677v3 (12 Jan 2022), Lemma 3.3; fetched PDF sha256
     1e92b7ce59924f4a839a9168fff5de00a4796f415f76ada9d262a893236e8ee2
  [Hinz] J. Hinz, "Über Nullstellen der Heckeschen Zetafunktionen in algebraischen Zahlkörpern",
     Acta Arith. 31 (1976) 167-193, Satz A and Satz B (only the statement page was read; scan
     matwbn aa3127.pdf sha256 5349862b73cc44197ced0a4edc913b79bf16195dcce5b6c766e3adaf2a54ed71)
  [Duke] W. Duke, Acta Arith. 52 (1989) 203-228, Thm 1.1 and Thm 2.1 and the remark after it
     (scan aa5231.pdf sha256 1a6e8b792029a32fb7da1e3edbda1780b488f07ce7e6450b0797aa97eb04d3a4)
  [GL] Goldmakher-Louvel, arXiv:1112.1642v2, Definition 1, Thm 1.1, Cor 1.2 (sha256 5cc5f03388d3996b4333f07be51f989f60779fe172f8bd24c7aa6ddad64dd304)
  [OAI] OpenAI 7/8 manuscript (sha256 8fe93046...99e7), used only to map dependencies
What was actually run: read [K] in full (pp. 1-27) and [K ref 4] Sections 1-3; read the statement
  pages of [Hinz] and [Duke] and GL Definition 1 / Thm 1.1 / Cor 1.2. Ran
  kintali_exponent_check.py (sympy + exact Fractions) for (22), (23), E(d,a), the dyadic sum at v=4000,
  the 29/30 maximum with R(a)=min(1,5(1-a)) and with Hinz Satz A alone, and 149/4800. All match [K].
Smallest remaining gap: Lemma 3 (weak reflection, p. 8 eq. (12); proof App. B pp. 22-26) and the exact
  identities (4) and (5)-(6) (p. 5; App. A pp. 18-22). These were not verified here. Lemma 4, and with
  it the low bound J << Z^{1/4+eps}, rests on Lemma 3.
```

RH is not touched by this paper. [K] claims a zero-free half-plane `Re s > 47/48`, which is
weaker than the 11/12 half-plane of [OAI] Part I. Nothing below is a repository result. The verdict
is limited to the steps listed under Scope.

## 0. Verdict

**Every step I checked holds.** I found no error in Sec. 4.1, Lemma 2, Sec. 4.3-4.4, or the
constants in Sec. 5.1. There is one citation-level defect and two cosmetic points (Section 1.4):

* **p. 12, density display.** [K] calls [K ref 4, Lemma 3.3] "the published general Hecke
  zero-density theorem". In [K ref 4] that lemma has only a short sketch. The `3/(2-σ)` branch is
  reduced to Duke's fixed-modulus theorem "with Theorem 1.1(ii) in place of (i)". The `2/σ` branch
  is justified only by pointers to Montgomery, Hinz and Coleman. The fragment [K] actually uses
  (angular type zero) is, however, a fully published theorem: **Hinz 1976, Satz A/B**. Moreover,
  **only the `3/(2-σ)` branch (Satz A) is load-bearing for 47/48** (Section 1.3). This is a citation
  repair, not a mathematical gap.

The first step that is **unverified**, as opposed to wrong, is listed under Smallest remaining
gap above.

## 1. Reference [4] and the zero-density input

### 1.1 What [K ref 4, Lemma 3.3] states (arXiv v3, p. 18)

> There is a constant B > 0 such that for all σ ∈ [1/2, 1], R > 1 and M > 2,
> Σ_{N a ≤ R} Σ*_{μ mod a} Σ_{m ∈ Z^d, ||m|| ≤ M} N(σ, M, μλ^m) ≪ (R² M^n)^{min(3/(2−σ), 2/σ)(1−σ)} (log RM)^B.

* **Field.** `K/Q` is a finite Galois extension of degree `n`, and `d = n − 1`. `Q(√−3)` qualifies,
  with `n = 2`, `d = 1`. Then `R² M^n = Q² T²`, matching [K].
* **Family.** By Sec. 1.1 of [K ref 4], `μ` runs over characters of the narrow ray class group `I_f/P_f`.
  For an imaginary quadratic field narrow and wide coincide, so the `m = 0` slice runs over **all
  primitive finite-order Hecke characters of conductor norm ≤ R**. The `λ^m` with `m ≠ 0` have
  nontrivial infinity type and so are not of finite order. Keeping only `m = 0` drops nonnegative
  terms. [K]'s "angular type zero" restriction is therefore legitimate.
* **Uniformity.** The bound is stated for all `σ ∈ [1/2, 1]`, `R > 1`, `M > 2` with one constant `B`.
  Height and angular range share the same `M`; [K] needs height only.
* **Exponent.** `h(σ) = min(3/(2−σ), 2/σ)` as stated. Its maximum is `5/2`, attained at `σ = 4/5`,
  so `2h(σ)(1−σ) ≤ 5(1−σ)`.
* **Proof status.** It is a sketch. The R-uniform `3/(2−σ)` bound is said to "follow from work of
  Duke" ([Duke] Thm 2.1, fixed modulus) by switching to his hybrid large sieve [Duke, Thm 1.1(ii)]:
  `Σ_{q≤Q} Σ*_{χ mod q} Σ_{|m|≤T} ∫ |Σ c(a) χλ^m(a) N(a)^{it}|² ≪ (N + Q²T^n) log⁴(QT) ||c||²`.
  I confirmed that statement on the scan. The `2/σ` improvement is attributed to Montgomery, Hinz
  and Coleman with no further detail.

### 1.2 Independent published source for the fragment [K] uses

Immediately after his Theorem 2.1, Duke remarks that the conductor-uniform version summed over
`q ≤ Q`, without the m-aspect, "has been done by Hinz". **Hinz (1976), p. 168** proves, for any
number field `K` of degree `n`, summing over **all integral ideals `q` with `Nq ≤ Q` and all
primitive characters of the narrow ray class group mod `q`**, with `Q ≥ 1` and `T ≥ 2`:

* **Satz A(a)** (`1/2 ≤ σ ≤ 1 − 1/(2n)`): `≪ {Q² T^{(2/3)n(2−σ)} (log QT)^{3n}}^{3(1−σ)/(2−σ)} (log QT)^{10}`
* **Satz A(b)** (`1 − 1/(2n) ≤ σ ≤ 1`): `≪ {Q² T^b (log QT)^{3n}}^{3(1−σ)/(2−σ)} (log QT)^{10}`, with `(2n+1)/3 ≤ b ≤ n`
* **Satz B** (`3/4 ≤ σ ≤ 1`): `≪ (Q² T^n)^{2(1−σ)/σ} (log QT)^c`, with `c` bounded
* All implied constants depend only on `K`.

For `n = 2`, the Q-exponent is exactly `2h(σ)(1−σ)` with [K]'s `h`. The T-exponent is polynomial
and never larger than [K]'s `T^{2h(1−σ)}`. [K] only needs some fixed power of T, absorbed into
`(3+T)^A` with `T = 3Z^τ`. I read the statements only, not Hinz's proof. Hinz is a refereed Acta
Arithmetica paper and a direct analogue of Montgomery's Theorems 12.1-12.2.

### 1.3 Which branch is load-bearing

Using only Satz A, `R(a) = min(1, 6(1−a)/(2−a))`. Both branches equal 1 at `a = 4/5`. For
`a ≥ 4/5`, `d/da [a + 3(1−a)/(2−a)] = 1 − 3/(2−a)² < 0`. So `max_a [a + R(a)/2 − 1/3] = 29/30`
is still attained at `a = 4/5`. The script checks this exactly on a 1e-5 grid and symbolically.
The d-slope `R(a) + a − 21/25` stays in `[4/25, 24/25]`. **The `2/σ` branch, the least-documented
part of [K ref 4], is not needed for 47/48.**

### 1.4 Minor points (non-fatal)

* [K] restricts to `1/2 ≤ σ < 1` and adds "at a possible label a = 1, take σ ↑ 1". The case is
  vacuous: labels satisfy `a ≤ M_u < 1`, because nonprincipal Hecke L-functions do not vanish on
  `Re s = 1`.
* [K] credits "[4, Lemma 3.3]" with a theorem whose proof there is a sketch. A corrected citation is
  Hinz 1976 Satz A, optionally with Satz B, or Duke 1989 together with Hinz.

## 2. Section 4.1 and Lemma 2: checked items

| Item | Check | Result |
|---|---|---|
| Lemma 2 conductor `O(U)` | Tame local Kummer character has exact order 6 on units and is trivial on `1+p`, so conductor exponent 1 iff `1 ≤ v_p(u) ≤ 5`. Hensel bound `m > 2v_p(6)` at S. Twists in Θ are fixed. Conductor divides fixed ideal × rad(u). | holds |
| Lemma 2 "twelve rows" | Given the primitive character and `ε`, the inertia restrictions fix `ε v_p(u) mod 6`, hence each `v_p(u) ∈ {0..5}`, hence the ideal `(u)`. That gives 6 generators per ideal and 2 orientations. ν ∈ Θ is unramified outside S. | holds |
| Principal-row exclusion (Sec. 2.5) | `n ≡ π = −2−3ω (mod 36)` gives `Nn ≡ 7 (mod 36)` and `χ_n(u) = u^{(Nn−1)/6} = u ≠ 1` | holds |
| Lemma 5 (zero-free disk) | Borel-Carathéodory on `R3 → R4` (gap e), then three circles with inner radius `r0 = 49/100` (Euler region). `R6 > r0` for `a ≤ 1`, `e < 10⁻³`. θ_e < 1 uniformly by compactness. `exp(C(log C)^θ) ≪ C^δ`. Same as [OAI] Lemma 4.9. | holds |
| (15) global reciprocal | Disks with `a = β*` are zero-free at every height by definition of β*. Principal case via `(s−1)ζ_F/(s+1)`. Deleted factors cost `(N rad u)^δ`. | holds |
| Lemma 6 labels | `a = 51/100 + e⌊(M_u−51/100)/e⌋`, so `a ≤ M_u < a+e`. The disk at `2+it`, `|t| ≤ T`, radius `2−a−2e`, has `Re s > a+2e > M_u` and `|Im s| < T+1.49 ≤ 2T`, so it is zero-free. Item 3: FE costs `Q^{a−1/2+6e}`, deleted factors at `Re w ≥ −6e` cost `U^{6e+δ}`, and the conjugate lies in `X_u` (Θ conjugation-stable, ε → −ε). | holds |
| (16) | Each row with `a > 51/100` maps to a primitive character of conductor `≤ C·2U` that has a zero in `[a,1] × [−2T,2T]`, and at most 12 rows map to one character. So `#B_a ≤ 12 Σ N(a, 2T, ψ) ≪ U^{5(1−a)+δ}(3+T)^A`; take the minimum with the trivial `O(U)`. | holds (citation per Section 1) |
| Labels near 1 | `R(a) = 5(1−a) → 0` gives `#B_a ≪ U^δ (3+T)^A (log)^B`, uniformly in σ ([K ref 4]; Hinz constants depend only on K) | holds |

## 3. Spot-checks of Lemma 3 / Lemma 4 against GL

* **GL hypotheses.** GL Definition 1 asks for a family `{χ_a : a ∈ I(c) squarefree}` of primitive,
  trivial-infinity-type characters of order dividing 2, a reciprocity law `χ_a(b) = χ_b(a)C([a],[b])`
  with finite `G`, and primitivity of `χ_aχ_b` mod `ab` when `[a] = [b]`. [K]'s `θ_R((x)) = (x_prim/R)_2`
  has conductor `R λ^{e(R)}`. The class map is a ray class mod 4 (or 36), which fixes `e(R)`, so the
  λ-parts cancel in products. Reciprocity is the cube of (A.2) with `R³ = R`. Consistent.
* **Orientation.** GL Thm 1.1 sums the outer index over arguments `a` and the inner index over family
  indices `b`. [K] (11) puts the family index R outside. The bound `(MN)^ε(M+N)` is symmetric and
  `||A|| = ||Aᵀ||`, so transpose duality alone gives (11); reciprocity is not needed. This paragraph
  of [K] is a close paraphrase of [OAI] Sec. 5.4.
* **Lemma 4 bookkeeping.** `|d(μ)|/q_μ^{1/2} ≤ 27·3^{−k/3}N^{−1/2}B^{−1}` follows from the stated
  support bound. Minkowski over `O(B)` values of `b` costs `B`, cancelled by `B^{−1}`, giving (13).
  Square roots of the two terms carry `3^{−k/3}` and `3^{−5k/6}`. The block cut-off yields
  `Z·(D0/p0 + D0³/p0²) ≤ 2Z p0^{−1/2}`. The sum over powerful `P` is `≪ log Z`. Discarded blocks are
  `O(Z^{5/4−Aτ})` per row. All consistent. The structural inputs from Lemma 3 (the R-dependence
  being only `ζ_R`, `χ_R(·)^3` and `q_R` in the kernel after a fixed ray subdivision) are **assumed,
  not verified**.
* **(14) and Sec. 3.3.** `(Q + Y²)/Y` with `Q ≍ Z`, `Y = Z^{1/2}` gives `Z^{1/2}`. Then
  `Z^{−1/2}·Z^{1/4}·Z^{1/2+ε} = Z^{1/4+ε}`. Exponent-level only.

## 4. Sections 4.3-4.4: exponents (exact; script output)

* **(22).** At `(a+16e, 1−a−6e, 17/50)`, `x+z/2+w/2−5/4 = a/2 − 3/4 + 17/100 + 13e`. The U-power is
  `(a−1/2) − 17/50 = a − 21/25`. Relative to `C(β*) = β* − 2/3` the constant is `13/150`. So
  `E(d,a) = a/2 − β* + 13/150 + d(R(a)+a−21/25)` and `E(1/2,a) = a − β* + R(a)/2 − 1/3`. ✔
* **(23).** `Ew: −1/8 + 3e/2`; `Ez: −1/48 + e`; unit rows `−49/300 + e`; large rows
  `Z^{7/4+v/2}U^{1−v}`. ✔
* **Monotonicity.** `R(a) + a − 21/25 ∈ [4/25, 24/25]`, which is positive and at most 1, so `E`
  increases in `d`. Then `E(d,a) ≤ −1/80 + 1/1000 = −23/2000 < −1/100`. ✔
* **v = 4000.** The sum over `U > Z^{501/1000}` gives `Z^{7/4 + 501/1000 − v/1000} = Z^{−1749/1000}`. ✔
  Moving z to `Re z = 4000` crosses no pole (M is holomorphic for `Re z > 0`, and `ζ_F(6z)` is
  fine). The constants are large but fixed.
* **Lemma 7 / Sec. 5.1.** `m0 = 1/1200 < 23/2000`; `C(b) − δ0 − 9/32 = 149/4800`;
  `b − δ0 = 4699/4800 > 11/12`, so `|H_η| ≥ 1/2` applies. ✔
* **Lemma 6 geometry.** `R2 = 2−a−2e`, `R6 = 2−a−6e > 49/100` on `[51/100, 1]`. ✔

## 5. Dependence on the OpenAI manuscript; does [K] shrink the unverified surface?

[K] cites [OAI] for no lemma. Every step has an in-paper proof. Substantively, most of [K] is a
compressed re-derivation of [OAI] **Part I** (the 11/12 theorem, [OAI] Thm 3.1 and Sec. 4-11). Note:
[OAI] has no Appendix A of its own. The "Appendix A" both papers rely on is Dunn-Radziwiłł's (cusp
expansions), and [K]'s own Appendix A re-derives [OAI] Sec. 4.2 and Sec. 7.

| [K] | [OAI] counterpart | Status in [K] |
|---|---|---|
| Sec. 1, Sec. 5.1 (continuation, contradiction) | Sec. 2 Prop. 2.1, Sec. 11 | re-proved (standard; read) |
| Sec. 2.1-2.2, App. A.1 (Γq, G, R, sextic reciprocity, Gauss-Jacobi) | Sec. 4.1-4.2, Lemmas 4.2-4.4 | re-proved; **not checked** |
| Sec. 2.3 (4), `A_{m,σ,v}`, `B_{m,σ}` | Sec. 6.1, eq. (6.2) (near-verbatim) | **not checked** |
| (5)-(6), App. A.2-A.3, (8) | Sec. 7.1-7.2, Lemma 7.1 | **not checked** |
| Lemma 2 | Lemma 4.1, Sec. 9.2 | checked |
| (11) GL conductor check | Sec. 5.4 (near-verbatim) | checked |
| Lemma 3 / App. B (weak reflection, `|ζ_R| ≤ 1/81`) | Prop. 5.1 (Sec. 5.1) | **not checked**; load-bearing |
| Lemma 4 (balanced energy) | Lemmas 5.5-5.8 (replaced by a simpler argument) | bookkeeping checked |
| (14), Sec. 3.3 | Lemmas 6.1-6.2, Prop. 6.3 | exponent-level only |
| Lemma 5 | Lemma 4.9 (near-verbatim) | checked |
| Lemma 6 | Lemma 8.1 (simplified: one height level) | checked |
| (16) via Hinz / [K ref 4] | **replaces** Sec. 8.2 (saturated witnesses) and Sec. 9 (sextic large sieve, Prop. 9.2) | checked modulo the citation |
| Sec. 4.2-4.4 | Sec. 10, Sec. 11.1 | exponents checked; monomial table not checked |
| Sec. 5.2 | Prop. 11.3 | read |

**Assessment.** For a weaker conclusion (47/48 instead of 11/12), [K] removes from the trust base:
* the zero detector and sextic large sieve ([OAI] Sec. 8-9, about 15 pp.);
* the collision lemmas of [OAI] Sec. 5.4-5.5;
* all of [OAI] Part II.

In their place [K] puts a classical published density theorem (Hinz 1976) and a short energy argument.

What remains unverified is the shared core:
* the probe and its two exact representations ([OAI] Sec. 4, 6.1, 7; [K] Sec. 2, App. A);
* the cubic-theta reflection ([OAI] Prop. 5.1; [K] Lemma 3, App. B).

So [K] does shrink the unverified surface, but not to zero. A full verification of [K] still needs
an independent check of [K] App. A-B or [OAI] Sec. 4-7. [K] is not an independent confirmation of
[OAI]'s 7/8 or 11/12. It reuses the same probe mechanism.

## 6. Not done

* No line-by-line check of Lemma 3 / App. B: cusp normalization, multiplier (B.2), the claim that
  `d` and `ϑ` are R-independent after a fixed subdivision, and Mellin normalization (B.3).
* No check of the Poisson representation (5)-(6), the local table (A.4), or (8).
* No check of the Sec. 4.2 monomial table or the tail bounds.
* Hinz's and Duke's proofs were not read; only their statements were.
