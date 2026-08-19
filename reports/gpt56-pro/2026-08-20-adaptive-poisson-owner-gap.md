# Adaptive Poisson-owner gap after the native SHARP audit

## Live graph

The repository has converged to one conclusion-facing scalar:

\[
h(x)=H_{67}^{\rm sharp}(x).
\]

PR #647 proves its exact reciprocal-zeta Mellin transform and certifies
`h(x)>0` for every real `x<100,000,001`. PRs #652--#654 close or remove the
compact Hall, RN endpoint, causal/Euler, calibration and fixed-row consumer
interfaces. The binding open statement is now either pointwise positivity of
the unbounded tail or the weaker subpower logarithmic negative-mass estimate
of PR #653.

PR #655 then proves that every fixed logarithmic owner order fails after the
duplicated 67 factor and that the untwisted owner variance vanishes on the
principal parity sector.

## New mechanism

The Cauchy density

\[
P_\tau(\gamma)=\tau/[\pi(\tau^2+\gamma^2)]
\]

has characteristic function `exp(-tau |u|)`. Averaging the phase-owner square
therefore converts every owner phase `q^(i gamma)` into `q^(-tau)` and gives

\[
\overline V_\tau(n)
\ge2(1-2^{-\tau})|a(n)|^2
\]

for every nonzero native coefficient, including the exceptional
`v_67(n)=2` sector.

Choose `tau_x=1/loglog x`. The gap loses only `loglog x`, while evaluation on
the left strip costs

\[
x^{\tau_x}=\exp(\log x/\log\log x)=x^{o(1)}.
\]

This exactly matches the slack allowed by the negative-mass Mellin theorem.
The remaining estimate `APOC99710` is one source-conditioned martingale
Carleson embedding for the adaptive Poisson square function.

## Continuous-order stress test

Summing every fixed logarithmic order with exponential weights produces

\[
c_u=\beta*\operatorname{id}^u.
\]

It is coefficientwise nonnegative exactly when

\[
u\ge\log2/\log67.
\]

This is a genuine positive all-order completion and a strong check that the
owner hierarchy contains hidden positivity. It is not the conclusion: its
Mellin transform contains `zeta(z-u)` and hence a positive-real pole at
`s=u+1/2`. Distributional pole subtraction introduces negative activation
atoms. The packet freezes this firewall explicitly.

## Current closure chain

```text
exact native SHARP scalar and finite 1e8 theorem
 -> adaptive Cauchy-Poisson phase square
 -> exact owner spectral gap
 -> APOC99710 source-tent Carleson packing
 -> subpower logarithmic negative mass of h
 -> zero-safe Mellin/Landau
 -> RH.
```

## Honest boundary

```text
native source/operator firewall                 closed by PR #652
scalar analytic consumer                        closed by PRs #647/#653
fixed-order owner positivity                    refuted by PR #655
Cauchy-Poisson owner coercivity                  proved here
adaptive subpower strip tradeoff                 proved here
continuous all-order positive completion         proved here
real-order direct Landau shortcut                refuted here
APOC99710 source-Carleson estimate               open / RH-bearing
Riemann Hypothesis                               unproved
```
