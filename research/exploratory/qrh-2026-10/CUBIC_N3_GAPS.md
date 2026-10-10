# The three n = 3 gaps of the cubic fourth-moment route: local tables, Kummer lemma, centred stage

```text
Status: EXPLORATION with PROPOSED written proofs of the cubic finite lemmas and EXACT finite checks
  (38/38 PASS; 14 failing controls detected: 10 dedicated CTRL lines and 4 inside [E]). All three
  red-team gaps close at the level of the displayed steps: no loss of order M was found. The cubic
  fourth moment stays CONDITIONAL (Sec. 4) and OPEN. No moment bound is proved. RH is not addressed.
Scope: the n = 3 gaps listed in reviews/CUBIC_NESTED_REDTEAM.md Sec. 6, items 2-3:
  (1) cubic correlations at prime powers, including the unequal case j0 = 3, and the cubic
      common-support allocation;
  (2) the Kummer / fixed-numerator-ray lemma with mu_3 in place of mu_6;
  (3) the centred-stage saving at n = 3 (comparison length L up to about 0.42M, F_1 + F_2 >= (5/6)v,
      total loss below M/12).
  Case 1 (z = 0) of Lemma 18.1 only. The order-independent machinery of the sextic proof is
  inherited, not re-proved.
Exact sources or dependencies:
  repo HEAD ce9ee8bdbc684d53f1392a513eceb8629fffd187 (branch claude/peaceful-faraday-ki4ewu).
  pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
    The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, sha256 42a5ee0f...deac6a3
    (re-hashed; untrusted data). Read: l. 555-720 (conventions, Lemma 4.1 fixed-numerator-ray),
    1040-1090 (row fixed-ray reduction), 7042-7245 (finite correlations), 12477-12610,
    12686-12712, 12780-13015, 13074-13090, 13176-13186, 13350-13410, 13596-13870, 13934-13975,
    14312-14815. Every occurrence of the order (6, "sixth", "mod six") in l. 12477-14973 was
    grepped and catalogued (Sec. 3.1).
  Notes read in full: CUBIC_FOURTH_MOMENT_TRANSFER.md (f86b7e26...), CUBIC_RELAXED_INDUCTION.md
    (5ec47bca...), reviews/CUBIC_NESTED_REDTEAM.md (56a174b2...), reviews/LEMMA18_1_REVIEW.md,
    reviews/LEMMA18_1_COMMON_SUPPORT.md, with reviews/lemma18_support_checks.py (509a3dbb...) and
    reviews/lemma18_local.py. Section 6 of reviews/LEMMA18_1_CASE2_SEC188.md (imported-inputs list).
  Code: scripts/cubic_local_checks.py (NEW; sha256 10cab5ec...b5a86c29, working tree). It imports
    a2/eis.py read-only (sha256 87ca11d9...2798e65, unchanged). Other processes committed this
    script without my action: checkpoint ce9ee8bdb holds an earlier draft, and the copy at
    901ca763c is identical to the version that was run (sha256 10cab5ec...b5a86c29).
What was actually run:
  nice -n 10 python3 -I scripts/cubic_local_checks.py -> 38/38 PASS, 200 s wall, one process.
  Log: session scratchpad cubic_n3/run2.log (also copied there as cubic_local_checks_output.txt).
  An earlier run (run1.log) had 36/38: a float leak in [A3] and a misplaced control. Both were
  fixed before the final run.
  Arithmetic: EXACT. Character values are pairs in Z[omega]. Sums with additive characters are
  integer vectors over Z/N, tested for zero modulo Phi_N; this is exact because 3 does not divide
  N. The sympy ledger is symbolic. No floating point is used in any PASS criterion.
Smallest remaining gap: nothing order-dependent remains open at the level of displayed steps. The
  route now needs (A) the order-independent analytic core of Lemma 18.1, case 1: Lemmas 4.5
  smooth-calculus and 4.7 kernel-seminorms, and the fact that the displayed ledgers describe the
  analysis. It also needs (B) the PROPOSED nested comparison ordering. The single most load-bearing
  inherited statement is the centred-coefficient invariance (Lemma centered-coefficient-invariant,
  l. 13954) together with lattice cancellation. At n = 3 they must cancel the Theta-row main terms
  to relative precision Z^{-(A - 2M/3)}, which is about Z^{-M/3}; the sextic proof needs only
  Z^{-M/6}.
```

RH is unsolved. This note proves nothing about RH, about Lemma 18.1, or about cubic moments.
"Closes" means that the displayed affine exponent ledgers balance once the stated finite lemmas
hold. The finite checks are exact computations on small moduli: they verify identities on those
cases and do not prove the lemmas.

## 0. Verdict per gap

| gap | result | label |
|---|---|---|
| (1) cubic local correlations, `j0 = 3`, common-support allocation | The paper's lemmas hold for n = 3 with `6 → 3`. Every proof uses the order only through "`χ_p` has exact order n on `(O/p)^×`". Every brute-force table matches exactly, including `(4,3)`, `(5,3)`, `(3,4)`, `(3,5)` and `D = E = p³`. The unequal `j0 = 3` case is **not tight**: `F_2 − b_2 = (i−3)/2 ≥ 1/2`. | PROPOSED proof + EXACT checks |
| (2) Kummer / fixed-ray with `μ_3` | Holds, and is simpler: ramification only above `3a`; `27 = 3^{|S|+1}` numerator characters, not `6^{|S|+1}`; trivial reciprocity bicharacter and `χ_n(−1) = 1`; exceptional rows `(h') = 𝔥_0𝔳³`, count `Z^{(m'−f)/3}`. One thing changes: at nonunit primes of multiplicity 1 the forcing gives `q_{𝔥_0} ≥ Z^{v_1}`, so `f = v_1` with **no spare**. The sextic keeps a spare `f/6` there. | PROPOSED proof + EXACT checks |
| (3) centred stage | Lattice cancellation is order-free and gives `r = (L − v)_+` whenever `L ≤ min(A/2, A − M/2)`. That cap also makes the short-plain branch vacuous. The cubic exponents are exact: deficit `A − 2M/3 − F_1 − F_2 − (L−v)_+ ≤ A − 2M/3 − (5/6)L`. Explicit losses are terminal: `4σ/3 + (2/3)δ_fr,1 + δ_fr,2/3 + 2θ_N + ε_1 (+δ)`. **No loss `cM` was found, for any `c > 0`.** The two-stage uniform margin is `0.0179M` (A ≤ M) and `0.0155M` (A ≤ 1.01M). | ledger EXACT; scheme CONDITIONAL |

## 1. Gap (1): cubic local correlations and the common-support allocation

Notation. `F = Q(ω)`, `O = Z[ω]`. A good prime `p` is outside `S ⊇ {2, λ}`, with `P = q_p ≡ 1 (mod 3)`.
`χ_p(a) = (a/p)_3 ≡ a^{(P−1)/3} (mod p)`, zero-extended. This is the square of the paper's sextic
symbol [S1]. For primary `c = Π p^{v_p}`, `χ_c = Π χ_p^{v_p}`, and an exponent divisible by 3
means `1_{(a,c)=1}`.

**Fact 0 (the only order input).** For good `p`, `χ_p` has exact order 3 on `(O/p)^×`, because
`P ≡ 1 (mod 3)` and `x ↦ x^{(P−1)/3}` maps the cyclic group `(O/p)^×` onto `μ_3`. Hence `χ_p^a` is
principal on units iff `3 | a`. Also `χ_n(−1) = 1`, since `−1 = (−1)³`. [S1]

### 1.1 Cubic statements (PROPOSED; the paper's proofs with 6 → 3)

**Lemma G3 (cubic `eq:gauss-local`).** For `G(a,k) = q_a^{-1/2} Σ_{x mod a} χ_a(x) e(kx/a)` and `a ≥ 1`:

    |G(p^a,k)| = P^{(a−1)/2} 1_{v_p(k)=a−1}                  (3 ∤ a),
     G(p^a,k)  = P^{a/2} 1_{p^a | k} − P^{a/2−1} 1_{p^{a−1} | k}   (3 | a).

*Proof.* Use the paper's proof (l. 7062-7079): split `x = x_0 + p y`. The sum over `y` forces
`p^{a−1} | k`. The remaining field sum is a Gauss sum of `χ_p^a`. By Fact 0 it is nonprincipal
iff `3 ∤ a`; then it has modulus `√P` when `p ∤ k_0` and vanishes when `p | k_0`. Otherwise it is
the Ramanujan sum `P·1_{p|k_0} − 1`. ∎

At `k = 0` (the Gauss-row zero, l. 13572-13594) this gives `G(u,0) = 0` unless `u` is a cube.
[G1] checks every case exactly at split `Np = 7` (`a ≤ 4`), `Np = 13` (`a ≤ 3`) and inert `Np = 25`
(`a ≤ 2`). It includes `|g|² = P^{2a−1}`, computed as `g·ḡ` in `Z[ω][C_N]` modulo `Φ_N`. Control:
the sextic rule ("vanishes unless 6 | a") is contradicted at `a = 3`.

**Lemma FC3 (cubic `lem:full-correlation`).** Take `F(u,v;j)` as in (old-eq:2.11), `C = (u,v)`,
`u = Cn_1`, `v = Cn_2`. Then `F = 0` unless `C | j`. For `j = Ck`,

    F = χ_{n_1}(k) \bar χ_{n_2}(−k) R(n_1,n_2) Π_{p^c ∥ C} L_{p^c},   with R ≡ 1 (cubic reciprocity),
    L_{p^c} = P^{c−1} χ_p(n_1/n_2)^c · { P−1 (p | k);  −1 (p ∤ k, 3 ∤ c);  P−2 (p ∤ k, 3 | c) }   (p ∤ n_1n_2),
    L_{p^c} = P^{c−1}(P−1) 1_{3|c} 1_{p∤k}                                               (p divides one of n_1, n_2).

*Proof.* Use the paper's proof (l. 7138-7180) verbatim. The local field sum is
`Σ_{z ≠ 0,1} A(z)` with `A = χ_p^c`, which is `−1` or `P−2` according to Fact 0. The one-sided
case needs `A` principal, i.e. `3 | c`. The unit factors give
`χ_{n_2}(n_1)\bar χ_{n_1}(n_2) = 1` by cubic reciprocity for primary elements of norm prime to 3
[S2: 3298 pairs; control: the sextic `R` is nontrivial on 1060 of them]. ∎

**Corollary (single prime, all cases).** With `g = min(i, j0)`:

| case | `F(p^i, p^{j0}; j)` |
|---|---|
| `i = j0 = c` | `0` unless `p^c ∣ j`; `P^{c−1}(P−1)` if `p^{c+1} ∣ j`; else `−P^{c−1}` (`3 ∤ c`) or `P^{c−1}(P−2)` (`3 ∣ c`) |
| `i > j0` | `0` unless `3 ∣ j0` and `j = p^{j0}k`, `p ∤ k`; then `P^{j0−1}(P−1) χ_p(k)^{i−j0}` |
| `i < j0` | `0` unless `3 ∣ i` and `j = p^i k`, `p ∤ k`; then `P^{i−1}(P−1) \bar χ_p(−k)^{j0−i}` |

So the first nonvanishing unequal case is `j0 = 3`, `i ≥ 4`, with value `P²(P−1)χ_p(k)^{i−3}`. It
has no sextic counterpart below `j0 = 6`.

[F1] checks this by brute force from the definition (old-eq:2.11), over all `(x, y)` and hence all
`j mod p^{i+j0}`:

* 44 tables: `Np = 7` with `i + j0 ≤ 8`, which includes `(4,3)`, `(5,3)`, `(3,4)`, `(3,5)` and `(3,3)`;
  `Np = 13` with `i + j0 ≤ 5`; inert `Np = 25` with `i + j0 ≤ 4`.
* Exact equality holds in every table.
* Controls. The sextic rules (`6 | j0`, `6 | c`) mis-predict all 5 tables with `g = 3`. The
  conjugated child character mis-predicts all 4 unequal `j0 = 3` tables.

**Lemma CS3 (cubic `eq:correlation-child-character`).** For `u = Da`, `v = Eb` with `(a,b) = 1`
and `(ab, DE) = 1`:

    F(Da,Eb;j) = F(D,E;j) χ_a(j) \bar χ_b(−j)

The three `R` factors equal 1 for n = 3. *Proof:* as at l. 7196-7215. ∎

[C1] and [E] verify this over all `j` for six configurations each. They include:

* `D = p⁴, E = p³` (unequal, `j0 = 3`) and its mirror;
* `D = E = p³` with `a = p'`, `b = p13`;
* `D = E = p7·p13` with `a = p7'²`;
* inert `D = E = (5)`;
* one-sided common primes with `c = 1` (identically 0) and `c = 3`.

Up to 10.7·10⁶ frequencies per configuration. Control: replacing `χ_a(j)` by its conjugate is
detected in every configuration with `F ≢ 0`.

### 1.2 The cubic second-transform tables (DERIVED from the brute-force maxima)

[T1] Exact norms give the absolute table (cubic analogue of l. 13742-13751):

| common case | bound | exact value |
|---|---|---|
| equal `i`, `3 ∤ i`, unit | `P^{i−1}` | `P^{i−1}` |
| equal `i`, `3 ∤ i`, nonunit | `P^i` | `P^{i−1}(P−1)` |
| equal `i`, `3 ∣ i` | `P^i` | `P^{i−1}(P−2)` or `P^{i−1}(P−1)` |
| unequal `i > j0`, `3 ∣ j0`, `v(j) = j0` | `P^{j0}` | `P^{j0−1}(P−1)` |

[T2] reads the correlation saving `t_2` off the maxima. It is 1 exactly at equal, `3 ∤ i`, unit
primes.

[T3] With `θ = 1/3` and `F_2 = 2b_2 − (2/3)g_2 − p_2 + t_2 + V/3 + f/3`, per prime in units of
`log q_p`:

| case | `F_2` | `b_2` | `F_2 − b_2` |
|---|---|---|---|
| equal `i`, `3 ∤ i`, unit | `4i/3` | `i` | `i/3` |
| equal `i`, `3 ∤ i`, nonunit | `4i/3 − 2/3 + (1/3)1_{i=1}` | `i` | `0` at `i = 1, 2`; `(i−2)/3` otherwise |
| equal `i`, `3 ∣ i` | `4i/3 − 1` | `i` | `i/3 − 1` (`0` at `i = 3`) |
| unequal `i > j0`, `3 ∣ j0` | `i + j0/3 − 1` | `(i+j0)/2` | `(3i − j0 − 6)/6 ≥ 1/2` (`j0 = 3`: `(i−3)/2`) |

So `F_2 ≥ b_2` (`κ_2 = 1`), with zero slack exactly at nonunit `i = 1, 2` and at equal `i = 3`.
Control: without the nonunit forcing `f`, `min F_2/b_2 = 2/3 = 2θ`.

### 1.3 First-transform allocation for n = 3

* **Classification.** A common prime with multiplicities `(i, j)` is an `𝔯`-prime iff
  `3 ∤ i − j`; otherwise it is an `𝔢`-mask prime. This differs from the sextic rule. For example,
  `(4,1)`, `(5,2)` and `(7,1)` are `𝔢`-primes for n = 3 but `𝔯`-primes for n = 6. [A-B1] checks
  `χ_C\bar χ_D = ξ_𝔯 1_{(k,𝔠/𝔯)=1}` exactly, with `ξ_𝔯 = Π χ_p^{(i−j) mod 3}`.
* **Primitivity and CRT.**
  * [A-B2] checks exactly that `ξ_𝔯` is primitive mod `𝔯`, i.e. `g_ξ(h) = \bar ξ(h)τ(ξ)` for all
    `h`. Control: the sextic classification at `(4,1)` makes `ξ` principal there, and the identity
    fails.
  * [A-B3] checks exactly the CRT factorisation of the Gauss sum modulo `𝔯ab` (l. 13250-13262),
    including prime powers and an inert prime.
  * The reciprocity phase `\bar R(a,b)` of the bridge is 1.
* **Budget (old-eq:2.6), cubic allowance.** Take `B_c = ((3c − 4d − 2R)/6)_+`. *Proof of
  `B_c + B_d ≤ c + d − 2p − R`:* at most one of `B_c, B_d` is positive. Per prime with `i ≥ j`,
  six times (budget − local numerator) is `3i + 10j − 12 − 4r`. This is at least 1 if `r = 0`
  (where a positive numerator needs `3i > 4j`, so `i ≥ 2`). If `r = 1` then `i ≥ j + 1`, so it is
  at least `13j − 13 ≥ 0`, with equality only at `(2,1)`. Positive parts are subadditive. ∎
* **`κ_1 = 5/6` on `J < 0`.** `F_1 = c/3 + 2D_0/3 + q̃/3 + B_c ≥ c/3 + 2d/3 + R/3 + B_c − (2/3)δ_fr,1 ≥ 5c/6 − (2/3)δ_fr,1`.
  When `3c ≥ 4d + 2R` this is an identity. Otherwise `(2d + R)/3 > c/2`. Equality holds at
  `(2,1)` primes.
* **Uses of `B_c`.** In the paper `B_c` occurs at l. 13377, 13422, 13645, 13869 and 14445. Every
  occurrence except (2.6) has the favourable sign: target, Gauss-row allowance, diagonal,
  `Δ_child`, `F_1`. So the redesign is a parameter change constrained only by (2.6).
* [A3] checks the budget and `F_1 ≥ 5c/6` exactly over 30000 random multi-prime configurations:
  minimum slack 0, minimum `F_1/c = 5/6`, zero-slack local types `(1,1)` and `(2,1)`. Control:
  the sextic allowance gives `F_1/c = 19/24 < 5/6` at a cubic `(4,1)` prime.
* The order-free parts of the allocation (A1 bijection, A4 Möbius `s`, A5 `𝔱`-allocation, L1-L4
  label ledgers) contain no 6 and were checked by `lemma18_support_checks.py`. They were not
  re-run.

## 2. Gap (2): the cubic Kummer / fixed-numerator-ray lemma

**Lemma K3 (PROPOSED; cubic analogue of Lemma 4.1, l. 647).** Fix `0 ≠ a ∈ O`. For a prime
`𝔭 ∤ 3a` let `(a/𝔭)_3 ≡ a^{(q_𝔭−1)/3} (mod 𝔭)`. Then:

* `F(a^{1/3})/F` is abelian and unramified outside `3a`.
* `Frob_𝔭(a^{1/3})/a^{1/3} = (a/𝔭)_3`.
* `A ↦ (a/A)_3` on ideals prime to `3a` is a finite-order ray character with conductor supported
  on the primes dividing `3a`.

Fix generators `π_𝔭` for `𝔭 ∈ S`. On primary ideals outside `S`, the characters
`A ↦ χ_A(u Π π_𝔭^{v_𝔭})` form one finite family. That family is determined by `u` modulo cubes (3
classes) and by `v_𝔭 mod 3`, so it has at most `3^{|S|+1}` members.

*Proof.* `μ_3 ⊂ F`, so `F(ξ)/F` with `ξ³ = a` is Kummer, and `σ ↦ σ(ξ)/ξ` embeds its Galois
group into `μ_3`. The discriminant of `X³ − a` is `−27a²`, which is supported on `3a`. Frobenius
reduces to `x ↦ x^{q_𝔭}`, giving `a^{(q_𝔭−1)/3}`; reduction is injective on `μ_3` away from 3.
Artin reciprocity (Milne CFT VIII (5.3), (5.5), as cited by the paper) gives the ray character.
For the family, `O^× = μ_6` and `μ_6/μ_6^3 ≅ μ_3`, since `−1` is a cube. ∎

**Corollary (exceptional rows).** Let `h' = ε h_S h_good`. By (eq:row-fixed-ray-reduction) with
`R ≡ 1`,

    χ_n(h') = χ_n(ε h_S) Π_{p | h_good} χ_p(n)^{v_p(h')}.

The child character is `τ_1(n) χ_n(G_cV_id h')`. It induces a member of `Θ` (conductor on `S`)
iff, at every good prime, its total local exponent is `≡ 0 (mod 3)` (Fact 0: `χ_p^e` is ramified
at `p` iff `3 ∤ e`). Hence, for each of the finitely many `S`/unit data,
`(h') = 𝔥_0 𝔳³` with `𝔥_0` fixed and cube-free, and

    #{h' exceptional : q_{h'} ≪ Z^{m'_act}} ≪ Z^{(m'_act − f)/3 + ε},   f = v_1.

The forced residue at a second-transform prime with no older moving character is
`v_p(h') ≡ −e_p (mod 3)`. At a nonunit equal-multiplicity prime, `e_p = i + 1`, so the residue is
1 for `i = 1` (giving `f = v_1`), 0 for `i = 2`, 1 for `i = 4`, and so on.

**Where `μ_3` changes the sextic lemma.** Nothing breaks, but six details move.

| item | n = 6 (paper) | n = 3 |
|---|---|---|
| ramification of the Kummer extension | above `6a` | above `3a` (2 is not needed, though harmless in `S`) |
| units modulo n-th powers | 6 classes | 3 classes (`−1` is a cube) |
| S-numerator family | `≤ 6^{|S|+1}` | `≤ 3^{|S|+1}` (exactly 27 for `S = {2, λ}` [K2]) |
| supplementary `χ_n(−1)`, bicharacter `R` | nontrivial; `Θ` must contain them | trivial |
| exceptional rows | `𝔥_0𝔳⁶`, count `Z^{(m'−f)/6}` | `𝔥_0𝔳³`, count `Z^{(m'−f)/3}` (the source of the threshold `2M/3`) |
| nonunit `i = 1` forcing | residue 4 mod 6: `q_{𝔥_0} ≥ Z^{2f}`, so the paper keeps `f/6` spare | residue 1 mod 3: `q_{𝔥_0} ≥ Z^{v_1}`, `f = v_1`, **no spare** |

A further spare, unused by the paper and not needed here: at an equal `3 ∤ i` unit prime the
child exponent is `i ≢ 0` while `p ∤ h'`. No row of the original partition is exceptional there;
only rows admitted after positivity can be.

**Checks.**

* [K1] Each `u λ^e 2^f` numerator gives an `n ↦ χ_n(·)` that is periodic mod 18 (conductor
  divides 18). Control: not all are periodic mod 6.
* [K2] Exactly 27 distinct characters.
* [K3] 120 random `m`: `n ↦ χ_n(m)` has conductor on `S` iff `3 | v_p(m)` at every good `p`.
* [K4] All 908 good `h'` with `N h' ≤ 3000` (with an `S`-part): character-exceptional iff a cube
  times an `S`-ideal (5 cases). This uses a finite test set of 451 `n`, so it is a consistency
  check, not a proof.
* [K5] Forced residues `{1:1, 2:0, 3:2, 4:1, 5:0, 6:2}`.

## 3. Gap (3): the cubic centred stage, exponents recomputed

### 3.1 Every order-dependent spot in Sec. 18 (z = 0)

The grep of l. 12477-14973 for the order finds the following. All are now covered:

| lines | content | n = 3 replacement | where checked |
|---|---|---|---|
| 12500-12609, 13081 | zero extension mod six | mod 3 | definitions |
| 12686-12697 | conductor bound via fixed-numerator ray | Lemma K3 | [K1-K2] |
| 13180-13186 | zero frequency: exponents `≡ 0 mod 6`, so the product is powerful | `≡ 0 mod 3` still forces powerful; same `X^{1+ε}` count | transfer note |
| 13209-13224, 13379-13408 | `𝔯 = {6 ∤ i−j}`, `B_c`, (2.6) | `𝔯 = {3 ∤ i−j}`, cubic `B_c` | [A-B1..B3], [A3] |
| 13572-13590 | Gauss-row zero: sixth powers | cubes: `2a_0/3 − 2s_0 ≤ a_0 − s_0` | [G1] (`k = 0`), transfer note [E1] |
| 13699-13786 | second-transform local rules and tables | Sec. 1.1-1.2 | [F1], [T1-T3], [C1], [E] |
| 14329-14379 | Θ rows: Kummer, forced residue, count | Lemma K3 and its corollary | [K3-K5] |
| 14440-14452 | `(2.15)-(2.16)` with `θ = 1/6` | `θ = 1/3` | [L1] (sympy) |
| 14760-14770 | `(2.19)` with `5M/6`, `L = M/4` | `2M/3`, nested A-dependent `L` | [L4], [L5] |
| 13457-13552, 14204 | the `p⁶` amplifier, `ℓ_p ≥ σ/6` | case 2 only | not used |

### 3.2 The centred exceptional deficit at n = 3

Fix a centred input in the padded core (`n_i ≤ M/2 + ξ`, `2M/3 < A ≤ M + δ`) and a comparison
length `L` with

    L ≤ A/2,   L ≤ A − M/2   (caps).                                                   (3.1)

1. **All four plain lengths are at least `L`.** In the padded core, `n_i ≥ A − M/2 − ξ ≥ L − ξ`.
   The comparison rectangle `(L, A − L)` has `A − L ≥ L`. So the short-plain branch is empty up
   to `ξ`. If it occurs, it gives a reflected total `≤ M − A + 2L + O(ξ)`, the same as the
   comparison. The reflected comparison `(L, M − A + L)` stays in the core by (3.1).
2. **Lattice cancellation (Lemma centered-lattice-cancellation, l. 14545-14660) is order-free.**
   It needs only:
   * a fixed finite set of ray characters `ϑ` with conductors in `S` (Lemma K3);
   * a squarefree mask with `2^{ω} ≪ Z^ε`;
   * smooth annular profiles.

   It gives relative saving `Z^{−r}` with `Z^r = min(U_i, V_i)`. After extraction, with
   `v = c + w + min(c_2, d_2)`, the paper's argument (l. 14684-14740, (2.18h)) gives
   `r = (L − v)_+`, with no allocation loss (`t_- − r̃_1 − r̃_2 − (r − r̃_1)_+ ≤ ω_2 − r`). Nothing
   here depends on `L ≤ M/4`.
3. **Count × volume / allowance** [L1, sympy identity]:

       (m' − f)/3 + a_0 − b_2 − (M' + Δ_child) = A − 2M/3 − F_1 − F_2,
       F_1 = c/3 + 2(d + K_0 − K)/3 + 2w/3 + q̃/3 + w_o + B_c − 2g/3 + ℓ,
       F_2 = 2b_2 − (2/3)g_2 − p_2 + t_2 + V/3 + f/3.

   With `θ = 1/6` the same identity reproduces the paper's (2.16). Control: the sextic `F_1`
   differs.
4. **Lower bounds.**
   * `J ≥ 0`: `F_1 = c + 2w + q̃/3 + w_o/3 + B_c + ℓ ≥ c` [L2].
   * `J < 0`: `F_1 ≥ (5/6)c − (4/3)σ − (2/3)δ_fr,1` (Sec. 1.3; the σ-term is `(1−θ)·2σ` from
     `g ≤ J_+ + 2σ` [L3]).
   * `F_2 ≥ b_2 ≥ min(c_2, d_2)` [T3].

   Hence `F_1 + F_2 ≥ (5/6)v − (4/3)σ − (2/3)δ_fr,1`, uniformly over every common-support and
   `𝔱`-allocation. Every term is a sum of the per-prime contributions verified above (`F_2` is
   additive over second-transform primes; `F_1` uses only the global `B_c`).
5. **Deficit** [L4, exact grid]:

       A − 2M/3 − F_1 − F_2 − (L − v)_+ ≤ max_v [A − 2M/3 − (5/6)v − (L − v)_+] + T
                                          = A − 2M/3 − (5/6)L + T,

   The maximum is attained at `v = L`. The terminal term is
   `T = 4σ/3 + (2/3)δ_fr,1 + δ_fr,2/3 + 2θ_N + ε_1` (`+ δ` in the padded core).
6. **Closing.** Closure needs `(5/6)L ≥ A − 2M/3`, with (3.1) and the comparison landing in a
   proved range.
   * At `A = M` this means `L ≥ 2M/5`. The single window (`A_comp ≤ 2M/3`, so `L ≤ M/3`) fails, as
     already known.
   * The nested ordering with two centred stages has uniform margin `0.0179M` (split `0.861M`,
     `A ≤ M`) and `0.0155M` (split `0.867M`, `A ≤ 1.01M`) [L5]. This independently reproduces the
     red team's `0.01794` / `0.01555`. The largest `L` used is about `0.42M`, inside (3.1).

**Answer to gap (3).** The cubic centred stage delivers the saving `(L − v)_+` for every `L`
allowed by (3.1), and `F_1 + F_2 ≥ (5/6)v` holds uniformly. The only losses in the displayed
steps are the terminal `T` and the `C_*ξ` edge costs. These are absolute constants absorbed into
`ε`, not multiples of `M`. **No loss `cM` with `c > 0` was found, so in particular none with
`c ≥ 1/12`.** The route's tolerance for a hidden uniform loss is `< 0.0155M` with two stages,
rising toward `M/12` with more stages (red team [T3]).

What this does not show: that the inherited sextic analysis behind items 2-3 is correct. The
cubic route asks the same machinery for twice the relative cancellation of the sextic proof
(`Z^{−M/3}` against `Z^{−M/6}` at `A = M`; Patterson polar term, red team Sec. 4.2).

## 4. Current status

> **CONDITIONAL statement.** Assume:
>
> * **(A) Inherited core.** The proof of Lemma 18.1, case 1 (z = 0), of the OpenAI manuscript is
>   correct in its order-independent steps. Concretely:
>   * Lemma 4.5 `smooth-calculus` and Lemma 4.7 `kernel-seminorms` hold as stated;
>   * the displayed ledgers of l. 12602-14984 describe the analysis. All lines were read by the
>     bounded reviews LEMMA18_1_REVIEW, LEMMA18_1_COMMON_SUPPORT and LEMMA18_1_CASE2_SEC188,
>     which found no wrong step; this includes the centred-coefficient invariance and lattice
>     cancellation.
>   * (Lemma 4.9 `logarithmic-control` enters only through the slot bound (old-eq:3.5), i.e.
>     case 2, per LEMMA18_1_CASE2_SEC188.)
> * **(B) Nested ordering.** The PROPOSED nested comparison ordering of
>   CUBIC_RELAXED_INDUCTION.md Sec. 4 is admissible. A centred stage may call the earlier centred
>   stage at the same width, with an A-dependent `L` satisfying (3.1), two stages, and the
>   bookkeeping of the red team, Sec. 5 items 3-4.
>
> Then, for every `ε > 0`,
>
>     Σ_{c ∈ O squarefree, c ≡ 1 (mod 9), N c ≤ X} |L(1/2, χ_c)|⁴ ≪_ε X^{1+ε},   χ_c = (·/c)_3.

Every order-dependent ingredient is supplied here (Secs. 1-3) by a written proof plus exact
finite checks. These are the cubic finite Fourier lemmas, Lemma K3, the `F_2` table, the cubic
`B_c`, the nonunit forcing and the centred exponents. They are therefore not on the list. The
(2,1)-forcing of CUBIC_RELAXED_INDUCTION.md Sec. 5 is not needed.

Variants:

* **(A) + (2,1)-forcing in place of (B):** `X^{1+ε}` in the paper's own order, with zero slack.
* **(A) + relaxed bookkeeping, no (B):** `X^{53/51+ε}` (CUBIC_RELAXED_INDUCTION.md Sec. 3).
* **Unconditionally:** still `X^{4/3+ε}` (cubic large sieve). `X^{1+ε}` would be new.

**Steps that still need a human-level proof or referee check** (most load-bearing first):

1. **(A) itself.** Lemmas 4.5 and 4.7 (not reviewed by us). An expert confirmation that the
   case-1 ledgers describe the analysis, in particular:
   * Lemma centered-coefficient-invariant (l. 13954) and the coefficient lemma (l. 13934-14310);
   * the Fourier separation before Cauchy-Schwarz.

   The cubic route uses these at twice the sextic relative precision.
2. **(B).** A written restatement of the induction order (l. 12903-12938, 14779-14810) with two
   centred stages:
   * `ξ < ε/(16(k+1)C_*D)`;
   * profile types closed under `k` nested reflections before `C_ref`;
   * `L(A, j)` fixed with `ρ, σ, δ`.
3. **The cubic functional equation and conductor bound for reflection** (Lemma 4.8 analogue).
   This needs:
   * primitive Hecke characters of order 3 over `Q(ω)` with `Γ(s)/Γ(1−s)` and `|ε| = 1`;
   * tameness at good primes;
   * the `S`-part from Lemma K3.

   Standard, but not written out.
4. **Referee check of the PROPOSED proofs here.** Lemmas G3, FC3, CS3, K3 and the corollaries,
   the cubic (2.6) proof, and the substitution of the new `B_c` at its five occurrences. All are
   short and routine; the exact checks cover small moduli only.
5. **The application.** Positivity `R_sf ⊂ R_0`, cubic reciprocity `(k/n)_3 = (n/k)_3` for
   primary elements, the approximate functional equation and dyadic Mellin inversion from
   `|S(m/2)²|²` to `|L(1/2, χ_c)|⁴`. Routine (review Sec. 0).

**Smallest statement whose failure breaks the X^{1+ε} route.** For n = 3, every centred
Theta-row child must keep its common character, mask and norm power across both rectangles
(centred-coefficient invariance). Lattice cancellation then removes its main term to relative
precision `Z^{−(L−v)_+}` with `L ≥ (6/5)(A − 2M/3)`. A uniform loss of `0.0155M` or more inside
that step breaks the two-stage version, and `M/12` or more breaks every version.

## 5. Files

* `scripts/cubic_local_checks.py` (NEW). Sections [S], [G], [F], [T], [C], [E], [A], [K], [L];
  38 checks; 10 dedicated failing controls plus 4 embedded in [E] (a fifth [E] control is vacuous because
  `F ≡ 0` there). EXACT arithmetic. Run:
  `nice -n 10 python3 -I scripts/cubic_local_checks.py` (about 3.5 minutes).
* The output log is kept in the session scratchpad (`cubic_n3/run2.log`), per the run rules. The
  script is the reproducible artifact.
