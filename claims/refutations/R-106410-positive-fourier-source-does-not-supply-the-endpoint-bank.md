# R-106410 — Positive Fourier source does not supply the endpoint bank

Claim ID: `R-106410`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-24  
Depends on: `L-106410--L-106411`  
RH status: **not assumed**

Fix \(0<a<1\) and consider the real entire exponential-type function

\[
F_a(t)=1+a\cos t.
\]

Its Fourier measure is positive and even:

\[
\widehat F_a
=\delta_0+\frac a2(\delta_1+\delta_{-1}).
\]

Because \(1-a>0\),

\[
F_a(t)>0\qquad(t\in\mathbb R),
\]

so \(F_a\) has no real zero.  On the other hand,

\[
F_a''(t)=-a\cos t
\]

has only simple real zeros, with asymptotic density \(1/\pi\).

Thus the reverse descent

\[
F_a''\longrightarrow F_a
\]

can lose every real zero even though the parent has a positive compact Fourier
source.  The one-sided and reflected source contractions of
`L-106410--L-106411` still apply at every sufficiently small positive
\(\lambda\): they are algebraic consequences of nonnegative compact Fourier
support, not a real-rootedness theorem.

Therefore none of the following implications is valid source-blindly:

```text
positive Fourier density
  -> endpoint companion bank covers its topological initial space;

small endpoint-Turan source energy
  -> few wrong extrema;

pointwise positive denominator source
  -> cofinal reverse-Rolle descent.
```

The missing `ENDPOINTBANK106410` statement must use Xi-specific global
information—its completed-zeta normalization, safe-line/contour relation,
source-owned frame, or an equivalent model-space sampling theorem.  It cannot
be deleted by citing only the positivity of the Xi Fourier kernel.
