# Genus-two model, orbit, and affine-stack measures

Status: **DRAFT exact lemma plus frozen finite comparisons**

Scope: monic squarefree quintics over `F_q`, modulo the declared affine change
of variable with the point at infinity retained. This is not the full moduli
stack of unpointed genus-two curves.

Exact sources or dependencies: `genus2_affine_orbits.py` and its frozen JSON
certificate.

What was actually run: exact rational post-processing of the checked-in orbit
and stabilizer histograms for `q=3,5,7`; no field was enumerated.

Smallest remaining gap: determine which detector statistics descend through a
source-faithful moduli problem, then prove their stack-weighted character
averages rather than silently replacing them by uniform orbit averages.

## Exact all-field identity

Let `X=H_5(q)` be the monic squarefree quintics and let
`G=AGL(1,F_q)` act by

\[
D(T)\longmapsto \alpha^{-5}D(\alpha T+\beta).
\]

For every odd prime power,

\[
|X|=q^5-q^4=q^4(q-1),\qquad |G|=q(q-1).
\]

Orbit-stabilizer therefore gives the exact groupoid cardinality

\[
\boxed{\sum_{[D]\in X/G}\frac1{|\operatorname{Stab}(D)|}=q^3}.
\]

More generally, if `f` is invariant under this action, then

\[
\boxed{
\frac1{|X|}\sum_{D\in X}f(D)
=\frac1{q^3}\sum_{[D]\in X/G}
  \frac{f(D)}{|\operatorname{Stab}(D)|}.}
\]

Thus the uniform polynomial-model family is already the stabilizer-weighted
affine-stack measure on this quotient. It is **not** the uniform measure on coarse
orbit representatives. An orbit with stabilizer order `s` receives coarse to
affine-stack weight ratio

\[
\frac{s q^3}{N_q},
\]

where `N_q` is the number of affine orbits. Coarse averaging systematically
overweights the automorphism strata.

## Exact Burnside classification of the coarse quotient

The nonidentity fixed loci can also be classified for every odd prime power.
For `alpha != 1`, translation to the unique fixed point reduces an affine
element to `S -> alpha*S`. If `d` is the order of `alpha`, a fixed monic
quintic can contain only powers `S^j` with `j=5 mod d`. Squarefreeness leaves
only the following contributions:

| order | fixed shape | squarefree count per element |
|---:|---|---:|
| 2 | `S^5+c3*S^3+c1*S` | `(q-1)^2` |
| 3 | `S^5+c2*S^2` | `0` |
| 4 | `S^5+c1*S` | `q-1` |
| 5 | `S^5+c0` | `q-1` |
| every other order | `S^5` | `0` |

For order two, write the polynomial as
`S(S^4+c3*S^2+c1)`. The root at zero is simple exactly when `c1!=0`;
putting `x=S^2` shows that a nonzero repeated root occurs exactly when
`c3^2=4*c1`. Of the `q(q-1)` pairs with `c1!=0`, precisely `q-1` lie on that
discriminant, leaving `(q-1)^2`. The order-three shape has an unavoidable
factor `S^2`. The order-four and order-five shapes are squarefree exactly when
their displayed coefficient is nonzero (order five cannot occur in
characteristic five because then `5` does not divide `q-1`).

There are `q` affine elements over each nontrivial scaling. A nonidentity
translation fixes a monic quintic only in characteristic five, where the `q`
polynomials

\[
S^5-\beta^4S+c_0
\]

are all squarefree.

For completeness, the translation claim follows directly from the leading
coefficient of `D(S+beta)-D(S)`: it is `5*beta` in degree four, so no fixed
monic quintic exists outside characteristic five. In characteristic five,
successive lower-degree coefficients force the unique nonconstant lower term
to be `-beta^4*S`; the derivative is the nonzero constant `-beta^4`.

Burnside's lemma therefore gives the exact all-field count

\[
\boxed{
N_q=q^3+q-1
+2\mathbf 1_{4\mid q-1}
+4\mathbf 1_{5\mid q-1}
+\mathbf 1_{\operatorname{char}\mathbb F_q=5}.}
\]

This yields `N_3=29`, `N_5=132`, and `N_7=349` without enumerating a curve.
It also explains why the coarse quotient has congruence- and
characteristic-dependent corrections even though its affine-stack cardinality
is the uniform polynomial `q^3`.

Let `delta_q=N_q-q^3`. For the uniform measure on coarse orbits and the
affine-stack measure, the triangle inequality gives

\[
\operatorname{TV}(\mu_{\rm coarse},\mu_{\rm affine\ stack})
\le \frac{\delta_q}{q^3}
\le \frac{q+6}{q^3}=O(q^{-2}).
\]

Indeed, summing the discrepancy introduced by replacing `1/N_q` first with
`1/q^3` and then with `1/(s q^3)` over a stabilizer-`s` orbit gives two copies
of `delta_q/q^3`, followed by the factor `1/2` in total variation. Since
`N_q<2q^3`, free orbits are underweighted and every nonfree orbit is
overweighted by the coarse measure. If `n_1(q)` is the number of free orbits,
the exact distance is therefore

\[
\operatorname{TV}
=\frac{n_1(q)\delta_q}{q^3N_q}.
\]

Consequently every uniformly bounded invariant has the same large-`q` limit
under the two measures whenever either limit exists. For `|f|<=M`, their
expectations differ by at most `2M*delta_q/q^3`. The choice of measure remains
important for finite fields and rare tails, but it cannot change a bounded
limiting statistic at leading order.

## Frozen measure distortion

The exact total-variation distances between the uniform coarse-orbit measure
and the model/affine-stack measure are

```text
q=3: 50/783       = 0.0638569604...
q=5: 77/1500      = 0.0513333333...
q=7: 2022/119707  = 0.0168912427...
```

Even the negative-sign frequency depends on the family measure:

| `q` | uniform coarse orbits | uniform models = affine stack | coarse minus affine stack |
|---:|---:|---:|---:|
| 3 | `19/29` | `17/27` | `20/783` |
| 5 | `43/66` | `33/50` | `-7/825` |
| 7 | `237/349` | `33/49` | `96/17101` |

The discrepancy changes sign, so there is no responsible monotone correction
to infer from these three fields.

The nonfree locus is more visible under the coarse measure than under the
model/affine-stack measure:

| `q` | coarse-orbit mass | model/affine-stack mass |
|---:|---:|---:|
| 3 | `4/29` | `2/27` |
| 5 | `1/12` | `4/125` |
| 7 | `12/349` | `6/343` |

At `q=5`, the exceptional orbit fixed by all 20 affine elements has weight
`1/132` under uniform representatives but only `1/2500` under the affine-stack
measure: an amplification by `625/33`. This is exactly the kind of distortion
that can dominate a tail-sensitive detector if the family measure is left
implicit.

## Interpretation firewall

This lemma does not identify the quotient with the full unpointed genus-two
moduli stack. In particular, non-affine automorphisms need not be visible in an
`AGL(1,q)` stabilizer. It proves no equidistribution or arithmetic
equidistribution rate. Its purpose is to make the family measure a typed
mathematical input: raw equations, stack
weights, and coarse isomorphism representatives are different ensembles, and
only the first two agree in the declared affine model problem.
