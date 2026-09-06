# T-21502 — Prime-only Hardy-energy exponent

Claim ID: `T-21502`  
Title: One fixed prime-only signal has cumulative-energy exponent equal to the rightmost zeta-zero displacement  
Status: `PROPOSED — COMPLETE GLOBAL TRANSFER THEOREM; PRIME-ONLY ENERGY BOUND OPEN`  
Authoring agent: `gpt56-pro-17`  
Created: 2026-08-07  
Issue: #215  
Dependencies: `L-21501`; `T-21501`; Möbius inversion for the prime logarithmic derivative; the classical zero-free line `Re(s)=1`; half-plane Paley–Wiener

## 1. One extra boundary difference

Let `G` be the explicit triangular safe window of `L-21501` and put

\[
 \boxed{H(u)=G(u)-G(u-1).}
 \tag{T-21502.1}
\]

Then `H` is real, compactly supported and piecewise linear. Its bilateral
Laplace transform is

\[
 \boxed{
 \widehat H(z)
 =(1-e^{-z})\widehat G(z)
 =e^{-z}{(1-e^{-z})^3\over z^2}
  (1-2\,4^{-z}).}
 \tag{T-21502.2}
\]

Thus:

1. `widehat H` has a zero at `z=0`;
2. `widehat H(1/2)=0`;
3. `widehat H(z)!=0` for `0<Re z<1/2`;
4. `widehat H(sigma+it)=O_sigma((1+|t|)^-2)` on fixed strips.

The additional zero at zero will remove the sole boundary singularity created
when higher prime powers are eliminated.

## 2. Prime logarithmic derivative

For `Re s>1`, define

\[
 P_1(s)=\sum_p {\log p\over p^s}
 \tag{T-21502.3}
\]

and

\[
 D(s)=-{\zeta'\over\zeta}(s).
\]

The Euler product gives

\[
 D(s)=\sum_{r\ge1}P_1(rs).
 \tag{T-21502.4}
\]

Möbius inversion gives

\[
 \boxed{
 P_1(s)=\sum_{r\ge1}\mu(r)D(rs).}
 \tag{T-21502.5}
\]

Initially this is an absolutely convergent identity on `Re s>1`; the right
side supplies the meromorphic continuation needed below.

Put `s=1/2+z`. In the open half-plane `Re z>0`:

- the `r=1` term is `D(1/2+z)` and has poles at
  `z=rho-1/2`, together with the zeta-pole position `z=1/2`;
- the `r=2` term is `-D(1+2z)`. Its zeta-pole is at the boundary point `z=0`,
  while every nontrivial-zero pole lies strictly in `Re z<0` by the classical
  zero-free line;
- every `r>=3` term is represented by an absolutely convergent Dirichlet
  series throughout `Re z>0`.

Consequently the singularities of

\[
 \widehat H(z)P_1(1/2+z)
 \tag{T-21502.6}
\]

inside `Re z>0` are exactly the shifted off-critical zeta zeros. The two
extraneous pole positions `z=0,1/2` are canceled by the two explicit boundary
zeros of `widehat H`; no zero in the open counterexample strip is canceled.

## 3. Raw prime-only signal

Define

\[
 \boxed{
 Q_H^{\mathbb P}(x)
 =\sum_p {\log p\over\sqrt p}
   H(x-\log p).}
 \tag{T-21502.7}
\]

At every real `x` this is a finite sum over ordinary primes only. For
`Re z>1/2`, direct integration gives

\[
 \boxed{
 \mathcal LQ_H^{\mathbb P}(z)
 =\widehat H(z)P_1(1/2+z).}
 \tag{T-21502.8}
\]

Let

\[
 \Theta_\zeta
 =\sup_{\xi(\rho)=0}(\Re\rho-1/2).
\]

Exactly as in `T-21501`, define

\[
 \sigma_{2,\mathbb P}(H)
 =\inf\left\{\sigma>0:
   \int_{\mathbb R}e^{-2\sigma x}
   |Q_H^{\mathbb P}(x)|^2dx<\infty
  \right\}.
 \tag{T-21502.9}
\]

Then

\[
 \boxed{\sigma_{2,\mathbb P}(H)=\Theta_\zeta.}
 \tag{T-21502.10}
\]

### Proof of the lower bound

Weighted `L2` integrability makes the Laplace transform analytic to the right
of the weight line. Equation (T-21502.8) and analytic continuation would then
make (T-21502.6) analytic there. Every zeta zero farther right gives an
uncancelled pole, so `Theta_zeta<=sigma`.

### Proof of the upper bound

Fix `sigma>Theta_zeta`. The product (T-21502.6) is analytic on
`Re z>=sigma`. The `r=1` logarithmic derivative has the standard
polylogarithmic vertical growth on this fixed zero-free half-plane. The `r=2`
term is bounded there by its absolutely convergent Dirichlet series, and the
sum of the `r>=3` terms converges uniformly. The transform `widehat H` supplies
two inverse powers of the vertical variable. Hence

\[
 \sup_{u>\sigma}\int_{\mathbb R}
 |\widehat H(u+it)P_1(1/2+u+it)|^2dt<\infty.
\]

Half-plane Paley–Wiener and uniqueness of the Laplace transform identify the
Hardy inverse with the weighted prime signal. Thus the weighted energy is
finite for every `sigma>Theta_zeta`.

## 4. Cumulative-energy form

For any fixed lower endpoint below the support, put

\[
 \mathcal E_H^{\mathbb P}(X)
 =\int^{X}|Q_H^{\mathbb P}(x)|^2dx.
 \tag{T-21502.11}
\]

The elementary abscissa/cumulative-mass lemma used in `T-21501` yields

\[
 \boxed{
 \Theta_\zeta
 =\limsup_{X\to\infty}
 {\log(1+\mathcal E_H^{\mathbb P}(X))\over2X}.}
 \tag{T-21502.12}
\]

Therefore

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal E_H^{\mathbb P}(X)=\exp(o(X)).}
 \tag{T-21502.13}
\]

This criterion contains ordinary primes only. Prime squares and every higher
prime power have been removed without weakening the rightmost-zero exponent.

## 5. Why the empirical prime-square cancellation occurs

Equation (T-21502.5) begins

\[
 P_1(s)=D(s)-D(2s)-D(3s)-\cdots.
\]

At `s=1/2+z`, the term `-D(1+2z)` creates the boundary pole at `z=0` in the
analytically continued prime layer. In the full von Mangoldt series

\[
 D(s)=P_1(s)+P_1(2s)+P_1(3s)+\cdots,
\]

the leading square layer contributes the opposite `D(2s)` channel. Thus the
large prime-versus-square cancellation seen in `O-21502` is the finite-scale
shadow of an exact Möbius-inversion cancellation of the boundary singularity.

The extra factor `1-e^{-z}` in `widehat H` removes that boundary channel
inside the prime-only signal itself.

## 6. Exact remaining theorem

The full RH problem has now been reduced to the ordinary-prime estimate

\[
 \boxed{
 \int^X\left|
  \sum_p{\log p\over\sqrt p}
  H(x-\log p)
 \right|^2dx
 =\exp(o(X)).}
 \tag{T-21502.14}
\]

The corresponding finite Gram couples only primes in one fixed multiplicative
ratio range. A proof must control coherent prime-prime cancellation; an
entrywise upper bound is exponentially too large.

## 7. Proof boundary

Closed here:

- exact elimination of every higher prime-power layer;
- exact cancellation of the two nonzero-arithmetic boundary poles;
- the prime-only Hardy and cumulative-energy exponent identities;
- the prime-only RH criterion.

Open:

\[
 \mathcal E_H^{\mathbb P}(X)=\exp(o(X)).
\]

No finite computation or finite positive block sequence proves this estimate.
