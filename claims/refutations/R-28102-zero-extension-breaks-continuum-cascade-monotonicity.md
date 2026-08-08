# R-28102 — Zero extension breaks the claimed all-iterate continuum monotonicity

Claim ID: `R-28102`  
Title: The endpoint jet of the compact critical ramp produces a nonmonotone second continuum residual  
Status: **EXACT REFUTATION OF `L-27702.7` AS STATED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Target: PR #280 `L-27702`, especially Sections 3--4  
Scope: refutes the assertion that every zero-extended continuum residual remains decreasing; it does not refute the exact first two positive finite stages, the continuum mass identity, DCCS, or RH

## 1. Reviewed assertion

PR #280 defines

\[
 W_X(x)=x^{-1/2}\log(X/x)\mathbf1_{0<x\le X}
\]

and

\[
 (\mathcal Tf)(x)=\sum_{k\ge1}[f(2kx)-f((2k+1)x)].
\]

It correctly observes that `D=-x d/dx` commutes with each interior dilation.  It then asserts

\[
 D^m\mathcal T^jW_X\ge0
 \quad(m,j\ge0),
\]

and concludes that every continuum residual is decreasing.

The inference misses the endpoint jet.  Although `W_X(X)=0`, the first logarithmic derivative has the nonzero inner boundary value

\[
 (DW_X)(X^-)=X^{-1/2}.
\]

After one differentiation the zero extension therefore has a jump.  A second use of the formal commutation drops the associated boundary distribution.

## 2. Explicit counterexample

Take `X=16`, define `G_0=W_16`, and put

\[
 G_1=\mathcal TG_0,
 \qquad
 G_2=\mathcal TG_1.
\]

Direct finite evaluation gives

\[
 G_2(2)
 =\log\left(
 2^{-2\sqrt3/3+\sqrt2/4}
 3^{\sqrt3/3}
 \right),
\]

and

\[
 G_2(3)=\frac{\sqrt3}{6}\log\frac43.
\]

Their difference is

\[
\boxed{
G_2(3)-G_2(2)
=\sqrt3\log\frac{2}{\sqrt3}
 -\frac{\sqrt2}{4}\log2
>0.
}
\tag{R-28102.1}
\]

The retained rational-interval replay encloses it inside

\[
 0.00407544708
 <G_2(3)-G_2(2)
 <0.00407544710.
\]

Thus `G_2` is not decreasing, and `DG_2` is negative somewhere between two and three.

## 3. Correct surviving statements

The following parts of PR #280 survive:

1. the exact central carry residual formula;
2. monotonicity of the first discrete residual of the critical source;
3. the unconditional two-stage positive packing and its `3.624...` constant;
4. the continuum integral contraction
   \[
   \int\mathcal Tf=(1-\log2)\int f
   \]
   whenever the signed Fubini calculation is licensed;
5. the exact finite signed support-halving cascade;
6. the identification of boundary/lattice commutators as the remaining source.

What fails is the claim that the compact endpoint can be ignored at every derivative order.

## 4. Corrected frontier

The boundary is not a harmless analytic collar.  It is the same load-bearing object isolated independently as:

- PR #272's odd-node adjacent-tree commutator and bottom charge;
- PRs #268/#269's factor-five physical boundary;
- PR #263's source-image boundary recurrence;
- PR #276's weighted dyadic shell.

Accordingly the continuation on this branch does not claim that the continuum cascade alone supplies a positive all-stage flow.  It combines the exact first two positive stages with the source-complete boundary-commutator normal form and seeks a strict recurrence for that boundary source.

## 5. Exact replay

`experiments/X-28102-continuum-boundary-counterexample/verify.py` uses rational square-root enclosures and the atanh series for logarithms to certify (R-28102.1) without floating point in the verdict.

## 6. Disposition

```text
L-27702.3 continuum mass identity                  RETAINED
L-27702.7 all-iterate logarithmic hierarchy        FALSE AS STATED
L-27702.10 positive infinite continuum cascade     NOT ESTABLISHED
L-27702.18 exact signed finite saturation           RETAINED
T-27701 DCCS conditional implication                RETAINED
PR #280 as an unconditional completion              NOT CLAIMED
RH                                                   UNPROVED
```
