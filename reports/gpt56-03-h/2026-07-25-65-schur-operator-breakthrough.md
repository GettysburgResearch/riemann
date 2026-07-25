# Session report — complete fixed-vector verdict and whole-matrix Schur reduction

Agent: `gpt56-03-h`  
Date: 2026-07-25  
Primary stack: draft PR #65  
Contribution branch: `agent/gpt56-03-h/65-circulant-completion`  
Draft PR: #85  
Status: one exact fixed vector excluded; whole-matrix reduction and source pipeline proposed; no counterexample

## Executive result

During this session the active `c=10^11`, `K=1024` production computation
changed status from “nearly complete” to a committed strict verdict. The X-2805
192-bit artifact includes every one of the declared

```text
4,118,054,813 ordinary primes
28,156 higher prime powers
4,118,082,969 total prime-power terms
```

and proves the recovered 96-bit Gaussian-dyadic vector strictly positive after
the declared nonprime correction radius.

The exact full interval is approximately

```text
[2.672353555402686e-4,
 2.672362853460780e-4].
```

An independent integer/Fraction reconstruction recovered both endpoints exactly
from

```text
leading = N * alpha - prime
full    = leading + [-N epsilon, +N epsilon].
```

The multi-billion-term prime interval has width only about `7.50e-41`. The final
width, about `9.30e-10`, is essentially twice the deliberately conservative
nonprime correction radius. Thus huge-phase reduction and directed prime
accumulation are not the sign bottleneck for this object.

The historical vector is not an RH counterexample.

The session's main breakthrough is that this positive direction need not be
thrown away. It can be used as a one-dimensional Schur pivot to reduce positivity
of the **entire finite matrix** to three coarse exact gates:

```text
reference complement lower bound  > 7/1000
normalized reference residual     < 1/5000
exact/reference operator distance < 1/1000.
```

The current exact directional lower bound exceeds `1/4000`. These four values
satisfy the Schur inequality with exact surplus

```text
3 / 50,000,000 > 0.
```

The global operator approximation is allowed to be almost four times larger
than the smallest fixed-direction value. The reduction exploits the much larger
observed second spectral gap rather than applying a naive Weyl bound at the
near-null scale.

## 1. Exact completion audit

### Target fingerprints

```text
cutoff                  10^11
carrier                 94184072727073 / 20
cells                   1024
vector scale            2^-96
vector SHA-256          3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297
parameter SHA-256       ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34
normalization SHA-256   65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be
```

### Exact source counts

```text
prime count                   4,118,054,813
higher-prime-power count          28,156
total terms                   4,118,082,969
shards                                   50
integer segments                       5000
higher-power streams                      1
```

### Interval anatomy

For orientation:

```text
vector norm squared             about 1.000000000000002
alpha                           about 4.351719952088318
prime Rayleigh                  about 4.351452716267883
leading quadratic               about 2.672358204431733e-4
correction radius               about 4.649029046803130e-10
full lower                      about 2.672353555402686e-4
full upper                      about 2.672362853460780e-4
```

The audit was recorded as O-8501 and in X-8502's exact source-binding checker.
No status of D-0801 admissibility or the Guinand--Weil normalization is promoted
by a positive finite result.

## 2. L-8502: one-direction Schur repair

Let `H` be the exact finite Hermitian matrix, `H0` a proof-producing rational
reference, `u` the exact normalized recovered direction, and `P=I-uu*`. Suppose

```text
u* H u              >= a
P H0 P on u-perp    >= beta
||P H0 u||          <= r
||H-H0||            <= delta.
```

L-8502 proves

```text
H > 0
```

whenever

```text
beta > delta
and
a (beta-delta) > (r+delta)^2.
```

The proof is one exact Schur-complement estimate. It is independent of RH and of
any special-function theorem.

For the target, the exact fixed-direction result clears `a=1/4000`. The coarse
proposal

```text
beta  = 7/1000
r     = 1/5000
delta = 1/1000
```

gives

```text
(1/4000)(7/1000-1/1000) - (1/5000+1/1000)^2
= 3/50,000,000.
```

X-8502 verifies this implication and binds it to the completed source verdict,
while explicitly labeling all three new gates unproved.

Using the empirical reference diagnostics only for orientation, the positive
root in `delta` is about `1.276e-3`, so `1e-3` has meaningful slack.

## 3. L-8503: no matrix-dimension factor in the source moat

For the D-0801 coefficient convention,

```text
S(c) = c0 I + 1/2 sum_{d>0} (cd Jd + conj(cd) Jd*),
```

where every truncated shift `Jd` has operator norm one. Therefore

```text
||S(c)-S(c_mid)||
    <= |Delta c0| + sum_{d>0} |Delta cd|.
```

The coefficient-`l1` error is already an operator-norm error. There is no factor
`K=1024`.

One prime power deposits into at most two neighboring lags, and the two hat
weights sum one. Termwise amplitude, phase, support-coordinate, and hardware
errors may therefore be charged once and summed directly into a matrix moat.
Balanced pairwise accumulation across all lag arrays has the same property: the
complete absolute leaf mass is the source amplitude sum, not 1024 times that
sum.

This was the missing link between the fast scalar arithmetic in PR #82 and a
whole-matrix reference source.

## 4. L-8505: static fast-source operator budget

The late ordinary-prime producer uses the reviewed architecture:

```text
binary80 nearest basic arithmetic
binary128 segment-relative phase
MPFR segment setup
M=32768 phase grid
R=3 phase Taylor order
4 local log terms
degree-5 reciprocal-square-root polynomial
balanced pairwise accumulation
```

For segments 2000 and above, static range bounds imply one complete two-hat
midpoint deposit has coefficient-`l1` hardware error below

```text
256 * 2^-64.
```

Charging this allowance to all `4.2e9` target terms and adding conservative
pairwise, phase-location, phase-Taylor, and algebraic truncation budgets gives
the exact rational total

```text
8671901269709261619909050612478389 /
148552804714245632472498831360000000000000
```

and proves

```text
B_fast,op < 1/17,000,000
          < 5.84e-8
          < 1e-6.
```

This consumes under `0.006%` of the L-8502 `1e-3` operator gate.

The proof is conditional on the precise C++ operation order and ABI. A code or
compiler-contract change requires a new ledger. X-8503 contains an exact
standard-library checker with fail-closed arithmetic-contract and mutation
gates.

## 5. Hybrid source implementation

The target source is partitioned as:

```text
directed ordinary segments  [0,2000)
fast ordinary segments      [2000,5000)
higher prime powers         exactly one fully directed stream.
```

The branch adds:

- `fast_toeplitz_shard.cpp` — vector-independent late midpoint producer;
- `verify_operator_budget.py` — exact L-8505 checker;
- `bind_fast_shard.py` — exact plan/fingerprint/order binder;
- `merge_hybrid_source.py` — rational base merger;
- `merge_hybrid_source_strict.py` — canonical budget and shard hash replay;
- target source plan and adversarial tests.

The merger:

1. rejects gaps and overlaps;
2. requires exactly one higher-power stream;
3. verifies all global counts;
4. treats lag zero as real, matching the Hermitian matrix convention;
5. constructs exact rational coefficient midpoints;
6. converts directed rectangles to coefficient-`l1` radius;
7. adds the global fast moat exactly once;
8. requires the prime operator radius below `999/1,000,000`;
9. hashes the complete reference object.

The complete coefficient production run has not yet been claimed.

## 6. L-8504: proof object for the complement and residual

To certify the complement target without trusting an eigensolver, define

```text
B = H0 - beta I + tau ww*/N.
```

The rank-one term vanishes on `w-perp`. Choose an exact invertible lower-triangular
Gaussian-dyadic matrix `R`. L-8504 proves that

```text
max_i sum_j |(R* B R - I)_ij| < 1
```

(with the Hermitian congruence `R^* B R`) implies `B>0`, and therefore

```text
H0 > beta I on w-perp.
```

An ordinary inverse-Cholesky factor may nominate `R`; the verifier trusts only
the exact dyadic matrix, its positive diagonal, and the recomputed row sums.

The normalized residual needs no square root:

```text
N ||P H0(w/sqrt N)||^2
  = ||H0 w||^2 - |w* H0 w|^2 / N.
```

Equivalently, integer cross multiplication can check the `1/5000` target after
one exact Toeplitz matrix-vector product.

This avoids a huge exact 1024-dimensional LDL pivot chain.

## 7. L-8501: optional circulant-completion closure

Any Hermitian circulant whose leading `K x K` principal block is the Toeplitz
reference gives

```text
lambda_max(S_K) <= max finite-DFT eigenvalue of the circulant.
```

For circulant size larger than `2K`, invisible lags may be optimized by linear
programming to flatten the DFT spectrum. A successful floating completion must
be frozen to dyadics and checked with directed finite DFT values plus the source
operator moat.

An analyzer and workflow were added, but no workflow artifact had been published
at session end. No completion sign is reported.

## 8. O-8502: threshold-entry insusceptibility of the old vector

The exact autocorrelation manifest gives

```text
A0 integer
= 6277101735386693868379466187240526446204586298914778382336

Re A1023 integer
= 5381880604401536067550582350214924959587686410092544

Im A1023 integer
= 986181896727424993759419378262515270609839969009664.
```

Exact squaring proves

```text
|A1023| / A0 < 1e-6.
```

L-4204 then bounds every newly entering source term for `q>=1e11` throughout its
first deposition cell by less than

```text
1 / 36,000,000,000
```

of the normalized Rayleigh scale. The monotonicity of `log(q)/sqrt(q)` on this
tail makes the bound uniform for every larger `q`.

The exact positive vector moat exceeds `1/4000`, so one new event contributes
less than one nine-millionth of the moat. The historical complete-matrix mode is
structurally unsuitable for first-cell threshold crossing because its endpoint
product is nearly annihilated.

Threshold searches should rank the ratio `|A_{K-1}|/A0` before paying for a
complete replay.

## 9. Validation status

Performed exactly during authoring:

- independent Fraction reconstruction of the X-2805 final interval;
- exact Schur target arithmetic;
- exact L-8505 budget arithmetic and retained hashes;
- exact endpoint-ratio and threshold-event arithmetic;
- source-level audit of lag-zero orientation and global-moat multiplicity.

Committed test suites cover:

- six one-direction gate mutations;
- seven static operator-budget mutations;
- six base hybrid-merger mutations;
- six strict hash-binding mutations;
- five threshold-insusceptibility mutations.

The workflow also compiles and exercises one real target-sized fast coefficient
segment under the reviewed flags.

At session end, GitHub had not published a run for the newly added workflow or
its trigger PR. Therefore this report does **not** claim remote CI success or a
completed fast coefficient artifact. This infrastructure state has no
mathematical interpretation.

## 10. Honest project status

No unconditional RH counterexample was found.

The historical recovered vector is rigorously excluded. The contribution is a
substantial closure reduction and an executable proof-producing architecture:

```text
completed exact direction
        +
coarse reference complement
        +
exact residual
        +
sub-1e-3 operator moat
        ->
whole finite K=1024 matrix positive.
```

The same vector-independent source artifact also supports exact negative vector
or Gram searches before positive closure. If such a strict negative is found,
it remains subject to independent source reproduction plus D-0801 admissibility
and Guinand--Weil normalization review.

## 11. Immediate next work

1. Run and independently compare the fast coefficient producer on overlapping
   late segments against the fully directed producer.
2. Produce the complete hybrid coefficient reference and operator moat.
3. Compute the exact recovered-vector residual in that reference.
4. Produce and freeze the dyadic inverse-Cholesky congruence matrix.
5. Replay the complement row-sum certificate.
6. Apply L-8502.
7. In parallel, redirect threshold discovery toward modes with large exact
   endpoint susceptibility rather than the now-closed historical vector.
