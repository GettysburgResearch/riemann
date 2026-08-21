# Advertised `T-91651` deposit census

Cutoff: `2026-08-13T17:18:44Z`

Frozen heads:

```text
main     9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
PR #399  9deddaa92c1b709b052e0994bd9a6dc0bb307366
PR #439  1546d866cdedb8a13b55b2deb154e47e0559e808
PR #424  9f2ea36fd295efb117967edf8288f0e10d6fa716
```

## Expected files from the supplied proposal summary

```text
claims/refutations/R-91650-*.md
claims/refutations/R-91651-*.md
claims/refutations/R-91652-*.md
claims/lemmas/L-91650-*.md
claims/lemmas/L-91652-*.md
claims/lemmas/L-91653-*.md
claims/lemmas/L-91654-*.md
claims/lemmas/L-91655-*.md
claims/lemmas/L-91656-*.md
claims/theorems/T-91650-*.md
claims/theorems/T-91651-provenance-causal-packet-factor54-resolution-proposal.md
claims/observations/O-91650-*.md
reports/gpt56-pro/2026-08-13-pr431-counterexamples-and-two-route-repair.md
claims/lemmas/L-91651-large-prime-lorenz-determinant-has-positive-leading-term.md
```

## Census result

All expected `R/L/T/O-9165x` files above were absent from the current trees of
PR #399 and PR #439 and from main. Direct retrieval of the named `T-91651`
theorem returned `404` on both advertised PR heads. Repository code search,
commit search, branch search, and recursive tree searches found no immutable
copy of that theorem.

PR #439 has durable comments recording that:

```text
the finite Lorenz determinant remains open;
complete terminal/collar/common-port typing remains open;
a later full packet publication was being retried after connector write failure.
```

PR #431 had no corresponding deposited status response at the cutoff.

## Nearby durable work

The following related results do exist, but they are not a substitute for the
missing exact theorem and dependency manifest:

```text
PR #439 L-91355   exact causal coefficient budget, recursive mass <1/8
PR #399 L-91406   packet deficit homogeneity and subadditivity
PR #399 T-91401   abstract packet-envelope consumer
PR #424 L-91559   exact nested native row/detail embedding
PR #424 T-91561   separate candidate composition on frozen inputs
```

## Disposition

```text
advertised formulas              mathematically reviewable from the summary
advertised theorem at exact SHA  absent
full immutable proof DAG         absent
independent proof verification   impossible until deposited
RH status                        unproved
```
