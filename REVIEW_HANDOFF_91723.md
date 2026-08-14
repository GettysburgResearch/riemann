# Review handoff — factor-67 all-column reserve repair

## Placement

```text
repository:       gfreund123/riemann
base PR:          #476
base branch:      research/gpt56-pro/91692-triple-closure-proposal
base head:        9f16ce483954d4233b68ee09cb6bec47400aa3cc
successor branch: research/gpt56-pro/91723-factor67-all-column-reserve
```

The packet also reviews the later explicit compact reserve on PR #473 at

```text
71d6a859ea741fe035de709e8d10ed37301b778e
```

and uses its factor-67 constants only at their stated frozen scope.

## New result

`L-91723` notices that the published `177/K` finite-realization estimate uses
`q>=K`; it does not cover `2<=q<K`. The collar still feeds those columns
through multiples `jq>=K`.

Partitioning the finite mismatch by adjacent carry cells yields the exact
all-column bounds

```text
ordinary mismatch < 57/(2 q sqrt(K));
detail mismatch   < 171/(4 q sqrt(K));
collar+mismatch   < 971/(4 q sqrt(K));
relative error    < 129/sqrt(K).
```

One source-owned thinning

```text
tau_K=sqrt(K)/(sqrt(K)+130)
```

then leaves strict detail reserve

```text
Omega_X(q)/(sqrt(K)+130)
```

for every nonterminal physical column. It has equality-score cost below `4290`
and is stronger than the old `K/(K+178)` thinning for `K>=2`, so the terminal
proof is only improved.

## Replay

```bash
cd experiments/X-91723-factor67-all-column-reserve
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_FACTOR67_ALL_COLUMN_SQRTK_RESERVE
```

## Review order

1. `L-91723`
2. `O-91723`
3. `T-91721`
4. `X-91723`
5. report and dependency lock
6. frozen `L-91111`, `L-91691`, `L-91694`
7. the remaining factor-67 Hall/port/terminal/endpoint inputs

## Exact boundary

```text
small physical columns 2<=q<K              CLOSED ON FROZEN CARRY INPUT
all nonterminal detail/ordinary columns     CLOSED
terminal scaling compatibility              PROVED EXACT
additional score loss                       <4290
mass-weighted child contraction              IMPORT L-91694 / EXACT
full factor-67 stack                         RECONSTRUCTION REQUIRED
Riemann Hypothesis                           UNPROVEN
```
