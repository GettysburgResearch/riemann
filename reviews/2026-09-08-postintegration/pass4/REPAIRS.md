# Current extraction repairs and qualifications

These repairs apply prospectively to the readable integrated statements and accepting entrypoints. Original research files and all earlier review records remain unchanged. The six items are not six failed mathematical programmes.

## R01 — rational-capture minimum brackets (inherited)

Source: #803, `db175de165a9077e709b1cb482998171ffc0c6e7`, `standalone/2026-09-08-rational-residual-capture/PROOF.md`, blob `e7b0dfd9db3a114962ed610c9b19900df135b58b`.

The three tight balance-only minimum brackets use the separately minimized lower and upper comparison forms in equation (18), not equation (8) alone. State that construction explicitly. Published pass-three independent KKT reconstruction supports the printed brackets. Keep these one-jet feasible classes separate from RN's two-jet classes. Neither finite decrease proves a growing-prefix estimate.

## R02 — balanced lift: energy is a squared norm (inherited)

Source: #805, `602d7ddf9dbd2ba79bd6cada149772111ca72150`, `standalone/2026-09-06-astra-balanced-lift/PROOF.md`, blob `5fb7798a5d3ade45ec761e24744593cbc056a369`.

The explanatory lower growth of order `sqrt(M)` concerns `||F||^2`, not `||F||`. The corresponding unsquared lower growth is order `M^(1/4)`. Preserve the displayed parallelogram argument and its sign selection. This is a counterfamily of nearly optimal detail, not a lower bound against the unique exact native minimizer.

## R03 — terminal harmonic first interval (inherited)

Source: #805 at the same head, `standalone/2026-09-06-astra-terminal-endpoint/PROOF.md`, blob `138dd98c2f8f32b8979926593443986f98f263c5`.

When `M` is only an upper support bound, write the prescribed interval `(0,1/M)` rather than asserting that it is the entire first active mesh cell. The current is constant there and its stated contribution is valid. The actual first active cell can be longer. The terminal-family fourth-power-grid theorem is unchanged.

## R04 — N=32 divisor example (inherited)

Source: #825 at `e4a486d3fd4009e3722e9e93f35710b834fbd195`, PR description and finite inverse example.

There are **eleven** prime bases through 31, not ten. All 65 allowed prime-power edges belong to the finite form. The pass-two independent inverse certificate used the correct graph; this is a count correction, not a changed inverse value.

## R05 — domain of trial maps for the infinite Schur extension (new)

Source: #825 at the same head, `standalone/2026-09-08-astra-divisor-gap/APPLICATION.md`, blob `debeac1969d146ea8c31ffc9a88b68713ecea8b6`, especially section 2 and its stated infinite-reservoir extension.

The finite-matrix statement is valid. For an unbounded positive self-adjoint operator on a fixed-prime infinite reservoir, the wording “any bounded proposed solve” is insufficient to define `AY` and a Hilbert-space residual. The trial map must take values in the operator domain, not merely the form domain.

### Readable repaired statement

Let `U` and `H` be Hilbert spaces, let `A` be self-adjoint on `U` with `A >= gamma I` for `gamma>0`, and let `B:H->U` be bounded. Let `H_0:H->H` be bounded self-adjoint. Suppose `Y:H->U` is bounded, `Y(H) subset Dom(A)`, and `AY` is bounded. Define

\[
 R=B-AY,\qquad V=Y^*B+B^*Y-Y^*AY,
 \qquad S=H_0-B^*A^{-1}B.
\]

Then

\[
 B^*A^{-1}B-V=R^*A^{-1}R,
 \qquad H_0-V-\gamma^{-1}R^*R\preceq S\preceq H_0-V.
\]

In finite dimension the domain condition is automatic. On an infinite reservoir it is a real requirement. One may alternatively formulate a form-domain/dual-residual theorem, but that is not the strong Hilbert-residual formula above.

### Proof route and necessity of the qualification

The lower bound makes `A^{-1}` bounded with `0 <= A^{-1} <= gamma^{-1}I`. The domain assumption gives `A^{-1}R=A^{-1}B-Y`; expansion proves the exact identity, then the inverse bound gives both Loewner inequalities. The requirement that `AY` be bounded also follows from the closed graph theorem when `Y` is bounded and maps its entire domain into `Dom(A)`, but stating it explicitly prevents an ambiguous residual contract.

Already in the literal one-prime infinite reservoir, the normalized mean-zero eigenvectors have eigenvalues comparable to `j`. The vector `v=sum_(j>=1) j^(-3/2)e_j` is in the Hilbert space and in the form domain, because `sum j^-3` and `sum j*j^-3` converge, but is not in `Dom(A)`, because `sum j^2*j^-3` diverges. The bounded rank-one map `Y:a->av` therefore has no `U`-valued residual `B-AY`. This is an explicit domain obstruction, not a failure of the graph gap or its finite certificates.

The corrected statement is ready for extraction at this scope. Do not silently install it as an already repaired author manuscript or infer an actual xi coupling from it.

## R06 — MW expected-receipt parsing (new, implemented at review boundary)

Source: #804, `0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad`, `standalone/2026-09-06-astra-mobius-work-resonance/certify.py`, blob `3d1e3b10135a8504a5d3639b507211014be7eecc`.

The original `--expect` path uses `json.loads(...) == result`. In both Python modes, actual CLI tests accept (a) a floating event count together with a Boolean first checkpoint and (b) duplicate event-count keys whose last value is correct. A changed numerical endpoint is rejected after recomputation. The evidence is [the original-parser probe](evidence/mw-original-parser.json).

This is a typed-receipt and duplicate-key weakness. It is **not** evidence of a wrong MW numerical bound. The full producer output matches the published result byte-for-byte and has a separate direct-integration reconstruction.

Use the new [replay.py](replay.py) for selected trusted replays. It checks the exact source inventory and immutable source blobs before compiling the consumed bytes, rejects duplicates, floats/nonfinite JSON, oversize/nonobject/symlink receipts, and compares canonical typed content against a fresh complete reconstruction. Boolean/integer aliases cannot pass that canonical comparison. Eighteen actual refusal cases and four pristine full replays pass in each mode. No privileged workflow is installed.

The original producer remains byte-preserved under `sources/MW/`. Replacing the author's CLI on its research branch is not part of this review. If that CLI is later promoted as a general accepting entrypoint, repair it there and review the delta; otherwise retain it as an archived producer and use this source-pinned review wrapper.
