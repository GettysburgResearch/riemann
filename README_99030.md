# T-99030 — Survival-resolvent Bellman hardening

This add-only successor to PR #620 introduces one new idea:

> move the causal survival copy to the left and divide by its killed mass.

The exact score-defect identity then becomes a discounted Bellman equation on
the **actual** rough-prime tree. Combined with Hall target exactness, it proves:

```text
exact integrated root target mass     <16
complete arithmetic score debt        <32
leaf-count dependence                  absent
artificial fixed-67 path               unnecessary
```

The branch strengthens the all-depth score interface of T-99020. It remains a
proposed complete RH proof candidate pending hostile independent review. RH is
not established by publication.

Review first:

```text
L-99030
L-99031
T-99030
X-99030
R-99030
```
