# Five routes: field averaging, paired probes, strip compactness, native energy, determinant mass

**PROPOSED component mathematics with complete written arguments and finite
replays. No improved zeta zero-free boundary or RH proof is claimed.** This
packet attacks the five directions requested in the conversation rather than
retuning the old near-0.9 exponent budget.

Base: #1000 at `6c4d5309d64978b420c2b897977d6db2ea01ce03`.
All files are new. Inherited proofs and integrated scientific status are
unchanged. Source qualifications and open estimates are part of each theorem.

## What actually advanced

| Route | New component in this pass | What is still missing |
| --- | --- | --- |
| Varying quadratic fields | A ramification-preserving primitive source, conductor-uniform invertible Euler kernels, and a complete signed average approximating ordinary Mobius with error at most `96 X^(5/4) sqrt(1+log X)/sqrt Q`. | A power bound on that signed average; cofactor orthogonality does not remove the common Mobius term. |
| Principal Eisenstein / multiprobe | Two incommensurate scale notches remove real power-log modes without jointly losing any target zero, with only polynomial height cost. Explicit positive paired series make the same argument legal for the principal Eisenstein and Gaussian fields. | A complete physical theta adapter and a stronger signed bound for BOTH filtered remainders. |
| Narrow-strip finite laws | An explicit counterexample to variance/moment-only compactness, followed by a one-exponential-moment strip-transfer theorem and a product-law budget. | Cofinal approximation of the actual theta law satisfying that budget and a narrower zero band. |
| Rational Newton energy | An energy-adaptive core cutoff can spend an intermediate power-error allowance on much larger cores; a complete conditional recurrence gives an exact improvement budget. | The rough-core upper estimate, and a justified transfer from sparse native cuts to a full recurrence when needed. |
| Primitive determinant | The complete regularization comparison now holds for every mass. An RH-scale choice gives condition number `O(N^(1/2))`; a 5/6 target gives `O(N^(1/6))` and heat window `O(N^(1/6) log N)`. | The centered short-time trace/height bound. A larger explicit bulk must be subtracted; conditioning is not prime cancellation. |

Reading order: [QUADRATIC_AVERAGE.md](QUADRATIC_AVERAGE.md),
[PAIRED_PROBES.md](PAIRED_PROBES.md),
[STRIP_COMPACTNESS.md](STRIP_COMPACTNESS.md),
[MESOSCOPIC_DETERMINANT.md](MESOSCOPIC_DETERMINANT.md), then
[NEWTON_BUDGET.md](NEWTON_BUDGET.md).

## The strongest new arithmetic interface

Let `D(Q)` contain all positive squarefree d<=Q with d=3 mod 4, and let
chi_(-d) be the actual primitive quadratic character. Remove only rational
2 and 3, retaining every other ramified prime. For squarefree n prime to 6,

    b_(-d)(n)=mu(n) product_(p|n)(1+chi_(-d)(p)),

and it is zero otherwise. For Q>=2^16 and every array |u_n|<=1,

    |average_(d in D(Q)) sum_(n<=X)b_(-d)(n)u_n
                         -sum_(n<=X)mu6(n)u_n|
       <=96 X^(5/4) sqrt(1+log X)/sqrt Q.

The estimate is elementary and retains the whole finite family. At a desired
boundary theta>1/2, choosing Q=X^(5/2-2theta) makes this comparison error
small enough at the target power. In particular Q=X^(5/6) is adequate for
a 5/6 target and Q=X^(3/2) for the square-root target. These are FAMILY
SCALES, not newly established zero-free boundaries. The remaining signed
average has not been bounded at those powers.

## The most important correction to the speculative plan

A common narrow zero band, variance one, and convergence of every fixed
moment do not guarantee convergence where zero exclusion is needed. The
rare-jump construction in STRIP_COMPACTNESS.md proves this explicitly.
A uniform exponential moment at just ONE R>1/2 in the actual Xi variable
repairs the argument. This avoids imposing uniform graph-size or all-order
Jacobian bounds, but it adds a real tail condition which finite moment
matching alone cannot replace. No new degree-22 fit is claimed.

## Reproduction and review boundary

Run `python -I -S -B replay.py` from this directory. It authenticates the
manifest, runs five finite verification lanes in parallel in normal and
optimized Python, checks their complete output digests, and rejects twelve
separately executed corruptions. `verify.py --lane determinant` emits all
directed finite enclosures; the other lanes likewise emit their full reports.
CHECKS.json binds those full reports without storing their large fractions.

The result is **20,279 finite predicates per mode**, including repeated
coefficient/domain checks, and twelve rejected mutations. Finite tests do
not certify the infinite proofs or the explicitly open arithmetic estimates.

The user requested parallel research agents. No separate agent-launch tool
was available after discovery, and no agents were launched. The five research
notes and checker have the same author. Concurrent verification subprocesses
are not independent research agents or referees. There is no Lean build,
actual L-value/zero computation, whole-repository validator, or remote CI claim.

See [SOURCES_AND_REVIEW.md](SOURCES_AND_REVIEW.md) for exact source scope,
benchmark correction, tradeoffs and the remaining five research targets.
