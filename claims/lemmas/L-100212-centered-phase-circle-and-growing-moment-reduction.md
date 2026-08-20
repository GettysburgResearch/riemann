# L-100212 — Centered phase-circle energy removes the root and reduces to a subpower moment tower

Claim ID: `L-100212`  
Status: **PROVED EXACT HILBERT/FINITE-TAIL REDUCTION**  
Created: 2026-08-20  
Depends on: `L-100211`; the graded owner framework of PRs #655–#656  
RH status: **not assumed**

Use the entire function

\[
\mathscr A_X(z)=
\sum_{X/8\le n\le X}
 c_X(n)e^{-z\ell_X(n)},
\]

where

\[
c_X(n)=\frac{\mu(n)}{\sqrt n}J_0(X/n),
\qquad
\ell_X(n)=\log(X/n)\in[0,\log8].
\]

Put

\[
M_k(X)=\sum_n c_X(n)\ell_X(n)^k.
\tag{L-100212.1}
\]

Then

\[
\mathscr A_X(z)-\mathscr A_X(0)
 =\sum_{k\ge1}\frac{(-z)^k}{k!}M_k(X).
\]

Orthogonality of the circle characters gives the exact identity

\[
\boxed{
\frac1{2\pi}
\int_0^{2\pi}
|\mathscr A_X(re^{i\vartheta})-\mathscr A_X(0)|^2d\vartheta
=
\sum_{k\ge1}\frac{r^{2k}}{(k!)^2}|M_k(X)|^2.
}
\tag{L-100212.2}
\]

The constant/root term is absent.  Since

\[
M_1(X)=G_\mu(X),
\]

(L-100212.2) implies

\[
\boxed{
|G_\mu(X)|^2
\le
\frac1{2\pi r^2}
\int_0^{2\pi}
|\mathscr A_X(re^{i\vartheta})-\mathscr A_X(0)|^2d\vartheta.
}
\tag{L-100212.3
}

This is the correct root-free version of the phase-circle estimate.

## Growing moment truncation

Let

\[
L_0=\log8,
\qquad
K_X=\left\lceil\frac{4\log(3X)}{\log\log(9X)}\right\rceil.
\]

The compact bounded kernel `J_0` gives

\[
\sum_n|c_X(n)|\ll\sqrt X.
\tag{L-100212.4}
\]

For fixed `0<r<=1`, the Taylor remainder after order `K_X` satisfies

\[
\begin{aligned}
\sup_{|z|=r}
\left|
\sum_{k>K_X}\frac{(-z)^k}{k!}M_k(X)
\right|
&\le
\left(\sum_n|c_X(n)|\right)
\sum_{k>K_X}\frac{(rL_0)^k}{k!}\\
&\ll X^{-2}
\end{aligned}
\tag{L-100212.5}
\]

for all sufficiently large `X`; enlarging the constant handles the finite
range.  This follows from

\[
\sum_{k>K}\frac{L_0^k}{k!}
\le e^{L_0}\left(\frac{eL_0}{K+1}\right)^{K+1}
\]

and the definition of `K_X`.

Consequently the centered circle energy is, up to `O(X^{-2})`, the finite
positive tower

\[
\boxed{
\sum_{1\le k\le K_X}
\frac{r^{2k}}{(k!)^2}|M_k(X)|^2,
\qquad
K_X=X^{o(1)}.
}
\tag{L-100212.6}

Every `M_k` is a compact, fixed-ratio logarithmic moment of the literal
ordinary-Mobius source.  Thus the closure problem has been reduced from one
root-containing Hardy square to a subpower number of root-free graded moments.

## Remaining theorem

Define `GMPC100212` by

\[
\int_2^Y
\left[
\sum_{1\le k\le K_X}
\frac{r^{2k}}{(k!)^2}|M_k(X)|^2
\right]^{1/2}
\frac{dX}{X}
=Y^{o(1)}.
\]

Then `GMPC100212` implies RH through (L-100212.3) and the minimal-wavelet
Mellin--Landau consumer.

The diagonal and moment-tail costs are closed.  The remaining burden is the
signed cross-core packing inside these finitely many moments.
