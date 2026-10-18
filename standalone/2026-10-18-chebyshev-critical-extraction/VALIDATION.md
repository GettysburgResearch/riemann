# What was actually validated

The accepting standard-library verifier runs in ordinary Python and python -O
with byte-identical CHECKS.json. It uses explicit checks, not Python assert.
There are **3,773 finite predicates**, with the group counts published in the
report. This is not a count of independent analytic cases.

Coverage:

1. Exact rational Chebyshev polynomial algebra at orders 1 through 24; complete
   Newton root sums, quadrature, endpoint reproduction, squared kernel norms,
   Markov witnesses, and 96 exact rational-function interpolation/error cases.
   No rounded cosine node is accepted as an exact algebraic root.
2. All 157 exterior Eisenstein ideals through norm 512, with primes above 2
   and 3 excluded. A distinct rational-divisor norm-count construction checks
   all 512 norm fibers. Both paths use the same classical splitting rules;
   this is not complete implementation independence. The coefficient germ
   identity is checked through order six as a polynomial in separate formal
   prime-ideal logarithms, before specializing them to actual logarithms.
   Shared divisors and distinct conjugate ideals are retained.
3. Exact synthetic meromorphic models with multiplicities one through eight;
   the shifted-pole subtraction; one canceled shift with uncanceled neighboring
   shifts; and 24 exact pole-energy constants. These are not actual zeta zeros.
4. Ten corruption flags modify the runtime model and are each executed in a
   separate optimized subprocess. They must fail at their declared gate.
   They are not described as externally authored mutations or peer review.

The original #986 replay also passed after extracting the mounted archive:
two original accepting modes, its complete manifest, and its ten separately
executed original negative controls. No other historical checker was rerun.

The new full replay authenticates every manifested payload by byte length,
SHA-256 and Git blob SHA; repeats both accepting modes; and repeats all ten
corruption cases. A fresh ZIP extraction is replayed separately before delivery.
The manifest seals the new packet, not the mathematical truth of a theorem.

## Explicit limits

No real L-values, zeta zeros, infinite Gaussian source values, or asymptotic
numerical evidence were computed. The existence and source dependence of the
small fixed H rest on the written local-pole proof; no numerical H for a number
field is certified. The finite ideal cap is not the analytic theorem's support
cap. Infinite tails are justified in the written proof, not by the finite census.

PROOF.md and FIXED_SHIFT_TARGET.md require independent mathematical review.
There was no Lean build, full-repository validator, remote CI result, complete
external theorem reconstruction, or independent mathematical referee. The
arithmetic upper estimates OPEN-H and OPEN-J remain unproved.

## Review priorities

Challenge Lemma 1's uniform complex-h bound and full Gaussian tails first;
then the endpoint weights, coefficient cost and entire growing-order error.
For the critical implication review the fixed versus moving averaging measures,
the exact pole continuum, V-valued Mellin normal convergence, and nonzero
pole-vector norm. Theorem E's limsup argument is valid without a rightmost-zero
hypothesis only because a finite limsup itself licenses the necessary Laplace
half-plane. Its multiple-zero constant is not claimed sharp.
