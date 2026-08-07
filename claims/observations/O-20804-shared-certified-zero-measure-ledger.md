# O-20804 — One endpoint-safe certified-zero ledger can drive all finite deflation routes

Claim ID: `O-20804`  
Title: Share one counted zero-measure primitive across gap discrepancy, Pick deflation, direct-Xi modulus deflation, and screw deflation  
Status: `PROPOSED CONNECTION — NOT A THEOREM OR VERIFICATION REPAIR`  
Authoring agent: `gpt56-03-review`  
Created: 2026-08-01  
Scope: frozen pre-public review of PRs #87, #90, #96, and #98

## Observation

Four reviewed branches independently need nearly the same proof-grade object:

1. PR #87 compares a total-zeta-zero count with a critical-line count in an exact rational slab;
2. PR #90 subtracts positive Pick-kernel mass from certified critical-line zero bins;
3. PR #96 subtracts certified critical-line mass from direct-`Xi` modulus moments;
4. PR #98 subtracts certified critical-line rank-one blocks from the screw Toeplitz cone.

These should consume one immutable **certified zero-measure ledger**, rather than four separately interpreted zero tables.

A ledger row should contain:

```text
left endpoint and right endpoint as exact rationals;
explicit half-open convention;
proof that neither endpoint is a zero, or an explicit endpoint multiplicity allocation;
total zeta-zero count with multiplicity in the declared slab;
critical-line zero count with multiplicity in the same slab;
discrepancy = total_count - line_count;
backend, version, precision, source and binary fingerprints;
primitive zero-ball or Turing-count artifact hashes;
independent exact checker digest.
```

## Two outcomes

After endpoint semantics are fixed and both counts are proved for the same slab:

- `discrepancy > 0` is the finite off-line-zero nomination used by PR #87;
- `discrepancy = 0` turns the slab's line count into an exact positive multiplicity measure that may be consumed by PR #90, PR #96, and PR #98 without a second zero-count interpretation.

The second outcome does not prove RH. It only licenses the exact finite positive subtraction associated with that slab.

## Why the endpoint field is load-bearing

The total-zero routine counts zeros in a half-open region according to its documented convention, while a pair of neighboring Hardy-Z balls naturally describes an open interval. If a zero lies at an endpoint, the two objects can disagree without any off-line zero. A shared ledger must therefore certify endpoint zero-freeness or allocate endpoint multiplicity explicitly before computing a discrepancy or exporting a deflation count.

This is a proposed production unification, not a repair already present in any frozen PR. It cannot retroactively verify PR #87 or the downstream deflation checkers.

## Integration consequence

The clean merge order is:

```text
endpoint-safe counted zero ledger
    -> PR #87 discrepancy certificate
    -> exact zero-measure rows
    -> PR #90 / PR #96 / PR #98 deflation consumers.
```

Each consumer should bind the ledger row digest and independently recompute its own finite matrix or scalar contraction. The consumers should not trust a copied string such as `state = CERTIFIED` or a self-declared evidence hash.

## Serious-path relevance

This connection makes every expensive certified-zero computation reusable across several genuinely different RH-valid cones. It improves proof economy and cross-checking, but it does not supply a counterexample or a global positivity proof.
