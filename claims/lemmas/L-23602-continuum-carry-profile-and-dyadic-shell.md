# L-23602 — Continuum carry profile and dyadic-shell bridge

Claim ID: `L-23602`  
Title: The sharp carry inverse is one explicit Möbius–Riesz profile, and its dyadic alignment is the fixed-ratio Mertens shell  
Status: **PROPOSED EXACT ANALYTIC REDUCTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-q`  
Created: 2026-08-07  
Dependencies: `L-23601`; PR #234 `L-23405`  
Scope: continuum scaling and exact transforms; positivity is separated into `L-23603`

## 1. Carry kernel

For `x>=1`, define

\[
\boxed{
K(x)=\frac{\lfloor x\rfloor(1-\{x\})}{x}.}
\tag{L-23602.1}
\]

If `n/X -> r` and `q/X -> s` with `0<s<=r<=1`, then

\[
\beta_{nq}=K(r/s)+O(X^{-1})
\]

away from the finite quotient boundaries. Thus the continuum positive-minorant
problem is

\[
\boxed{
\int_s^1D(r)K(r/s)\,dr
\le s^{-1/2}\log(1/s),
\qquad 0<s<=1,}
\tag{L-23602.2}
\]

with `D>=0`. Its entropy objective is

\[
\boxed{
\mathscr J(D)=\frac12\int_0^1rD(r)\,dr.}
\tag{L-23602.3}
\]

The constant dual density is sharp at the formal level because

\[
\boxed{
\int_1^\infty K(x)x^{-2}\,dx=\frac12.}
\tag{L-23602.4}
\]

Indeed the integral over `[m,m+1)` is `1/[2m(m+1)]`, and the sum telescopes.
Consequently every feasible `D` satisfies

\[
\mathscr J(D)\le
\int_0^1s^{-1/2}\log(1/s)\,ds=4.
\tag{L-23602.5}
\]

This is the source of the exact archimedean constant `4 sqrt(X)`.

## 2. Explicit inverse profile

Put, for `y>=1`,

\[
\boxed{
h(y)=8\sqrt y-7-\frac32\log y,}
\tag{L-23602.6}
\]

and set `h(y)=0` for `0<y<1`. Define

\[
\boxed{
\mathfrak C(y)
=\sum_{d\le y}\frac{\mu(d)}{\sqrt d}\,h(y/d).}
\tag{L-23602.7}
\]

Then the exact continuum inverse is

\[
\boxed{
D(r)=r^{-3/2}\mathfrak C(1/r).}
\tag{L-23602.8}
\]

Substitution into (L-23602.2), followed by multiplicative convolution, proves
that equality holds in (L-23602.2) whenever the sums and integrals are initially
taken in their absolute-convergence half-plane. Equivalently, in logarithmic
coordinates the carry equation is a causal Volterra convolution.

## 3. Mellin transform

For `Re z>1/2`,

\[
\boxed{
\int_1^\infty\mathfrak C(y)y^{-z-1}\,dy
=\frac{(z+\frac12)(z+\frac32)}
 {z^2(z-\frac12)\zeta(z+\frac12)}.}
\tag{L-23602.9}
\]

The proof uses

\[
\int_1^\infty h(y)y^{-z-1}dy
=\frac{(z+\frac12)(z+\frac32)}
 {z^2(z-\frac12)}
\]

and the Dirichlet series for `1/zeta(z+1/2)`.

Thus a nonnegative profile of subpower growth would exclude every zero with
`Re rho>1/2` by Landau's one-sign theorem. The positivity theorem is therefore
allowed to be elementary, but it is not allowed to be phase blind: it contains
the full RH burden.

## 4. Scaling of the finite inverse

Let `X_j,n_j -> infinity` with

\[
X_j/n_j\to y>1
\]

and suppose `y` is not an integer quotient boundary. The exact inverse
(L-23601.10), with one Euler expansion of its finite tail, gives

\[
\boxed{
 n_j^{3/2}c_{X_j}(n_j)\longrightarrow\mathfrak C(y).}
\tag{L-23602.10}
\]

The convergence is locally uniform on compact subintervals avoiding the
positive integers. The one-sided limits at an integer differ by the explicit
jump `mu(m)/sqrt(m)` inherited from (L-23602.7).

This proves that full Carry Saturation cannot be established by an argument
which misses a negative value of `mathfrak C`: such a value would generate a
macroscopic family of negative finite coefficients.

## 5. Dyadic Euler alignment

Define the fixed-ratio shell coefficient

\[
\boxed{
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2),}
\tag{L-23602.11}
\]

so that

\[
\sum_{n\ge1}\frac{b_2(n)}{n^s}
=\frac{1-2^{-s}}{\zeta(s)}.
\tag{L-23602.12}
\]

Put

\[
H(y)=\sqrt y\,h(y)
=8y-7\sqrt y-\frac32\sqrt y\log y
\tag{L-23602.13}
\]

for `y>=1`, and

\[
\boxed{
H_2(y)=\sum_{j\ge0}H(y/2^j),}
\tag{L-23602.14}
\]

where the sum is finite. Then

\[
\boxed{
\sqrt y\,\mathfrak C(y)
=\sum_{n\le y}b_2(n)H_2(y/n).}
\tag{L-23602.15}
\]

This is simply the factorization

\[
\frac1{\zeta(s)}
=\frac{1-2^{-s}}{\zeta(s)}\cdot\frac1{1-2^{-s}},
\]

but it is load bearing: the carry profile and the dyadic Mertens shell are the
same source in two Green gauges.

PR #234 proves that `b_2` has the positive inverse

\[
a_2(n)=v_2(n)+1,
\]

the nonnegative generalized prime sequence

\[
\Lambda_2^\#(n)
=\Lambda(n)+(\log2)\mathbf1_{n=2^k},
\]

and the exact reflected Selberg forcing

\[
b_2*(a_2\log^2)
=\Lambda_2^\#\log+\Lambda_2^\#*\Lambda_2^\#.
\tag{L-23602.16}
\]

The right side is coefficientwise nonnegative. `L-23603` uses this identity
before any absolute value is taken.

## 6. Finite minorants from the continuum profile

Assume `mathfrak C>=0`. For a slowly increasing cutoff `Y_X`, sample the
profile

\[
D_X(r)=r^{-3/2}\mathfrak C(1/r)\mathbf1_{r\ge1/Y_X}
\]

on the integer mesh, shrink it by the explicit Euler error, and call the
resulting coefficients `d_X(n)`. Bounded variation of the carry cells gives

\[
\sum_{n=q}^Xd_X(n)\beta_{nq}\le w_X(q)
\]

for every `q`, while

\[
\frac12\sum_n n d_X(n)
=4\sqrt X+O(\log^2X)
-O\!\left(\sqrt{X/Y_X}\log Y_X\right).
\]

Taking `Y_X=X/(log X)^A` with fixed large `A` makes the omitted contribution
polylogarithmic. The lower-order coefficient mass is also `O(log^2 X)`.

The complete directed discretization ledger is stated in `T-23601`; no exact
finite coefficient positivity is required.

## 7. Proof boundary

Closed here:

- the continuum carry operator and sharp dual constant;
- the explicit Möbius profile and Mellin transform;
- finite-to-continuum scaling;
- the exact dyadic-shell identity;
- the interface from profile positivity to a near-saturating finite minorant.

Open in this file:

- positivity of `mathfrak C`;
- the reflected quotient-layer factorization proving that positivity;
- RH.
