# Sources, reading boundary, and relationship to the repository

## Classical input

1. Luis Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the
   Riemann Hypothesis*, Atti Accad. Naz. Lincei (9), Mat. Appl. 14 (2003),
   5–11; arXiv:math/0202141. Abstract and publication metadata read. The
   integer/step-space RH equivalence is imported in the precise form stated
   by source 2, Proposition 10; the original analytic proof was not freshly
   audited line by line.
   https://arxiv.org/abs/math/0202141

2. Michel Balazard, *An arithmetical function related to Báez-Duarte's
   criterion for the Riemann hypothesis*, arXiv:1812.04309v1, 11 December 2018.
   Read the 13-page parsed paper, especially §§1–2 and §§4–6; page images of
   printed pages 9 and 10 were inspected. The step space, Vasyunin's duals,
   orthogonal-projection coefficients, and the notation nu_0 are classical
   inputs. The packet reconstructs the finite-difference dual proof and adds
   its own dilation-residual and sparse-dictionary arguments. We do not
   claim a solution of Balazard's general spectral-synthesis question.
   https://arxiv.org/pdf/1812.04309

3. NIST Digital Library of Mathematical Functions, §§2.10(i), 5.11(i)–(ii).
   The Euler–Maclaurin formula and the positive-real digamma remainder were
   checked. NUMERICS.md derives the more conservative bounded-periodic-
   Bernoulli remainder actually used, instead of treating an asymptotic
   series as an interval enclosure.
   https://dlmf.nist.gov/2.10
   https://dlmf.nist.gov/5.11

Standard Hilbert-space projection, Cauchy–Schwarz, the identity theorem,
Möbius inversion, unique factorization, and the zeta functional equation are
used at their ordinary classical strength. Their use does not import RH.
Neither the integer Nyman–Beurling equivalence nor these analytic facts have
been checked in Lean or an independent proof kernel in this pass.

## Exact repository anchor

Repository: GettysburgResearch/riemann.
Observed main: 051808c1f8367b4320c52f94b40908eb2173d622.
Root tree: 115c71ffd64b5f9ab3568185634c9efd07c89333.
Observed merge: PR #802, graph-prerequisite correction, 6 September 2026.

The authenticated connector was used to read the main branch metadata and
these exact source files:

- AGENTS.md: blob 0ad1dc2034c5d83e777343f77b41dcaf3683ef14;
- README.md: blob 56593fc6e1f1e46cdd2ede2c54f08aeb253aafb1;
- research/RESULTS_INDEX.md: blob 5eb1bf14a075e2f0881689ce15f1367d37619082.

The current integrated warning that RH is not proved is retained. This
packet does not change the canonical registry, the formal spine, earlier
reviewer verdicts, or any other research branch.

PR #793 was read through its current metadata/body at exact head
cdf2f15965decbd35afbbd09a16c89cb3e215737, branch
research/astra/20260905-three-route-assault. That description records the
finite Euler-product/full-norm obstruction and the line-one Dickman
completion, with the half-plane estimate still open. We do not revalidate
all of its source proofs or inherit its claims as dependencies.

The previously supplied local PR #792 energy-Schur proof was inspected for
its energy-completion distinction. This is contextual reading, not a fresh
remote source lock or independent acceptance of that branch. In particular,
the new finite positive Gram is not silently identified with PR #792's
indefinite Weil-form reduction.

## Overlap and novelty boundary

A default-branch code search for “Nyman Beurling projection” returned no
matches; this is not exhaustive. A PR search for “Nyman” returned historical
PRs #204, #289, #297 and #333. Their descriptions were read. They already
record local-versus-global reconstruction, carry/Mellin criteria, and
critical-neutrality warnings. Their exact proof trees were not reaudited
here and are not premises of the present theorems.

Bounded web searches for the local projection/dilation and Schur connection
did not establish priority. One search also surfaced a 2026 secondary
listing of a finite Ramanujan-energy Schur framework; its full proof was not
audited or used. Schur complements, prediction identities and the
Nyman–Beurling approach are emphatically not claimed as new theories.
The possible project-specific contribution is the combined, explicitly
proved local observability/leakage/support packet. External novelty remains
unassessed.

## Authorship and publication

The author of this packet previously acted as Reviewer C. This research is
an **author submission**, not an independent Reviewer C acceptance. The
counterexamples and new component proofs require non-author mathematical
and code review.

The active GitHub tools supplied authenticated reads but no repository-write
action. Plugin discovery found only the already-installed GitHub plugin;
no authenticated CLI was available in the execution environment. No remote
branch, commit, PR, comment, workflow or settings change is claimed.
The application patch and proposed branch name are a handoff, not evidence
that publication occurred.
