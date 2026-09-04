# Improvement and repair roadmap after the hostile review

```text
Current v1 status: proof invalid as written
Primary obstruction: +(rho^2/2) B^2 log B in the max-summand majorant
At rho=1/20: +B^2 log B/800
```

The earlier roadmap treated Proposition 9.5 as an unwritten ledger. The
hostile countercheck now shows more: evaluating the exact largest-summand
route described in the paper leaves a positive leading logarithmic term.
Therefore editorial corrections and missing numerical certificates are no
longer sufficient. A successful v2 needs a genuinely new global mechanism.

## Priority 0: choose a real repair architecture

A corrected proof must do at least one of the following.

### Route A: signed Cauchy--Binet cancellation

Do not replace

\[
\sum_I\Xi_I
\]

by the largest absolute summand. Instead prove cancellation strong enough to
remove at least

\[
\frac{\rho^2}{2}B^2\log B
\]

from the logarithmic size of the complete determinant.

This requires:

- a canonical sign or phase description of `Xi_I`;
- a determinant-level identity, not termwise absolute values;
- uniform control for the row set `A` selected by nonvanishing;
- a proof robust to the variation of the tail factors;
- an explicit lower bound on the amount of cancellation.

A numerical observation of cancellation is not sufficient.

### Route B: stronger common divisibility

Find a divisor of the complete Cauchy--Binet sum whose small-prime singular
coefficient is at least `2rho`, rather than

\[
2\rho-\rho^2/2.
\]

The divisor must be common to the actual determinant, not merely to a selected
term or to different local minimizers. It must also remain attached to the
same scalar used at the real place.

### Route C: redesign the weights or completion

Modify the weighted tails, clearing factors, or Newton completion so that the
compulsory selected product

\[
\prod_{i<S}\Pi_i
\]

does not contribute `2rho B^2 log B`, or so that an exact matching local
factor is forced.

The design problem is now quantitative:

```text
selected clearing-factor coefficient
<=
common local-minimum coefficient.
```

The current design fails this by `rho^2/2`.

### Route D: build a different adelic scalar

Retain the attractive same-scalar philosophy but abandon this particular
Pascal--Cauchy determinant. The replacement must have:

```text
forced nonvanishing
complete local valuation ledger
archimedean contraction
compatible optimization directions
no uncancelled entropy/clearing-factor tax.
```

## Priority 1: publish a corrected local algebra packet

The finite core remains worth preserving, but it must be separated from the
failed global conclusion.

Required repairs:

1. define `T_0:=G`;
2. repair the `T_i`/`T_{i+1}` residual index and global column sign;
3. define `D:=2B` before the square completion;
4. add `S<=B/20` to Theorem 5.1;
5. replace the factorial quotient in Lemma 4.1 by its global polynomial
   product where necessary;
6. treat zero Cauchy--Binet terms as valuation `+infinity`;
7. replace the false `5B` cutoff by a proved `O(B)` support bound;
8. supply explicit full-row/ideal-row exchanges.

This packet should make no irrationality claim.

## Priority 2: formalize the countercheck

The leading-order obstruction is simple enough for a small formal or
proof-assistant project.

Suggested theorem surface:

```text
pascal_consecutive_minor_ne_zero
selected_clearing_log_asymptotic
consecutive_cauchy_log_is_O_B2
tail_product_log_is_O_BlogB
odd_a_layer_exact_cancellation
small_prime_m_singular_coefficient
max_summand_majorant_lower_bound
```

The final theorem should state

\[
\mathcal M_B\ge
\frac{\rho^2}{2}B^2\log B-O_\rho(B^2).
\]

This would provide a durable refutation of the v1 proof route independent of
floating computation.

## Priority 3: release the missing numerical artifacts

The missing certificates no longer repair the theorem, but they remain useful
for validating the local optimization and for any redesigned scalar.

### Odd-small-prime certificate

For every merged interval publish:

```text
rational endpoints
marginal-ladder ordering
rational quadratic Q_0(v)
symbolic antiderivative identifier
outward-rounded endpoint enclosure
Euler--Maclaurin remainder
```

The checker must verify the full partition, formulas, argument shifts,
remainder signs, and final interval.

### Middle-prime certificate

For every one of the claimed 235 cells publish:

```text
t interval
affine boundary ordering
selected marginal levels
rational affine E_{1/20}(t)
exact integral.
```

The checker should recover the displayed rational exactly.

## Priority 4: understand the min/max mismatch abstractly

Formulate a general theorem for determinant expansions

\[
D=\sum_I X_I.
\]

The v1 failure has the pattern:

```text
local common divisor = sum over primes of minimum_I local_cost_p(I)
real majorant         = maximum_I real_cost(I)
```

The minimum may be attained at different subsets for different primes, while
the real maximum is forced to include subsets with a larger clearing-factor
burden. A useful abstract quantity is the compatibility defect

\[
\mathfrak D=
\max_I R(I)-\sum_p\min_I L_p(I).
\]

Research goals:

- derive lower bounds for `D` from compulsory subsets;
- identify convex-duality conditions under which local minima and the real
  maximum are compatible;
- characterize when signed summation can beat the maximum;
- translate the defect into a Hall, transport, or entropy problem.

This abstraction is directly relevant to Riemann's Gram, Schur, and
coefficient-extraction programs.

## Priority 5: optimize only after the leading obstruction is removed

The paper fixes `rho=1/20`. Changing `rho` within the current absolute
max-summand method does not solve the problem, because

\[
\rho^2/2>0
\]

for every fixed positive `rho`.

Possible asymptotic regimes to investigate are:

- `rho=rho(B)->0`, while retaining enough columns for nonvanishing and a
  meaningful contradiction;
- a different local layer whose singular coefficient equals or exceeds
  `2rho`;
- a signed determinant estimate in which the `rho^2/2` tax cancels.

Only after one of these succeeds should the finite `B^2` margin

\[
4\rho-2\rho^2+c_{\rm odd}(\rho)
-\Lambda_{\rm mid}(\rho)-\Delta_{>B}(\rho)
\]

be re-optimized.

## Priority 6: effective bounds and irrationality measures

An effective threshold or irrationality measure is premature until the
leading-order sign is repaired. After that, one would need:

- effective Stirling errors;
- an effective PNT error for every compact prime range;
- explicit stability constants;
- a complete Pascal quotient height bound;
- directed numerical certificates;
- a uniform negative margin after every error.

## Priority 7: generalize the salvageable finite algebra

For a periodic coefficient sequence or Dirichlet character, study vector tails

\[
T_m^{(\chi)}=
\sum_{r\ge0}\frac{\chi(m+r)}{(m+r)^2}.
\]

A possible source-design program is

```text
period-q vector recurrence
-> weighted vector tails
-> block or confluent Cauchy matrix
-> block Pascal alternant
-> local occupancy
-> explicit compatibility-defect calculation.
```

The first target should be a classification theorem saying which weight and
completion choices pass the leading-order compatibility test. Irrationality
claims should come only after that gate.

## Priority 8: Riemann-facing extraction

The strongest lesson for the Riemann project is now a firewall rather than a
positive theorem:

```text
same scalar is necessary but not sufficient;
local minimum and archimedean maximum must also be compatible.
```

For every proposed zeta determinant or Gram proof, record:

1. the exact finite object whose nonvanishing is known;
2. the exact object receiving local arithmetic divisibility;
3. the exact object receiving the archimedean bound;
4. every minimization or maximization over auxiliary subsets;
5. a leading-order compatibility calculation before finite constants are
   optimized.

A possible RH architecture inspired by the product-formula idea would still
require wholly new theorems:

```text
one off-line zero
-> canonical nonzero arithmetic determinant at infinitely many scales
-> compatible common local saturation
-> signed archimedean contraction
-> product-formula contradiction.
```

The Catalan v1 paper supplies neither the first arrow nor a valid final
contraction, but its failure gives a precise test that future architectures
must pass.
