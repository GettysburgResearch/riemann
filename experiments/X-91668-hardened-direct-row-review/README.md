# X-91668 — Hardened direct-row review replay

This standard-library replay supports `L-91668`, `L-91669`, and the algebraic
shell of `T-91655`.

Run from the experiment directory:

```bash
python3 verify.py \
  --manifest ../../integration/2026-08-14/t91655-dependency-manifest.json \
  --json results/verification.json
```

Expected:

```text
PASS_HARDENED_DIRECT_ROW_REVIEW_PACKET
proof object: 669a507b06a5720c18968abad812c2572d9e5e595393d2d0b27d6e530169f88d
```

## What is replayed

The checker deterministically reconstructs every squarefree source index at
six physical endpoints through `120000`.  It verifies:

```text
unique P_61 Boolean label;
strictly ordered rough-prime factors;
unique stopping/current ownership;
no source atom in two labels;
exact least-prime recursion edge structure;
exact branch coefficient sum;
same-index ordinary and detail replacement algebra;
terminal target-mass telescope;
all-depth terminal debt <= 2 root target;
rejection of source-fraction weighting of an unrelated signed deficit;
complete dependency-manifest syntax and frozen SHAs.
```

Retained structural counts:

```text
labelled squarefree source records: 121696
least-prime recursion edges:        126638
stopped source records:              76979
finite P_61 records:                  6989
current rough-frontier records:      37728
ownership digest:
88e402b38d9822d806a5471f89beef97433b82c9ecda10c601ba0e98b20a46cf
```

## Scope firewall

The replay does **not** replace the frozen directed Hall-prefix and
normalized-row certificates.  It does not rerun the global fixed-67 analytic
proof, which has its own exact replay in `X-91666`.  It also does not rerun the
external Mellin contour, prime-square asymptotic, or Landau theorem.

The result deliberately records:

```text
actual_frozen_hall_cells_replayed_here = false
endpoint_contour_replayed_here          = false
rh_established_by_replay                = false
```

A passing replay means the new source-ownership and ledger shell is internally
consistent.  It is not an independent acceptance of the complete RH proposal.
