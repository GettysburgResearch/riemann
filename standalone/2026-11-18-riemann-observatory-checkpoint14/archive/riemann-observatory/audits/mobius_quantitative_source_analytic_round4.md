# Quantitative Möbius input: actual source and Abel consequences

Reviewer: analytic_frontier.17November2026. Source statement inspected, not a full paper audit. This supplies the precise external theorem requested for the Noor/Bergman track; it does not prove that track's approximation theorem.

## Primary source boundary

PAPER-A008 is Lee–Leong, arXiv2208.06141v5,9September2026. Theorem1.1,eq(9),PDFp2 states unconditionally

|M(x)|<33.56x(logx)exp(−sqrt(logx/5.56)), forallrealx>=exp(4589.20).

The actual page was rendered to verify that5.56 is inside the square root denominator. PDF SHA256:76e61bb702beecade0deca82896d5125043cd747c694986ec7e732d13be54ad1. Full25-page proof and computational smoothing were not audited. The arXiv landing and actual v3 withdrawal notice were read: v3 was withdrawn after errors in cited ingredients; currentv4/v5 are later replacements. No comparison/repair audit is claimed. Citation must identifyv5, not silently reuse a withdrawn version.

Letc=1/sqrt(5.56)>0. The cited input has the simpler asymptotic form|M(x)|<=C xlogx exp(−c sqrt(logx)). Only that consequence is used below; the numerical threshold is immaterial for eventual bounds and a finite initial segment changes constants only.

## Series limits at1, without RH

For Re(s)>1, F(s)=sum_n mu(n)n^(-s)=1/zeta(s). Abel summation writes it as s integral_1^infinity M(t)t^(-s-1)dt. The cited cancellation makes the integral and its firsts derivative absolutely/uniformly convergent up to Re(s)=1 on bounded sets. Indeed powers oflogt multiplyingexp(−c sqrt(logt)) are integrable againstdt/t. Consequently F and its first derivative extend continuously from the right to1 through these formulas.

The ordinary Laurent expansion zeta(s)=1/(s−1)+O(1) implies1/zeta(s)=(s−1)+O((s−1)^2). Hence F(1)=0,F'(1)=1. Abel summation therefore gives the convergent boundary series

sum_n mu(n)/n=0,

sum_n mu(n)logn/n=−1.

The differentiation is justified by the displayed uniform integral domination, not by assuming absolute convergence of the boundary series themselves.

## Quantitative tails

For integerN large enough, put A_N=sum_(n<=N)mu(n)/n andB_N=sum_(n<=N)mu(n)logn/n. Exact tail summation by parts gives

A_N=M(N)/N−integral_N^infinity M(t)/t²dt,

B_N+1=M(N)logN/N+integral_N^infinity M(t)(1−logt)/t²dt.

Withu=sqrt(logt),dt/t=2u du, the integrals are bounded by fixed multiples of integrals fromsqrt(logN) toinfinity ofu³exp(−cu), respectively(u⁵+u³)exp(−cu). Integration by parts yields

A_N=O((logN)^(3/2)exp(−c sqrt(logN))),

B_N+1=O((logN)^(5/2)exp(−c sqrt(logN))).

For every fixedK>0 these areO_K((logN)^(-K)). No RH, growing-K uniformity or finite-height-zero computation is being inferred by this Abel step. All remaining reliance on the current explicit Mertens bound is an openly cited external theorem, whose original proof was not independently checked here.
