# PR #500 live-marginal and replay-scope audit

Frozen PR: `#500` at `d73c1e7a1a482cac31581211a84db43cc34c824e`

## The theorem layer

`L-91850` is a valid abstract theorem once supplied with:

```text
actual Hall input measures E_s,O_s;
actual Hall coupling pi_s;
actual residual measure;
actual causal kernel C_s;
actual positive physical placements P_(a,s);
actual label-blind endpoint quantizer Q_X.
```

`L-91851` names those objects in the factor-67 setting but does not write the joint coupling \(\Gamma_X\) in terms of the live arithmetic data. In particular, the positive physical placement of the Hall row bonus is not instantiated.

## The replay layer

`physical_coupling.py` uses only synthetic data:

```text
hard-coded rational Hall masses;
arbitrary rational profile vectors;
synthetic tags 12 through 16;
a hard-coded 1/4,1/2,1/4 quantizer;
arbitrary signed error and Y4 vectors;
64 randomized abstract fixtures.
```

It does not read the frozen imported theorem files and does not calculate the actual Möbius atoms, target weights, component rows, Hall flow, rough monoid, endpoint density, or B-spline kernel.

## Owner-map bug

The validator rejects repeated owner values:

```python
if len(owners) != len(set(owners.values())):
    raise ContractError("duplicate first owner")
```

But a first-owner map is naturally many-to-one. Both `67` and `67*71` have the unique first owner `67`. The current test would reject a valid live source partition.

## Verdict

```text
abstract coupling theorem                  VERIFIED WITH FIXES
live arithmetic marginal                   UNPROVEN / GAP
current replay                             EMPIRICAL ONLY
claim that replay instantiates live data   FALSE
```

A valid successor replay must derive the certificate from the repository's arithmetic definitions and verify the actual source marginals and output row.
