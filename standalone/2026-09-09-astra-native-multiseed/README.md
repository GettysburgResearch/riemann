# NM26: three small native generators, one genuine zeta obstruction

**Proposed component proofs. RH and the complete growing-horizon energy bound
remain UNPROVED. Independent mathematical and code review required.**

This pass directly tests feedback on the native floor residual. A fixed balanced
seed has recurrent auxiliary zeros which defeat every one-variable polynomial
feedback with the required normalization. We then construct THREE explicit
finite native seeds which eliminate all common auxiliary zeros. Each has full
error below0.02, exact Mobius prefix through2, balance0, derivative1, center-2.
Their supports are at most16,24,81.

The new bounded source identity is h_j=d*kappa_j, where kappa_j is a fully
specified compact signed measure. The joint closed space of ALL real causal
translates is precisely the original factorial-source space: its only shared
inner obstruction is the actual zeta Blaschke factor, not an added seed factor.
This does not prove that factor is constant, nor bounded synthesis coefficients.

An actual simultaneous-phase estimate also shows no bounded analytic Bezout
inverse for a fixed bank, and quantifies the coefficient cost of multivariate
polynomial feedback. A subpower full-energy construction is still missing.

Reading path: PROOF.md, SEED.md, ATTEMPT.md, then SOURCES.json and VALIDATION.md.
Local theorem labels NM1--NM4 are not canonical acceptance identifiers.
Classical almost periodicity, Hardy cyclicity and Nyman--Beurling mechanisms
are credited; no external novelty/priority determination is claimed.

The seed is a self-contained extraction from the LOCAL NJP26 packet, not a
claim that its entire previous handoff is now resident. Its full norm is freshly
reconstructed by direct floor summation and a pairwise-gcd period mean. All
1,048,575 required cells and the analytic infinite tail are covered. The finite
checks do not machine-prove analytic domain or feedback theorems.

Run from this directory:

    python -I -S -B verify.py --check result.json
    python -I -S -B -O verify.py --check result.json
    python -I -S -B verify.py --inventory-only

`--emit` is producer-only, not authenticated acceptance. No parent campaign,
full checkout/build, Lean proof, actual zero calculation or remote CI is claimed.
