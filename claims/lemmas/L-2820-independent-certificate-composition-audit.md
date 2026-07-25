# L-2820 — Independent audit of the exact fixed-vector certificate composition

Claim ID: L-2820  
Title: The X-2805/X-2801 checker composes alpha, complete prime intervals, and symmetric corrections in the correct outward direction  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: L-2801--L-2807; T-2801/T-2819  
Scope: final quantitative verdict for one exact D-0801 vector  
Related counterexample candidates: any future strict negative X-2805 certificate

## Verdict

The exact arithmetic composition in

- `assemble_directed_certificate.py`, and
- `verify_fixed_vector_certificate.py`

passes this independent audit. The interval directions, vector-norm scaling, segment coverage checks, higher-power uniqueness, count identities, and positive/negative verdict tests are correct.

The checker intentionally does not prove producer provenance, prime enumeration inside a segment, or the analytic dictionary; those are supplied by L-2806, L-2807, and T-2801/T-2819.

## Abstract certificate theorem

Let `x` be a nonzero exact complex vector and let

\[
 N=x^*x>0.
\]

Suppose:

1. `alpha` lies in `[a_-,a_+]`;
2. a contiguous exact shard partition gives complete prime intervals
   \[
   P_j\in[p_{j,-},p_{j,+}];
   \]
3. exactly one shard contains all higher prime powers;
4. the global counts match the declared complete finite source;
5. the nonprime correction satisfies
   \[
   |C(x)|\le BN
   \]
   for an exact nonnegative rational `B`.

Put

\[
 P_- =\sum_jp_{j,-},
 \qquad
 P_+ =\sum_jp_{j,+}.
\]

Then the exact D-0801 value

\[
 Q(x)=\alpha N-P+C(x)
\]

lies in

\[
 \boxed{
 Q(x)\in
 [a_-N-P_+-BN,\;a_+N-P_-+BN].
 }
\]

Consequently:

- a positive lower endpoint certifies `Q(x)>0`;
- a negative upper endpoint certifies `Q(x)<0`;
- otherwise the sign is unresolved.

## Proof

Since `N>=0`, interval scaling gives

\[
 \alpha N\in[a_-N,a_+N].
\]

Minkowski addition of all shard intervals gives

\[
 P\in[P_-,P_+].
\]

Therefore interval subtraction gives

\[
 \alpha N-P
 \in[a_-N-P_+,a_+N-P_-].
\]

The correction condition is equivalent to

\[
 C(x)\in[-BN,BN].
\]

Adding this symmetric interval proves the boxed formula. Strict endpoint separation yields the sign statements. ∎

## Audit of `assemble_directed_certificate.py`

The assembler correctly:

1. reconstructs the exact dyadic vector and its canonical digest;
2. reconstructs the exact carrier and alpha interval;
3. derives one parameter digest from carrier, cutoff, cells, and total segment count;
4. requires every shard to match vector, parameter, and normalization fingerprints;
5. requires the exact shard-range ledger in the run plan;
6. intersects multiple directed precision intervals only after proving nonempty overlap;
7. rejects precision-level count disagreement;
8. verifies exact global prime, higher-power, and total counts;
9. emits exact rational endpoints rather than decimal midpoints.

For one valid precision interval per range, intersection returns that interval unchanged. Multiple precisions may narrow the interval but can never enlarge it or manufacture overlap.

## Audit of `verify_fixed_vector_certificate.py`

The checker correctly:

1. recomputes `N=x*x` from exact dyadic coordinates;
2. rejects the zero vector;
3. rechecks vector and parameter digests;
4. sorts shard ranges and requires exact contiguous coverage from zero to `total_segments`;
5. requires exactly one higher-power stream;
6. rejects a nonzero higher-power count without its inclusion flag;
7. adds all prime intervals by Minkowski addition;
8. multiplies the alpha interval by the nonnegative exact norm;
9. subtracts the prime interval with endpoint reversal;
10. recomputes the correction bound from exact target parameters;
11. scales the correction radius by the exact norm squared;
12. widens the leading interval symmetrically;
13. uses strict `lower>0` and `upper<0` tests.

The wrapper additionally requires the canonical T-2801 normalization digest.

## Layer separation

The final proof consists of four logically distinct layers:

1. **analytic identity:** T-2801/T-2819;
2. **finite-source completeness:** L-2807 plus the exact segment ledger;
3. **directed analytic enclosures:** L-2805/L-2806 and the producer artifacts;
4. **exact rational composition:** this lemma and the standard-library checker.

The exact checker is not expected to reprove layers 1--3. A candidate review must examine all four independently.

## Adversarial mutations

A valid checker must reject or change verdict under:

- a segment gap or overlap;
- duplicate or missing higher-power stream;
- a global count mismatch;
- vector, parameter, or normalization mutation;
- a reversed shard interval;
- nonoverlapping precision intervals;
- omission of the vector-norm factor from alpha or correction;
- subtraction without endpoint reversal;
- adding the correction budget only on one side;
- non-strict comparison at zero.

The current checker implements these directions correctly.

## Remaining uncertainty

No algebraic composition gap was found. The trusted-base risks are upstream:

- whether each compiled producer matches its reviewed source;
- whether each directed interval encloses the intended analytic term;
- whether the segment sieve and higher-power stream executed without fault;
- whether T-2801/T-2819 is accepted under repository review.

Independent producer reproduction remains mandatory for a strict negative result.

## Suggested next attack

When the final `4800:4900` shard lands, run the assembler and checker immediately, preserve the complete output and digests, and classify the result before beginning any 256-bit or postselection work. A strict 192-bit interval is already a proof interval; higher precision is independent stability evidence, not a logical prerequisite.