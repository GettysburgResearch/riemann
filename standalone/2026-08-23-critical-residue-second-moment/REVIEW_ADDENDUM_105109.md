# Review addendum — L/T/R/M-105109 quotient-edge margins

Checkpoint base:
`e223f98823bdb7b11736a05993ac12b75d5263b3`.

## What changed

The unweighted edge factor is now expressed through exact lower margins for
\(F'/F\) and \(F''/F\).  Constant boundary modulus makes the optimally
weighted supremum equal to \(\tau\) times the raw quotient supremum.

The family \(F_s=\exp(z^2/2-z^4/(4s))\) has fixed target coefficients,
stable interior event topology, and bounded selector norms, yet both
weighted boundary suprema diverge as exterior critical points approach the
unit circle.

## Hostile checks

- Verify \(F''/F=\mathscr L^2+\mathscr L'\) and both quotient identities.
- Verify the second exact margin is \(\inf|\mathscr L\mathscr A|\).
- Verify the cubic has one simple root in each stated interval.
- Verify \(\beta_0=-\alpha\), \(W_2(0)=1\), and
  \(\tau_2=1/\alpha\).
- Verify the target principal coefficients both equal one.
- Verify the rational \(s=101/100\) signs and boundary values.
- Verify the full contour integrals stay one; only supremum envelopes
  diverge.
- Verify the moving second support and order-four/non-Xi scope are explicit.

Exact replay:

    python -B experiments/X-105109-log-derivative-edge-obstruction/tests/test_verify.py
    python -B -O experiments/X-105109-log-derivative-edge-obstruction/tests/test_verify.py

Expected:

    PASS_T105109_LOG_DERIVATIVE_EDGE_OBSTRUCTION
    17/17 normal / 17/17 optimized
    54829e77cb2aa90192aabdd61f86ff045a04ba3549f82c75384bc9a4e08f2890

Xi collar/lower-margin estimates, phase-sensitive cancellation, cofinal
Green–Gram control, strict coherence, RCMV104530, and RH remain open.
