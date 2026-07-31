# Uniform Hankel moat audit

Date: 2026-08-01  
Agent: `gpt56-05-l`  
Issue: #180  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`

## Requested target

The requested positive conclusion was

\[
 \exists\kappa<1:\qquad
 \|\mathsf H_\omega\|\le\kappa
 \quad(0<\omega<1/2),
\]

where `mathsf H_omega` is the anti-causal Hankel block of Suzuki's unimodular
xi scattering symbol.

## Repository audit

The complete current Hardy/Hankel work is pushed on draft PR #165, including:

- the exact symmetric boundary filter;
- the filtered Hardy pole-Gram decomposition;
- the residue-free reflection refutation;
- the Toeplitz/Hankel defect identity;
- the strict-contraction criterion;
- exact finite Cauchy-Gram regressions.

Earlier `gpt56-05*` work is present in PRs #33, #40, #43, #48, #51, #69,
#80, #82, #89, #124, #144, and #165. The threshold-directed X-5501 theorem
layer is present on branch
`agent/gpt56-05-f/55-threshold-directed-carrier-certification`; its large local
artifact bundle was not completed into a pull request and must not be described
as fully uploaded.

## Exact new result

For

\[
 p=x+i(\delta-\omega),
 \qquad
 q=x+i(\delta+\omega),
 \qquad0<\omega<\delta,
\]

the isolated off-line-pair boundary factor is

\[
 \phi=\overline{b_p}b_q.
\]

Its Hankel operator is rank one and satisfies

\[
 \mathsf H_\phi^*\mathsf H_\phi
 =|b_q(p)|^2P_{K_{b_p}},
\]

so

\[
 \|\mathsf H_\phi\|=\frac\omega\delta.
\]

The corresponding Toeplitz operator has exact lower modulus

\[
 m(T_\phi)^2=1-\frac{\omega^2}{\delta^2}.
\]

Thus, as the scattering offset approaches the horizontal displacement of an
off-line zero,

\[
 \|\mathsf H\|\to1,
 \qquad
 m(T)\sim\sqrt{2(\delta-\omega)/\delta}.
\]

The full xi scattering symbol has the same limiting pressure after grouping all
same-ordinate factors and localizing with the normalized reproducing kernel.

## Main theorem-level conclusion

For the xi scattering family, the following are equivalent, subject to Suzuki's
normalization and the declared local-factorization audit:

1. RH;
2. one uniform `kappa<1` bounds all Hankel norms;
3. one uniform `eta>0` satisfies
   \[
    T_\omega^*T_\omega\succeq\eta I;
   \]
4. the Toeplitz lower singular values have a positive uniform infimum.

Under RH every symbol is inner and `mathsf H_omega=0`. Under false RH the exact
Blaschke-pair bubble drives the supremum to one.

Therefore the requested bound is not an intermediate estimate now derivable
from the preceding algebra; it is an exact RH-equivalent spectral-gap
formulation.

## Refuted shortcuts

The explicit family

\[
 \phi_\epsilon
 =\overline{b_{i\epsilon}}b_{i(2\delta-\epsilon)}
\]

satisfies

\[
 \|\mathsf H_{\phi_\epsilon}\|
 =1-\epsilon/\delta<1
\]

for every fixed `epsilon`, while the supremum is one. Moreover the boundary
symbols converge pointwise and locally in every finite `Lp` space to the inner
symbol `b_(2i delta)`, whose Hankel operator is zero.

Hence none of the following closes the target:

- pointwise strict norms below one;
- finite offset grids;
- boundary `Lp` convergence;
- finitely many Fourier coefficients;
- fixed-rank or weakly-null defect estimates;
- compactness on offset intervals chosen before an unknown crossing is known.

## Exact regression

`X-15409` retains two rational controls:

```text
(delta,omega)=(3/10,1/10)
||H||=1/3
m(T)^2=8/9

(delta,omega)=(3/10,29/100)
||H||=29/30
m(T)^2=59/900.
```

The checker uses integers and `fractions.Fraction` only. The committed tests
cover false norms, false floors, crossing parameters, duplicate cases, Boolean
integers, and monotonicity mutations.

## Honest outcome

The requested uniform moat was not proved. Proving it would prove RH by
`T-15408`. The pass nevertheless supplies:

1. the exact singular-value law of the obstruction;
2. the exact Toeplitz LMI equivalent to the moat;
3. an explicit counterexample to soft compactness arguments;
4. a finite checker for the local operator mechanism;
5. a clean review boundary for any future claimed positive proof.

The next legitimate positive attack must prove one independent arithmetic or
canonical-system inequality of the form

\[
 T_\omega^*T_\omega\succeq\eta I
\]

uniformly for all offsets, without importing zero locations or RH-conditional
innerness.
