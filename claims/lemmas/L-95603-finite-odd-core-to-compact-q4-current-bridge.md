# L-95603 — Exact bridge from the finite odd-core source to the compact Q4 Schur current

Claim ID: `L-95603`  
Status: **PROPOSED COMPLETE SOURCE-INTERFACE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Scope: exact source and critical-scale operators; no Schur domination claim

Put

\[
z=2^{-s},
\qquad
P=1-4z^2,
\qquad
R=1-z^2.
\]

The reciprocal source used by PRs #554--#595 is

\[
A_4(s)=\frac{P}{R\zeta(s)}.
\]

The compact source used by the older Q4 Schur programme is

\[
B_\sharp(s)=R A_4(s)=\frac{P}{\zeta(s)}.
\]

Let

\[
D_4(s)=-P A_4'(s)
\]

be the logarithmic Q4 source. Since

\[
R'(s)=(\log4)z^2,
\]

differentiation gives the exact identity

\[
\boxed{
R^2D_4
=
PR(-B_\sharp')
+
(\log4)Pz^2B_\sharp.
}
\tag{L-95603.1}
\]

The first term is the compact RH-sensitive current through a finite Q4
filter. The second is an explicit delayed bare-source gauge.

## Critical-scale realization

For a critical observation

\[
\mathcal O_c(X)=\sum_n\frac{c(n)}{\sqrt n}\psi(n/X),
\]

convolution by \(\delta_4\) acts as

\[
\mathcal O_{\delta_4*c}(X)=\frac12\mathcal O_c(X/4).
\]

Thus the factor \(R=1-4^{-s}\) is represented by

\[
I-\frac12S^2.
\]

Its squared inverse is stable:

\[
\boxed{
\left(I-\frac12S^2\right)^{-2}
=
\sum_{j\ge0}(j+1)2^{-j}S^{2j},
\qquad
\sum_{j\ge0}(j+1)2^{-j}=4.
}
\tag{L-95603.2}
\]

Therefore the finite odd-core observation and the compact current-plus-gauge
observation are equivalent at the subpower scale.

At a zeta zero of multiplicity \(m\), the compact current term has pole order
\(m+1\), while the bare gauge has order at most \(m\). The gauge cannot cancel
the conclusion-producing current pole.

This identifies the true nonlocal frontier: a source-complete Schur,
Bellman, or Hardy estimate for the compact current. It does not prove that
estimate.


---
