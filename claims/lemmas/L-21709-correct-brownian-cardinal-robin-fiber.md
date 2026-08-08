# L-21709 — Correct Brownian cardinal Robin fiber

Claim ID: `L-21709`  
Title: The centered Brownian tail fiber is a Neumann–Robin determinant; positive lengths have only critical-line zeros and negative lengths have exactly one real off-line pair  
Status: **PROPOSED COMPLETE EXACT SPECTRAL LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `R-21703`; elementary regular Sturm–Liouville theory  
Scope: one cardinal length fiber; no closure under positive mixtures

## 1. Correct fiber

For real `ell`, define

\[
\boxed{
\Phi_\ell(z)
=\cosh\frac{\ell z}{2}
+2z\sinh\frac{\ell z}{2}.
}
\tag{L-21709.1}

It is entire and even in `z`.

## 2. Positive length

Let `ell>0` and put

\[
L=\frac\ell2.
\]

Consider the self-adjoint boundary problem

\[
-u''=\lambda u
\qquad(0<x<L),
\tag{L-21709.2}

with

\[
u'(0)=0,
\qquad
u'(L)+\frac12u(L)=0.
\tag{L-21709.3}

For `lambda=-z^2`, the Neumann-normalized solution is

\[
u_z(x)=\cosh(zx).
\]

The terminal boundary determinant is

\[
z\sinh(Lz)+\frac12\cosh(Lz)
=\frac12\Phi_\ell(z).
\tag{L-21709.4}

The quadratic form is

\[
Q_+[u]
=\int_0^L|u'(x)|^2dx
+\frac12|u(L)|^2
\ge0.
\tag{L-21709.5}

Thus every eigenvalue `lambda` is real and nonnegative. Since `lambda=-z^2`, every zero of `Phi_ell` lies on the imaginary axis:

\[
\boxed{
\ell>0
\Longrightarrow
\Phi_\ell(z)=0
\Longrightarrow
\operatorname{Re}z=0.
}
\tag{L-21709.6}

Regular separated Sturm–Liouville theory also gives simple eigenvalues, so the nonzero zeros are simple apart from the expected `+-` symmetry.

## 3. Negative length

Let `ell<0` and put

\[
L=-\frac\ell2>0.
\]

Then

\[
\Phi_\ell(z)
=\cosh(Lz)-2z\sinh(Lz).
\tag{L-21709.7}

Up to the nonzero factor `-2`, this is the determinant of

\[
-u''=\lambda u,
\qquad
u'(0)=0,
\qquad
u'(L)-\frac12u(L)=0.
\tag{L-21709.8}

Its quadratic form is

\[
Q_-[u]
=\int_0^L|u'(x)|^2dx
-\frac12|u(L)|^2.
\tag{L-21709.9}

A negative eigenvalue `lambda=-kappa^2` satisfies

\[
\boxed{
\kappa\tanh(\kappa L)=\frac12.
}
\tag{L-21709.10}

The left side is continuous and strictly increasing from `0` to `infinity`. Hence there is exactly one `kappa>0`. The fiber has exactly one real zero pair

\[
\boxed{z=+-\kappa.}
\tag{L-21709.11}

All remaining eigenvalues are nonnegative and therefore give imaginary zeros. Thus

\[
\boxed{
\ell<0
\Longrightarrow
\Phi_\ell
\text{ has exactly one real off-line pair.}
}
\tag{L-21709.12}

## 4. Zero length

The continuous limit is

\[
\Phi_0(z)=1.
\tag{L-21709.13}

It is zero free.

## 5. Pairing reflected lengths

For `a>0` and nonnegative weights `W_+,W_-`,

\[
W_+\Phi_a(z)+W_-\Phi_{-a}(z)
=(W_++W_-)
\left[
\cosh\frac{az}{2}
+2h z\sinh\frac{az}{2}
\right],
\tag{L-21709.14}

where

\[
h=\frac{W_+-W_-}{W_++W_-}.
\tag{L-21709.15}

The bracket is the same Neumann–Robin determinant with terminal Robin parameter `1/(2h)` when `h>0`. Hence one paired fiber has only imaginary zeros when `h>=0`, and exactly one real pair when `h<0`.

This gives the exact local meaning of reflected-length imbalance. It does not imply that an integral or positive sum of individually good fibers remains real-rooted; common interlacing or a global canonical system is still required.

## 6. Proof boundary

Closed exactly:

1. the correct centered fiber;
2. its self-adjoint Robin realization;
3. imaginary-zero classification for positive lengths;
4. the unique real pair for negative lengths;
5. the reflected-pair criterion.

Not proved:

1. closure of the real-zero property under the Nörlund length mixture;
2. BLNRZ;
3. RH.