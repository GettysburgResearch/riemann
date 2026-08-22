# L-105208 — Every low-order Xi Levinson companion has exact mean Hermite–Biehler orientation

Claim ID: `L-105208`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-23  
Audited: 2026-08-23  
Depends on: the positive Xi Fourier kernel; `L-104512`; `L-105207`  
RH status: **not assumed**

Let

\[
F_k(z)=\Xi^{(k)}(z),
\qquad
E_{k,\lambda}(z)=F_k(z)-i\lambda F_{k+1}(z),
\qquad \lambda>0,
\]

and

\[
E_{k,\lambda}^{\#}(z)
=\overline{E_{k,\lambda}(\bar z)}
=F_k(z)+i\lambda F_{k+1}(z).
\]

The theorem applies to every fixed derivative order, including `k=0`.

## 1. Exact linewise Fourier norms

Use the two-sided positive representation

\[
\Xi(z)=\int_{\mathbb R}\varphi(u)e^{izu}\,du,
\qquad \varphi(u)=\Phi(|u|)>0.
\]

On `z=x-iy`, with `y>0`,

\[
E_{k,\lambda}(x-iy)
=
\int_{\mathbb R}(iu)^k(1+\lambda u)
\varphi(u)e^{ixu+yu}\,du,
\tag{L-105208.1}
\]

whereas `E#` has multiplier `1-lambda u`. Define

\[
A_k(y)=2\pi\int_{\mathbb R}u^{2k}\varphi(u)^2e^{2yu}\,du,
\]

\[
B_k(y)=2\pi\int_{\mathbb R}u^{2k+2}\varphi(u)^2e^{2yu}\,du,
\]

\[
C_k(y)=2\pi\int_{\mathbb R}u^{2k+1}\varphi(u)^2e^{2yu}\,du.
\tag{L-105208.2}
\]

Pairing positive and negative frequencies gives

\[
\boxed{
C_k(y)
=4\pi\int_0^\infty
u^{2k+1}\Phi(u)^2\sinh(2yu)\,du>0.
}
\tag{L-105208.3}
\]

Plancherel now yields

\[
\boxed{
\|E_{k,\lambda}(\cdot-iy)\|_2^2
=A_k(y)+2\lambda C_k(y)+\lambda^2B_k(y),
}
\tag{L-105208.4}
\]

\[
\boxed{
\|E_{k,\lambda}^{\#}(\cdot-iy)\|_2^2
=A_k(y)-2\lambda C_k(y)+\lambda^2B_k(y).
}
\tag{L-105208.5}

Therefore

\[
\boxed{
\|E_{k,\lambda}(\cdot-iy)\|_2^2
-
\|E_{k,\lambda}^{\#}(\cdot-iy)\|_2^2
=4\lambda C_k(y)>0.
}
\tag{L-105208.6}

In the `s`-plane this is exactly

\[
\int_{\mathbb R}
\left|\left(\xi^{(k)}+\lambda\xi^{(k+1)}\right)
\left({1\over2}+y+it\right)\right|^2dt
>
\int_{\mathbb R}
\left|\left(\xi^{(k)}-\lambda\xi^{(k+1)}\right)
\left({1\over2}+y+it\right)\right|^2dt.
\tag{L-105208.7}
\]

Thus the actual Levinson orientation is correct in line-averaged `L2` at
every derivative order and every positive distance from the critical line.

## 2. Optimal mean Levinson parameter

The normalized line orientation is

\[
\mathfrak H_{k,y}(\lambda)
={2\lambda C_k(y)\over A_k(y)+\lambda^2B_k(y)}.
\tag{L-105208.8}
\]

It is maximized at

\[
\boxed{
\lambda_{k,y}^{\rm opt}=\sqrt{A_k(y)/B_k(y)},
}
\tag{L-105208.9}
\]

with value

\[
\boxed{
\mathfrak H_{k,y}^{\rm opt}
={C_k(y)\over\sqrt{A_k(y)B_k(y)}}\in(0,1).
}
\tag{L-105208.10}
\]

At this parameter,

\[
\boxed{
{\|E^\#\|_2^2\over\|E\|_2^2}
={1-\mathfrak H_{k,y}^{\rm opt}
 \over1+\mathfrak H_{k,y}^{\rm opt}}.
}
\tag{L-105208.11}
\]

This is a source-determined best first-order Levinson scale, not a parameter
selected after a hypothetical zero.

## 3. Exact real-axis phase sum rule

Assume first that `F_k` and `F_(k+1)` have no common real zero, and choose a
continuous phase

\[
\theta_{k,\lambda}(t)=\arg E_{k,\lambda}(t).
\]

By `L-104512`,

\[
|E_{k,\lambda}(t)|^2\theta_{k,\lambda}'(t)
=\lambda\Lambda_k(t),
\qquad
\Lambda_k=F_{k+1}^2-F_kF_{k+2}.
\tag{L-105208.12}
\]

Every Xi derivative decays exponentially on the real axis, so integration by
parts gives

\[
\int_{\mathbb R}\Lambda_k(t)dt
=2\int_{\mathbb R}F_{k+1}(t)^2dt.
\]

Hence

\[
\boxed{
\int_{\mathbb R}|E_{k,\lambda}(t)|^2
\theta_{k,\lambda}'(t)dt
=2\lambda\int_{\mathbb R}F_{k+1}(t)^2dt>0.
}
\tag{L-105208.13}

Equivalently,

\[
\boxed{
\int |E|^2\theta' dt
=8\pi\lambda\int_0^\infty u^{2k+2}\Phi(u)^2du.
}
\tag{L-105208.14}

Common-zero cases follow by regular-level perturbation. Clockwise phase can
occur only with a strictly larger compensating counterclockwise
**amplitude-weighted** flux.

## 4. Relation to the exterior-square Gram

The numerator in (L-105208.12) is the kernel `Lambda_k` of `L-105207`.
Consequently all phase numerators, at every low derivative order, are entries
of one positive exterior-square Fourier Gram after translation and index
coupling. In particular, every Fejer-windowed derivative-index matrix of the
amplitude-weighted phase flux is positive semidefinite.

## 5. Scope

Mean Hermite--Biehler orientation is not pointwise Hermite--Biehler dominance.
Neither (L-105208.6) nor (L-105208.13) bounds the continued argument at one
fixed ordinate `T`; a small set of heights can still carry the complete inward
index. The remaining theorem is a height-localization or maximum-principle
upgrade to the single Levinson quotient of `L-105206`.
