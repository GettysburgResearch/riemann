# T-108514 — An infinite family of purely expansion-side Ramanujan failures: GP(n,2), n >= 24

```text
Claim ID: T-108514
Status:   PROVED (three-piece proof, each piece independently
          adversarially verified SOUND with full certificate re-runs;
          exact Sturm certificates throughout, floats labelled
          reconnaissance only)
Created:  2026-08-31 (pass 3 continuation; capstone of the O-108006
          breach-side programme)
Programme: #763 (graph purity mechanisms)
Depends on: elementary linear algebra + exact Sturm; complements
          O-108006 and graphs/WITNESS16_STRUCTURE.md
Proof:    standalone/2026-08-31-gp-positive-family/PROOF.md (piece
          texts verbatim from the verified workflow record
          wf_70eda207-75f)
Machine:  certificates inside the proof; graphs/gp24_certificate.json
          (independent base-case corroboration); the verifiers'
          additional exact runs (identity for all n = 5..40; GP(23,2)
          below threshold; fresh end-to-end n = 25, 26)
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary)

For every `n >= 24`, `GP(n, 2)` is a simple connected cubic graph with
`lambda_2 > 2 sqrt 2` and `lambda_min > -2 sqrt 2`: an INFINITE family
whose Ramanujan failure is purely expansion-side. The threshold is
exact (`GP(23,2)` certified below), the negative end never breaches at
ANY `n >= 5` (block minimum > -2.421), and `lambda_2 -> 3`.

Proof skeleton: (1) rotation-equivariant Fourier decomposition:
`spec(GP(n,2)) = union_j spec [[c_j, 1], [1, c_j^2 - 2]]`,
`c_j = 2cos(2 pi j/n)` (complete proof + exact trace-identity
certificates; the verifier confirmed the identity for every
`n = 5..40` independently); (2) `F_-(c) > -2 sqrt 2` on all of
`[-2, 2]` by two sign-conditioned squarings reduced to integer-Sturm
root-freeness; (3) `F_+` strictly increasing on `[0, 2]` via an exact
derivative identity with manifestly positive minorant, plus the base
inequality `F_+(193/100) > 2 sqrt 2` by a pure integer comparison
(difference 176933570751), plus `193/100 < 2cos(pi/12)` via the
minimal polynomial `x^4 - 4x^2 + 1` — and Piece 3 is self-contained
even without (1), using an explicit cosine eigenvector.

## Why it matters for #763

O-108006's two-failure-directions story is now complete with proofs at
both poles: the capped-ladder families pass through a FINITE
positive-only window (exact certificates, WITNESS16_STRUCTURE.md)
while GP(n,2) realizes a PERMANENT positive-only regime — the
mechanism dichotomy (near-bipartite corridor vs block-bounded
lambda_min) is exhibited by explicit, fully certified families. In the
mechanism-dictionary language of L-108005: the spectral-gap supplier
can fail on one side only, forever, and the minimal such failures (16
vertices, transient) and the stable such failures (this family) are
structurally different objects.
```
