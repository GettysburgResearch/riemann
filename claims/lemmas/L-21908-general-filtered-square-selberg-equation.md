# L-21908 — General square-preserving filtered Selberg equation

Claim ID: `L-21908`  
Title: Every finite translation filter closes the centered Selberg equation on its own filtered prime measure, and every positive real filter symbol has explicit positive-Hankel exponential adjoints  
Status: **PROPOSED — COMPLETE FINITE-TRANSLATION, ADJOINT, AND ENERGY ALGEBRA**  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-07  
Dependencies: `L-21906`; `L-21907`; the centered Selberg equation  
Scope: Haar, prime-only boundary-difference, and arbitrary finite safe filters

## 1. Finite translation algebra

For `a>=0`, let `tau_a` denote right translation of measures.  Let

\[
 \boxed{
 P=\sum_{j=0}^J c_j\tau_{a_j}}
 \tag{L-21908.1}
\]

be a nonzero real finite translation filter.  Define its translation derivative

\[
 \boxed{
 \dot P=\sum_{j=0}^J a_jc_j\tau_{a_j}.}
 \tag{L-21908.2}
\]

Because translations commute,

\[
 \dot{(PQ)}=\dot P\,Q+P\dot Q.
 \tag{L-21908.3}
\]

The centered Selberg operator satisfies

\[
 \mathscr L\tau_a=\tau_a\mathscr L+a\tau_a,
 \]

and therefore

\[
 \boxed{
 \mathscr LP=P\mathscr L+\dot P.}
 \tag{L-21908.4}
\]

## 2. Closed filtered equation

Let

\[
 \mathscr L\nu+\nu*\nu=R
 \tag{L-21908.5}
\]

be the centered Selberg equation and put

\[
 \boxed{
 \mu_P=P\nu.}
 \tag{L-21908.6}
\]

Apply `P^2` to (L-21908.5).  Since translations commute with convolution,

\[
 P^2(\nu*\nu)=\mu_P*\mu_P.
 \tag{L-21908.7}
\]

Also, by (L-21908.3)--(L-21908.4),

\[
 \begin{aligned}
 P^2\mathscr L\nu
 &=\mathscr LP^2\nu-\dot{(P^2)}\nu\\
 &=\mathscr LP\mu_P-2\dot P\mu_P.
 \end{aligned}
 \tag{L-21908.8}
\]

Hence

\[
 \boxed{
 \mathscr L_P\mu_P+\mu_P*\mu_P=P^2R,
 }
 \tag{L-21908.9}
\]

where

\[
 \boxed{
 \mathscr L_P=\mathscr LP-2\dot P.}
 \tag{L-21908.10}
\]

This is a closed nonlinear equation for the filtered measure itself.  The
quadratic term is always its literal convolution square.

For `P=I-tau_h`, equation (L-21908.9) is exactly `L-21906`.

## 3. Adjoint

The adjoint on test functions is

\[
 \boxed{
 \mathscr L_P^*=P^*\mathscr L^*-2\dot P^*.
 }
 \tag{L-21908.11}
\]

Let the real Laplace symbol be

\[
 \boxed{
 p(u)=\sum_{j=0}^Jc_je^{-a_ju}.}
 \tag{L-21908.12}
\]

Then

\[
 p'(u)=-\sum_j a_jc_je^{-a_ju}.
 \tag{L-21908.13}
\]

Assume

\[
 \boxed{
 p(u)>0\qquad(u>1/2).}
 \tag{L-21908.14}
\]

This is the real-axis safe-filter condition.

## 4. Explicit positive-Hankel adjoint

Fix `s>1/2` and define

\[
 \boxed{
 m_{P,s}(u)
 ={p(s)(s-1/2)^2
   \over
   p(u)^2(u-1/2)^2}
 {\bf1}_{[s,\infty)}(u).
 }
 \tag{L-21908.15}
\]

Put

\[
 \boxed{
 f_{P,s}(y)=\int_s^\infty m_{P,s}(u)e^{-uy}du.
 }
 \tag{L-21908.16}
\]

The density is positive, so `f_(P,s)` is completely monotone and
`f_(P,s)(x+y)` is a positive Hankel kernel.

Its logarithmic derivative is

\[
 {m_{P,s}'(u)\over m_{P,s}(u)}
 =-{2\over u-1/2}-{2p'(u)\over p(u)}.
 \tag{L-21908.17}
\]

For a general density `m`, applying (L-21908.11) to its Laplace mixture gives
continuous density

\[
 p(u)m'(u)
 +\left[2p'(u)+{2p(u)\over u-1/2}\right]m(u)
 \tag{L-21908.18}
\]

and boundary atom `p(s)m(s) delta_s`.  Equations
(L-21908.15)--(L-21908.17) cancel the continuous density and normalize the atom
to one.  Therefore

\[
 \boxed{
 \mathscr L_P^*f_{P,s}=e^{-s\,\cdot}.
 }
 \tag{L-21908.19}
\]

## 5. Positive energy identity

Let

\[
 H(z)=\langle\nu,e^{-z\,\cdot}\rangle,
 \qquad
 M_P(z)=p(z)H(z),
 \tag{L-21908.20}
\]

and

\[
 \mathcal R_P(z)=p(z)^2\mathcal R(z).
 \tag{L-21908.21}
\]

Pairing (L-21908.9) with `f_(P,s)` yields

\[
 \boxed{
 M_P(s)
 +\int_s^\infty m_{P,s}(u)M_P(u)^2du
 =\int_s^\infty m_{P,s}(u)\mathcal R_P(u)du.
 }
 \tag{L-21908.22}
\]

The nonlinear prime channel is a literal nonnegative square.  Positive
matrix-valued mixtures of the adjoints give the corresponding matrix identity.

In transform coordinates the same equation is

\[
 \boxed{
 -pM_P'
 +\left[p'+{2p\over z-1/2}\right]M_P
 +M_P^2
 =p^2\mathcal R.
 }
 \tag{L-21908.23}
\]

## 6. Prime-only safe filter

The prime-only boundary-safe filter of `T-21502` has real symbol

\[
 \boxed{
 p_H(s)
 =(1-e^{-s})^3(1-2e^{-s\log4}).
 }
 \tag{L-21908.24}
\]

For every `s>1/2`, both factors are positive, so (L-21908.14) holds.  Therefore
the exact ordinary-prime Hardy signal has a closed square-preserving Selberg
equation and the explicit adjoints (L-21908.15).

The zero of `p_H` at `1/2` cancels the pole model, while its other zeros lie on
the declared boundary lines; no open-strip zeta pole is removed.

## 7. Exact remaining obstruction

Equation (L-21908.22) gives complete control of **real exponential tests** for
every safe finite filter.  It does not automatically give the vertical Hardy
bound

\[
 \int_{\mathbb R}|M_P(\sigma+it)|^2dt<\infty
 \]

or the all-order Stieltjes positivity needed to exclude an off-axis pole.
Likewise, the compact signed Type-II kernel is not generally a positive mixture
of real exponentials.

Thus the remaining theorem is now precisely one of:

1. a vertical `H^2/H^1` estimate derived from the filtered Riccati equation;
2. a conditionally positive representation of the finite signed window;
3. a balanced Type-II square completing the ratio channel;
4. an all-order real-axis total-positivity theorem.

The filter, nonlinear closure, and positive adjoint no longer contribute any
unresolved algebra.

## 8. Proof boundary

- The finite-translation commutator and square-preserving equation are exact.
- The adjoint density and energy identity are exact under (L-21908.14).
- No RH assumption is used.
- The theorem does not prove the final vertical or Type-II estimate and does not
  prove RH.
