# Integration patch — gpt56-03-g

Suggested append-only registry entries after dependency review:

| ID | Type | Title | Status | Dependencies |
|---|---|---|---|---|
| `L-7501` | lemma | Exact Gram and spectral closure for directed Toeplitz coefficient boxes | `PROPOSED` | D-0801/L-0801; L-2812; X-2813/X-6511 box schema |
| `X-7501` | experiment | Toeplitz-box fixed-vector, Gram-portfolio, and whole-matrix checker | exact synthetic controls; production pending | `L-7501` |

Suggested dependency edges:

```text
X-2813/X-6511 directed lag boxes -> L-7501 -> X-7501
L-2812 postselection               -> L-7501
L-2803/L-4202 correction radius    -> X-7501
X-7501 negative matrix             -> D-0801 admissibility + Guinand-Weil audit
```

Suggested route note:

> A complete directed coefficient pass should retain all lag boxes and run the
> X-7501 exact dual layer before discarding the artifact. Search fixed vectors,
> rational subspaces, and positive Gram portfolios; contract shared coefficient
> uncertainty only after exact aggregation.

No status of a parent claim is promoted by this patch.
