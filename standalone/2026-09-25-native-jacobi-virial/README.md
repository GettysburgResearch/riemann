# NJV34 — Native Jacobi renormalization and logarithmic covariance

**Proposed; independent mathematical review required. No RH proof or native asymptotic improvement.**

This is pass 2 of PR #907, following the unchanged RAB33 packet at commit `12433ee0056756da006788a8b82e492aac9e6d1d`.

Start with **PROOF.md**. Its principal components are an exact native Green/Jacobi comparison, centered reciprocal variance, arithmetic Schur renormalization with one terminal correction, an explicit classical continuous dual Hahn transform, and a tail-free Mellin comparison.

The source-specific quantitative result is

```
0 <= W_N + V_N = Q_N <= 2 E_N
```

for every cutoff N. Here W_N is the fully specified von Mangoldt-weighted dilation covariance, V_N the native logarithmic moment, and Q_N an explicitly positive Volterra-resolvent energy. This controls a complete weighted target; it does not control arbitrary weights, the complete Newton covariance, or E_N itself.

The Hardy/Jacobi kernel and orthogonal polynomials are known classical structures. The packet attributes them and proves the source/boundary adapters rather than claiming their invention.

## Replay

Python 3.10 or newer, standard library only:

```sh
sha256sum -c SHA256SUMS
python -I -S -B check.py --check receipt.json
python -I -S -B -O check.py --check receipt.json
```

The default run executes 106,893 finite predicates. It authenticates Mobius coefficients through 4095, checks every pair of spectral degrees through 20 with exact moments, performs rational Schur elimination, checks exact prime-log coefficient identities at six native cutoffs, and repeats the identity for real characters modulo 3 and 4.

`--limit` supports 1023 through 16383. A different limit produces a different receipt; do not compare it to the stored default receipt.

No floating-point value decides acceptance. Decimal fields are displays of outward dyadic intervals. Analytic Plancherel and imported orthogonality remain written mathematical inputs, not proof-assistant certificates. See VALIDATION.md for precise scope and controls.
