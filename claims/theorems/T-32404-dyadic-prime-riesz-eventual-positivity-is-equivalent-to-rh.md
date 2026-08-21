# T-32404 — Dyadic prime Riesz eventual positivity is equivalent to RH

Claim ID: `T-32404`  
Title: One pole-cancelled dyadic difference of the smoothed von Mangoldt Riesz mean is eventually positive exactly when the Riemann Hypothesis holds  
Status: **PROPOSED COMPLETE RH CRITERION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: standard explicit-formula contour shift for `-zeta'/zeta`; Landau's one-sign theorem; functional equation of `zeta`  
Scope: exact scalar criterion and RH asymptotic; no unconditional proof of the eventual sign

## 1. The dyadic prime Riesz defect

For real `X>=1`, put

\[
 P_\Lambda(X)
 =\sum_{n\le X}{\Lambda(n)\over\sqrt n}\log{X\over n},
\tag{T-32404.1}
\]

with the sum interpreted as zero below the first prime power. Define

\[
\boxed{
 D_\Lambda(X)
 =P_\Lambda(X)-\sqrt2\,P_\Lambda(X/2).
}
\tag{T-32404.2}
\]

The coefficient `sqrt(2)` is forced by the requirement that the pole at `s=1` be cancelled.

## 2. Exact Mellin transform

For `Re z>1/2`, finite Fubini gives

\[
 \int_1^\infty P_\Lambda(X)X^{-z-1}dX
 ={1\over z^2}
 \sum_{n\ge2}{\Lambda(n)\over n^{z+1/2}}
 ={1\over z^2}
 \left[-{\zeta'\over\zeta}\left(z+{1\over2}\right)\right].
\tag{T-32404.3}
\]

The dilation `X mapsto X/2` contributes the Mellin multiplier `2^{-z}`. Hence

\[
\boxed{
 \int_1^\infty D_\Lambda(X)X^{-z-1}dX
 ={1-2^{1/2-z}\over z^2}
 \left[-{\zeta'\over\zeta}\left(z+{1\over2}\right)\right].
}
\tag{T-32404.4}

Equivalently, with `s=z+1/2`, the multiplier is

\[
 1-2^{1-s}.
\]

At the real zeta pole `s=1`, or `z=1/2`, this multiplier vanishes simply, so the pole is removed exactly.

## 3. Every off-line zero survives

Let

\[
 \rho=\beta+i\gamma
\]

be a nontrivial zeta zero of multiplicity `m_rho`. The logarithmic derivative has residue

\[
 \operatorname*{Res}_{s=\rho}
 \left(-{\zeta'\over\zeta}(s)\right)
 =-m_\rho.
\]

Thus (T-32404.4) has a pole at

\[
 z_\rho=\rho-{1\over2}
\]

unless

\[
 1-2^{1-\rho}=0.
\]

But the zeros of the finite factor satisfy

\[
 \Re\rho=1.
\]

There are no nontrivial zeta zeros on `Re s=1`. In particular every hypothetical zero with

\[
 {1\over2}<\beta<1
\]

produces an uncancelled nonreal pole in `Re z>0`.

This is a useful difference from reciprocal-zeta criteria: the pole residue depends only on the integer multiplicity, not on `1/zeta'(rho)`.

## 4. No positive-real singularity

For every positive real `z`, the point `s=z+1/2` is real and zeta has no zero there. At `z=1/2`, the only real pole of `-zeta'/zeta` is cancelled by `1-2^{1/2-z}`. Therefore the meromorphic continuation of (T-32404.4) has no singularity on

\[
 z\in(0,\infty).
\tag{T-32404.5}
\]

The point `z=0` is the boundary of the RH half-plane and is deliberately retained.

## 5. Eventual one-sidedness implies RH

Suppose `D_Lambda(X)` has one sign for all sufficiently large `X`. After changing sign if necessary and adding a compactly supported correction, obtain a nonnegative locally integrable function

\[
 f(t)=\pm D_\Lambda(e^t)
\]

on `[0,infinity)`.

If an off-line zero existed, Section 3 would give a singularity of its Laplace transform in `Re z>0`. Hence the abscissa of convergence would be positive. Landau's one-sign theorem would force a singularity at the corresponding **positive real** abscissa. Section 4 shows there is no such positive-real singularity.

Therefore every nontrivial zero satisfies `Re rho<=1/2`; functional-equation symmetry yields

\[
\boxed{
 D_\Lambda(X)\text{ eventually one-signed}
 \Longrightarrow \mathrm{RH}.
}
\tag{T-32404.6}

No estimate for primes has been used in this implication beyond the standard meromorphic continuation and the finite pole audit.

## 6. The critical boundary term is explicitly positive

At `z=0`, zeta is nonzero and the multiplier does not vanish. Put

\[
 C_\Lambda
 =(1-\sqrt2)
 \left[-{\zeta'\over\zeta}\left({1\over2}\right)\right]
 =(\sqrt2-1){\zeta'\over\zeta}\left({1\over2}\right).
\tag{T-32404.7}
\]

The completed-zeta functional equation gives

\[
 {\zeta'\over\zeta}\left({1\over2}\right)
 ={1\over2}\left[
 \log\pi+\gamma+{\pi\over2}+3\log2
 \right].
\tag{T-32404.8}
\]

Consequently

\[
\boxed{
 C_\Lambda
 ={\sqrt2-1\over2}
 \left[
 \log\pi+\gamma+{\pi\over2}+3\log2
 \right]>0.
}
\tag{T-32404.9}
\]

Thus the double pole at `z=0` contributes the positive term

\[
 C_\Lambda\log X.
\]

## 7. RH gives a bounded oscillatory remainder

Assume RH. Every nontrivial zero is

\[
 \rho={1\over2}+i\gamma.
\]

The residue contributed by this zero to the inverse Mellin formula has absolute value at most

\[
 { (1+\sqrt2)m_\rho\over\gamma^2}.
\tag{T-32404.10}
\]

The standard zero-counting estimate implies

\[
 \sum_\rho {m_\rho\over1+|\gamma|^2}<\infty.
\tag{T-32404.11}
\]

Hence the complete critical-line residue series is absolutely and uniformly convergent as a Fourier series in `log X`. The trivial-zero residues lie strictly in the left half-plane and give a bounded decaying contribution. A standard truncated-rectangle explicit-formula contour shift therefore yields

\[
\boxed{
 D_\Lambda(X)
 =C_\Lambda\log X+O(1)
 \qquad(X\to\infty)
}
\tag{T-32404.12}
\]

under RH. The `O(1)` term contains the absolutely convergent critical-line Fourier series, the finite part at `z=0`, and the decaying trivial-zero series.

Since `C_Lambda>0`, RH implies

\[
 D_\Lambda(X)>0
\]

for every sufficiently large `X`.

Combining with Section 5 gives the exact equivalence

\[
\boxed{
 \mathrm{RH}
 \iff
 D_\Lambda(X)>0\text{ for all sufficiently large }X.
}
\tag{T-32404.13}

Equivalently,

\[
\boxed{
 \mathrm{RH}
 \iff
 P_\Lambda(X)>\sqrt2\,P_\Lambda(X/2)
 \text{ eventually}.
}
\tag{T-32404.14}

## 8. Why the one logarithmic smoothing is load bearing

Differentiating in `log X` gives the unsmoothed dyadic contrast

\[
 \sum_{n\le X}{\Lambda(n)\over\sqrt n}
 -\sqrt2\sum_{n\le X/2}{\Lambda(n)\over\sqrt n}.
\]

Its zero residues lose one factor of `1/(rho-1/2)`, so no absolutely convergent bounded zero series is available by the elementary argument above. The extra logarithmic Riesz smoothing supplies exactly the second denominator needed for (T-32404.11).

Thus the theorem is naturally located at smoothing order one rather than at the raw Chebyshev half-moment.

## 9. Proof boundary

Closed, subject to independent review:

- exact dyadic Mellin transform;
- cancellation of the pole at `s=1`;
- survival of every off-line zeta zero;
- absence of positive-real singularities;
- Landau implication from eventual one-sidedness to RH;
- explicit positive `z=0` coefficient;
- under RH, an absolutely convergent bounded critical-line zero series;
- RH equivalence with eventual positivity.

Open:

- an unconditional proof of the eventual positivity in (T-32404.14);
- RH.
