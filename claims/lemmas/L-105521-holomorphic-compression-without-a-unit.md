# L-105521 — Holomorphic compression does not require a zero-free unit

Claim ID: `L-105521`  
Status: **PROVED EXACT, FINITE HERMITIAN ALGEBRA**  
Created: 2026-08-24  
Depends on: elementary inertia monotonicity  
RH status: **not assumed**

Let \(H\) be a finite-dimensional Hermitian form and let
\(V:\mathbb C^d\to\mathbb C^M\) be an observation map.  The compressed form is

\[
C=V^*HV.
\]

For any source-fixed linear map \(A:\mathbb C^r\to\mathbb C^d\),

\[
C_A=A^*CA=(VA)^*H(VA),
\]

so

\[
\boxed{\nu_+(C_A)\le\nu_+(H).}
\tag{L-105521.1}
\]

No injectivity or invertibility of \(A\) is required.

In the residue setting, replacing analytic observations
\(\phi_j\) by \(p\phi_j\), for any holomorphic \(p\) fixed before the critical
signs are seen, produces another valid compression.  The function \(p\) need
not be zero-free.  Zeros of \(p\) can delete sampled directions, but they
cannot create positive directions absent from the full residue form.

A unit is required only for the stronger assertion that the **full inertia is
preserved by congruence**.  Therefore the scalar zeros of the triangular Wick
polynomial do not by themselves invalidate a lower-bound compression.  The
load-bearing problem is instead whether the intended one-sided source
coordinate is represented by the actual off-real Hermitian contour; that
polarization issue is recorded in `R-105520`.
