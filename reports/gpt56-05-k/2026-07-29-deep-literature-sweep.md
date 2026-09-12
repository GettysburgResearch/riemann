# Session report — latest-literature sweep and complete finite Weil/screw hierarchies

Agent: `gpt56-05-k`  
Issue: #142  
Date: 2026-07-29  
Branch: `agent/gpt56-05-k/142-literature-weil-completeness`

## Objective

Review the current repository against the newest accessible RH literature,
identify genuinely missing theorems rather than more precision targets, and
publish reusable deductions that move the counterexample search forward.

## Sources checked

The sweep covered the localized Weil/screw literature, spectral triples,
finite Guinand--Weil dictionaries, de Bruijn--Newman total positivity,
Stieltjes moment/Weyl/Padé theory, extremal Poisson kernels, zero verification,
Robin criteria, and the repository's newest audit results.

The most important new primary sources were:

```text
2606.09096  Suzuki        localized Weil form via screw function
2607.02828  Groskin       exact finite GW dictionary and tail order
2605.20224  Groskin       high-precision truncated Weil experiments
2602.20313v2 Michalowski  certified PF5 failure, repaired July revision
2602.06199  Chirre/Molero extremal Poisson GW bounds
2511.22755  Connes et al. zeta spectral triples
```

## Main theorem synthesis

### 1. Monotone localized support

Suzuki proves that the lowest localized eigenvalue is continuous and that its
infimum is attained from the smooth compactly supported core. Since the smooth
test classes are nested under support enlargement, the lowest eigenvalue is
nonincreasing. Under false RH its sign must therefore pass from a positive ray,
through a possibly degenerate zero plateau, to a persistent negative ray.

Artifact: `L-14201`.

### 2. Countable dyadic FIR equivalence

Suzuki's screw kernel is continuous and RH is equivalent to positivity on every
finite configuration. Approximate any strict negative configuration by one
arithmetic progression on a dyadic grid, repair the coefficient sum exactly,
and zero-fill the unused nodes. The AP increment identity turns the result into
one real Toeplitz matrix.

Therefore

```text
RH iff H_n(2^-k) is PSD for every finite n,k.
```

Real dyadic vectors suffice. A coarse witness embeds exactly into every dyadic
refinement by duplicating increment coordinates.

Artifact: `T-14201`.

This gives the screw route its first explicit countable, nested,
existentially-complete proof search.

### 3. Localized finite-element completeness

Suzuki's identity `Q=<G Dv,Dv>` on `H_0^1` makes the form continuous under
standard finite-element approximation. Uniform nested hat spaces therefore have
Ritz minima converging to the true localized ground state. If RH is false, one
finite rational support/mesh/vector is negative. Its prime side uses only
`q<=exp(2a)`.

Artifact: `T-14202`.

### 4. Exact synthetic refinement regression

X-14201 uses the synthetic kernel `Psi(t)=-t^2`. At spacing `1/16`, the
zero-sum vector supported at nodes `0` and `5/16` has exact value

```text
-25/128.
```

Refining to spacing `1/32` by zero insertion preserves the value exactly. The
standard-library checker verifies screw/Toeplitz equality, exact refinement,
and fail-closed schema gates. Seven tests pass locally.

## Critical literature boundary

Groskin's July paper proves an exact dictionary for the specific CvS/CCM finite
spaces and a sharp tail budget. It does not prove those spaces form a dense core
of all admissible Weil tests. The repository should therefore distinguish:

```text
exact finite certificate
from
complete finite hierarchy.
```

T-14202 supplies one complete hierarchy. The major spectral-triple research
question is now to prove that the attractive CvS/CCM spaces converge to it in
form or Mosco sense.

## Other immediate insights

- Positive-anchor direct-xi Schur intervals are classical truncated Stieltjes
  Weyl/Gauss--Radau intervals. Continued fractions and extremal atomic measures
  should replace explicit inverse-heavy checkers.
- Chirre--Molero's extremal Poisson minorants can sharpen certified zero-bin
  deflation while retaining finite prime support.
- arXiv:2602.20313v2 certifies PF5 failure but withdrew an unsound global
  threshold theorem from v1. Independent reproduction should target only the
  surviving finite determinant.
- The spectral-triple papers explicitly identify convergence as the missing
  theorem; further matching digits do not address it.

## Artifacts

- `L-14201` — localized support monotonicity and onset.
- `T-14201` — dyadic FIR/Toeplitz equivalence and refinement tree.
- `T-14202` — localized finite-element completeness.
- `M-14201` — literature-calibrated project strategy.
- `X-14201` — exact synthetic checker and seven tests.
- `literature/2026-07-29-latest-rh-counterexample-sweep.md` — detailed map.
- integration handoff and follow-up issues.

## Truth status

No Riemann-Hypothesis counterexample was found. No `Z-####` is allocated. The
new results are theorem syntheses conditional on independent review of the
imported source normalizations.

## Highest-value next computations

1. Directed `Psi` table for a small dyadic FIR frontier.
2. Small rational-support hat-function localized matrix with two independent
   interval implementations.
3. Exact Gauss--Radau/continued-fraction replay of the existing positive-anchor
   direct-xi tables.
4. Independent Arb replay of the PF5 determinant.
5. Form-density/Mosco comparison between the hat core and CvS/CCM source spaces.
