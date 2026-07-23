# Agent report — xi passivity adversarial scan

Agent: `gpt56-02-e`  
Issue: #39, independent parallel attempt  
Branch: `agent/gpt56-02-e/39-xi-passivity-adversarial-scan`  
Date: 2026-07-23  
Status: no counterexample; one new fixed-vector lemma and several refuted anomalies

## Starting hypothesis

The optimized finite-Weil carrier basin from PR #44, whose leading margin had
fallen to about `+2.69e-4`, might be the spectral shadow of an off-critical zero.
If so, the independent xi-passivity route should exhibit a scalar, differential,
Pick, or shifted-Stieltjes failure near the same ordinate.

## Approaches attempted

1. Extended the simultaneous Riemann--Siegel assembly to zeta derivatives
   through order four.
2. Evaluated `Re F`, the L-4101 differential localizer, and `2 x 2` L-4102
   matrices at the carrier center.
3. Widened the no-remainder curvature screen to `T0 +/- 100`.
4. Escalated every negative screen with simultaneous exact-point jets.
5. Replaced sampled-Pick eigenvectors by exact barycentric fixed vectors.
6. Derived a resolvent-product identity and an explicit linear error
   amplification bound.

## New exact result

L-3901 proves that the barycentric vector on distinct horizontal offsets gives

```text
c* K c = sum_gamma 1/product_i(x_i^2+(T-gamma)^2) >= 0
```

under RH. For a same-ordinate off-line symmetric pair, its contribution is

```text
2/product_i(x_i^2-delta^2).
```

Thus two dyadic offsets bracketing the hidden horizontal displacement form an
existentially complete two-point witness family. The final quantity is a fixed
rational linear combination of `Re F` values, with an exact amplification
budget.

## Refuted anomalies

### No-remainder curvature

Two negative curvature midpoints were found. Both occurred at small approximate
Hardy values and both became strongly positive under simultaneous zeta jets.
This isolates a concrete omitted-remainder failure mode.

### Shifted-Stieltjes cancellation

At `x=1e-4`, 24-digit arithmetic manufactured large negative `2 x 2` moment
matrix eigenvalues. At 36 digits, both were positive near `8.406268`. The
finite-jet formula divides cancellation residuals by powers through `x^-7`.

### Pick near-rank sign

An eight-point Pick matrix initially showed a smallest eigenvalue around
`-8.7e-13`. Increasing precision moved it successively through
`-5.2e-18`, `-3.3e-26`, `-9.5e-35`, then to a stable positive value near
`+4.726708e-42`.

The exact integer barycentric vector followed the same pattern and stabilized
at a positive normalized Rayleigh value near `+1.315115824e-38`.

## Candidate counterexamples

None. No directed negative interval exists and no `Z-####` identifier is
allocated.

## Files changed

- `claims/lemmas/L-3901-barycentric-pick-product-localizer.md`;
- `claims/methodology/M-3901-passivity-precision-ladder.md`;
- `claims/observations/O-3901-carrier-basin-passivity-audit.md`;
- `experiments/X-3901-xi-passivity-adversarial/`;
- this report.

## Verification performed

Eight tests pass. They include exact critical-line product identities, exact
off-line bracket signs, the primitive integer vector, fourth-order
Riemann--Siegel zeta-jet comparison against independent `mp.diff`, and the
identity `B00=D/2`.

## Recommended next actions

1. Implement L-3901 two-point brackets with Arb and exact dyadic offsets.
2. Use the scalar-left/differential-right pair as a mandatory anomaly signature.
3. Derive the exact PR #44 archimedean and pole corrections before another
   billion-prime continuation.
4. For every higher-order Pick or moment search, publish the fixed vector and
   amplification factor before reporting its midpoint sign.

## Organizational improvement

Passivity searches should maintain a machine-readable refutation ledger. A
negative screen that vanishes under a declared precision ladder is useful
project knowledge and should not be rediscovered by another agent.
