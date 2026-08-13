# L-91421 — The corrected factor-54 route is exact four-state propagation followed by one boundary projection

Claim ID: `L-91421`  
Status: **EXACT ARCHITECTURAL REDUCTION; ONE RESET-BOUNDARY PROJECTION THEOREM OPEN**  
Created: 2026-08-12  
Depends on: `R-91420`, `L-91320`–`L-91328`, `T-91101`  
RH status: **unproved**

## 1. Why projection must be deferred

`R-91420` shows that the positive two-state completion \(N_p\) preserves the SHARP row for one prime but not under a raw product \(N_qN_p\). The compositionally exact object is instead the positive four-state parity vector

\[
z=(X_+,X_-,Y_+,Y_-)^{\mathsf T}
\]

with diagonal rough action

\[
z\mapsto\widetilde D_4(A,B)z
=\operatorname{diag}(A,A,B,B)z.
\tag{L-91421.1}
\]

The signed physical observation is

\[
(L,R)^{\mathsf T}=J_4z,
\tag{L-91421.2}
\]

and the identity

\[
J_4\widetilde D_4(A,B)=M(A,B)J_4
\tag{L-91421.3}
\]

holds under arbitrary composition.

Therefore the parity state must be propagated exactly through the full rough packet and projected only at the reset boundary.

## 2. One-prime-per-reset simplification

`L-91317` assigns every rough source atom to its unique least prime and sends the child below \(c_0X\). `L-91328` proves a uniform positive forcing margin after that one new least prime.

Consequently one generation has the exact order

```text
finite block through 61
-> one new least rough prime in the four-state representation
-> factor-54 contraction
-> one boundary projection
-> next generation.
```

No theorem about products of completed two-state matrices is needed.

## 3. Corrected reset-boundary theorem

The remaining theorem can be stated without any hidden multiprime tensorization.

> **Four-State Reset Projection (`FSRP_X`).**  
> For every sufficiently large endpoint \(X\), after the finite block through \(61\) and one least-prime transition, construct a positive linear map from the four-state endpoint/carry packet into:
>
> 1. nonnegative outer endpoint rows already covered by the factor-54 packing;
> 2. one nonnegative contracted \((L,R)\) child state at \(K_X\le c_0X+O(1)\);
> 3. the finite positive boundary/collar packets;
>
> such that:
>
> \[
> \text{native SHARP mass used}
> =
> \text{outer SHARP mass}
> +
> \text{child SHARP mass},
> \tag{L-91421.4}
> \]
>
> every ordinary and radix-four physical column is spent at most once, and
>
> \[
> \mathfrak L_X\le\mathfrak L_{K_X}+O(1).
> \tag{L-91421.5}
> \]

The map must be defined before evaluating the target score. It may use:

- the no-upward balanced Hall transport of `L-91320`;
- the positive interval/butterfly or exact component-row lifts of `L-91321/L-91322`;
- the common Hilbert defect and linear four-state ledger of `L-91326/L-91327`;
- the \(P_{61}\) one-prime margin of `L-91328`;
- the single global target disintegration and finite collars already resident.

## 4. Why `FSRP_X` would complete the route

`T-91101` already proves that a coefficient-one reset with contraction \(K_X\le c_0X+O(1)\) and bounded debt yields

\[
\mathfrak L_X=O(\log X)=o(\log^2X)
\]

and therefore RH.

Thus

\[
\boxed{
(\forall X\gg1)\;FSRP_X
\Longrightarrow \mathrm{RH}.
}
\tag{L-91421.6}
\]

This is not yet a complete proof. It is the corrected single theorem that a complete proof must supply after the compositional firewall.

## 5. Audit focus

A proposed proof of `FSRP_X` must demonstrate, rather than assert:

1. a positive decomposition of the actual four parity coordinates;
2. one-use target capacity after colors are forgotten;
3. exact SHARP accounting at the boundary projection;
4. radix-four detail feasibility without subtracting ordinary inequalities;
5. coefficient-one recursion over generations.

```text
four-state propagation                 EXACT
one least prime per generation         EXACT SUPPORT LOGIC
finite window and terminal collars     AVAILABLE
reset-boundary positive projection     OPEN
bounded coefficient-one recurrence     OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVED
```
