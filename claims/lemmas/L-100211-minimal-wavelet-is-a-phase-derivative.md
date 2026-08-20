# L-100211 — The minimal Möbius wavelet is an exact phase derivative with bounded carrier width

Claim ID: `L-100211`  
Status: **PROVED EXACT PHASE-LIFT IDENTITY**  
Created: 2026-08-20  
Depends on: PRs #674–#675  
RH status: **not assumed**

Let `K_0` be the minimal ratio-eight kernel of PR #674.  It is supported on
`[1,8]` and vanishes to first order at its activation point:

\[
K_0(1)=0.
\]

Define

\[
J_0(y)=
\begin{cases}
K_0(y)/\log y,&1<y\le8,\\
\displaystyle\lim_{z\downarrow1}K_0(z)/\log z,&y=1,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-100211.1}
\]

The explicit first band

\[
K_0(y)=8\sqrt y-8-3\log y
\qquad(1\le y<2)
\]

shows that the limit in (L-100211.1) is one.  Hence `J_0` is bounded and
piecewise smooth on `[1,8]`.

Put

\[
\mathscr A_X(z)
 =\sum_{X/8\le n\le X}
 \frac{\mu(n)}{\sqrt n}
 J_0(X/n)
 \exp[-z\log(X/n)],
\qquad z\in\mathbb C.
\tag{L-100211.2}
\]

This is an entire function of exponential type at most `log 8`.  Differentiating
the finite sum gives

\[
\boxed{
G_\mu(X)=-\mathscr A_X'(0),
}
\tag{L-100211.3}
\]

where

\[
G_\mu(X)
 =\sum_{X/8\le n\le X}
 \frac{\mu(n)}{\sqrt n}K_0(X/n)
\]

is the conclusion-facing minimal wavelet.

For every fixed `r>0`, Cauchy's derivative formula and Cauchy--Schwarz give the
exact root-free circle estimate

\[
\boxed{
|G_\mu(X)|^2
 \le\frac1{2\pi r^2}
 \int_0^{2\pi}
 |\mathscr A_X(re^{i\vartheta})|^2d\vartheta.
}
\tag{L-100211.4
}

All coefficient real shifts on the circle cost at most `8^r`, independent of
`X`.  Except at two measure-zero points, the boundary has a nonzero arithmetic
phase

\[
\Im(re^{i\vartheta}),
\]

and

\[
e^{-z\log(X/n)}=X^{-z}n^z.
\]

Thus the zero-frequency value has been replaced by a first phase derivative,
and its exact point evaluation is controlled by a fixed compact circle of
nonzero multiplicative phases.

## Conclusion-facing criterion

Define `CPCP100211` by

\[
\int_2^Y
 \left(
 {1\over2\pi}
 \int_0^{2\pi}|\mathscr A_X(re^{i\vartheta})|^2d\vartheta
 \right)^{1/2}
 \frac{dX}{X}
 =Y^{o(1)}
\]

for one fixed `r>0`.  Then (L-100211.4), PR #674's positive desmoothing, and
the negative-mass Mellin--Landau theorem imply RH.

The theorem does not prove `CPCP100211`.  It replaces the root-containing
Hardy square of PR #671 by a derivative evaluation whose neutral mode has been
removed at the kernel level.
