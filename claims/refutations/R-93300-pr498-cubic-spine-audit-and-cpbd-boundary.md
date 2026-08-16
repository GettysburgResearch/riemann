# R-93300 — Hostile audit of the frozen centered-cubic spine and its exact boundary

Claim ID: `R-93300`  
Status: **INDEPENDENT RECONSTRUCTION / NORMATIVE SCOPE FIREWALL**  
Created: 2026-08-16  
Frozen proposal: PR #498 at `6cc0da2fa5711017e260ebdcea4ba8c22e453288`  
RH status: **unproved**

## 1. Reconstructed finite identity

Let

\[
c_\circ(m)=
\Lambda(m)-4\mathbf 1_{4\mid m}\Lambda(m/4)
+3(\log4)\sum_{a\ge1}\mathbf 1_{m=4^a},
\]

and let `Q_(circ,N)`, `M_N`, and `V_(circ)(N)` have the normalization of frozen `L-93250`. The predecessor in the reflected cell is `N-j-1`. For

\[
w(\theta)=\theta(1-\theta)-\frac16,
\qquad
K(x)=\frac{x(1-x)(2x-1)}3,
\]

one has exactly

\[
\int_0^1w=0,
\qquad
\int_0^1w^2=\frac1{180},
\qquad
K'=2w,
\]

and

\[
\boxed{
\mathcal A_\circ(N)=
\int_0^1w(\theta)Q_{\circ,N}(\theta)d\theta
=\sum_{m\le N}c_\circ(m)K(m/N).
}
\]

The normalization bridge is

\[
\boxed{|\mathcal A_\circ(N)|^2\le\frac N{180}\mathscr V_\circ(N).}
\]

These identities survive exact rational replay.

## 2. Mellin and interpolation audit

The Mellin multiplier is

\[
\widehat K(s)=\frac{s-1}{3(s+1)(s+2)(s+3)}.
\]

The complete source Dirichlet series is

\[
(1-4^{1-s})\left(-\frac{\zeta'}{\zeta}(s)\right)
+3(\log4)\frac{4^{-s}}{1-4^{-s}}.
\]

At a nontrivial zero `rho` in the open strip, neither `s-1`, nor `1-4^(1-s)`, nor any displayed denominator vanishes. The four-adic summand is holomorphic there. Thus every open-strip zero remains a nonremovable pole.

For `N<=X<N+1`, the endpoint term is absent because `K(1)=0`, and

\[
|K(m/X)-K(m/N)|\le\frac{m}{3N^2}.
\]

The elementary bound `sum_(m<=N)m|c_circ(m)|<<N^2` therefore gives `A_circ(X)-A_circ(N)=O(1)`. The integer-to-real bridge is valid.

## 3. Exact disposition of the frozen equivalences

Subject only to classical meromorphic continuation, the functional equation, and the standard RH-to-von-Koch implication, the chain

\[
\mathscr V_\circ(N)\ll\log^A(2N)
\Longrightarrow
\mathcal A_\circ(X)\ll_\varepsilon X^{1/2+\varepsilon}
\Longrightarrow\mathrm{RH}
\]

is valid. The mean coordinate is not used.

```text
L-93250 centered cubic identity              VERIFIED
T-93251 centered-energy criterion            VERIFIED WITH FROZEN ANALYTIC INPUTS
T-93253 mean-free major-arc reduction         CONDITIONAL ON FROZEN FOURIER INPUTS
R-93254 cardinality firewall                 VERIFIED AND BINDING
T-93255 CPBD estimate                         OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```

## 4. Binding prohibition

`R-93254` remains normative. A lower bound on aligned prime blocks, a diagonal estimate, or common-half-plane participation cannot be promoted into cancellation. Any successor must use additional arithmetic: a Möbius factor, carrier phases, additive moduli, endpoint variation, or an equivalent source-specific mechanism.

The present successor does not rename CPBD. It replaces the prime-only frontier by an exact Vaughan decomposition, proves every unbalanced range safe, introduces a zero-safe higher-order endpoint family, and isolates the remaining near-square Möbius-prime hyperbola together with its exact carrier factorization.
