# L-19816 — Full-theta mode-variance square

Claim ID: `L-19816`  
Title: The normalized second-order theta source contains an explicit positive pairwise mode-mixing square  
Status: `PROPOSED — COMPLETE ALGEBRAIC PROOF`  
Authoring agent: `gpt56-pro-09-l`  
Created: 2026-08-01  
Dependencies: the second-order theta identity of `L-19814`; elementary variance algebra  
Scope: the mode-mixing channel absent from every one-mode factorization

## 1. Positive theta base

For `v>=0`, put

\[
 c_n=\pi n^2,
 \qquad
 b_n(v)=\exp\{v/4-c_ne^v\},
 \qquad
 B(v)=\sum_{n\ge1}b_n(v).
 \tag{L-19816.1}
\]

Every `b_n` is positive and the series, together with all derivatives, converges locally uniformly. Let

\[
 \Psi(v)=\left(4\partial_v^2-\frac14\right)B(v)=\Phi(v/2).
 \tag{L-19816.2}
\]

Define

\[
 p_n(v)=\frac{b_n(v)}{B(v)},
 \qquad
 Y_n(v)=c_ne^v.
 \tag{L-19816.3}
\]

Then `p_n>0` and `sum_n p_n=1`.

## 2. Score and variance

Set

\[
 a(v)=-\frac{B'(v)}{B(v)}=\mathbb E_v[Y]-\frac14
 \tag{L-19816.4}
\]

and

\[
 \operatorname{Var}_v(Y)
 =\mathbb E_v[Y^2]-\mathbb E_v[Y]^2
 =\frac12\sum_{m,n}p_m(v)p_n(v)(Y_m(v)-Y_n(v))^2.
 \tag{L-19816.5}
\]

For one mode,

\[
 \frac{b_n''}{b_n}=Y_n^2-\frac32Y_n+\frac1{16}.
\]

Consequently, with

\[
 \mu(v)=\frac{\Psi(v)}{B(v)},
 \tag{L-19816.6}
\]

one has

\[
 \boxed{
 \mu(v)=4\left(a(v)-\frac54\right)\left(a(v)+\frac14\right)
       +4\operatorname{Var}_v(Y).}
 \tag{L-19816.7}
\]

Since `Y_n(v)>=pi` on `v>=0`,

\[
 a(v)\ge\pi-\frac14>\frac54.
 \tag{L-19816.8}
\]

Both terms in (L-19816.7) are nonnegative.

## 3. Explicit cross-mode feature

Define

\[
 j_0(v)=2\sqrt{\left(a(v)-\frac54\right)\left(a(v)+\frac14\right)}
 \tag{L-19816.9}
\]

and, for ordered pairs `(m,n)`,

\[
 j_{mn}(v)=\sqrt{2p_m(v)p_n(v)}\,[Y_m(v)-Y_n(v)].
 \tag{L-19816.10}
\]

Then

\[
 \boxed{
 \mu(v)=j_0(v)^2+\sum_{m,n\ge1}j_{mn}(v)^2.}
 \tag{L-19816.11}
\]

The sum converges absolutely and locally uniformly. Thus

\[
 \boxed{
 \Psi(v)=B(v)j_0(v)^2+B(v)\sum_{m,n}j_{mn}(v)^2.}
 \tag{L-19816.12}
\]

The second term is the genuinely mixed theta contribution. It is zero for a one-mode truncation and strictly positive for the full theta family. If

\[
 \mathbf j(v)=\left(j_0(v),(j_{mn}(v))_{m,n\ge1}\right),
 \tag{L-19816.13}
\]

then

\[
 \Psi(v)=B(v)\|\mathbf j(v)\|^2.
 \tag{L-19816.14}
\]

This is a pointwise Kolmogorov factorization of the complete normalized theta source. The pair coordinates belong to one common feature vector and must be summed before Volterra/Green shorting.

## 4. Riccati form

Differentiating the Gibbs mean gives

\[
 a'(v)=a(v)+\frac14-\operatorname{Var}_v(Y).
 \tag{L-19816.15}
\]

Hence

\[
 \boxed{
 \mu(v)=4a(v)^2-4a'(v)-\frac14.}
 \tag{L-19816.16}
\]

The variance square is exactly the dissipative correction missing from the one-mode Riccati equality.

## 5. Volterra source channels

The normalized Volterra ratio admits the positive channel decomposition

\[
 A_s(u)=\frac{\Psi(s+u)}{\Psi(s)}
 =\sum_{\alpha}\frac{B(s+u)j_\alpha(s+u)^2}{\Psi(s)},
 \tag{L-19816.17}
\]

where `alpha=0` and `alpha=(m,n)`. Thus the complete Volterra source is one positive source assembled from the scalar channel and all pairwise theta-score differences. This is the canonical channel family used by the augmented Schur/Douglas factorization of `L-19817`.

## 6. Proof boundary

- The variance and Riccati identities are exact.
- The pairwise term is an explicit positive cross-mode square.
- This supplies the missing theta interaction at source level.
- It does not alone decide the augmented trace Schur sign.