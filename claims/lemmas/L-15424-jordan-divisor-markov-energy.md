# L-15424 — Suzuki’s Jordan coefficients carry an exact divisor-Markov carré du champ

Claim ID: `L-15424`  
Title: Positive Jordan-totient transitions give a candidate arithmetic Green lift  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: Suzuki’s coefficients `c_omega(n)`; elementary Dirichlet convolution  
Scope: independent arithmetic mechanism for the Green-lift gate in `L-15423`  
Related counterexample candidates: none

## Generalized Jordan weights

For `omega>0`, Suzuki defines

\[
 c_\omega(n)
 =n^\omega\prod_{p\mid n}(1-p^{-2\omega}).
 \tag{L-15424.1}
\]

Put

\[
 \boxed{
 J_{2\omega}(n)=n^\omega c_\omega(n)
 =n^{2\omega}\prod_{p\mid n}(1-p^{-2\omega}).}
 \tag{L-15424.2}
\]

Equivalently,

\[
 J_{2\omega}=\mu*\operatorname{id}^{2\omega}.
 \tag{L-15424.3}
\]

Therefore

\[
 \boxed{
 \sum_{d\mid n}J_{2\omega}(d)=n^{2\omega}.}
 \tag{L-15424.4}
\]

All terms are positive.

## Exact divisor Markov kernel

For every integer `n>=1`, define

\[
 \boxed{
 P_\omega(n,d)
 =\frac{J_{2\omega}(d)}{n^{2\omega}}
 \mathbf 1_{d\mid n}.}
 \tag{L-15424.5}
\]

Then

\[
 P_\omega(n,d)\ge0,
 \qquad
 \sum_{d\mid n}P_\omega(n,d)=1.
 \tag{L-15424.6}
\]

Thus the arithmetic coefficients already present in Suzuki’s Mellin kernel define one exact downward divisor Markov step.

## Local data-processing inequality

For any complex function `F` on the divisor set of `n`, put

\[
 (\mathcal P_\omega F)(n)
 =\sum_{d\mid n}P_\omega(n,d)F(d).
 \tag{L-15424.7}
\]

Jensen’s inequality gives

\[
 \boxed{
 |\mathcal P_\omega F(n)|^2
 \le
 \sum_{d\mid n}P_\omega(n,d)|F(d)|^2.}
 \tag{L-15424.8}
\]

The exact defect is the divisor carré du champ

\[
 \boxed{
 \sum_{d\mid n}P_\omega(n,d)|F(d)|^2
 -|\mathcal P_\omega F(n)|^2
 =\frac12\sum_{d,e\mid n}
 P_\omega(n,d)P_\omega(n,e)
 |F(d)-F(e)|^2.}
 \tag{L-15424.9}
\]

This is a positive energy identity with no zeta-zero input.

## Candidate arithmetic realization of the Green lift

Suzuki’s scattering kernel is the Mellin convolution

\[
 h_\omega(x)
 ={1\over x}\sum_{n\le x}
 c_\omega(n)g_\omega(n/x).
 \tag{L-15424.10}
\]

The occurrence of the same positive `c_omega(n)` suggests the following noncircular target:

> Construct the lifted plus-branch Volterra integrand as a conditional expectation over the Jordan divisor transition (L-15424.5), with the multiplier `kappa` of `L-15423` represented by a bounded score on the one-step fiber.

If an exact unitary/isometric adapter `U_omega` satisfies

\[
 U_\omega E_{\omega,+}
 =\text{conditional-expectation lift for }P_\omega
 \tag{L-15424.11}
\]

and intertwines the minus multiplier, then (L-15424.8) gives

\[
 \|M_{-,\omega}f\|
 \le\|M_{+,\omega}f\|
 \tag{L-15424.12}
\]

and the desired endpoint energy follows through `L-15422`.

## Why this is an independent arithmetic mechanism

The positivity in (L-15424.9) comes solely from:

1. Möbius inversion;
2. positivity of generalized Jordan totients;
3. the divisor identity (L-15424.4);
4. Hilbert-space data processing.

It does not use zero locations, an RH-conditional explicit formula, or innerness of the scattering ratio.

## Smallest arithmetic blocker

The remaining task is one exact intertwining identity, not a new positivity inequality:

\[
 \boxed{
 \text{Jordan divisor conditional expectation}
 \quad\longleftrightarrow\quad
 \text{continuous Volterra Green-minimal lift}.}
 \tag{L-15424.13}
\]

More concretely, one must derive the Volterra ratio

\[
 A_s(u)=\Psi(s+u)/\Psi(s)
 \tag{L-15424.14}
\]

and its endpoint trace metric as the Mellin/continuum limit of the divisor-chain Green kernel, including the archimedean factor `g_omega`. The discrete Markov identity alone does not provide the physical metric equality required by `L-15423`.

## Gap audit

- Formula (L-15424.4) is exact for every real `omega>0` by Dirichlet convolution.
- The chain is absorbing/downward; a global invariant `L2` measure is not asserted.
- Pointwise Jensen is not yet the complete branch-norm inequality.
- The archimedean kernel `g_omega` is sign-sensitive and must be included in any exact adapter.
- This lemma supplies the arithmetic carré du champ and the precise intertwining target; it does not prove that target.
