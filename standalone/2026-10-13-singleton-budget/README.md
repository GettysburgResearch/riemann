# A larger native sector and a growing-order singleton bound

**PROPOSED component mathematics; no new zero-free exponent or full moment theorem.**
This packet continues #932, reads the new #936 and #937 constructions, and
publishes the preceding replica packet that had only been available as downloads.

## Actual new result

In a Hermitian 2k-tuple of squarefree columns, call a prime a singleton when it
occurs in exactly ONE of the 2k columns. The absolute sum of all native tuple
contributions whose singleton primes have norm at most (log X)^2 is

    O_{k,epsilon}(H X^(k+epsilon))

for every fixed k. All element rows, original zero masks, and arbitrary additional
tuple selectors are retained. The column cap is Nn<=X. Constants do not depend
on the row or coefficient vector bounded by one.

This is a larger COMPLETE sector than either the smooth residual sextic-conductor
sector in #936 or the partially frozen sign moment in #937, and also includes the
older no-singleton sector. Rough primes occurring 3, 5, or any number >=2 are
allowed; a residual character need not become principal at those primes.

The proof is elementary positive Rankin accounting. It uses the local factor

    (1+r)^(2k)-2k*r,

not an unfiltered signed Euler product or a substitute physical row measure.
The generic method is classical and the overlapping fixed-order results are
credited; no global novelty claim is made.

## Explicit dependence on growing moment order

For every integer 1<=k<=log X and all sufficiently large X,

    T_{k,(log X)^2}(u)^(1/(2k))
      <= X^[1/2 + (log log log X)/(2 log log X) + C/(log log X)],

where C depends only on the fixed field. Thus this sector costs X^(k+o(k))
uniformly in that growing-order range, without hiding a potentially enormous C_k.
This is not a theorem about the whole moment or an explicit band in zero height.

A second bound allows rough singleton product norm at most Z, at cost

    O_{k,epsilon}(H X^(k+epsilon) sqrt(Z)).

All hypotheses, normalization, proofs and quantifiers are in
[MATHEMATICS.md](MATHEMATICS.md), Theorems 4.1 and 5.1 and Section 6.

## Exact arithmetic that remains

The complement has a unique largest singleton prime. Factoring it out of its
one column gives the exact native identity

    M_{2k} = E_{k,y} - 2k Re sum_p nu(p) sum_u w_H(u) chi_p(u) C_{p,u}.

The complete E sector is now bounded at the stated size. C retains every native
composite cofactor, the shorter column D/Np, exclusions, the same physical row,
and the largest-singleton selector. The one-sided lower bound for this signed
prime/cofactor sum is OPEN. Its k=2 case, with the inherited extraction hypotheses,
would give 17/24; no such lower bound is proved in this packet.

## Recovered work

The adjacent directory
[2026-10-13-replica-physical-model](../2026-10-13-replica-physical-model/README.md)
is the exact eleven-file packet from the preceding conversation. Its old
"not pushed" labels describe its historical creation state and are deliberately
preserved so its original hashes and diagnostics stay intact. This continuation
publishes those bytes, rather than silently rewriting its history.

The recovered packet proves a comparison of principal divisibility replicas with
an independent model, relative to the UNKNOWN Mobius source envelope. It does
not supply that envelope. The new bound above concerns the actual original
moment sector instead of trying to make that coherent source disappear.

## Verification and limits

The new checker passed 23,604 exact predicates in ordinary and optimized Python
with byte-identical results. The recovered checker was rerun in both modes and
reproduced its archived results exactly. The finite character test uses only
five named prime ideals; its columns are not all native ideals under the cap.

There was no independent agent/human review, proof-assistant build, remote CI,
or full-repository validator. These are explicit proposed proofs, not integrated
results. See [VALIDATION.md](VALIDATION.md) and the publication record.
