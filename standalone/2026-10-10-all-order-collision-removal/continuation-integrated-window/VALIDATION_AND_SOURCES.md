# Validation, source boundaries, and review status

Date: 2026-10-10. Parent: PR #916 at `8d49acb264577f63374358c33636ebe8e05ccf70`. All new material is confined to `continuation-integrated-window/`.

## Executed in this session

From this directory:

```sh
python -I -S -B check_integrated_window.py --write result.json
python -O -I -S -B check_integrated_window.py --check result.json
```

Both executions succeeded and stdout was byte-identical. Each reconstructed 32,082 explicit successful predicates and rejected three deliberately false algebraic claims. The recorded counts are in result.json. A separate copy of the JSON with its total count incremented was rejected by full reconstruction with exit status 2 and message `stored result differs from full reconstruction`. `python -m py_compile` also succeeded. No bare Python assert is used as an acceptance gate.

The finite checks cover: local inverse coefficients; the sixth-root field and zero masks; exact rational window moments through order 30; finite convolution products with their exact scaled remainder; the window-zero multiplicity lattice; integrated balanced comparisons on a logarithmic grid; exact prime-removal identities and weighted norm inequalities; and rational exponent envelopes for the newer sieve and moment extraction.

The norm fixtures use a FREE MONOID with three generator norms 8,16,32, and all 343 assignments of a sixth root or zero to those generators. These are not three prime ideals of the Eisenstein field. The purpose is to test algebra and dilation bookkeeping under literal nonunit zeros. The discrete window is a finite fixture, not numerical evaluation of the infinite smooth window. The infinite window properties and measure-space inequalities are established in the written proofs, not inferred from this finite checker.

## Sources actually inspected

1. `GettysburgResearch/riemann` PR #916 at the exact parent above. In particular `continuation-balanced-closure/BALANCED_CLOSURE.md`, including its inverse identity, finite-envelope comparison, fixed cutoff and row-range boundary. The new proof restates and proves its needed kernel identities, and changes the norm argument to the joint row/scale measure.
2. PR #917 at `6b4723042b3d250024eef45cb1924f88f28e902c` and PR #919 at `9b04a887e171b3104a66cf57296ce5b0b2920d78`: PR metadata and summaries only. Their complete proofs and independent-review claims are NOT imported here. They motivated avoiding duplication of the already announced averaged-moment route. Our extraction is independently proved from the exact single-prime identity.
3. Alexandre de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, October 2, 2026: https://arxiv.org/html/2610.04045v1 . Inspected Theorem 1.1 and Sections 2.2-2.5, including both power-free index conditions, fixed construction data, zero extensions and reciprocity. The full recursion proving that theorem was not independently reconstructed. The adapter and exponent arithmetic are supplied in OPTIMAL_SIEVE_AUDIT.md. The main integrated criterion does not depend on this external theorem.
4. Juan Arias de Reyna, *An infinitely differentiable function with compact support: Definition and properties*, arXiv:1702.05442: https://arxiv.org/abs/1702.05442 ; and *Arithmetic of the Fabius function*, arXiv:1702.06487: https://arxiv.org/abs/1702.06487 . Bibliographic/abstract information identifies the classical window construction. All properties needed in the new argument are proved directly in Section 5; no unexplained normalization is imported.
5. Classical fixed-field prime ideal counting, ideal divisor bounds, Holder, Minkowski, Fourier inversion and Mellin continuation are used with their stated domains. They are not claimed as new results. No zero-density estimate or RH-conditional prime theorem is used in the principal integrated implication.

## Self-audit: the load-bearing boundaries

- The row measure is fixed while applying Holder and changing the scale variable. It is not silently replaced by the natural curve H=X^h.
- Every finite-horizon integral vanishes below a fixed positive scale, so absorption does not assume the desired growth bound.
- The prime set used for extraction is fixed at the outer horizon. Prime ideals are outside S and distinct primary sixth powers are included in the complete row set.
- The smooth window is compact despite having a zero-free Mellin transform in a half-plane. Normal convergence of its infinite product excludes non-factor zeros there. No height-uniform inverse bound is inferred.
- The covariance retains its real part, original divisor allocations, phases and signs. Only a one-sided upper estimate is proposed. Its diagonal is proved small, not the off-diagonal.
- The external theorem is power-free, not all-row. The adapter explicitly restores sixth powers and the finite bad-prime part, preserving masks. The resulting generic obstruction is not a counterexample to the specified Mobius coefficients.

These items were checked by the authoring model. There was no independent agent/human mathematical review, fresh Lean build, full upstream analytic audit, full-repository validator, or proof of an infinite moment in this pass. Earlier validation records remain unchanged and are not enlarged by the new tests.

MANIFEST.json covers the six non-manifest release files with SHA-256 and Git blob identifiers. Its own hash is not recursively included. Files and hashes can authenticate the released finite objects; they do not turn the open covariance estimate into a theorem.
