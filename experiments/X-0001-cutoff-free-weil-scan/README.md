# X-0001 — Cutoff-free finite Weil scan

Experiment ID: X-0001  
Issue: #1  
Agent: `gpt56-01`  
Branch: `agent/gpt56-01/1-weil-positivity-search`  
Status: EMPIRICAL; certificate checker exact, matrix search not certified  
Created: 2026-07-22

## Research question

Does the exact cutoff-free finite Weil matrix `Q_N(c)` exhibit a reproducible
negative quadratic direction at any scanned real cutoff `c` and finite band
`N`, and can such a direction be packaged for a small exact verifier?

A strict certified negative would activate L-0001.  An ordinary negative from
this script would only be a lead.

## Why cutoff-free

A finite archimedean integration cutoff can create deep negative eigenvalues
that disappear after the omitted positive tail is restored.  This experiment
therefore evaluates closed forms for the entrywise `T -> infinity` matrix.  It
never treats a finite-T eigenvalue as the target object.

## Files

- `run.py` — independent mpmath construction, precision ladder, residuals,
  empirical inertia, and JSON output.
- `verify_dyadic_certificate.py` — standard-library exact rational checker for
  a dyadic interval matrix and dyadic vector.
- `test_run.py` — implementation and invariant tests.
- `test_certificate.py` — exact interval-propagation tests.
- `requirements.txt` — pinned discovery dependency and test runner.
- `results/scan-metadata.json` — parameter grids, environments, aggregate counts, and SHA-256 digests of the uncommitted raw outputs.
- `results/README.md` — result-retention policy.
- `results/synthetic-negative-certificate.json` — explicitly synthetic test of
  the exact checker; it is not a Weil matrix and not a counterexample.
- `results/SHA256SUMS` — digests for committed result artifacts.

## Mathematical assembly

The implementation uses the cutoff-free closed forms traced in D-0001 and
`LITERATURE.md`.  In full indices `m,n in {-N,...,N}`, it assembles

\[
 Q_N(c)=W_{0,2}-W_{\mathbb R}-W_p
\]

in the closed-form convention of the source implementation.  The pole block is

\[
 (W_{0,2})_{mn}=
 \frac{32L\sinh^2(L/4)(L^2-16\pi^2mn)}
 {(L^2+16\pi^2m^2)(L^2+16\pi^2n^2)}.
\]

The archimedean entries use digamma/trigamma closed forms plus exponentially
convergent geometric corrections.  `run.py` records conservative analytic
bounds for omitted geometric tails, but mpmath does not use directed rounding;
those bounds are diagnostics, not a proof enclosure.  The prime block is the
finite sum over prime powers `q<=c`.

The matrix is projected to the even sector with

\[
 u_0=v_0,\qquad u_{\pm k}=v_k/\sqrt2.
\]

## Reproduce

From the repository root:

```bash
python -m pip install -r experiments/X-0001-cutoff-free-weil-scan/requirements.txt
pytest -q \
  experiments/X-0001-cutoff-free-weil-scan/test_run.py \
  experiments/X-0001-cutoff-free-weil-scan/test_certificate.py
```

Baseline scan:

```bash
python experiments/X-0001-cutoff-free-weil-scan/run.py \
  --cutoffs 2 3 5 7 11 13 \
  --bands 2 4 6 8 \
  --dps 60 --guard-dps 90 \
  --output experiments/X-0001-cutoff-free-weil-scan/results/baseline.json
```

Extended integer scan:

```bash
python experiments/X-0001-cutoff-free-weil-scan/run.py \
  --cutoffs 17 19 23 29 31 37 41 43 47 53 59 61 67 100 \
  --bands 4 8 12 \
  --dps 90 --guard-dps 130 \
  --output experiments/X-0001-cutoff-free-weil-scan/results/extended.json
```

The off-integer grid is listed verbatim under the `log-grid` entry in
`results/scan-metadata.json`; rerun by passing its `parameters.cutoffs` array to
`--cutoffs`, with `--bands 8 --dps 70 --guard-dps 100`.

Exact synthetic checker test:

```bash
python experiments/X-0001-cutoff-free-weil-scan/verify_dyadic_certificate.py \
  experiments/X-0001-cutoff-free-weil-scan/results/synthetic-negative-certificate.json
```

## Results

| Scan | Cells | Empirical negative | Sign-unstable under guard precision |
|---|---:|---:|---:|
| baseline | 24 | 0 | 0 |
| extended integer | 42 | 0 | 0 |
| off-integer log grid | 16 | 0 | 0 |
| **total** | **82** | **0** | **0** |

The `c=13,N=8` full matrix had empirical inertia `(17 positive, 0 negative)` at
both 60 and 90 decimal digits.  The guard smallest even eigenvalue was about
`7.67439255636e-23`, with infinity-norm eigenpair residual below `7e-92`.
This agrees qualitatively with the released cutoff-free positive-inertia
self-test, but is not an independent interval proof.

No candidate ID is created.

## Exact dyadic certificate layer

The checker consumes a schema named
`riemann.weil-rayleigh-dyadic.v1`.  Every upper-triangular matrix entry is a
dyadic interval, and the vector has dyadic coordinates.  Using only exact
fractions, it encloses

\[
 v^{\mathsf T}Qv
 =\sum_i v_i^2Q_{ii}+2\sum_{i<j}v_iv_jQ_{ij}.
\]

It exits successfully only when the exact upper endpoint is strictly negative.
The checker deliberately does not know zeta functions, digamma functions, or
floating point.

A full certificate still needs an independently audited generator proving that
each dyadic interval encloses the correct D-0001 entry.  That is Q-0001.

## Adversarial tests

The test suite checks:

- exact prime-power enumeration;
- contraction of analytic geometric-tail bounds;
- matrix symmetry and parity;
- even-projector orthonormality;
- high-precision eigenpair residuals;
- input rejection, including accidental binary-float cutoffs;
- exact interval endpoint reversal for negative coefficients;
- rejection when a Rayleigh interval touches zero;
- rejection of incomplete matrices and the zero vector.

## Failed or limited attempts

A 31-point off-integer grid at bands `N=8,12` and 90/130 decimal digits exceeded
the initial execution budget before completion.  No result was emitted and no
mathematical conclusion was drawn.  The smaller grid finished.  This exposes a
need for continuation, low-rank updates, and cheaper screening before precision
escalation.

## Limitations

1. mpmath arithmetic is not directed-rounding interval arithmetic.
2. The implementation transcribes recent closed forms and needs an independent
   analytic derivation.
3. The scans are tiny relative to the unrestricted `(c,N)` space.
4. Only the even sector is optimized in the current discovery output.
5. Absence of a negative in these cells says nothing universal.
6. Small eigenvalues can require far more precision at larger `N`.
7. The exact checker verifies algebraic interval propagation, not provenance of
   the entry intervals.

## Primary references

See `LITERATURE.md`.  The most directly used source is the July 2026 finite
Guinand--Weil dictionary and its released `arb_ldlt_certify.py` implementation.
The experiment is intentionally labeled empirical until a separate Arb route
is implemented and reviewed.
