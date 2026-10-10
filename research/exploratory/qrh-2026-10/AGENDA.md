# Bounded open problems from the October 2026 quasi-RH wave

```text
Status: OPEN problem list (no claims); each item states its payoff and its exact source
Scope: next steps for the two external architectures and their bridges to this repository
Exact sources or dependencies: SYNTHESIS.md and the files cited per item; PRs 908-910; branch w5copg
What was actually run: n/a (planning document)
Smallest remaining gap: n/a
```

RH remains unproved. Items are ordered by leverage toward the critical line, not by ease. Each one
names its payoff *if* the imported, unreviewed manuscript machinery is correct.

## A. The moment ladder (Oct 5 architecture): the only route found that scales to 1/2

> **Reframing ([RUNG_STRENGTH.md](RUNG_STRENGTH.md)).** Every rung's boundary is `1/2 + 5ρ/12` in
> `ρ = h/k` alone. A1 is therefore one instance of the basic target, the **sub-diagonal second
> moment**
>
>     Σ_{N u ≤ D^ρ} |A_u(D)|² ≪ D^{1+ρ+ε},   ρ < 1.
>
> * `ρ < 9/10` beats 7/8.
> * Numerically it holds at `ρ ≥ 0.4` for `D ≤ 64000` (finite).
> * Any proof must contain an on-average GRH for the sextic family, and row-blind large sieves
>   cannot give it.
>
> The fourth moment below is worth pursuing only for its bilinear structure.

**A1. Partial fourth-moment rung (PROPOSED target).** Prove a diagonal-size fourth moment over a
row range *shorter than* `D²`: for some `h < 2`,

    Σ_{N u ≤ H} |A_u(D)|⁴ ≪ D^{2+ε} H,   H = D^h,
    A_u(D) = Σ_n μ(n) ν(n) χ_n(u) W(N n/D),

over **all** rows `u`, sixth powers included. This is PR 910's moment hypothesis with general `h`.
Its exact prime-removal recursion (Prop. 7.2: Hölder exponent `(k + h − h/6)/(2k)`) then gives
zero-freeness for

    Re s > 1/2 + 5h/24.

Equivalently, writing `h = 2 − η`, the boundary is `11/12 − 5η/24`.

Thresholds:
* any `h < 2` beats 11/12;
* `h < 9/5` beats 7/8;
* `h → 1` gives 17/24.

Notes:
* At `h = 2` the bound is large-sieve-sized, yet even that is not a consequence of a known large
  sieve: the sextic BGL large sieve carries an extra `(HN)^{2/3}` term.
* PR 910's reduction (3.5) to balanced-divisor columns applies.
* Smallest first step: the case `c = 1` of (3.5) at `X = D` with `H = D^{2−η}`.

**A2. GL(3) reflection: the decisive local computation.** The fourth-moment dual has coefficients
`γ₂(d)γ₂(e)·conj((e/d)₃)` ([FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md)). Compute the row twist
produced at a prime `p | h` by the A2 functional equation, or equivalently by the automorphy of the
cubic `GL(3)` theta, with Kazhdan–Patterson's unique Whittaker model. In `GL(2)` it was
`χ_p^{-1}χ_p^{-2} = χ_p³` (quadratic), which made Goldmakher–Louvel's large sieve applicable.
* Quadratic again: A1 becomes a well-posed `GL(3)` analogue of the Oct 5 proof.
* Cubic: the BGL extra term must be beaten.

**Status after the literature check: closed as proposed.** The cubic theta on `GL(3)` has
`τ(m,1) = 0` unless `m` is a cube, so its coefficients vanish on every coprime squarefree pair.
The A2 functional equations act only on Gauss-sum variables, keep the twist index, and lengthen
the sums in the needed regime ([A2_LITERATURE.md](A2_LITERATURE.md) §§3, 6). What would be needed
instead is an unconditional dispersion asymptotic for `Σ_h |C_h|²` with error `O(L^{2+ε})`.
Dunn–Radziwiłł's estimate does not supply it, even under GRH, and its GRH input is circular here
([DISPERSION_GRH_STEP.md](DISPERSION_GRH_STEP.md)). The precise target is to keep the `μ(f)` sign
through the positivity step (eq:weighted). The candidate (Q_ρ) is stated there as OPEN.

**A2′. Induction by alternating Poisson and reflection (SPECULATIVE).** One `GL(2)` reflection of
the fourth-moment dual returns a Möbius sum in the second factor `e`, twisted by
`conj(α(e)) χ_e(h)` with cubic pair phases ([FOURTH_MOMENT_A2.md](FOURTH_MOMENT_A2.md),
second-step analysis). Its rows satisfy `N h ≤ 𝓗 = X⁴/H`, and `𝓗 > X^{1+θ}`. That is the regime
where an Oct 5-type mean square of Möbius sums gives square-root cancellation on average.

Two questions remain:
* whether the Oct 5 mean square extends to an angular twist `conj(α)` plus the pair-phase
  cocycle. PR 910 Prop. 4.4 already handles archimedean twists with a polynomial conductor cost;
* whether the coupling to the long reflected `ℓ`-sum (length about `(N(h)N(e))²/X`) can be
  organized as a bilinear form that this mean square controls.

If both work, the `k`-th moment would reduce to a `(k−1)`-th-type statement for a twisted family,
which is an induction on the moment ladder. Nothing here is checked beyond the local identities.

**A3. Fourth-moment numerics on the true sextic family.** PR 910 tested only `±1` surrogates; see
[moments/](moments/README.md). Report `M₄/(diagonal)` across `D`, the row-type decomposition, and any
structured excess. A finite trend is not a theorem, but a structured excess would falsify A1 at
small `η`.

## B. The 7/8 architecture (Sep 30): structurally capped

**B1. Cross-row cancellation for zero-free rows.** A signed bound
`Σ_{u ∈ floor bin} q_u^{-z} L(w,χ_u) H/L(s,ηχ_u) ≪ U^{1−θ}` on the central contours. With DH-quality
counts, `θ ≥ 1/50` reaches 13/15. Below 13/15 it must be combined with B2. No rigorous `θ > 0` is
known ([FLOOR_BIN_BARRIER.md](FLOOR_BIN_BARRIER.md)).

*Cross-architecture remark.* The Oct 5 mean square controls truncated reciprocals
`A_u ≈ 1/L(s, χ_u)` on average over rows. Used through Cauchy–Schwarz it gives only absolute-value
control. The floor bin needs a *signed first moment* of the ratios `L(w, χ_u)/L(s, ηχ_u)`, and over
a *zero-defined* subset of rows, which breaks the Poisson/theta structure that makes the full row
sum tractable. A workable variant would estimate the sum over all rows by the probe identity and
subtract the few non-floor rows using zero-density counts. Whether that subtraction can be made
uniform is open.

**B2. Bilinear saving on the reflected side.** Beat Cauchy–Schwarz in `Σ_m A_m(Y) B_m(Z)` by
`Z^{ϑ}`. The barrier moves by `4/5` per unit ([THRESHOLD_CALCULUS.md](THRESHOLD_CALCULUS.md) §5),
and the paper's own optimum by `≈ 0.8125` per unit ([BILINEAR_B2.md](BILINEAR_B2.md)).
* No known theorem gives `ϑ > 0`.
* Exact gap: a bound better than the large sieve for `Σ_m w(m) χ̄_s(m) B_m`, averaged over
  `s ≍ Y'`.
* The `P_a^{1/6}` excess matches the conjectured `n = 6` large-sieve term of
  de Faveri–Dunn–Hoffstein, so it is likely genuine.

**B3. Things that are not worth doing.**
* Tuning the geometry: exhausted at ≈ 0.874957.
* Iterating the bootstrap.
* Single moment constants: under `5·10⁻⁴` each.
* Joint moments: at most 1/192, because the floor bin binds.

## C. Verification (needed before anything above is cited)

**C1.** Build the 7/8 Lean closure and run the comparator challenges, and record
`#print axioms`. See [reviews/LEAN_BUILD_ATTEMPT.md](reviews/LEAN_BUILD_ATTEMPT.md) for this wave's
attempt. *Done in part:* the closure is built; `#print axioms` is standard for the zeta,
Dirichlet and Hecke theorems; comparator accepts the zeta, Dirichlet and Hecke challenges;
the remaining comparator runs are recorded in Addendum C.

**C2.** Kintali Lemma 3 (weak reflection, Appendix B) and identities (4)–(6).
* *Done in this wave: no error found* ([reviews/KINTALI_LEMMA3_REVIEW.md](reviews/KINTALI_LEMMA3_REVIEW.md)).
* Remaining unverified step: App. A.2 ("fixed and moving phase cancellation"), which serves the
  high-side identity.

**C2′. Lemma 18.1 of the 7/8 manuscript** ([reviews/LEMMA18_1_REVIEW.md](reviews/LEMMA18_1_REVIEW.md)).
* It asserts a Lindelöf-strength fourth moment of the sextic family, which would be new as a
  standalone theorem.
* A bounded review found no error. The first unverified step is the common-support allocation
  (paper.tex l. 13192–13349 and 13686–13933).
* The numerology has zero slack at three points. This is the highest-value single verification
  target in the 7/8 manuscript.
* *Complete read* ([reviews/LEMMA18_1_CASE2_SEC188.md](reviews/LEMMA18_1_CASE2_SEC188.md)).
  * With case 2 and Sec. 18.8 done, every proof line of Lemma 18.1 has been read with no wrong
    step found.
  * Imported: helper Lemmas 4.x and Sec. 13; the ray-class prime ideal theorem; Rankin.
  * Not a certification.
* *Follow-up done* ([reviews/LEMMA18_1_COMMON_SUPPORT.md](reviews/LEMMA18_1_COMMON_SUPPORT.md)):
  no error was found in the common-support allocations, and 24/24 checks passed. Lemma 18.1 as a
  whole is still not certified. Case 2, Sec. 18.8 and the use in Prop. 19.2 remain unreviewed.

**C2″. Spin-off: the cubic fourth moment** ([CUBIC_FOURTH_MOMENT_TRANSFER.md](CUBIC_FOURTH_MOMENT_TRANSFER.md)).
* Lemma 18.1's scheme, transferred to cubic characters, fails as is. The saving is `κ = 5/6`
  at the `(2,1)` common primes.
* A proposed residue repair closes it with zero slack.
* A relaxed induction heuristically gives `X^{53/51+ε}` for the fourth moment of cubic Hecke
  L-functions, against `X^{4/3+ε}` from known tools.
* Writing out the relaxed induction is a concrete target that would be new as a standalone result.
  It is conditional on Lemma 18.1's unverified bookkeeping.
* *Done as exponent ledgers* ([CUBIC_RELAXED_INDUCTION.md](CUBIC_RELAXED_INDUCTION.md)):
  * the paper's induction order gives exactly `X^{53/51}`;
  * the (2,1) forcing gives `X^{1+ε}` with zero slack;
  * a PROPOSED nested comparison order gives `X^{1+ε}` with margin `M/12`, and in the quadratic case
    reproduces Heath-Brown's `K^{1+ε}`.
* Six steps are unproved, including the n = 3 bookkeeping and the legitimacy of the nested order.
  If all of them hold, this would be the optimal cubic fourth moment, an open problem; the
  literature best is `X^{4/3}`. Highest-value non-RH spin-off of the wave.
* *Adversarial check* ([reviews/CUBIC_NESTED_REDTEAM.md](reviews/CUBIC_NESTED_REDTEAM.md)): no
  break at ledger level.
  * The nested order is well-founded, and the uniform margin is `≈ 0.018M`.
  * Patterson bias enters as the modelled exceptional excess.
  * Remaining for `n = 3`:
    * cubic correlations at prime powers;
    * the Kummer/fixed-ray lemma with `μ₃`;
    * the centred-stage saving (`L ≲ 0.42M`, `F₁ + F₂ ≥ (5/6)v`, total loss `< M/12`).
  * Everything stays conditional on the unreviewed Lemma 18.1 machinery.

**C3.** The coefficient (7.4) of the 7/8 manuscript, factored into the local series (7.10). This
needs (7.9) and the `b*`/`ξ`/`τ` and pair-phase cancellations; only the local identity was checked
([numerics/](numerics/README.md)).
* *Done in this wave* ([numerics/COEFF74_CHECK.md](numerics/COEFF74_CHECK.md)): on 141,264 tuples,
  (7.4) equals the product of the (7.10) local summands, with relative deviation 7e-13 on nonzero
  values. The `b*`/`ξ`/`τ` and pair phases are exercised, and all 16 controls fail.
* This is finite floating point. Gaps: `r ≥ 1` for three families, `k = 3`, and the analytic part
  of (7.5).

**C4.** PR 910's 139999/160000 deduction, second replay
([reviews/PR910_REPLAY.md](reviews/PR910_REPLAY.md)), and its height route
([falsification/](falsification/)).

## D. Bridges back to this repository's own programmes

**D1.** Port the twisted NRC32 adapter and record the exact twist set generated by the coarse
kernel. This decides whether a family-supremum bootstrap for issue 902 needs a finite family or a
growing-conductor family ([BRIDGE_MELLIN.md](BRIDGE_MELLIN.md) C1–C2).
* *Done in this wave* ([NRC32_TWISTS.md](NRC32_TWISTS.md)): the coarse kernel generates only the
  trivial character.
* So the family-supremum mechanism gives nothing for issue 902; twists decouple through the Newton
  identity.
* The step stays RH-equivalent: BM-3 needs a representation of `S_Y` that does not depend on where
  the zeros are.

**D2.** Record each Θ-graded repository criterion with exponent `θ` in place of "subpower". Under
the import the starting exponent is `3/8`; RH needs `0`
([CONDITIONAL_CONSEQUENCES.md](CONDITIONAL_CONSEQUENCES.md), Lemma G).
