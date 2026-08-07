# Critical-correlation completion attempt

Date: 2026-08-07  
Agent: `gpt56-pro-09-o`  
Branch: `agent/gpt56-pro-09-o/230-repository-wide-rh-proof-candidate`  
Status: **GAP/BLOCKED at one scalar Möbius estimate; RH is not claimed proved**

## Objective

Complete `L-23002`, remove the last gap in `T-23001`, and promote PR #229 to a
full proposed proof of RH.

## Routes attacked

I attacked the same gate in all four repository coordinates:

1. dyadic prime-polygon transport minus Bregman curvature;
2. signed balanced-semiprime common-cell energy;
3. prime-only vertical Hardy energy;
4. analytic-totient local-to-Bohr second moment.

I also tested two proposed positivity shortcuts:

- a compact positive-Hankel adjoint for the stop-loss row;
- a uniform critical Farey-cluster operator contraction.

Both shortcuts fail exactly.

## Exact new result

For the completed analytic-totient packet, the first positive critical Farey
cell is

\[
 B_{D,1}
 =\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
 [M(D)-M(2D/3)].
\]

This is `L-23003`.

Consequently, square-root control of that one cell is already equivalent to RH:

\[
 |B_{D,1}|\ll_\varepsilon D^{1/2+\varepsilon}
 \quad\Longleftrightarrow\quad
 M(D)=O_\varepsilon(D^{1/2+\varepsilon})
 \quad\Longleftrightarrow\quad RH.
\]

The fixed-ratio implication follows by a geometric telescoping sum.  This is
`T-23002`.

## Exact refutations incorporated

### Compact stop-loss adjoint

`R-23001` proves that the exact compact solution of

\[
 \mathscr L^*f=-(T-y)_+
\]

is negative near its terminal endpoint.  Its Hankel kernel cannot be positive.

### Uniform cluster operator

PR #231 proves that every fixed positive critical cell has an operator row of
norm at least `c_k sqrt(D)`.  Deleting finitely many cells does not help.
`R-23002` imports that refutation and shows why it is arithmetically relevant:
the first row is the Mertens increment above, not an artificial worst-case
vector.

## What the latest literature changes

Two recent primary-source developments were checked.

- Verjovsky, arXiv:2607.25002, obtains critical local-moment formulations of RH
  and explicitly recovers the Mertens value from local moments.  This supports
  the decoder but does not prove the required moment bound.
- Dong--Robles--Zeindler, arXiv:2601.00292, improve bilinear Kloosterman-fraction
  estimates.  Their balanced saving is far smaller than the full critical power
  needed here and does not close the coherent first-cell mode.

Thus no located literature theorem supplies the missing square-root Möbius
cancellation.

## Strongest surviving scalar theorem

The exact completed packet is

\[
 \mathscr C_D(x)
 =1+S_D(x)+\frac{M_D}{3}+x^2R_D
 =2E^{\rm AN}(x)
 \qquad(0\le x\le D).
\]

The correct scalar target is

\[
\boxed{
 \int_{D/2}^{D}|\mathscr C_D(x)|^2dx
 \ll_\varepsilon
 D^{1+\varepsilon}(1+\mathcal B_D),
}
\]

where the exact Bohr/Jordan energy satisfies `mathcal B_D<<D`.

This would imply

\[
 \int_{D/2}^{D}|E^{\rm AN}(x)|^2dx
 \ll_\varepsilon D^{2+\varepsilon},
\]

and hence RH through `T-9506`.

A valid proof must preserve together:

1. the actual signs `mu(d)`;
2. the divisor coordinates `U_q(D),V_q(D)`;
3. the endpoint channels `M_D/3` and `x^2R_D`;
4. the common signed critical-cell contraction.

## Why I did not promote a full proof

The first-cell identity proves that completing `L-23002` is not a routine
functional-analytic estimate left after the arithmetic work.  It is already a
square-root Mertens theorem in exact finite coordinates.

I found no valid derivation of that cancellation from the available Selberg,
Kloosterman, Brownian, operator, or local-moment inputs.  Promoting the PR by
writing the scalar estimate as if it had been proved would merely rename RH as a
lemma.

## Review handoff

Review in this order:

1. `L-23003-first-farey-cell-mertens-decoder.md`;
2. `T-23002-critical-cell-mertens-rh-equivalence.md`;
3. `R-23002-generic-critical-cluster-operator-closure-fails.md`;
4. PR #231 `R-22802` and `L-22801`;
5. the original `L-23002` and `T-23001` proof spine.

The decisive research question is now:

> Can the endpoint-completed Möbius packet satisfy the scalar local-to-Bohr
> estimate through a sign-preserving Selberg/Ramanujan identity, despite the
> exact Mertens mode in its first critical cell?

Until that question is answered, RH remains unproved.
