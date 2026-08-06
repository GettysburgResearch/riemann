# O-22101 — Prime energy as a critical local Dirichlet-Hardy embedding

Claim ID: `O-22101`  
Status: `PROPOSED CONNECTION / RESEARCH HANDOFF`  
Authoring agent: `gpt56-pro-18`  
Created: 2026-08-07  
Issue: #221

## 1. Vertical Hardy norm

Let

\[
 P_1(s)=\sum_p\frac{\log p}{p^s}
\]

in its initial half-plane, and let `H` be the prime-only safe window. For every
`sigma` to the right of all shifted poles, Laplace Plancherel gives

\[
\boxed{
\int_{\mathbb R}e^{-2\sigma x}|Q_H^{\mathbb P}(x)|^2dx
 =\frac1{2\pi}\int_{\mathbb R}
  |\widehat H(\sigma+it)|^2
  |P_1(1/2+\sigma+it)|^2dt.
}
\tag{O-22101.1}
\]

`T-21502` identifies the infimum of the admissible `sigma` with the rightmost
zeta-zero displacement. Thus RH is equivalent to finiteness of (O-22101.1) for
every `sigma>0`.

## 2. The easy Bohr norm and the hard local norm

At every fixed `sigma>0`, the prime coefficient square sum is

\[
 \sum_p\frac{(\log p)^2}{p^{1+2\sigma}}<\infty.
 \tag{O-22101.2}
\]

The prime number theorem gives the asymptotic

\[
 \boxed{
 \sum_p\frac{(\log p)^2}{p^{1+2\sigma}}
 \sim\frac1{4\sigma^2}
 \qquad(\sigma\downarrow0).
 }
 \tag{O-22101.3}
\]

This is the global Bohr/torus `H^2` norm of the prime-supported linear Dirichlet
series. It grows only polynomially.

The unresolved quantity in (O-22101.1) is a **local one-parameter vertical
embedding** of that Dirichlet series after the exact boundary multiplier. Dense
log-prime frequencies can be coherent on a bounded vertical interval even when
their Bohr phases are orthogonal on the full infinite torus.

Therefore the final RH arrow may be stated as a prime-specific critical local
embedding theorem:

\[
\boxed{
 \int_{\mathbb R}
  |\widehat H(\sigma+it)|^2
  |P_1(1/2+\sigma+it)|^2dt
 <\infty
 \quad(\sigma>0).
}
\tag{O-22101.4}
\]

A quantitative subexponential bound as `sigma->0` gives the same rightmost-zero
exponent.

## 3. Relation to existing Hardy spaces of Dirichlet series

General Hardy--Hilbert spaces of Dirichlet series admit local half-plane
embeddings only after a critical horizontal shift. The present series is much
more structured—linear and supported on primes—but `R-22102` shows why a naive
frequency-resolution argument cannot remove the shift: resolving all neighboring
log-primes forces an exponential diagonal.

Relevant primary reference:

- O. F. Brevig, *An embedding constant for the Hardy space of Dirichlet
  series*, arXiv:1606.03101.

The new research question is whether the exact pole-annihilating multiplier and
the arithmetic prime coefficients permit a signed local embedding unavailable
for arbitrary Dirichlet coefficients.

## 4. Why this connection matters

This interface imports mature tools from:

- local embeddings of Hardy spaces of Dirichlet series;
- Bohr lifts and infinite-dimensional torus methods;
- nonharmonic Fourier frames;
- Carleson embeddings;
- decoupling and hypercontractive estimates.

But any successful theorem must use the arithmetic centering. A generic local
embedding for arbitrary prime-supported coefficients is false because a dense
cluster of log-prime frequencies can be chosen with coherent coefficients.

## 5. Proof boundary

Equation (O-22101.1) is the ordinary Laplace-Plancherel identity in its
convergence half-plane. The critical extension (O-22101.4) is equivalent to RH
through `T-21502`; it is not proved here.
