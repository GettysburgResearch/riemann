# T-91004 — One dyadic Cauchy-square gate is equivalent to RH

Claim ID: `T-91004`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91008`, `L-91012`; the standard zero count  
RH status: **unproved**

Define the Cauchy-square soft count

\[
 \mathcal N_x(a)
 =\frac12\left[
 a\Re{\xi'\over\xi}(1/2+a+ix)
 -a^2\partial_a\Re{\xi'\over\xi}(1/2+a+ix)
 \right].
\]

Then

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal N_x(2a)\ge\mathcal N_x(a)
 \quad
 (x\in\mathbb R,\ a>0).
 }
 \tag{T-91004.1}
\]

It is enough to require the inequality for \(0<a<1/2\), and rational \(x,a\)
already form a countable equivalent criterion.

## Proof under RH

Under RH,

\[
 \mathcal N_x(a)
 =\sum_\gamma m_\gamma
 {a^4\over[a^2+(\gamma-x)^2]^2}.
\]

Every summand increases with \(a\). More sharply, `L-91012` gives

\[
 \mathcal N_x(2a)-\mathcal N_x(a)
 =\sum_\gamma m_\gamma
 \left(
 |g_{1,a}(\gamma-x)|^2+|g_{2,a}(\gamma-x)|^2
 \right)\ge0.
\]

## Failure under false RH

Assume false RH. Choose an ordinate \(\gamma\) carrying a right-side zero and,
among the finitely many zeros at that exact ordinate, choose one of maximal
horizontal depth

\[
 y=\Re\rho-\frac12>0.
\]

At the matched centre \(x=\gamma\), as \(a\downarrow y\) from the right, this
pair contributes

\[
 {2ma^4\over(a^2-y^2)^2}\longrightarrow+\infty
\]

to \(\mathcal N_x(a)\).

The quantity \(\mathcal N_x(2a)\) remains bounded along a sequence
\(a\downarrow y\). Indeed a real singularity at the limit \(2y\) would require
a zero at the same ordinate with depth \(2y>y\), contradicting maximality; if
\(2y\ge1/2\), such a nontrivial depth is impossible. Other ordinates do not
produce a real singularity at this centre.

Therefore

\[
 \mathcal N_\gamma(2a)<\mathcal N_\gamma(a)
\]

for all sufficiently close admissible \(a>y\), contradicting the dyadic gate.
The failure is strict and persists under rational perturbation.

## Why this is a better production target

The differential theorem of `T-91003` asks for every infinitesimal scale.
`T-91004` shows that one fixed dilation is complete. It aligns exactly with:

```text
critical-line increment   -> two rational Hermitian channels;
arithmetic deformation    -> positive sieve cocycle
                              Q_(2a)=Q_a(s)Q_a(s+2a).
```

Hence the sole source-facing theorem may be stated as the **Dyadic
Cauchy-Square Gate**:

\[
 \boxed{
 \Delta_a\mathcal N_x
 :=\mathcal N_x(2a)-\mathcal N_x(a)\ge0
 \quad\text{for every }x,a.
 }
\]

This remains open and RH-equivalent. The Riemann Hypothesis is not proved.
