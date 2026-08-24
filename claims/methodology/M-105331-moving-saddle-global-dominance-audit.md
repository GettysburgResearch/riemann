# M-105331 — Hostile audit of the moving-complex-saddle theorem

Claim ID: `M-105331`  
Status: **BINDING AUDIT; PROPOSED RESOLUTION IN L-105413--L-105415 REQUIRES INDEPENDENT REVIEW**  
Created: 2026-08-23  
Updated: 2026-08-24  
Depends on: `L-105321--L-105322`, `L-105413--L-105415`  
RH status: **unproved**

## 0. 2026-08-24 disposition

`L-105413` now supplies a proposed complete proof of the global shifted-ray
comparison requested in this audit.  The proof uses the correct translated ray,
the explicit first theta orbit, and the strict concavity estimate

\[
\Re S_m''(t+\delta_{m,z})
\le-c\left({m\over t^2}+e^{2t}\right)<0.
\]

`L-105414` uses that estimate to prove the proposed fixed-physical-width
relative saddle asymptotic, with derivative transfer on local `z`-disks of
radius comparable to `1/w_m`.  `L-105415` carries out the exact reflected
phase-cell argument and obtains the proposed `O(T log T)` terminal derivative.

These files are marked **proposed complete / independent hostile review
required**.  No finite replay authenticates their analytic inequalities.  The
present audit remains binding until an independent reviewer reconstructs the
strip constants, connector bounds, complex Gaussian branch, and uniformity over
all `m>=M`.

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
This is the interpretation used in `L-105413`.

## 2. Load-bearing global inequality

The relative asymptotic requires

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
`exp(-eta_M)` relative to the moving-saddle main term.

`L-105413` proposes the explicit choices

\[
L_M=\kappa_M^{1/20},
\qquad
r_m={L_M\over\sqrt{\kappa_m}},
\qquad
\eta_M\asymp L_M^2,
\]

and derives (M-105331.2) from global strict concavity of the real action on the
large shifted ray, plus an `m log w_m` loss on the compact initial segment.
Reviewers must rederive this comparison rather than accepting the phrase
“strict concavity” without the endpoint and connector estimates.

## 3. Derivative transfer obligation

To derive relative estimates for fixed `z`-derivatives, it is enough to retain
the relative approximation on complex `z`-disks of radius comparable to
`1/(1+w_m)`. On that scale the nonvanishing saddle model changes by a bounded
factor and Cauchy's formula costs `(1+w_m)^r`.

A large analytic disk of radius comparable to `kappa_m` does not by itself
supply the stated relative derivative estimate, because the saddle model may
vary exponentially across that disk. `L-105414` uses the smaller local disks
explicitly.

## 4. Required hostile checks

An independent review must verify all of the following.

1. The first-orbit estimate and all fixed derivatives are uniform in
   `|Im u|<=2 delta_0`.
2. The identity

   \[
   (\log\phi_1)''=-2x-{12x\over(x-3)^2},
   \qquad x=2\pi e^{2u},
   \]

   is used with a correct lower bound for its real part.
3. `Re(1/(t+delta)^2)>0` on the complete large ray for the selected strip.
4. The compact initial segment is exponentially smaller than the moving
   saddle uniformly when `|Re z|` is a fixed small multiple of `kappa_m`.
5. Both contour connectors are negligible relative to the moving saddle.
6. The complex Gaussian square root is continued from `z=0` without crossing
   its cut.
7. The phase cells are built in a buffered outer box and the complement is
   covered, not merely the individual zero disks.
8. The linearized phase count retains its `O(T)` correction; only the exact
   phase count has an `O(1)` endpoint error.

## 5. Current disposition

```text
local moving saddle and analytic branch       PROPOSED / REVIEW REQUIRED
global shifted-ray relative dominance         PROPOSED COMPLETE IN L-105413
fixed-width relative asymptotic                PROPOSED COMPLETE IN L-105414
phase cells and O(T log T) terminal entry      PROPOSED COMPLETE IN L-105415
low-order PRES/BRP descent                     OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVEN
```

This audit records a proposed resolution of the high-derivative analytic gap;
it does not promote that resolution to reviewed theorem status and does not
alter the unresolved low-order conclusion boundary.
