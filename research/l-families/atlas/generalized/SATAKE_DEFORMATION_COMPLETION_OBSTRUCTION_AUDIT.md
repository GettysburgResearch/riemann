# Independent audit: fixed-parameter Satake completion obstruction

Status: exact-source review passed; proposed programme mathematics, not an
integrated RH result. No source repair was needed.

Reviewed source: b895598abd936a2e42e5b7d14a7e10cc2bf41486.
Programme copy: abc7d84e57da75fdd4f47db4b9df31e6304868f6.
Review date: 2026-08-30.

The root reviewer read the complete proof, producer, tests and source manifest,
authenticated and regenerated the fixture, and independently reconstructed the
analytic argument. A separate reviewer also audited the exact frozen source
and replayed its tests without changing it.

## Exact object and import boundary

The proof-bearing [source note](SATAKE_DEFORMATION_COMPLETION_OBSTRUCTION.md)
has Git blob 907bb4c262939d4f812b282f155857218a97b2e5 at the reviewed SHA.
The producer, fixture and tests have blobs, respectively:

- e3131456ec7d0f1678645ecfca0c8723ce66dabd;
- bcae904fffd09ce508db3c137a8807406750e9b7;
- 6fafc40956a87379b139b88417bc7b1ea22f70b7.

The fixture payload is
bff3cd95a75f5953fde2d1331e736d17144851827bd92affa8e7bdd268ebc60f.
These are frozen identities, not claims that remote PDFs were machine-proved.

The arithmetic inputs are exactly normalized Delta unitarity and qualitative
Delta Sato--Tate. The reviewer checked Deligne's Theorem 8.2, printed p.302,
including the roots of the Hecke polynomial and exponent (k-1)/2, in the
[author's IAS copy](https://publications.ias.edu/sites/default/files/Number23.pdf);
the Numdam copy is identified in the source. BLGHT Corollary C, printed p.32,
explicitly concerns tau(p)/(2 p^(11/2)); see the
[publisher PDF](https://ems.press/content/serial-article-files/41128?nt=1).
There is no additional unverified non-CM premise, effective rate, PNT or
numerical Delta sample hidden in this application.

## Analytic review

1. The deformation is conjugation-equivariant. On the inverse-pair-plus-one
   unitary class its generator is skew-Hermitian, traceless and commutes with
   the original matrix. Rank, unitarity, determinant one and contragredient
   compatibility survive. Tensor and twist functoriality are not asserted.
2. The pushed Sato--Tate density is (1-cos(phi))/(2 pi). The frequency-three
   shift annihilates the two needed nonconstant phase modes for every fixed
   parameter. Thus the prime trace mean is exactly 1-J_0(epsilon), with J_0
   merely shorthand for the displayed elementary circle integral.
3. The two cosine inequalities give the stated rational lower and upper
   bounds. For each fixed 0<|epsilon|<=1 these put the mean strictly between
   zero and one. This is not an inference from a finite Taylor expansion.
4. The Abel argument is valid with only centered prime sums o(pi(x)).
   The elementary Euler logarithm of zeta gives
   sum_p p^(-sigma)=log(1/(sigma-1))+O(1), without a prime-number theorem.
   The higher-prime-power logarithmic remainder is uniformly bounded.
5. Positive real Euler factors fix the real logarithm on sigma>1. A
   meromorphic germ would have an integer Laurent order, incompatible with
   the proved noninteger logarithmic limit. Division by any nonzero
   meromorphic multiplier germ proves the stated no-rescue corollary.

In particular, the conclusion applies to each parameter separately. It does
not require joint analytic dependence of a hypothetical completion family.
It does not assert a constant-times asymptotic, an algebraic branch germ,
monodromy, or a natural boundary.

## Reproduction and hostile controls

The root reran all 20 tests, the complete source-authenticated fixture checker,
and its typed/hash contracts in both normal Python and Python -O. All passed.
The separate exact-SHA reviewer also reported both modes and Ruff passing.

The root additionally evaluated 7,350 independent binomial coefficient
comparisons: all formal degrees 0,...,24, frequencies 1,...,6, and phases
-24,...,24. The independent formula extracts the required monomial directly
from (z^f-z^(-f))^n/(2^n n!), rather than multiplying the producer's Laurent
polynomials. Four additional signed rational parameter controls included
denominator 2^127-1. All passed.

The second reviewer separately reported a 648-case phase census,
nonorthogonal conjugation checks, tiny signed parameters, and strict
work-bound equality rejection. These additional reported checks are
distinguished from the root's own replay.

The exact computations authenticate bounded algebraic controls. The infinite
arithmetic distribution theorem, analytic convergence and meromorphic-germ
argument remain written/imported mathematics, not a formal computation proof.

## Decision and remaining research

Accept this exclusion family within the proposed generalized-L-object
programme. Preserve the frozen five-file source unchanged.

The result does not classify globally completable deformations and does not
establish a new automorphic object. Its first trace-mean variation vanishes;
the obstruction begins quadratically. The next substantive test is a family
that preserves the first prime trace mean, and then a comparison between
finitely many tensor moments and the full tensor-completion requirement.
No priority or novelty claim has been established.
