# Cross-route review and disposition of the all-out proof attempt

Status: focused mathematical reading and a proposed cross-route theorem packet;
not an independent audit of all repository claims. RH remains unproved.
No other agent's branch, historical file, canonical claim or review status is changed.

## What was read, and what changed the approach

The current PR descriptions were surveyed, followed by the actual proof files
listed below. Dates and stale PR text are not treated as proof provenance.

| Exact source | Mathematical conclusion used in this pass | What does not follow |
|---|---|---|
| PR #793, f22b67db113d1aa4f986fe35a2fc0321fdff7d47, pass2/R3_HARDY_CAPTURE.md | The damped resolvent is a source-defined self-adjoint trace-class operator; each hypothetical nonreal pair survives the infinite Hardy background and has a finite witness. | Arithmetic positivity. The construction changes the compact-band metric; the original Lamzouri/BGST constants do not transfer. |
| Same head, pass2/R2_CAUSAL_ENERGY.md | Every individual reciprocal-zeta pole forces positive causal-energy blow-up; the complete Mobius diagonal is finite at every positive damping. | Finiteness of a meromorphic line integral is not causal Hardy membership. The signed off-diagonal is not bounded. |
| Same head, pass2/R1_XI_MINIMAL_RANK.md | Explicit actual-source determinant completions through orders two and three have minimal ranks 15 and 32. | These completion matrices are not compressions of Route 3's operator, and no all-order completion is supplied. |
| PR #790, 634d9a8ec4b0819442e601686a109ff7015b7b0b, joint-ray-pass4/PROOF.md | The Gaussian/Gamma-mixture Fourier comparison is uniform in its stated joint regime, the full prime main term is removed, and fixed rational rays detect off-line zeros. | The ray t=m/u eventually leaves t<=c log m. A small-time or growing-frequency theorem cannot be used on a fixed-center ray. The prime-weighted norm, not just pointwise Fourier error, matters. |
| PR #785, 9a965c26fd3e0310736829689db1734bcb5c3ec4, 02_SOURCE_HERMITE_STIELTJES_CLOSURE.md | Companion, Hermite, safe-Pick and Stieltjes signs are linked by exact transforms. Nonreal locations contribute negative squares, not one direction per multiplicity. | Spectral generating-function positivity does not imply coefficientwise positivity; a Stieltjes representation is not supplied. |
| PR #786, fc550cb0531e7abbc438a9b6eefa5ca11f90abc7, reports/claude/2026-09-01-repository-assessment.md | The critique correctly demands distinguishing genuinely new estimates from reformulations and from finite evidence. | Its sweeping historical/novelty judgments and each claimed global refutation were not independently audited here. This pass does not adopt all of them by citation. |
| Own PR #792, 875e8dd47186e924445533513a1ad405af09d7a7 | Prime powers, archimedean coefficients, the diagonal and exact signed energy are separated; the remaining coefficient bound is source-specific. | A trace-norm bound or a finite meromorphic radial bound is not the missing positivity. |

The most useful new connection is between #793's actual operator and #792's
actual scalar coefficients. Neither needs to be relabeled as the other.
BRIDGE.md proves their precise relation, an arithmetic construction with
explicit cutoff tails, and a fixed-basis finite-section transfer.

## Why this is more than a changed name for the old inequality

The new unconditional assertions are: an absolutely nuclear gamma-plus-prime
construction with norm below 30; a one-safe-point formula for every finite
matrix; a linear-size recovery of degree-n trace moments with an explicit
O(log n/sqrt n) tail; quantitative convergence of predetermined finite
sections; and an actual 4-by-4 rational source certificate.

The identity A*TA=T is universal stationarity, not arithmetic positivity.
The attempted end-to-end proof would use that form as a positive metric,
apply Hilbert--Schmidt Cauchy--Schwarz, and bound all scalar coefficients.
The positivity step fails as a deduction from the established hypotheses:
a rational strip-confined control has a positive first four sections and a
negative fifth pivot. Its ordinary invariant heat is positive at every time.
This does not refute positivity for actual xi.

The arithmetic norm calculation exposes another specific mismatch. A prime
atom has trace norm O(Lambda(n)n^-5/4), but its SHARP form bound relative to
the base positive resolvent is Lambda(n)/(b sqrt n). The latter constants
are not summable. An absolutely convergent trace-class perturbation need
not be a small relative perturbation of an injective compact positive
operator. No uniform spectral gap is available to erase that distinction.

## What to attack next in this exact formulation

The conclusion-facing task is to prove positivity of the literal arithmetic
form in BRIDGE.md, Section 8, retaining all shifts and the pole/gamma terms.
A source-specific factorization or a signed relative-form estimate would
be substantive progress. The finite matrices can test such a conjecture
without zero input, and the tail bounds make the test interface explicit.
More successful finite pivots, or merely another norm on the same meromorphic
continuation, would not establish the missing assertion.

The present attempt does NOT produce a signed estimate beyond the previous
prime-cancellation boundary. It changes the available constructive interface
and the finite-section error cost, not the truth status of RH.

## Primary-literature boundary

The underlying Laguerre and Fourier identities are classical. DLMF 18.12.13
and 18.18(i) supply generating functions and L2 completeness; the analytic
proof explicitly derives every normalization used here. Euler--Maclaurin,
the Bernoulli Fourier bound, and the expansion of log Gamma are standard.
The source/positivity setting is the established Weil--Hardy framework.
Relevant primary reference: Masatoshi Suzuki, *On the Hilbert space derived
from the Weil distribution*, arXiv:2301.00421 (abstract/version metadata
checked; no new theorem from the unread full article is imported).
A search also located arXiv:2606.09096, *Weil's quadratic form via the screw
function*. Its abstract was read; the attempted HTML fetch did not succeed.
No result from that full paper is assumed or claimed independently verified.
No new external priority is claimed for any general RH criterion.

Primary URLs:
- https://dlmf.nist.gov/18.12
- https://dlmf.nist.gov/18.18
- https://dlmf.nist.gov/25.2
- https://dlmf.nist.gov/5.7
- https://dlmf.nist.gov/24.8
- https://arxiv.org/abs/2301.00421
- https://arxiv.org/abs/2606.09096
