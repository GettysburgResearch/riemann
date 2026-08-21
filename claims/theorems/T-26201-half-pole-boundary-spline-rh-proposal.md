# T-26201 — Half-pole boundary-spline proposal for the Riemann Hypothesis

Claim ID: `T-26201`  
Title: Boundary-Jet Domination for completed dyadic carry sources implies positivity of the reciprocal-zeta Green profile and RH  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW OF `L-26204`**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-26201`–`L-26204`; Landau's one-sign theorem; zeta functional equation  
Scope: complete conditional deduction; no finite numerical ladder

## 1. Surviving exact carry state

Define

\[
\boxed{
\mathfrak C(y)
=
\sum_{d\le y}\frac{\mu(d)}{\sqrt d}
\left(
8\sqrt{y/d}-7-\frac32\log(y/d)
\right),
\qquad y\ge1.}
\tag{T-26201.1}
\]

The exact carry–Möbius inversion gives this profile as the scaling state of the
finite carry inverse. Its Mellin transform is

\[
\boxed{
\int_1^\infty\mathfrak C(y)y^{-z-1}dy
=
\frac{(z+\frac12)(z+\frac32)}
{z^2(z-\frac12)\zeta(z+\frac12)},
\qquad\Re z>\frac12.}
\tag{T-26201.2}
\]

The old conditional-Hankel proof of its positivity is not used.

## 2. New sign mechanism

For every endpoint `Y`, complete the truncated Möbius source by the weighted
dyadic difference

\[
I-2^{-1/2}\tau_{\log2}.
\]

The complete source is half-pole-null. `L-26201` makes its interior Green form a
rank-one positive Gram. `L-26202` expands every quotient-cell remainder into a
positive triangular B-spline bulk and endpoint jets. `L-26203` identifies the
oversupport jets exactly with the dyadic Mertens shell and its logarithmic
companion.

`L-26204` assembles the actual two-frequency reflected block in those same
coordinates and proposes the source-image LMI

\[
D_Y+R_Y\succeq N_Y.
\]

The exact complete identity then gives

\[
\boxed{\mathfrak C(Y)\ge0\qquad(Y\ge Y_0).}
\tag{T-26201.3}
\]

The finitely many earlier endpoints can be checked directly or absorbed by a
compact correction; Landau's theorem depends only on the tail sign.

## 3. Landau continuation

Let `sigma_c` be the abscissa of convergence of the Mellin integral in
(T-26201.2). Trivial estimates give `sigma_c<=1/2`.

If `sigma_c>0`, eventual nonnegativity of `mathfrak C` and Landau's theorem force
a singularity at the positive real point `sigma_c`. But the meromorphic right
side of (T-26201.2) is regular on the positive real axis:

- `zeta(z+1/2)` has no real zero for `z>0`;
- the point `z=1/2` is removable because
  `(z-1/2)zeta(z+1/2)->1`.

Therefore

\[
\boxed{\sigma_c\le0.}
\tag{T-26201.4}
\]

The Mellin integral is holomorphic in `Re z>0`.

## 4. Pole exclusion

If `rho` is a nontrivial zeta zero with `Re rho>1/2`, then

\[
z_\rho=\rho-1/2
\]

lies in `Re z>0` and produces an uncancelled pole in (T-26201.2). This
contradicts holomorphy of the Mellin integral. Hence zeta has no zero to the
right of the critical line. The functional equation and conjugation symmetry
exclude the reflected half.

Thus

\[
\boxed{\mathrm{RH}.}
\tag{T-26201.5}
\]

## 5. Finite-minorant alternative

A weaker form of `BJD` may certify only

\[
\mathfrak C(Y)\ge-O(\log^A Y)
\]

or directly emit a finite nonnegative carry minorant with polylogarithmic
boundary debt. The exact carry mass–slack law then gives

\[
P(X)\ge4\sqrt X-O(\log^{A'}X),
\]

and the reviewed square-screw/Landau transfer also proves RH. This variant does
not require pointwise positivity of the global profile.

## 6. Distinction from earlier proposals

The proof does not invoke:

- ordinary zero-mass conditional-Hankel positivity;
- a global positive Hankel approximation of the stop-loss ramp;
- bounded endpoint-face rank;
- a generic balanced Type-II operator norm;
- monotone positive-part covering;
- a finite positive ladder.

The coherent Möbius shell is an explicit boundary jet and is paid inside the
source-specific reflected/digital LMI.

## 7. Exact status

The carry inversion, Mellin transform, dyadic alignment, digital endpoint
identity, half-pole factorization, and B-spline formula are supplied exactly.
The proposed proof stands or falls on the complete boundary-jet assembly and LMI
of `L-26204`.

This is a full proposal for review, not an independently verified proof of RH.
