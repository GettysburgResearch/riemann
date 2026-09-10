# Actual-source stability and the cost of an approximate inverse

**PROPOSED COMPONENT THEOREMS. RH and the growing-horizon corrected-error
bound remain unproved. This is not a complete proposed RH proof.**

Read PROOF.md Sections 1--3 for the source-specific Gram floor, Section 5 for
the inverse-cost theorem, and Sections 6--8 for the attempted completion and
its exact failure. REVIEW.md is the independent-review handoff.

For the unchanged factorial source and all-pass orbit from PR #812, every
finite Gram of size n satisfies

    lambda_min >= 2^[-3-2(23+6ell)(79+16ell)],
    ell=ceil(log2(n+1)).

The inverse norm is therefore exp(O(log^2 n)), improving the parent's
exp(O(sqrt n)) envelope asymptotically. The new constants are very conservative;
the older bound is better at currently small ranks. Use the larger floor.
The proof uses actual zeta analytic continuation, local Jensen counts and
minimum modulus away from a small exceptional set. It allows off-line zeros;
it does not prove outerness or RH.

Full source truncation can correspondingly use logarithmic time O(log^2 n),
with explicit constants, while retaining every filtered tail. This controls
finite conditioning and coefficient sensitivity, not target capture.

For any boundary zero of multiplicity m and nonvanishing target value, a
causal approximate inverse achieving error epsilon must have input norm
at least c epsilon^[-(2m-1)]. Applied to the literal source, classical
critical-line zero existence makes this an unconditional restriction.
The exponent is sharp for explicit rational stable source models. No exact
L2 input gives the target; closure and actual range must stay distinct.

No new actual-source energy run, zero census or broad campaign was performed.
The previously certified 300-fold small-horizon improvement is not rerun or
strengthened by this packet. There is no uniform-in-horizon approximation rate.

## Replay

From a repository checkout, with the source-locked parent's PROOF.md present:

    python -I -B standalone/2026-09-07-astra-source-stability/check.py
    python -I -B -O standalone/2026-09-07-astra-source-stability/check.py
    python -I -B standalone/2026-09-07-astra-source-stability/test_check.py
    python -I -B -O standalone/2026-09-07-astra-source-stability/test_check.py

The delivery ZIP includes the unchanged parent proof at its expected path.
No parent Python is imported or executed. The --reconstruct mode only emits
rebuilt bounded data; it is not the authenticated acceptance mode.

The 1,994 bounded controls are primarily elementary constant checks through
n=256, sixteen synthetic Gram sizes and nine rational inverse models. They
are not 1,994 independently verified analytic theorems. The complete analytic
arguments still require independent review.
