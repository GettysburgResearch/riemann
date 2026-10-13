# Validation and exact boundaries

## What was done

The author derived the proofs, wrote the producer and second finite assembly,
and ran the tests. There was NO independent agent or human mathematical review,
formal proof-assistant build, full-repository CI, or reconstruction of all older
analytic packets. An independent referee is still required.

- Recomputed every case in results.json with ordinary Python and python -O;
  both complete nine-case outputs are byte-identical.
- Ran checks/verify.py in both modes: 13,526 explicit finite predicates,
  including seven negative controls; outputs match checks.json byte for byte.
- Replayed the unchanged #936 helper in both modes: both outputs agree and
  report 4,937 predicates, including four older negative controls. These are
  separate counts, not new independent asymptotic cases.
- Compared the complete full-row numbers to the source-qualified #943/#942
  values and checked the newly resolved row partitions exactly.

Environment used: Python 3.13.5, NumPy 2.3.5. No floating-point spectral
calculation or numerical optimizer is used. REPLAY.json binds the actual
paired-output hashes. Duplicate replay outputs need not be committed because
these outputs are reproduced from the committed programs and their hashes.

## Domain and independent-assembly limits

The producer includes every good squarefree ideal in each declared hard norm
annulus, not merely a selected finite-prime semigroup. Its prime ideals are
formed by complete bounded Eisenstein lattice enumeration and exact splitting
conditions; conjugate ideals are retained separately. Every nonzero lattice
row in the hard norm ball is included. The largest domain has 1,145 columns,
46,608 rows, and norms D=8192,H=12855.

The second checker verifies canonical ideal enumeration/divisibility against
the product enumeration at caps 64,128,256. It compares direct scalar character
and ordered-product assemblies to the vectorized degree Gram at small cases
and orders 2,4,6,8. It independently assembles the masked principal reference
by direct per-row product support, rather than only accepting derived totals.
Both assemblies share the same authenticated finite-field helper. They are
NOT independent arithmetic backends or mathematical reviewers.

At fourth order with squarefree columns, principal sextic charge means equal
pair products because all exponent differences lie in [-2,2]. That fact is
NOT extended to unrestricted columns or order twelve. A negative control
checks the 926-versus-924 sixth-power alias discrepancy explicitly.

For the large principal reference, ordered pair products retain their actual
ideal factors and every neutral-prime nonunit mask. Divisor-mask counts use the
exact rotation-invariant hard lattice count. The sixth-row unmasked shortcut
is guarded by a direct column test; it would abort if a good root prime removed
a column. The general proof separately retains that mask.

The producer rejects domains failing its conservative int64 gate
`16 * row_count * column_count^(2k) < 2^63` before forming the Grams. Each
coefficient has coordinates bounded by its underlying term count; the factor
16 bounds intermediate real/imaginary product sums as well as the final norms.
Negative controls reject overflow, incorrect row classification, erased masks,
omitted aliases, the wrong sign conclusion, confusion of the two references,
and a one-unit mutation of the stated total.

## Analytic scope

PROOF.md Theorems 2.1 and 4.1 are exact algebra/elementary estimates on the stated
physical rows. Theorem 3.2 and the logarithmic corollary of 4.1 use Lemma 3.1's
explicitly imported classical Mobius bounds. The fixed-field, fixed-exclusion
and bounded-variation adapters are proved. The norm test has positive integral;
merely being nonzero at a single point would not suffice for the positive main
term. The twist is trivial for the positive-profile/logarithmic statements.

The finite census uses a HARD column window and HARD rows, not the smooth
Schwartz row majorant of #942. It checks no infinite Poisson tail. No small
finite percentage is extrapolated into an asymptotic exponent or sign.

The full generalized moment remains unproved. Neither the coherent native value
nor the complement degree trace is bounded here at the required diagonal power.
The proof explicitly rules out treating the logarithmic relative cancellation
as such a bound.

## Publication scope

Intended parent: #941 at f106e31f12b8a10f2d57b336c983a25fb8dd6adc.
Only the new standalone/2026-10-13-coherent-row-audit directory is to be added.
No inherited proof or integrated status is modified. Publication uses connected
GitHub actions and remote blob identities, not an asserted clean local clone.
MANIFEST.json authenticates bytes and scope; it does not certify the proofs.
