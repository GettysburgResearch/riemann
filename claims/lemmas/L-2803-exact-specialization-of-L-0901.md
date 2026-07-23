# L-2803 — Exact rational specialization of the uniform carrier correction bound

Claim ID: L-2803  
Title: The L-0901 correction bound is below one half-billionth at the optimized carrier target  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0901; elementary inequalities recorded below  
Scope: exact target specialization for Issue #28 and draft PR #44  
Related counterexample candidates: none

## Statement

Assume the proposed operator inequality L-0901. At

\[
 c=10^{11},\qquad K=1024,\qquad
 T=4709203636353.65=\frac{94184072727073}{20},
\]

the normalized D-0801 archimedean-plus-pole correction satisfies

\[
 \|E_{\rm arch}+E_{\rm pole}\|_{\rm op}<E_{\rm var},
\]

where the exact rational upper bound is

\[
 \boxed{
 E_{\rm var}=
 \frac{136091541158257193750}
 {292731105330133011007855861857}}
\]

and

\[
 \boxed{E_{\rm var}<\frac1{2000000000}.}
\]

More explicitly, the two rational majorants used by X-2801 are

\[
 E_{\rm arch}=
 \frac{481650}{1036024799997803},
\]

and

\[
 E_{\rm pole}=
 \frac{24115570278400}
 {26611918666375728273441441987}.
\]

The result contains no floating-point or special-function evaluation. It is a
conditional exact certification of L-0901's target specialization, not a
certification of the complete prime matrix or of the Guinand--Weil
normalization.

## Relation to the independent reconstruction

L-2801 independently reconstructs the compact cellwise archimedean and pole
formulas from Fourier inversion and the regularized digamma integral. Those are
the starting source formulas of L-0901. L-0901 then obtains a substantially
sharper `O(1/T)` operator estimate by integrating the oscillatory residual by
parts. L-2803 does not duplicate that analytic argument; it independently
checks its target constants with exact rational arithmetic and records every
transcendental majorant used.

## Proof

L-0901 states

\[
 B_{\rm arch}
 =\frac1{\pi T}\left[
 \frac K L(\log K+2)+6K+5+\frac1L
 \right],
\]

and

\[
 B_{\rm pole}
 =\frac{4\sqrt c K^2}{\pi L T^2},
 \qquad L=\log c.
\]

We use four strict elementary bounds.

### 1. `pi>3`

The circumference of a circle is strictly larger than the perimeter of its
inscribed regular hexagon, hence `2*pi>6`.

### 2. `log(10)>2`

For `m>=2`, `m!>=2^(m-1)`, so

\[
 e=\sum_{m=0}^\infty\frac1{m!}<1+1+
 \sum_{m=2}^\infty\frac1{2^{m-1}}=3.
\]

Thus `e^2<9<10`, and monotonicity of the real logarithm gives
`log(10)>2`. Consequently

\[
 L=11\log(10)>22.
\]

### 3. `log(1024)<7`

The positive exponential series gives

\[
 e^{7/10}>
 1+\frac7{10}+\frac{(7/10)^2}{2}
 +\frac{(7/10)^3}{6}
 =\frac{12013}{6000}>2.
\]

Hence `log(2)<7/10`, and therefore

\[
 \log(1024)=10\log2<7.
\]

### 4. `sqrt(10^11)<316228`

Direct integer arithmetic gives

\[
 316228^2=100000147984>100000000000=10^{11}.
\]

Substitution into the L-0901 formulas yields

\[
 B_{\rm arch}<
 \frac{
 (1024/22)(7+2)+6144+5+1/22
 }{3T}
 =\frac{481650}{1036024799997803},
\]

and

\[
 B_{\rm pole}<
 \frac{4\cdot316228\cdot1024^2}{3\cdot22\,T^2}
 =\frac{24115570278400}
 {26611918666375728273441441987}.
\]

Their exact sum is the stated `E_var`.

Finally,

\[
 292731105330133011007855861857
 -2000000000\cdot136091541158257193750
\]

is the positive integer

\[
 20548023013618623507855861857.
\]

Cross multiplication therefore proves

\[
 E_{\rm var}<1/2000000000.
\]

## Analytic domain audit

- Every logarithm in the dependency L-0901 is the ordinary real logarithm at a
  positive argument.
- This specialization evaluates no logarithm, square root, or `pi`; it replaces
  them by proved rational majorants or minorants.
- `T` is represented by the exact displayed rational number.
- No prime phase, eigensolver, or special-function value enters the checker.

## Dependency audit

- L-2801 independently supports the compact source formulas.
- L-0901 supplies the integration-by-parts operator inequality.
- The displayed target specialization is checked from scratch by X-2801 using
  Python integers and `fractions.Fraction`.
- The implication from a negative complete D-0801 value to falsity of RH remains
  dependent on the unresolved admissibility and explicit-formula audit.

## Gap audit

1. The theorem is conditional on independent review of L-0901.
2. It does not certify the `4,118,082,969`-term prime Toeplitz value in PR #44.
3. It does not certify huge phase range reduction, accumulation, or an
   eigenvector.
4. It does not promote the empirical PR #44 margin to a positive theorem.
5. A different carrier with a leading margin below this budget remains
   unresolved.

## Adversarial tests

The exact checker verifies the target component fractions, the strict
`1/2000000000` comparison, non-power-of-two cell support, zero-touch rejection,
synthetic positive and negative threshold behavior, strict schema handling, and
integer type validation.

## Remaining uncertainty

No arithmetic uncertainty remains in the specialization. The mathematical
uncertainty lies in L-0901's proposed analytic inequality and the inherited
project normalization.

## Suggested next attack

Freeze the complete-prime vector and certify a directed leading-margin interval.
At this target it is enough for the lower endpoint to exceed
`1/2000000000`; a negative leading upper endpoint below its negative would
survive all corrections controlled by L-0901.
