# Integration patch — zero-evaluation split of the positive low block

This append-only handoff does not edit concurrent global registries.

## Proposed claim registrations

| ID | Kind | Title | Status | Primary dependency |
|---|---|---|---|---|
| `L-15303` | lemma | Growing exact Hermite radical packets | `PROPOSED` | base Gaussian radical-tail theorem |
| `L-15304` | lemma | Zero-evaluation obstruction to full-packet radical repair | `PROPOSED` | global zeta-factor radical identity; Hardy evaluation bound |
| `M-15301` | methodology | Zero-evaluation-split lower-floor pipeline | `PROPOSED` | T-14302, L-14308, L-15304 |
| `O-15301` | observation | July 2026 positive-path convergence audit | `LITERATURE_AND_REPOSITORY_AUDIT` | located primary sources and current PR stack |

## Proposed experiment registration

| ID | Path | Classification |
|---|---|---|
| `X-15302` | `experiments/X-15302-zero-evaluation-obstruction/` | exact rational singular-floor and radical-distance checker |

## Withdrawn duplicate claims

The first version of this branch independently derived a three-mode source
repair and auxiliary-factor Hurwitz criterion. The active base branch landed
the same results in more developed form. The duplicate `L-15302`, `T-15301`,
and `X-15301` files were therefore removed rather than competing for registry
space.

## Base registry defect requiring repair

PR #152 currently has distinct files sharing:

```text
L-14312
L-14313
T-14303
X-14307.
```

Review `4827072827` requests append-only ID reallocation and dependency updates
before integration.

## Exact finite fingerprint

```text
X-15302 synthetic obstruction verification
475f0f5955170c08c6cf2477d0d60f90dde71ea3539e21593ea8704bcf87d054
```

## Dependency graph

```text
complete finite low-symbol packet U
        + proof-grade certified zeta zeros Z
        -> exact evaluation map V_Z|U
        -> rational near-kernel R plus visible block V

R
        -> growing exact Hermite/Gaussian radical packets (L-15303)
        -> small localized form block and cross residual

V
        -> direct finite lower certificate

R + V + ambient complement
        -> L-14308 block Schur floor
        -> symbolic cofinal envelope
        -> T-14302
        -> RH
```

## Exact obstruction

If a normalized low-packet vector `u` is approximated by a localized radical
truncation `k` with tail norm at most `epsilon`, then for a certified zero set
`Z`

```text
||u-k||_tau >= sigma_Z(U)/C_Z - epsilon.
```

Thus only the small-singular evaluation near-kernel can have a vanishing
radical-repair angle.

## Located literature

```text
arXiv:2106.01715  Connes--Consani
arXiv:2511.22755  Connes--Consani--Moscovici
arXiv:2606.09096  Suzuki
arXiv:2603.07407  Kulikov
arXiv:2603.23832  Kulikov--Dam Larsen
arXiv:2607.23016  Azimifard
```

## Review order

1. `L-15304`
2. `X-15302/verify.py`
3. `L-15303`
4. `M-15301`
5. `O-15301`
6. report
7. corrected Issue #156

## Promotion boundary

- The finite rational obstruction checker is exact.
- No Riemann-data low packet or evaluation matrix exists yet.
- The growing Hermite block is not proved to span the certified near-kernel.
- The evaluation-visible block has no direct positive floor yet.
- No cofinal lower envelope and no proof of RH are claimed.