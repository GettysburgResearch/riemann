# Generalized L-objects: continuation checkpoint

Status: exact local classifications and representation-parent boundaries
for [programme #764](https://github.com/gfreund123/riemann/issues/764),
carried by [draft PR #766](https://github.com/gfreund123/riemann/pull/766).
This is a checkpoint during the requested research pass, not a statement
that eight hours have elapsed or that a new global L-function exists.

## The main conclusion

There are now three distinct questions, with different answers:

1. Does a scalar sequence have a finite recurrence?
2. Is it a matrix coefficient of an honest finite representation?
3. Is its generating function the determinant inverse of a universal
   representation, possibly with finitely many positive grades?

An affirmative answer to the first or second does not imply the third.
Even a formal infinite-graded answer supplies no analytic continuation
or canonical completion.

## Exact packet map

| Packet | What it settles | Scope boundary |
|---|---|---|
| [Positive-log chamber](NONINTEGRAL_LOCAL_POWER_RATIONALITY.md) | Complex coefficient powers are rational exactly at nonnegative integers for the positive hyperbolic recurrence | This is the non-tempered chamber, not all automorphic local parameters |
| [Irrational absolute powers](IRRATIONAL_ROTATION_ABSOLUTE_POWER_RATIONALITY.md) | Real nonnegative absolute powers are rational exactly at even integers | Irrational rotation and the stated zero convention are essential |
| [Rational branch census](RATIONAL_ROTATION_BRANCH_CENSUS.md) | Periods, exact zero classes, branch conventions, and integer collision sums | Periodicity at each denominator does not give uniform degree |
| [Irrational complex powers](IRRATIONAL_ROTATION_PRINCIPAL_COMPLEX_POWER_RATIONALITY.md) | The fixed-branch complex classification for zero or positive-real-part exponents | No unrestricted branch or nonpositive-real-part classification |
| [Symmetric state-space parent](TRANSFER_MATRIX_SYMMETRIC_PARENT.md) | Integer powers as genuine finite representation matrix coefficients; determinant-relation quotient | A resolvent matrix coefficient is not a determinant L-factor |
| [Uniform rational-angle degree](RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md) | Uniform reduced degree exactly in the relevant polynomial chambers | The complex-exponent result is qualitative outside them |
| [Positive determinant release](POSITIVE_DETERMINANT_POWER_RELEASE.md) | Exact scalar rescaling with positive real eigenvalues and determinant | No unspecified square-root or logarithm branch |
| [Dense torus trace powers](DENSE_TORUS_TRACE_ABSOLUTE_POWER_RATIONALITY.md) | Higher-rank rigidity and exact surviving character counts | Dense compact torus, not an arbitrary singular orbit |
| [Real rational-angle exact degree](RATIONAL_ROTATION_REAL_POWER_EXACT_DEGREE.md) | For real lambda>0, degree b unless lambda=2m, when it is min(b,2m+1) | The all-real statement is false for complex lambda; an exact counterexample is retained |
| [Universal single-grade Euler obstruction](UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION.md) | For n,k>=2 no finite universal virtual representation has the required determinant inverse | Extra arbitrary Frobenius scalars and resolvent parents are outside the theorem |
| [Finite-graded classification](FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md) | Finitely many universal virtual grades exist exactly for n=1, k=0,1, or (n,k)=(2,2) | The remaining infinite-graded escape is formal and necessarily virtual |

Each row links to the resident proof, exact hypotheses, checker, fixture,
and source bindings. The last three packets have separate exact-source
review reports in this directory.

## Why the parent distinction changes the programme

For

\[
 F_{n,k}(A,T)=\sum_{r\ge0}
       \operatorname{Tr}(\operatorname{Sym}^r A)^k T^r,
\]

the identity matrix is decisive. A representation must send it to
identity; freely fitting eigenvalues there is not a universal
representation construction.

The [single-grade proof](UNIVERSAL_COEFFICIENT_POWER_EULER_OBSTRUCTION.md)
already finds a positive second-coefficient discrepancy. Allowing
positive integral grades gives the one additional chamber

\[
 F_{2,2}(A,T)=
 \frac{1-\det(A)^2T^2}{\det(1-T(A\otimes A))}.
\]

The second grade is negative. For every n,k>=2, the unique formal
infinite-graded factorization has second class equal to minus the
nonzero quadratic relation representation of the diagonal Segre
algebra. Outside the listed finite chambers infinitely many grades
are required.

This uses classical Segre/Eulerian and symmetric-power algebra.
The result is an exact programme boundary, not a novelty claim for
those theories.

There is also a constructive change of observable:
power traces rather than coefficients give the usual determinant
identity for End(V) tensor powers on compact unitary inputs.
That is a coherent representation operation, but it changes the
scalar object. It does not realize the original coefficient-power
series by renaming it.

## Current L0--L9 position

| Levels | Current result |
|---|---|
| L0--L1: definition and multiplicativity | Several branch/zero chambers and the monomial multiplicativity obstruction are exact |
| L2--L3: Euler structure and finite degree | Formal multiplicative products require their input hypotheses; scalar degrees and universal representation obstructions are now sharply separated |
| L4: weights, determinant, duality | Finite representation and determinant identities are explicit; no general ramified or global compatibility theorem is supplied |
| L5--L6: completion and continuation | No new global completion is established by these eleven packets |
| L7--L8: functoriality and realization | Honest local state-space and representation operations exist; global realization is not inferred |
| L9: explicit formula and zeros | No new zero theorem, positivity theorem, RH, or GRH consequence |

## The next pass should leave the coefficient catalogue

Two global diagnostics are now being pursued separately from the closed
local classifications:

1. An all-prime unitary Satake deformation of an actual arithmetic
   family, tested for a meromorphic germ at s=1. Local purity and
   determinant preservation are not assumed to imply completion.
   This candidate is under independent review, not imported as a
   theorem by this checkpoint.
2. A precise classical Estermann comparison for the global divisor-power
   model. This tests whether a formal infinite parent can survive
   analytic continuation. Its hypotheses must not be transferred
   silently to varying automorphic Frobenius parameters.

Other useful gates are tensor/duality coherence, genuinely coupled
multivariable parents, and independently defined dynamical operators.
An added variable, a fitted matrix, or an ad hoc gamma factor is not
itself a new object. A proposed parent must recover the scalar shadow
and support an operation or symmetry before specialization.

Finite-prime surgery has a strong existing multiplicity-one literature.
Even some coprime-twist functional equations admit artificial paired
Euler modifications. Such examples are controls, not evidence of a
new automorphic family.

The [wave-2 research map](WAVE2_RESEARCH_MAP.md) retains the broader
primary-literature comparison. Its six-packet status and queue are
historical; the exact-degree, determinant-release, dense-torus,
single-grade, and finite-graded results above supersede those entries.

## Earlier work is not displaced

The native relative-extraction, signed finite-field cancellation, and
actual-Xi metric work continue under
[PR #765](https://github.com/gfreund123/riemann/pull/765).
The central 67-free/core-wavelet reduction remains under
[PR #760](https://github.com/gfreund123/riemann/pull/760).
These are separate mathematical consumers, not consequences of local
coefficient-power rationality.

Minor scalar extensions belong on this programme branch. A further
branch should earn its independence through a different load-bearing
global or non-scalar theorem, not through another periodic example.

## Replay and exact identities

Every packet has a bounded exact producer and tests, exercised in
normal and optimized Python. Source manifests bind frozen Git blobs,
not just internally consistent derived JSON. No finite census is the
proof of an all-parameter classification.

Original scientific commits named by the reviews are retained on
durable source refs. For this programme fetch:

    git fetch --no-tags origin refs/heads/codex/review-sources-universal-euler-wave2 refs/heads/codex/review-sources-finite-graded-parent-wave2

The exact targets are 330c6f8b85fa1923f2d4914ce3ab1775b0e56c75 and
7c9e7bde7980c4cfc0b3c3e521fa022319244caa. The former retains the
02e53055 source state used by an executable manifest. These refs
are acquisition aids; the commit/path/blob checks remain authoritative.

No external publication priority is established. RH and GRH remain open.
