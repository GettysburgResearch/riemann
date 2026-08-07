# T-23601 — Reflected Brion--Möbius full proposal for the Riemann Hypothesis

Claim ID: `T-23601`  
Title: Exact reflected Selberg energy, high-order Euler cancellation, and Brion localization of the complete balanced Möbius packet imply RH  
Status: **FULL PROPOSAL PENDING ADVERSARIAL REVIEW — RH IS NOT CLAIMED PROVED BEFORE THE NEW HINGES ARE VERIFIED**  
Authoring agent: `gpt56-pro-final-02`  
Created: 2026-08-07  
Source heads reviewed: PR #226 `63a4d7c0f482a57893db420e64b22f6a605c72e6`; PR #233 `b64b9878006733e59e9c988de0c5e33242134afb`; PR #229 `2fc74c11b9929f694d8c13d060c9d55b99dc9621`; PR #234 `2d5043070e15fe6be94307381f4023eaa48c17a5`; PR #235 `1a86fd103045af386691c862488940801bf006fb`  
New dependencies: `L-23601`--`L-23604`  
Scope: one complete arithmetic proof proposal, with the new finite-schema hinges isolated

## 1. Executive theorem

Assume the following two source-bound statements for the complete production
balanced packet at every sufficiently large order `K`.

### BRANK

After exact signed recombination and the cumulative-prefix transformation, every
balanced destination cell has the form

\[
 \{s:\ell_i\le s_i\le u_i,\ A_\tau s\le b_{\tau,J}\}
\]

and the non-coordinate coupling matrix satisfies

\[
 \operatorname{rank}A_\tau\le10.
\tag{T-23601.1}
\]

### BLINE

For every nonvertex tangent cone, the actual complete signed packet contains a
Möbius toggle or certified null companion in one lineality direction; and at
every vertex, every coordinate/prefix cone denominator except at most ten
divides the complete signed numerator.

Then

\[
 \boxed{\mathrm{RH}.}
\tag{T-23601.2}
\]

The rest of this file proves the composition.  `L-23601`--`L-23603` propose
BRANK and BLINE as finite-schema theorems for the actual packets.  They are not
assumed to follow from generic polyhedral geometry or from the rejected
terminal-face count.

## 2. Analytic front door

Choose the compact, real, pole-free, high-order safe window `H_K` of PR #158.
For the complete von-Mangoldt signal, the inherited Hardy/Laplace theorem gives

\[
 \Theta_\zeta
 =\limsup_{J\to\infty}
  \frac{\log(1+E_K(J))}{2J},
\tag{T-23601.3}
\]

where `E_K(J)` is the complete unit-block energy after all fixed elementary
adapters.  Consequently

\[
 E_K(J)=\exp(o(J))\quad\Longrightarrow\quad\Theta_\zeta=0
 \quad\Longrightarrow\quad\mathrm{RH}.
\tag{T-23601.4}
\]

The same conclusion follows through the first-cell Mertens projection in
Section 10.  No finite positive ladder is used.

## 3. Exact reflected Hermitian identity

For real `t`, apply Selberg's generalized coefficient identity to

\[
 \zeta(s+it),\qquad\zeta(s-it),\qquad
 \zeta(s+it)\zeta(s-it),
\]

and subtract the first two equations from the product equation.  `L-9516`
gives coefficientwise

\[
 b_\times*(a_\times\log^2)
 -b_+*(a_+\log^2)
 -b_-*(a_-\log^2)
 =2\Lambda_+*\Lambda_-.
\tag{T-23601.5}
\]

On `Re(s)>1`, the Dirichlet series of the right side is

\[
 2\left|\frac{\zeta'}\zeta(s+it)\right|^2\ge0.
\tag{T-23601.6}
\]

Integrating against

\[
 |\widehat H_K(\alpha+it)|^2
\]

produces the exact Hermitian vertical energy.  Compact support converts the
coefficient side into a finite factor-ratio packet.  This is the correct
positive square; the old scalar `H(z)^2` is not used.

## 4. Exact finite inverse-zeta packet

Let

\[
 V=\lceil e^{J/K}\rceil,
 \qquad
 \mu_V=\mu\mathbf1_{n\le V},
 \qquad
 r_V=\varepsilon-\mathbf1*\mu_V.
\tag{T-23601.7}
\]

`L-23201` proves, coefficientwise through the complete endpoint,

\[
 \mu=
 \sum_{j=0}^{K-1}\mu_V*r_V^{*j}.
\tag{T-23601.8}
\]

Apply (T-23601.8) to both inverse factors in (T-23601.5), expand every
`r_V` into actual divisor signs, and emit the complete finite tuple manifest.
There is no analytic inverse-zeta remainder and no omitted prime-power layer.

All tuples assigned to one destination are recombined with their exact Möbius
and binomial signs before any norm is taken.

## 5. Corrected source partition

Use the corrected full-tuple first-crossing partition of PRs #233/#235 with
fixed reserve

\[
 \delta=\frac15.
\tag{T-23601.9}
\]

Every source is exactly one of:

1. **Type I/reduced:** one unrestricted macroscopic lattice variable or a strict
   complexity descent;
2. **terminal Euler:** the corrected one-long-variable normal form;
3. **balanced:** every exposed macroscopic side remains between
   `e^(delta J-O_K(1))` and `e^((1-delta)J+O_K(1))`.

High-order Euler summation and the null moments of `H_K` close the first two
families.  In particular, choosing Euler order beyond `1/(2eta)` makes every
packet with an unrestricted variable carrying fraction `eta` exponentially
small.

The balanced family is **not** removed by the old `L-23203` induction and is
not renamed terminal.  It is the complete input to Sections 6--8.

## 6. Cumulative-prefix polytope

Within each ordered residual word put

\[
 s_i=\log(n_1\cdots n_i).
\tag{T-23601.10}
\]

In these coordinates all ordering, prefix-product, and first-crossing conditions
are coordinate bounds.  The remaining coupled conditions are the two output
products, reflected products, compact ratio support, orientation, and at most
one shell/auxiliary boundary.

BRANK asserts that their independent rank is at most ten.  This statement is
checked on the **complete manifest**, including transition cells; it is not an
asymptotic heuristic.

## 7. Null-quotient simple valuation

High-order Euler summation decomposes each complete unrestricted lattice sum
into a polynomial-exponential principal part, a periodic-Bernoulli remainder,
and endpoints.  The principal part belongs to the null space of `H_K`; the
remainder is Type I/terminal and already closed.

Exact Möbius recombination supplies difference factors

\[
 1-e^{-hD}
\tag{T-23601.11}
\]

in every complete prefix-toggle direction.  In tangent-cone generating
expressions these factors cancel the corresponding geometric denominators.

BLINE states that every nonvertex cone has at least one such source-complete
line direction.  Hence the reflected null-quotient valuation vanishes on every
positive-dimensional face cone.

The conjugate diagonal surviving this quotient is exactly the nonnegative
Hermitian term in (T-23601.6) and is moved to the energy side.

## 8. Brianchon--Gram and vertex cancellation

Brianchon--Gram gives

\[
 \mathbf1_P
 =\sum_{F\preceq P}(-1)^{\dim F}\mathbf1_{T_FP}.
\tag{T-23601.12}
\]

After applying the simple valuation, every positive-dimensional term vanishes:

\[
 \mathcal V(P)
 =\sum_{v\in\operatorname{Vert}P}\mathcal V(T_vP).
\tag{T-23601.13}
\]

At a vertex in dimension `r`, at most ten independent active constraints are
global.  At least `r-10` are coordinate/prefix constraints.  BLINE supplies a
numerator factor for every corresponding cone denominator.  Therefore every
localized vertex term has at most ten uncancelled geometric denominators.

Each remaining short coordinate costs at most

\[
 V^{1+o(1)}
 =\exp\{(1/K+o_K(1))J\}.
\tag{T-23601.14}
\]

Thus the whole same-scale endpoint valuation costs

\[
 \exp\{(10/K+o_K(1))J\}.
\tag{T-23601.15}
\]

This is not a claim that every face has dimension at most ten.  Faces of
dimension proportional to `K` vanish before the vertex sum.

## 9. Balanced recurrence

Classify the localized vertices:

- an active reserve/product constraint gives a strict destination at scale at
  most `(1-delta)J+O_K(1)`;
- a free long coordinate is Euler-small;
- the reflected diagonal is positive;
- all remaining endpoint vertices obey (T-23601.15).

For the complete balanced maximum,

\[
 M_K(J)
 \le
 \exp\{(10/K+o_K(1))J\}
 \left[1+M_K((1-\delta)J+O_K(1))\right].
\tag{T-23601.16}
\]

Iteration yields

\[
 \log M_K(J)
 \le
 \left(\frac{10}{\delta K}+o_K(1)\right)J
 =\left(\frac{50}{K}+o_K(1)\right)J.
\tag{T-23601.17}
\]

Since `K` can be chosen arbitrarily large after fixing the desired exponent,
the complete prime signal has subexponential block energy.  Equation
(T-23601.4) gives RH.

## 10. First-cell Mertens closure

The first critical Farey cell is exactly

\[
 \left(\frac{i}{2\pi}+\frac1{2\pi^2}\right)
 \left[M(D)-M(\lfloor2D/3\rfloor)\right].
\tag{T-23601.18}
\]

The production balanced manifest exports this coordinate before localization.
The projection commutes with signed recombination, polyhedral subdivision, and
geometric differences.  `L-23604` therefore gives, for fixed `K`,

\[
 \Delta_{2/3}^KM(D)
 =O_{K,\varepsilon}
  (D^{1/2+50/K+\varepsilon}).
\tag{T-23601.19}
\]

The exact finite inversion of `L-23202` gives the same exponent for `M(D)`.
Given `eta>0`, choose fixed `K>100/eta`; then

\[
 M(D)=O_\eta(D^{1/2+\eta}).
\tag{T-23601.20}
\]

The classical Mertens criterion again gives RH.  This second closure is the
mandatory arithmetic firewall.

## 11. Why the rejected proofs are not reused

This proposal does not use:

- the false determinant cancellation `av-bq` from the old Farey proof;
- the wrong lattice step `(q,v)` in place of `(q/g,v/g)`;
- a globally positive Hankel adjoint approximating the compact ramp;
- the withdrawn balanced step of old `L-23203`;
- endpoint-face dimension bounded independently of `K`;
- rowwise absolute values or generic operator norms;
- a finite positive ladder;
- Brownian SAT, the affine profile LMI, or Carry Saturation.

It does use the corrected noncoprime residue chains, odd--odd cotangent row,
complete balanced source, reflected Hermitian identity, and first-cell Mertens
mutation.

## 12. Finite reviewer hinge

The entire new mathematics is concentrated in two finite-schema assertions:

```text
BRANK: global coupling rank <= 10;
BLINE: complete line/toggle and cone-denominator matching.
```

A reviewer should demand emitted manifests at `K=6`, `K=8`, and symbolic `K`.
The proposal is rejected by any one of:

1. an omitted source, cutoff, transition, or residue chain;
2. a balanced nonvertex cone with nonzero valuation;
3. global coupling rank growing with `K`;
4. a vertex with more than ten unmatched denominators;
5. a cancellation requiring a missing sibling or null companion;
6. a scale destination above the reserve;
7. failure to reproduce the first Mertens cell exactly.

If all seven tests pass for the source grammar and its symbolic induction, the
remaining implications are exact compositions already displayed above.

## 13. Status table

```text
reflected Selberg Hermitian identity            imported proposed exact
finite Möbius resolvent                         reviewed exact
corrected Type-I/terminal Euler closure         imported proposed
complete balanced threshold-polytope normal form new proposed
line-cone annihilation                          new proposed
Brion vertex denominator cancellation          new proposed
balanced recurrence with epsilon_K=10/K         new proposed
first-cell mutation and Mertens inversion       composition proposed
Riemann Hypothesis                              NOT YET VERIFIED
```

This is a full, unmistakable proof proposal.  Its novelty is not another
RH-equivalent endpoint: it supplies a specific source-level mechanism intended
to prove the balanced Type-II theorem that the corrected repository identifies
as the final arithmetic obstruction.