# L-23405 — Euler-aligned dyadic shell and positive Selberg coefficients

Claim ID: `L-23405`  
Title: At ratio one half, the Mertens shell is the summatory function of a bounded multiplicative inverse with one squared Euler factor and a nonnegative generalized Selberg forcing  
Status: **PROPOSED — COMPLETE DIRICHLET-COEFFICIENT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: `L-23401/T-23401`; the general Selberg coefficient identity of PR #226 `L-9516`  
Scope: the distinguished ratio `c=1/2`

## 1. The dyadic shell is a summatory multiplicative function

Define

\[
\boxed{
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2).}
\tag{L-23405.1}

Then, for every real `x>=1`,

\[
\boxed{
M(x)-M(x/2)=\sum_{n\le x}b_2(n).}
\tag{L-23405.2}

Its Dirichlet series is

\[
\boxed{
B_2(s)=\sum_{n\ge1}{b_2(n)\over n^s}
={1-2^{-s}\over\zeta(s)},
\qquad\Re s>1.}
\tag{L-23405.3}

Thus the fixed-ratio shell multiplier is itself one finite Euler modification of `1/zeta`.

The function `b_2` is multiplicative. Writing

\[
n=2^\nu m,
\qquad m\text{ odd},
\]

one has

\[
\boxed{
b_2(2^\nu m)=
\begin{cases}
\mu(m),&\nu=0,\\
-2\mu(m),&\nu=1,\\
\mu(m),&\nu=2,\\
0,&\nu\ge3.
\end{cases}}
\tag{L-23405.4}

Equivalently, its local Euler factor at `2` is

\[
(1-2^{-s})^2,
\]

while at every odd prime it is `1-p^(-s)`.

## 2. Positive inverse coefficients

Put

\[
\boxed{
A_2(s)=B_2(s)^{-1}
={\zeta(s)\over1-2^{-s}}.}
\tag{L-23405.5}

Then

\[
A_2(s)=\sum_{n\ge1}{a_2(n)\over n^s},
\qquad
\boxed{a_2(n)=v_2(n)+1.}
\tag{L-23405.6}

In particular,

\[
a_2(n)\ge1
\]

for every positive integer, and

\[
\boxed{a_2*b_2=\varepsilon.}
\tag{L-23405.7}

The dyadic shell therefore has an inverse Dirichlet series with completely nonnegative coefficients.

## 3. Positive generalized von Mangoldt sequence

Define `Lambda_2^#` by

\[
-\frac{A_2'}{A_2}(s)
=\sum_{n\ge1}{\Lambda_2^\#(n)\over n^s}.
\]

Since

\[
\log A_2(s)=\log\zeta(s)-\log(1-2^{-s}),
\]

one obtains

\[
\boxed{
\Lambda_2^\#(n)
=\Lambda(n)+
(\log2)\mathbf1_{\{n=2^k,\ k\ge1\}}.}
\tag{L-23405.8}

Thus

\[
\Lambda_2^\#(n)\ge0.
\]

At every power of two its value is `2 log 2`; at every other prime power it equals the ordinary von Mangoldt weight.

## 4. Exact first and second logarithmic identities

Dirichlet differentiation of `B_2=A_2^(-1)` gives

\[
\boxed{
b_2\log=-\Lambda_2^\#*b_2.}
\tag{L-23405.9}

Differentiating again gives

\[
\boxed{
b_2\log^2
=\Lambda_2^\#*\Lambda_2^\#*b_2
 -(\Lambda_2^\#\log)*b_2.}
\tag{L-23405.10}

These are coefficientwise identities. They are the dyadic-shell versions of the centered prime-renewal and second-order Type-II equations.

## 5. Positive Selberg coefficient identity

Apply the general identity

\[
b*(a\log^2)=\Lambda_A\log+\Lambda_A*\Lambda_A
\]

to `A_2` and its inverse `B_2`. One obtains

\[
\boxed{
b_2*(a_2\log^2)
=\Lambda_2^\#\log
 +\Lambda_2^\#*\Lambda_2^\#.}
\tag{L-23405.11}

Every coefficient on the right is nonnegative.

This is stronger algebraic structure than the generic ratio `c=2/3`:

- the shell source is multiplicative;
- the inverse coefficients are positive;
- the generalized prime weights are positive;
- the complete Selberg forcing is coefficientwise positive.

It does not by itself bound the partial sums of `b_2` at square-root scale.

## 6. Reflected Hermitian square

Twist `A_2` by `n^(+-it)` and apply the conjugate-product subtraction of `L-9516`. The linear terms cancel and give

\[
\boxed{
2\left|{A_2'\over A_2}(\sigma+it)\right|^2
=\mathcal C_{2,\times}(\sigma,t)
 -\mathcal C_{2,+}(\sigma,t)
 -\mathcal C_{2,-}(\sigma,t),}
\tag{L-23405.12}

where all three coefficient packets are generated from the explicit nonnegative sequences `a_2` and `Lambda_2^#`, together with the signed inverse `b_2`.

Since

\[
B_2'=-(A_2'/A_2)B_2,
\]

multiplying (L-23405.12) by `|B_2|^2` produces the positive derivative energy

\[
\boxed{
2|B_2'(\sigma+it)|^2.}
\tag{L-23405.13}

At coefficient level, this multiplication is the complete reflected convolution with the actual `b_2` pair. No arbitrary packet vector is introduced.

A successful use must keep that complete convolution until the Hermitian square is assembled; a terminal-only or rowwise estimate loses the shell source.

## 7. Dyadic shell RH criterion

By `T-23401`, for every fixed `B>0`,

\[
\boxed{
\mathrm{RH}
\iff
\int_J^{J+B}
 e^{-t}|M(e^t)-M(e^t/2)|^2dt
=e^{o(J)}.}
\tag{L-23405.14}

Equivalently, this is the fixed-block energy of the summatory multiplicative function `b_2`.

The new Selberg identities make `c=1/2` the preferred arithmetic ratio for a source-specific reflected proof, while `c=2/3` remains the mandatory first-Farey mutation.

A complete proposal must provide an exact bounded transform between the two shell ratios or prove the dyadic criterion directly and invoke `T-23401`.

## 8. Proof boundary

Closed exactly:

- the multiplicative coefficient formula;
- the positive inverse coefficients;
- the generalized von Mangoldt sequence;
- the first and second logarithmic identities;
- the positive Selberg forcing;
- the reflected derivative-square interface.

Open:

- a critical block upper bound for the dyadic shell;
- a reflected forcing estimate retaining the full `b_2` convolution;
- RH.
