# Red-team review of the offense wave (O1-O7 and the coordinator index)

```text
Status: EXPLORATORY review (adversarial). Not an integration review. Nothing here proves RH or any
  zero-free region. The Sep 30 ("7/8") and Oct 5 ("11/12") OpenAI manuscripts are external,
  unreviewed imports; every statement resting on them is CONDITIONAL/IMPORTED.
Scope: the PROVED-HERE and exact-ledger claims of offense/README.md (state at 00:36 UTC),
  O1 README (00:28), O2 README (00:35), O3 README (00:06), O4 README (00:22), O5 README +
  KUMMER_FIELD_COROLLARIES.md + ROW_REWEIGHTING_CLOSURE.md section 3 (00:14), O7 README +
  closed_forms.out (00:19). O3b was read only for the item that the coordinator delegated to it.
  O6 was not reviewed.
Exact sources or dependencies: Sep 30 scratchpad/paper_sep30.tex (l. 106 thm:main, 642 gamma_j,
  960-968 eq:signal, 3336-3395 S, xi, Xi, T_{m,s,eta}, 3397-3475 eq:general-probe,
  A_{m,sigma,v}, B_{m,sigma}, eq:low-separated, 8073-8107 T_D, B^J); ../SEXTIC_THETA_S6.md
  l. 86 and 207 (Kubota pole conventions); O2/o2_ledger.py; O1/ledger.py.
What was actually run: python3 -I scratchpad/rt/check.py (sympy, exact rationals, < 5 s): all
  closed forms listed below; 45 checks, all pass. The script lives in the session scratchpad,
  not in the repository. No floating-point runs of the families.
Smallest remaining gap: none for this review; each finding names its own correction.
```

RH remains unproved. Verdicts: OK / MINOR ISSUE / ERROR / OVERCLAIM. Most serious first.

## A. Serious findings

**A1. Coordinator README, "Sep 30 side": "on the m-diagonal of the low pairing the coefficient
product is `γ₁γ₂ᾱη = μGη`, i.e. the probe's own Möbius signal". Verdict: ERROR in the mechanism
(the coefficient identity itself is OK).**
* Coefficient algebra: correct. On `a = cn³` with `c = s`, `A_{m,σ,v}` contributes
  `conj χ_s(−m)γ₁(s)` (O3.1), and `B_{m,σ}` (through `T(t+1/2, ν_σθχ_•(m))`,
  `ν_σ = ηΞ⁻¹R(·,s_σ)`, l. 3426) contributes `γ₂(s)ᾱ(s)η(s)`. By eq:signal, `γ₁γ₂ = μαG`.
  Precisely, the Fourier sum `Σ_θ a_θ θ(A) = conj G(A)` inside `B` then cancels `G(s)`. So the
  coefficient is `μ(s)η(s)` times fixed finite-order factors (`ξ̄(s)²`, `R(s,s_σ)`, `χ_s(−1)`,
  `τ⁻¹`), not `μGη`.
* But that "diagonal" carries no main term in [S30]'s pairing. Its `m`-character is
  `ξ(m)·χ_s(−1)·1_{(m,s)=1}`. Here `ξ` is primitive and nonprincipal modulo `b_*` (l. 3350-3355).
  The paper introduces it precisely to "force the Poisson frequency to be prime to S", including
  zero (l. 3345-3346, 3373-3374).
  * The smooth `m`-sum over the ball `q_m ≍ Q ≫ q_s` is therefore negligible.
  * O3b Prop. O3b.1 (README written 00:39, after the coordinator text) finds the diagonal
    *identically* zero via `ξ(−1) = −1`. That argument assumes `S = {2, λ}`. In [S30], `S` also
    contains every prime of norm `≤ P₀` (l. 3337-3340), so `ξ(−1) = Π_p ξ_p(−1)` is not forced.
    The robust statement is "negligible by primitivity of ξ", not "identically zero".
* Consequence: the coordinator's reason for "(NA) is likely circular" is wrong as stated. O3b now
  argues circularity through a *different* route (B's principal row and the exceptional dual
  frequencies). That conclusion may stand, but the synthesis text, the ranked table and the O3 row
  ("pending O3b"; "its diagonal may be the probe's own Moebius signal") are stale and should be
  replaced.

**A2. Coordinator ranked table, row "(NA) + FB#(1/3, 1) → 926/1077, then 28/33". Verdict:
OVERCLAIM (a hypothesis was silently dropped).**
* 28/33 also needs DH-strength row counts above the raised floor,
  `R(δ) ≤ 19/20 − 17δ/20` on `(1/3, 23/33]` (O7 README; FLOOR_ROWS.md l. 395-396). FLOOR_ROWS.md
  l. 241 calls DH-rows "beyond current technology for this family".
* With the manuscript's own counts, raised floors do not close, and the best is about 0.8582
  (O7 README, float full model).
* The O7 row of the results table does state "DH-strength row counts". The ranked table does not.

**A3. Coordinator: "Numerically, every needed statement holds with a large margin … What is missing
is a mechanism, not truth." Verdict: OVERCLAIM. It breaks AGENTS.md: "never turn a finite positive
result into global evidence".**
* The needed statements are asymptotic power savings. The data stop at `D ≤ 45000` (O2), `X ≤ 10⁵`
  (O1) and `D ≤ 32000` (O4).
* The quoted "cancellation exponent 0.71-1.59" is `log(P/|S|)/log D` at finite `D`, and `S`
  changes sign. For example `S = 0.0049` at `D = 2000, ρ = 0.6` produces the 1.59.
* O2 itself says that no growth exponent of `|S|` is resolvable and that `e` is inflated by the
  logarithms in `P`. O1 says its trend is "not evidence of an asymptotic". O5 says finite data
  "are not evidence of provability".
* "Not truth" asserts the truth of open statements. Replace the sentence with "consistent with, in
  the tested finite range".

**A4. Coordinator ranked table, (LS*_κ): "the only known obstruction … is provably harmless for
this sequence (O1 Prop 5)". Verdict: OVERCLAIM.**
* Prop. 5 is labelled PROPOSED. It bounds only the main term of a *hypothetical* Kubota pole, and
  it imports the KP Hecke relation.
* "Only known obstruction" rests on the dFDH *abstract*; O1 §9 says the paper body was not read.
* Its exponent is also wrong (A5). "Provably" must go.

**A5. O1 Prop. 5 (Gauss-sum-bias obstruction harmless). Verdict: ERROR (not load-bearing).**
* The proof places the 6-fold pole at `s = 7/12` and takes the main term of `B_h` to be
  `X^{7/12}N(h)^{−1/3}`. But `7/12 = 1/2 + 1/(2n)` is the Eisenstein-series variable.
* The Dirichlet series `Σ_c G_6(m,c)N(c)^{−s}`, which governs the partial sums, has its pole at
  `1/2 + 1/n = 2/3`. Sources: SEXTIC_THETA_S6.md l. 86 vs l. 207; O3 README §2.3 and §5 ("Kubota
  residue at 2/3").
* The cubic control in the same proof silently uses the Dirichlet-series pole `5/6 = 1/2 + 1/3`.
  That is what gives the correct `X^{2/3}𝓗^{2/3}` and matches the `γ₂` numerics. The 7/12
  convention would give `X^{1/3}𝓗^{2/3}`.
* Corrected sextic contribution: main term `X^{2/3}N(h)^{−1/3}`, so `E ≪ X^{1/3}𝓗^{1/3}` (stated:
  `X^{1/6}𝓗^{1/3}`). This is still `≤ X` for `𝓗 ≤ X`, so the qualitative conclusion survives.

## B. Item-by-item verdicts

### Coordinator README (cells checked against the folders)

| cell | verdict | justification |
|---|---|---|
| lever table (ρ < 9/10, c < 3/4, 17/24, 5/6, κ < 1/6) | OK | `1/2 + 5ρ/12 < 7/8 ⟺ ρ < 9/10`; `1/2 + c/2 < 7/8 ⟺ c < 3/4`; the rest is checked in sympy |
| "δ > (1−ρ)/6 is the same as κ < 5/6" | OK | `δ = (1−κ)η` with `η = 1−ρ`, so `δ − η/6 = η(5/6 − κ)` |
| "principal rows force the identical inequality on A₁, no slack to borrow" | MINOR ISSUE | O2 Prop L item 2 is item 1 read backwards: the bound `Σ ≥ H^{1/6}\|A₁\|²` is used both ways. A bound implying its own corollary is not circularity, so "presupposes" is misleading |
| "Amplifiers cost κ = 1 (O4, both rounds)" | OVERCLAIM | O4 shows κ = 1 only for design (a), CONDITIONAL on Oct 5. Designs (b)-(e) are "exponent-level analyses, not proofs of impossibility" (O4 §6). Round 2's j = 4 design is worse (`κ + 5δ/6 ≥ 5/4`). Add "for the designs examined, on the Oct 5 tools" |
| (AMP_t) "neither the row-blind nor the orbit barrier applies" | MINOR ISSUE | True of the pre-reflection statement. But O4 §7.2 shows the same prime amplifier, after reflection, needs a bound `L^{17/6}` below the reflected column count, equivalent to TM(5/12, 1). The synthesis lists both without reconciling them |
| "kappa-law / Prop L", sources "O2, O5" | MINOR ISSUE | Claim-ID collision: O2 Prop L is the leverage law, O5 Prop L is the `p⁶` lifting. Rename one (AGENTS: do not recycle IDs) |
| O1 row "WMDS and Rankin-Selberg routes give 1 and 13/12" | MINOR ISSUE | O1 §3 gives WMDS no exponent (no finite Weyl group; route closed). The σ = 1 belongs to the Kubota-FE routes |
| O1 row "mu*gamma_2*xi shows no BGL excess" | MINOR ISSUE | The numerics use `μγ₂` without `ξ`, split primes only, primary rows only (O1 §6) |
| O1/Statement B "(S6) locally consistent …; both known cases n = 3, 4 are reproduced" | OVERCLAIM (mild) | n = 4 is reproduced at literature level only ("no Z[i] numerics", O1 §8A table). See also B-O1 below |
| O2 row "exact check on 400 cases" | MINOR ISSUE | `o2_ledger.py` C1 is complex floating point (`np.exp(2πi e/6)`, tol 1e-9, error 1.5e-15), yet it is labelled [EXACT] in O2 §0/§1.2. Round 2 labels its analogues [FLOAT] correctly |
| O2 row (Prop G, Prop L, `\|S\|/H ≤ 0.71 %`) | OK | max `\|S\|/H` = 0.4461/63 = 0.708 % (D = 1000, ρ = 0.6) |
| O3 row "squared cubic Gauss sum family, not Moebius" | MINOR ISSUE | `γ₁ = Gγ₂² = μαG·conj γ₂`, so it is Möbius-weighted. The accurate statement is "class θ², not the Oct 5 class θ³ (μ × finite order)" (O3 itself says this) |
| O3 row "pending O3b" | MINOR ISSUE (stale) | O3b has reported. See A1 |
| O4 row break-even law "PROVED-HERE: \|A₁\| ≪ D^{…}" | MINOR ISSUE | The law is correct (re-derived), but the cell drops its hypothesis (`M_amp ≪ D^ε HDL^{1+κ}` at `H = DL^{1+δ}`), the `ε` and the extraction floor `D^{1−h/6}`. As printed it reads like an unconditional bound |
| O4 row "column count L^2 H^2/D" | MINOR ISSUE | O4 has `L²𝓗²/D` with `𝓗 = DL^{1−δ}` the dual row count, not the primal `H` |
| O4 row "\|kappa_emp\| <= 0.004" | MINOR ISSUE | This is §5.1 only. §5.2 has κ_emp up to +0.0145, and O4 §0 says "≤ 0.01" |
| O7 row closed form, "iff κ > 5/6", 28/33, 38/45 | OK | see B-O7 |
| O7 row "with Gram loss b/12, nothing beats 13/15" | MINOR ISSUE | O7 says this holds "with the manuscript's energy lemma". With the hypothetical E\*, 106/123 ≈ 0.8618 < 13/15 |
| O5 row (14/3/1 triage, κ-law, lifting, Kummer) | OK | The counts match the triage table, and the labels are CONDITIONAL. Caveats are in B-O5 |
| results table | MINOR ISSUE | It has no rows for O6 or O3b, although both folders have reported |

### O2_SIGNED_DUAL

* **Prop G (gcd collapse): OK** (re-derived).
  * `χ_{(g/f)z_j}(k)` factors.
  * The `j = 1, 2` product gives `|χ_{g/f}(k)|² = 1_{(g/f,k)=1}`.
  * `Σ_{f|g} μ(f)1_{g₁|f} = μ(g)1_{g|k}`.
  * The `a`, norm and `W₀` bookkeeping is consistent.
  * Cor. N's `χ_z(gk')χ_z(g)⁴ = χ_z(k')conj χ_z(g)` holds.
  * Only the check label is wrong (see the table).
* **Prop L: OK** (sympy).
  * `σ = (m − ρ/6)/2` with `m = 2 − δ` gives `1 − δ/2 − ρ/12`.
  * It is `< 11/12 ⟺ δ > (1−ρ)/6`, and `< 7/8 ⟺ δ > 1/4 − ρ/6`.
  * Full δ gives `1/2 + 5ρ/12`.
  * All five table rows are correct.
  * MINOR: "only possible for ρ ≤ 9/10" should read `ρ < 9/10`. At ρ = 9/10 the full saving gives
    exactly 7/8, as the table row itself shows.
* **(AMP_t) `σ = 11/12 + λ(5t − 6)/12`: OK.**
  * From `2σ = 5h/6 + 1 − λ` at `h = 1 + tλ`: t = 1, λ = 1/2 gives 7/8.
  * `t = (3+s)/2 < 6/5 ⟺ s < −3/5`.
  * Variants (a) `13λ/24` and (b) `λ/3` are correct.
  * At t = 1 the statement fails for λ > 5 (σ < 1/2), as stated.

### O4_AMPLIFIER

* **Lemma A1 / break-even law: OK.**
  * `σ = (e − h/6 − 2λ)/2` with `e = h + 1 + λ(1+κ)` and `h = 1 + (1+δ)λ` gives
    `11/12 + λ(κ + 5δ/6 − 1/6)/2`.
  * `κ* = 1/6`, `δ* = 1/5`.
  * TM route: `σ = 11/12 + λ(5s/6 − 2η)/2`. The GRH-random threshold is `λ < 3/2`.
  * Design (a1): `11/12 + 5λ/12`.
  * 233/240 at `(h, λ) = (5/4, 1/10)` is correct.
* **§7: OK.**
  * Route (i): `min max(0, 1−δ, 3−2δ) + 5δ/6 = 5/4` at δ = 3/2, which gives `11/12 + 13λ/24`.
  * Route (ii′): 5/6 at δ = 1, which gives `11/12 + λ/3`.
  * The no-solution argument (`δ > 17/7` vs `δ < 3/2`) holds.
  * `L^{4 − 7/6} = L^{17/6}` holds.
  * The operator-norm lower bound `≥ max(rows, columns)` holds only up to the vanishing entries of
    `χ_ℓ(k)⁴(k/n′)₂`. Harmless.

### O5_WILD_IDEAS

* **Prop K1: OK.** `M̃ = M·σ(M)` is normal over Q:
  * an embedding fixing K preserves `M̃`, because `M̃/K` is normal;
  * an embedding acting as conjugation on K sends `M̃` to `σ(M̃) = M̃`.

  So `M̃/F` is Galois, and Aramata–Brauer gives `ζ_F | ζ_{M̃}`. HECKE-7/8 matches [S30]
  thm:main (l. 106: every finite-order Hecke L-function over Q(√−3)), so the CONDITIONAL label is
  right. MINOR: "dihedral extension of Q whose quadratic subfield is Q(√−3)" is ambiguous for `D_n`
  with n even, which has three quadratic subfields. It should say that `L/K` is cyclic.
* **Prop K2: OK.**
  * Inert `q`: `m^{(q²−1)/3} = (m^{q−1})^{(q+1)/3} = 1`; in the sextic case `q ≡ 5 (6)`, so
    `6 | q + 1`.
  * Non-cubes in Z stay non-cubes in K.
  * `y ≪ y^{7/8}(log m)^{1+ε}` gives `(log m)^{8+ε}`.
  * MINOR: for the sextic version with `m < 0`, "non-sixth-power" must be read in K, since
    `−27 = (√−3)⁶`.
  * MINOR: the effective Chebotarev error `O(x^{7/8} log(xm))` probably needs `log²(xm)`, as the
    standard truncated explicit formula gives. The claim is labelled PROPOSED.
* **κ-law `σ = 11/12 − η(5/6 − κ)/2`: OK.**
  * Extraction with `m = 2 − (1−κ)η` and `ρ = 1−η` gives it.
  * Pointwise 7/8 gives `κ = 3/(4η)` and `31/24 − 5η/12`.
  * Detector: `f = 1/6 ⟺ σ = 11/12`, `f(7/8) = 2/7`, `f(13/15) = 49/159`.
* **"Prop L (lifting gives κ = 5/6 for η < 6/11)": OK, with a MINOR proof slip.**
  * The separation identity is right, including the sign (`μ(pm) = −μ(m)`, `χ_m(up⁶) = χ_m(u)1_{p∤m}`).
  * The threshold is right: `θ′ = η/(6−η) ≤ 1/10 ⟺ η ≤ 6/11`.
  * The slip is in the second term. The scales `x/Np` differ with `p`, so rows cannot be pooled
    across `p`. The bound is `x′^{2+θ′} = x^{2+θ−(η+θ)/6}` per prime, hence on average, with no
    `J⁻¹` factor. It is of the same order as the first term, not "smaller". The final
    `x^{2−η/6+ε}` is unaffected.
  * README wording "already *proves*" is acceptable only with its attached "conditional on Oct 5".

### O7_FLOOR_ROWS

* **Closed form `σ0 = 2(9 + 13δ0 − 12κδ0)/(3(7 + 9δ0 − 8κδ0))`: OK.**
  * It gives 6/7 at δ0 = 0, and **identically 6/7 at κ = 5/6** (all δ0).
  * `6/7 − σ0 = 4δ0(6κ − 5)/(21(7 + 9δ0 − 8κδ0))`, with positive denominator for κ ≤ 1. So
    "improves on 6/7 iff κ > 5/6" is right.
  * `dσ0/dδ0|₀ = (20 − 24κ)/147`.
  * At (1/3, 1): `2(28/3)/(3·22/3) = 28/33 = 0.848485`. At (1/2, 1): 38/45. 902/1053 at θ = 1/50 is
    right.
  * MINOR: the README states the formula without its domain. It is valid only while the L2 slack is
    ≥ 0 (at κ = 1, δ0 ≤ 1/2; `closed_forms.out`). At δ0 = 1 it would print 5/6, below the 38/45
    wall.

### O1_CUBIC_FAMILY_REFLECTION

* **Ledger `σ(κ) = (9κ − 2)/(6κ)`: OK** for 5/6 (1/2), 7/8 (8/15), 11/12 (4/7) and 1 (2/3), and the
  function is increasing.
  * MINOR: it is valid only for κ ≥ 1/2. Below that, ρ = 1 binds and σ = 5/6; the formula would
    give 1/2 at κ = 1/3. `ledger.py` notes this, but README and coordinator do not.
  * The 8/9 benchmark is right: `𝓗 ≤ X^{5/6}`, ρ = 7/6.
* **Lemma 1 (numerator `−h⁴`): OK** (re-derived). It uses `γ₋₁(y,n) = χ_n(y)γ₋₁(n)` and
  `χ_n(h)⁴ = conj χ_n(h)²` on top of the imported S6 `μγ₂ = χ(−1)αGγ₋₁`. PROPOSED is appropriate.
* **Prop 5: ERROR** in the exponent; the conclusion survives (A5).
* **§8A (local consistency of (S6)): MINOR ISSUE, labels mostly honest.**
  * PROPOSED, with KP84/Hoffstein imported and not re-read, as stated.
  * But "locally consistent at every unramified prime" was tested only against the `j`-orbit
    relations (P), (H) at fixed `m`. It does not analyse how a local Whittaker functional lets
    `τ(mp)/τ(m)` depend on the class of `m` at `p` (torus/unit equivariance). (S6) prescribes that
    dependence (`ε(m,p)`, `χ_p(16)`, `(η/α)(p)`). The supported claim is "not contradicted by (H)".
  * H6 (108 cases, 3.4e-15) is a floating-point check of the algebraic equivalence, not of
    consistency.
  * "Contradicted by [BH]" rests on [BH] Conj. 5.7, a numerically supported conjecture. The
    infinity-type argument carries the [INF] caveat. The text says both, but the coordinator
    compresses them away.

### O3_SEP30_X_OCT5

* **Prop O3.1 (`γ₁ = Gγ₂²` on squarefree s): OK.**
  * eq:signal (l. 966-967) gives `γ₂³ = μα` and `γ₁γ₂ = μαG`. With `|γ₂| = 1`, `γ₁ = γ₂³G/γ₂`.
  * The first factor follows from `d ↦ −m⁻¹d` with `g_ψ(c,k) = Σ ψ(d)e(kd/c)` (l. 3358) and
    `γ_j` as at l. 642.
  * PROVED-HERE given the imports is fair.
* **Coordinator's m-diagonal circularity claim: ERROR in mechanism** (A1). It was checked against
  `A_{m,σ,v}` (l. 3460-3465), `B_{m,σ}` (l. 3424-3431), `T` (l. 3381-3386) and `T_D`/`B^J`
  (l. 8080-8104).

## C. What is solid

These re-derive exactly:
* O2 Prop G and Prop L;
* AMP_t;
* O4 Lemma A1 and §7;
* the κ-law, its equivalence with O2 Prop L, and the lifting threshold 6/11;
* O7's closed form and its 5/6 threshold;
* O1's ledger and Lemma 1;
* O3.1;
* K1 and K2 (as conditional, proposed arguments).

The defects are in the coordinator's synthesis (A1-A4), one wrong pole convention (A5), and labels.

**Smallest statement whose failure would invalidate the wave's headline reading.** The Sep 30 side
of the synthesis needs: "the probe's signal lies inside the pairing `⟨A^exc, B⟩` that (NA) bounds".
The coordinator's version of that statement (the m-diagonal) fails. O3b's replacement (the
principal row of B) is PROPOSED and has not yet been checked by anyone else.
