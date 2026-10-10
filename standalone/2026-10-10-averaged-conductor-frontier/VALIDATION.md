# Validation and proof boundaries

Date: 2026-10-10. This packet contains proposed mathematical reductions and source audits. Neither a successful file check nor a scoped proof review establishes the remaining inverse-moment arithmetic estimate, a new zero-free boundary, or RH.

## Mathematical review

| Item | Independent evidence | Scope |
| --- | --- | --- |
| Small-gcd and conductor combination | SMALL_GCD_CONDUCTOR_REVIEW.md | Exact row masks, cubic overlap tail, cutoff optimization, polynomial split before smoothing, positive conductor accounting, real signed remainder, strict domain reduction, and averaged extraction |
| Cofinal averaged higher-order criterion | COFINAL_AVERAGED_REVIEW.md | Signed inequality from the smooth residual square, one-sided integration, cutoff cost, fixed-character cofinal quantifiers, finite exclusions and contragredient coverage |
| PR #917 scale-averaged source | SCALE_AVERAGED_SOURCE_AUDIT.md | Distinct sixth-power row copies, moving cutoff, weighted causal inverse on finite intervals, low-scale forcing and holomorphic Mellin extraction |
| PR #916 collision kernel and moment frontier | ALL_ORDER_KERNEL_AUDIT.md | Explicit enlarged-S hypothesis, positive-kernel singularity, critical logarithmic mass, fixed-row-range rectangles, weak hierarchy, and limits of an A2 application |
| Publication overview | README_REVIEW.md | Agreement with the frozen proofs, conditional numerical thresholds and the distinction between the two routes' analytic dependencies |

Authors and reviewers of each new main reduction are distinct AI research agents. Their reports state exact SHA-256 bindings. The root agent also read the complete new mathematical notes and checked the main normalizations. These are bounded AI-agent reviews, not human peer review, repository integration approval, or Lean verification.

The small-gcd fourth-moment route uses classical character sieves, elementary conductor accounting and the pinned averaged extraction. It does not require the imported native inverse second moment. The higher-order one-sided periphery does require that second moment; an optional exponent below one also requires the stated uniform pointwise bound. At b=1 only elementary counting is added to that second-moment premise. The fixed universal Mellin test is a declared source input in both extraction routes.

The kernel audit has separate independent subsection reviews: the mapper checked the local kernel, mass and norm-transfer sections, while the formalization reviewer checked the moment-frontier extraction and cofinal quantifiers. Its comparison with the A2 interface refers to the exact INTERFACE_COMPARISON.md object in SOURCE_LOCK.json; the authoring-directory locator preserved in the audit identifies that same frozen parent proof.

## File and publication verification

The publication pass checks the following against the frozen bytes:

- Every packet manifest entry matches its actual byte length and SHA-256 hash. MANIFEST.json covers every packet file except itself.
- Each of the four adjacent source snapshots is byte-identical to its recorded source Git object. The source manifest records both SHA-256 and Git blob identities.
- Every SOURCE_LOCK.json entry matches the exact source commit and path, byte length, SHA-256 and Git blob identity.
- Every proof hash stated in a new independent review matches the copied proof file. Source-audit bindings are also compared with the exact snapshots and inherited source objects.
- Authored Markdown has paired inline and display math delimiters, valid relative file links, and no unexpected control bytes. Source copies are preserved verbatim, and their original relative-link context is documented in sources/README.md.
- JSON parses, text files end in a newline, and the staged patch passes git diff --check.
- The patch changes only this new packet and root README navigation. Previous source and proof packets retain their exact bytes.
- The published commit has the intended sole parent and staged tree. Every changed remote file matches the staged payload byte-for-byte, and the manifest is checked again at the remote commit before publication is reported complete.

The source lock describes immediate dependencies and audit comparison objects. It is not a claim to have rebuilt every imported theorem, rechecked every reference in every adjacent packet, or transferred prior source acceptance automatically.

## Computation and conclusions not claimed

No new numerical moment experiment, zero census, certified interval computation, finite-field theorem test, or Lean build was performed for these combinations. The exact local arithmetic checks in PR #915 and the separate checkers in PR #917 retain their original scopes. They were not relabeled as numerical evidence for a new asymptotic moment bound.

The signed fourth-order average remains unproved. The general cofinal criterion allows sublinear losses but does not establish them. The collision kernel supplies logarithmic transfer when the required rectangular bound is already available; it does not generate that bound from the current anisotropic estimate. Constants need not be uniform as the order grows, so the qualitative cofinal implication supplies no explicit height-dependent shrinking band.
