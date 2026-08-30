# Generalized L-objects: continuation checkpoint

Status: exact local/global boundaries and a source-specified global quotient
for [programme #764](https://github.com/gfreund123/riemann/issues/764),
carried by [draft PR #766](https://github.com/gfreund123/riemann/pull/766).
This is a checkpoint during the requested research pass, not a statement
that eight hours have elapsed. No new automorphic L-function or external
novelty is claimed.

Checkpoint updated: 2026-08-31. Sixteen exact packets are resident,
including the independently reviewed Rankin--Selberg quotient.

## The main conclusion

There are now five distinct questions, with different answers:

1. Does a scalar sequence have a finite recurrence?
2. Is it a matrix coefficient of an honest finite representation?
3. Is its generating function a universal determinant product, possibly
   with finitely many positive integer grade indices and virtual classes?
4. Do the infinite virtual grades come from an independently presented
   algebra, rather than scalar fitting?
5. Does the all-prime object have the required continuation and completion?

An affirmative answer at one level does not supply the next. Here the
infinite grades do have a classical Koszul--Lie realization, but the
unaltered divisor-power models still face a global natural boundary or
a finite-gamma obstruction.

There is now a distinct constructive answer: a canonical quotient of an
actual, genuinely coupled automorphic period matrix. It inherits a global
meromorphic reflection law but acquires a provably noninteger Dirichlet
frequency. This is a concrete global quotient, not another fitted local
recurrence. It remains in the rational closure of classical period entries
and is not a new automorphic representation.

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
| [Finite-graded classification](FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md) | Finitely many universal virtual grades exist exactly for n=1, k=0,1, or (n,k)=(2,2) | The remaining infinite product is formal and signed; its classical Lie parent is now constructed |
| [Actual Satake deformation](SATAKE_DEFORMATION_COMPLETION_OBSTRUCTION.md) | A unitary determinant-preserving deformation of Delta's symmetric-square parameters fails meromorphy at s=1 | Local purity is retained; tensor compatibility is not |
| [Tensor-moment rigidity](TENSOR_MOMENT_COMPLETION_RIGIDITY.md) | Meromorphic completion of every tensor moment forces the stated connected monotone folded-angle deformation to be trivial | Common-interval continuity and monotonicity are essential; finitely many moments do not suffice |
| [Global graded boundary](GRADED_PARENT_GLOBAL_BOUNDARY.md) | Natural boundary, finite-gamma obstruction, graded convergence threshold, and an explicit centered change of object | Theorems concern the stated divisor-power model, not arbitrary varying automorphic parameters |
| [Classical Segre Lie parent](SEGRE_KOSZUL_LIE_PARENT.md) | Actual signed dual Lie modules in every grade and strict all-grade signs | This is established Koszul duality; no analytic completion or positive Euler parent |
| [Rankin--Selberg quotient](RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md) | Canonical cusp-flag quotient, global reflection, positive real quotient metric, and first noninteger frequency 9/2 | Possible denominator-zero poles; no ordinary expandable Euler product or new automorphic representation |

Each row links to its resident proof and reproduction contract. The later
analytic/parent packets and the earlier exact-degree, single-grade and
finite-graded packets have separate exact-source audit reports here.

## An actual global quotient, with its loss of ordinary frequencies

Let V=S24(SL2Z), f0=Delta E4^3, f1=Delta^2, and ell(f)=[q]f.
The functional and normalized cusp coordinate specify the flag
W=ker ell=span(f1). Form the actual completed Eisenstein period matrix

    I_ij(s)=integral_(Gamma\H) y^24 conjugate(f_i) f_j E*(z,s) dmu,
    I(s)=A(s) zeta(2s) D(s),
    A(s)=pi^(-s) Gamma(s) (4pi)^(-s-23) Gamma(s+23).

Its canonical one-dimensional quotient is

    Q(s)=det I(s)/I_11(s)=A(s) L_Q(s),
    L_Q(s)=zeta(2s) [D00-D01 D10/D11],
    Q(s)=Q(1-s).

This is invariant under all constant complex changes preserving the
normalized flag. For real sigma>1 it is the strictly positive minimum
of the period norm over ell(f)=1. No constant basis diagonalizes the
entire period family: its first three coefficient directions already
rule that out. Parameter-dependent diagonalization is not excluded.

Both completed endpoint poles, zero and one, survive, with opposite
residues det(G)/(2G11), where G is the Petersson Gram. Additional poles
can occur at zeros of I11; the exact local cancellation condition is
stated in the proof. Real positivity does not settle complex zeros.

The first noninteger frequency is an exact source calculation. For
w=s+23, after the shear g=f0-696 f1, one has b1=0,b2=1,c2=0,
b3=-48 and c3=195660. Consequently the quotient has the
fractional-frequency contribution

    [(9/2)^(-w)] F = -88203653222400.

An absolute Neumann expansion on a right half-plane justifies the
calculation globally as a generalized Dirichlet series. The multiplier
zeta(2s) leaves that first noninteger coefficient unchanged. Therefore
neither F nor L_Q can be an absolutely convergent integer-indexed
Dirichlet series on any right half-plane, or an ordinary-prime Euler
product with normalized power-series factors and absolute expansion.

Generalized prime/norm systems, conditional or formal products, and
other modified objects are not excluded. The completion is inherited
from the actual period, not fitted afterward. Schur quotients, modular
forms and Rankin--Selberg periods are classical; no priority claim is
made for this source-specified construction.

The [exact-source audit](RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT_AUDIT.md)
records separate proof review, independent q/frequency reconstruction,
and the correction of an introductory completed-pole omission in the
Miller--Schmid source. The analytic imports are not machine-certified.

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
are required. The new classical parent makes this more concrete:

    R_r = tensor_i Sym^r(V_i),
    g = FreeLie_super(E-star) / <image of dual multiplication>,
    W_d = (-1)^(d+1) [g_d-star].

The independently defined ring is Koszul. Super PBW and the equivariant
resolution give the exact product-group identity; restriction to the
diagonal recovers the original coefficient powers. The no-gap lemma for
a degree-one-generated Lie algebra proves that every nonexceptional
equal-rank grade is nonzero, with strict alternating signs. This is
stronger than eventual dimension asymptotics, but is still signed.
Direct bar complexes and an unequal-rank syzygy control test the actual
multiplication and relations, not a fitted Hilbert series.

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
| L5--L6: completion and continuation | The actual period quotient has global meromorphy and reflection, with possible denominator-zero poles; the divisor-power obstructions remain unchanged |
| L7--L8: functoriality and realization | Honest local state-space, a classical signed Lie parent and an actual flagged period source exist; no new automorphic representation or twist compatibility is inferred |
| L9: explicit formula and zeros | Local-factor obstructions and a quotient pole ledger are explicit; no critical-line or complex zero-free theorem, RH or GRH consequence |

## The all-prime tests now have answers

For the actual Delta symmetric-square Satake matrices, the independently
defined map A -> A exp(epsilon(A^3-A^(-3))/2) preserves unitarity,
determinant and contragredience. Sato--Tate gives prime trace mean
1-J_0(epsilon), strictly between zero and one for
0<abs(epsilon)<=1. The logarithmic order at s=1 is therefore nonintegral,
which excludes a meromorphic germ. A nonzero meromorphic multiplier
cannot repair that germ. No stronger branch-singularity or natural-boundary
claim is inferred from this mean alone.

Within a connected, pointwise-continuous family of increasing folded-angle
homeomorphisms, meromorphy at s=1 for every tensor-power Euler object forces
all trace moments to remain integral and constant, hence forces the family
to be the identity. Explicit perturbations preserve any prescribed finite
prefix of moments and break the next one. Preserving those lower moments
does not prove meromorphic completion of their Euler products.

For the separate scalar model

    D_(n,k)(s) = sum_m d_n(m)^k m^(-s),

the Dirichlet series converges absolutely for Re(s)>1. Outside n=1,
k=0,1 and (n,k)=(2,2), its integer local numerator is noncyclotomic.
The classical Estermann theorem gives meromorphic continuation to
Re(s)>0 and a natural boundary on Re(s)=0. This excludes the proposed
same-center meromorphic functional equation and any repair by a
multiplier meromorphic across a boundary point.

The exceptional D_(2,2)=zeta(s)^4/zeta(2s) is globally meromorphic, but
the native pole-reflection argument excludes a same-center completion
by the stated finite real-slope gamma/rational/exponential factors.
It does not exclude arbitrary meromorphic multipliers: multiplying by
zeta(2s) would change the problem.

If A>2 is the largest positive reciprocal modulus of a numerator root,
the ordered real graded logarithm sum w_m log zeta(m sigma) converges
absolutely exactly for sigma>log_2(A). It converges conditionally at that
real endpoint and fails the term test below it in 1<sigma<log_2(A).
This is a convergence threshold for that graded ordering, not a natural
boundary of the rational local factor.

The centered replacement zeta(s)^4/zeta(2s-1/2) has an explicit completion,
but changes the prime-square coefficient from 9 to 10-sqrt(p), violating
the usual subpower coefficient bound. It is an example of changing the
observable, not completing the original series.

## What still merits research

Do not reopen the closed scalar catalogue or present the classical
Koszul construction as new territory. The period quotient now supplies
one actual coupled global object and a tested quotient operation. Its
next burdens are denominator-zero cancellation/control and a justified
extension to other intrinsic cusp flags. A higher-rank first-frequency
formula is under investigation, not imported as a theorem here.

An added variable, fitted matrix, formal regularization or ad hoc gamma
factor is not enough. Cross-prime or twist compatibility must be proved
where invoked. Finite-prime surgery also has a substantial existing
multiplicity-one literature and is not, by itself, a new automorphic
family.

The [wave-2 research map](WAVE2_RESEARCH_MAP.md) remains the historical
literature map. Its six-packet status and queue are superseded by this
sixteen-packet checkpoint.

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

Every packet has a bounded exact producer and tests. The current
changed-test-module scope contains 260 tests in sixteen modules. All
260 tests passed in normal Python (37.580 seconds) and under -O
(37.710 seconds). All sixteen producers passed checks in both modes.
Source manifests bind frozen Git blobs, not just internally consistent
derived JSON. For the new period quotient, the pinned programme file is
context; modularity and Eisenstein continuation are explicit primary-source
imports, not consequences of that context hash. No finite census proves
an all-parameter classification or analytic continuation.

Original scientific commits named by the reviews are retained on
durable source refs. For this programme fetch:

    git fetch --no-tags origin refs/heads/codex/review-sources-universal-euler-wave2 refs/heads/codex/review-sources-finite-graded-parent-wave2 refs/heads/codex/review-sources-satake-tensor-wave2 refs/heads/codex/review-sources-graded-global-wave2 refs/heads/codex/review-sources-segre-koszul-lie-wave2 refs/heads/codex/review-sources-rankin-selberg-quotient-wave2

Their exact targets, in that order, are:

- 330c6f8b85fa1923f2d4914ce3ab1775b0e56c75;
- 7c9e7bde7980c4cfc0b3c3e521fa022319244caa;
- 0d7503b8575db40a46303315b8130973ed214d50;
- a432061f12fd15658e9790966e5bf3d1e9830e07;
- 39f19e361c476c77cd016d314662448f43df7a80;
- b62dfc6348661992bca659c99de226a1b6b22e14.

The first retains 02e53055; the third retains b895598a; the fourth
retains the global proof 334bec3b and its independent review. The sixth
retains the original five-file quotient proof reviewed in the audit. These refs
are acquisition aids; commit/path/blob checks remain authoritative.

The recursive source-acquisition audit passed for all sixteen root
manifests: 23 frozen manifest versions, 86 literal source edges, 55 unique
commit/path file versions and fourteen source commits. Every such commit
is reachable from this programme or one of the six source refs above.
The audit follows the manifest's explicit imported-parent identity where
it differs from a historical base identity; it does not authenticate a
different file merely because the path matches.

No external publication priority is established. RH and GRH remain open.
