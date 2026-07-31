# M-15403 — Certified-zero notch scheduling for the one-window prime criterion

Claim ID: `M-15403`  
Title: Spend compact support where it most reduces the RH-valid terminal-window moat  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: `T-15403`, `L-15406`  
Scope: proof-producing optimization of one-window counterexample searches

## Input

- one explicit zero-free smooth base window from `L-15405`;
- certified critical-line zero balls `(gamma_j^-,gamma_j^+)` with multiplicities;
- an explicit shell-count majorant for all unlisted zeros;
- a support budget `R_max`;
- a directed profile evaluator and terminal-prime producer.

## Candidate notch

For one zero ball, choose a rational design center `tilde gamma_j` and a directed
length enclosure for

```text
r_j = 2 pi / tilde gamma_j.
```

Compute the exact worst-case attenuation

```text
alpha_j
 = sup_(gamma in ball_j)
   |(1-exp(-i r_j gamma))/(i r_j gamma)|^2.
```

The simple closed bound in `L-15406` is admissible; direct interval
trigonometry may be sharper.

## Gain and cost

Let `w_j` be the current certified upper contribution of that zero ball to the
RH-valid bound. The gain is

```text
gain_j = w_j (1-alpha_j),
```

and the support cost is

```text
cost_j = r_j.
```

Rank initially by `gain_j/cost_j`, but recompute gains after every accepted
notch because transform factors multiply. The exact selection problem is a
finite knapsack or submodular scheduling problem with directed objective bounds.

## Search modes

### Bound-minimization mode

Select notches to minimize the explicit RH-valid constant `B_*`. Then evaluate
the single terminal prime statistic and compare its directed interval with the
reduced moat.

### Collision mode

At a nominated high-height zero ball, install an especially sharp notch there.
An actual on-line zero is suppressed, whereas a hypothetical horizontal
displacement survives with response approximately `(delta/gamma)^2` before the
cofinal exponential factor.

### Background-whitening mode

Notch the handful of low zeros dominating the base transform. The remaining
RH-valid zero sum becomes small and high-frequency, making terminal support
scans less dominated by known oscillations.

## Fail-closed rules

- Never use the difference of two cumulative zero-count upper bounds as a shell
  count without a separate proof.
- Never replace a zero ball by its midpoint in the final attenuation.
- Preserve multiplicity.
- Include the notch support in the terminal annulus width exactly.
- Recompute the transform tail and trivial-zero bound after every profile
  change.
- A smaller moat is not a counterexample; only a strict directed violation is.
- A notch centered at a known zero cannot cancel an off-line point in the open
  right half-plane, but its small displacement response must still be included
  quantitatively.

## Production ladder

1. Base dyadic window with no notch.
2. Notch the first one, three, eight, and sixteen rigorously isolated zeros.
3. Compare support cost and computed `B_*` after each rung.
4. Add targeted high-height notches only when they materially reduce an active
   candidate's uncertainty or known-zero background.
5. Freeze the best profile and run the complete terminal-prime annulus at two
   directed precisions.
6. Independently reproduce both the zero-ball attenuation and prime manifest.

## Wider role

This scheduler converts the repository's large certified-zero infrastructure
into an exact prime-side filter. It is the phase-aware analogue of zero
deflation, but it keeps the final witness as one von Mangoldt window rather than
a direct-xi value or logarithmic derivative.
