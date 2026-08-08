# L-23809 — Cofinal FGCM compactness collapses to the global Gamma factor

Claim ID: `L-23809`  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA — PENDING INDEPENDENT REVIEW**  
Scope: relation between `FGCM` of `L-23807` and global `GCF` of `L-23805`  
RH status: **unproved**

## 1. Statement

Assume there is a cofinal sequence `X_j -> infinity` with finite Gamma–carry minorants `b_j=b_(X_j)` satisfying `L-23807.4` and

\[
\int b_j(t)dt\longrightarrow1.
\tag{L-23809.1}
\]

Then there exists a positive finite measure `beta` on `[0,infinity)` of total mass one such that, with

\[
c(du)=8e^{u/2}\,\beta(du),
\]

one has the exact global convolution identity

\[
\boxed{c*\kappa=t\,dt.}
\tag{L-23809.2}
\]

Consequently the Laplace transform of `beta` is exactly the quotient `A(s)` of `L-23805`, so `GCF` holds in the measure sense. By uniqueness of Laplace inversion it agrees with the explicit Möbius–Riesz inverse where that inverse is represented as a locally integrable function.

Thus a cofinal FGCM family with asymptotically full mass cannot avoid global Gamma/carry factor positivity by sending its mass to the moving endpoint.

## 2. Uniform local lower bound for the carry kernel

Take

\[
\delta=\log(4/3).
\]

For `0<=v<=delta`, one lies in the first carry cell and

\[
K(e^v)=2e^{-v}-1\ge\frac12.
\]

Also `e^{-v/2}>=sqrt(3)/2>3/4`. Therefore

\[
\boxed{\kappa(v)=e^{-v/2}K(e^v)\ge\frac38
\qquad(0\le v\le\delta).}
\tag{L-23809.3}
\]

## 3. Uniform exponential tightness

The FGCM inequality is

\[
\int_0^t8e^{u/2}b_j(u)\kappa(t-u)du\le t.
\tag{L-23809.4}
\]

For `delta<=t<=T_(X_j)`, restrict to `t-delta<=u<=t` and use (L-23809.3):

\[
3e^{(t-\delta)/2}
\int_{t-\delta}^{t}b_j(u)du\le t.
\]

Hence

\[
\boxed{
\int_{t-\delta}^{t}b_j(u)du
\le {t\over3}e^{-(t-\delta)/2}.}
\tag{L-23809.5}
\]

Covering `[L,T_(X_j)]` by consecutive intervals of length `delta` and using the terminal partial interval with `t=T_(X_j)` gives an absolute constant `C_delta` such that

\[
\boxed{
\int_L^{T_(X_j)}b_j(u)du
\le C_\delta(1+L)e^{-L/2}}
\tag{L-23809.6}
\]

for every `j` with `T_(X_j)>=L+delta`.

Thus the positive measures `b_j(t)dt` are uniformly tight. In particular the finite horizon cannot hide asymptotically unit mass in a boundary layer.

## 4. Total mass cannot exceed one in the limit

Put

\[
J(R)=\int_0^R e^{-v/2}\kappa(v)dv.
\]

From `L-23804.4` (equivalently the removable value of the shifted Mellin transform),

\[
\boxed{J(\infty)=\frac12.}
\tag{L-23809.7}
\]

Multiply (L-23809.4) by `e^{-t/2}` and integrate from `0` to `T=T_(X_j)`. Fubini gives

\[
8\int_0^T b_j(u)J(T-u)du
\le\int_0^Tte^{-t/2}dt<4.
\tag{L-23809.8}
\]

For fixed `L<T`,

\[
8J(T-L)\int_0^L b_j(u)du<4.
\]

Let first `j->infinity` and then `L->infinity`, using tightness and (L-23809.7). Every weak limit `beta` therefore satisfies

\[
\beta([0,\infty))\le1.
\]

The assumed lower mass limit (L-23809.1) and tightness give the reverse inequality, so

\[
\boxed{\beta([0,\infty))=1.}
\tag{L-23809.9}
\]

## 5. Passage to the global convolution inequality

By tightness, take a weakly convergent subsequence

\[
b_j(t)dt\Rightarrow\beta.
\]

For every nonnegative compactly supported continuous test function `phi`, integrate the finite convolution inequality against `phi(t)dt`, use Fubini, and pass to the limit. The inner convolution of `phi` with the locally integrable carry kernel is continuous in the source coordinate, so weak convergence applies. One obtains

\[
\boxed{c*\kappa\le t\,dt}
\tag{L-23809.10}
\]

as positive locally finite measures on the whole half-line.

## 6. Critical-mass conservation forces equality

Integrate (L-23809.10) against the strictly positive weight `e^{-t/2}`. By Fubini, (L-23809.7), and (L-23809.9),

\[
\int_0^\infty e^{-t/2}d(c*\kappa)(t)
=8\,\beta([0,\infty))\,J(\infty)
=4.
\]

But

\[
\int_0^\infty te^{-t/2}dt=4.
\]

The residual measure

\[
t\,dt-c*\kappa
\]

is nonnegative and has zero integral against a strictly positive function. Hence it is identically zero. This proves (L-23809.2).

## 7. Laplace identification

For `s>1/2`, taking Laplace transforms in (L-23809.2) gives

\[
8\int_0^\infty e^{-(s-1/2)u}\beta(du)\,\widehat\kappa(s)
={1\over s^2}.
\]

Using the exact shifted carry transform from `L-23804`, the transform of `beta` is precisely

\[
\boxed{
{(r+1)(r+2)\over8r(r+1/2)^2\zeta(r+1)}=A(r),
\qquad r=s-1/2>0.}
\tag{L-23809.11}
\]

This is the Gamma/carry quotient of `L-23805`.

## 8. Consequences for the proof programme

The intended distinction

```text
GCF  = one global exact positive factor
FGCM = moving finite positive minorants with vanishing mass defect
```

does not survive the sharp FGCM mass requirement: local positivity of `kappa` forces tightness, and the conserved critical mass forces any cofinal full-mass limit to be the exact global factor.

Therefore an unconditional proof of FGCM at the stated strength is already a proof of GCF. Finite-horizon boundary escape is not an independent mechanism.

This does not refute FGCM; it identifies its exact strength.

## Review boundary

Reviewers should check:

1. the first-cell lower bound (L-23809.3);
2. the uniform tail covering in (L-23809.6), including the terminal partial interval;
3. weak passage through the convolution kernel at reset knots;
4. the critical transform value `J(infinity)=1/2`;
5. Laplace normalization in (L-23809.11).
