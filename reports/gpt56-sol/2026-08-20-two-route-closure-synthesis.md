# Two-route closure synthesis — adaptive critical squaring + activation-free descent

Status: **active research synthesis; RH unproved**

The two strongest current routes are now compatible and meet at one exact interface.

## Route A: activation-free critical descent

PR #676 and successor PR #681 give a globally positive quadratic/centered Bernstein hierarchy, remove activation atoms, and identify the unique critical residue as the factor-67 half-order endpoint term

\[
B_\beta(X)=M_{1/2}(X)-67^{-1/2}M_{1/2}(X/67).
\]

The fully active critical Euler cube is already positive; only partial activation contributes to the remaining debt.

## Route B: adaptive finite Euler squaring

PR #677 proves that a finite completion squares every Euler factor below a cutoff `Z` while preserving every off-line reciprocal-zeta pole. The same adjacent-level argument crosses the final centered-Bernstein prime-harmonic wall whenever

\[
1\le X\le Z^{10/9}.
\]

This is recorded as `L-100180`.

## Exact synthesis

At a fixed physical scale `X`, choose `Z>=X^(9/10)`. Then the small-prime contribution to the final critical owner mass is converted from `1/p` to `1/p^2`; only the short unsquared tail `Z<p<=X` remains at exponent one. Thus the unique half-order activation residue decomposes canonically into

```text
squared small-prime block: strictly subcritical / adjacent-level positive;
large-prime product collar: short multiplicative band / conclusion-bearing.
```

The remaining theorem must be proved on this **local decomposition of the fixed original observable**. One may not use an alternating inverse of the completion and may not diagonalize Landau over an X-dependent multiplier.

## Firewalls retained

- positive finite-completion inversion is impossible;
- an X-dependent family of initial positivity corridors is not a fixed Mellin density;
- source-blind negative-mass desmoothing pays power-sized positive child mass;
- extra completion labels do not automatically gain a `p^-3/2` factor after critical kernel scaling.

## Current target

Prove a blockwise local variation inequality for the fixed activation-free critical observable in which the `p<=X^(9/10)` contribution is evaluated through the exact squared three-state blocks `(1-rS_p)(1+rS_p)=1-r^2S_(p^2)`, and only the tail `X^(9/10)<p<=X` enters the one-sided boundary ledger.

A subpower bound for that tail contribution closes the negative-mass criterion and therefore RH through the already frozen Mellin-Landau consumer.
