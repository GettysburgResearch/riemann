# L-105645 — Strong log-concavity sandwiches the Xi current profile by a Maxwell law

Claim ID: `L-105645`  
Status: **PROVED EXACT STRONG-LOG-CONCAVE SOURCE THEOREM; INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-25  
Depends on: `L-105624`, `L-105640--L-105641`  
RH status: **not assumed**

## 1. Strong source curvature

Put

\[
\kappa_0={20476\over2345}>8.
\tag{L-105645.1}
\]

`L-105640` proves for the standard Xi kernel

\[
\boxed{
\psi''(u)>\kappa_0,
\qquad
\psi=-\log\Phi.
}
\tag{L-105645.2}

Fix a sum frequency `s>=0`. The exterior-square conditional density of
`L-105624` is

\[
q_s(x)
={1\over Z_s}
 x^2
 e^{-\psi(s/2+x)-\psi(s/2-x)},
\qquad x>0.
\tag{L-105645.3}

## 2. Monotone-likelihood domination by a Maxwell law

Let

\[
\boxed{
g_{\kappa_0}(x)
={4\kappa_0^{3/2}\over\sqrt\pi}
 x^2e^{-\kappa_0x^2},
\qquad x>0.
}
\tag{L-105645.4}

This is a probability density. Differentiating the logarithm of the likelihood
ratio gives

\[
\begin{aligned}
{d\over dx}\log{q_s(x)\over g_{\kappa_0}(x)}
={}&-\psi'(s/2+x)+\psi'(s/2-x)+2\kappa_0x.
\end{aligned}
\tag{L-105645.5}

By (L-105645.2),

\[
\psi'(s/2+x)-\psi'(s/2-x)
=
\int_{s/2-x}^{s/2+x}\psi''(t)dt
\ge2\kappa_0x.
\]

Therefore

\[
\boxed{
{d\over dx}\log{q_s(x)\over g_{\kappa_0}(x)}
\le0.
}
\tag{L-105645.6}

The likelihood ratio is nonincreasing. Since both densities have mass one,
`q_s/g_(kappa_0)` crosses the level one at most once, from above to below.
Consequently

\[
\boxed{q_s\preceq_{\rm st}g_{\kappa_0},}
\tag{L-105645.7}

meaning that `q_s` is first-order stochastically dominated by the Maxwell law.
Every nondecreasing test function has no larger expectation under `q_s`.

## 3. The Maxwell hyperbolic moment is exact

For `H>=0`, the function

\[
G_H(x)={\sinh(2Hx)\over2Hx}
\]

is nondecreasing on `(0,infinity)`. Hence (L-105645.7) gives

\[
\mathbb E_{q_s}G_H(X)
\le
\mathbb E_{g_{\kappa_0}}G_H(X).
\tag{L-105645.8}

The right side can be evaluated exactly. Differentiate

\[
\int_0^\infty e^{-\kappa_0x^2}\cosh(2Hx)dx
={\sqrt\pi\over2\sqrt{\kappa_0}}
 e^{H^2/\kappa_0}
\]

with respect to `H`. One obtains

\[
\int_0^\infty
x e^{-\kappa_0x^2}\sinh(2Hx)dx
={\sqrt\pi H\over2\kappa_0^{3/2}}
 e^{H^2/\kappa_0}.
\]

Substitution in (L-105645.4) yields

\[
\boxed{
\mathbb E_{g_{\kappa_0}}
{\sinh(2HX)\over2HX}
=e^{H^2/\kappa_0}.
}
\tag{L-105645.9}

## 4. Two-sided current-profile theorem

`L-105641` gives

\[
R_H(s)
={e^{-Hs}\over
 \displaystyle\mathbb E_{q_s}
 {\sinh(2HX)\over2HX}}.
\]

The lower bound `sinh(z)/z>=1` and the upper expectation bound
(L-105645.8)--(L-105645.9) prove

\[
\boxed{
e^{-Hs-H^2/\kappa_0}
\le
R_H(s)
\le
e^{-Hs}
\qquad(H>=0,\ s>=0).
}
\tag{L-105645.10}

For a base `b`, physical scale `h`, and total height `H=b+h`,

\[
\boxed{
{h\over H}e^{-H^2/\kappa_0}e^{-H\xi}
\le
r_{b,h}(\xi)
\le
{h\over H}e^{-H\xi}.
}
\tag{L-105645.11}

Thus the actual current metric is uniformly equivalent to the canonical
exponential Paley--Wiener metric.

## 5. Critical-height numerical form

For

\[
0\le H\le{1\over2},
\]

one has

\[
e^{-H^2/\kappa_0}
\ge e^{-1/(4\kappa_0)}
>1-{1\over4\kappa_0}
={79559\over81904}
>{97\over100}.
\tag{L-105645.12}

Therefore throughout the complete critical-height range,

\[
\boxed{
{97\over100}e^{-H\xi}
< R_H(\xi)
\le e^{-H\xi}.
}
\tag{L-105645.13}

The current profile differs from the elementary exponential source metric by
less than three percent in multiplicative order.

## 6. Exact model-space consequence

For every finite inner function `B`, operator order gives

\[
\boxed{
e^{-H^2/\kappa_0}
\operatorname{tr}_{K_B}M_{e^{-H\xi}}
\le
\operatorname{tr}_{K_B}M_{R_H}
\le
\operatorname{tr}_{K_B}M_{e^{-H\xi}}.
}
\tag{L-105645.14]

For one zero at depth `y`,

\[
\boxed{
e^{-H^2/\kappa_0}{2y\over H+2y}
\le
\langle M_{R_H}\phi_y,\phi_y\rangle
\le
{2y\over H+2y}.
}
\tag{L-105645.15]

At `H<=1/2`, the lower constant may be replaced by `97/100`.

Hence the soft-depth price of `L-105643` is not an artifact of replacing the
actual current profile by an exponential majorant. The two metrics are
quantitatively equivalent at the conclusion-facing heights.

## 7. Scope

A two-sided source-metric comparison is still not an unweighted degree theorem
and is not a pointwise physical evaluation theorem. A zero at depth `y->0`
remains cheap in both equivalent metrics. The theorem narrows
`BCOLLAR105643/HOWNXFER105644`; it does not prove either gate or RH.