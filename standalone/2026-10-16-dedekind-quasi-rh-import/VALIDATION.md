# Validation and scope of this import

## Source and access

The author-maintained formal repository was read through the connected GitHub tools and pinned to `09afbb4ce6570c1615d58509dc197fc9f0956b7d`. Thirteen selected files were reconstructed locally and authenticated against their actual upstream Git blob IDs, then copied unchanged into this repository. The full selected-source subtree is:

`8135714e86e39e70ae116bd28669050a3c310b9d`.

This tree was calculated from the local bytes and matched the newly stored GitHub tree. Initial transport omitted three terminal newlines; the mismatch was detected by the whole-tree comparison and corrected before committing. No source theorem text was changed. UPSTREAM_LOCK.json also records SHA-256 and byte lengths.

The Hexagon landing metadata was available through web search. Direct manuscript, version, and source downloads failed. No manuscript PDF, LaTeX source, PDF screenshot, or manuscript-version diff was obtained. In particular the 13 October formal pin is not represented as a verified formalization of the advertised 14 October v2.

## Checks actually run

The released `checks/check_import.py` was run with ordinary Python and with `python -O`. Their JSON outputs matched each other and CHECKS.json byte for byte. The checks cover:

- All thirteen copied source identities and the declared Challenge/Solution/build interface. The two intentional Challenge placeholders are disclosed; token checks are not Lean elaboration or proof-term verification.
- 676 exact Gaussian-rational local configurations for the correction, extracted numerator, and convex-combination nonzero condition. Zero phases are included. These are local algebra tests, not finite-field sextic character or native-row computations.
- Three exact finite Mellin/dilation identities with distinct prime labels of norms 7, 7, and 25. Equal norms remain separate before products are aggregated.
- Six rejected false substitutions: omitted extraction factor, omitted q^-1 weight, a local zero outside the valid disk, omitted dilation weight, wrong dilation power, and an added coprimality restriction.
- Rational reconstruction of the published 31/32 exponent, the 1937/2000 fixed-comparison floor, the 1/4000 gap, the two Euler-product convergence thresholds, and the linear higher-moment excess.

The reproduction shell script passed `bash -n`. Its Git/network/Lean execution was not performed: the container could not resolve the remote hosts and had no `lake` executable. The script is an explicit future reproduction recipe, not an existing success receipt.

## Mathematical boundary

RENORMALIZED_CERTIFICATE.md contains the written proofs of local-to-global numerator normalization, degree-explicit bounds, the exact weighted sixth-dilation transform, and the conditional zero-exclusion implication. They use ordinary convergent-product and Mellin arguments. Applying the criterion to the paper is explicitly conditional on the pinned actual-source identity, flatness, and continuation semantics.

The finite checks do not prove these analytic arguments. Proof, implementation, and reconstruction have the same author. No independent agent or human referee, full Lean build, comparator execution, transitive axiom audit, external theorem reconstruction, or repository-wide CI run is claimed.

The unproved estimate is OPEN-R: the actual renormalized signed probe must have growth Z^(1/2+epsilon) for every epsilon>0. The source's available bound remains 31/32. No full native moment or RH conclusion is asserted by this import.

## Repository publication

The branch starts at main commit `f99d9e3908dde4865377c75d9ca051c1f545bf4f`. Only this new standalone import directory is added. The other research PRs are cited at immutable commits and are not merged. The publication is a proposed draft, not an update to the integrated scientific status.

Publication uses GitHub Git-data actions and tree read-back, rather than a claimed clean full-repository clone. The final immutable commit binds the authored report, source map, proof note, diagnostics, and copied source. No font, credential, private account data, or generated proof-of-RH certificate is part of the packet.
