# L-23008 — Causal transfer between all fixed-ratio Mertens shells

Claim ID: `L-23008`  
Title: Every normalized fixed-ratio Mertens shell is an absolutely summable causal translate filter of every other one  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: elementary telescoping of the Mertens function  
Scope: scalar fixed-ratio shell signals; no estimate for any one shell is assumed

## 1. Shell signals

Extend

\[
M(x)=\sum_{n\le x}\mu(n)
\]

by `M(x)=0` for `0<=x<1`.  For a fixed ratio

\[
0<c<1
\]

define

\[
I_c(x)=M(x)-M(cx),
\tag{L-23008.1}
\]

\[
Q_c(t)=e^{-t/2}I_c(e^t),
\qquad t\in\mathbb R,
\tag{L-23008.2}
\]

and

\[
a_c=\log(1/c)>0.
\tag{L-23008.3}
\]

The function `Q_c` vanishes for all sufficiently negative `t`.

## 2. Exact geometric reconstruction

Fix another ratio `0<d<1`.  Pointwise, the sum

\[
\sum_{k\ge0}I_d(d^kx)
\]

is finite and telescopes:

\[
\boxed{
M(x)=\sum_{k\ge0}I_d(d^kx).}
\tag{L-23008.4}
\]

Indeed, its first `N+1` terms equal

\[
M(x)-M(d^{N+1}x),
\]

and the last term is zero once `d^(N+1)x<1`.

Subtracting (L-23008.4) at `x` and `cx` gives

\[
\boxed{
I_c(x)=
\sum_{k\ge0}
\left[I_d(d^kx)-I_d(cd^kx)\right].}
\tag{L-23008.5}
\]

Again the sum is pointwise finite.

## 3. Normalized causal filter

Let

\[
(\tau_uF)(t)=F(t-u),
\qquad u\ge0.
\]

Substituting `x=e^t` into (L-23008.5) and applying the square-root normalization gives

\[
\boxed{
Q_c
=
\sum_{k\ge0}d^{k/2}
\left[
 \tau_{ka_d}Q_d
 -\sqrt c\,\tau_{a_c+ka_d}Q_d
\right].}
\tag{L-23008.6}

Thus

\[
Q_c=\nu_{c\leftarrow d}*Q_d
\tag{L-23008.7}
\]

for the causal signed atomic measure

\[
\boxed{
\nu_{c\leftarrow d}
=
\sum_{k\ge0}d^{k/2}
\left(
 \delta_{ka_d}-\sqrt c\,\delta_{a_c+ka_d}
\right).}
\tag{L-23008.8}

Its total variation satisfies

\[
\boxed{
\|\nu_{c\leftarrow d}\|_{\rm TV}
\le {1+\sqrt c\over1-\sqrt d}.}
\tag{L-23008.9}

Interchanging `c` and `d` gives the inverse causal representation

\[
Q_d=\nu_{d\leftarrow c}*Q_c.
\tag{L-23008.10}

The two filters are inverse on the actual shell range because both were derived from the exact telescoping identity, not from a formal division of transforms.

## 4. Transform check

On every right half-plane on which the transforms converge, the multiplier of
(L-23008.8) is

\[
\begin{aligned}
\widehat\nu_{c\leftarrow d}(z)
&=
\sum_{k\ge0}d^{k(z+1/2)}
\left(1-c^{z+1/2}\right)\\
&=\boxed{
{1-c^{z+1/2}\over1-d^{z+1/2}}.}
\end{aligned}
\tag{L-23008.11}

This is exactly the quotient of the two shell-window multipliers

\[
{(1-c^{z+1/2})/(z+1/2)
 \over
 (1-d^{z+1/2})/(z+1/2)}.
\]

The apparent zeros of the denominator in (L-23008.11) are harmless in the causal identity: they are common boundary-lattice zeros of the shell windows, and the pointwise series (L-23008.6) is the primary definition.

## 5. Cumulative energy comparison

Put

\[
\mathcal A_c(X)=
\int_{-\infty}^{X}|Q_c(t)|^2dt.
\tag{L-23008.12}

Every shift in (L-23008.6) is causal.  Minkowski's inequality therefore gives

\[
\begin{aligned}
\mathcal A_c(X)^{1/2}
&\le
\sum_{k\ge0}d^{k/2}
\left[
 \mathcal A_d(X-ka_d)^{1/2}
 +\sqrt c\,\mathcal A_d(X-a_c-ka_d)^{1/2}
\right]\\
&\le
{1+\sqrt c\over1-\sqrt d}\,
\mathcal A_d(X)^{1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal A_c(X)
\le
\left({1+\sqrt c\over1-\sqrt d}\right)^2
\mathcal A_d(X).}
\tag{L-23008.13}

The reverse comparison is

\[
\boxed{
\mathcal A_d(X)
\le
\left({1+\sqrt d\over1-\sqrt c}\right)^2
\mathcal A_c(X).}
\tag{L-23008.14}

The constants are independent of `X`.

## 6. Damped Hardy comparison

For `sigma>=0`, suppose one of the two damped signals lies in `L^2(R)`.  Multiplying (L-23008.6) by `e^(-sigma t)` gives an `L1` convolution with norm at most

\[
\boxed{
{1+c^{\sigma+1/2}\over1-d^{\sigma+1/2}}.}
\tag{L-23008.15}

Consequently

\[
\boxed{
\|e^{-\sigma\cdot}Q_c\|_2
\le
{1+c^{\sigma+1/2}\over1-d^{\sigma+1/2}}
\|e^{-\sigma\cdot}Q_d\|_2,}
\tag{L-23008.16}

with the symmetric reverse inequality after interchanging the ratios.

Thus all fixed-ratio shell signals have exactly the same Hardy abscissa.

## 7. Pointwise square-root transfer

If, for one fixed ratio `d` and every `epsilon>0`,

\[
I_d(x)=O_\epsilon(x^{1/2+\epsilon}),
\]

then (L-23008.5) gives

\[
\boxed{
I_c(x)=O_\epsilon(x^{1/2+\epsilon})}
\tag{L-23008.17}

for every fixed `c`, with the explicit geometric factor

\[
{1+c^{1/2+\epsilon}\over1-d^{1/2+\epsilon}}.
\]

The converse is symmetric.

## 8. Proof boundary

Closed exactly:

- pointwise finite reconstruction of every shell from every other shell;
- causal `ell^1` transfer in the square-root normalization;
- two-sided cumulative-energy comparison;
- equality of all damped Hardy abscissae;
- transfer of the square-root pointwise estimate.

Not closed:

- a subexponential estimate for one shell;
- the Euler-aligned dyadic shell recurrence;
- RH.
