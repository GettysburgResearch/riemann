# Exact finite execution and what it rules out

All accepting arithmetic is integer or Fraction arithmetic. A preliminary
floating-point scout was used to choose diagnostics; it has no accepting
role. `result.json` is regenerated entirely without NumPy, quadrature,
randomness, or any stored numerical source coefficients.

## 1. Two independent source constructions

The producer computes `e=delta-1*g` from mu through Y, separates e by its
least prime, and convolves each residual channel with g. It then discards
exactly zero coalesced coefficients. It does not set nonnative or nonsquarefree
coefficients to zero by fiat.

The checker independently trial-factors every output integer. It computes
mu by squarefreeness and parity, finds the unique descending-prime suffix
that crosses Y, and builds the resulting disjoint channel rows. It matches
every row digest and event count before validating the energy table.

The two algorithms agree on Y=3,7,15,31,63,255. A separate regression checks
every Y from 1 through 24, including non-square-ladder cutoffs.

## 2. Exact energy rather than a sparse observation grid

The producer integrates constant steps on complete event intervals:

```text
integral_[s,t) V_i V_j dx/x^2 = V_i V_j (1/s - 1/t).
```

It rounds each signed rational contribution outwards to denominator 2^80.
The checker uses a different identity:

```text
integral V_i V_j dx/x^2
  = sum_n Delta(V_i V_j)(n) (1/n - 1/b^2).
```

The simultaneous-jump term is retained. It constructs 160-bit enclosures
and requires them to be CONTAINED in the reported 80-bit interval, not
merely overlap. A Fraction fallback treats degenerate intervals exactly.
The total E, u, A and F are separately checked by direct weighted sums of
the independently factored complete Mertens prefix.

## 3. Results (display values rounded; JSON is authoritative)

| Y | Declared rows | Annular I | Raw pivot D | Ordered C=I-D |
|---:|---:|---:|---:|---:|
| 3 | 4 | 0.516271228771 | 0.657937895438 | -0.141666666667 |
| 7 | 6 | 0.455360288806 | 1.418242578700 | -0.962882289893 |
| 15 | 8 | 0.307965014621 | 1.150734277937 | -0.842769263316 |
| 31 | 13 | 0.217214998590 | 2.798129990821 | -2.580914992231 |
| 63 | 20 | 0.188488550832 | 3.420388793557 | -3.231900242725 |
| 255 | 56 | 0.179852003503 | 14.492272686482 | -14.312420682979 |

Rows include the constant prefix, every prime <=Y, and one aggregate for
p>Y. Empty rows are retained. Aggregating the last group changes its
diagonal compared with a fully singleton-prime partition; the theorem's
positive sector uses distinct primes <=Y and is unaffected.

At Y=255, the positive ordered cross mass is approximately
29.813487280772 and the negative ordered cross mass -44.125907963751.
Some largest negative pairs involve the p>Y group and pivots 19,23,29,31.
The largest positive pair here is (11,13), about 0.635034780066 after
counting both orders. These observations motivate retaining cross-sector
signs; they are not a theorem that a particular pair dominates at all scales.

The completed A state changes from approximately 1.444181751809 to
1.587579815076. Annular I alone is not that update.

The existing NSR26 prime-bank regrouping at the same Y has a much smaller
separated diagonal (about 0.2192 for bank 210). This pass's raw pivot
diagonal is not an improvement. We retain and explain that negative
result rather than selecting an attractive metric.

## 4. Native, rather than synthetic, obstruction

For Y=255 the rectangle in PROOF.md has

```text
P = {193,197,199},     Q = {211,223,227,229}.
```

The exact lower bounds are

```text
diagonal sector:             16/65025
ordered cross sector:        32/65025
coprime ordered cross:        8/21675.
```

These deliberately weak finite bounds certify the rectangle argument.
The power-size asymptotic follows analytically from the prime number
theorem, not from fitting this small table.

## 5. Failing controls and adversarial checks

A multiplicative squarefree-supported sign twist of mu, obtained by
flipping its value at the prime 2, retains ternary coefficients and the
same squarefree support. It fails inverse cancellation at 2 and creates
nonsquarefree leakage in the purported component collapse. Thus multiplicative
signs plus antichain supports are not enough for the fixed inverse of 1.

The fixed balanced fake source on {1,2,3,5,6,10,15,30} from NSR26 has
both moments zero but fails the divisor equation at 6. This small check
is not a replay of NSR26's large oscillatory counterexample certificate.

The test suite also checks cutoff strictness, the b^2 error, simultaneous
jumps, roughness in the antichain statement, twelve corrupted report
variants, duplicate JSON keys, numerical type aliases, invalid cubic
group orders, inadmissible family primes, a wrong Fermat lift, sampling
at a pole, and the sign of the rank-deflation correction.

## 6. Scope

Finite implementation consistency is not independent mathematical review.
The universal source-collapse and lower-bound proofs require review on
their own. No all-scale sign of the total covariance, no new native
upper bound, no elliptic L-value enclosure, no remote CI, no Lean build,
and no whole-repository validation are claimed.
