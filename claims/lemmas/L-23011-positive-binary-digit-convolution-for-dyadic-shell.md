# L-23011 — Positive binary-digit convolution for the dyadic shell

Claim ID: `L-23011`  
Title: The dyadic Euler-aligned shell coefficient has an explicit positive causal convolution inverse whose summatory values are binary digit sums  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: PR #234 `L-23405/L-23406`; `L-23010`  
Scope: the dyadic shell `c=1/2`

## 1. Euler-aligned coefficients

Define

\[
 b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2)
\tag{L-23011.1}
\]

and

\[
 c_2(n)=1-v_2(n).
\tag{L-23011.2}

Their Dirichlet series are

\[
B_2(s)={1-2^{-s}\over\zeta(s)},
\tag{L-23011.3}
\]

\[
C_2(s)=
\zeta(s){1-2^{1-s}\over1-2^{-s}}.
\tag{L-23011.4}
\]

Therefore

\[
\boxed{
C_2(s)B_2(s)=1-2^{1-s}.}
\tag{L-23011.5}

Equivalently, coefficientwise,

\[
\boxed{
 c_2*b_2=d_2,}
\tag{L-23011.6}

where

\[
 d_2(1)=1,
\qquad
 d_2(2)=-2,
\qquad
 d_2(n)=0\ (n\ne1,2).
\tag{L-23011.7}

## 2. Exact binary digit partial sums

Let `s_2(N)` be the sum of the binary digits of the nonnegative integer `N`.
Legendre's identity

\[
\sum_{n\le N}v_2(n)=v_2(N!)=N-s_2(N)
\]

gives

\[
\boxed{
\sum_{n\le N}c_2(n)=s_2(N).}
\tag{L-23011.8}

In particular,

\[
0\le s_2(N)\le1+\log_2N.
\tag{L-23011.9}

The increment identity is

\[
\boxed{
 s_2(n)-s_2(n-1)=1-v_2(n)=c_2(n).}
\tag{L-23011.10}

## 3. Positive causal digit kernel

Define

\[
\boxed{
 S_2(t)=
 e^{-t/2}s_2(\lfloor e^t\rfloor),}
\tag{L-23011.11}

with `s_2(0)=0`.  Then

\[
 S_2(t)\ge0
\]

and

\[
 S_2\in L^1(\mathbb R)\cap L^2(\mathbb R)
\tag{L-23011.12}

by (L-23011.9).

Between its jump points, `S_2'=-S_2/2`; at `t=log n` its jump is

\[
{c_2(n)\over\sqrt n}.
\]

Thus, in distributions,

\[
\boxed{
\left(\partial_t+\frac12\right)S_2
=\kappa_2,
\qquad
\kappa_2=
\sum_{n\ge1}{c_2(n)\over\sqrt n}\delta_{\log n}.}
\tag{L-23011.13}

## 4. Exact convolution with the dyadic shell source

Let

\[
\beta_2=
\sum_{n\ge1}{b_2(n)\over\sqrt n}\delta_{\log n}.
\tag{L-23011.14}

Dirichlet convolution becomes additive convolution of the normalized atomic
measures. Equations (L-23011.6)--(L-23011.7) give

\[
\boxed{
\kappa_2*\beta_2
=\delta_0-\sqrt2\,\delta_{\log2}.}
\tag{L-23011.15}

Convolving (L-23011.13) with `beta_2`,

\[
\left(\partial_t+\frac12\right)(S_2*\beta_2)
=\delta_0-\sqrt2\,\delta_{\log2}.
\tag{L-23011.16}

Let

\[
 w_\infty(t)=e^{-t/2}\mathbf1_{t\ge0}.
\]

Since

\[
\left(\partial_t+\frac12\right)w_\infty=\delta_0,
\]

the unique causal solution of (L-23011.16) is

\[
\boxed{
S_2*\beta_2
=w_\infty-\sqrt2\,\tau_{\log2}w_\infty.}
\tag{L-23011.17}

Explicitly,

\[
\boxed{
(S_2*\beta_2)(t)=
\begin{cases}
0,&t<0,\\
e^{-t/2},&0\le t<\log2,\\
-e^{-t/2},&t\ge\log2.
\end{cases}}
\tag{L-23011.18}

Thus the full dyadic Möbius shell source is inverted by one nonnegative,
integrable, completely explicit binary-digit kernel, up to the two-tap causal
boundary source on the right.

## 5. Relation to the shell primitive

By `L-23010`,

\[
\left(\partial_t+\frac12\right)Q_{1/2}=\beta_2.
\tag{L-23011.19}

Consequently

\[
\boxed{
S_2*
\left(\partial_t+\frac12\right)Q_{1/2}
=
 w_\infty-\sqrt2\,\tau_{\log2}w_\infty.}
\tag{L-23011.20}

After convolution with any fixed compact smooth test, every term is an ordinary
`L2` function and the equality is exact.

The right-hand side is elementary and exponentially decaying.  The entire
arithmetic difficulty has therefore been moved into stable inversion of one
positive causal kernel `S_2`.

## 6. Transform and zero geometry

The bilateral Laplace transform of (L-23011.13) gives

\[
\boxed{
\widehat S_2(z)=
{C_2(z+1/2)\over z+1/2}}
\tag{L-23011.21}

initially in its convergence half-plane and thereafter by continuation.
Equation (L-23011.17) becomes

\[
\widehat S_2(z)B_2(z+1/2)
={1-2^{1/2-z}\over z+1/2}.
\tag{L-23011.22}

The positivity and integrability of `S_2` do not make its convolution inverse
bounded on the critical identity orbit.  Its transform contains the factor
`zeta(z+1/2)`, and its complex zero/pole geometry is precisely where the
rightmost-zero obstruction can re-enter.

Thus (L-23011.17) is a strong exact first-kind equation but not, by itself, a
coercive inverse estimate.

## 7. Proof-facing completion target

A full proof would follow from any one of the following source-specific
statements:

1. a critical weighted `L2` lower bound
   \[
   \|S_2*f\|_2\ge e^{-o(J)}\|f\|_2
   \]
   on the actual dyadic shell packets at scale `J`;
2. a Wiener--Hopf factorization of `S_2` whose unstable factor is shown absent
   by an independent positive arithmetic argument;
3. a one-sided reflected Selberg identity proving the required lower bound only
   for `f=(partial+1/2)Q_(1/2)`;
4. an exact martingale representation of the binary-digit kernel with a
   conditional-variance reserve dominating the shell source.

A generic inverse theorem is impossible if RH is false and would be circular.
The target must exploit the actual coefficient vector `b_2`.

## 8. Proof boundary

Closed exactly:

- the binary digit partial-sum identity;
- positivity and integrability of the digit kernel;
- its distributional derivative;
- the exact normalized Dirichlet/additive convolution;
- the explicit two-tap causal output.

Open:

- a critical coercivity estimate for convolution by `S_2` on the actual shell
  source;
- the dyadic shell energy theorem;
- RH.
