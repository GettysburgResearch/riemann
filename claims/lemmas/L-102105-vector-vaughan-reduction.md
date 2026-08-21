# L-102105 — The carrier-free bridge has one vector Vaughan decomposition and one balanced source packet

Claim ID: `L-102105`  
Status: **PROVED EXACT DECOMPOSITION; TWO-COMPONENT BALANCED ESTIMATE OPEN**  
Created: 2026-08-21  
Depends on: `L-102103--L-102104`; PR #685/PR #696 Vaughan identities  
RH status: **not assumed**

Let `K^dagger=(K_Q^dagger,K_A^dagger)` and define

\[
W_\mu^\dagger(X)=\sum_{n\ge1}{\mu(n)\over\sqrt n}K^\dagger(X/n).
\]

For `U>=1`, put `mu_U=mu 1_(n<=U)` and `a_U=epsilon-mu_U*1`. The exact identity

\[
\mu=2\mu_U-\mu_U*\mu_U*\mathbf1+a_U*a_U*\mu
\tag{L-102105.1}
\]

has `a_U(n)=0` for `n<=U`. Because both kernels are supported on `[1,32]`, the first term vanishes for `U<X/32`. Hence

\[
\boxed{W_\mu^\dagger(X)=T_U(X)+B_U(X),}
\tag{L-102105.2}
\]

where

\[
T_U(X)=-\sum_{a,b\le U}{\mu(a)\mu(b)\over\sqrt{ab}}
\sum_{m\ge1}{1\over\sqrt m}K^\dagger(X/(abm))
\tag{L-102105.3}
\]

and

\[
\boxed{
B_U(X)=\sum_{r,s>U\atop m\ge1}{a_U(r)a_U(s)\mu(m)\over\sqrt{rsm}}K^\dagger(X/(rsm)).
}
\tag{L-102105.4}
\]

The arithmetic coefficient in (L-102105.4) is identical in both coordinates. By `L-102103.6`,

\[
|T_U(X)|\le{(V_Q,V_A)\over12}X^{-3/2}\left(\sum_{a\le U}a\right)^2.
\]

With `U=floor(X^(1/3))`,

\[
\boxed{T_U(X)=O(X^{-1/6}),}
\tag{L-102105.5}
\]

so its logarithmic `L1` mass is finite.

For the duplicate-67 source,

\[
W_\beta^\dagger=(I-67^{-1/2}S_{67})W_\mu^\dagger.
\tag{L-102105.6}
\]

Using the same cutoff gives an integrable vector Type-I error and the balanced vector

\[
\boxed{B_{\beta,U}^\dagger(X)=B_U(X)-67^{-1/2}B_U(X/67).}
\tag{L-102105.7}
\]

Thus every complete-lattice, carrier, and Type-I contribution has been removed simultaneously. The surviving middle estimate is one balanced arithmetic packet observed in two differential coordinates of the same positive spline.
