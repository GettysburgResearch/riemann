# L-26202 — Parity renewal and Peano B-spline expansion

Claim ID: `L-26202`  
Title: The aligned carry source obeys an exact parity renewal, and every paired remainder has a valid positive Peano B-spline representation  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26201`  
Scope: exact renewal and boundary expansion; no contraction asserted

## 1. Exact finite-forcing renewal

Retain the aligned source `b_R`, finite coefficient sequence `d_R`, and positive
causal Green kernel `q_R` of `L-26201`. Put

\[
 U_R(t)=\sum_{n\ge1}\frac{b_R(n)}{\sqrt n}
 q_R(t-\log n)
 \tag{L-26202.1}
\]

and

\[
 Q_R^{\partial}(t)=
 \sum_{n\ge1}\frac{d_R(n)}{\sqrt n}
 q_R(t-\log n).
 \tag{L-26202.2}
\]

The second sum is finite because `d_R` is supported on finitely many powers of
two. From

\[
 \varepsilon*b_R=d_R,
 \qquad \varepsilon(k)=(-1)^{k+1},
\]

one obtains the exact causal renewal

\[
 \boxed{
 Q_R^{\partial}(t)
 =\sum_{k\ge1}\frac{(-1)^{k+1}}{\sqrt k}
 U_R(t-\log k).}
 \tag{L-26202.3}
\]

At each fixed `t` the sum is finite.

## 2. Adjacent-pair boundary transport

Separate the `k=1` term and pair every even integer with its following odd
integer. Equation (L-26202.3) becomes

\[
\boxed{
\begin{aligned}
 U_R(t)=Q_R^{\partial}(t)
 +\sum_{m\ge1}\Bigg[&
 \frac{U_R(t-\log(2m))}{\sqrt{2m}}\\
 &-\frac{U_R(t-\log(2m+1))}{\sqrt{2m+1}}
 \Bigg].
\end{aligned}}
\tag{L-26202.4}
\]

For

\[
 A_t(x)=x^{-1/2}U_R(t-\log x),
 \tag{L-26202.5}
\]

ordinary differentiation gives

\[
 -A_t'(x)
 =x^{-3/2}
 (\partial_t+\tfrac12)U_R(t-\log x).
 \tag{L-26202.6}
\]

Therefore every paired bracket is an exact boundary integral and

\[
 \boxed{
 U_R(t)=Q_R^{\partial}(t)
 +\int_{\mathcal E}
 x^{-3/2}(\partial_t+\tfrac12)
 U_R(t-\log x)\,dx,}
 \tag{L-26202.7}
\]

where

\[
 \mathcal E=\bigcup_{m\ge1}[2m,2m+1].
 \tag{L-26202.8}
\]

This is a signed boundary-transport identity. It is not a Hankel
representation.

The positive transport mass is

\[
\begin{aligned}
 \kappa
 &=\int_{\mathcal E}x^{-3/2}dx\\
 &=2\sum_{m\ge1}
 \left((2m)^{-1/2}-(2m+1)^{-1/2}\right)\\
 &=2\left(1-\eta(\tfrac12)\right).
\end{aligned}
 \tag{L-26202.9}
\]

The alternating-series lower bound obtained from the first twenty-four terms
is strictly larger than `1/2`. Hence

\[
 \boxed{0<\kappa<1.}
 \tag{L-26202.10}
\]

The exact checker on this branch verifies a rational lower enclosure for that
finite alternating sum.

Equation (L-26202.10) is only a reserve in a derivative graph norm. It does not
by itself imply pointwise or `L2` contraction of `U_R`.

## 3. Exact finite Euler transformation

For a finite-support sequence `a=(a_1,a_2,...)`, define

\[
 (\Delta a)_n=a_n-a_{n+1}.
 \tag{L-26202.11}
\]

The alternating functional

\[
 \mathcal A(a)=\sum_{n\ge1}(-1)^{n+1}a_n
 \tag{L-26202.12}
\]

satisfies

\[
 \mathcal A(a)=\frac{a_1}{2}
 +\frac12\mathcal A(\Delta a).
 \tag{L-26202.13}
\]

Iterating gives, for every integer `M>=1`,

\[
 \boxed{
 \mathcal A(a)
 =\sum_{j=0}^{M-1}2^{-j-1}(\Delta^ja)_1
 +2^{-M}\mathcal A(\Delta^Ma).}
 \tag{L-26202.14}
\]

This is an exact identity, not an asymptotic Euler acceleration.

Apply it to the tail sequence

\[
 a_n(t)=n^{-1/2}U_R(t-\log n),
 \qquad n\ge2.
 \tag{L-26202.15}
\]

Since (L-26202.4) is `U_R=Q_R^partial+mathcal A(a)`, one obtains

\[
 \boxed{
\begin{aligned}
 U_R(t)={}&Q_R^{\partial}(t)
 +\sum_{j=0}^{M-1}2^{-j-1}
  \Delta^j\!\left[n^{-1/2}U_R(t-\log n)
  \right]_{n=2}\\
 &+2^{-M}\mathcal A\!\left(
  \Delta^M[n^{-1/2}U_R(t-\log n)]_{n\ge2}
  \right).
\end{aligned}}
 \tag{L-26202.16}
\]

Every nonforcing term on the right is delayed by at least `log 2`.

## 4. Valid Peano B-spline formula

Let `\mathsf B_j` be the cardinal B-spline of order `j`, equivalently the
probability density of the sum of `j` independent uniform variables on
`[0,1]`. It is nonnegative, supported on `[0,j]`, and has integral one.

For

\[
 A_t(x)=x^{-1/2}U_R(t-\log x),
\]

one has

\[
 \boxed{
 (-1)^jA_t^{(j)}(x)
 =x^{-j-1/2}
 \prod_{\ell=0}^{j-1}
 (\partial_t+\ell+\tfrac12)
 U_R(t-\log x).}
 \tag{L-26202.17}
\]

The Peano formula for finite differences therefore gives

\[
 \boxed{
\begin{aligned}
 \Delta^j A_t(n)
 =\int_0^j&\mathsf B_j(u)(n+u)^{-j-1/2}\\
 &\times
 \prod_{\ell=0}^{j-1}
 (\partial_t+\ell+\tfrac12)
 U_R(t-\log(n+u))\,du.
\end{aligned}}
 \tag{L-26202.18}
\]

This is the replacement for the false conditional-Hankel step. Positivity is
used only for the one-variable Peano B-spline weight. No claim is made that a
kernel of the form `f(x+y)` is positive semidefinite.

## 5. Source-specific reflected remainder

The only term in (L-26202.16) not reduced to finitely many explicit boundary
columns is

\[
 \boxed{
 \mathscr R_{R,M}(t)
 =\mathcal A\!\left(
 \Delta^M[n^{-1/2}U_R(t-\log n)]_{n\ge2}
 \right).}
 \tag{L-26202.19}
\]

Its coefficient sequence is the actual aligned inverse-zeta source. It must be
estimated after exact reflected recombination, not by an arbitrary-vector
operator norm or entrywise absolute values.

`L-26203` states the one source-specific graph estimate that would turn the
factor `2^{-M}` in (L-26202.16) into a strict lower-scale contraction.

## 6. Proof boundary

Closed exactly:

- the finite-forcing parity renewal;
- adjacent-pair boundary transport;
- the strict mass reserve `kappa<1`;
- the finite Euler identity;
- the positive Peano B-spline representation;
- strict delay of every nonforcing column.

Open:

- a source-specific reflected bound for `mathscr R_(R,M)` and the finite graph
  columns;
- a cofinal block-energy recurrence;
- RH.
