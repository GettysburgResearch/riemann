# L-28001 — Dyadic bottom-charge collapse of the binary–ternary producer

Claim ID: `L-28001`  
Title: The Euler-aligned dyadic Möbius source annihilates every binary–ternary producer row above three  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #277 at `d5be8262c80a1debcf86922b45a4d00a406803f1`  
Dependencies: `L-23810/L-23811`; elementary Dirichlet convolution

## 1. Dyadic Euler-aligned source

Define

\[
\boxed{
b_2(q)=\mu(q)-\mathbf1_{2\mid q}\mu(q/2).}
\tag{L-28001.1}
\]

Its Dirichlet series is

\[
\boxed{
\sum_{q\ge1}\frac{b_2(q)}{q^s}
=\frac{1-2^{-s}}{\zeta(s)}.}
\tag{L-28001.2}
\]

Since

\[
\mathbf1*b_2=\varepsilon-\delta_2,
\]

finite divisor switching gives, for every real `x>=0`,

\[
\boxed{
\sum_{q\le x}b_2(q)\left\lfloor\frac{x}{q}\right\rfloor
=\mathbf1_{1\le x<2}.}
\tag{L-28001.3}
\]

For the carry indicator

\[
\chi_{n,j}(q)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor,
\]

substitution in (L-28001.3) yields the pointwise two-contact identity

\[
\boxed{
\sum_{q=1}^{n}b_2(q)\chi_{n,j}(q)
=-\mathbf1_{j=1}-\mathbf1_{j=n-1}.}
\tag{L-28001.4}
\]

No average, norm, or asymptotic estimate enters this formula.

## 2. Exact collapse on the declared producer rows

The equal binary–ternary producer uses

\[
j_2(n)=\lfloor n/2\rfloor,
\qquad
j_3(n)=\lceil n/3\rceil,
\]

and the averaged carry row

\[
\overline\chi_n(q)
=\frac12\chi_{n,j_2(n)}(q)
+\frac12\chi_{n,j_3(n)}(q).
\tag{L-28001.5}
\]

For `n>=4`, all four declared children are at least two.  Equation
(L-28001.4) therefore gives zero.  The two bottom rows are immediate.  Hence

\[
\boxed{
\sum_{q=1}^{n}b_2(q)\overline\chi_n(q)
=
\begin{cases}
-2,&n=2,\\
-1,&n=3,\\
0,&n\ge4.
\end{cases}}
\tag{L-28001.6}
\]

This is an exact source-image theorem: every producer row above three disappears.

## 3. Bottom-charge identity

Let `w(2),...,w(X)` be any finite target, with `w(1)=0`, and let `A_w(n)` be
the exact binary–ternary producer.  Its column identity is

\[
w(q)=\sum_{n=q}^{X}A_w(n)\overline\chi_n(q).
\tag{L-28001.7}
\]

Multiply by `b_2(q)` and sum.  Equation (L-28001.6) gives

\[
\boxed{
\sum_{q=2}^{X}b_2(q)w(q)
=-2A_w(2)-A_w(3).}
\tag{L-28001.8}
\]

For the critical target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

put

\[
\boxed{
\mathcal C_2(X)=2A_X(2)+A_X(3).}
\tag{L-28001.9}
\]

Then

\[
\boxed{
\mathcal C_2(X)
=-\sum_{q=2}^{X}\frac{b_2(q)}{\sqrt q}\log\frac Xq.}
\tag{L-28001.10}
\]

In the divergence coordinates of `L-23810`, the right side is `-r_X(1)`.
Thus `mathcal C_2` is literally the total unit-leaf charge of the declared
fragmentation.

Any nonnegative fragmentation producer necessarily has
`mathcal C_2(X)>=0`, but full producer positivity is much stronger than this
single scalar sign.

## 4. Direct Landau consumer

For real `x>=2`, define

\[
R_2(x)=
\sum_{2\le q\le x}
\frac{b_2(q)}{\sqrt q}\log\frac{x}{q}.
\tag{L-28001.11}
\]

Initially for `Re z` large, with `s=z+1/2`,

\[
\boxed{
\int_0^\infty e^{-zt}R_2(e^t)\,dt
=
\frac{(1-2^{-s})/\zeta(s)-1}{z^2}.}
\tag{L-28001.12}
\]

The `-1` removes the omitted coefficient `q=1`.

Suppose

\[
\boxed{
\mathcal C_2(N)\ge0
\quad\text{for every sufficiently large integer }N.}
\tag{L-28001.13}
\]

Then `R_2(N)<=0`.  Between consecutive integer knots the derivative of
`R_2(x)` is

\[
\frac1x\sum_{q\le N}\frac{b_2(q)}{\sqrt q},
\]

whose sign is constant on that interval.  The maximum on each interval is
therefore attained at an endpoint.  Thus (L-28001.13) implies

\[
R_2(x)\le0
\]

for every sufficiently large real `x`.

Apply Landau's one-sign theorem to `-R_2(e^t)`.  A positive abscissa of
convergence would have to be a singularity on the positive real `z`-axis.  The
right side of (L-28001.12) has no such singularity: zeta has no real zero in
`1/2<s<1`, and is zero-free for `s>1`.

Every hypothetical zeta zero `rho` with `Re rho>1/2` would, however, give an
uncancelled pole at

\[
z=\rho-1/2,
\]

because `1-2^{-rho}` cannot vanish there.  Hence no such zero exists.
Functional-equation symmetry gives RH.

Consequently

\[
\boxed{
\mathcal C_2(N)\ge0\text{ eventually}
\quad\Longrightarrow\quad
\mathrm{RH}.}
\tag{L-28001.14}
\]

## 5. Significance

The full binary–ternary positivity problem has collapsed to one bottom scalar:

\[
\boxed{2A_X(2)+A_X(3).}
\]

A proof need not control every producer coefficient, total variation, every
Abel kernel, or the complete carry LP.  It may attack this bottom charge through

- the Euler-aligned positive inverse and generalized Selberg equation;
- the factor-eighteen binary–ternary source of `L-28002`;
- the correct independent-frequency physical block;
- a direct digital or boundary-commutator argument.

## 6. Proof boundary

Proved exactly here:

1. the pointwise `b_2` two-contact identity;
2. annihilation of every declared producer row above three;
3. the bottom-charge formula for every finite target;
4. eventual nonnegativity of the bottom charge implies RH.

Open:

1. unconditional nonnegativity of `mathcal C_2(X)`;
2. RH.
