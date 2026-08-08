# O-21706 — Nörlund half-plane stability reconnaissance

Claim ID: `O-21706`  
Status: **FLOATING / HIGH-PRECISION RECONNAISSANCE ONLY**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-21706`, `L-21707`, `T-21705`  
Scope: discovery record; no finite or asymptotic zero certificate

## 1. The raw mutation occurs in the right half-plane

For the unaveraged endpoint `N=75`, high-precision nonlinear root refinement gives a zero of the raw one-sided Dirichlet spline near

\[
\boxed{
0.5503373256777979612
+111.6107190834724691\,i.}
\tag{O-21706.1}
\]

Thus the raw function already violates the half-plane stability target
`Re(s)<=1/2`. This is the one-sided source of the off-line pair observed after
raw functional-equation symmetrization.

The value in (O-21706.1) is a high-precision floating root, not an interval
certificate. It is retained as a mutation which any structural proof must fail
for the raw producer.

## 2. Nörlund roots appear, but on the correct side

The Nörlund one-sided function is not globally zero-free. At `N=200`, a
high-precision root occurs near

\[
\boxed{
0.03402238199329508331
+111.5438217217457054\,i.}
\tag{O-21706.2}
\]

This is strictly left of the critical midline. It refutes an unnecessarily
strong global zero-free conjecture while remaining compatible with `NHS`.

The first important source separation is therefore

```text
raw endpoint:       a detected zero with Re(s)>1/2;
logarithmic mean:   detected one-sided zeros remain left of Re(s)=1/2.
```

## 3. Argument-principle scans

Ordinary complex128 contour scans, with phase-increment monitoring, gave the
following one-sided counts in the upper half of the strip:

```text
producer       N      height       zeros in 0<Re<1/2   zeros in 1/2<Re<1
Norlund       200      1000                  2                    0
Norlund       500      2000                 52                    0
Norlund      1000      2000                117                    0
```

Separate symmetrized scans gave:

```text
N=500,  height=5000:
critical-line crossings = 4520
strip winding count     = 4520

N=200,  height=20000:
critical-line crossings = 22491
strip winding count     = 22491
```

These computations are nondirected. They do not exclude missed near-boundary
zeros, numerical cancellation, or failures beyond the scanned height.

## 4. Boundary minimum-modulus pattern

On the sampled critical boundary,

\[
|\overline D_N(1/2+it)|
\]

attained its minimum at `t=0` for every tested `N` through `1000`. Representative
values were

```text
N=1       1.2500000000
N=50      1.3803235456
N=200     1.3984558322
N=500     1.4066796666
N=1000    1.4116123346
```

This nominates the stronger inequality

\[
|\overline D_N(1/2+it)|
\ge\overline D_N(1/2),
\]

which would follow from `RCM`. No floating minimum proves the all-`t` statement.

## 5. Reciprocal derivative probes

Using high-precision formal Taylor-series division rather than finite
differences, the signs required for complete monotonicity of

\[
x\mapsto\frac1{\overline D_N(1/2+x)}
\]

were observed through derivative order `100`, at several positive base points,
for `N<=200`.

This evidence is deliberately weak. The raw `N=75` producer also passes many
low-order derivative probes despite possessing the distant right-half-plane
zero (O-21706.1). A distant pole can remain invisible to a long finite derivative
prefix. Therefore no derivative table may be described as evidence of `RCM`
without a uniform all-order mechanism.

## 6. Mean-gauged phase observation

For the one-sided Mellin function

\[
M_N(s)=\overline m_N(s),
\qquad
c_N=-\log M_N(1),
\]

floating scans found

\[
c_N+\operatorname{Re}
\frac{M_N'(1/2+it)}{M_N(1/2+it)}>0
\]

through the displayed ranges for the Nörlund producer. The raw producer develops
a large negative phase excursion at the root height in (O-21706.1).

This is compatible with a Hermite–Biehler interpretation but is not used in the
shorter `NHS -> RH` argument.

## 7. Correct production target

The reconnaissance supports only the following research decision:

```text
do not seek global zero-freeness;
do not infer stability from finite contour counts;
attack the exact half-plane Re(s)>1/2;
prefer a positive inverse-Laplace or cardinal Hermite-Biehler proof;
retain the raw right-half root as a mandatory mutation.
```

`T-21705` states the proof theorem. RH remains unproved.
