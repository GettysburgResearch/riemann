# Execution and trust boundary

The standalone verifier reconstructs finite arithmetic and Laurent-series fixtures. It does not numerically integrate a contour, prove a uniform analytic bound, or establish OPEN.

The only accepting numerical transcendental calculation is the small native expression at m=2. Logarithms use positive rational atanh series after binary range reduction, with 80 terms and an explicit geometric remainder. Final endpoints are rounded outward to denominator 2^112. No floating-point library, zeta/gamma/zero oracle, optimizer, or numerical quadrature is imported.

The finite source ranges are: Mobius sieve versus independent trial factorization through 256; nine Y values 2,...,10 and three rational variations each; full convolution identities including the first omitted coefficient through 2Y^2<=200; complete small annular coefficient sums for Y=4,...,10. Formal prime logarithms are retained symbolically. The native sign itself uses all prime powers through 16.

The 534 fixtures are in 16 named groups; 256 are sieve-versus-factorization comparisons. They are not 534 theorem proofs. The Laurent fixtures reconstruct products and derivatives before reading residues; the comparison polynomial is not used as its own producer.

An initial local run failed because integer Mobius entries were not explicitly converted to Fraction before Python division in one normalization fixture. That unintended floating division was removed, and the completed runs use Fraction entries. The failed preliminary run is not counted as a successful execution or as mathematical evidence against the theorem.

Replays and mutation/roundtrip receipts are recorded in the delivery archive. They are author executions, not independent mathematical acceptance. No formal build, remote CI, predecessor-wide audit, newly verified zeros, or large arithmetic campaign is claimed.

## Completed executions

- `python -I -S -B verify.py --check result.json` and the same command with `-O` pass with identical reconstructed output. Result SHA-256: `1405dfceb2e65e447294cd872b8cfb35e8d110a384b84176e190e98dc99d3234`.
- Eight actual CLI corruptions reject with code 2 in each interpreter mode, after a pristine copied packet passes: false RH status, false native bound, floating count alias, duplicate JSON key, wrong parent head, changed native interval, changed proof and an extra file. The semantic result/source mutations are rehashed to test reconstruction beyond the manifest. Sixteen completed refusal subprocesses are recorded, not inferred from exception checks alone.
- The unchanged BMC parent verifier was separately replayed in normal and optimized isolated Python: both reconstructed its 1,055-control result identically. This is a replay of that finite suite, not independent review of its infinite analytic proofs. The sparse-sign parent suite was not replayed.
- A temporary minimal-context Git repository supplies the two exact parent manuscripts and an unrelated sentinel. The add-only patch recreates all eight new files byte for byte, preserves the sentinel, and replays both modes. It is not a complete repository checkout or CI run. Delivery receipts record the resulting subtree hash.

All seven manifest entries and the exact eight-file inventory are authenticated. No parent Python is imported by the new checker. The source-constant and arithmetic fixtures use standard-library integers and Fractions only. The general uniform bounds and the conditional endpoint are paper arguments, not consequences of the finite fixture count.
