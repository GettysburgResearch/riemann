# L-23603 — Brion vertex localization closes the balanced Möbius packet

Claim ID: `L-23603`  
Title: A line-annihilating reflected Möbius valuation localizes to vertices, where all but a bounded number of cone denominators cancel  
Status: **PROPOSED CLOSING LEMMA / FULL-PROOF HINGE PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-final-02`  
Created: 2026-08-07  
Corrected: 2026-08-07 to separate denominator count from unmatched-edge shortness  
Dependencies: `L-23601`, `L-23602`, `L-23605`; Brianchon--Gram/Brion valuation algebra; PR #233 `L-23207`; PR #234 fixed-ratio shell criterion  
Scope: the complete balanced Type-II family, not only terminal rows

## 1. Statement

Retain the fixed reserve

\[
 \delta=\frac15
\tag{L-23603.1}
\]

and let `M_K(X)` be the complete balanced energy maximum of `L-23207`.  Assume
the BRANK and BLINE schema properties of `L-23601/L-23602`, and the BSHORT
short-edge trichotomy of `L-23605`.  Then

\[
 \boxed{
 M_K(J)
 \le
 \exp\left\{
  \left(\frac{g_0}{K}+o_K(1)\right)J
 \right\}
 \left[
 1+M_K\bigl((1-\delta)J+O_K(1)\bigr)
 \right],}
\tag{L-23603.2}
\]

with the absolute constant

\[
 \boxed{g_0=10.}
\tag{L-23603.3}
\]

Consequently `BTP(K)` holds with

\[
 \varepsilon_K\le\frac{10}{K},
\tag{L-23603.4}
\]

and the required coefficient tends to zero along every unbounded sequence of
orders.

The proof does not assume that a balanced face has bounded dimension.  It
localizes the complete valuation to vertices and counts only uncancelled cone
denominators.  `L-23605` separately proves that every unmatched same-scale
direction has short range; denominator count alone is not enough.

## 2. Brianchon--Gram localization

For a polytope `P` and a face `F`, let `T_F P` be the tangent cone at `F`.
Brianchon--Gram gives the indicator identity, as a polyhedral valuation,

\[
 \mathbf1_P
 =\sum_{F\preceq P}
  (-1)^{\dim F}\mathbf1_{T_F P}.
\tag{L-23603.5}
\]

Apply the reflected null-quotient valuation of `L-23602`.  Every tangent cone at
a positive-dimensional face contains a certified source-complete line and
therefore vanishes.  Hence

\[
 \boxed{
 \overline{\mathcal V}^{\rm ref}_{K,\tau}(P)
 =\sum_{v\in\operatorname{Vert}P}
   \overline{\mathcal V}^{\rm ref}_{K,\tau}(T_vP).}
\tag{L-23603.6}
\]

Equation (L-23603.6) replaces the unsupported assertion that every endpoint
face has only `O(1)` free coordinates.

## 3. Cone generating expression

Let the cell dimension be `r`.  After a simplicial refinement, a vertex cone
has primitive edge directions `e_(v,1),...,e_(v,r)`.  Its exponential or
geometric-series expression is

\[
 \mathscr G_v(z)
 =e^{-\langle z,v\rangle}
  \frac{N_v(z)}
  {\prod_{j=1}^r
   (1-e^{-\langle z,e_{v,j}\rangle})}.
\tag{L-23603.7}
\]

Here `N_v` contains:

- the exact signed Möbius toggle factors;
- the high-order safe-window numerator;
- reflected Selberg source coefficients;
- finite transition and endpoint numerators.

No denominator in (L-23603.7) is estimated until exact divisibility by `N_v`
has been checked.

## 4. Active-constraint linear algebra

The prefix normal form of `L-23601` separates constraints into:

1. coordinate/prefix bounds; and
2. at most `g_0` independent global coupling rows.

At a nondegenerate vertex in dimension `r`, `r` independent constraints are
active.  At most `g_0` of them can be global, so at least

\[
 r-g_0
\tag{L-23603.8}
\]

active constraints are coordinate or prefix bounds.  The same conclusion holds
after a lexicographic simplicial refinement of a degenerate vertex.

For every coordinate/prefix edge, exact signed recombination supplies the
factor

\[
 1-e^{-\langle z,e_{v,j}\rangle}
\tag{L-23603.9}
\]

in `N_v`; this is the cone version of `L-23602.6`.  Therefore at least
`r-g_0` denominator factors cancel algebraically.  The reduced vertex term has
at most `g_0` geometric denominators:

\[
 \boxed{
 \mathscr G_v(z)
 =e^{-\langle z,v\rangle}
  \frac{\widetilde N_v(z)}
  {\prod_{j\in U_v}
   (1-e^{-\langle z,e_{v,j}\rangle})},
 \qquad |U_v|\le g_0.}
\tag{L-23603.10}
\]

This denominator-divisibility assertion, rather than the dimension of the
original face, is the first main reviewer hinge.

## 5. Shortness and endpoint exponent

The bound `|U_v|<=g_0` does not by itself imply a vanishing exponent.  Invoke
the independent BSHORT theorem `L-23605`: every unmatched same-scale edge is a
short divisor/quotient edge with multiplicative range at most

\[
 V^{1+o(1)}
 =\exp\left\{
  \left(\frac1K+o_K(1)\right)J
 \right\}.
\tag{L-23603.11}
\]

Every longer edge is canceled, strict lower-scale, or Euler-small.  Therefore
(L-23603.10) costs at most

\[
 \exp\left\{
  \left(\frac{g_0}{K}+o_K(1)\right)J
 \right\}.
\tag{L-23603.12}
\]

For fixed `K`, the number of cells, vertices, simplicial cones, binomial
multiplicities, fixed-order divisor multiplicities, and prefix-transform
determinants contributes only `exp(o_K(J))`.

No factor `V^(Omega(K))` remains.  The `Omega(K)`-dimensional faces have already
vanished in (L-23603.6), while any unmatched long edge would violate BSHORT and
reject the theorem.

## 6. Scale destinations

Each vertex is classified from its active constraints and edge types.

### Strict vertices

If a total-product or first-crossing global row is active away from the output
endpoint, one exposed factor is at most

\[
 \exp\{(1-\delta)J+O_K(1)\}.
\tag{L-23603.13}
\]

The vertex term is exactly a declared lower-scale balanced destination and is
bounded by

\[
 M_K((1-\delta)J+O_K(1)).
\tag{L-23603.14}
\]

### Euler vertices

If an unrestricted macroscopic complete lattice coordinate remains, the
high-order Euler lemma applies and the term is exponentially small.

### Reflected diagonal vertices

The surviving conjugate diagonal is the nonnegative left side of `L-9516` and
is absorbed into the energy.

### Endpoint vertices

All remaining same-scale vertices have at most `g_0` uncancelled denominator
directions by BLINE, and all those directions are short by BSHORT.  They obey
(L-23603.12).

Combining the four classes proves (L-23603.2).

## 7. Why the balanced class is not imported

The proof of (L-23603.2) does not call the withdrawn balanced step in the old
`L-23203`.  Its inputs are:

```text
complete balanced manifest,
reflected Hermitian identity,
null-moment/Euler line annihilation,
prefix-polytope normal form,
Brianchon--Gram,
vertex denominator cancellation,
and the independent short-edge trichotomy.
```

The balanced rows are the object being evaluated by (L-23603.6); they are not
removed by a prior induction.

## 8. First-cell firewall

The fixed `q_0=2` projection of PR #229 commutes with the valuation and vertex
localization.  On that projection, (L-23603.2) becomes the high-order
fixed-ratio Mertens difference estimate recorded in `L-23604`.

The coherent long Mertens shell direction is not labeled short.  It is consumed
by the complete signed toggle and reappears in the projected finite-difference
coordinate, as required by `L-23605`.

The following mutations are mandatory:

1. replace the Möbius vector by absolute values;
2. omit the noncoprime `q=v=5,r=5` residue chain;
3. delete the odd--odd cotangent residue;
4. route the first cell to the terminal-only family;
5. add one unmatched coordinate edge at a vertex;
6. relabel one long shell edge as short.

All six must fail.

## 9. Exact adversarial questions

A reviewer can reject the theorem by exhibiting any one of:

- a production balanced cell whose nonvertex cone has nonzero valuation;
- a constraint omitted from the prefix normal form;
- global coupling rank growing with `K`;
- a vertex with more than ten unmatched cone denominators;
- a denominator cancellation that requires a missing sibling or null companion;
- one unmatched same-scale edge with range larger than `V^(1+o(1))`;
- an incomplete-lattice Euler label;
- a first-cell projection not reproduced with its exact coefficient;
- a strict-scale destination above `(1-delta)J+O_K(1)`.

Conversely, complete `K=6`, `K=8`, and symbolic-`K` manifests satisfying these
checks verify the new arithmetic hinge.

## 10. Proof boundary

The polyhedral identities and active-constraint rank count are standard exact
algebra.  The source-specific assertions requiring independent verification are:

1. every nonvertex line is matched by an actual source toggle;
2. every coordinate/prefix cone denominator divides the complete numerator;
3. global constraint rank is at most ten after all transition cells are
   included;
4. every unmatched same-scale edge is short;
5. the vertex classification is complete.

Subject to those five finite-schema checks, (L-23603.2) proves `BTP` with the
rate required for RH.