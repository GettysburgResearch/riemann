# R-24501 — Rank, face-count, and Abel-mass shortcuts do not close the carry resolvent

Claim ID: `R-24501`  
Title: Three exact scope firewalls for post-review RH proposals built from the reflected Selberg identity  
Status: **PROPOSED SCOPE CORRECTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: PR #241 frozen review; PR #234 fixed-ratio shell; `L-24501`--`L-24503`  
Scope: logical sufficiency only; no verdict on every lemma in PRs #240, #242, or #244

## 1. Fixed output rank does not bound an arithmetic coefficient

Collapsing a tuple fiber to one arithmetic output can reduce geometric
dimension without reducing coefficient size.

The first coherent Farey/shell coordinate is already a scalar:

\[
 M(D)-M(\lfloor2D/3\rfloor).
 \tag{R-24501.1}
\]

It has output rank one, yet square-root control of this one scalar is
RH-equivalent by the exact geometric inversion on PRs #229/#234.

Therefore the implication

\[
\boxed{
 \text{bounded post-contraction output rank}
 \Longrightarrow X^{o(1)}\text{ arithmetic loss}}
 \tag{R-24501.2}
\]

is false without an independent coefficient estimate. A box-spline or
fixed-rank endpoint theorem must still control the actual Möbius coefficient on
each surviving output.

## 2. Cone-denominator cancellation does not bound the surviving numerator

Suppose a polyhedral or Brion representation cancels all but `r` geometric
denominators. This proves only that the remaining generating expression has
`r` free geometric directions. It does not bound the numerator coefficient
carried by a long Möbius shell.

In particular, a scalar vertex term may still contain (R-24501.1). Hence

\[
\boxed{
 \text{few unmatched cone denominators}
 \not\Longrightarrow
 \text{small signed arithmetic coefficient}.}
 \tag{R-24501.3}
\]

A valid localization proof additionally needs:

1. a source-complete line/toggle map;
2. a proof that every uncancelled direction is short;
3. a bound for the surviving source-specific numerator;
4. the exact first-cell mutation.

This is why the new carry proposal does not import face count, global constraint
rank, or fixed output rank as an estimate.

## 3. Abel mass does not produce a positive finite minorant

`L-24501` proves the removable boundary value

\[
 G(1/2)=8.
 \tag{R-24501.4}
\]

This is an Abel value of a signed inverse-zeta state. It does not imply:

\[
 g(u)\ge0,
 \tag{R-24501.5}
\]

ordinary boundary convergence of

\[
 \int e^{-u/2}g(u)du,
 \tag{R-24501.6}
\]

or the existence of a finite nonnegative vector of mass `8 sqrt(X)`.

Indeed every off-line zero gives an uncancelled pole of `G` at
`s=rho-1/2`. Any positivity or boundary-stability theorem for the infinite state
must confront that mode.

Thus

\[
\boxed{
 \text{critical Abel mass eight}
 \not\Longrightarrow
 \text{DCRS}.}
 \tag{R-24501.7}
\]

The finite positive profile and its boundary correction are separate obligations
in `L-24503`.

## 4. Kernel domination has only one safe direction

The exact comparison is

\[
 0\le\beta_{nq}\le b(n/q).
 \tag{R-24501.8}
\]

For a nonnegative vector `d`, a continuum-majorant inequality

\[
 \sum_nd_n b(n/q)\le w(q)
 \tag{R-24501.9}
\]

implies the discrete feasibility

\[
 \sum_nd_n\beta_{nq}\le w(q).
 \tag{R-24501.10}
\]

The converse is false. Nor may one apply (R-24501.8) to a signed continuum
inverse. A proof must first produce a nonnegative finite profile satisfying the
stronger continuum inequalities or directly charge the discretization error.

## 5. Aggregate reflected positivity is not packet coercivity

The repaired two-frequency identity on PR #241 is an exact equality for the
complete normal Gram. If a source is decomposed into packet components, the
identity contains every cross term. It does not provide a positive lower bound
for each component separately.

Therefore

\[
\boxed{
 \text{positive aggregate reflected square}
 \not\Longrightarrow
 \text{packetwise positive contraction}.}
 \tag{R-24501.11}
\]

Any use inside a carry blocker proof must write one coupled scalar or matrix
identity for the actual unmatched source.

## 6. Consequence for proposal design

A review-hardened proposal may use:

- exact reflected algebra;
- exact finite carry algebra;
- exact continuum transforms;
- explicit one-sided kernel comparison.

It may not infer the cofinal estimate from:

- bounded rank;
- bounded face dimension;
- canceled geometric denominators alone;
- the Abel value alone;
- aggregate positivity after packet splitting.

The remaining theorem must be stated directly as a source-specific finite mass,
boundary, and blocker estimate, as in `L-24503`.

## 7. Proof boundary

This refutation does not prove DCRS or reject every alternative proposal. It
records the minimal logical firewalls forced by the frozen PR #241 review and
the exact fixed-ratio shell.
