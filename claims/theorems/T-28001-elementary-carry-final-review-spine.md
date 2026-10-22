# T-28001 — Canonical elementary carry review spine

Claim ID: `T-28001`  
Status: **REVIEW CONSOLIDATION — ONE RH-EQUIVALENT THEOREM UNPROVEN**  
Date: 2026-08-08  
RH status: **UNPROVED**

## 1. Purpose

This file is a review front door, not a new proof mechanism. It consolidates the live elementary carry programme after the refutations and scope corrections on PRs #259, #265, #268, #269, #270, #271, #274, #276, and #277.

The repository has now isolated one canonical finite theorem. Parallel Green, endpoint-scale, fragmentation, factor-five, and transport proposals are retained only as possible producers for this theorem; none is imported as proved.

## 2. Canonical scalar

For the parabolic seed at endpoint `X`, let

\[
r_X(p)=v_p(b_X^{(0)})-p^{-1/2}\log(X/p)
\qquad(p\le X,\ p\text{ prime}).
\]

Put

\[
Y=\lfloor X/2\rfloor,
\qquad
s_X(p)=r_X(p)-\mathbf1_{p\le Y}r_Y(p).
\]

Define the weighted dyadic shell-tail charge

\[
\boxed{
\mathcal B_X
=
\max_{2\le z\le X}
\left[
\sum_{z\le p\le X}(\log p)s_X(p)
\right]_+.
}
\]

The canonical theorem is

\[
\boxed{
\textbf{WSTS:}
\quad
\forall\varepsilon>0,
\qquad
\mathcal B_X=O_\varepsilon(X^\varepsilon).
}
\]

PR #276 `T-27501` proves at proposed-complete scope

\[
\boxed{\mathrm{WSTS}\Longleftrightarrow\mathrm{RH}.}
\]

In particular, under RH one has the stronger quantitative bound

\[
\mathcal B_X=O(\log^4 X).
\]

Thus WSTS is not a routine sampling lemma left after the geometry. It is exactly the final RH-bearing arithmetic scalar.

## 3. Canonical proof spine

The only conclusion-producing elementary spine retained for review is

```text
sharp parabolic seed
-> dyadic endpoint shell subtraction
-> continuum weighted shell-tail majorization
-> exact finite floor/sampling decomposition
-> WSTS
-> weighted prime-tail transport
-> dyadic shell telescope
-> ordinary-prime ramp >= 4 sqrt(X)-X^o(1)
-> complete prime-power ramp
-> square-screw / Landau pole exclusion
-> RH.
```

Every arrow except unconditional WSTS has a current finite/analytic claim in the frozen PR #276 dependency packet.

## 4. What is genuinely closed at current proposed-exact scope

The following are not separate open existence problems in the canonical spine:

1. **Positive seed geometry.** PR #265 proves that the sharp parabolic seed is already a nonnegative average-binomial carry-row combination and that its endpoint increments form positive atoms.
2. **Continuum order.** PR #265 proves the upper-tail defect inequality `int_theta^1 E<=0`, including the exact reciprocal-cell analysis.
3. **Finite shell geometry.** The frozen PR #240/#276 packet gives the exact dyadic shell subtraction, finite carry-floor decomposition, and weighted prime-tail transport.
4. **Prime-power reduction.** The ordinary-prime and complete prime-power ramps differ only by the declared lower-order term.
5. **Analytic consumer.** The source-pinned square-screw/Landau transfer turns the sharp ramp into RH.
6. **Converse.** PR #276 proves `RH -> WSTS` quantitatively by Stieltjes integration against `vartheta(t)-t`.

These claims still require adversarial reconstruction at their frozen heads, but no additional theorem is silently assumed in this consolidation.

## 5. Superseded or refuted closures

The following must not be used as completed dependencies:

- Generic truncated absolutely-monotone/B-spline shift positivity: refuted on PR #259.
- Direct no-double-spend prime-shift parent charging: refuted by root overload on PR #259.
- Sharp FGCM as a moving-horizon escape from the global Gamma factor: removed by the compactness/tightness argument on PR #259.
- Monotone positive-part divisibility cover: refuted by square-root-scale dual cost.
- Prime-only subpower queue/tail `PTQ/PTC`: proposed refuted by deterministic positive density drift on PR #274.
- One-frequency reflected physical block: refuted in the earlier review graph.
- Direct pure-carry physical transference: rejected on PR #269 because the carry window supplies a zeta factor that cancels the RH pole.
- Conditional-Hankel/Bernstein middle line: refuted by the exact `-233/64` determinant.

## 6. Parallel mechanisms and their correct role

The following are **producer attacks on WSTS or an equivalent prime-ramp scalar**, not independent completed proofs:

- endpoint-scale blocker control `ESBT/ESGS` — PR #265;
- factor-five boundary/commutator transition `BCF5TC` — PR #269;
- affine-continuum finite Green deformation `FAGD` — PR #270;
- source-image factor-five domination `SIFD` — PRs #263/#271;
- squarefree collector lift `SCL` — PR #274;
- cycle debt `CDT` — PR #272;
- binary–ternary producer / half-moment alternatives — PR #277;
- annular dual frame `ADF` — PR #267, known to be overstrong on the logarithmic ray.

A future completion from any of these routes must export an explicit WSTS bound, the sharp prime-ramp bound, or a formally mapped RH-equivalent scalar. Merely proving its finite geometry is insufficient.

## 7. Why the project is not yet an unconditional proof

`T-27501` itself records

```text
unconditional WSTS      UNPROVEN
Riemann Hypothesis      UNPROVEN
```

and the recent producer PRs continue to mark their own cofinal estimates open. No current branch supplies an unconditional proof of

\[
\mathcal B_X=O_\varepsilon(X^\varepsilon).
\]

Therefore this consolidation must not be represented as an RH proof.

## 8. Reviewer protocol

Reviewers should freeze PR #276 at

```text
a65a02b9463c1cc3a10d0af03ab359a637e357cd
```

and reconstruct the following in order:

1. the parabolic shell definitions and dyadic telescope;
2. the continuum weighted upper-tail sign and quantitative moat;
3. the finite carry-floor and prime-sampling decomposition;
4. the exact weighted transport cost;
5. `WSTS ->` sharp ordinary-prime ramp;
6. ordinary-prime to prime-power reduction;
7. square-screw/Landau normalization and sign orientation;
8. `RH -> WSTS` via the Stieltjes remainder;
9. the equivalence statement.

A reviewer should **not** attempt to verify every parallel producer before deciding the status of the canonical reduction.

## 9. Mandatory mutation tests

Reject a claimed unconditional completion if it:

1. substitutes a continuum integral for the weighted prime sample without a uniform Stieltjes remainder;
2. uses fixed-ratio PNT uniformly at a shrinking ratio;
3. takes positive parts before the complete dyadic shell recombination;
4. removes the logarithmic/von-Mangoldt mode;
5. loses the dyadic or `2/3` Mertens mutation;
6. invokes a finite numerical ladder as a cofinal theorem;
7. silently imports `ESBT`, `FAGD`, `SIFD`, `BCF5TC`, `SCL`, `CDT`, `ADF`, or another open producer;
8. returns to any refuted one-frequency, generic-Hankel, bounded-rank, or monotone-cover argument.

## 10. Final status

```text
positive elementary carry geometry          CONSOLIDATED / PROPOSED COMPLETE
continuum shell ordering                    CONSOLIDATED / PROPOSED COMPLETE
finite shell and transport algebra          CONSOLIDATED / PROPOSED COMPLETE
WSTS -> prime ramp -> RH                     PROPOSED COMPLETE
RH -> WSTS                                   PROPOSED COMPLETE
WSTS <=> RH                                  PROPOSED COMPLETE
unconditional WSTS                          OPEN / RH-EQUIVALENT
Riemann Hypothesis                          UNPROVED
```

The repository is therefore ready for a focused adversarial review of the **final reduction**, but not for an unconditional RH-proof verdict.