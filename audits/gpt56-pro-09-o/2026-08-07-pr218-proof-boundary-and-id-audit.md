# PR #218 proof-boundary and claim-ID audit

Date: 2026-08-07  
Frozen head: `5fade63daa279fe6003b66f3763ca3bf05fd912d`  
Status: **AUDIT / INTEGRATION BLOCKER; NO RH CLAIM**

## 1. Duplicate claim identifiers

PR #218 contains the following duplicate IDs on distinct files:

| ID | First file | Second file |
|---|---|---|
| `L-20208` | `L-20208-curvature-corrected-renormalized-prime-polygon.md` | `L-20208-fejer-ramp-half-knot-barrier.md` |
| `L-20209` | `L-20209-dual-bregman-square-gate.md` | `L-20209-prime-ramp-autocorrelation-duality.md` |
| `L-20210` | `L-20210-shrinking-cell-taylor-curvature-normal-form.md` | `L-20210-stable-infinite-half-knot-barrier.md` |
| `L-20211` | `L-20211-exact-dyadic-block-prefix-normal-form.md` | `L-20211-optimal-endpoint-fejer-autocorrelations.md` |
| `L-20212` | `L-20212-dyadic-cell-endpoint-stitching.md` | `L-20212-pole-descent-safe-filter-cone.md` |
| `L-20213` | `L-20213-selberg-hankel-dual-certificate.md` | `L-20213-transcendental-pin-prime-localization.md` |
| `L-20214` | `L-20214-exact-archimedean-curvature.md` | `L-20214-generic-transcendental-pin.md` |
| `T-20206` | `T-20206-curvature-corrected-prime-transport-rh-criterion.md` | `T-20206-transcendental-pinned-fejer-rh-criterion.md` |
| `T-20207` | `T-20207-field-separating-algebraic-pin.md` | `T-20207-shrinking-cell-tiling-rh-criterion.md` |

No public registry or integration packet may cite these IDs without the complete
file name and frozen blob identity. Before merge, one of the two concurrent
families must be renumbered atomically across theorem bodies, reports,
experiments, SHA ledgers, and PR text.

## 2. Sign-correction dependency

`R-20202-terminal-flat-filter-sign-reversal.md` records the exact identity

```text
D_r(t)-M^-2 D_(Mr)(t) = -M^-2 D_M(r t).
```

Any statement using the opposite sign is refuted, even if a later file reuses a
nearby theorem number. The original Haar theorem `T-20201`, the single `r`-adic
criterion `T-20203`, and the exact Fejer--Gram factorization are logically
separate from this correction.

## 3. Archimedean curvature wording

The exact formula is

```text
F''(t)=exp(t/2)-exp(-5t/2)/(1-exp(-2t)).
```

It is not positive near zero. The valid global statement is

```text
F'''(t)>0,
```

so `F''` is strictly increasing. Therefore

```text
H_r''(T)=F''(T)-F''(T/r)>0
```

for `r>1`. Any proof that invokes global positivity of `F''` rather than its
strict monotonicity requires repair. The renormalized convexity conclusion
survives after that repair.

## 4. Finite-versus-global boundary

The exact synthetic checkers `X-20201`--`X-20204` verify algebraic identities,
not:

- the imported screw/Laplace normalization;
- Landau's one-sign continuation in the stated normalization;
- a cofinal prime inequality;
- complete monotonicity of the real-axis function;
- the critical signed near-resonance estimate;
- RH.

Likewise, twelve positive ordinary Hankel levels and positive ordinary
S-fraction coefficients are reconnaissance only.

## 5. Current safe integration order

A review should proceed by file, not by duplicated ID:

1. `T-20201-single-haar-renormalization-rh-criterion.md`;
2. `T-20203-critical-mesh-r-adic-screw-criterion.md`;
3. `L-20204-r-adic-fejer-gram-factorization.md`;
4. `R-20202-terminal-flat-filter-sign-reversal.md`;
5. the dyadic transport files, each cited by full name;
6. the endpoint/field-pin files, each cited by full name;
7. `T-23001` and its exact gap `L-23002`.

## 6. Status conclusion

PR #218 contains several serious proposed global reductions, but the branch is
not publication-ready as one theorem stack. Duplicate IDs, a recorded sign
refutation, and the unresolved critical-correlation gate must remain visible.
No current file proves RH.
