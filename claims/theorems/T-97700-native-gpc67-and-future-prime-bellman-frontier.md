# T-97700 — Native `GPC67` and the corrected future-prime Bellman closure frontier

Claim ID: `T-97700`  
Status: **UNCONDITIONAL CORRECTION + EXACT REDUCTION; EXPLICIT BARRIER OPEN**  
Created: 2026-08-18  
Depends on: PRs #576, #584, #586; `R-97700`, `L-97700`, `L-97701`; `L-97604` Mellin-Landau consumer  
RH status: **unproved**

## 1. Canonical native scalar

Let

\[
F_{61}(Y)=
\sum_{d\mid P_{61}}{\mu(d)\over\sqrt d}Q_*(Y/d)
\]

be the complete `P_61` annular `5:3` base.  Unique decomposition of a squarefree
index into its `P_61` part and its rough part gives the exact source identity

\[
\boxed{
R_X
=
\sum_{\substack{m\ \mathrm{squarefree}\\P^-(m)\ge67}}
{\mu(m)\over\sqrt m}F_{61}(X/m).
}
\tag{T-97700.1}
\]

This is the scalar consumed by `L-97604`; no recombined surrogate is permitted.

Define the canonical arithmetic target:

> **Global Parity Cancellation at 67 (`GPC67`).**  There exists `X_0` such that
> for every real `X>=X_0`, the native scalar in (T-97700.1) is nonnegative.

By `L-97604`,

\[
\boxed{\mathrm{GPC67}\Longrightarrow\mathrm{RH}.}
\tag{T-97700.2}
\]

The implication uses the exact reciprocal-zeta Mellin transform, the zero-safe
finite numerator, Landau's theorem, and functional-equation symmetry.

## 2. Corrected status of the adaptive route

`R-97700` proves that `LAPBR67` from PR #578 is false as quantified.  The failure
occurs at moving admissible states with least allowed rough prime immediately
above `(log X)^(1/4)`: the small-prime harmonic mass is empty, the adaptive depth
freezes at eight, and the seventh rough layer eventually dominates negatively.

Thus

```text
small-prime critical cube          PROVED / RETAINED
LAPBR67                             REFUTED
LAPBR67 -> RH                       logically irrelevant after refutation
```

No replacement theorem may silently retain the same fixed-depth behavior after
crossing the moving cutoff.

## 3. A new safe local edge

`L-97700` proves the source-faithful inequality

\[
F_{61}(Y)-p^{-1/2}F_{61}(Y/p)
\ge
\left({1\over42}-{1\over8\sqrt p}\right)M_{61}(Y)>0
\]

for every prime `p>=67` and `Y>=67p`.

This is a valid local peeling rule and may be used inside a future-prime
barrier.  It does not by itself compose through arbitrary rough depth.

## 4. The exact Bellman form of `CPSL67`

At every finite owner state `v`, define the oriented Lorenz hinge deficit
`D_v^+(lambda)` as in `L-97701`.  Then completed-parity scalar common-source
feasibility at `v` is exactly

\[
D_v^+(\lambda)\ge0
\qquad\text{for every real }\lambda.
\tag{T-97700.3}
\]

The unique least-prime recursion gives

\[
(I-R^2)D^+=g^+,
\qquad
g^+=d^+ + R d^-.
\tag{T-97700.4}
\]

Hence the exact parity-restored transition is the positive two-prime operator
`R^2`, not a source-blind reserve.

Define **Future-Prime Hinge Barrier 67 (`FPHB67`)** to mean that there is an
explicit source-computable function `B_v(lambda)` such that, for every finite
state and every real hinge parameter,

\[
B_v(\lambda)\ge0,
\tag{T-97700.5}
\]

and

\[
\boxed{
B_v(\lambda)
\le
g_v^+(\lambda)+(R^2B)_v(\lambda).
}
\tag{T-97700.6}
\]

The barrier is required to be defined without the unknown completed deficit
`D^+` itself; using `B=D^+` is the tautological existence proof and is not an
unconditional producer.

By backward induction,

\[
\boxed{
\mathrm{FPHB67}
\Longrightarrow
\mathrm{CPSL67}
\Longrightarrow
\mathrm{GPC67}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-97700.7}
\]

Abstract existence of a nonnegative barrier is equivalent to `CPSL67`, because
`B=D^+` satisfies equality.  The conclusion-producing work is therefore the
construction of an **explicit lower-dimensional source barrier**.

## 5. Minimal estimate to finish this architecture

The remaining theorem can now be stated without transport ambiguity:

> **Explicit future-prime Bellman theorem.**  Construct `B_v(lambda)` from the
> local `P_61` owner data, the future-prime quotient profile, and finitely many
> source moments, and prove (T-97700.5)--(T-97700.6) uniformly at every real
> endpoint and every hinge breakpoint.

Because each finite `D^+` is piecewise affine in `lambda`, it is enough at a
fixed endpoint to control the finite Lorenz breakpoints and the affine tails.
The hard quantifier is uniformity over all endpoints/states.

Expanding `R^2` makes the remaining interaction explicitly bilinear:

\[
(R^2B)_v
=
\sum_{p<q\ \mathrm{active}}
{1\over\sqrt{pq}}\,B_{v_{p,q}},
\tag{T-97700.8}
\]

with the exact least-prime activation constraints.  This is the native place to
use sparsity, short remaining histories, Type-I/Type-II decomposition, or the
separated-coprime machinery of the Q4 lane.  Any such estimate must be proved
before absolute values erase the Möbius/parity correlation.

## 6. Current exact frontier

```text
repaired P61 annular bias                     PROVED
native one-prime P61 edge                     PROVED
completed rough owner ledger                  PROVED
finite scalar Lorenz primal/dual              PROVED
Lorenz hinge Bellman equations                PROVED
small-prime adaptive cube                     PROVED
LAPBR67                                       REFUTED
GPC67                                         OPEN / RH-BEARING
explicit FPHB67 barrier                       OPEN / RH-BEARING
FPHB67 -> CPSL67 -> GPC67 -> RH               PROVED CONDITIONAL
Riemann Hypothesis                            UNPROVED
```

This theorem deliberately does not relabel the open Bellman producer as a proof.
It replaces a false large-prime sign target by a source-exact two-prime Bellman
interface on the same scalar the Mellin consumer actually observes.
