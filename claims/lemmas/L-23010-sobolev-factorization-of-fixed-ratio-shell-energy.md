# L-23010 — Sobolev factorization of fixed-ratio shell energy

Claim ID: `L-23010`  
Title: A fixed-ratio Mertens shell is the causal primitive of an explicit finite-Euler inverse coefficient, and every smoothed shell energy is an exact first-order Sobolev norm  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-23008`; PR #234 `L-23405`  
Scope: fixed ratios `c=1/p` with `p` prime, especially the dyadic ratio `1/2`

## 1. Causal shell window

For `0<c<1`, put

\[
L_c=\log(1/c)
\]

and define the causal shell window

\[
\boxed{
 w_c(u)=e^{-u/2}\mathbf 1_{[0,L_c)}(u).}
\tag{L-23010.1}
\]

Let

\[
\alpha_\mu=
\sum_{n\ge1}{\mu(n)\over\sqrt n}\,\delta_{\log n}.
\tag{L-23010.2}
\]

Then the normalized fixed-ratio Mertens shell is exactly

\[
\boxed{
 Q_c=w_c*\alpha_\mu.}
\tag{L-23010.3}
\]

Indeed the atom at `log n` contributes precisely when

\[
ce^t<n\le e^t.
\]

## 2. First-order boundary operator

In distributions,

\[
\boxed{
\left(\partial_u+\frac12\right)w_c
=\delta_0-\sqrt c\,\delta_{L_c}.}
\tag{L-23010.4}

Consequently

\[
\boxed{
\left(\partial_t+\frac12\right)Q_c
=
\left(\delta_0-\sqrt c\,\delta_{L_c}\right)*\alpha_\mu.}
\tag{L-23010.5}

When

\[
c={1\over p}
\]

for a prime `p`, the atom at `log m` on the right has coefficient

\[
{1\over\sqrt m}
\left[
\mu(m)-\mathbf 1_{p\mid m}\mu(m/p)
\right].
\]

Define

\[
\boxed{
 b_p(m)=\mu(m)-\mathbf1_{p\mid m}\mu(m/p).}
\tag{L-23010.6}

Then

\[
\boxed{
\left(\partial_t+\frac12\right)Q_{1/p}
=
\beta_p,
\qquad
\beta_p=\sum_{m\ge1}{b_p(m)\over\sqrt m}\delta_{\log m}.}
\tag{L-23010.7}

For `p=2`, this is exactly the Euler-aligned coefficient `b_2` of PR #234
`L-23405`.

## 3. Autocorrelation Green kernel

The whole-line autocorrelation of `w_c` is

\[
 h_c(v)=
\int_{\mathbb R}w_c(u)w_c(u-v)\,du.
\tag{L-23010.8}
\]

A direct calculation gives

\[
\boxed{
 h_c(v)=
\left(e^{-|v|/2}-c e^{|v|/2}\right)
\mathbf1_{|v|<L_c}.}
\tag{L-23010.9}

Equivalently,

\[
 h_c(v)=2\sqrt c\,
\sinh\!\left({L_c-|v|\over2}\right)_+.
\tag{L-23010.10}

Its Fourier transform is

\[
\boxed{
\widehat h_c(\xi)
=
{1+c-2\sqrt c\cos(L_c\xi)
 \over \xi^2+1/4}
=
{\left|1-\sqrt c\,e^{-iL_c\xi}\right|^2
 \over \xi^2+1/4}.}
\tag{L-23010.11}

Thus `h_c` is positive definite.  In distributions it is the Green kernel
identity

\[
\boxed{
\left(-\partial_v^2+\frac14\right)h_c
=(1+c)\delta_0
-\sqrt c\left(\delta_{L_c}+\delta_{-L_c}\right).}
\tag{L-23010.12}

The right side factors as

\[
\left(\delta_0-\sqrt c\,\delta_{L_c}\right)
*
\left(\delta_0-\sqrt c\,\delta_{-L_c}\right).
\]

## 4. Exact smoothed Sobolev identity

Let `g` be a compactly supported `C^1` test and define

\[
 q_c=g*Q_c,
\qquad
 r_c=g*\beta_p
\]

for `c=1/p`.  Convolution of (L-23010.7) gives

\[
\boxed{
 r_c=\left(\partial_t+\frac12\right)q_c.}
\tag{L-23010.13}

Because `q_c` has compact support at every finite arithmetic truncation, or
belongs to the corresponding damped Sobolev space after passage to the full
signal, integration by parts yields

\[
\boxed{
\|r_c\|_2^2
=
\|q_c'\|_2^2
+\frac14\|q_c\|_2^2.}
\tag{L-23010.14}

The mixed term has zero real part:

\[
2\operatorname{Re}\int q_c'\overline{q_c}
=
\int (|q_c|^2)'=0.
\]

In particular,

\[
\boxed{
\|q_c\|_2\le2\|r_c\|_2.}
\tag{L-23010.15}

The identity is exact, not a Poincare estimate.

## 5. Damped identity

For `sigma>=0`, put

\[
\widetilde q_c(t)=e^{-\sigma t}q_c(t).
\]

Then

\[
e^{-\sigma t}r_c(t)
=
\left(\partial_t+\sigma+\frac12\right)
\widetilde q_c(t),
\]

and hence

\[
\boxed{
\|e^{-\sigma\cdot}r_c\|_2^2
=
\|\widetilde q_c'\|_2^2
+\left(\sigma+\frac12\right)^2
\|\widetilde q_c\|_2^2.}
\tag{L-23010.16}

Therefore the shell and Euler-aligned derivative source have the same damped
Hardy abscissa.

## 6. Consequence for the final arithmetic theorem

For the dyadic shell, the remaining RH-equivalent estimate may be stated in
either of two exactly equivalent Sobolev coordinates:

\[
Q_{1/2}(t)
=e^{-t/2}[M(e^t)-M(e^t/2)]
\]

or

\[
\beta_2
=
\sum_n{b_2(n)\over\sqrt n}\delta_{\log n}.
\]

After a fixed compact smoothing, subexponential block energy of one is
equivalent to subexponential first-order Sobolev energy of the other.  The
coefficient `b_2` has:

- a bounded multiplicative local formula;
- positive inverse coefficients;
- positive generalized von Mangoldt weights;
- positive reflected Selberg forcing;
- the digital convolution identity of `L-23011`.

Thus the first-cell export and the shell primitive are no longer independent
obligations.  The final obstruction is the critical local energy of the
Euler-aligned atomic source itself.

## 7. Proof boundary

Closed exactly:

- the causal primitive identity;
- the explicit Euler-aligned derivative coefficient;
- the shell autocorrelation and Green equation;
- the undamped and damped Sobolev norm identities.

Open:

- a critical block bound for the smoothed `b_2` source;
- coercive inversion of the digital convolution kernel;
- RH.
