# Exact finite replay and proof boundary

Status: **PASS for the declared finite predicates.** Both ordinary and optimized
Python reproduced 10,364 explicit checks and byte-identical reports. The infinite
estimate is proved in `PROOF.md`; it is not inferred from this finite replay.

## Frozen identities for this replay

| File | SHA-256 |
| --- | --- |
| `PROOF.md` | `9f79dd54fb7e8ff26723c1bc8853c4a220d852b32c8b900c71ba9d9e15b6e6c1` |
| `check_amplitude.py` | `fa7d06cd7d3657761079f7bfe3b77099ba7be97086b09183520bd9f5b1071220` |
| `CHECKS.json` | `c1ae6f048bd895b84526a84004647061a02a54625492d744151b87a7c926a067` |
| `CHECKS_OPTIMIZED.json` | `c1ae6f048bd895b84526a84004647061a02a54625492d744151b87a7c926a067` |

## Primitive source and arithmetic

The old prefix is constructed by trial factorization and the defining
squarefree/parity rule for the Möbius function. The comparison array through
the first excluded Newton coefficient is independently produced by an Euler
sieve. The literal truncated product is built from **every ordered input pair**.
It is not reconstructed from a supplied convolution table or energy report.

All harmonic numbers, coefficients, Möbius values and period covariances use
integers and exact `fractions.Fraction` arithmetic. Integer logarithms are
represented by prime-exponent vectors and Euler's constant by a separate formal
symbol. Formal equality verifies the required identities using only exact log
product relations; no claim of transcendence or algebraic independence is
needed. Negative controls involving these symbols detect changed formal
expressions; they are not certified numerical lower bounds for a transcendental
difference.

The cutoff `floor(X^(5/8))` is computed by an exact integer eighth-root search
and checked between consecutive eighth powers. No floating rounding decision
enters the coverage.

Every acceptance predicate calls an explicit `require` function that raises
`ValueError` on failure. Optimization cannot disable these predicates. A stored
JSON report is output, not a premise of acceptance.

## Complete declared coverage

- Native strict Newton steps for `Y = 1, 2, 3, 4, 7, 10, 15`: all **446** output
  cells through `(Y+1)^2-1`, with no endpoint or annulus strip omitted. The
  separate first excluded coefficient is checked against its predicted defect
  `mu(Y+1)^2`.
- Both native balance identities, the full balanced formula, and the filtered
  reconstruction on every one of those cells. The check retains products above
  the output index and the original cofactor weights.
- Exact filtered means for **196** complete, deliberately unequal blocks,
  using both direct cell summation and the harmonic antiderivative formula.
- Complete primitive-wave periods through denominator 15, their zero means,
  all pairwise complete-period covariances and the Jordan-function norm identity.
  This uses rational Möbius inversion, separately from the proof's complex
  Fourier derivation.
- Reduced-fraction grouping and circular spacing through cutoff 8, including
  the zero frequency. Positive divisor, alternating divisor and native product
  fixtures cover **4,203** complete-period cells. Their source-stream hash is
  `fae8bb2ed44e376b8b7cb8eb23302b81c6cf5e941429d0d81fe16fbbc245ba58`.
- Source-tuple inclusion for every declared small native case, plus a separate
  `Y=512` top-annulus inclusion check. There `X=262656`, `D=2438`, and every
  ordered pair with minimum index at most 4 is included: **4,080** pairs. This
  last fixture authenticates tuple coverage only; it is not a large energy
  computation.

There are 27 explicit negative-control predicates, covering loss of the zero
frequency, substitution of the wrong cofactor weight, deletion of the balances
or above-output products, and an attempted extension to the first erroneous
Newton endpoint. Endpoint defects that vanish for a particular nonsquarefree
`Y+1` are allowed; the global control includes nonzero endpoint fixtures.

## Commands actually run

From the directory containing these files:

```bash
python3 check_amplitude.py --output CHECKS.json
python3 -O check_amplitude.py --output CHECKS_OPTIMIZED.json
```

Both commands exited successfully. A separate byte comparison confirmed the
two report files are identical. The proof's source hash is included in both
reports. Standard Python is sufficient; no symbolic or numeric third-party
package is required.

## What this establishes and what it does not

The replay checks primitive-source algebra, exact integer-cell normalization,
finite period covariance and complete declared coverage. It independently
constructs the Möbius comparison source and uses a rational method for the
period decomposition, but it is one finite checker, not a formal proof assistant
or a second transcendental implementation.

It does not prove the harmonic asymptotic, the all-scale frequency estimate,
or the geometric summation by testing. Those have written proofs. It does not
bound the remaining high-product amplitude, prove the coarse-energy recurrence,
establish RH, reproduce remote CI, or approve unrelated repository claims.
