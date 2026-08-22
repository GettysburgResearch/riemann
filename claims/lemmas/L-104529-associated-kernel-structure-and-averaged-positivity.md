# L-104529 — Associated-kernel structure and unconditional averaged orientation

Claim ID: `L-104529`  
Status: **PROVED EXACT PARTIAL ADVANCE**  
Created: 2026-08-23  
Depends on: `L-104528`  
RH status: **not assumed**

Let

\[
A(x)=\int_{\mathbb R}\varphi_2(u)\varphi_2(u-2x)\,du,
\]

and

\[
B(x)=\int_{\mathbb R}u\varphi_2(u)(u-2x)\varphi_2(u-2x)\,du.
\]

Both are autocorrelations: `A` is the autocorrelation of `varphi_2`, while `B`
is the autocorrelation of `u varphi_2(u)`.  The exact algebraic decomposition

\[
(u-x)^2=u(u-2x)+x^2
\]

gives

\[
\boxed{
\mathcal K_2(x)=B(x)+x^2A(x).
}
\tag{L-104529.1}
\]

Thus the difficult kernel is one positive-definite autocorrelation plus one
explicit quadratic modulation of a second positive-definite autocorrelation.
The only possible loss of positive definiteness is the quadratic modulation;
no hidden arithmetic or zero-dependent term remains.

For every nonnegative even Schwartz test `omega` whose Fourier transform is
nonnegative,

\[
\boxed{
\int_{\mathbb R}\mathcal L_2(t)\omega(t)\,dt
=4\int_{\mathbb R}\mathcal K_2(x)\widehat\omega(2x)\,dx
\ge0.
}
\tag{L-104529.2}
\]

This gives an unconditional family of smoothed orientation inequalities.  It
does not imply the pointwise sign at the real zeros of `Xi'''`; removing that
smoothing is exactly the `LAG2XI104550` gate.

## Relation to the classical Fourier-kernel programme

The representation (L-104528.2) is the order-one associated-kernel identity
for the Fourier transform of `u^2 Phi(u)`.  It places the fixed-order
reverse-Rolle problem inside the Csordas positive-definite-kernel programme,
but at the differentiated Xi kernel rather than at the original Xi kernel.
The required conclusion is positive definiteness of this one explicit
associated kernel, not merely its pointwise positivity or log-concavity.
