# Hostile reconstruction of T-91821 and two-sorted successor

## Frozen targets

```text
PR #499: 99d3983b57f82941131caa8d9c36e4947f1179a0
PR #500: d73c1e7a1a482cac31581211a84db43cc34c824e
review #501: 2f58a65097206c4b80142cead52282161302d10c
```

PR #499 is not modified.

## First broken arrow

The complete target-null Hall packet in `L-91820` does not exist. At `x=2`, the forced edge `2->1` has negative declared-score correction even though every component-row correction is nonnegative. The correct output is a positive residual source plus a row-only current bonus.

## Repair

The successor uses a two-sorted fibre:

```text
source sort:
    positive Hall residual;
    rough first ownership;
    causal current and internal child sources;

row sort:
    target-null nonnegative Hall bonus;
    Hall-edge ownership;
    current generation only.
```

After whole-cell restriction, the source sort is physically placed and passed through one label-blind B-spline block. The row bonus and exact finite anchors pass through identity blocks. All three channels are summed into one row and thinned once.

The signed finite/continuum comparison concerns only the bulk source block. The identity channels occur identically in the ideal and realized row and cancel. All-column and terminal bounds therefore apply to the same final row whose complement is paired with `Y_4`.

## Comparison with PR #500

PR #500 correctly observes that output marginal equality cannot certify source ownership and supplies a valid abstract coupling theorem. Its live instantiation and replay remain schematic. The successor takes the useful coupling lesson but avoids a nonexistent physical placement kernel for the Hall bonus: the bonus is already a finite row and uses an identity row channel.

The successor also corrects the owner validator: first ownership is a function from monomials to primes and is naturally many-to-one.

## Proposed endpoint result

On the frozen analytic inputs, the single realized row satisfies

```text
native ordinary/detail feasibility in every column;
terminal margin 581 X^-3/2;
native deficit <60989 for X>=10^12;
no exported recursive family;
no auxiliary matrix port;
no J_Lambda-4sqrt(X) bridge.
```

The endpoint consumer then gives a candidate RH conclusion. Independent reconstruction remains mandatory.
