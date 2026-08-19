# R-99710 — The positive continuous-owner completion carries a genuine real pole and is not itself an RH proof

Claim ID: `R-99710`  
Status: **PROVED STATEMENT-TO-USE FIREWALL**  
Created: 2026-08-20  
Depends on: `L-99712`; the scalar Mellin transform of PR #647  
RH status: **unproved**

Let `z=s+1/2`.  The Dirichlet series of `c_u` is

\[
\sum_{n\ge1}{c_u(n)\over n^z}
=
{(1-67^{-z})\zeta(z-u)\over\zeta(z)}.
\tag{R-99710.1}
\]

Therefore the Mellin transform of the positive endpoint packet
`mathcal F_u` is

\[
\boxed{
\int_1^\infty\mathcal F_u(x)x^{-s-1}\,dx
=
{(1-67^{-z})(s+3/2)\zeta(z-u)
 \over s(s-1/2)\zeta(z)}.
}
\tag{R-99710.2}
\]

The extra zeta factor has a genuine pole at

\[
z-u=1,
\qquad s=u+1/2>0.
\tag{R-99710.3}
\]

That real singularity is exactly the Landau singularity required by the
nonnegative density `mathcal F_u`.  Thus coefficientwise positivity of
`L-99712` does not force the transform to continue through `Re s>0` and cannot
exclude off-line zeros.

## Distributional pole subtraction also fails positivity

The formal operator that cancels the real pole is

\[
\left(u+\frac12-x{d\over dx}\right)\mathcal F_u.
\tag{R-99710.4}
\]

The SHARP kernel has a unit jump at every activation `x=n`.  In the
Stieltjes/distributional derivative, (R-99710.4) therefore contains the
negative atom

\[
-{c_u(n)\over\sqrt n}\,\delta_n
\tag{R-99710.5}
\]

at every active coefficient.  Ignoring these atoms and differentiating only on
open cells falsely produces a positive leading term; the omitted jump measure
is exactly what cancels the positive-real pole.

Similarly, no positive mixture over real `u` can cancel (R-99710.3): a positive
measure has a strictly positive Laplace transform at a real argument.

```text
continuous-order coefficient positivity    PROVED
positive endpoint Riesz completion          PROVED
real Landau singularity                     PRESENT / LOAD-BEARING
cellwise derivative pole subtraction        INVALID WITHOUT NEGATIVE ATOMS
positive-u mixture pole cancellation        IMPOSSIBLE
```

The correct use of `L-99712` is therefore as a positive comparison/diagnostic.
The conclusion-facing route must remain phase-sensitive, where the Cauchy–Poisson
owner gap introduces coercivity without a new real-axis pole.