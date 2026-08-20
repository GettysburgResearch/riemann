# L-102002 — Composite-owner lifting should be formulated as a joint min–max collar certificate

Claim ID: `L-102002`
Status: **PROVED EXACT REDUCTION; TWO LOCAL CERTIFICATES OPEN**
Created: 2026-08-21
Depends on: PR #691 `L-100616`; `L-102001`
RH status: **not assumed**

The live double-owner framework already supplies the stable coefficient

\[
\pi_{ij}=r_ir_jL_iR_j,
\]

which is the literal probability that `i,j` are the least and greatest selected labels. Any valid conjunction must preserve this coefficient until after estimating the same collar occurrence.

For a real physical observation, `L-100616` gives

\[
(OE f)_-
\le\sum_{i<j}\pi_{ij}(H_{ij})_-.
\tag{L-102002.1}
\]

Suppose one can prove two source-faithful local certificates on each same interval occurrence,

\[
(H_{ij})_-^2\le A_{ij}B_{ij},
\tag{L-102002.2}
\]

where:

- `A_ij` is adapted to least-owner / future-prime structure;
- `B_ij` is adapted to greatest-owner / cofactor-largest-prime structure;
- neither deletes the outside survival factors encoded in `pi_ij`.

Then Cauchy--Schwarz on the joint min--max probability space yields

\[
\boxed{
(OE f)_-
\le
\left(\sum_{i<j}\pi_{ij}A_{ij}\right)^{1/2}
\left(\sum_{i<j}\pi_{ij}B_{ij}\right)^{1/2}.
}
\tag{L-102002.3}
\]

This is the correct implication-matrix conjunction. The divergent absolute marginal refutation `R-100616` does not apply because both survival factors remain attached to every occurrence.

## Parabolic specialization

For the balanced Vaughan large-divisor form `L-102001`, every active ordered divisor pair is asymptotically parabolic. The exact gcd coordinates

\[
d=ga,\qquad e=gb,\qquad(a,b)=1
\]

remove the common gcd sign but retain a coupled square dilation `g^2ab`.

Accordingly, a future composite-owner proof should not split into independent `g` and `(a,b)` estimates. Instead, for every same joint occurrence indexed by its outer min/max prime owners and its inner divisor coordinates, prove a product certificate of the form

\[
\boxed{
\text{collar}_{i,j,g,a,b,-}^2
\le
A_{i,j,g,a,b}^{\rm future}
B_{i,j,g,a,b}^{\rm cofactor}.
}
\tag{L-102002.4}
\]

The global estimate is then obtained only after summing with the literal joint owner weight.

## Open local targets

Define:

`JFC102002` — a least-owner/future-prime certificate on the same long partial-activation collar occurrence, using the parabolic width and finite interior squaring.

`JLC102002` — a greatest-owner/cofactor certificate on that same occurrence, using largest-prime ownership and positive divisor renewal.

If their joint weighted sums are subpower on logarithmic blocks, then `L-100616.7`, the zero-moment Vaughan reduction, and `L-100312` imply RH.

No claim that `JFC102002` or `JLC102002` is proved is made here. The advance is the exact logical correction: the conjunction must occur pointwise/sourcewise before owner summation, not by multiplying unrelated marginal norms.