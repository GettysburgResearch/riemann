# L-105200 — Natural-scale Gaussian saddle law for the Xi derivative companions

Claim ID: `L-105200`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: PR #716 `L-104504`; PR #720 `L-104516--L-104517`  
RH status: **not assumed**

## 1. Tilted Xi measure and curvature scale

Use the classical positive Fourier kernel

\[
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du,
\qquad \Phi(u)>0,
\]

with the explicit rapidly decreasing `Phi` of `L-104504`. For every integer
`m>=1`, put

\[
M_m=\int_0^\infty u^m\Phi(u)\,du,
\qquad
d\nu_m(u)=M_m^{-1}u^m\Phi(u)\,du,
\]

and

\[
S_m(u)=m\log u+\log\Phi(u).
\]

Let `w_m` be the unique global maximizer of `S_m` for all sufficiently large
`m`, define

\[
\kappa_m=-S_m''(w_m),
\qquad
s_m=\kappa_m^{-1/2},
\tag{L-105200.1}
\]

and write

\[
X_m={u-w_m\over s_m}
\quad (u\sim\nu_m).
\]

The saddle equation and the differentiated `m=1` asymptotic of `Phi` give

\[
2\pi e^{2w_m}={m\over w_m}+O(1),
\qquad
w_m={1\over2}\log m+O(\log\log m),
\tag{L-105200.2}
\]

and

\[
\boxed{
\kappa_m={2m\over w_m}\left(1+O(1/w_m)\right),
\qquad
s_m^2={w_m\over2m}\left(1+O(1/w_m)\right).
}
\tag{L-105200.3}
\]

Thus `s_m` is the natural absolute Fourier-width scale. It is comparable to
`sqrt(log m/m)` and tends to zero.

## 2. Uniform complex Gaussian limit

For every fixed `B>0`,

\[
\boxed{
\sup_{m\ge M}\sup_{|\lambda|\le B}
\left|
\int e^{\lambda X_m}\,d\nu_m
-e^{\lambda^2/2}
\right|
\longrightarrow0
\qquad(M\to\infty).
}
\tag{L-105200.4}
\]

Here `lambda` is complex and the disk is the ordinary complex disk.

### Proof

On `|u-w_m|<=1`, termwise differentiation of the explicit positive kernel
used in `L-104504` gives

\[
S_m^{(3)}(u)=O(m/w_m),
\qquad
S_m^{(4)}(u)=O(m/w_m),
\tag{L-105200.5}
\]

uniformly for large `m`. Consequently, with `u=w_m+s_m x`,

\[
S_m(w_m+s_mx)-S_m(w_m)
=-{x^2\over2}
+O\!\left(\sqrt{w_m/m}\,|x|^3
          +{w_m\over m}|x|^4\right).
\tag{L-105200.6}
\]

Choose

\[
R_m=(m/w_m)^{1/12}.
\]

The error in (L-105200.6) is `o(1)` uniformly on `|x|<=R_m`. On the
complement of that interval but still inside `|u-w_m|<=1`, strict concavity
and the curvature bound give `exp(-cR_m^2)` domination. The two exterior tails
are exponentially smaller than the central saddle mass by the same elementary
estimates as `L-104504`: the left tail loses through `u^m`, and the right tail
through `exp(-pi exp(2u))`.

After the change of variables `u=w_m+s_mx`, both the numerator and denominator
of the tilted expectation therefore converge to their Gaussian integrals.
For `|lambda|<=B`, the factor `exp(lambda x)` is absorbed by
`exp(-x^2/4)` outside a fixed compact interval. The preceding estimates are
uniform once `m>=M`; this proves (L-105200.4). No probabilistic limit theorem is
imported.

## 3. Natural-scale one-sided Fourier model

Let

\[
A_m(z)=\int_0^\infty e^{izu}\,d\nu_m(u).
\]

Fix `C,H>0` and define the common half-infinite-tail height

\[
\boxed{
T_M=C\sqrt{M\over\log M}.
}
\tag{L-105200.7}
\]

Since `log m/m` decreases for large `m`, (L-105200.3) gives

\[
\sup_{m\ge M}s_mT_M=O_C(1).
\]

Apply (L-105200.4) with `lambda=i s_m z`. Uniformly for

\[
m\ge M,
\qquad |\Re z|\le T_M,
\qquad |\Im z|\le H,
\]

one obtains the relative asymptotic

\[
\boxed{
A_m(z)
=
\exp\!\left(iw_mz-{s_m^2z^2\over2}\right)
\left(1+\epsilon_M(m,z)\right),
}
\tag{L-105200.8}
\]

where

\[
\sup_{m\ge M,\ z}|\epsilon_M(m,z)|\longrightarrow0.
\tag{L-105200.9}
\]

The Gaussian factor is nonzero. The approximation reaches a fixed multiple of
the reciprocal standard deviation, rather than only the
`o(sqrt(m/log m))` range of the first-moment estimate in `L-104517`.

## 4. Derivative form

Uniform convergence in (L-105200.4) holds on every slightly larger compact
`lambda` disk. Cauchy's formula therefore gives convergence of all fixed
`lambda` derivatives. For `r=0,1,2`, uniformly in the same natural box,

\[
\boxed{
A_m^{(r)}(z)
=
{d^r\over dz^r}
\exp\!\left(iw_mz-{s_m^2z^2\over2}\right)
+o\!\left(w_m^r
 e^{w_m|\Im z|+O_C(1)}\right).
}
\tag{L-105200.10}
\]

The same statement holds at `-z`. This derivative control is the input needed
to compute critical-value/curvature residues, not merely zero locations.

## 5. Scope

This theorem proves a Gaussian local limit for the actual positive Xi Fourier
measure, uniformly over the complete derivative tail `m>=M`. It does not
control any fixed low derivative as `M->infinity`, and it does not itself
exclude a zeta zero. Its conclusion-facing uses are the natural-height
real-rootedness theorem `L-105201` and the residue-coherence theorem
`L-105202`.
