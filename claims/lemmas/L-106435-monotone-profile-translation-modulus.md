# L-106435 — Monotone source profiles have a sharp one-sided translation modulus

Claim ID: `L-106435`  
Status: **PROVED EXACT; SAFE-REGION PHASE-COLLISION INPUT**  
Created: 2026-08-25  
Depends on: sibling PR #729 `L-105623--L-105628`; `L-106441`  
RH status: **not assumed**

Let \(r:[0,\infty)\to[0,\infty)\) be nonincreasing and integrable, and put
\(f=\sqrt r\). For \(h\ge0\), define

\[
\omega_r(h)
=
\int_0^\infty|f(x+h)-f(x)|^2\,dx.
\]

Since \(f(x)\ge f(x+h)\ge0\),

\[
(f(x)-f(x+h))^2
\le
f(x)^2-f(x+h)^2
=
r(x)-r(x+h).
\]

Integration telescopes, giving

\[
\boxed{
\omega_r(h)
\le
\int_0^h r(x)\,dx
\le
h\,r(0).
}
\tag{L-106435.1}
\]

The constant one is sharp in the hard-step limit.

## Causal all-pass commutator

Let \(V\) be a causal convolution operator on \(L^2(0,\infty)\), with
nonconstant Fourier kernel \(\widehat V(h)\) supported on \(h\ge0\). Whenever
the commutator is Hilbert--Schmidt, the kernel formula of sibling `L-105623`
and (L-106435.1) give

\[
\boxed{
\|[V,M_{\sqrt r}]\|_{\mathcal S_2}^2
\le
\int_0^\infty
|\widehat V(h)|^2
\left(\int_0^h r(x)\,dx\right)dh
\le
r(0)\int_0^\infty h|\widehat V(h)|^2dh.
}
\tag{L-106435.2}
\]

For the Xi current--Turán profile of PR #729, strict log-concavity proves the
required monotonicity, and innerness supplies causality throughout the safe
region above the adjacent derivative zero height. Thus the physical
phase-collision commutator there is bounded by one favorable
half-derivative channel.

This applies to the literal causal vertical-shift phase authenticated on PR
#729. `L-106441` proves that a finite-alpha derivative companion has a
different divisor and need not be inner even when the vertical-shift quotient
is inner. Therefore (L-106435.2) transfers to the endpoint programme only
after a source-exact factorization, product-cocycle estimate, or
zero-crossing-free homotopy. Below that bridge, the adverse derivative-
companion divisor remains the signed pole tail isolated in `T-106440`.
