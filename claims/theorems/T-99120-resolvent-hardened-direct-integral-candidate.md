# T-99120 — Resolvent-hardened direct-integral score-free Hall candidate

Claim ID: `T-99120`  
Status: **PROPOSED APPLICATION HARDENING — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Base: PR #620 at `493e12fcba3f9b98dda7c3595bff73b256e00ca4`  
RH status: **unproved**

## Result

Assume the local compact Hall, component-profile monotonicity, residual-only
causal identity, positive endpoint measure, finite/continuum discrepancy and
all-column estimates stated in `L-99020`--`L-99023` survive independent
reconstruction.

Then `L-99120` applies to the complete labelled source tree. The all-depth ideal
physical row is the exact nilpotent resolvent

\[
D_X^{\rm ideal}
=J_X(I-T_X)^{-1}s_X
=E_X^{\rm eq}.
\]

Consequently the complete physical score is inherited directly from the
endpoint equality row:

\[
\mathcal H(D_X^{\rm ideal})=4\sqrt X.
\]

One common omission and one common thinning give

\[
\mathcal H(d_X)
\ge4\sqrt X-C
\]

for an absolute constant, while preserving every ordinary and radix-four
capacity on the same row. The elementary parabolic comparison of `L-99025`
then gives

\[
J_\Lambda(X)-\mathcal H(d_X)=O(\log X),
\]

and the frozen prime-power/Mellin–Landau consumer supplies the same proposed RH
conclusion as PR #620.

## What is new

The conclusion-producing chain no longer uses the sourcewise score telescope
of `L-99024`. It uses the exact physical-row resolvent instead. This removes:

```text
one declared-score/source interface;
one per-generation debt interpretation;
one convergence argument;
all generation-specific cubature or quantization choices.
```

## Exact scientific boundary

```text
nilpotent two-sort row resolvent             PROVED EXACT
score/capacity/provenance commutation         PROVED EXACT
all-depth score interface of PR #620          REPLACED CLEANLY
local compact Hall/direct-integral inputs     NOT REPROVED HERE
all-column finite discrepancy input           NOT REPROVED HERE
endpoint consumer                             RETAINED FROM PR #620
Riemann Hypothesis                            UNPROVEN
```

This is a substantive hardening of a candidate, not an accepted proof of RH.
