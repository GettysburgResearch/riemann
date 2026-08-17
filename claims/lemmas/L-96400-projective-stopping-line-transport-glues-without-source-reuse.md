# L-96400 — Projective stopping-line transport glues terminal parity couplings without source reuse

Claim ID: `L-96400`  
Status: **PROPOSED COMPLETE EXACT SOURCE-GLUING THEOREM — HOSTILE RECONSTRUCTION REQUIRED**  
Created: 2026-08-17  
Builds on: exact squarefree source expansion; least-rough-prime stopping line; compact factor-67 Hall source; current-only row-bonus type firewall  
RH status: **unproved**

## 1. Typed source intervals

A source occurrence has the immutable label

\[
\omega=(X,d,R,\epsilon,\mathfrak h),
\]

where `d|P_61`, `R` is a finite ordered rough-prime history,
`\epsilon` is Möbius parity, and `\mathfrak h` records all previous interval
refinements.

The coefficient of an occurrence is its literal native coefficient.  Replace
that coefficient by a half-open interval of the same length.  Intervals with
different complete labels are disjoint.  A source operation may partition an
interval, but may not copy it.

For active rough primes `p_1<...<p_k`, write

\[
r_i=p_i^{-1/2},\qquad
s_i=\prod_{h\le i}(1-r_h),\qquad
\lambda_i=r_is_{i-1},\qquad
\alpha_i=r_i\lambda_i.
\]

Then

\[
s_k+\sum_i\lambda_i=1,\qquad
\sum_i\alpha_i<\frac18.
\tag{L-96400.1}
\]

Partition each parent interval into one survival interval of relative length
`s_k` and current intervals of relative lengths `lambda_i`.  Inside current
interval `i`, mark the terminal/recursive demand subinterval of relative length
`r_i`; its absolute length is `alpha_i`.

The demand subinterval is *nested* in its current interval.  It is not an
additional copy.  Before terminalization the pair is a pending incidence, not
a physical output.

## 2. Pending incidences

A pending incidence consists of

```text
one parent interval;
one parity-flipped demand subinterval;
one rough owner p_i;
one common endpoint state;
zero physical output.
```

Refining a pending incidence partitions both sides by the same later source
labels.  Consequently every descendant subinterval has one parent, one parity,
and one coefficient.  Refinement preserves the signed source functional
exactly.

If the child endpoint is still at least `67`, only refinement occurs.  If the
child endpoint is below `67`, no additional rough prime can occur and the
incidence is terminal.

## 3. Canonical interval Hall map at a terminal fibre

At a terminal fibre `(p,y)` with `p>=67` and `1<=y<67`, order the complete
`P_61` atoms by the frozen target order.  Represent positive target capacity
and negative target demand by adjacent half-open intervals in cumulative
target coordinate.

The Hall prefix inequalities imply that the left-quantile map exhausts every
negative interval.  It leaves a positive residual source.  The same map is used
in target, declared score, rows `2` and `3`, and literal source ownership.

The target-normalized row monotonicity and the declared-score surplus give

\[
R_j(\nu_{p,y})+B_{p,y,j}
=
R_j(E_{p,y})-R_j(O_{p,y}),
\qquad
B_{p,y,j}\ge0,
\quad j=2,3.
\tag{L-96400.2}
\]

`B` is row-only and current-only.  It is not assigned target or declared-score
packet mass.

## 4. Projective compatibility

The cumulative interval map has the following exact refinement property:

> If a source interval is partitioned into labelled subintervals before the
> left-quantile Hall map is applied, the resulting transport is the restriction
> of the unrefined transport to those subintervals, up to splitting transport
> edges at common endpoints.

This follows because both constructions are intersections of half-open
intervals in one cumulative coordinate.  Hence rough refinement and terminal
Hall transport commute as measures, although they need not commute as a list
of unsplit edges.

Therefore all finite stopping-line truncations form a projective family.  At a
fixed endpoint `X` the source set is finite, so the family stabilizes after
finitely many rough primes.  No limiting or compactness argument is needed.

## 5. Exact global output

Terminalize every stabilized pending incidence and retain every unmatched
positive survival interval.  The global row is

\[
\mathscr R_X(j)
=
\sum_{\text{terminal fibres}}
\bigl(R_j(\nu)+B_j\bigr)
+
\sum_{\text{positive survivals}}R_j,
\qquad j=2,3.
\tag{L-96400.3}
\]

Every summand is nonnegative.  Source incidence conservation and projective
compatibility give

\[
\boxed{\mathscr R_X(j)=c_X(j),\qquad j=2,3.}
\tag{L-96400.4}
\]

Thus

\[
\boxed{c_X(2)\ge0,\qquad c_X(3)\ge0\qquad(X\ge1).}
\tag{L-96400.5}
\]

## 6. Mandatory hostile checks

A reconstruction must reject the theorem at the first occurrence of:

```text
one native source interval copied rather than partitioned;
a demand interval counted both as pending and as physical output;
a nonterminal incidence observed before refinement;
a rough prime remaining after a claimed y<67 terminal leaf;
different Hall coefficients in target, score, row 2, or row 3;
a row-only Hall bonus assigned source target;
a terminal map that is not the restriction of the global cumulative map;
one stabilized source interval without an owner;
failure of the exact equality in (L-96400.4).
```

The accompanying replay checks the interval/refinement algebra on finite rough
trees.  It is not a substitute for reconstructing the frozen compact and
tail Hall inequalities.
