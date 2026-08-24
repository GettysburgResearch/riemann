# R-105630 — Causal source contraction does not imply the pointwise physical sign

Claim ID: `R-105630`  
Status: **PROVED EXACT TWO-FREQUENCY SEPARATOR**  
Created: 2026-08-25  
Depends on: `L-105625--L-105629`; `T-105630`  
RH status: **not assumed**

The safe-region theorem proves an exact weighted contraction for a causal inner
phase. This file proves that such an operator inequality cannot be evaluated
pointwise without an additional source-to-physical kernel theorem.

## 1. Exact causal contraction

Work on `ell^2(N_0)` and let `S` be the unilateral shift. Put

\[
R=\operatorname{diag}(1,1/2,0,0,\ldots).
\]

Then

\[
\boxed{S^*RS\preceq R.}
\tag{R-105630.1}
\]

This is the finite atomic version of `L-105625`: the profile is decreasing and
`S` is a causal inner isometry.

## 2. Physical trigonometric evaluation

Take positive source coefficients

\[
j_0=j_1=1
\]

and the contracted numerator coefficients

\[
t_0=1,
\qquad t_1=1/2.
\]

Define

\[
J(\theta)=1+2\cos\theta,
\]

\[
T(\theta)=1+{1\over2}e^{i\theta},
\qquad
U(\theta)=e^{i\theta}.
\]

The phase `U` is the boundary value of the simplest inner function. The source
ratio `(t_0,t_1)/(j_0,j_1)=(1,1/2)` is exactly the decreasing contraction
profile.

Nevertheless, at `theta=pi`,

\[
J(\pi)=-1,
\]

\[
\operatorname{Re}(U(\pi)T(\pi))=-{1\over2},
\]

and therefore

\[
\boxed{
J(\pi)-\operatorname{Re}(U(\pi)T(\pi))
=-{1\over2}<0.
}
\tag{R-105630.2}
\]

Thus the exact causal weighted contraction does not imply the desired
pointwise physical inequality.

## 3. Missing interface

The source theorem controls quadratic energy after a causal convolution. The
physical microscope evaluates an oscillatory off-diagonal Fourier kernel at
one spatial point. Point evaluation is not a positive compression of the
source metric in this fixture.

Consequently `POINTID105630` must supply genuine Xi-specific structure, such
as a positive reproducing kernel, total-positivity statement, or an exact
source-owned two-trace evaluation. It cannot be deleted merely because the
infinite-line phase is inner and contractive.

## 4. Scope

The fixture is not a model of the complete Xi current hierarchy and does not
refute a source-specific pointwise theorem. It proves only the logical
separation between weighted Hardy contraction and pointwise physical sign.
