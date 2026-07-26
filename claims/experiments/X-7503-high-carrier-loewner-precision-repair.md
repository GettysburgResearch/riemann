# X-7503 — High-carrier Loewner precision repair

Claim ID: X-7503  
Title: Fresh 130-decimal direct-`xi` replay reverses two apparent high-order Loewner negatives induced by rounded 50-decimal transport strings  
Status: EMPIRICAL  
Authoring agent: `gpt56-08`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: L-7501, L-7504; X-7501 node and normalization conventions  
Scope: numerical conditioning and candidate-triage rule for direct completed-`xi` Loewner minors  
Related counterexample candidates: none

## Statement

At the exact ordinate

\[
 T=\frac{20225875608343121406355}{2^{32}},
\]

use the nine exact horizontal nodes

\[
 x=2^{-k},\qquad
 k\in\{20,18,16,14,12,10,8,6,5\},
\]

and define

\[
 G(u)=\log\left|
 \xi\!\left(\frac12+\sqrt u+iT\right)
 \right|^2,
 \qquad u=x^2.
\]

Form the twelve increasing cross-Loewner minors declared by X-7502.

Evaluating those minors from the rounded relative-logarithm strings committed by
X-7501 produces the apparent signs

\[
 D_{3,0}\approx-8.2617864354\times10^{-38},
 \qquad
 D_{4,0}\approx-4.7294737295\times10^{-53}.
\]

A fresh direct evaluation of every primitive value at 130 decimal digits gives
instead

\[
 \boxed{
 D_{3,0}\approx
 1.3781895945113788266796882269\times10^{-40}>0,
 }
\]

and

\[
 \boxed{
 D_{4,0}\approx
 3.0974729927292389272641596989\times10^{-64}>0.
 }
\]

All twelve freshly evaluated minors are positive.  Thus the two negative signs
computed from the X-7501 transport strings are **precision ghosts**, not
counterexample nominations.

This is an ordinary arbitrary-precision result, not a directed certificate.

## Definitions

For disjoint increasing node lists `u_1<...<u_n` and `v_1<...<v_n`, the
cross-Loewner matrix is

\[
 L_{ij}=\frac{G(u_i)-G(v_j)}{u_i-v_j}.
\]

The relevant minor is `det L`.  The node lists and identifiers `d2-0` through
`d4-1` are exactly those fixed in X-7502.

The completed function is

\[
 \xi(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The fresh evaluator computes the real logarithm of the modulus through

\[
\begin{aligned}
 \log|\xi(s)|^2=2\biggl(&\log|s|+\log|s-1|-\log2
 -\frac{\operatorname{Re}s}{2}\log\pi\\
 &+\operatorname{Re}\log\Gamma(s/2)+\log|\zeta(s)|\biggr).
\end{aligned}
\]

## Motivation

High-order total-positivity minors cancel large correlated backgrounds.  Their
final values can be dozens of orders of magnitude smaller than the primitive
logarithms and many orders smaller than the displayed relative increments.
Such minors are powerful search objects, but only when discovery precision is
chosen from the condition number rather than from the number of visible digits
in a primitive table.

This experiment prevents a visually compelling but false pair of negative signs
from being promoted and supplies an explicit sensitivity budget for future
searches.

## Computation

The reproduction script is

```text
experiments/X-7503-xi-loewner-precision-repair/replay_high_precision.py
```

and the preserved output is

```text
experiments/X-7503-xi-loewner-precision-repair/results/replay-130d.json
```

The run used Python 3.13.5, mpmath 1.3.0, nine processes, and 130 decimal digits.
Every primitive value was recomputed directly; the old strings were used only
for the comparison block.

The fresh determinant ladder includes

```text
d2-0  +1.0343222578901203427717044993519e-15
d2-1  +2.6478644616346923300315400379493e-13
d2-2  +6.7785117814687776202097548230517e-11
d2-3  +1.7352120200499793435237158881792e-8
d2-4  +4.4385822493094465952942071096220e-6
d2-5  +2.7982946354341669576321792949112e-4
d3-0  +1.3781895945113788266796882269029e-40
d3-1  +2.3120305355656669941550290749882e-33
d3-2  +3.8739045475361688464200795988667e-26
d3-3  +3.9933173827948163059357888193556e-20
d4-0  +3.0974729927292389272641596989115e-64
d4-1  +1.3364232083718981643258716362400e-51
```

## Sensitivity explanation

At the fresh point, the numerical first variation of `d3-0` with respect to the
relative primitive logarithms at `k=20,18,16,14,12,10` is approximately

\[
 (-4.95043049,\ 5.28045416,\ -0.331317559,
   0.00129420924,\ -3.14739717\times10^{-7},
   4.50241852\times10^{-12}).
\]

The 50-decimal transport corrections in the dominant `k=20` and `k=18`
coordinates are of order `10^-38`.  Their contraction against coefficients of
order five is therefore naturally of order `10^-38`, while the true determinant
is only `1.38e-40`.  The observed sign reversal is quantitatively explained by
the condition number; no anomaly remains.

## Precision-budget rule

For a frozen minor `D(y)` over primitive vector `y`, a discovery sign must not be
promoted unless a declared primitive error box `|delta y_j|<=epsilon_j` satisfies

\[
 |D(y)|>
 \sum_j |\partial_jD(y)|\epsilon_j
 +R_2,
\]

where `R_2` bounds the nonlinear remainder, or unless a direct interval
contraction already excludes zero.  Decimal display precision is not an error
bound.

For high-order minors, the discovery producer should recompute primitive values
with guard digits until the complete sensitivity budget is at most one quarter
of the observed margin, then freeze exact nodes before directed replay.

## Analytic domain audit

- Every node has `u>0`, so the real modulus logarithm is meaningful provided the
  evaluated completed-`xi` rectangle excludes zero.
- The mpmath computation does not certify nonvanishing or an error radius; it is
  reconnaissance only.
- No branch of complex `log xi` is used.  The evaluator combines real logarithms
  of absolute values and the real part of `loggamma`.
- The exact ordinate and horizontal nodes are unchanged between the old and new
  computations.

## Dependency audit

- L-7501 supplies the direct completed-`xi` horizontal object under RH.
- L-7504 supplies nonnegativity of increasing cross-Loewner minors under RH.
- X-7501 supplies the target and rounded comparison strings.
- X-7502 supplies the twelve node-list definitions.
- No directed Riemann--Siegel or Arb output is imported into the fresh mpmath
  calculation.

## Gap audit

- The 130-decimal values are not outward-rounded intervals.
- Agreement between two mpmath precisions would still not constitute an
  independent backend reproduction.
- The old strings were rounded transport values, not a promise of 50 correct
  decimal places after determinant contraction.
- A determinant's sign cannot be inferred coordinatewise from positive
  primitive increments.
- The result closes only this exact finite target and node table.
- A future directed negative at the same target would supersede this empirical
  result rather than contradict it.

## Adversarial tests

1. Recompute at 100 and 130 decimal digits and require stable leading digits of
   all fresh determinants.
2. Recompute `d3-0` from the committed rounded strings and require the negative
   comparison sign.
3. Perturb each primitive independently by `10^-60` and compare the finite
   difference with the recorded sensitivity.
4. Add a common constant to all `G(u)` values and require every secant and
   determinant to remain unchanged.
5. Permute one node list out of increasing order and verify the expected
   orientation-sign change rather than treating it as an RH violation.

## Remaining uncertainty

A proof-grade Arb/Riemann--Siegel direct-`xi` replay at this shifted ordinate has
not yet been preserved.  The empirical positive signs are stable at the used
precision but are not certified intervals.

## Suggested next attack

Do not spend further search effort on the same fixed nine-point table.  Move the
exact ordinate and node geometry, use sensitivity-aware precision from the first
pass, and direct proof-grade escalation toward order-two or well-conditioned
order-three rows whose discovery moat is many orders larger than the complete
primitive uncertainty budget.
