# Red-team review of this wave's own claims (qrh-2026-10)

```text
Status: REVIEW (adversarial, bounded, single agent). Exploration level; not an integration verdict.
  No RH claim. Nothing here proves or refutes any zero-free region.
Scope: the PROPOSED / HEURISTIC notes of research/exploratory/qrh-2026-10/ named below, at
  HEAD d47a04076f34152bd9d0276a9eaa3f43804120f9 (branch claude/peaceful-faraday-ki4ewu).
  Reviewed in full: RUNG_STRENGTH.md, HEIGHT_LEVELS.md (+ a2/check_triple.py), LEVERAGE_FAMILIES.md,
  Q_RHO_ANALYSIS.md, DISPERSION_GRH_STEP.md, SHORT_PROOF_FRONTIER.md (against THRESHOLD_CALCULUS.md),
  ROBIN_GRADED.md, SIEGEL_DETERMINANT.md, CONDITIONAL_CONSEQUENCES.md, SYNTHESIS.md, README.md.
  Spot-read only: FOURTH_MOMENT_A2.md, A2_LITERATURE.md §5, moments/README.md, INTAKE.md (definition
  of QRH-IMPORT), reviews/PR910_REPLAY.md (scope line).
  sha256 prefixes of the reviewed notes: RUNG 1cd6034a, HEIGHT 9a36f178, LEVERAGE fb4903fd,
  Q_RHO b755e89d, DISPERSION eeab8786, SPF 0a514f48, THRESHOLD 839484d1, ROBIN 30723e76,
  SIEGEL 4839dc39, CONDITIONAL aae10fee, SYNTHESIS bc62a84c, README f7a41c38.
Exact sources or dependencies:
  PR 910 at local ref pr910 = 670a76c1a3a8f325c43c1755b1cfc24d313a3e3c:
    standalone/2026-10-10-quasi-riemann-height-descent/UPSTREAM_HEIGHT_AND_MOMENTS.md §7 (Prop. 7.2),
    .../REVIEW.md (scope paragraph, line 5), .../FOURTH_MOMENT_REDUCTION.md (eq. 3.5).
  Sep 30 manuscript paper.tex and Oct 5 manuscript paper2.tex at pr908 (Prop. 6.3 statement,
    Lemma 5.8 statement, Lemma 6.2 additive norm; Oct 5 abstract and thm:main).
  Standard facts used in the derivations: Mellin inversion, Hölder, Perron, the GRH bound for 1/L,
    Kummer theory for (u/n)_6, the spectrum of J.
What was actually run:
  * python3 a2/check_triple.py 60 20000: 209 triples, max deviation 3.54e-14, control 1.732
    (reproduces HEIGHT_LEVELS). Floating point, not certified.
  * a scratch script (scratchpad, not committed), sympy + Fractions: 37/37 exact checks of
    sigma(k,h) = 1/2 + 5rho/12, the R' exponent, the 11/12 bootstrap fixed point, det(3I - J) for
    k <= 7 and the k = 4 spectrum, the DISPERSION map sigma_new and fixed point 1 - 1/(6A) (with
    A = 2, 12/5, 3, 4/3), the Q_rho orbit table and invariant at rho = 9/10, the effective degree
    48/11, the Li-inflation law (grid over w), the SPF closed forms (7A-3)/(7A-2), its geometry,
    (31A-18)/(33A-18), and the Robin constants (0.04643, 17A, 1.406, the log log n ~ 35 crossover,
    eps(T), 7e22, 3e30).
  * eis.py symbol check: (u/pi)_6 for the six units and for +-27 at the 44 primary primes of norm
    <= 200. Units other than 1 give a nonprincipal symbol (for example -1 is nontrivial at 24/44);
    -27 is principal; +27 is not.
  Not done: no manuscript lemma was re-proved; Robin 1984, Nicolas 1983, Lagarias and the
  function-field literature were not opened; no new numerics beyond the above.
Smallest remaining gap: the ROBIN/CONDITIONAL "QRH <=> Robin-type inequality" equivalence uses the
  wrong premise (zeta only, not QRH-IMPORT as INTAKE defines it), and RUNG_STRENGTH's Prop. R'
  rests on PR 910 Prop. 7.2, which no review has covered. Both are labelling and provenance fixes;
  the underlying algebra checked out.
```

RH remains unsolved. Every manuscript discussed below is external and unreviewed. This file reviews
the wave's *own* notes. It applies no fixes. The coordinator applies them.

## 0. Verdict in brief

The algebra and exponent bookkeeping of the wave are sound. I re-derived the following and found
them correct:
* RUNG_STRENGTH Observation 1 and Observation 2;
* Prop. R (the Mellin argument);
* Prop. R′, step by step against PR 910 §7;
* both directions of the endpoint Corollary;
* the Q_ρ orbit invariant;
* the fixed-point law `1 − 1/(6A)`;
* the SPF closed forms and the Hinz certificate;
* the Cartan determinant;
* the Robin constants.

The defects are of four kinds:
1. **Premise conflation:** ROBIN_GRADED states an equivalence with QRH-IMPORT, but QRH-IMPORT covers
   all Dirichlet `L`, and the equivalence holds only for `ζ`.
2. **Provenance:** PR 910 Prop. 7.2 is described as reviewed. PR 910's own REVIEW.md excludes it.
3. **Internal inconsistency:**
   * RUNG's Corollary and HEIGHT_LEVELS §4 contradict Prop. R′;
   * DISPERSION's "quasi-GRH ⇒ Mom(1, ρ) trivially" contradicts its own §3(a).
4. **Strengthening in summaries:**
   * "the Sep 30 architecture … proves 7/8";
   * the WMDS type ladder stated as fact;
   * "equivalent to sub-diagonal mean squares";
   * "c = 5/6 is forced", and 11/12 called "the optimum over all … families".

## 1. Issue table

Severity: **error** = false or self-contradictory statement; **overclaim** = stronger than the
evidence or the label allows; **imprecision** = true in substance but misstated, unqualified or
mis-cited; **cosmetic**. Line numbers are at HEAD `d47a0407`.

| # | File : location | Problem | Severity |
|---|---|---|---|
| 1 | ROBIN_GRADED l.24, l.36, l.199, l.212, l.262, l.293; CONDITIONAL_CONSEQUENCES l.27, l.76; README l.73 | "QRH-IMPORT is `H(7/8)`" and "QRH-IMPORT ⟺ Robin-type inequality". INTAKE defines QRH-IMPORT for **every Dirichlet L**. The Robin inequality is equivalent only to `Θ ≤ 7/8` for `ζ`. The ⇐ direction gives nothing about other Dirichlet `L` | **error** |
| 2 | RUNG_STRENGTH l.35, l.100; FOURTH_MOMENT_A2 l.35 | "PR 910's own review found no error" and "(reviewed there)" for Prop. 7.2. PR 910 REVIEW.md, line 5 at pr910: "the broader completed-height and higher-moment extraction arguments in UPSTREAM_HEIGHT_AND_MOMENTS.md are not independently reviewed by this report". PR910_REPLAY.md's scope also excludes it | **error** (provenance) |
| 3 | RUNG_STRENGTH l.135–136 (Corollary, third bullet); HEIGHT_LEVELS l.100–101 (§4 table) | The member exponent is given as `1/2 + ρ/2` (or "trivial" for ρ > 1). Prop. R′ in the same file gives `1/2 + 5ρ/12` for every member, which is nontrivial for all `ρ < 6/5` | **error** (internal inconsistency) |
| 4 | DISPERSION_GRH_STEP l.50–51 (§0 item 2), l.332–334 (§5 second bullet); SYNTHESIS l.72 | "quasi-GRH … already implies Mom(1, ρ) trivially". The file's own §3(a) shows that axiom (iv) at loss η gives `m = 1 + ρ + 2η`, which is not Mom(1, ρ). "By Prop. R it implies member half-planes 1/2 + ρ/2" is vacuous, because the input already gives `1/2 + η` | **error** |
| 5 | SYNTHESIS l.34 | "The Sep 30 architecture is the one that proves 7/8 today." The manuscript is external and unreviewed. This breaks the AGENTS.md boundary | **overclaim** (boundary) |
| 6 | SYNTHESIS l.124 | "Either QRH claim implies it with `c = (log 3)/8`". The Oct 5 (11/12) claim gives `(log 3)/12`, as SIEGEL §5 says | **error** (minor) |
| 7 | HEIGHT_LEVELS l.104, l.115 | "Going deeper is the same as going sub-diagonal"; "equivalent to sub-diagonal mean squares". Only Mom ⇒ half-plane holds. A member half-plane `β* > 1/2` does not give Mom(1, ρ) for any ρ (DISPERSION §3(a)). The converse holds only at the GRH endpoint | **overclaim** |
| 8 | HEIGHT_LEVELS §1.2 table (l.53–58), §5 (l.112); SYNTHESIS l.150–155; README l.62 | `A₁ → A₂ → Ã₂ → Lorentzian` is stated as the type of the dual objects. The `K_k` pair pattern is forced by the one-variable twisted multiplicativity of `γ₂`, for any split of `r` into coprime factors. A WMDS type also needs separate variables and the non-coprime prime-power data, which were not checked. The k = 3 check is implied by the k = 2 identity | **overclaim** (summaries); imprecision (HEIGHT) |
| 9 | HEIGHT_LEVELS l.94 | "Even its [quartic theta's] GL(2) coefficients are known only up to sign." LEVERAGE §3.3 says they are undetermined, and Eckhardt–Patterson is an open conjecture | **overclaim** |
| 10 | LEVERAGE_FAMILIES l.49 (§0), l.394–395 (§6); README l.63; RUNG_STRENGTH l.203–206 (§3(c)) | "c = 5/6 is forced"; "11/12 is the optimum over all Kummer families, products, quotients, norm forms and twisted rows"; "every other family fails"; "The only escape is …". These hold only relative to the HEURISTIC pipeline model of §3 and to the families examined | **overclaim** |
| 11 | SYNTHESIS l.78; HEIGHT_LEVELS l.101 | "A rigorous single-row proposition"; "(Prop. R, rigorous)". RUNG labels it PROPOSED, proved there but not reviewed | **overclaim** (label) |
| 12 | SYNTHESIS l.101–103; README l.71 | "Hinz gives 29/31, better than Kintali's 29/30". This is a model value, and SPF §6 says it is not a theorem. The obligation that Sep 30 Prop. 6.3 is *stated* only at `X = Y = Z^{1/2}` is missing | **overclaim** (mild) |
| 13 | RUNG_STRENGTH l.310–311 (§7 last sentence) | "The family estimate is useful exactly when it is proved without looking at individual members, i.e. at ρ ≥ 1." Rhetorical, and contradicted by the GRH endpoint | **overclaim** (mild) |
| 14 | Q_RHO_ANALYSIS l.371–372 | "zero-density exponent `A < 4/3` … would beat 7/8". Reaching the fixed point needs (Z1) uniformly over `N u ≤ H` at every iteration. Extraction and Prop. R′ give non-uniform member bounds | **imprecision** |
| 15 | SIEGEL_DETERMINANT l.51 | "(d) The proof is effective … `c ≳ 3·10⁻⁴`". §3(d) says "effective in principle (PROPOSED)", and its own table gives `δ_M(q = 3) = 2.8·10⁻⁴` with the paper's `H` | **imprecision** |
| 16 | CONDITIONAL_CONSEQUENCES l.51–66 | The Siegel and class-number bullets sit under "1.4 Non-improvements" but are called "a major consequence". The effectivity wording needs its conditions | **imprecision** |
| 17 | RUNG_STRENGTH l.66–87, l.105–107 | ψ_u is defined as the *primitive* character, but `F_u` and step 2 of R′ use the *imprimitive* symbol `χ_n(u)`. With the primitive character, step 2's identity fails at primes dividing `u` | **imprecision** |
| 18 | RUNG_STRENGTH l.32–37 (§1) | Prop. 7.2 is a cancellation bound for `A_1(D)`. The zero-free conclusion also needs Mom for **every** `W` and a Mellin step (PR 910 §7 "Consequences"). Mom(k, h) as defined fixes neither `W` nor `ν` | **imprecision** |
| 19 | RUNG_STRENGTH l.303 (§7 table); LEVERAGE l.185, l.191–192 | "principal member … rows `u = unit·v⁶`"; "principal iff `u ∈ (unit)·F^{×m}`"; "`u = ±w⁶` … principal". Units are not sixth powers, so `ψ_ε` is nonprincipal (checked: `(−1/π)₆ ≠ 1` at 24/44 primes). `−w⁶` and `+27w⁶` are nonprincipal; `w⁶` and `−27w⁶` are principal. Exponents are unchanged | **imprecision** |
| 20 | RUNG_STRENGTH l.220–222 (§4 item 2), l.307 (§7 "conductor dependence") | Prop. R′ at `N w = D^ω`, a conductor that grows with `D`. R′ is stated for fixed `u` (`≪_{u,k,h,η}`), so uniformity in `u` is unproved | **imprecision** |
| 21 | RUNG_STRENGTH l.155 | "the dual mean square equals its diagonal to within 1–3 %". The cited sources give `M/Diag ∈ [0.968, 1.137]` (A2_LITERATURE §5) and "within 4 %" (FOURTH_MOMENT_A2 §6) | **imprecision** |
| 22 | Q_RHO l.64, l.311–314; RUNG_STRENGTH l.191–192 | "Every known quadratic-twist asymptotic … degree ≤ 4"; "technology stops at degree 4". True over number fields. To my knowledge function-field results reach all moments over `F_q(t)` for large `q` (Bergström–Diaconu–Petersen–Westerland, arXiv:2302.07664; not re-read here) | **imprecision** |
| 23 | DISPERSION l.69 (§0 item 5), l.350, l.363–365; FOURTH_MOMENT_A2 l.230 | The stale "only non-involutive step" phrasing. The coordinator note at l.341–343 covers only §5 "below" | **imprecision** (stale) |
| 24 | SHORT_PROOF_FRONTIER l.258, header l.33–37 | "Lemma 15.1 hypothesis `M + ℓ = 1` lifted by the LP-verified third branch". The LP verifies the closed form of sup (14.14), not Lemma 15.1 off `M + ℓ = 1` (THRESHOLD §2, §7). At `ℓ = 0`, SPF §4 correctly reroutes through Lemma 5.8, which is stated for general `M`, but the header omits Prop. 6.3 | **imprecision** |
| 25 | "Prop. R" in DISPERSION (l.303 = Oct 5 prop:R; l.333 = RUNG's Prop. R), Q_RHO l.67, l.171, SYNTHESIS l.136–138 | The same name for two different statements | **imprecision** |
| 26 | README l.12; SYNTHESIS l.22 | "The manuscripts claim a zero-free half-plane `Re s > 7/8`". Oct 5 claims 11/12, Kintali 47/48, and Oct 1 is a Landau–Siegel statement | **imprecision** |
| 27 | HEIGHT_LEVELS l.56 | "4th (PR 910 (3.5))". UPSTREAM (3.5) is the partial-summation identity; the intended reference is FOURTH_MOMENT_REDUCTION.md (3.5) | cosmetic |
| 28 | DISPERSION l.211 | "RUNG_STRENGTH §2 Remark" does not exist. The `(N u)^{1/(12k)}` statement follows Prop. R′ | cosmetic |
| 29 | ROBIN l.35 (exponent called `b`; R3 uses β, with `b = Re ρ`), l.238 ("`Θ − 1/2 = 3/8`" should be "≤ 3/8") | notation | cosmetic |
| 30 | RUNG l.201 "`J(χ₃, χ₃) = −p`"; SPF `(Q²T²)` vs THRESHOLD §8 `(Q²T)` | `p` is the primary (≡ 1 mod 3) prime *element*. The height normalisation differs; the conductor exponent is unaffected | cosmetic |

## 2. Details, derivations and exact fixes

### 2.1 RUNG_STRENGTH.md

**Observation 1 (correct).** `(k + h − h/6)/(2k) = 1/2 + 5h/(12k) = 1/2 + 5ρ/12`. Also
`1/2 + 5ρ/12 < 7/8 ⟺ ρ < 9/10`. Hölder over `≍ D^h` rows gives
`Σ|A|² ≤ D^{h(1−1/k)}(Σ|A|^{2k})^{1/k} ≤ D^{1+h}`, which is Mom(1, h) at ρ′ = h ≥ h/k. That
matches "a larger ρ".

**Observation 2 (correct).** `D^{2k} ≤ D^{k+h} ⟺ ρ ≥ 1`. Under Mom(k, h),
`|A_u|^{2k} ≤ D^{k+h+ε}` gives `|A_u| ≪ D^{(1+ρ)/2+ε}`. *Cosmetic:* say "under Mom(k, h)" in
the second bullet.

**Prop. R (correct).** I re-derived each step:
* `∫_0^∞ W(Nn/D) D^{−s−1} dD = N(n)^{−s} Ŵ(s)`, with `y = Nn/D`.
* `A_u(D) = 0` for `D < 1/2`, and `A_u(D) ≪ D^{a+ε}` once `D^h ≥ N u`.
* Hence the Mellin integral is holomorphic on `Re s > a`, and it agrees with `Ŵ F_u` on `Re s > 1`.
* `E_u` has its poles on `Re s = 0` only.
* A zero `ρ₀` of `L(s, ψ_u)` with `Re ρ₀ > a` would force `Ŵ(ρ₀) = 0` for all `W ∈ C_c^∞(1, 2)`.
  This is false: take `W ≥ 0` concentrated near 1.
* If `ψ_u` is principal (`u = v⁶`), the pole of `ζ_K` is harmless.

*Imprecision (#17).* The statement defines `ψ_u` as "the primitive character inducing it", but:
* `F_u` must be `Σ μ(n)ν(n)χ_n(u)N(n)^{−s}`, with the imprimitive symbol, for the Mellin identity
  to hold;
* step 2 of R′ (`χ_n(u𝔭⁶) = ψ_u(n)1_{𝔭∤n}`) is true only for the imprimitive symbol, which
  vanishes when `(n, u) ≠ 1`.

**Fix:** after "denotes the primitive character inducing it" add: "We write `ψ_u^♭(n) := χ_n(u)`
for the imprimitive symbol (zero when `(n, 6u) ≠ 1`); `F_u` and step 2 of Prop. R′ use `ψ_u^♭`,
and `F_u = E_u/L(s, ψ_u)` with `E_u` as stated."

**Prop. R′ (correct as an adaptation; provenance wrong, #2).** I checked it against PR 910
(7.3)–(7.8):
* `N(u𝔭⁶) ≤ N u·Y⁶ = D^h`.
* The separation identity `A_u(x) = B_𝔭(x) − ν(𝔭)ψ_u(𝔭)B_𝔭(x/N𝔭)` holds. It uses
  `μ(𝔭m) = −μ(m)` and the complete multiplicativity of `νψ_u^♭`. Its inversion is a finite sum
  by compact support.
* The Hölder term is `(D^{k+h+ε} log Y/Y)^{1/(2k)} = D^{1/2+5h/(12k)}(N u)^{1/(12k)}(log)^{1/(2k)}`.
* The dyadic induction is unchanged, because `|ν(𝔭)ψ_u(𝔭)| = 1` and every argument is `≤ 2D/Y`.
* `0 < h < 6` is inherited from PR 910 (7.1).

The proposition is fine. But PR 910's REVIEW.md (pr910, line 5) states that the higher-moment
extraction arguments of UPSTREAM_HEIGHT_AND_MOMENTS.md are **not** independently reviewed.
reviews/PR910_REPLAY.md's scope ("exponent arithmetic and the stated geometric adapters ONLY")
excludes them too. Prop. 7.2 therefore has no review anywhere. My reconstruction above is a
partial check, not a review.

**Fix, l.35:** replace "[imported; PR 910's own review found no error]" with "[imported; PR 910's
REVIEW.md explicitly does not review it; reconstructed in Prop. R′ below, not independently
reviewed]".

**Fix, l.100:** replace "(reviewed there)" with "(not reviewed in PR 910; each step re-derived in
reviews/WAVE_REDTEAM.md §2.1)".

**Same fix in FOURTH_MOMENT_A2 l.35:** replace "which the same PR's review found no error in" with
"not covered by the same PR's review".

**Corollary (both directions correct; third bullet wrong, #3).**
* ⇒: Prop. R at k = 1, `h = ρ → 0`.
* ⇐: Perron at `Re s = 1/2 + ε` uses three bounds:
  * the rapid decay of `Ŵ`;
  * `1/L(s, ψ) ≪ (q(|t|+2))^ε` under GRH, uniformly in the conductor;
  * `|E_u| ≤ (1 − 2^{−1/2})^{−ω(6u)} ≪ (N u)^ε`.

  Together they give `A_u ≪ D^{1/2+ε}(Nu)^ε`, and summing gives `D^{1+ρ+ε}`. The equivalence is
  correct.
* The third bullet contradicts Prop. R′.

**Fix, l.135–136:** "In between, Mom(1, ρ) gives `1/2 + 5ρ/12` for every member (Prop. R′, via
the unreviewed PR 910 extraction), and the weaker `1/2 + ρ/2` for every member by the
self-contained Prop. R."

**§1 (#18).** **Fix, l.35–36:** "…says that Mom(k, h) for a fixed `W` implies `A_1(D) ≪
D^{(k+h−h/6)/(2k)+η}`; if Mom(k, h) holds for every smooth `W` on `[1, 2]` (fixed `ν = 1_{(n,6)=1}`),
the Mellin argument of Prop. R turns this into: `ζ_K`, hence `ζ`, has no zero in …".

**§3(b), l.155 (#21).** **Fix:** "…the dual mean square is diagonal-sized at tiny scale:
`M/Diag ∈ [0.968, 1.137]` for 1.8–43 rows per column (A2_LITERATURE §5), and within 4 % on the A2
checks (FOURTH_MOMENT_A2 §6)."

**§3(b) invariant bullet.** This is consistent with Q_RHO §2.3; I recomputed the orbit at
ρ = 9/10, and `|cols − rows| = 1/10` in all six states. Two small points:
* "a saving of some multiple `k(1−ρ)`" reuses `k`, which already denotes the moment order;
* the bullet should add the decisive conjunct.

**Fix:** "…asks for a deficit `j(1−ρ)`, `j ≥ 0`, below its own diagonal; `j = 0` occurs only at
Mom(1, ρ) itself, which has fewer rows than columns. No reachable state is both diagonal-sized and
has rows ≥ columns."

**§3(b) degree-4 bullet (#22).** **Fix:** "Quadratic-twist moment technology over number fields
stops at …".

**§3(c) (#10, #30).** **Fix, l.203:** "Within the HEURISTIC pipeline model of LEVERAGE_FAMILIES §3
and on known automorphic inputs, the only escape found is …".

**Fix, l.201:** "`J(ψ, ψ) = −π` for the primary prime element π (`π ≡ 1 mod 3`), `ψ = (·/π)₃`".

**§4 item 2 and §7 "conductor dependence" (#20).** Prop. R′ is for fixed `u`. For `N w = D^ω`,
two things go wrong:
* the starting threshold of the dyadic induction depends on `u`;
* below `x = (N w)^{1/h}` the row `w` is not even in range, so only the trivial bound `x` is
  available there.

**Fix:** append "(heuristic extrapolation of Prop. R′; uniformity in `u` is not proved)" to
item 2 and to the §7 conductor row.

**§7 table (#19).** **Fix, l.303:** "The principal member has multiplicity `≍ H^{1/6}` (rows
`u = v⁶`). The rows `ε v⁶`, with `ε` a nontrivial unit, carry the five nonprincipal members
`ψ_ε`, each with the same multiplicity."

**§7 last sentence (#13).** **Fix:** "At `ρ ≥ 1` the estimate can be proved row-blind (no single
row can violate it). At `ρ < 1` it already contains a power saving for every member
(Observation 2), so it cannot be proved without member-level input."

### 2.2 HEIGHT_LEVELS.md and a2/check_triple.py

**Cartan matrix (correct).**
* `C_k = 2I − (J − I) = 3I − J`.
* `J` has eigenvalues `k` (once) and `0` (`k−1` times), so `det C_k = 3^{k−1}(3−k)`, checked
  exactly for `k ≤ 7`.
* For `k ≥ 4` the signature is `(k−1, 1)`, so "Lorentzian" is right. `K_4` is moreover hyperbolic,
  since every proper subdiagram is `A₁`, `A₂` or `Ã₂`.
* `k = 3`: a 3-cycle is `Ã₂`.

**DGH comparison (correct in substance).** In DGH's multiple Dirichlet series for moments of
quadratic L-functions, the r = 4 moment is the star with four leaves, affine `D̃₄`, with an infinite
group. "Natural boundaries expected" is a fair "cf.".

**check_triple.py (reproduced).** I got 209 triples, deviation `3.54·10⁻¹⁴`, control `1.732`.
The formula matches the docstring: `(y/x)₃ = χ_x(y)²`, and the conjugated product of all three
pair symbols. Floating Gauss sums, so the label EMPIRICAL is right.

**Substantive caveat (#8).** The identity `γ₂(d₁⋯d_k) = ∏γ₂(d_i)∏_{i<j}conj((d_j/d_i)₃)` follows by
induction from the two-factor rule `γ₂(ab) = γ₂(a)γ₂(b)conj((b/a)₃)`. The `k = 3` check is
therefore implied by the `k = 2` check; it is a consistency check of `eis.py`, not new evidence.
The complete-graph pattern also appears for *any* split of `r` into `k` coprime factors, so the
coefficient of the single variable `r` has no intrinsic "k".

What makes `k` meaningful is the balanced `k`-fold divisor weight, i.e. giving each `d_i` its own
Mellin variable. Whether `Σ γ₂(d₁⋯d_k)∏ N d_i^{−s_i}` (with its quadratic factor) is a WMDS of
type `K_k` also depends on the prime-power data at primes dividing several `d_i`. The support is
cube-free, not coprime (PR 910 §8), and that data was not checked.

**Fix, §1.2 after the table:** "The pair pattern is forced by the one-variable twisted
multiplicativity of `γ₂`. The type assignment presumes one complex variable per factor (supplied by
the balanced divisor weight) and has been checked only on coprime squarefree support. It is a
PROPOSED coefficient-shape analogy, not an identification of the series."

Rename the table column "type" to "coprime-support coefficient shape".

**#9, l.94.** **Fix:** "Even its GL(2) prime coefficients are undetermined (non-unique Whittaker
models); the open Eckhardt–Patterson conjecture would fix their square (LEVERAGE §3.3)."

**§4 table (#3, #7, #11).** **Fix, rows 1–2:**

| statement | members `L(s, ψ_u)` | principal |
|---|---|---|
| Mom(1, ρ), `ρ > 1` | `1/2 + 5ρ/12` (Prop. R′, PROPOSED via unreviewed PR 910 extraction; nontrivial for `ρ < 6/5`) | `1/2 + 5ρ/12` → 11/12 |
| Mom(1, ρ), `ρ < 1` | `1/2 + 5ρ/12` (Prop. R′); `1/2 + ρ/2` (Prop. R, elementary, unreviewed) | `1/2 + 5ρ/12` |

**Fix, l.104:** "Going deeper *requires* going sub-diagonal: sub-diagonal mean squares imply
half-planes. The converse holds only at the GRH endpoint; a member half-plane `β* > 1/2` gives
`M₂ ≪ D^{1+ρ+2(β*−1/2)}`, not Mom(1, ρ) (DISPERSION §3(a))."

**Fix, l.115:** "implied by sub-diagonal mean squares (converse only at the endpoint); endpoint ⇔
family GRH".

**#27.** **Fix, l.56:** "4th (PR 910 FOURTH_MOMENT_REDUCTION.md (3.5); UPSTREAM (7.1) at k = 2)".

### 2.3 LEVERAGE_FAMILIES.md and Q_RHO_ANALYSIS.md

**Correct, as checked:**
* §1.1 chain `γ₁ = χ̄(4)γ₃γ₂² = −αχ̄(4)γ₃conj(γ₂)`, given `γ₂γ₄ = 1`, `γ₄ = conj γ₂` (ψ even) and
  `γ₂³ = −α`.
* The angle example `1/6 − 4/6 ≡ 1/2`.
* `J(ψ, ψ) = −π` for π ≡ 1 mod 3. This is Ireland–Rosen's `J = π` for `π ≡ 2 mod 3`, with
  `−π ≡ 2 mod 3`.
* §3.4: `m(n)` = denominator of `1/2 − 1/n` gives 2n / n/2 / n by n mod 4. All 7 rows of the σ
  table check, and the claim "σ < 11/12 only for m = 2 (r ≤ 5) or m ∈ {3, 4, 5}, r ≤ 2" is right.
* `n ∈ {6, 4, 10} ↔ m ∈ {3, 4, 5} ↔ 5/6, 7/8, 9/10` is consistent with RUNG §3(c).
* The no-Hecke-character-is-−1 argument is right.

**#19 (§2.1, l.185, l.191–192).** By Kummer theory, `n ↦ (u/n)_m` is principal iff
`u ∈ F^{×m}`. Units are not m-th powers here: `(ζ₆/π)₆ = ζ₆^{(Nπ−1)/6}`, and the eis.py check is
in the header. This contradicts the file's own §2.3, "kernel `F^{×m}`".

**Fix, l.185:** "principal in `n` iff `u ∈ F^{×m}`; each of the finitely many classes
`ε F^{×m}` (ε a unit) is a single nonprincipal member, so each member still has `≍ H^{1/m}` rows".

**Fix, l.191:** "(e.g. `u ∈ Z`, where `u = w⁶` or `−27w⁶ = ((1+2ω)w)⁶` are principal)".

**#10.** **Fix, l.49:** "**On the HEURISTIC model of §3 and every automorphic input currently
known, no examined family beats c = 5/6.**"

**Fix, l.394–395:** "…11/12 is the best value among the families examined here (Kummer, products,
quotients, norm forms, twisted rows), on the HEURISTIC model of §3."

**Fix, README l.63:** "every other examined family …".

**Q_RHO, correct, as checked:**
* §2.3: `P: (δ, s) ↦ (δ + s, −s)`, `R: (δ, s) ↦ (δ, −s)`, the six-state table and
  `ρ′ = (6−5ρ)/(5−4ρ) > 1`.
* The orbits of `j ↦ −j−2` mod 6.
* `k(ρ) = 4(3−2ρ)/(2−ρ)` (16/3, 24/5, 48/11).
* Li inflation: the minimum over `w` of `(max(1+ρ+5w, 2+ρ−2w) − ρ/6)/2` subject to `ρ + 6w ≥ 1` is
  `11/12` for `ρ ≤ 1/7` and `6/7 + 5ρ/12` otherwise.

**#14, l.371–372.** **Fix:** "…with exponent `A < 4/3`, **together with** zero-free half-planes for
all members `N u ≤ H`, uniform in `u`, at each stage of the bootstrap (not supplied by extraction
or Prop. R′, whose constants depend on `u`). Its formal fixed point `1 − 1/(6A)` would then beat
7/8."

**#22.** Add "over number fields" at l.64 and l.311. Add one line to §5: "Function-field results
(e.g. Bergström–Diaconu–Petersen–Westerland, arXiv:2302.07664) reach higher moments for large `q`;
they were not examined, and the number-field obstruction is what matters here."

### 2.4 DISPERSION_GRH_STEP.md

**Fixed-point law (correct).** Under (Z1)+(Z2), `f(σ) = Aρ(1−σ) + 2σ` is increasing iff `Aρ < 2`,
so the maximum is at `β*`. Then `σ_new = (Aρ(1−β*) + 2β* − ρ/6)/2 = β* + ρ(A(1−β*) − 1/6)/2`. This
is independent of ρ iff `β* = 1 − 1/(6A)`. Further checks:
* At `A = 2`, `σ_new = (1−ρ)β* + (11/12)ρ`, a convex combination, hence "never below 11/12" for
  ρ ≤ 1.
* `A = 12/5 → 67/72` and `A = 3 → 17/18`.
* §3(d): the relative precision `(H/L)^{2(1−β*)}` is correct.
* The §4 table (29/24, 17/16, 39/40; 23/24, 15/16, 37/40; 17/24, 13/16, 7/8) is all correct.

It is a fixed point of a *formal* map; see #14 for the iteration caveat. The header's "HEURISTIC in
constants" should read "HEURISTIC (constants, and uniformity over rows at each iteration)".

**#4.** §3(a) of the same file says axiom (iv) at loss η gives `m = 1 + ρ + 2η`.

**Fix, l.50–51:** "So DR's GRH input becomes a quasi-GRH (axiom (iv) at loss η) for the family
members `L(s, ψ_u)`, `N u ≤ H`, themselves. That gives Mom(1, ρ) only up to `D^{2η}`, and it already
contains member half-planes `1/2 + η`, stronger than anything extraction returns (§3(a))."

**Fix, l.332–334:** "…this is quasi-GRH for `L(s, ψ_u)`, `N u ≤ H`: it gives Mom(1, ρ) up to
`D^{2η}` and member half-planes `1/2 + η` directly." Delete "by Prop. R it implies member
half-planes 1/2 + ρ/2".

**SYNTHESIS l.72:** "Its GRH input becomes quasi-GRH for our own family after Poisson, which is
circular" is acceptable once DISPERSION is fixed.

**#23.** Extend the coordinator note to §0 item 5. **Fix, l.69:** "…must act through the theta
reflection (but see Q_RHO_ANALYSIS: it is also an involution, and (Q_ρ) ⟺ Mom(1, ρ))".

At l.363–365, replace "does not visibly return to A_u" and "has not been checked" with "returns to
`A_u` exactly (Q_RHO §2.1)". FOURTH_MOMENT_A2 l.230 needs the same note.

**#25.** In DISPERSION, l.303 is Oct 5 `prop:R` and l.333 is RUNG's Prop. R. Rename RUNG's
statement "Prop. R (RUNG)" (or "Prop. M", for Mellin) everywhere, and keep "prop:R" for the Oct 5
reflection bound.

**#28, l.211.** Replace "RUNG_STRENGTH §2 Remark" with "RUNG_STRENGTH §2, after Prop. R′".

### 2.5 SHORT_PROOF_FRONTIER.md vs THRESHOLD_CALCULUS.md

**Correct, as checked:**
* `a* = 1 − 1/(2A)` and `σ0 = (1+6a*)/(3+4a*) = (7A−3)/(7A−2)`. Balancing
  `1/3 + 7L/6 = (1−L)(2a* + 1/3)` gives `L = 4a*/(3+4a*) = (4A−2)/(7A−2)`.
* All five values: 29/31, 69/74, 40/43, 51/55, 11/12.
* The Hinz certificate weights `58/93, 35/93`.
* `(36a*−5)/(36a*−3) = (31A−18)/(33A−18)`, including 7/8 at `A = 18/17` with `ℓ = 1/6`.
* `29/31 − 7/8 = 15/248`.

**Comparison with THRESHOLD.** THRESHOLD §2 says:
* Lemma 15.1's proof uses `M + ℓ = 1`;
* the closed form `E_B` adds the branch `2M′ + ℓ′ − 1`;
* lifting `M + ℓ = 1` costs `(M + ℓ − 1)/2`.

SPF's frontier sits at `M = 32/31`, `ℓ = 0`, and the binding low row is exactly that branch (L3:
`E = 2M − 1`). The two notes are **consistent**, for three reasons:
* SPF pays the branch rather than ignoring it;
* at `ℓ = 0` SPF reroutes through Part I Lemma 5.8, which I checked is stated "for bounded ranges
  of `M ≥ 0`";
* the additive norm `(Q + Y²)/Y ≤ 2Q/Y` stays valid because `Q = q_{b*}XY = q_{b*}Y²`.

Two clarifications remain (#24):
1. **l.258:** "lifted by the LP-verified third branch" overstates. The LP verifies only that the
   closed form equals sup (14.14). **Fix:** "with the Lemma 15.1 hypothesis `M + ℓ = 1` replaced
   by the model's third branch (the LP-verified closed form of sup (14.14); Lemma 15.1 itself is
   proved only at `M + ℓ = 1`). At `ℓ = 0` the branch is supplied instead by Part I Lemma 5.8
   (§4)."
2. **Header gap:** add "and the proof of Prop. 6.3, which is *stated* only at `X = Y = Z^{1/2}`
   (Sep 30 paper.tex, prop:balanced-low), re-run at `X = Y = Z^{16/31}`". §4 l.273 already says
   this; the header and SYNTHESIS do not.

*Cosmetic (#30).* SPF writes `N ≪ (Q²T²)^{A(1−σ)}`, THRESHOLD §8 `(Q²T)^{A(1−σ)}`. Unify; only
the conductor exponent matters.

### 2.6 ROBIN_GRADED.md

**β-range of Robin's Ω-theorem: transcribed correctly, second-hand.**
* R3 quotes Lagarias: any `β ∈ (1 − b, 1/2)` with `b = Re ρ` for a zero with `Re ρ > 1/2`.
* Taking zeros with `Re ρ → Θ` gives every `β ∈ (1−Θ, 1/2)`, which is nonempty since `Θ > 1/2`.
* The lower half of Theorem V (`v_R ≥ −β` for all such β, hence `v_R ≥ Θ − 1`) follows.
* The upper half: `H(Θ)` holds by definition of sup, and Prop. R at θ = Θ gives `v_R ≤ Θ − 1` for
  `Θ < 1`; for `Θ = 1`, R2 gives `v_R ≤ 0`.
* The risk is correctly recorded in §1.4 and §7. The originals were not accessed, and I did not
  access them either.

**Other checks (correct).**
* Lemma K: integration by parts with `|R₁(t)| ≤ A t^{θ+1} + O(t)`, giving
  `A(1 + 2/(1−θ)) = A(3−θ)/(1−θ)` and `C_{7/8} = 17A`.
* `Σ 1/|ρ|² ≤ 2(1 + 14.1347^{−2})·0.0230957 = 0.046423`, so `17A ≤ 0.7892` and
  `e^γ·17A ≤ 1.4056 ≤ 1.41`.
* The crossover with R2 is at `log log n ≈ 34.6`.
* `ε(T) = 2.96·10⁻¹²`, `x ≲ 6.9·10²²` and `2.9·10³⁰`.
* Prop. R steps 1–5.

**#1 (error).**
* INTAKE.md l.30: "**(QRH-IMPORT)** every Dirichlet L-function, including ζ, has no zero with
  `Re s > 7/8`".
* ROBIN l.24: "`H(θ)` means that `ζ(s) ≠ 0` for `Re s > θ`, so QRH-IMPORT is `H(7/8)`".

QRH-IMPORT ⇒ `H(7/8)`, not conversely. The Robin-type inequality is equivalent to `H(7/8)`,
i.e. `Θ ≤ 7/8`, and says nothing about other Dirichlet `L`. All "⟺ QRH-IMPORT" statements are
therefore false as written.

**Fix (global):** introduce `QRH_ζ := H(7/8)` (the ζ-part of QRH-IMPORT). Then:
* **l.24:** "…so QRH-IMPORT implies `H(7/8)`; write `QRH_ζ := H(7/8)`, the only part used here."
* **l.36:** "In particular **`QRH_ζ` (Θ ≤ 7/8) ⟺ for every ε > 0, … for all sufficiently large n.**
  QRH-IMPORT implies this inequality; the converse gives only `QRH_ζ`."
* **l.199:** "…it is a **Robin-language equivalent of `QRH_ζ`** (the ζ-part of QRH-IMPORT)."
* **l.212:** "`≤ −1/8` (⟺ `QRH_ζ`; implied by QRH-IMPORT)".
* **l.262 (§5.4 proposed text):** "…so `Θ ≤ 7/8` ⟺ eventually …".
* **l.293:** "'`Θ ≤ 7/8` ⟺ `v_R ≤ −1/8`' is cofinal …".

Apply the same correction to CONDITIONAL_CONSEQUENCES l.76 ("with Robin's Ω-result this exponent is
sharp: `Θ ≤ 7/8` ⟺ that inequality for every `ε`") and to README l.73 ("…(so an asymptotic
criterion for `Θ ≤ 7/8`, the ζ-part of QRH)").

CONDITIONAL l.27 also *redefines* QRH-IMPORT as `Θ ≤ 7/8`, in conflict with INTAKE. **Fix:**
"**QRH-IMPORT** (INTAKE.md) is the unreviewed claim that every Dirichlet `L` is zero-free in
`Re s > 7/8`; Sections 1.1–1.3 and 2 use only its ζ-part `Θ ≤ 7/8`, while the Siegel bullet uses
the full statement."

**Cosmetic (#29).**
* l.35: "with every exponent β ∈ (1−Θ, 1/2)" (`b` is `Re ρ` in R3).
* l.238: "The exponent gap `7/8 − 1/2 = 3/8` (Θ − 1/2 ≤ 3/8 under QRH)".

### 2.7 SIEGEL_DETERMINANT.md and the class-number wording in CONDITIONAL_CONSEQUENCES.md

**Effectivity (#15).** §3(d) carefully says "effective in principle (PROPOSED)". It also notes that
the published and Lean statements are existential. But the §0 summary bullet (l.51) says flatly
"The proof is effective" and "`c ≳ 3·10⁻⁴`", while the §3(d) table gives `δ_M(q = 3) = 2.8·10⁻⁴`
at the paper's `H = 86 713 344`; `≥ 3·10⁻⁴` needs `H = 10⁹`.

**Fix, l.51:** "(d) The proof appears effective in principle (PROPOSED reading). Following the
manuscript's own constants gives `c ≈ 2.8·10⁻⁴` (`≈ 4·10⁻⁴` with `H = 10⁹`) for all `q ≥ 3`,
`q ≠ 8`, conditional on the manuscript; `q = 8` is handled separately." Apply the same to l.253
("`c ≈ 3·10⁻⁴`" → "`c ≈ 3·10⁻⁴` (2.8·10⁻⁴ at the paper's `H`)").

**§5 class numbers (correct).** The Goldfeld positivity argument with `1 − σ = c/ℓ`, `x = q^A`
gives `L(1, χ) ≫ (c/ℓ)e^{−Ac}`, effectively. The class-number formula then gives
`h(D) ≫ c√|D|/log|D|`.

**CONDITIONAL_CONSEQUENCES l.51–66 (#16).**
* The bullets sit under the heading "1.4 Non-improvements (recorded to prevent misreadings)" but
  describe "a major consequence". Move them to a new "1.5 Siegel zeros and class numbers
  (CONDITIONAL on QRH-IMPORT for all real primitive characters)".
* Reword: "Hence, **if QRH-IMPORT (or the Oct 5 claim) holds for every real primitive Dirichlet
  character**, `h(D) ≫ √|D|/log|D|` for imaginary quadratic fields, with an effectively computable
  constant. A half-plane should give more (`L(1,χ) ≫ 1/log log q` by the usual short Euler
  product argument; standard, not re-derived here). The logarithmic form is recorded only for
  comparison with the Oct 1 paper."
* Optionally, "(≤ 11/12 from the Oct 5 claim)" → "(`β ≤ 11/12`, hence `(1−β) log q ≥ (log 3)/12`,
  from the Oct 5 claim)".

**SYNTHESIS l.124 (#6).** **Fix:** "Either QRH claim would imply it, with `c = (log 3)/8` (Sep 30)
or `(log 3)/12` (Oct 5), effectively, and hence (conditionally) effective class-number lower
bounds."

### 2.8 SYNTHESIS.md and README.md: faithfulness

| Location | Problem | Exact replacement |
|---|---|---|
| SYNTHESIS l.22 (#26) | "The October 2026 manuscripts claim *quasi*-RH (a zero-free half-plane `Re s > 7/8`)" | "The October 2026 manuscripts claim zero-free half-planes (`Re s > 7/8` Sep 30; `Re s > 11/12` Oct 5; Kintali `47/48`) and, separately, a Landau–Siegel exclusion (Oct 1)" |
| SYNTHESIS l.34 (#5) | "the one that proves 7/8 today" | "The Sep 30 architecture is the one whose (unreviewed) manuscript claims 7/8." |
| SYNTHESIS l.72 (#4) | inherits DISPERSION's "quasi-GRH" | keep after the DISPERSION fix, or add "(at loss η; not Mom(1, ρ) itself)" |
| SYNTHESIS l.78–79 (#11) | "A rigorous single-row proposition: Mom(k,h) ⇒ … `1/2 + h/(2k)`" | "An elementary single-row proposition (PROPOSED, unreviewed): Mom(k,h) ⇒ … `1/2 + h/(2k)`. Prop. R′ (PROPOSED, via the unreviewed PR 910 extraction) improves every member to `1/2 + 5h/(12k)`. Mom(1, ρ) for all ρ > 0 ⟺ GRH for the family." |
| SYNTHESIS l.101–103 (#12) | "Hinz … gives 29/31 …, better than …" | "Hinz (`A = 5/2`) would give the **model value** 29/31 ≈ 0.9355 (not a theorem; SPF §6). This needs `M + ℓ > 1`, re-running Sep 30 Prop. 6.3 (stated only at `X = Y = Z^{1/2}`) and the Part I high-side steps at `X = Y = Z^{16/31}`." |
| SYNTHESIS l.124 (#6) | `(log 3)/8` for either claim | see §2.7 |
| SYNTHESIS l.150–155 (#8) | type ladder stated as fact | "…the dual coefficients have, on coprime squarefree support, the pair pattern of the complete graph `K_k` (Cartan matrix `3I − J`); read as a WMDS shape (PROPOSED analogy, not an identification): `A₂` at the 4th moment, affine `Ã₂` at the 6th, Lorentzian from the 8th." |
| SYNTHESIS l.183–186 | "Every reachable reformulation … is Mom(1, ρ) in disguise" | acceptable; optionally add "(each asks for a deficit `j(1−ρ)` below its own diagonal)" |
| README l.12 (#26) | "The manuscripts claim … `Re s > 7/8`" | as for SYNTHESIS l.22 |
| README l.62 (#8) | "the dual type goes A₁ → A₂ → affine Ã₂ → Lorentzian" | "the dual coefficient shape on coprime support goes A₁ → A₂ → affine Ã₂ → Lorentzian (PROPOSED analogy)" |
| README l.63 (#10) | "every other family fails …" | "every other examined family fails … (HEURISTIC pipeline model)" |
| README l.65 | omits Prop. R′ and the GRH endpoint | "…a single-row Prop. R and an every-member extraction Prop. R′ (PROPOSED); the endpoint Mom(1, ρ) ∀ρ > 0 ⟺ family GRH; …" |
| README l.71 (#12) | "Hinz gives 29/31" | "Hinz gives the model value 29/31" |
| README l.73 (#1) | "(so an asymptotic criterion for QRH)" | "(so an asymptotic criterion for `Θ ≤ 7/8`, the ζ-part of QRH)" |
| README l.35 | "must contain an on-average GRH" | acceptable; optionally "must imply the large-values count of RUNG §4 item 3 (an on-average GRH)" |

No summary was found to *invent* a result, and the RH boundary is respected everywhere. The
problems are the strengthenings listed above, plus the one boundary violation in SYNTHESIS l.34.

## 3. What was confirmed (for the record)

* Observations 1 and 2, Prop. R, Prop. R′ and the endpoint Corollary of RUNG_STRENGTH are
  mathematically correct. The Corollary's two directions are correct as stated, with Mom for every
  smooth `W`. The defects are provenance (#2), notation (#17) and the stale third bullet (#3).
* RUNG §3(a) is correct. It is a trivial single-row lower bound `Δ ≥ ‖b‖² ≍ L`, as the note itself
  says.
* RUNG §4 items 3 and 4 are correct as consequences: Chebyshev's count, and the fixed point
  `σ₀ = 11/12` of `σ₀(k−1)/k + 11/(12k)`.
* HEIGHT_LEVELS: `det(3I − J) = 3^{k−1}(3−k)`; signatures; the `Ã₂` and `D̃₄` comparison; the
  check_triple.py output reproduces.
* LEVERAGE: the absorption identity, the angle condition, the `m(n)` rule, and the σ table.
* Q_RHO: the orbit, the invariant `|cols − rows| = 1 − ρ`, the effective degree and the inflation
  law, all exact.
* DISPERSION: the fixed-point law `1 − 1/(6A)` and every number in §§3–4, exact.
* SPF: the closed forms and the certificate, exact. SPF is consistent with THRESHOLD's
  `M + ℓ = 1` finding.
* ROBIN: the constants, Lemma K, Theorem V's logic (given R3), and the β-range (as transcribed).
* SIEGEL: the conditional class-number chain is standard.

## 4. Smallest statements whose failure would matter

* RUNG Prop. R′ and everything built on it: PR 910 Prop. 7.2, step (7.8) (the dyadic induction).
  It is unreviewed. My re-derivation found no gap, but this is not a review.
* ROBIN Theorem V lower half: Lagarias's transcription of Robin's β-range (R3). The original was not
  read.
* SPF 29/31: Sep 30 Prop. 6.3 and Lemma 5.8 at `L = 16/31` and row exponent `32/31`.
