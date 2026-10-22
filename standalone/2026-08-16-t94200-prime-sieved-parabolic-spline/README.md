# T-94200 prime-sieved parabolic-spline publication

This directory is the durable publication front door for draft PR #537.

```text
repository: gfreund123/riemann
branch:     research/gpt56-pro/94200-prime-sieved-parabolic-spline
base:       main@9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
status:     proposed complete unconditional RH candidate
RH status:  not treated as established before independent reconstruction
```

## Proof-bearing files

- `claims/lemmas/L-94200-initial-prime-euler-sieving-preserves-parabolic-row-positivity.md`
- `claims/lemmas/L-94201-full-native-mobius-component-row-is-nonnegative.md`
- `claims/lemmas/L-94202-positive-full-row-saturates-native-capacity-with-zero-deficit.md`
- `claims/theorems/T-94200-prime-sieved-parabolic-spline-rh-closure.md`
- `claims/refutations/R-94200-noninteger-shifts-are-not-the-prime-sieve-proof.md`

## Review boundary

The smallest load-bearing claim is the `FRONTIER-CHAIN` divisor-cube decomposition and reservoir-capacity argument in `L-94200`. A failure there retracts the proposed RH composition while leaving the exact native normalization and endpoint consumer as separate prior mathematics.

## Deterministic packet

`.github/workflows/t94200-deterministic-packet.yml` builds a fixed-timestamp ZIP containing the proof-bearing files, metadata, and SHA-256 manifests. The resulting artifact is mirrored to Google Drive as an independent download path.
