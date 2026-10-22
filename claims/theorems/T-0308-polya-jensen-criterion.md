# T-0308 — Pólya--Jensen criterion and effective degree barrier

Claim ID: T-0308  
Title: Jensen-polynomial criterion for RH and its verified-height barrier  
Status: PROPOSED  
Authoring agent: `gpt56-03`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: external theorems of Pólya and Griffin et al.; T-0310 for the numerical corollary  
Scope: imported equivalence plus search exclusion  
Related counterexample candidates: nonhyperbolic Jensen polynomials

## Statement

Define positive Taylor coefficients `gamma(j)` by
\[
 \xi\!\left(\frac12+z\right)
 =\sum_{j=0}^{\infty}\frac{\gamma(j)}{j!}z^{2j},
\]
and for integers `d,n>=0` define
\[
 J^{d,n}(X)=\sum_{j=0}^{d}{d\choose j}\gamma(n+j)X^j.
\]
A real polynomial is **hyperbolic** if all its zeros are real.

Pólya's criterion states:
\[
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 J^{d,n}\text{ is hyperbolic for every }d,n\ge0.
\]

The effective theorem of Griffin--Ono--Rolen--Thorner--Tripp--Wagner states
that if all zeros of `xi^{(m)}` with imaginary part at most `T` lie on the
critical line, then
\[
 J^{d,n}\text{ is hyperbolic for all }n\ge m
 \quad\text{whenever}\quad d\le\lfloor T\rfloor^2.
\]
For `m=0`, combining with T-0310 gives:
\[
 J^{d,n}\text{ is hyperbolic for every }n\ge0
 \quad\text{and every }d\le9\cdot10^{24}.
\]

Thus any brute-force search for a nonhyperbolic zeta Jensen polynomial at or
below that degree is provably futile.

## Sources

- Michael Griffin, Ken Ono, Larry Rolen, Don Zagier, *Jensen polynomials for
  the Riemann zeta function and other sequences*, PNAS 116 (2019),
  11103--11110, DOI 10.1073/pnas.1902572116, arXiv:1902.07321.
- Michael Griffin, Ken Ono, Larry Rolen, Jesse Thorner, Zachary Tripp, Ian
  Wagner, *Jensen polynomials for the Riemann xi-function*, Adv. Math. 397
  (2022), 108186, DOI 10.1016/j.aim.2022.108186, arXiv:1910.01227.

Inspection level: full arXiv HTML/text inspected.  Equations (1.1), (1.2),
Theorem 1.2, and the discussion of inefficiency were located.

## Proof status

Imported theorem.  The arithmetic corollary `9*10^24` is proved here by
squaring `3*10^12`:
\[
 (3\cdot10^{12})^2=9\cdot10^{24}.
\]

## Analytic/domain audit

- This coefficient convention uses `j!`, not `(2j)!`.
- The polynomial degree `d` and shift `n` are independent nonnegative integers.
- The verified-height theorem uses `floor(T)^2`.
- Hyperbolicity must be exact; near-real floating roots are insufficient.

## Gap audit

- Coefficient normalization errors change every polynomial.
- A numerical root with tiny imaginary part may be roundoff.
- Eventual fixed-degree hyperbolicity does not prove RH.
- The enormous exclusion range makes direct search strategically poor but does
  not invalidate the equivalence above it.

## Remaining uncertainty

Independent review should verify that the `T=3*10^12` theorem's hypotheses
match `RH_0(T)` exactly, including the use of both positive and negative
ordinates (symmetry supplies the latter).

## Suggested next attack

Record this as a negative search result and redirect polynomial work toward
theoretical converses or compressed high-degree certificates, not enumeration.
