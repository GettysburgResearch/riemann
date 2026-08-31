# Independent audit: tensor moments and ordered Satake deformation

Status: exact-source review passed; no repair required. Proposed programme
mathematics, not a new automorphy, group-reconstruction or RH theorem.

Reviewed source: 0d7503b8575db40a46303315b8130973ed214d50.
Programme copy: 335a768d1316e5d2e49a62202af35952dd02009b.
Review date: 2026-08-30.

The root read the complete proof, producer, tests and source manifest, rebuilt
the authenticated fixture, and independently reconstructed the proof. A
separate exact-SHA reviewer also completed a clean mathematical/code audit.

## Identities and dependencies

The [proof note](TENSOR_MOMENT_COMPLETION_RIGIDITY.md) has Git blob
a2b9ab0014fe63e19dd2efb9c576905171a35aff at the reviewed source.
Producer, fixture and tests have blobs, respectively:

- 6b204cbccd4de8f801234d670c5d860c6c12101d;
- 140c626d1977f0171319c6c6ecf6676c652e8b8a;
- 8b0593a4a50144a0f7df8a4e73569e0156fa8211.

The payload digest is
9eeb9b0fa03986830bc63b8cdbaa3f1796d4c7ed844ad70840660e7e137e53b8.
The three parent files at b895598abd936a2e42e5b7d14a7e10cc2bf41486
authenticate and remain byte-equivalent after LF normalization.

## Mathematical audit

The folded Sato--Tate density is (1-cos(phi))/pi on [0,pi]. Each fixed tensor
rank is finite, each local tensor spectrum is conjugation symmetric and
unitary, and the real Euler factors are positive. The parent's Abel lemma
therefore identifies the prime moment with the real logarithmic order at one.
Meromorphy makes that order an integer.

For each fixed moment, pointwise continuity of the ordered homeomorphisms
and a uniform bounded integrand imply continuity in the parameter. On the
same connected interval this integer is constant. There is no interchange
of an unbounded tensor limit with a prime or analytic limit.

All compact trace moments then agree. The note supplies the needed uniform
polynomial approximation argument, rather than treating finite moment
agreement as distributional equality. The trace is injective on the ordered
angle interval. Equality of its laws therefore gives equality of angle laws,
and the strictly increasing CDF forces the homeomorphism to be identity.
No common meromorphic neighborhood or joint analytic completion is needed.

For the counterfamilies, the density telescoping identity and CDF transport
direction are correct. Strict positivity holds throughout the stated open
parameter interval. Inverse-CDF continuity follows from uniform CDF convergence,
compactness and uniqueness of the limiting inverse.

The coefficient difference C_(m,j)-C_(m,j+1) vanishes for m<j and is one for
m=j. Consequently each nonzero admissible parameter produces a noninteger
j-th tensor log order. In particular j=2 preserves the first mean and changes
the second moment from one to 1+epsilon. This passes the first necessary
moment test; it does not prove meromorphy of the first Euler product.

The two important escape boundaries are retained: arbitrary measure-preserving
rearrangements need not be identity, and tensor-dependent parameter intervals
can have no common nonzero parameter. Neither is covered by the theorem.

## Independent reproduction

The root reran all 20 tests and both checker modes, normally and under Python
-O. All passed, including full typed reconstruction, source hashes, strict
parameter endpoints, tiny signed rationals and artifact tampering.

An additional root algorithm used walks on nonnegative spin indices, with
only an upward step at zero and three steps j-1,j,j+1 above zero. It compared
25 baseline moments and all 300 shifts in 0<=m<=24, 1<=j<=12 against the
producer. Every value agreed. This uses the direct character-product
recurrence, not the producer's Laurent multiplication or binomial formula.

The separate reviewer reported another normal/-O replay, complete fixture
checks, and independent algebra through m,j=30. The author separately
reported a clean fresh detached CRLF checkout. These are finite algebra
checks; they do not machine-prove Sato--Tate or analytic continuation.

## Prior art and decision

[Larsen's paper](https://arxiv.org/pdf/math/0212193) explicitly relates
compact-group trace moments to mixed-tensor invariant dimensions and studies
isolation among genuine Sato--Tate measures. Its introduction distinguishes
this from general reconstruction; the source also records the
[Larsen--Pink reconstruction boundary](https://people.math.ethz.ch/~pink/ftp/LP1.pdf).
The counterfamilies here vary arbitrary positive laws, not genuine compact
group realizations, so finite-moment insufficiency does not contradict that
prior art. No novelty priority is claimed.

Accept the two statements at their stated quantifiers. Preserve the frozen
source and its explicit distinction between necessary moment tests and actual
global completion. The remaining broad problem is classification of genuinely
completable generalized objects outside this ordered deformation model.
