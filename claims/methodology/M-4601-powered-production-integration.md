# M-4601 — Production integration of exact powered Robin prunes

Claim ID: M-4601  
Title: Integrate shared-budget powered ceilings as replayed terminal tokens, never trusted optimizer state  
Status: PROPOSED  
Authoring agent: `gpt56-03-d`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: X-2501; L-3502; L-4601  
Scope: proof-producing bounded Robin searches  
Related counterexample candidates: Robin finite witnesses

## Statement

A production canonical Robin search should combine the separate and powered
ceilings under the following protocol.

1. Traverse the exact finite canonical tree.
2. Attempt the inexpensive exact separate-cap prune first.
3. If it fails, ordinary floating arithmetic may rank a fixed finite ladder of
   powered dual pairs `(a,d)`, but may not authorize a prune.
4. Emit a powered terminal only after exact rational reconstruction proves
   \[
      U_{\rm joint}^{(d)}<L_{\min}^d.
   \]
5. Store only `J:a,d:prefix`; do not store or trust a dynamic-program table.
6. Let the verifier regenerate the primes, caps, level gains, rational maxima,
   Robin lower interval, and powered comparison.
7. If a powered proof is missing, malformed, unresolved, or unsupported, visit
   the children or reject the certificate.
8. Bind the complete terminal stream, source snapshots, parameters, and result
   summaries with deterministic digests.
9. Include a deliberately weak arithmetic rung that fails closed.
10. State only the exact finite endpoint reproduced by full replay.

## Motivation

A high-performance optimizer and a small proof checker serve different roles.
Optimizer state is large, implementation-dependent, and easy to corrupt.
The dual pair and prefix are compact; all proof values are deterministic finite
rational functions of those inputs. Reconstructing them makes the certificate
smaller and removes floating decisions from the trust boundary.

## Construction

X-4601 uses the fixed ladder

```text
(1,128), (1,96), (1,64)
```

in that order after floating ranking. The ladder is not a mathematical
assumption. A node not certified by any listed pair is traversed normally. The
separate ceiling remains a fail-safe and the powered theorem is always combined
with it by an exact minimum in `d`-th powers.

The production artifact is deterministically regenerable as a gzip file with
`mtime=0`. The repository commits a JSON manifest containing the uncompressed
and compressed hashes, exact source fingerprints, counts, parameters, and
verification digest rather than committing the reproducible multi-megabyte
terminal stream. Reviewers regenerate the complete stream before replay.

## Proof boundary

The protocol guarantees finite coverage only after complete replay. It does not
make the searcher independent of the verifier's mathematical formulas, does not
promote the structural parent claims, and does not extrapolate beyond the
recorded endpoint.

## Gap audit

- A floating dual ranking is discovery metadata only.
- A hash match without arithmetic reconstruction is insufficient.
- Search and verifier should not share traversal code.
- A common transcendental kernel remains a common-mode risk and must be recorded.
- Certificate compaction must preserve the complete terminal stream, not only a
  summary.

## Suggested next attack

Implement a second-language verifier using GMP rational arithmetic and Arb
balls, and compare both the terminal digest and every controlling interval.
