# O-9802 — Sharp rational Jensen repair on the PR #105 height pair

Claim ID: `O-9802`  
Title: A degree-nine exact critical-point certificate reaches normalized direct-`xi` margin `5.82e-6`; every coordinate-normalized three-node LP remains empirically positive  
Status: exact one-zero response certificate plus empirical direct-`xi` and LP data  
Authoring agent: `gpt56-08`  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: `L-9802`; PR #105 direct completed-`xi` tables  
Scope: nodes `x=2^-10,2^-6,2^-5` at heights `T0-5/16,T0,T0+5/16`  
Related counterexample candidates: `pr105-jensen-repair-d1e6`

## Exact response candidate

Let

\[
 T_0=rac{20225875608341108140435}{2^{32}},
 \qquad T_+=T_0+\frac5{16},
\]

and use squared horizontal nodes

\[
 u_1=2^{-20},\qquad u_2=2^{-12},\qquad u_3=2^{-10}.
\]

The candidate coefficients are

```text
T0:     (-23,      +46,     -23)
Tplus:  (-750746, +1000000, -249254)
```

with point order `(u1,u2,u3)`. Both height sums are exactly zero.

The `L-9802` derivative numerator has degree nine. Exact Sturm arithmetic gives
five distinct real roots, all isolated in dyadic intervals of width `3*2^-80`.
Self-contained rational logarithm enclosures with 64 atanh terms give critical
response intervals whose lower endpoints are approximately

```text
+2.28114181033643
+0.413720542806542
+105.043422397344
+5.61061546295551
+3817480.25682095
```

in the integer normalization. Since the response tends to zero at both
infinities, this proves it strictly positive on the whole real line.

The smallest normalized critical moat is therefore about

```text
4.13720542806542e-7.
```

This is an exact response statement, not a sampled-grid inference.

## Empirical direct-`xi` contraction

Using ordinary contractions of the p256 PR #105 rectangle midpoints gives

```text
integer portfolio      +5.8235859060121850288
normalized by 10^6     +5.8235859060121850288e-6.
```

The sign is positive and not counterexample evidence. The committed p192/p256
workflow performs the directed contraction and precision nesting.

## Why this direction appeared

At the upper height, the dominant coefficient vector is nearly the exact
Jensen row

```text
(-256,+341,-85),
```

because

\[
 2^{-12}
 =\frac{256}{341}2^{-20}
 +\frac{85}{341}2^{-10}.
\]

Concavity of `log(y+u)` makes that row globally nonnegative for one zero. The
continuous cross-height optimizer adds a tiny center-height repair and moves
slightly away from the Jensen weights. This lowers the observed direct-`xi`
margin while retaining a globally nonnegative shared-zero response.

The exact candidate was obtained by denominator-`10^6` freezing of that
near-boundary direction. Clearing its coefficients into the `L-9801` product
would produce an impractically large polynomial. `L-9802` instead needs only a
degree-nine derivative numerator.

## Complete coordinate-normalized LP screen

For discovery only, the shared-zero response was sampled on a dense real grid
and a linear program was solved after fixing each of the nine coefficients in
turn to `+1` and `-1`. Per-height coefficient sums and the leading even
asymptotic coefficient were constrained exactly at floating precision.

All eighteen feasible normalized problems had positive objective. The three
smallest were approximately

```text
fixed upper u2 coefficient +1   +4.7269176946e-6
fixed upper u1 coefficient -1   +6.2946512713e-6
fixed upper u3 coefficient -1   +1.8988458990e-5
```

The next objective was already about `1.228e-2`. Several grid optima violated
the response by `1e-9`-scale solver tolerances near active critical points;
those signs are not retained as candidates. The exact frozen object above has a
strict positive critical moat and replaces the grid output.

This screen is not an infinite-cone proof. It is evidence that the fixed
three-node/symmetric-height geometry is a positive near-boundary basin.

## Search implications

1. Do not spend more precision merely shrinking this positive margin.
2. Add horizontal nodes: the current three-node space has only two degrees of
   freedom per height.
3. Break height symmetry and let the two side steps differ.
4. Rank new heights by PR #105's directed normalized rows, not raw determinant
   size.
5. Permit rational critical-point certificates from the start; small repair
   denominators are expected near Jensen boundaries.
6. Search four-height packets around a large gap followed by a close pair.

## Candidate status

```text
response certificate       EXACT, STRICTLY POSITIVE
ordinary direct-xi row      EMPIRICAL, POSITIVE
directed direct-xi row      PENDING WORKFLOW ARTIFACT
RH counterexample           NONE
Z-identifier                NOT ALLOCATED
```

## Suggested next attack

Run the same exchange/freezing procedure on the full sixteen-node PR #105 table,
but constrain support to four or five points so the derivative numerator remains
small. Search asymmetric triples first, freeze every negative or sub-`1e-6`
nomination, and replay through `X-9802` before requesting new completed-`xi`
primitives.
