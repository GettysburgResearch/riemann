# Validation and review limits

## Exact replay

From this directory:

    python check.py > /tmp/native-freezing.json
    python -O check.py > /tmp/native-freezing.optimized.json
    cmp /tmp/native-freezing.json results.json
    cmp /tmp/native-freezing.optimized.json results.optimized.json
    cmp results.json results.optimized.json

Both committed runs completed with 12,630 explicit predicates and byte-identical
JSON. The checker raises exceptions directly rather than relying on Python
assertions, so optimized Python cannot disable its tests. There are no external
package dependencies, randomness, downloaded inputs, or network calls.

## Actual finite domain

The field is Q(sqrt(-3)), with exactly the primes over 2 and 3 excluded.
All 21 good prime ideals of norm <=96 are included, both ideals above each
split prime and the inert norm-25 ideal. The checker enumerates **all 27**
squarefree ideals in that norm range and compares their aggregate Mobius
coefficients with an independent rational-norm Euler sieve.

All 54 nonzero Eisenstein element rows of norm <=13 are used at orders 2 and 4.
Orders 6 and 8 are additionally checked on the first six enumerated rows and
the principal row 1. Exact coefficients use Z[omega] with omega^2+omega+1=0;
no floating-point phase approximation is used.

The diagnostic weight is W0(t)=30(t-1)^2(2-t)^2 on [1,2], zero outside,
with D=48 and a common denominator D^4 per polynomial coefficient. It is C^1,
not C^infinity. Finite algebraic identities do not require infinite smoothness;
this is not a silent substitution into the analytic theorem's hypotheses.

Tests cover all sextic values and nonunit zeros, local multiplicativity,
sixth-power masks, actual prime-ideal generators and replica heights, equality
of smooth means after a rough prime mask, the full freezing path, and agreement
between two moment calculations. The independent direct-sign calculation
checks 610 increments against explicit sign enumeration. The Walsh calculation
checks 2,562 restoration increments. Both signs occur: 644 positive and 576
negative steps, with 1,342 zero steps. These counts are finite diagnostics,
not statistical samples or evidence for the asymptotic exponents.

The three negative controls reject monotone freezing, replacing a nonunit
character by one, and collapsing conjugate prime ideals into one prime.
Mellin-jet tests check finite signs and Leibniz coefficients only.

The larger principal table at D=1,000, 10,000 and 100,000 uses the actual native
norm coefficients, not ordinary integer Mobius: split p contributes
(1-p^(-s))^2 and inert p contributes 1-p^(-2s). Every table entry is saved as
an exact integer numerator with its denominator and exact integer cutoff.
The signs vary and these modest scales need not be in the asymptotic regime.
**No asymptotic theorem is inferred from that table.**

## Written-proof reconstruction and limits

The author rechecked the finite-Euler Mellin contradiction, the cutoff-envelope
quantifiers, the prime-replica height and masks, the single-large-prime identity,
the fixed-field prime-sum error, the differentiated cofactor tail and lower
boundary, the Mellin coefficient signs, the centered fluctuation estimate, and
the distinction between replica-measure and full-row signed flux claims.
This is a same-author reconstruction, not an independent review.

No subagent, external human reviewer, Lean or other proof assistant,
full-repository validator, upstream quasi-Riemann audit, or remote CI run was
used. The classical estimates in MATHEMATICS.md (1.2) are explicit external
inputs, not conclusions of the checker.

## Integrity

MANIFEST.json records SHA-256, Git blob identity and byte length for every other
payload file. Its purpose is to bind the tested/proposed bytes, not certify the
mathematics. Publication should create one new directory on a branch based on
#937, leaving all prior files and integrated mathematical status unchanged.
Remote publication identity is reported in the pull request and conversation;
it is not inserted self-referentially into the frozen source files.
