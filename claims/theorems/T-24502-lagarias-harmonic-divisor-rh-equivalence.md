# T-24502 — Lagarias harmonic-divisor criterion for RH

Claim ID: `T-24502`  
Status: `IMPORTED — source theorem; elementary wrapper reproduced; Robin inputs imported`  
Scope: full Riemann Hypothesis  
Issue: #245  
Source: Jeffrey C. Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis*, arXiv:math/0008177v2, Theorem 1.1, Amer. Math. Monthly 109 (2002), 534–543.

For an integer `n>=1`, let

\[
H_n=\sum_{j=1}^n\frac1j,
\qquad
\sigma(n)=\sum_{d\mid n}d.
\]

Then Lagarias proves

\[
\boxed{
\mathrm{RH}
\iff
\sigma(n)\le H_n+e^{H_n}\log H_n
\quad\text{for every }n\ge1,
}
\tag{T-24502.1}
\]

with equality only at `n=1`.

## Imported proof structure

The theorem is an elementary wrapper around two theorems of Robin.

### Robin upper theorem

Under RH,

\[
\sigma(n)<e^\gamma n\log\log n
\qquad(n\ge5041).
\tag{T-24502.2}
\]

### Robin false-RH excess theorem

If RH is false, then there are constants `0<beta<1/2` and `C>0` for which

\[
\sigma(n)
\ge
 e^\gamma n\log\log n
 +\frac{C n\log\log n}{(\log n)^\beta}
\tag{T-24502.3}
\]

for infinitely many integers `n`.

If an off-line zero has real part `b>1/2`, the source states that `beta` may be chosen with

\[
1-b<\beta<\frac12.
\]

### Elementary harmonic bridge

The two estimates imported and reproved in `L-24506` are

\[
e^{H_n}\log H_n\ge e^\gamma n\log\log n
\qquad(n\ge3),
\tag{T-24502.4}
\]

and

\[
H_n+e^{H_n}\log H_n
\le
 e^\gamma n\log\log n+\frac{7n}{\log n}
\qquad(n\ge20).
\tag{T-24502.5}
\]

Under RH, (T-24502.2) and (T-24502.4) prove the criterion for `n>=5041`; Lagarias reports a direct finite check for `1<=n<=5040`. Conversely, (T-24502.3) eventually exceeds (T-24502.5), so the criterion for all integers forces RH.

## Extremal localization

Lagarias explains that a counterexample may be sought in the extremely sparse colossally-abundant family. These are maximizers of

\[
\frac{\sigma(k)}{k^{1+\varepsilon}}
\]

for some `epsilon>0`, and have consecutive-prime support with nonincreasing exponents. The source states that if RH is false, a Robin counterexample exists in this family, and that the analogous localization can be established for (T-24502.1).

This localization is useful as a proof/search reduction, but it is not an unconditional proof of (T-24502.1).

## Dependency boundary

- The harmonic inequalities and the final contradiction are elementary and reproduced locally.
- The finite verification through `5040` is source-reported, not replayed here.
- Robin's theorems are imported primary dependencies and are not reproved in Lagarias's paper.
- This claim is an imported equivalence, not new evidence for RH.

## Review targets

1. Check the inequality directions and thresholds `3`, `20`, and `5041`.
2. Keep the source-reported finite check separate from a repository-replayed certificate.
3. Do not describe the criterion as an elementary proof of RH: the difficult global inputs are Robin's theorems.
4. Preserve the quantitative false-RH excess, since it may be useful for rightmost-zero exponent comparisons elsewhere in the repository.
