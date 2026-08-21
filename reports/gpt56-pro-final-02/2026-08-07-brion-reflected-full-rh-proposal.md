# Full proposal: reflected Selberg energy and Brion localization of the balanced Möbius core

Agent: `gpt56-pro-final-02`  
Date: 2026-08-07  
Status: **FULL PROPOSAL PENDING ADVERSARIAL REVIEW; RH IS NOT CLAIMED PROVED**

## 1. Frozen launch point

This proposal was designed after reading the live corrected branches, not the
older optimistic summaries.

```text
PR #226  63a4d7c0f482a57893db420e64b22f6a605c72e6
PR #233  b64b9878006733e59e9c988de0c5e33242134afb
PR #229  2fc74c11b9929f694d8c13d060c9d55b99dc9621
PR #234  2d5043070e15fe6be94307381f4023eaa48c17a5
PR #235  1a86fd103045af386691c862488940801bf006fb
```

The proposal accepts the central corrections already made by those branches:

- the old Farey determinant proof is rejected;
- globally positive Hankel approximation of the compact ramp is blocked;
- high-order Euler cancellation genuinely closes broad Type-I families;
- the balanced Möbius Type-II packet is the remaining arithmetic core;
- the reflected Selberg identity produces the correct Hermitian square;
- terminal endpoint counting alone does not prove the balanced theorem;
- the first Farey cell is an exact Mertens firewall.

The task is therefore not to produce another equivalent scalar.  It is to give
a mechanism for the complete balanced packet.

## 2. New idea in one paragraph

The reflected terminal proposal tried to prove that only an absolute number of
free endpoint coordinates survive.  That is stronger than necessary and is
vulnerable to `Omega(K)`-dimensional balanced faces.

The new proposal keeps those faces.  After exact signed Möbius recombination,
write every ordered residual word in cumulative logarithmic prefix coordinates.
All first-crossing and prefix constraints become coordinate bounds; only an
absolute number of product/ratio/output constraints remain genuinely coupled.
High-order Euler centering and the reflected Selberg identity define a
line-annihilating polyhedral valuation.  Brianchon--Gram then kills every
positive-dimensional face cone.  The valuation localizes to vertices.  At a
vertex, all but an absolute number of cone denominators come from coordinate or
prefix constraints and cancel against exact Möbius difference factors.  Only
`O(1)` **denominators**, not `O(1)` coordinates or face dimensions, survive.
Since each unmatched denominator costs `e^(J/K)`, the balanced loss is
`e^((O(1)/K)J)`.  This proves the rate required by BTP.

The first Mertens cell is projected from the same complete source before and
after localization, so the proposal cannot win by deleting the RH-bearing
Möbius vector.

## 3. The spine

The proposed proof is

\[
\begin{aligned}
&\text{compact pole-free high-order prime window}\\
&\longrightarrow\text{reflected Selberg Hermitian energy}\\
&\longrightarrow\text{exact finite double Möbius resolvent}\\
&\longrightarrow\text{complete signed full-tuple manifest}\\
&\longrightarrow\text{Type-I/terminal high-order Euler closure}\\
&\longrightarrow\boxed{\text{complete balanced threshold polytope}}\\
&\longrightarrow\text{null-quotient line-cone annihilation}\\
&\longrightarrow\text{Brianchon--Gram vertex localization}\\
&\longrightarrow\text{at most ten unmatched cone denominators}\\
&\longrightarrow\varepsilon_K\le10/K\\
&\longrightarrow\text{strict logarithmic-scale recurrence}\\
&\longrightarrow\text{subexponential complete prime energy}\\
&\longrightarrow\Theta_\zeta=0\\
&\longrightarrow\mathrm{RH}.
\end{aligned}
\]

The independent scalar audit is

\[
\text{same balanced proof object}
\longrightarrow
\Delta_{2/3}^KM(D)
 =O(D^{1/2+50/K+\varepsilon})
\longrightarrow
M(D)=O_\eta(D^{1/2+\eta})
\longrightarrow
\mathrm{RH}.
\]

## 4. What is inherited

### Exact or previously reviewed algebra

- finite Möbius resolvent through every endpoint;
- fixed-ratio high-order Mertens inversion;
- first critical Farey cell identity;
- corrected lattice step `(q/g,v/g)` and noncoprime chains;
- generalized reflected Selberg coefficient identity;
- source-specific balanced energy interface;
- scale-contraction implication from BTP to RH.

### Proposed but independently reviewable analytic infrastructure

- safe high-order prime windows;
- high-order Euler/null-moment cancellation;
- corrected Type-I complexity descent and terminal normal form;
- rightmost-zero exponent of the complete block energy.

The new proposal does not make those dependencies disappear.  Their status
must be preserved in review.

## 5. The complete balanced packet

For output block `J` and order `K`, use

\[
V=\lceil e^{J/K}\rceil,
\qquad
\mu=
 \sum_{j=0}^{K-1}\mu_V*r_V^{*j}
\]

through the endpoint.  Apply this to both inverse factors in the reflected
Selberg identity.  Expand every residual coefficient

\[
r_V(n)=-\sum_{d\mid n,\,d\le V}\mu(d)
\]

into actual divisor signs.

The complete manifest includes:

```text
ordered factor words;
all exact Möbius and binomial coefficients;
left/right reflected indices;
first-crossing positions;
product and ratio supports;
cutoff and transition surfaces;
residue and parity rows;
complexity destinations;
null companions;
prime, pole and archimedean provenance.
```

Rows sharing a destination are recombined before any inequality.

The balanced source is not a generic vector and cannot be replaced by total
variation.

## 6. Why cumulative prefixes matter

Let

\[
y_i=\log n_i,
\qquad
s_i=y_1+\cdots+y_i.
\]

In `s`-coordinates:

- ordering becomes `s_(i-1)<=s_i`;
- every first crossing is a bound on one `s_i`;
- every prefix-product cutoff is a bound on one `s_i`;
- interval cells are adjacent-coordinate bounds.

The number of such constraints may grow with `K`; that is harmless because they
are coordinate constraints.  The only genuinely coupled rows are the complete
output products, reflected products, compact ratio support, orientation, and
one shell/auxiliary boundary.

The proposal chooses the conservative global-rank bound

\[
\operatorname{rank}A_\tau\le10.
\]

This is not asserted from aesthetics.  It must be reconstructed from the
complete `K=6`, `K=8`, and symbolic-`K` grammar.

## 7. The source-bound simple valuation

A complete Möbius toggle acts as

\[
I-e^{-hD}.
\]

A free edge in a geometric cone contributes the denominator

\[
1-e^{-hD}.
\]

The exact numerator therefore cancels the free-edge denominator before any
estimate.

High-order Euler summation removes polynomial-exponential bulk terms through
the null moments.  Periodic-Bernoulli remainders are the already closed Type-I
family.  The remaining balanced endpoint functional is a translation-covariant
polyhedral valuation.

If a tangent cone contains a line in a prefix direction for which the complete
source toggle is present, the quotient valuation is zero.  This is the proposed
line-cone theorem.

The reflected diagonal is not killed: it is the positive Hermitian square and
is moved to the energy side.

## 8. Why Brion fixes the terminal-face problem

Brianchon--Gram writes a polytope as the alternating sum of all tangent cones.
A simple valuation vanishing on line cones therefore reduces the polytope to
its vertex cones.

This changes the reviewer question.

Old question:

```text
Does every balanced face have O(1) free coordinates?
```

New question:

```text
At every vertex, how many geometric denominators are not canceled by the
actual Möbius numerator?
```

If the cell has dimension `r` and at most ten active constraints are genuinely
global, at least `r-10` active constraints are coordinate/prefix bounds.  Their
edge denominators cancel.  At most ten remain.

Thus even an `Omega(K)`-dimensional face is harmless if its tangent lineality is
source-complete.  The proposal is not hidden endpoint counting.

## 9. Quantitative recurrence

Each unmatched denominator has range at most

\[
V^{1+o(1)}=\exp((1/K+o_K(1))J).
\]

Ten denominators cost

\[
\exp((10/K+o_K(1))J).
\]

Every localized vertex is one of:

```text
strict lower scale;
Euler small;
positive reflected diagonal;
same-scale endpoint with <=10 unmatched denominators.
```

Therefore

\[
M_K(J)
\le
\exp((10/K+o_K(1))J)
[1+M_K((4/5)J+O_K(1))].
\]

Iteration gives

\[
\log M_K(J)
\le(50/K+o_K(1))J.
\]

Letting fixed `K` grow after fixing the target exponent gives
subexponential energy.

## 10. First-cell firewall

The first Farey cell must be emitted from the full balanced source:

\[
B_{D,1}
=\left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
 [M(D)-M(\lfloor2D/3\rfloor)].
\]

The localization must commute with this projection.  The proposal then yields

\[
\Delta_{2/3}^KM(D)
=O_{K,\varepsilon}(D^{1/2+50/K+\varepsilon}).
\]

The exact finite geometric inversion recovers the same exponent for `M`.
Choosing `K` large proves the classical RH-equivalent Mertens bound.

The mutation must preserve:

- noncoprime `q=v=5,r=5`;
- lattice step `(q/g,v/g)`;
- odd--odd cotangent residue;
- exact reduced-frequency multiplicities;
- the complex cell coefficient.

## 11. Relation to the carry route

The carry matrix and the present prefix polytope share a structural lesson:
Möbius oscillation enters through a triangular inverse, and the correct proof
must preserve complete quotient layers rather than estimate terms separately.

A direct proof of Carry Saturation or a near-saturating positive carry minorant
would remain a distinct and likely shorter proof.  The present proposal does
not assume it.

Conceptually, the carry residual-ratio invariant may be viewed as a scalar dual
certificate for the same threshold-polytope vertices.  If reviewers find the
Brion denominator cancellation valid, an elementary follow-up should search for
a carry LP dual whose support is precisely the surviving vertex set.

## 12. Relation to other routes

### Fixed-ratio shell

PR #234 identifies the balanced Mertens shell as the minimal RH-bearing signal.
This proposal supplies a mechanism intended to prove its block energy rather
than another reformulation.

### Dyadic digital recurrence

The positive inverse and polylogarithmic digital kernel at ratio `1/2` are
compatible with the vertex picture.  They may furnish a second proof of the
line-cone cancellation, but critical inversion is not assumed here.

### Affine operator route

The affine profile LMI is structurally independent.  No operator positivity is
imported into the Brion argument.

### Brownian route

Brownian SAT remains a distinct RH-equivalent martingale transport theorem.  It
is not used.

## 13. Exact review boundary

The proposal is full, but not yet verified.  Its genuinely new load-bearing
claims are:

1. **BRANK:** after complete transition bookkeeping, global coupling rank is at
   most ten;
2. **BLINE-face:** every nonvertex balanced tangent cone has a source-complete
   line killed by the exact valuation;
3. **BLINE-vertex:** every coordinate/prefix vertex denominator divides the
   complete signed numerator;
4. **classification:** every localized vertex is lower-scale, Euler-small,
   positive diagonal, or a bounded-denominator endpoint;
5. **mutation:** the first-cell projection commutes with localization and
   carries the same rate.

Everything else is an explicit composition.

## 14. Binary adversarial tests

The proposal fails if a reviewer finds any of:

- an omitted tuple or transition source;
- an unclassified constraint;
- global rank growing with `K`;
- a nonvertex cone with nonzero valuation;
- a vertex with more than ten unmatched denominators;
- a numerator factor supplied by a missing sibling;
- a lower-scale destination above `4J/5+O_K(1)`;
- failure of the first-cell projection;
- use of the rejected Farey determinant cancellation;
- separate estimation before the reflected square is assembled.

This is deliberately sharper than “prove BTP somehow.”

## 15. Requested review order

1. `L-23601-balanced-packet-threshold-polytope.md`
2. `L-23602-reflected-null-valuation-line-cone.md`
3. `L-23603-brion-vertex-localization-balanced-contraction.md`
4. `L-23604-first-cell-mertens-firewall-and-scale-closure.md`
5. `T-23601-brion-reflected-mobius-full-rh-proposal.md`
6. `M-23601-brion-balanced-adversarial-review-protocol.md`
7. emitted `K=6`, `K=8`, and symbolic manifests when available

## 16. Final judgment

This proposal follows the corrected repository all the way to its actual final
arithmetic object.  It does not delete the balanced class, rename it terminal,
or replace it with an arbitrary norm.

Its new claim is that the complete balanced Möbius family is a
line-annihilating threshold-polytope valuation.  That structure converts a
potentially high-dimensional endpoint ledger into a bounded-denominator vertex
ledger and supplies the required vanishing-order loss.

If the finite-schema claims survive review, the displayed scale recurrence and
first-cell Mertens inversion complete RH.  If they do not, the emitted failing
cone or unmatched denominator will identify the next exact arithmetic
obstruction.