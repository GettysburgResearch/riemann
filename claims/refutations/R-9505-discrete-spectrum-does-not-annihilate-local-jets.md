# R-9505 — Discrete spectral support does not annihilate a local second jet

Claim ID: `R-9505`  
Title: Exact counterexample to a proposed discrete-spectrum-versus-local-curvature shortcut  
Status: `PROPOSED SCOPE REFUTATION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Dependencies: elementary Fourier analysis  
Scope: recent local-jet/explicit-formula proof proposals  
Related counterexample candidates: none

## 1. The invalid implication

A recent unreviewed RH proof proposal argues, at abstract level, that a prime
sector with purely discrete logarithmic Fourier support cannot contribute a
local second-order jet in the probe-center variable.

The implication

\[
\boxed{
\text{purely discrete Fourier support}
\Longrightarrow
\text{vanishing local second jet}}
\tag{R-9505.1}
\]

is false.

## 2. One-frequency counterexample

For any nonzero real `lambda`, let

\[
P(y)=\cos(\lambda y).
\tag{R-9505.2}
\]

Its Fourier transform is supported on the two-point set

\[
\{-\lambda,+\lambda\}.
\tag{R-9505.3}
\]

Nevertheless

\[
\boxed{P''(y_0)=-\lambda^2\cos(\lambda y_0),}
\tag{R-9505.4}
\]

which is nonzero for generic `y_0`. In particular,

\[
P''(0)=-\lambda^2\ne0.
\tag{R-9505.5}
\]

Thus a single discrete spectral atom already carries nontrivial local
curvature.

## 3. Arbitrary finite second jets from discrete spectra

Choose three distinct real frequencies `lambda_0,lambda_1,lambda_2`. The map

\[
(c_0,c_1,c_2)
\longmapsto
\left(
P(y_0),P'(y_0),P''(y_0)
\right),
\qquad
P(y)=\sum_{j=0}^2c_je^{i\lambda_jy},
\tag{R-9505.6}
\]

has matrix

\[
\begin{pmatrix}
1&1&1\\
i\lambda_0&i\lambda_1&i\lambda_2\\
-\lambda_0^2&-\lambda_1^2&-\lambda_2^2
\end{pmatrix}
\operatorname{diag}
\left(e^{i\lambda_0y_0},e^{i\lambda_1y_0},e^{i\lambda_2y_0}\right).
\tag{R-9505.7}
\]

Its determinant is a nonzero Vandermonde factor. Therefore finite discrete
spectra realize arbitrary complex second-order jet data at `y_0`.

The same conclusion holds in the real-even sector by using sufficiently many
cosine frequencies.

## 4. Consequence for explicit-formula sectors

A prime sector of the form

\[
\sum_n a_ne^{i(\log n)y}
\tag{R-9505.8}
\]

has discrete logarithmic support, but its local second derivative is

\[
-\sum_n a_n(\log n)^2e^{i(\log n)y_0},
\tag{R-9505.9}
\]

whenever the differentiated sum is defined. There is no spectral-type reason
for this quantity to vanish.

To prove vanishing, one needs an additional exact identity on the coefficients,
a projection explicitly orthogonal to the weighted atoms, or a limiting theorem
that controls the differentiated series. Discreteness alone supplies none of
these.

Moreover, an isolated zero quartet also generates a finite exponential/hyperbolic
packet in a probe-center coordinate. A linear projection claimed to annihilate
all discrete spectra by spectral type would require a separate proof that it
does not simultaneously annihilate the proposed zero-quartet defect.

## 5. Status boundary

This refutation addresses only the implication (R-9505.1). It does not audit
every definition or distributional limit in the external working paper.

Any local-curvature proof of RH must retain and explicitly compute the prime
sector's second-jet contribution. It cannot set that contribution to zero merely
because the logarithmic prime spectrum is discrete.
