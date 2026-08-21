# O-19820 — Proposed pre-public integration connections

Claim ID: `O-19820`  
Status: **PROPOSED — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-m`  
Created: 2026-08-01  
Scope: connections uncovered during the frozen review of PRs #132–#159  
Proof status: integration observations only; no RH claim

## 1. Canonical Christoffel/Geronimus chain

PRs #134, #132, and #133 should be treated as one ordered construction:

```text
L-9314 one-anchor Geronimus extension
    -> L-13202 multi-anchor Christoffel ladder
    -> L-9316 source-allocated residual leverage budget.
```

The duplicated one-anchor statement `L-13201` should become an adapter or
corollary after its dimension-specific rank-one vectors are fixed. The final
leverage checker must bind one immutable source-allocation manifest so a physical
residual factor cannot be charged twice.

## 2. Hardy evaluation duality

The reciprocal-Hardy residual bound of `L-14303` and the zero-evaluation
obstruction of `L-15304` are dual uses of the same Hardy-strip evaluation RKHS:

- `L-14303` bounds the dual norm of an actual residual after quotienting the
  target direction;
- `L-15304` lower-bounds the distance from a packet to small-tail radical
  truncations through certified evaluations.

This suggests that the proof-facing low-packet split should use generalized
singular values in the Hardy metric rather than an ordinary Euclidean SVD. The
resulting near-kernel/visible decomposition can then be inserted directly into
`L-14317` for the complement leverage cap and `L-14308` for the finite Schur
composition.

This is a proposed architecture, not a proved uniform conditioning theorem.

## 3. Dual finite semidecision ledgers

`T-14201/T-14202` provide a finite negative-witness search that is complete under
a dense mesh schedule. `L-14316/L-14317/L-15305` provide finite lower-floor
components. These should share one immutable source/support/normalization ledger.

The joint ledger would enforce the distinction:

```text
negative finite witness
    -> genuine ambient negative by direct test inclusion;

positive finite compression
    -> no ambient conclusion without the complement and tail certificates.
```

This connection is operationally important because it prevents the two finite
directions from being treated symmetrically when their variational implications
are opposite.

## 4. Serious resolution architecture

The strongest reviewed positive architecture is:

```text
T-14302 cofinal lower envelope
    + L-14317 ambient packet-complement floor
    + L-15304 Hardy zero-evaluation split
    + exact radical tail on the near-kernel
    + L-15305 visible-block zero Gram minus complete tail
    + L-14308 block Schur composition.
```

The missing theorem is a cofinal, source-bound rate simultaneously controlling:

1. complete symbol/packet production;
2. radical near-kernel capture and conditioning;
3. all off-line-compatible omitted-zero tails;
4. complement coercivity and cross residuals;
5. directed assembly errors.

This is a serious research path, not a completed proof. In particular, the
visible-block omitted-zero estimate must remain valid in the presence of a
hypothetical off-line zero; it cannot import RH through the tail gate.