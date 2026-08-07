# L-15426 — Exact two-channel lift of Suzuki's archimedean factor

Claim ID: `L-15426`  
Title: The full sign-sensitive kernel `g_omega` is a contractive Krein multiplier between two positive Mellin channels  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: Suzuki's explicit formula for `g_omega`; elementary multiplicative convolution  
Scope: archimedean half of the requested Jordan/Volterra intertwiner  
Related counterexample candidates: none

## Positive beta channel and Volterra channel

For `0<x<1`, define

\[
 b_\omega(x)
 ={2\pi^\omega\over\Gamma(\omega)}
 x^{2-\omega}(1-x^2)^{\omega-1},
 \tag{L-15426.1}
\]

\[
 k_\omega(x)=x^{\omega-1}.
 \tag{L-15426.2}
\]

For multiplicative convolution

\[
 (f*_Mg)(x)=\int_x^1f(y)g(x/y){dy\over y},
 \tag{L-15426.3}
\]

put

\[
 v_\omega(x)=2\omega(b_\omega*_Mk_\omega)(x).
 \tag{L-15426.4}
\]

Both `b_omega` and `v_omega` are nonnegative. Direct substitution gives the
exact identity

\[
 \boxed{g_\omega=b_\omega-v_\omega.}
 \tag{L-15426.5}
\]

Indeed,

\[
 (b_\omega*_Mk_\omega)(x)
 ={\pi^\omega\over\Gamma(\omega)}x^{\omega-1}
 \int_{x^2}^1t^{1/2-\omega}(1-t)^{\omega-1}dt,
 \tag{L-15426.6}
\]

which is exactly one half of the incomplete-beta term in Suzuki's definition.

## Positive majorant and contractive score

Define

\[
 \ell_\omega=b_\omega+v_\omega>0,
 \qquad
 \kappa_\omega={b_\omega-v_\omega\over b_\omega+v_\omega}.
 \tag{L-15426.7}
\]

Then

\[
 |\kappa_\omega(x)|\le1,
 \qquad
 g_\omega(x)=\kappa_\omega(x)\ell_\omega(x).
 \tag{L-15426.8}
\]

On

\[
 \mathcal A_\omega
 =L^2((0,1),\ell_\omega(x)dx/x),
 \tag{L-15426.9}
\]

multiplication by `kappa_omega` is a self-adjoint contraction.

The map

\[
 \boxed{
 (W_\omega f)(x)
 =\left(
  \sqrt{b_\omega(x)/\ell_\omega(x)}f(x),
  \sqrt{v_\omega(x)/\ell_\omega(x)}f(x)
  \right)}
 \tag{L-15426.10}
\]

is an isometry from `A_omega` to

\[
 L^2(b_\omega dx/x)\oplus L^2(v_\omega dx/x).
\]

With `J=diag(1,-1)`, one has

\[
 \boxed{W_\omega^*JW_\omega=M_{\kappa_\omega}.}
 \tag{L-15426.11}
\]

Thus the gamma-factor channel is an exact two-positive-channel Krein
compression.

## Mellin identities

For complex `u` in the common convergence half-plane,

\[
 \widehat b_\omega(u)
 =\int_0^1b_\omega(x)x^u{dx\over x}
 =\pi^\omega
 {\Gamma((u-\omega)/2+1)
  \over\Gamma((u+\omega)/2+1)}.
 \tag{L-15426.12}
\]

Since

\[
 \widehat k_\omega(u)={1\over u+\omega-1},
 \tag{L-15426.13}
\]

we obtain

\[
 \widehat v_\omega(u)
 ={2\omega\widehat b_\omega(u)
   \over u+\omega-1},
 \tag{L-15426.14}
\]

and hence

\[
 \boxed{
 \widehat g_\omega(u)
 =\widehat b_\omega(u)
 {u-\omega-1\over u+\omega-1}
 ={\gamma(u-\omega)\over\gamma(u+\omega)}.}
 \tag{L-15426.15}
\]

For

\[
 \alpha_s(x)=x^{s/2}\sqrt{\ell_\omega(x)},
 \tag{L-15426.16}
\]

and `u=(s+bar(t))/2`,

\[
 \langle\alpha_t,M_{\kappa_\omega}\alpha_s\rangle
 =\widehat g_\omega(u),
 \qquad
 \langle\alpha_t,\alpha_s\rangle
 =\widehat\ell_\omega(u).
 \tag{L-15426.17}
\]

## Full local-place tensor in the safe half-plane

Combine `L-15425` and the present lift. Define

\[
 \mathfrak a_s(d,x)
 =\sqrt{J_{2\omega}(d)}d^{-(s+\omega)/2}
  x^{s/2}\sqrt{\ell_\omega(x)}.
 \tag{L-15426.18}
\]

Then, for `Re u>1+omega`,

\[
\boxed{
 \langle\mathfrak a_t,
  (I\otimes M_{\kappa_\omega})\mathfrak a_s\rangle
 ={\zeta(u-\omega)\over\zeta(u+\omega)}
  {\gamma(u-\omega)\over\gamma(u+\omega)}
 ={\xi(u-\omega)\over\xi(u+\omega)}.}
 \tag{L-15426.19}
\]

This is the requested explicit Euler--archimedean intertwiner in the maximal
half-plane where its positive Hilbert features exist.

## Gap audit

- The two-channel lift is Hilbert/Krein, not a one-channel positive
  factorization of `g_omega`.
- The tensor feature in (L-15426.18) has the arithmetic convergence boundary
  `Re u=1+omega`.
- The scalar completed ratio continues through that boundary by a pole-zero
  cancellation which is not a Hilbert-norm cancellation.
- The critical physical metric therefore requires a renormalized boundary
  channel before completion.
