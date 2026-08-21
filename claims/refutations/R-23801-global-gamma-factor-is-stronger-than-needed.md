# R-23801 — Global Gamma–carry positivity is stronger than the finite proof gate

Claim ID: `R-23801`  
Title: The global Möbius–Riesz density is a canonical producer, not the minimal carry theorem  
Status: **PROVED SCOPE CORRECTION**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-07  
Issue: #238  
Dependencies: `L-23805`, `L-23807`, upper-envelope Landau transfer  
Scope: prevents overclaiming the final hinge

## 1. Global GCF contains the strip obstruction

The canonical quotient

\[
 A(s)={(s+1)(s+2)
  \over8s(s+1/2)^2\zeta(s+1)}
\]

is the Laplace transform of the signed density `a` in `L-23805` on its initial
half-plane. If `a(t)>=0` globally, Landau's one-sign theorem identifies the
abscissa of convergence with a real singularity. Since `A` has no real
singularity in `-1/2<s<0`, its positive density has every exponential moment
strictly below order `1/2`.

The exact packing theorem then yields the sharp prime-ramp lower bound and RH.
Thus global GCF is itself a complete strip-sensitive arithmetic theorem. It may
not be described as a routine probability normalization.

## 2. The finite route is strictly weaker as a statement

`FGCM` in `L-23807` requires only one nonnegative profile on the finite interval
`[0,log(X/2)]` at each endpoint `X`. It permits:

- dependence on `X`;
- convolution slack;
- no positive continuation beyond the finite horizon;
- no exact equality with the signed Möbius inverse;
- quotient-layer recombination before positivity;
- a different certificate family at every scale.

Global GCF, together with its subcritical moments, implies `FGCM` by truncation.
No converse is asserted or needed.

Therefore a counterexample to the canonical density rejects GCF but does not by
itself reject the finite-minorant architecture. A reviewer must distinguish:

```text
GCF producer false
```

from

```text
no FGCM certificate can exist.
```

## 3. Why a finite positive ladder is insufficient

At each fixed `X`, `FGCM` is a finite convex feasibility statement after a
rational cell partition. But RH requires a cofinal theorem with the two mass
losses tending at the exact `X^-1/2+o(1)` rate.

Consequently none of the following proves the proposal:

- a long finite list of positive density layers;
- a long finite LP ladder;
- an empirical fit of the mass deficit;
- finite Hausdorff moment positivity;
- a floating-point nonnegative convolution table.

The cofinal construction is the RH-bearing theorem.

## 4. Status boundary

```text
GCF -> FGCM                        proved conditionally
FGCM -> sharp prime ramp -> RH     proved conditionally
GCF positivity                     open, strong producer
FGCM cofinal minorants              open, minimal stated hinge
RH                                 unproved
```
