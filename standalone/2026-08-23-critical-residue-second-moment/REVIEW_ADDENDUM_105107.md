# Review addendum — T-105107 boundary-optimal selectors

Checkpoint base:

    7e1cb178cd11202ed1e5877c898d1c2877d22521

Review together:

- claims/lemmas/L-105107-blaschke-pick-optimal-jet-selectors.md
- claims/theorems/T-105107-boundary-optimal-jet-observable-frontier.md
- claims/refutations/R-105107-reduced-polynomial-selector-need-not-be-boundary-optimal.md
- claims/methodology/M-105107-hinfinity-selector-review-contract.md
- experiments/X-105107-blaschke-pick-jet-selectors/

Load-bearing checks:

1. nontarget exponent \(d_a\), target exponent \(d_c-1\);
2. self derivative and all other forced Blaschke factors in \(\beta_c\);
3. full Pick PSD, not diagonal or another Xi kernel;
4. constant-modulus extremal and exact residue preservation;
5. Jordan continuity versus analytic boundary extension;
6. reflected poles checked per window;
7. all Xi/cofinal estimates left open.

Replay:

    python -B experiments/X-105107-blaschke-pick-jet-selectors/tests/test_verify.py
    python -B -O experiments/X-105107-blaschke-pick-jet-selectors/tests/test_verify.py

Expected:

    PASS_T105107_BLASCHKE_PICK_JET_SELECTORS
    82747e320365a97bf9824dd84960f00bbcb77cd738040c2c5214be844dfc738c

The Xi manifest, conformal data, cofinal Pick norm, quotient edge estimates,
RCMV104530, and RH remain open.
