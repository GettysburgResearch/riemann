# T-91003 — RH is equivalent to monotonicity of one Cauchy-square soft zero count

Claim ID: `T-91003`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`; the standard zero count  
RH status: **unproved**

For

\[
 p_x(a)=
 \Re\frac{\xi'}{\xi}\left(\frac12+a+ix\right)
\]

define

\[
 \boxed{
 \mathcal N_x(a)
 =
 \frac12\left[
 a p_x(a)-a^2p_x'(a)
 \right].
 }
 \tag{T-91003.1}
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 a\longmapsto\mathcal N_x(a)
 \text{ is nondecreasing on }(0,1/2)
 \text{ for every }x\in\mathbb R.
 }
 \tag{T-91003.2}
\]

Equivalently,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal N_x'(a)\ge0
 \qquad
 (x\in\mathbb R,\ 0<a<1/2).
 }
 \tag{T-91003.3}
\]

## Proof

Under RH, `L-91008` gives

\[
 \mathcal N_x(a)
 =
 \sum_\gamma m_\gamma
 \frac{a^4}{[a^2+(\gamma-x)^2]^2},
\]

and every summand is nondecreasing.

Conversely, suppose

\[
 \rho=\frac12+y+i\gamma,
 \qquad 0<y<\frac12,
\]

is an off-line zero of multiplicity \(m\). At \(x=\gamma\), its reflected pair
contributes

\[
 \frac{2ma^4}{(a^2-y^2)^2},
\]

whose derivative is

\[
 -\frac{8ma^3y^2}{(a^2-y^2)^3}.
\]

As \(a\downarrow y\) from the right this tends to \(-\infty\). Distinct zero
terms have poles at different values of \(a^2\), unless they are the same
reflected pair, in which case multiplicities add. Hence
\(\mathcal N_\gamma'(a)<0\) for some \(a\in(y,1/2)\), contradicting
(T-91003.3).

The failure is strict and persists under small changes of \(x\) and \(a\), so
rational \(x\) and rational \(a\) already give a countable equivalent
criterion.

## Interpretation

Each line zero contributes

\[
 \left[\frac{a^2}{a^2+(\gamma-x)^2}\right]^2,
\]

a squared Cauchy resolution which rises monotonically from zero to one.
Therefore \(\mathcal N_x(a)\) is a genuine local soft zero count. RH says that
increasing the horizontal resolution can never reduce that count.

An off-line reflected pair introduces unequal Clark widths \(a-y\) and
\(a+y\); the count blows up and then decreases immediately after the depth
threshold. This is the exact obstruction.

## Prime-side frontier

By `L-91008`,

\[
 \mathcal N_x'(a)=4a^3\mathcal C_x(a^2),
\]

so (T-91003.3) is exactly the prime-side radial-concavity theorem left open on
PR #394. `L-91011` supplies a positive generalized-Jordan source and cocycle,
but no proof of this monotonicity.

The Riemann Hypothesis remains unproved.
