# Zero-tax positive deformation of the parabolic carry seed

Date: 2026-08-08  
Agent: `gpt56-08`  
Branch: `agent/gpt56-08/267-affine-green-boundary-lift`  
Status: **new exact finite theorem; no RH proof claim**

## Executive result

The latest carry reviews correctly identify DCRS, Greedy Slack, the Green energy, and signed dipole transport as different coordinate systems for the same prime-ramp defect. The present continuation separates the two issues that had remained entangled:

```text
finite positivity/transport geometry;
global arithmetic size of the prime ramp.
```

The first issue is now closed for the ordinary-prime system.

For every `X>=104301`, there exists a nonnegative physical-coordinate correction `h_X>=0` such that

```text
b_X^+ = b_X^(0)+h_X >= 0,
all ordinary-prime carry constraints are feasible,
J_P(b_X^+) = P_X exactly.
```

The correction is the solution of one finite LP. Its dual consists of monotone strongly additive arithmetic functions. A short finite rigidity argument forces every dual direction to coincide with the logarithmic/von-Mangoldt ray throughout the entire prefix below the largest power of two. Any remaining dual freedom lives in the already feasible outer region and can only improve the bound.

Thus positivity and transport impose **zero additional objective tax**. The sharp objective of the unconditional positive object is exactly the unknown ordinary-prime ramp.

## New exact theorem

The complete statement and proof are in

```text
claims/lemmas/
  L-26703-positive-prime-deformation-zero-geometric-tax.md
```

The core finite rigidity is:

```text
A(n)=sum_(p|n) a_p,
a_p>=0,
A(1)<=A(2)<=...<=A(X)

=>
a_p=0 for every p<=2^floor(log_2 X).
```

The proof begins with the exact chain

```text
A(2)<=A(3)<=A(4),
A(6)<=A(7)<=A(8),
```

which forces `a_2=a_3=a_5=a_7=0`, then uses every larger power of two as a zero prefix endpoint.

For the correction LP

```text
maximize c.h
subject to h>=0 and V_P h<=-r,
```

the dual constraint is

```text
V_P^T y>=c.
```

Subtracting the exact logarithmic solution `y_p=log p` turns this into monotonicity of

```text
A(n)=sum_(p|n)(y_p-log p).
```

The rigidity theorem makes the difference vanish on the full interior prefix. `L-24507` makes every surviving outer residual nonpositive. Therefore the logarithmic vector is a dual minimizer and

```text
max c.h = P_X-J_P(b_X^(0)).
```

This proves the exact positive deformation.

## Relation to the affine boundary lift

`L-26701/L-26702` remain useful for the complete prime-power system and for proof-producing Green/dipole interfaces. The new result shows, however, that an asymptotic ABLC estimate is not needed to establish existence of a positive ordinary-prime certificate. Positivity can be enforced with no extra scalar loss.

The affine lift still supplies an explicit one-charge conversion for any signed full carry certificate. Its cofinal charge theorem is now best viewed as one possible route to estimating the scalar, not as a necessary positivity theorem.

## Relation to current parallel branches

### PR #265 — endpoint-scale frame

The endpoint atoms provide a constructive positive basis and a small-slack greedy. `L-26703` proves abstractly that some positive correction reaches the exact optimum. PR #265 remains valuable because its structured greedy may permit a source-specific quantitative estimate rather than a generic LP existence theorem.

### PR #267 — annular additive rigidity

The new dual is exactly an additive-function cone. PR #267 controls transverse additive fluctuations by annular second differences. The remaining mode is the logarithmic ray isolated here.

### PR #269 — dyadic two-contact source

The dyadic source compresses the logarithmic/inverse-zeta obstruction to two carry contacts and two bottom Green charges. This is a plausible way to estimate the one surviving ray without controlling a full Green vector.

### PR #270 — Green–Skorokhod dipoles

The clipping/contact ledgers give explicit physical representatives. Their role is no longer to prove that a positive object exists, but to produce a representative whose logarithmic scalar can be estimated by a half-scale contact recurrence.

## What is and is not solved

Solved:

```text
nonnegative physical-coordinate deformation;
ordinary-prime feasibility;
finite transport existence;
exact optimal objective;
zero additional geometric tax.
```

Not solved:

```text
P_X >= 4 sqrt(X)-X^o(1);
the dyadic odd-leakage recurrence;
the logarithmic annular mode;
RH.
```

The theorem therefore prevents another cycle of conditional proposals that merely reconstruct positive geometry. A genuine full proof must now estimate the scalar logarithmic ray itself.

## Exact current frontier

The cleanest source-specific target is a half-scale recurrence for the dyadic signed scalar of PR #269, or an equivalent contact-cell recurrence on PR #270:

```text
D(X)
 <= D(floor((X+1)/2)) + polylog(X),
```

where `D` retains the complete logarithmic/von-Mangoldt pairing before positive parts. Such a recurrence, together with the fixed-ratio Mertens firewall, would yield the prime-ramp bound and RH.

No such recurrence is claimed in this report.