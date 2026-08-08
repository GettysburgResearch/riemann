# T-28301 — Radix-two boundary-jet Pascal renewal proposal for RH

Claim ID: `T-28301`  
Title: Exact eta-comb jet contraction plus a finite Pascal/Peano boundary renewal would give the sharp carry ramp and RH  
Status: **FULL CONDITIONAL RH PROPOSAL — ONE BOUNDARY-RENEWAL THEOREM OPEN**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-08  
Scope: global composition; **RH is not claimed proved**

## 1. Why this proposal is needed

The recent central-cascade attacks correctly discovered a strict continuum mass
factor `1-log 2`, but two proposed closures fail:

1. later continuum iterates are not pointwise monotone once the compact-boundary
   distributions are retained;
2. fixed source-independent Abel orders do not preserve producer positivity.

`R-28301` gives exact witnesses.  The replacement must therefore retain the
complete boundary source and contract it in a norm which sees adjacent
logarithmic transport, rather than delete the boundary or increase a fixed Abel
order.

## 2. Exact current-scale reserve

`L-28301` identifies the complete logarithmic boundary kernel

\[
 \mathfrak b
 =\sum_{k\ge1}
 \left[
 {1\over2k}\delta_{\log(2k)}
 -{1\over2k+1}\delta_{\log(2k+1)}
 \right]
 \tag{T-28301.1}
\]

and decomposes it into:

```text
positive residual mass             rho=1-log 2;
adjacent logarithmic dipoles        cost c<rho.
```

Thus

\[
 \theta_*:=\rho+\mathfrak c<1.
 \tag{T-28301.2}
\]

For the finite jet norm

\[
 \mathcal J_M(F)=\sum_{m=0}^{M}\|F^{(m)}\|_\infty,
\]

one has exactly

\[
 \boxed{
 \mathcal J_M(\mathfrak b*F)
 \le
 \theta_*\mathcal J_M(F)
 +\mathfrak c\|F^{(M+1)}\|_\infty.
 }
 \tag{T-28301.3}
\]

This is a genuine strict current-scale reserve.  Only one top derivative is
exported.

## 3. Boundary-Jet Pascal Renewal (`BJPR`)

The sole new theorem is the following finite production statement.

> **BJPR.** There exist one fixed order `M`, one fixed finite endpoint-state
> space, constants `A,B,C`, and `Theta<1`, such that at every finite endpoint
> `X` the complete stopped central source admits a source-bound decomposition
> into:
>
> 1. a smooth `M`-jet state governed by (T-28301.3);
> 2. every delta jet generated at the compact endpoint;
> 3. every logarithmic eta dipole in (T-28301.1);
> 4. a finite family of exact balanced Pascal commutators and positive Peano
>    spline rows;
> 5. strict lower-scale destinations and a finite bottom/collar state;
>
> for which the optimized complete boundary debt obeys
>
> \[
> \boxed{
> \mathfrak D_{a+1}(X)
> \le
> \Theta\,\mathfrak D_a(X)
> +C(1+a)^A\log^B(2X),
> \qquad \Theta<1.
> }
> \tag{T-28301.4}
> \]
>
> Every repeated arithmetic destination must be recombined before the norm.

A valid certificate must include the exact source coefficient, every odd node,
the bottom logarithmic charge, all endpoint and first-crossing rows, and every
Pascal-cycle coordinate.  No floating spectral radius or generic ambient
operator norm is acceptable.

## 4. Proposed construction of the renewal state

The production attack is finite and radix-two.

### 4.1 Smooth bank

Use the first `M` logarithmic derivatives of the current source.  Equation
(T-28301.3) gives the strict bulk factor `theta_*`; the `(M+1)`-st derivative is
not estimated in place.

### 4.2 Positive Peano export

Apply finite Euler transformation to the exported derivative.  Every finite
difference is represented by a nonnegative one-variable cardinal B-spline, and
its support begins at the next dyadic boundary.  The corresponding arithmetic
rows are sent to exact balanced Pascal commutators.

### 4.3 Eta dipole adapter

The continuum dipole

\[
 \delta_{\log(2k)}-\delta_{\log(2k+1)}
\]

is paired with the adjacent-tree current

\[
 E_{2k}=T_{2k+1}-T_{2k}
\]

from the exact dyadic divergence normal form.  The adapter must preserve its
coefficient `1/(2k+1)` and the complete bottom recursion of `E_(2k)`.

### 4.4 Radix-two moment bank

A stable finite moment recurrence is used only to organize the boundary jets.
It may use the recent radix-`b` moment expansions of the zeta function, whose
inverse Mellin kernels are compact beta splines and whose remainders converge
geometrically on compact spectral sets.  This analytic expansion does **not**
by itself prove any zero-free statement; every factor which could vanish at a
zeta zero must remain in the physical/source ledger.

### 4.5 Finite collar

All rows below the fixed production threshold, all Mersenne/reciprocal knots,
and all source mutations are retained as one finite collar.  The collar is
allowed polynomial or polylogarithmic forcing, but no same-scale homogeneous
coefficient may exhaust `1-theta_*`.

## 5. Elementary consumer

PR #272 supplies the exact dyadic divergence/commutator normal form and the
Cycle-Debt consumer.  Under BJPR, iteration of (T-28301.4) for `O(log X)` support
halvings gives

\[
 \mathfrak D_a(X)=O(\log^{A'}(2X)).
 \tag{T-28301.5}
\]

The exact balanced entropy adapter then gives

\[
 \boxed{
 \sum_{p^r\le X}{\Lambda(p^r)\over\sqrt{p^r}}
 \log{X\over p^r}
 \ge4\sqrt X-O(\log^{A''}(2X)).
 }
 \tag{T-28301.6}
\]

At `X=N^2`, the exact square-screw formula yields a subpolynomial upper envelope
for the zeta screw function.  Critical square sampling and the one-sided Landau
argument exclude every zero to the right of `1/2`; functional-equation symmetry
gives RH.

## 6. Independent physical consumer

The same BJPR state can be inserted before the pure-carry zeta cancellation in
the parity-paired physical source of PRs #263/#269.  The smooth transverse
sector is controlled by the factor-five carry reserve, while the eta dipoles and
endpoint jets remain in the independent-frequency boundary block.  A strict
BJPR recurrence therefore also supplies the boundary-commutator theorem needed
by that route.

This second consumer is a consistency test, not an additional assumption.
The elementary Cycle-Debt consumer is the preferred minimal composition.

## 7. Relation to the current literature

Recent radix-`b` moment formulas express zeta as finite combinations of
geometrically convergent series and provide compact beta-spline inverse Mellin
kernels.  They supply a natural stable coordinate system for the finite jet
bank.  The new arithmetic content required here is the exact mapping of those
spline/jet terms into the Pascal boundary-current space with reserve; the
analytic continuation formula alone does not supply BJPR.

## 8. Review firewall

Reject a proposed BJPR certificate upon any:

- omitted endpoint delta jet;
- use of the false all-stage pointwise monotonicity;
- reuse of fixed third- or fourth-Abel positivity;
- total variation of the eta comb before even/odd pairing;
- missing odd node, bottom charge, or adjacent-tree recursion;
- unsigned estimate before Pascal siblings recombine;
- factor that cancels a hypothetical off-line zeta zero;
- current-scale collar relabeled as lower scale;
- finite numerical spectrum promoted to a uniform recurrence;
- failure of the fixed-ratio Mertens mutation.

## 9. Exact status

```text
eta boundary comb and symbol                  proposed exact
positive mass plus dipole decomposition       proposed exact
strict finite-jet contraction theta_*<1       proposed exact
third-Abel/all-stage monotonicity closures     refuted
finite Pascal/Peano boundary renewal BJPR      OPEN / RH-BEARING
BJPR -> Cycle Debt -> sharp prime ramp -> RH   COMPLETE CONDITIONAL
Riemann Hypothesis                             UNPROVED
```

This is a full conditional proposal with one sharply typed finite recurrence.
It is not an unconditional proof of RH until BJPR is constructed and reviewed.
