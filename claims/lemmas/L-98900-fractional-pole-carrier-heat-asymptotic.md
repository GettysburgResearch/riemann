# L-98900 — The fractional reciprocal-Julia heat packet has an unavoidable pole-carrier energy exponent one half

Claim ID: `L-98900`  
Status: **PROVED UNCONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-18  
Frozen input: PR #613 at `f28aa51a6d6740067202611d8ebda4be2ef0a1c9`  
RH status: **not assumed**

Let

\[
B_\diamond(s)=
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}
\]

and, for fixed `0<theta<1`, let `B_theta=B_diamond^theta` be the branch positive
on the real half-line `s>1`. Write

\[
B_\theta(s)=\sum_{n\ge1}b_\theta(n)n^{-s}
\qquad(\Re s>1)
\]

and define the heat packet used in `L-98702/L-98703` by

\[
\mathscr B_{\theta,T}(\tau)
=\sum_{n\ge1}\frac{b_\theta(n)}{\sqrt n}
 e^{-(\log n)^2/(4T)}e^{-i\tau\log n}.
\tag{L-98900.1}
\]

Then, uniformly for `y` in every fixed compact real interval,

\[
\boxed{
\mathscr B_{\theta,T}(y/\sqrt T)
=
\kappa_\theta e^{T/4}T^{-\theta-1/2}
 e^{-y^2}e^{-iy\sqrt T}(1+o_\theta(1)),
}
\tag{L-98900.2}
\]

where

\[
\boxed{
\kappa_\theta=
\frac{2\sqrt\pi\,(3/8)^\theta}{\Gamma(-\theta)}\ne0.
}
\tag{L-98900.3}
\]

Consequently the normalized Gaussian-window energy at center zero satisfies

\[
\boxed{
\begin{aligned}
\mathcal E_{\theta,T}(0)
&:=\int_{\mathbb R}|\mathscr B_{\theta,T}(\tau)|^2
 \frac{\sqrt T}{\sqrt\pi}e^{-T\tau^2}\,d\tau\\
&\sim
\frac{|\kappa_\theta|^2}{\sqrt3}
 e^{T/2}T^{-2\theta-1},
\end{aligned}}
\tag{L-98900.4}
\]

and in particular

\[
\boxed{
\lim_{T\to\infty}\frac1T\log\mathcal E_{\theta,T}(0)=\frac12.
}
\tag{L-98900.5}
\]

## Proof

The zeta Laurent expansion and the finite dyadic factor give, in a punctured
neighborhood of `s=1`,

\[
\zeta(s)=\frac1{s-1}+O(1),
\qquad
(1-2^{-s})(1-2^{-s-1})=\frac38+O(s-1),
\]

hence

\[
B_\theta(s)
=(3/8)^\theta(s-1)^\theta(1+O_\theta(s-1)).
\tag{L-98900.6}
\]

Gaussian Mellin inversion on `c_T=1+T^{-1}` gives

\[
\mathscr B_{\theta,T}(\tau)
=2\sqrt{\pi T}\,\frac1{2\pi i}
 \int_{c_T-i\infty}^{c_T+i\infty}
 B_\theta(s)e^{T(s-1/2-i\tau)^2}\,ds.
\tag{L-98900.7}
\]

Choose a fixed disk about `s=1` containing no zero of zeta and cut it along the
real segment immediately to the left of `1`. Outside a fixed horizontal
neighborhood of the cut, the Gaussian contributes an exponentially smaller
factor. Moving the local contour to the two sides of the cut gives the jump
of `(s-1)^theta`:

\[
(e^{i\pi\theta}-e^{-i\pi\theta})x^\theta
=2i\sin(\pi\theta)x^\theta.
\]

For `tau=y/sqrt(T)` and `s=1-x`, the local exponent is

\[
T(1/2-x-iy/\sqrt T)^2
=T/4-Tx+Tx^2-y^2-iy\sqrt T+2ixy\sqrt T.
\]

The cut integral is supported at `x\asymp T^{-1}`. Substituting `x=z/T`, using
(L-98900.6), and applying dominated convergence gives

\[
\mathscr B_{\theta,T}(y/\sqrt T)
=
-2\sqrt\pi(3/8)^\theta
 \frac{\sin(\pi\theta)}\pi
 \Gamma(1+\theta)
 e^{T/4}T^{-\theta-1/2}
 e^{-y^2}e^{-iy\sqrt T}(1+o(1)).
\]

The reflection identity

\[
\Gamma(-\theta)\Gamma(1+\theta)
=-\frac\pi{\sin(\pi\theta)}
\]

is exactly (L-98900.2)--(L-98900.3). Finally put `y=sqrt(T) tau` in the
window energy. The normalized measure becomes

\[
\pi^{-1/2}e^{-y^2}dy,
\]

while the squared packet contributes `e^{-2y^2}`. Since

\[
\pi^{-1/2}\int_{\mathbb R}e^{-3y^2}dy=3^{-1/2},
\]

(L-98900.4) follows.

## Interpretation

The exponent `1/2` is the unavoidable fractional branch at the real zeta pole.
It exists independently of the location of every nontrivial zero. A Weyl or
pole-centering operation can remove it only by changing the scalar packet in
(L-98900.1); it cannot change the numerical left side while continuing to call
it the same Dirichlet heat packet.
