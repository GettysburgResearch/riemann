# L-93272 - Exact polynomially conditioned transform from centered cubic scale fields to First-Hermite heat

Claim ID: `L-93272`
Status: **PROPOSED COMPLETE EXACT FOURIER-TRANSFORM THEOREM - INDEPENDENT REVIEW REQUIRED**
Created: 2026-08-16
Depends on: PR #379 at `589f1c05ccaf248cf08c87fefa7d5ab6d2380708`; PR #531; `L-93271`
Scope: exact transform between prime fields; no pointwise prime cancellation theorem

## 1. Fourier convention

Use

\[
\widehat f(\xi)=\int_{\mathbb R}f(v)e^{-i\xi v}\,dv,
\qquad
f(v)=\frac1{2\pi}\int_{\mathbb R}\widehat f(\xi)e^{i\xi v}\,d\xi.
\tag{L-93272.1}
\]

Let `W_C` be the centered-cubic kernel of PR #531 and put

\[
k_C(v)=e^{-v/2}W_C(e^{-v})\mathbf1_{v\ge0}.
\tag{L-93272.2}
\]

The change of variables `x=e^{-v}` gives

\[
\boxed{
\widehat k_C(\xi)
=\widehat W_C\left(\frac12+i\xi\right).
}
\tag{L-93272.3}
\]

Using

\[
\widehat W_C(s)
=\frac{(1-4^{1-s})(s-1)}{3(s+1)(s+2)(s+3)},
\tag{L-93272.4}
\]

we see that `widehat k_C(xi)` never vanishes on the real axis. Indeed,

\[
\left|4^{1-(1/2+i\xi)}\right|=2\ne1,
\tag{L-93272.5}
\]

and `1/2+i xi` is not `1,-1,-2,-3`. Moreover

\[
\boxed{
|\widehat k_C(\xi)|\asymp (1+|\xi|)^{-2}.
}
\tag{L-93272.6}
\]

## 2. The First-Hermite kernel

For `q>=1`, define

\[
h_q(v)=\left(1-\frac{v^2}{2q}\right)e^{-v^2/(4q)}.
\tag{L-93272.7}
\]

Two differentiations of the Gaussian transform give

\[
\boxed{
\widehat h_q(\xi)
=4\sqrt\pi\,q^{3/2}\xi^2e^{-q\xi^2}.
}
\tag{L-93272.8}
\]

Let

\[
\widetilde k_C(v)=k_C(-v)
\tag{L-93272.9}
\]

and define `A_q` by

\[
\boxed{
\widehat A_q(\xi)
=\frac{\widehat h_q(\xi)}{\widehat k_C(-\xi)}.
}
\tag{L-93272.10}
\]

The denominator has no real zero and its reciprocal has only quadratic polynomial growth. Therefore `A_q` is a real Schwartz function and

\[
\boxed{h_q=A_q*\widetilde k_C.}
\tag{L-93272.11}
\]

The scaling estimate is

\[
\boxed{\|A_q\|_2^2\ll q^{1/2}.}
\tag{L-93272.12}
\]

To see this, use (L-93272.6) in (L-93272.10):

\[
|\widehat A_q(\xi)|
\ll q^{3/2}|\xi|^2(1+\xi^2)e^{-q\xi^2},
\tag{L-93272.13}
\]

then integrate the Gaussian moments and apply Plancherel.

## 3. Prime-field identity

For real carrier `t`, define the centered-cubic scale field

\[
\mathcal F_C(r,t)
=\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}n^{it}
 k_C(r-\log n).
\tag{L-93272.14}
\]

At every fixed `r`, only `n<=e^r` contribute. Thus the sum is finite.

The centered First-Hermite prime polynomial is

\[
S_q(t)
=\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}n^{it}h_q(\log n).
\tag{L-93272.15}
\]

Using (L-93272.11), finite summation, and Fubini,

\[
\boxed{
S_q(t)
=\int_{\mathbb R}A_q(r)\mathcal F_C(r,t)\,dr.
}
\tag{L-93272.16}
\]

This is an exact transform. It does not discard prime powers, take absolute values before the scale convolution, or average over the carrier.

## 4. Consequence for a future producer

Cauchy-Schwarz gives the legal implication

\[
|S_q(t)|
\le \|A_q\|_2\,\|\mathcal F_C(\cdot,t)\|_2
\ll q^{1/4}\|\mathcal F_C(\cdot,t)\|_2.
\tag{L-93272.17}
\]

Hence a source-specific bound for the complete cubic scale field transfers to First-Hermite heat with only polynomial loss in `q`. This avoids the exponential `e^{q/4}` loss of an absolute Gaussian prime envelope.

The required scale-field bound remains open and RH-bearing.
