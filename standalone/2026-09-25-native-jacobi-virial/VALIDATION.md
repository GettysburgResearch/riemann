# NJV34 validation record

## Successful local replay

The final standard-library checker ran in both modes, producing byte-identical receipts:

```sh
python -I -S -B check.py --output receipt.json
python -I -S -B -O check.py --check receipt.json --output replay_optimized.json
cmp receipt.json replay_optimized.json
```

The receipt records **106,893** predicates, including:

- 38,024 entries each for the finite native Green inverse and rank-one boundary, covering all cutoffs 1 through 48;
- native quadratic, discrete Poisson/Dirichlet, and centered reciprocal-variance identities on deterministic signed sources at those cutoffs;
- 140 complete rational Schur eliminations for cutoffs through 24, 1,699 positive elimination pivots, and six comparisons of prime-factor elimination order;
- 441 exact orthogonality pairs and 441 exact resolvent-Green moment pairs, all polynomial degrees 0 through 20, with the terminating hypergeometric coefficients generated separately;
- 432 exact dilation/rounding energy identities;
- Mobius authentication via mu*1=delta at all 4,095 positions and 9,514 prime-log coefficient checks of the logarithmic derivative identity;
- exact complete covariance/virial prime-log vectors at N=31,63,127,255,1023,4095, with independent direct-cell versus hyperbola checks at the three smaller cutoffs;
- memberwise character controls modulo 3 and 4 at N=255, including their vanishing values and prime-power weights;
- 256 native escape signed-count checks and 100 squarefree-weighted nonnegative controls.

The number of finite predicates is a replay scope, not a confidence score for RH.

## Exact arithmetic and enclosures

Acceptance uses only integers and fractions. Native weighted sums use D=lcm(1,...,N+1), and logarithmic identities are verified coefficientwise in prime logarithms before evaluating them. The orthogonal-polynomial tests use exact Euler-number moments, not numerical quadrature.

For displays, logarithms are bounded using the positive atanh series after reducing to a ratio in [1,2). Forty terms plus an explicit positive remainder are rounded outward at 96 dyadic bits; final displayed quantities are rounded outward at 40 bits. Signed coefficient multiplication chooses the correct interval endpoint. Floating point appears only in decimal display fields.

At N=4095, the resulting outward intervals are approximately:

```
E_N  in [ 1.5057536015419828,  1.5057536015428923]
V_N  in [ 3.1504466516180400,  3.1504466516189495]
Q_N  in [ 0.7262373922767438,  0.7262373922776533]
W_N  in [-2.4242092593422058, -2.4242092593412963]
```

The exact dyadic integer endpoints in receipt.json are authoritative. These values illustrate the signed balance; they are not an extrapolation to all N.

## Rejected shortcuts and tamper test

The checker rejects a deliberately corrupted primitive Mobius coefficient through independent Dirichlet inversion. It also verifies actual discrepancies when the native rank-one endpoint is omitted, the dilation rounding term is omitted, spectral normalization is changed, or prime powers beyond primes are omitted from the covariance. The prime-insertion example increases the native energy from 1/2 to 2/3, disproving unconditional primewise contraction.

A separate copy of the final receipt had the last native panel's Q upper numerator changed by one. A complete primitive replay rejected it with nonzero exit status and `receipt does not match primitive replay`. It was not committed. Checks do not use Python assert statements that optimized mode could disable.

## Not established or not run

No independent mathematical review, proof-assistant verification, repository-wide CI, or historical branch validation was run. Universal analytic statements use the written proofs and the explicitly imported classical continuous dual Hahn orthogonality. Finite moment checks alone do not prove that theorem.

No new asymptotic native E_N estimate, no identification with the full Newton/Weil covariance, no new zero-free region, and no proof of RH is claimed. The Fourier/Dirichlet comparison proved here is for the specified cumulative-sum metric, not an arithmetic trace formula for zeta.
