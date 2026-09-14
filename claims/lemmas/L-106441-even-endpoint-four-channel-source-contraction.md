# L-106441 — Uniform four-channel source contraction for every even endpoint

Claim ID: `L-106441`  
Status: **PROVED EXACT FOR THE TRUNCATED POSITIVE/NEGATIVE XI FOURIER SOURCE**  
Created: 2026-08-25  
Depends on: `L-105260`, `L-106410--L-106413`, `L-106440`  
RH status: **not assumed**

Let `K=2m>=2`, let `Phi>=0`, and truncate the positive Xi half-source to
`0<=u<=L`.  Put

\[
c=\lambda L<1.
\]

The endpoint symbol is the one in `L-106440`.  The following bounds are
independent of the even order `K`.

## 1. Same-sign channels

For `u,v in [0,L]`, symmetrize the positive denominator density as

\[
\begin{aligned}
a_{=}(u,v)={1\over2}\big[&
 (1-\lambda u)(1+\lambda v)v^K\\
 &+(1-\lambda v)(1+\lambda u)u^K\big].
\end{aligned}
\tag{L-106441.1}
\]

The absolute endpoint numerator density is

\[
r_{=}(u,v)=\lambda|u-v|\,|u^K-v^K|.
\tag{L-106441.2}
\]

Since

\[
a_{=}(u,v)\ge {1-c\over2}(u^K+v^K),
\]

and

\[
|u-v|\le L,
\qquad
|u^K-v^K|\le u^K+v^K,
\]

one has the pointwise domination

\[
\boxed{
0\le r_{=}(u,v)
 \le {2c\over1-c}\,a_{=}(u,v).
}
\tag{L-106441.3}
\]

Consequently the squared same-sign Hankel ratio is at most

\[
\boxed{
\left({2c\over1-c}\right)^2.
}
\tag{L-106441.4}

This sharpens the order-two safe estimate in `L-106410` by using
`|u-v||u^K-v^K|<=L(u^K+v^K)` before separating the two factors.

## 2. Reflected channels

For one reflected orientation define

\[
\begin{aligned}
a_{\times}(u,v)={}&
 (1-\lambda u)(1-\lambda v)v^K\\
 &+(1+\lambda u)(1+\lambda v)u^K,
\end{aligned}
\tag{L-106441.5}
\]

and

\[
r_{\times}(u,v)
 =2\lambda(u+v)|u^K-v^K|.
\tag{L-106441.6}
\]

Then

\[
a_{\times}(u,v)\ge(1-c)^2(u^K+v^K)
\]

and

\[
r_{\times}(u,v)\le4c(u^K+v^K),
\]

so

\[
\boxed{
0\le r_{\times}(u,v)
 \le {4c\over(1-c)^2}\,a_{\times}(u,v).
}
\tag{L-106441.7}

The corresponding squared Toeplitz-channel ratio is at most

\[
\boxed{
\left({4c\over(1-c)^2}\right)^2.
}
\tag{L-106441.8
}

## 3. Complete four-channel cost

The two same-sign and two reflected orientations therefore obey

\[
\boxed{
\mathfrak r_{2m}(c)
 \le
 2\left({2c\over1-c}\right)^2
 +2\left({4c\over(1-c)^2}\right)^2.
}
\tag{L-106441.9}

At the explicit shift `c=1/200`,

\[
\boxed{
\mathfrak r_{2m}(1/200)
 \le
 {1596808\over1568239201}
 <{1\over982}.
}
\tag{L-106441.10}

The bound is uniform in the even endpoint order.  Constant unitary
recombination of the four channels preserves this energy exactly.

## 4. Scope

The theorem closes the finite source payment for each even endpoint.  The
actual Xi Fourier tail is superexponentially small under the same cofinal
truncation used in `L-106414`.  The theorem does not control the signed
unobserved all-pass tail; no absolute model-space coverage is asserted.