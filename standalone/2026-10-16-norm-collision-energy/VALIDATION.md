# Validation and review boundaries

Status: same-author proof reconstruction plus finite diagnostics. No
independent referee, proof-assistant build, upstream theta re-proof,
full-repository validator, or remote CI result is claimed.

## Exact checker

The standard-library check.py was run in ordinary and optimized Python;
the resulting JSON is byte-identical to CHECKS.json. It uses explicit
exceptions, not assertions that disappear under python -O.

159,956 predicates include 155,648 per-norm aggregation comparisons. Those
are not independent asymptotic cases. Exact local tests include all 29
partitions of field degrees 1 through 6, four rational primes 2,3,7,13,
and every m from 2 through 9: 928 combined local cases. They check the
finite-field tensor degree-one count, critical coefficient tails, the
absolute mass of the formal inverse-tensor quotient, and quadratic local
constant identities. The inverse quotient retains its small NONZERO
linear coefficient. Odd m is handled in exact Q(sqrt(p)).

The initial extension of the checker mistakenly expected every squared
local coefficient to be rational. A genuine odd-m collision of channels
violated that guard. It was replaced by exact quadratic-field absolute
values and sign comparisons; both final complete runs passed. The theorem
never required rational coefficients and its real-valued proof was not
changed to assume them. The numerical and proof boundaries are recorded
rather than hiding this development correction.

Six complete supported-ideal censuses over Q(omega), excluding prime ideals
above 2 and 3, are declared in CHECKS.json. The largest includes every ideal
with allowed 0/1/6 local exponents and norm at most 131072: 37001 ideals,
12207 nonzero aggregated norm coefficients. In particular norm 7^6 is
actually inside this census. Conjugate split ideals stay distinct, inert
norms are squared, and the four algebraic phase/mask profiles retain all
permitted columns. No restriction to a handpicked small prime semigroup
is used. These are NOT physical sextic character-row fixtures, a theta
calculation, all unrestricted ideals, or estimates at infinite scale.

One implementation enumerates labeled ideal choices and then aggregates;
another assembles rational-prime local polynomials and multiplicatively
reconstructs each integer norm. They share the prime sieve and local
coefficient/options specification. They are not independent arithmetic
backends or independent authors. Complete finite agreement does not prove
the analytic estimates.

Nine direct negative controls distinguish m=2 overlapping channels,
squaring before norm aggregation, omitted conjugates, a wrong prime-power
weight, incorrect masking, an incorrect prime-power twist, inert/split
confusion, missing graph degree, and false removal of equal-norm pairs by
twist averaging. Some are deliberately minimal algebraic inequalities;
no claim that these are nine mutated process executions is made.

## Separate numerical checks

numerics.py ran in ordinary and optimized Python with identical rounded
NUMERICS.json. It uses mpmath at 55 decimal digits, NOT directed intervals.
Three complete finite supported-ideal polynomials through norm 64 (19,17,16
terms respectively) compare direct log-scale quadrature with the full
pair kernel, agreeing within 1e-40. m=2 includes power-branch terms; m=6 at
this small cap does NOT. Four separately integrated Gaussian Fourier
identities test the twist factor. Four partial Schur sums through integer
1000 lie below the analytically proved infinite upper bound.

The phrase 'independent_fourier_quadratures' in JSON means a separately
computed formula, not an independent researcher or proof. These numbers
are not an infinite ideal evaluation, tail certification, fitted exponent,
or evidence about RH. Different finite signs are retained.

## Scope of the written proof

Theorems A and B are unconditional under the stated number-field and
coefficient definitions; constants are uniform in m, S, phases and masks,
not discriminants. Theorem C is a FIXED-m/profile asymptotic. The Tauberian
lemma is proved in full and credited as classical. The new prefix bound
uses a positive coefficientwise majorant, not analytic continuation to an
m-uniform strip. All Gaussian tails and distinct equal-norm pairs remain.

Priority review: Section 2's critical normalization; Section 3's tensor
count and inverse local coefficient mass (12a)--(12c); the Stieltjes tail
step in (16); the Gaussian off-diagonal Schur sum (18); and the positive
Euler limit/Tauberian passage for Theorem C. The largest logical risk is
mistaking the long twist mean for control at the principal twist tau=0.

## Packaging and publication

MANIFEST.json binds every other packet file by byte length, SHA-256 and
Git blob ID. Its own bytes are bound by the repository tree/publication
receipt. Local syntax, manifest and fresh ZIP extraction checks are
separate from mathematical approval. Remote publication is recorded only
after authenticated GitHub writes and read-back; it does not imply merge,
independent review, or a clean full-repository cloned worktree.
