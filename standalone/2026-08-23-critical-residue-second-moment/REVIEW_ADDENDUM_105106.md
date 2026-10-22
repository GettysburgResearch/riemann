# Review addendum — T-105106 primary-cardinal conditioning

Checkpoint base:

    0a7b83e596534a7b9633b1c59ea4fdb057551c05

Review the following files together:

- `claims/lemmas/L-105106-primary-cardinal-selector-conditioning.md`
- `claims/theorems/T-105106-weighted-selector-frontier.md`
- `claims/refutations/R-105106-selector-completeness-does-not-give-cofinal-control.md`
- `claims/methodology/M-105106-selector-conditioning-review-contract.md`
- `experiments/X-105106-primary-cardinal-conditioning/`

Load-bearing points:

1. the manifest uses actual post-cancellation pole orders;
2. top-primary data produce the closed cardinal formula;
3. \(M_c(c)\) normalization and full nontarget multiplicities are retained;
4. \(W/M\) is the stated simple target partial fraction;
5. the real-even cluster and Blaschke bounds block uniform or high-degree
   escape;
6. fixed-window envelopes are not presented as Xi asymptotics.

Replay:

    python -B experiments/X-105106-primary-cardinal-conditioning/tests/test_verify.py
    python -B -O experiments/X-105106-primary-cardinal-conditioning/tests/test_verify.py

Expected:

    PASS_T105106_PRIMARY_CARDINAL_CONDITIONING
    7dc8a3075e983d48032d74e14af2d3fed5611adb9735623e32a9dfa8623ace33

The Xi manifest, cofinal conditioning products, pole-cancelled holomorphic
factor estimates, weighted edges, RCMV104530, and RH remain open.
