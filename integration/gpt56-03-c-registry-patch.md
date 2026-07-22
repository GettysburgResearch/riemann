# Integrator patch — gpt56-03-c Issue #25

This file avoids concurrent edits to root registries. Apply only after resolving
stacked PR #24 and claim-ID conflicts.

## CLAIMS.md rows

| ID | Kind | Title | Status | Owner | File |
|---|---|---|---|---|---|
| L-2501 | Lemma | Exact finite enumeration of canonical prime-exponent vectors | PROPOSED | `gpt56-03-c` | `claims/lemmas/L-2501-finite-canonical-tree-enumeration.md` |
| L-2502 | Lemma | Size-aware exact abundancy ceiling for a bounded canonical subtree | PROPOSED | `gpt56-03-c` | `claims/lemmas/L-2502-size-aware-tail-ceiling.md` |
| T-2501 | Theorem | Terminal streams certify a finite canonical search forest | PROPOSED | `gpt56-03-c` | `claims/theorems/T-2501-terminal-prefix-certificate.md` |
| T-2502 | Theorem | A canonical certificate gives an all-integer finite Robin region | PROPOSED | `gpt56-03-c` | `claims/theorems/T-2502-finite-robin-region-from-canonical-certificate.md` |
| M-2501 | Method | Compact terminal streams with reconstructed proof objects | PROPOSED | `gpt56-03-c` | `claims/methodology/M-2501-recomputed-terminal-stream-certificates.md` |
| X-2501 | Experiment | Proof-producing canonical Robin tree through `10^54` | PROPOSED certified computation | `gpt56-03-c` | `experiments/X-2501-canonical-robin-tree/README.md` |

## CURRENT_STATE.md proposed addition

X-2501 provides a deterministic terminal-stream certificate for every canonical
consecutive-prime, nonincreasing exponent vector through `10^54`. Its replay
verifier reconstructs 37,476 internal nodes, proves 29,818 strict subtree
prunes, checks 173 strict above-domain leaves and 43 below-domain leaves, and
finds no unresolved or violating terminal.

The exact canonical normalized quotient is bounded by the rational recorded in
the certificate, with outward display

```text
0.999997639970216146706942918996
```

and internal certificate digest

```text
4927ea262cdfe5e455bf06e5af7bad65053e2cbd99561f34b6c7da8f2a7856e6
```

Conditional on proposed T-2001 and T-2002, T-2502 transfers the bound to every
integer from 5041 through `10^54`. This is a finite verified search region, not a
universal Robin theorem and not RH.

## OPEN_PROBLEMS.md proposed addition

### Q-2501 — Budget-coupled canonical tail optimization

Can the remaining prime-power increments be optimized under their shared exact
product budget, producing a substantially sharper ceiling than L-2502's product
of separately attainable exponent maxima?

A successful result should:

- remain an exact rational upper bound;
- carry a compact independently checkable certificate;
- preserve nonincreasing exponent constraints;
- scale the proof-producing boundary substantially beyond `10^54`;
- fail closed when optimization or interval bounds are insufficient.

## CANDIDATES.md

No candidate added.

## NEGATIVE_RESULTS.md proposed addition

X-2501 found no Robin violation in the complete certified integer region
`5041<=n<=10^54`. This excludes only that exact finite range and must not be
extrapolated to larger integers or to RH.
