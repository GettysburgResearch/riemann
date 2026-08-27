# L-105601 — Extremal-base descent is an exact backward Poisson evolution

Claim ID: `L-105601`  
Status: **PROVED EXACT HERGLOTZ/FOURIER IDENTITY**  
Created: 2026-08-24  
Depends on: `L-105451`, `L-105600`  
RH status: **not assumed**

## 1. Downward translation of one Pick ratio

Let `f` be the Pick function of `L-105600`, with Herglotz data

\[
f(z)=\alpha z+\beta+
\int_{\mathbb R}
\left({1\over t-z}-{t\over1+t^2}\right)d\mu(t).
\]

Fix a downward base displacement

\[
\delta>0
\]

and a physical microscope scale

\[
h>\delta.
\]

Put

\[
y=h-\delta>0.
\]

The field seen from the lower base is

\[
\boxed{
\mathcal C_h^{[\delta]}(a)
={1\over2}
\left[h\operatorname{Re}f'(a+iy)
      -\operatorname{Im}f(a+iy)\right].
}
\tag{L-105601.1}
\]

The good top-base field at the same physical scale is

\[
\mathcal C_h^{[0]}(a)
={1\over2}
\left[h\operatorname{Re}f'(a+ih)
      -\operatorname{Im}f(a+ih)\right].
\tag{L-105601.2}
\]

## 2. Universal signed kernel

Direct substitution of the Herglotz representation gives

\[
\boxed{
\begin{aligned}
\mathcal C_h^{[\delta]}(a)
={}&{\alpha\delta\over2}\\
&+{1\over2}
\int_{\mathbb R}
{\delta(a-t)^2-(2h-\delta)(h-\delta)^2
 \over
 ((a-t)^2+(h-\delta)^2)^2}
\,d\mu(t).
\end{aligned}
}
\tag{L-105601.3}
\]

Writing

\[
\lambda={\delta\over y},
\qquad
s={a-t\over y},
\]
the measure kernel becomes

\[
\boxed{
{1\over2y}
{\lambda s^2-(2+\lambda)
 \over(1+s^2)^2}.
}
\tag{L-105601.4}
\]

It has total integral

\[
\boxed{
\int_{\mathbb R}
{1\over2y}
{\lambda s^2-(2+\lambda)
 \over(1+s^2)^2}\,y\,ds
=-{\pi\over2},
}
\tag{L-105601.5}
\]

independently of the descent ratio `lambda`. It is negative in the central
region

\[
|s|<\sqrt{1+2/\lambda}
\]

and positive in the two remote tails. Base descent therefore does not destroy
the total negative mass; it moves part of that mass into a long-range positive
dipole tail.

## 3. Exact Fourier multiplier

Use

\[
\widehat g(\xi)=\int_{\mathbb R}e^{-ia\xi}g(a)\,da.
\]

For the measure part of (L-105601.3),

\[
\boxed{
\widehat{\mathcal C_h^{[\delta]}}(\xi)
=-{\pi\over2}
(1+h|\xi|)
 e^{-(h-\delta)|\xi|}
\widehat\mu(\xi).
}
\tag{L-105601.6}
\]

The affine term contributes the constant `alpha delta/2`. At the top base,

\[
\widehat{\mathcal C_h^{[0]}}(\xi)
=-{\pi\over2}
(1+h|\xi|)e^{-h|\xi|}\widehat\mu(\xi).
\]

Consequently, when `alpha=0`,

\[
\boxed{
\mathcal C_h^{[\delta]}
=e^{\delta|D|}\mathcal C_h^{[0]}.
}
\tag{L-105601.7}
\]

This is an exact **backward Poisson evolution**. The operator is not a bounded
positivity-preserving semigroup; it exponentially amplifies every physical
frequency. The anti-diffusive character previously seen in the scale variable
is now literal in the base-height variable as well.

## 4. A quantitative local-hole condition

Assume `alpha=0`. In the core `|t-a|<=y`, the kernel in (L-105601.3) obeys

\[
K_{\delta,y}(a-t)\le-{1\over4y}.
\tag{L-105601.8}
\]

Where its positive part is nonzero,

\[
K_{\delta,y}(a-t)_+
\le {\delta\over2(a-t)^2}.
\tag{L-105601.9}
\]

Therefore every nonnegative lower-base contact satisfies the necessary
inequality

\[
\boxed{
\mu([a-y,a+y])
\le
2\delta y
\int_{|t-a|>y}{d\mu(t)\over(t-a)^2}.
}
\tag{L-105601.10}
\]

A first contact is thus a precise local deficit of the extremal Herglotz
measure: the mass in one physical core must be paid completely by the remote
weighted tail.

## 5. Finite-measure firewall

Suppose `alpha=0`, `mu` is nonzero and compactly supported, and

\[
M=\mu(\mathbb R).
\]

For every fixed `h>delta>0`, expansion of (L-105601.3) gives

\[
\boxed{
\mathcal C_h^{[\delta]}(a)
={\delta M\over2a^2}+O_{h,\delta,\mu}(|a|^{-3})
>0
}
\tag{L-105601.11}
\]

for all sufficiently large `|a|`. If `alpha>0`, the positive constant
`alpha delta/2` already forces the same conclusion.

Thus no finite atomic/rational Pick model can validate a global downward-base
sign theorem. The infinite translation-dense Xi source is load bearing; finite
polynomial fixtures are intrinsically incapable of certifying the spatial
escape interface.

## 6. Xi specialization

At the maximal Xi zero height `beta_r`, put

\[
f_{r,\beta}(w)
={\Xi^{(r)}(w+i\beta_r)
 \over
 \Xi^{(r+1)}(w+i\beta_r)}.
\]

This is Pick by `L-105442`. The safe completed-zeta asymptotic gives

\[
{f_{r,\beta}(iy)\over iy}\longrightarrow0,
\]
so its Herglotz affine coefficient vanishes. For every attempted descent
`delta` and every scale `h>delta`, the Xi differential microscope therefore
obeys the exact anti-Poisson identity (L-105601.7).

The remaining theorem is no longer an unspecified spatial-infinity estimate:
it is the assertion that this particular infinite Herglotz measure remains in
the negative cone under the required backward-Poisson evolution.

## 7. Scope

The signed kernel and local-hole inequality do not prove that Xi has enough
local Herglotz mass. Equation (L-105601.11) is a firewall, not an Xi
counterexample. The source-specific input must exploit the positive reciprocal
Dirichlet family, the one-sided Hardy frame, or another mechanism unavailable
to finite measures. RH remains unproved.
