# D-0001 — Cutoff-free finite Weil block and normalization

Claim ID: D-0001  
Title: Cutoff-free finite Weil block and normalization  
Status: PROPOSED  
Authoring agent: `gpt56-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: Guinand--Weil explicit formula; finite dictionary source listed in `LITERATURE.md`  
Scope: Riemann zeta function only  
Related counterexample candidates: none

## Statement

Fix a real cutoff `c>1` and an integer `N>=0`.  Set

\[
 L=\log c,\qquad \Delta=\frac{L}{2\pi},\qquad \rho=\frac{2\pi}{L}.
\]

For a real even-sector vector `v=(v_0,...,v_N)`, define full coefficients

\[
 u_0=v_0,\qquad u_k=u_{-k}=\frac{v_k}{\sqrt2}\quad(1\le k\le N),
\]

and

\[
 T_v(t)=\sum_{m=-N}^{N}u_m e^{2\pi i m t},\qquad
 K_v(\omega)=2\int_0^\omega T_v(t)T_v(\omega-t)\,dt.
\]

Define

\[
 \widehat g_v(\xi)=
 \begin{cases}
 \pi K_v(1-|\xi|/\Delta),&|\xi|\le\Delta,\\
 0,&|\xi|>\Delta,
 \end{cases}
 \qquad
 g_v(z)=\int_{-\Delta}^{\Delta}\widehat g_v(\xi)e^{2\pi i z\xi}\,d\xi.
\]

For a continuously differentiable source `psi`, let its divided-difference
matrix on indices `{-N,...,N}` be

\[
 (Q_\psi)_{mn}=
 \begin{cases}
 \dfrac{\psi(m)-\psi(n)}{m-n},&m\ne n,\\[1ex]
 \psi'(m),&m=n.
 \end{cases}
\]

Use the prime, pole, and archimedean sources

\[
 \psi_p^{(c)}(x)=-\frac1\pi\sum_{q=p^a\le c}
 \frac{\Lambda(q)}{\sqrt q}
 \sin\!\left(2\pi x\left(1-\frac{\log q}{L}\right)\right),
\]

\[
 \psi_0(x)=\frac1\pi\int_0^L2\cosh(y/2)
 \sin\!\left(2\pi x\left(1-\frac yL\right)\right)\,dy,
\]

and

\[
 \psi_{\mathbb R,T}(x)=\frac1{2\pi^2}\int_{-T}^{T}h_+(r)
 \mathcal S(r,x,L)\,dr,
\]

where

\[
 h_+(r)=\operatorname{Re}\psi_\Gamma\!\left(\frac14+\frac{ir}{2}\right)-\log\pi,
\quad
 \mathcal S(r,x,L)=\int_0^L\sin\!\left(2\pi x\left(1-\frac yL\right)\right)\cos(ry)\,dy.
\]

The project normalization of the cutoff-free finite Weil block is

\[
 Q_N(c)=Q_{\psi_p^{(c)}}+Q_{\psi_0}
       +\lim_{T\to\infty}Q_{\psi_{\mathbb R,T}},
\]

with the limit interpreted entrywise.  Even-sector contraction means

\[
 \langle v,Q_N(c)v\rangle
 =\sum_{m,n=-N}^{N}u_m u_n\,(Q_N(c))_{mn}.
\]

## Definitions and implementation convention

The exploratory X-0001 code evaluates the equivalent cutoff-free closed forms
for the pole and archimedean blocks.  It does **not** approximate the last
matrix by selecting a finite `T`.

The discovery code accepts decimal cutoffs `c>=2`.  The mathematical definition
allows `c>1`; extending the code below 2 is routine but unnecessary for the
initial prime-supported search.

## Motivation

Compact support of `widehat g_v` makes the prime-power contribution finite:
prime powers `q>c` vanish from the explicit formula.  Thus a possible RH
counterexample can be encoded by a finite vector and a finite matrix whose
entries are amenable to interval enclosure.

## Analytic domain audit

- `zeta(s)` is understood by its meromorphic continuation with its pole at
  `s=1`; the zero set used later contains nontrivial zeros only.
- `digamma(1/4+ir/2)` has no pole for real `r`.
- The logarithm `L=log c` is the real natural logarithm for `c>1`; no complex
  logarithm branch occurs here.
- `g_v` is intended to be entire of finite exponential type, with compactly
  supported Fourier transform and sufficient horizontal-strip decay for the
  Guinand--Weil formula.  This admissibility is a dependency to be independently
  audited in Q-0004.
- The cutoff-free archimedean limit must be established entrywise.  A finite-T
  matrix is not interchangeable with this definition without a rigorous tail
  bound.

## Dependency audit

The exact normalization and the entrywise identification are currently traced
to the primary sources in `LITERATURE.md`, especially the July 2026 finite
dictionary paper.  X-0001 independently transcribes the released closed forms
but does not yet constitute an independent derivation.

## Gap audit

1. A sign swap among source blocks would invalidate all searches.
2. A finite-T approximation can have a different inertia from `Q_N(c)`.
3. Ordinary mpmath values do not provide directed-rounding enclosures.
4. The basis normalization `v_k/sqrt(2)` must be kept consistent between full
   and even sectors.
5. A real cutoff between prime powers changes `L` continuously even though the
   finite prime set is unchanged.

## Adversarial tests

X-0001 checks exact integer prime-power enumeration, matrix symmetry, parity,
even-projector orthonormality, precision stability, geometric-tail decay, and
eigenpair residuals.  These tests are necessary but not sufficient to verify
the analytic normalization.

## Remaining uncertainty

The definition is complete-looking but has not been independently reconstructed
from the classical explicit formula inside this repository.  Status remains
`PROPOSED`.

## Suggested next attack

Have an independent verifier derive the source signs and the autocorrelation
normalization from the completed zeta explicit formula, then compare exact
small matrices entry by entry against X-0001 and an Arb implementation.
