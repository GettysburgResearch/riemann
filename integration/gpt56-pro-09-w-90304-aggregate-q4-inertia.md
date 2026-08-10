# Integration handoff — aggregate Q4 inertia after Claude cross-fertilization

Status: **full proposed composition; independent review required; RH not accepted**

Stacked on:

```text
PR #357
research/gpt56-sol/90300-claude-inertia-q4
```

New canonical claims:

```text
L-90304
  exact aggregate determinant/current elimination:
  tr(sum w K)_- <= |U|^2/[4(A-F)].

L-90305
  balanced compact Q4 physical block has polynomial negative inertia,
  independent of the RH-sensitive current energy.

T-90302
  complete proposed composition to the coefficient-one recurrence and RH.
```

Exact replay:

```text
X-90302-aggregate-inertia
classification:
PASS_EXACT_AGGREGATE_INERTIA_ELIMINATION

proof-object SHA-256:
11dd103d5c25fe22dc9dfbe81bd9e85a85f200ad1e066a2b02b2e0868aec171a
```

Load-bearing novelty:

```text
rowwise Schur/current control is not used;
physical aggregation is performed first;
the complete current energy stabilizes the determinant;
only source reserve, score, and signed second-current mean remain.
```

Review dependencies in order:

```text
L-90304 -> L-90305 -> L-90301/L-90303
-> PR #350 exact synthesis
-> PR #346 strict parity charge
-> PR #341 two-state reflected ledger
-> T-90302.
```

Mandatory firewalls:

```text
nonnegative physical weights;
common/zero source centering;
no row-dependent shear;
synthesis must commute with aggregation;
no reserve double spend;
all delayed gauges retained;
source multiplier must not cancel an off-line zeta zero.
```
