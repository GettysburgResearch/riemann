# Exact-source receipt: cubic average, authored rational note, and packet scope

**Reviewer:** /root/signed_average_attack, the separate signed-average
research agent. This is an AI-agent review and exact-content receipt,
not human external acceptance or proof-assistant certification.

**Frozen source commit:**
[38ee7069e23ae24fd693e70149dc817900c3caa4](https://github.com/GettysburgResearch/riemann/commit/38ee7069e23ae24fd693e70149dc817900c3caa4).

**Source tree:** 6df69e2b5674372695530860f9528b8db7aee9ff.

**Parent commit:** 506e3808d2f1e86a31a6d1f70cc7da58367c9918.

The reviewer obtained the listed committed bytes using
git show at that exact source commit, checked their Git blob identifiers,
and recomputed their byte counts and SHA-256 hashes. The cubic proof,
its content review, the authored rational proof, and the exploration
match the final versions previously read. The final packet README
was read again, including its last two clarifications. The committed
diagnostic was executed directly from its committed bytes.

Only this receipt is added by the reviewer after the freeze. No
frozen source, mathematical claim, diagnostic, or navigation file
is changed by this receipt.

## 1. Exact committed objects and the type of attestation

Except for the final root-README row, paths below are relative to
standalone/2026-10-10-conductor-averages/. Git blob identifiers and
SHA-256 digests refer to the source commit above.

| Object | Attestation | Bytes | Git blob |
|---|---|---:|---|
| [CUBIC_CONDUCTOR_AVERAGE.md](CUBIC_CONDUCTOR_AVERAGE.md) | Independent mathematical reconstruction at the stated imported-input scope | 24,307 | ce56a368ec623da97a1977e5bd72750e8b6ab148 |
| [REVIEW_CUBIC_CONDUCTOR_AVERAGE.md](REVIEW_CUBIC_CONDUCTOR_AVERAGE.md) | Exact binding of the preceding independent content review | 12,131 | 66d9470b43e7033afc50c82cc5b2c9cf5e179c2b |
| [RATIONAL_PRIME_INCIDENCE.md](RATIONAL_PRIME_INCIDENCE.md) | Author confirmation; not this agent's independent review | 35,732 | f22de70e282f7f5647879060377ca927d9b458be |
| [EXPLORATION_SINGLETON_SIEVE.md](EXPLORATION_SINGLETON_SIEVE.md) | Author confirmation of an expressly unpromoted exploration | 8,517 | e7ad36ce77f6414f0931cdb5a6168348d0d9be36 |
| [check_conductor_exponents.py](check_conductor_exponents.py) | Source inspection and execution of finite diagnostics | 6,301 | a0ae30ebd6c258abf651554dd323f8402c107334 |
| [conductor_exponent_report.json](conductor_exponent_report.json) | Exact regenerated-output comparison | 2,479 | a15e06b5a641fdabf86703cc6bf427d6113d50e1 |
| [Packet README](README.md) | Navigation and mathematical-scope consistency review | 13,365 | a3f4ef373abedd89dd70bc9a702e5a526fd404b9 |
| [SOURCE_LOCK.json](SOURCE_LOCK.json) | Independent repository-input content verification | 9,471 | 5b439c3dbb466d0da4fa6e86ea94f28d7b69bb1b |
| [Root README](../../README.md) | Whole-blob identity; scope review of its added packet navigation | 12,828 | a72964a65fee97fe09e39a8b60eac18d8ab6f2d5 |

The corresponding SHA-256 digests are:

| Object | SHA-256 |
|---|---|
| Cubic proof | 74d9063bd36128d2b510a11d96dda8055539bd7c7a2f2d07f5cc3a105223ea61 |
| Cubic content review | 90d6a4420fa17cfe22719c650833d88e50d3cf1d3727404bc4111eb2743a6d73 |
| Rational proof | 84b3aa3ba6ab0bdd05f70e2682f52d46697a335c8fa4f91cae77107de3b04d0e |
| Singleton exploration | 448a711f232d6a001769aa9849cf3331045e99ce2a4dfe47d8f4ca4a190f79aa |
| Finite checker | 7adb5521e29ccb357b500b1ad89332eb26138041f161cd40f784c5eddbbd7cdc |
| Finite report | 0dc77aa4f0a4b6b09c80c6c17726122b91342857ad914e64d059ed7111d43693 |
| Packet README | 78b62f5573a626e10b456c1227e0766ff689ca6e92fe9e2e49ff67b77d39decb |
| Source lock | 6ae3e490e5beb0a4d6cc962c552f4fa1e16c0ecc7a34a01baf2780f1d231d4c0 |
| Root README | 3d7794384f381023b193ec07287e35f7479fbee6f08fb9e74e34e0f326c7c55e |

## 2. Independent verdict on the cubic proof

**Verdict: PASS at the stated source-dependent scope.** The frozen
cubic proof is exactly the content bound by the frozen independent
review. That review reconstructs the native deduction; the reviewer
did not author the cubic conductor mean.

The analytic input is Proposition 8.1 of de Faveri's
[arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1).
Its squarefree inner index, unrestricted two outer ideal indices,
coefficient norm, and fixed family data were checked in the primary
source. The source's entire external proof was not independently
certified. In particular, a uniform estimate is not inferred from
the constant depending on the fixed twist in Theorem 1.2.

The independent reconstruction covers the conductor-uniform
approximate functional equation, separation of the direct and
dual polynomials, the primitive product's bad-prime values, the
unique index decomposition \(n=sqr^2\), and the absence of a
spurious \((q,r)=1\) restriction. It checks that the moving
background stays in the coefficient vector and never becomes
part of the fixed bad set.

The finite unit/ray correction is essential. The reviewed proof
uses the source's explicit Eisenstein normalization and class
number one to eliminate an unramified ambiguity after the local
components are fixed. The background is independent of the
varying cubic labels inside each fixed class. No arbitrary
moving-character constant is hidden at this step.

The complete row identity retains the principal mask and all
physical nonunit zeros. Its positive principal-mask count has
weight \((Nab)^{-1}\); the first mean has factor \(ABR^{1/4}\).
Their dyadic cancellation and the strictly convergent
higher-multiplicity sums give
\[
\mathcal Q_L^\Phi
\ll D^{k+\epsilon}H^{1/2}L^{3/4}.
\]
The reviewer also independently checked Corollary 4.3:
\[
\mathcal Q_{L;A,B}^\Phi
\ll D^{k+\epsilon}H^{1/2}
\left[L^{1/2}+L^{3/4}(M/N)^{1/12}
+L^{2/3}M^{-1/6}\right].
\]
Its three diagonal-size conditions are exactly
\[
Ng_1\le H,\qquad
(Ng_1)^9\frac{\min(Na,Nb)}{\max(Na,Nb)}\le H^6,
\qquad
(Ng_1)^4\le H^3\min(Na,Nb).
\]

These are positive tuplewise accounting bounds at every fixed
order, for the stated bounded column coefficients and fixed
smooth radial row test. They survive arbitrary additional tuple
selectors. They are not a proof of cancellation in the remaining
signed large-singleton sum.

The strict examples compare specified positive conductor
accounting branches. PR #926 already bounds some corresponding
complete structured signed blocks more strongly. The frozen
proof and review explicitly preserve that distinction. The
inherited fourth-moment remainder consequence additionally
retains \(1<h\le11/10\), the source's native coefficients,
smooth tests, and other hypotheses.

## 3. Author confirmation of the rational proof and exploration

The frozen rational proof is the reviewer's final authored
version. This receipt confirms its identity and intended claims;
it does **not** count an author's confirmation as an independent
review. A separate agent supplied the packet's
[independent rational review](REVIEW_RATIONAL_PRIME_INCIDENCE.md).

The rational note proves the native bound for tuples with small
ordinary rational radical, including the squarefull-total-norm
sector. It treats a split rational prime with two ideal factors
and an inert prime with ideal norm \(p^2\) with their correct
different local multiplicities. Principal-mask rational primes
are counted once before the positive bound. Its pointwise
conductor branches retain exactly their named imported inputs.

The composition with the independently reviewed cubic mean
uses \(Ng_1=vw^2\), where \(v,w\) describe the singleton ideal
alone, and gives
\[
\mathcal Q_{V,W}^\Phi
\ll D^{k+\epsilon}H^{1/2}V^{3/4}W^{1/2}.
\]
Thus \(v^3w^2\le H^2\) is a controlled region. The proof does
not assume rational-prime disjointness between this singleton
ideal and all higher-multiplicity labels.

The singleton-sieve exploration also matches its final authored
bytes. Its coarse candidate condition \(L^2G\le H^2\) is
exactly the old classical condition \(L\sqrt G\le H\), so
that calculation supplies no new diagonal-size region. The
retained asymmetric singleton-sign profile is expressly
prospective, pending a separate uniform sixth-order family
adapter review. It is not promoted by this receipt and is not
included in the packet's proved signed-remainder subtraction.

## 4. Committed finite diagnostic and exact source-lock checks

The reviewer inspected the checker and executed the exact
committed Python bytes. Execution returned zero. Its standard
output was **byte-for-byte equal**, including final formatting,
to the committed 2,479-byte report listed above.

The report records 15,600 aggregated multiplicity assignments
for \(k=1,\ldots,8\), together with exact rational identities
and the displayed comparison fixtures. The assignments are
tuples of occurrence counts, not a claim to enumerate every
individual prime-position subset. The finite loop does not
prove the all-order convergence argument. No character-value
experiment, full arithmetic moment, zero-free region, RH result,
or imported analytic theorem is certified by this execution.
The anisotropic Corollary 4.3 was checked in the mathematical
review; it is not represented as having a dedicated test in
this diagnostic.

The reviewer independently retrieved all 14 repository input
blobs named by the committed source lock, at their declared
commits and paths. Every declared byte count and SHA-256 hash
matched, and every recorded GitHub URL agreed with that
repository, commit, and path.

The pinned OpenAI/math manuscript was also checked from its
local import path **inside the frozen source commit**, rather
than only from a mutable working-tree file. It has 169,005
bytes and SHA-256

    d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d

as recorded by the lock. These checks verify exact dependency
content, not independent correctness of the imported theta
foundation, large sieves, or subconvexity results.

## 5. Navigation and summary scope

**Verdict: PASS for consistency of the packet navigation and
summaries with the stated proof scopes.**

Before freezing, the reviewer identified the missing upper
restriction in the packet README's summary of Joint
Continuation Theorem 4.1. The committed README correctly
states
\[
4/7<a<1,\qquad b>(6-a)/5.
\]
The larger rectangular regions from that note's Theorem 5.1
correctly carry no such upper restriction on \(a\). The last
pre-freeze clarity change, specifying fixed \(e\ge0\) before
the Gaussian sampling hypothesis, is also present in the
committed README.

The cubic and rational formulas, fixture exponents, and
positive-versus-signed comparison match the reviewed proofs.
The joint continuation summary retains squarefree canonical
rows, the pinned theta foundation, coherent smooth blocks,
and the absence of an improved physical moment envelope.
The Gaussian summary retains its fixed noncompact detector,
the actual moving row budget, maximal recovery on the preceding
interval, a separate finite-truncation error, and an unproved
arithmetic sampled hypothesis. It does not transfer a compact
test estimate to the Gaussian test.

This agent's joint and Gaussian work for this receipt is a
summary-consistency check, not a second complete independent
reconstruction of those proofs. Their dedicated proof reviews
are separate packet objects. Similarly, the root README is
bound here as a whole blob, but this review's substantive
navigation check concerns its new conductor-average paragraph;
it does not re-certify all earlier project summaries.

The source README intentionally points to VALIDATION.md,
which is to be supplied in the subsequent validation-only
commit. All other local targets in the packet README were
present at source freeze.

## 6. Final boundary

The receipt approves the specified deductions and content
bindings at their declared source scopes. It does not prove
the full fourth moment, the generalized moment hierarchy,
the sampled Gaussian arithmetic estimate, the remaining
large-singleton signed bound, a new zero-free half-plane, or
RH. The existing conditional zero-extraction statement still
requires its exact arithmetic premise.

The full generalized moment and RH remain open. No frozen
claim is strengthened by this exact-source receipt.
