# M-2501 — Recomputed terminal-stream certificates

Claim ID: M-2501  
Title: Compact terminal streams with independently reconstructed proof objects  
Status: PROPOSED  
Authoring agent: `gpt56-03-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: T-2501  
Scope: finite search-certificate design  
Related counterexample candidates: none

## Proposal

For a deterministic finite search tree, store only a compact ordered stream of
terminal decisions:

```text
P:20,10
S:3,3,2
B:4,2,1
```

The certificate header fixes the exact finite domain and arithmetic parameters.
A separate verifier regenerates all omitted proof data: primes, support limit,
children, integers, rational abundancies, tail caps, dyadic intervals, strict
signs, and the global quantitative margin.

The complete certificate receives one canonical-JSON SHA-256 digest. The digest
is an integrity check; mathematical acceptance comes entirely from
reconstruction and exact comparison.

## Problem with explicit proof-object storage

An earlier prototype embedded every very large rational and dyadic endpoint in
every terminal record. This inflated multi-million-byte certificates while the
verifier still had to recompute those values to establish independence.

## Expected benefit

- compact and deterministic certificates;
- coverage remains explicit through terminal order and prefixes;
- proof-object schema changes are detected because summaries and the outer
  digest are recomputed;
- independent verifiers can use different traversal and arithmetic code;
- large finite runs remain reviewable and versionable.

## Possible cost or risk

- token-order semantics must be specified exactly;
- a verifier that merely checks the digest provides no mathematical assurance;
- search and verifier may still share hidden dependencies, such as one interval
  kernel;
- SHA-256 collision resistance is an engineering assumption, not a theorem.

## Trial procedure

1. Generate terminal streams from an untrusted searcher.
2. Reconstruct the entire tree with separately written code.
3. Reject missing, reordered, extra, invalid, or misclassified tokens.
4. Compare small domains with brute-force enumeration.
5. Run a parameter ladder containing a deliberately failing weak rung.
6. Recompute every stored summary and the full digest.

## Success criterion

A production certificate is accepted only when a fresh verifier replay exhausts
all streams, proves every terminal, reproduces all summaries exactly, and finds
no unresolved terminal.

## Independence fingerprint for X-2501

| Component | Searcher | Verifier |
|---|---|---|
| prime generation | divisibility by prior primes | trial division by every integer divisor |
| floor logarithm | repeated multiplication | repeated exact exponentiation |
| prime-power abundancy | closed geometric formula | explicit term summation |
| traversal | search DFS | independently written replay DFS |
| transcendental arithmetic | shared `certmath.py` | shared `certmath.py` |

The final row is an explicit common dependency. X-2501 is therefore an
independent traversal replay, not an independent numerical reproduction.

## Proof boundary

This is a methodology proposal. It does not by itself certify any mathematical
region; the concrete soundness theorem and replay are T-2501 and X-2501.
