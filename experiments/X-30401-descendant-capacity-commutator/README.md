# X-30401 — Descendant capacity and adjacent-commutator replay

This standard-library checker verifies finite exact algebra for the continuation
of PR #303.

It checks:

```text
expanded central-tree capacity = dyadic Haar formula      12,636
factor-two capacity recurrence                              12,636
adjacent commutator divisor-source rows                     13,040
integer capacity-majorant rows                               1,024
actual shifted-pair source ordering                          3,840
paired source / split-flow carry replay                    622,080
```

The exact scope mutations are:

```text
N=4, c_m=1/m:
root-only h_2 contribution      1/6
expanded h_2 coefficient       3/4

N=6, c_m=1/m:
expanded h_4 coefficient       1/20
model sibling requirement      1/5
```

Thus descendant capacity invalidates the root-only equality but does not prove a
zero-defect capacity theorem.

The integer capacity check uses

```text
omega_(n,j) <= 2 sqrt(n) <= 2 ceil_sqrt(n)
```

and verifies

```text
||E_h||_majorant <= 24 ceil_sqrt(h+1)
```

through `h=1024`.  The analytic proof is in `L-30402`; the finite replay is a
mutation test rather than its substitute.

Retained digest:

```text
b41721d6b9c6f82d05156f28be954d878e8f0560b3216188ddfbc3e7e9d6236d
```

The package proves neither the complete PR #286 source manifest, the
all-generation atomic-norm composition, Cycle Debt, nor RH.
