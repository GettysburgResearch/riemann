# L-23605 — Short unmatched-edge trichotomy

Claim ID: `L-23605`  
Title: Every uncancelled Brion cone direction is a short Möbius divisor edge; every long residual edge is canceled, lower-scale, or Euler-small  
Status: **PROPOSED INDEPENDENT FULL-PROOF HINGE PENDING REVIEW**  
Authoring agent: `gpt56-pro-final-02`  
Created: 2026-08-07  
Dependencies: `L-23601`--`L-23603`; PR #233 corrected first-crossing/terminal grammar; PR #234 top-order concentration; PR #235 full-tuple partition  
Scope: the quantitative step converting denominator count into the exponent `O(1/K)`

## 1. Why this is separate

A vertex with only `O(1)` uncancelled geometric denominators is not enough for
an `O(1/K)` exponent if one denominator parametrizes a range of length
`exp(O(J))`.  The endpoint estimate also requires every unmatched direction to
range over at most

\[
 V^{1+o(1)},
 \qquad
 V=\lceil e^{J/K}\rceil.
\tag{L-23605.1}
\]

This shortness does not follow from polyhedral rank alone.  It is a distinct
source-specific statement.

## 2. Edge types

After the finite Möbius resolvent and cumulative-prefix transformation, every
primitive edge direction of a balanced vertex is assigned one of four exact
types.

### S — short divisor edge

The edge changes one truncated Möbius divisor or one bounded quotient index.
Its multiplicative range is

\[
 \le V^{1+o(1)}.
\tag{L-23605.2}
\]

### T — toggled residual edge

The edge changes a residual/prefix coordinate whose full signed sibling is
present.  Its geometric denominator divides the complete Möbius numerator and
is canceled algebraically.

### L — lower-scale edge

Motion along the edge activates a first-crossing or total-product reserve and
routes the vertex to a destination of scale

\[
 \le(1-\delta)J+O_K(1).
\tag{L-23605.3}
\]

### E — Euler edge

The edge exposes a complete unrestricted lattice variable carrying a fixed
positive fraction of the scale.  The high-order Euler/null-moment theorem makes
the corresponding term exponentially small.

The proposed trichotomy is

\[
 \boxed{
 \text{every primitive balanced vertex edge belongs to exactly one of}
 \ S,T,L,E.}
\tag{L-23605.4}
\]

## 3. Unmatched-edge theorem

An unmatched cone denominator is, by definition, one not canceled by BLINE and
not consumed by a positive reflected diagonal.  The proposed theorem is

\[
 \boxed{
 \text{every unmatched same-scale denominator is type S}.}
\tag{L-23605.5}
\]

Equivalently, every edge with multiplicative range larger than
`V^(1+o(1))` is type `T`, `L`, or `E`.

This is the property denoted **BSHORT** in the corrected executive theorem.

## 4. Proposed proof by first crossing

Use the complete full-tuple partition, not an individual residual word.

1. If a long residual coordinate can move while all global product constraints
   remain inactive, then its complete sibling row is present in the same
   destination.  It is type `T`.
2. If one sibling is removed by a product or cutoff boundary, that boundary is
   active.  The first-crossing reserve makes the edge type `L`, unless the
   exposed lattice interval is complete.
3. If the interval is complete, high-order Euler summation applies and the edge
   is type `E`.
4. The only remaining degrees of freedom are the truncated divisor variables
   `d<=V` and bounded quotient/cell indices; these are type `S`.

Transition rows are essential in Step 2.  Omitting them can manufacture a false
short edge or a false toggle.

## 5. Quantitative consequence

Combine `L-23603`'s bound of at most `g_0=10` unmatched denominators with
(L-23605.5).  Every one costs at most

\[
 V^{1+o(1)}
 =\exp\left\{
   \left(\frac1K+o_K(1)\right)J
  \right\}.
\tag{L-23605.6}
\]

Therefore the same-scale vertex ledger costs

\[
 \boxed{
 \exp\left\{
   \left(\frac{10}{K}+o_K(1)\right)J
  \right\}.}
\tag{L-23605.7}
\]

Without BSHORT, no vanishing exponent follows from the Brion localization.

## 6. Exact production fields

Every vertex edge in the proof object must include:

```text
edge ID and primitive direction;
source variables changed;
multiplicative range;
S/T/L/E type;
for T: matching numerator factor and sibling rows;
for L: active reserve row and destination scale;
for E: complete lattice interval and Euler order;
for S: exact bound by V^(1+o(1)).
```

The checker must recompute the range and reject an untyped edge.

## 7. Mandatory mutations

The following controls must fail:

1. relabel a long residual edge as `S`;
2. delete the sibling of a `T` edge;
3. widen an `S` edge beyond `V^(1+o(1))`;
4. route an `L` edge above the reserve;
5. apply Euler to a truncated lattice interval;
6. omit the transition row separating `T` from `L`;
7. leave one long same-scale edge unmatched.

## 8. First-cell audit

The first Mertens cell contains a coherent long Möbius shell.  Its long shell
direction must **not** be labeled short.  Under the proposed grammar it is
consumed by the complete signed `T` valuation and reappears in the projected
finite-difference coordinate.  If it survives as an unmatched long edge, or is
routed away as Type I, the proposal fails.

## 9. Proof boundary

`L-23605` is an explicit correction to the initial draft of the Brion proposal.
BRANK and BLINE alone do not imply the `10/K` exponent.  The full composition
requires all three independent schema properties:

```text
BRANK   bounded global constraint rank;
BLINE   line-cone and denominator matching;
BSHORT  every unmatched same-scale edge is short.
```

The finite full-tuple manifests at `K=6`, `K=8`, and symbolic `K` must verify
the trichotomy before the recurrence is accepted.