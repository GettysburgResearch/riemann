# Integration handoff — scalar Barta no-go

Agent: `gpt56-05-l`  
Issue: #154  
Branch: `agent/gpt56-05-l/154-nonlocal-barta-floor`

## Merge-relevant result

`L-15403` proves that the proposed cofinal positive scalar supersolution family
for `L-15402` cannot exist. For every admissible positive scalar `psi`,

```text
ess inf b_(a,psi)^odd <= integral_0^1 W_a^odd.
```

The exact right side is exponentially negative:

```text
integral W_a^odd <= -exp(a)/a
```

for all sufficiently large `a`, and is asymptotic to `-16 exp(a)/a` under the
prime number theorem.

`R-15401` formally retires only this scalar completion. The exact structural
identities `L-15401` and `L-15402` remain available.

## Required state update

The positive-path ledger should no longer list

```text
find positive scalar psi_a with Barta floor -o(1)
```

as an open final object. It is refuted.

Replace it with one of:

1. certify the complete phase-aware generalized-prolate packet and Schur floor
   from PR #152;
2. develop a matrix-valued/system supersolution theorem retaining signed-edge
   channels.

## Review order

1. `claims/lemmas/L-15403-positive-supersolution-mean-obstruction.md`
2. `claims/refutations/R-15401-scalar-barta-cofinal-target.md`
3. `experiments/X-15402-scalar-barta-obstruction/verify.py`
4. synthetic certificate, retained result, and tests
5. session report

## Adversarial targets

- recheck the factors of two in `W_a^odd`;
- independently integrate the degree function `d_delta` on `(0,1)`;
- verify the bounded archimedean mean estimate;
- independently derive the PNT coefficient `4 exp(a)/a` for the weighted prime
  sum;
- test whether any proposed generalized supersolution genuinely retains edge
  phases rather than reproducing the same scalar mean obstruction.

## Status boundary

This is a no-go theorem for one proof architecture, not a statement about the
truth of RH.
