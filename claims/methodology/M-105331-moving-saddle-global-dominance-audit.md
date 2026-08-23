# M-105331 — Hostile audit of the proposed moving-complex-saddle theorem

Claim ID: `M-105331`  
Status: **BINDING PROOF-OBLIGATION AUDIT; THEOREM REMAINS PROPOSED**  
Created: 2026-08-23  
Depends on: `L-105321--L-105322`  
RH status: **unproved**

## 1. Correct contour translation

Let `w_m` be the positive real saddle and `u_(m,z)` the proposed moving saddle.
The translated ray that passes through `u_(m,z)` is

\[
\delta_{m,z}+[0,\infty),
\qquad
\delta_{m,z}=u_{m,z}-w_m,
\tag{M-105331.1}
\]

not `u_(m,z)+[0,infinity)`. On this contour the saddle occurs at real
parameter `w_m`, while the connector at the origin has length `O(|delta|)`.
This is the interpretation under which the existing connector estimate can be
valid.

## 2. Missing load-bearing inequality

Local existence of the saddle and local derivative bounds do not themselves
prove a relative asymptotic. The proof requires a uniform global comparison
of the shifted contour with the moving saddle. A sufficient explicit target is

\[
\boxed{
\sup_{\substack{t\ge0\\|t-w_m|\ge r_m}}
\Re\left[
 S_m(t+\delta_{m,z})+iz(t+\delta_{m,z})
 -S_m(u_{m,z})-izu_{m,z}
\right]
\le-\eta_M,
}
\tag{M-105331.2}
\]

uniformly for `m>=M` and the claimed complex box, with

\[
r_m\sqrt{\kappa_m}\to\infty,
\qquad
\eta_M\to\infty.
\]

The origin connector and the far-right connector must separately be
`exp(-eta_M)` relative to the moving-saddle main term. The phrase “strict real
saddle inequalities remain strict” is not yet a quantitative proof of
(M-105331.2) when `|Re z|` is a fixed multiple of `kappa_m`.

## 3. Derivative transfer obligation

To derive relative estimates for fixed `z`-derivatives, it is enough to retain
the relative approximation on complex `z`-disks of radius comparable to
`1/(1+w_m)`. On that scale the nonvanishing saddle model changes by a bounded
factor and Cauchy's formula costs `(1+w_m)^r`.

A large analytic disk of radius comparable to `kappa_m` does not by itself
supply the stated relative derivative estimate, because the saddle model may
vary exponentially across that disk. The proof should use the smaller local
disks explicitly.

## 4. Correct current disposition

```text
local moving saddle and analytic branch       plausible / review required
global shifted-contour relative dominance     OPEN PROOF OBLIGATION
fixed-derivative Cauchy transfer               REPAIR SPECIFIED
O(T log T) terminal derivative entry           CONDITIONAL
Riemann Hypothesis                             UNPROVEN
```

This audit does not refute the moving-saddle theorem. It prevents its local
saddle calculations from being promoted to the global relative asymptotic
until (M-105331.2) and the connector bounds are proved from the explicit Xi
kernel.
