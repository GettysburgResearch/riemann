# HBR29 execution and evidence limits

## Completed author executions

The interrupted derivation was restored into the active runtime and the finite
checker and diagnostic implementation were reconstructed from the retained work.
The final packet was freshly executed; old-session numerical outputs are not
silently counted as current runs.

Normal and optimized isolated Python each reconstruct **1,605** bounded rational
controls, accept one pristine copied CLI, and refuse **eight actual altered-copy
CLI processes**. Both modes regenerate the same result bytes:

    97cc8b500f6674c31c1e3c323f4fe2039cdc2b8e836892c6ec9d6d39b2a0a338

Commands (from this directory):

```sh
python -I -S -B check.py --check result.json --self-test
python -I -S -B -O check.py --check result.json --self-test
```

The exact groups are:

```
{
  "cutoff_density_algebra": 40,
  "exact_mean_difference": 14,
  "explicit_gamma_window": 1,
  "generating_function_ode": 20,
  "global_envelope_constants": 226,
  "jacobi_determinants": 55,
  "jacobi_even_origin": 6,
  "mellin_normalization": 160,
  "native_delay_coefficients": 252,
  "pareto_coefficients": 252,
  "phase_conjugation_sign": 24,
  "pollaczek_polynomial_identity": 20,
  "quantile_coth_bound": 40,
  "shift_coefficient_positivity": 210,
  "source_coefficients": 19,
  "survival_derivative_coefficients": 252,
  "survival_origin_density": 14
}
```

No `assert` implements acceptance. Strict parsing rejects duplicate keys,
float/Boolean aliases, and nonfinite JSON constants. The eight CLI corruptions
are false RH status, a wrong check count, a wrong shift polynomial, a Boolean
count, a floating count, a duplicate key, a false analytic budget, and a resealed
native delayed primitive changed from 4 to 3. The last case passes a freshly
resealed checksum inventory and fails independent moment/delay reconstruction.
Normal and optimized runs are the SAME implementation and author, not independent
mathematical acceptance. The hash inventory is not a digital signature and does
not purport to defeat arbitrary replacement of all code and manifests.

## Floating exploration, explicitly outside mathematical acceptance

The coarse and fine diagnostic commands each completed four modes
(c=31,127,511,2047) and 36 complex panels. Fine-grid cutoff CDF values at 2ell are

```
{
  "127": 0.37531121094823194,
  "2047": 0.3683294396719218,
  "31": 0.401012729792321,
  "511": 0.3696906706913646
}
```

The largest complex coarse/fine discrepancy across comparison, native and sharp
correction values is approximately 8.045673e-13. This is a numerical comparison,
NOT a rigorous error radius or extra significant digits of a theorem.

The code uses method-of-steps DOP853 integration and composite Gaussian quadrature.
It initializes the origin using only its leading Taylor term, truncates the r
integral at 2ell+40, and attaches no interval bounds to ODE, interpolation,
quadrature or omitted tails. At c=2047 the binary64 epsilon underflows to zero;
that replacement is disclosed and its error is NOT propagated in this scout.
All analytic full-tail proofs are in PROOF.md, not established by these runs.
The diagnostic JSON is bound by the inventory but is not a premise of any exact
mathematical test.

## Restoration and development disclosures

The previous attempt's HBR29 work directory did not survive into the active
runtime; HBR28 and the other uploaded artifacts did. HBR29 was restored from the
retained derivation and rerun. This is not a claim of byte identity with an
unavailable earlier HBR29 payload. The parent HBR28 proof was authenticated to
its exact Git blob.

The final source uses a uniquely newline-delimited DELAY_DEN mutation target,
not an ambiguous substring matching the mutation-test code itself. Bytecode
writing is disabled so that the strict regular-file inventory remains intact.
Two textual boundaries were made explicit: the gamma modulus product uses a
non-strict inequality at t=0, and any possible descent must preserve exclusion
of off-critical zeros rather than preserve total zero-freedom down to G_1.

## Delivery and publication scope

The outer delivery gate reruns both final sealed modes, applies the add-only patch
to a minimal Git fixture, compares every new file byte-for-byte, preserves a
frozen predecessor proof and an unrelated sentinel, and reruns both modes there.
A clean archive extraction also replays both modes. Actual commands and object
identities are recorded outside the sealed packet in the delivery receipts.
These fixtures are NOT full Riemann checkouts. The final archive receipt binds
the archive separately and does not pretend to be a remote commit.

No new PR or commit was pushed by this author session. No parent certificate
campaign, actual Xi zero evaluation, complete repository validator, Lean build,
remote CI, independent referee acceptance, or unbounded phase sign was executed.
The source and convergence arguments are proposed paper proofs requiring review.
