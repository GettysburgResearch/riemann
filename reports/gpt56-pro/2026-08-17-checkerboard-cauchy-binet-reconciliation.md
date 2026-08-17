# Reconciliation of the unpublished stronger T-97200 description with PR #567

## Finding

The response preceding PR #567 overclaimed a complete checkerboard,
Cauchy–Binet, and global Hall closure. The remote artifact never contained those
theorems. PR #567 correctly and intentionally labels the global producer open.

## Exact first broken arrows

### Owner incidence

One nonnegative entry per source column does not imply nonnegative minors. The
\(2\times2\) swap matrix is the minimal counterexample.

### Terminal checkerboard

Positive target and scalar coordinates at each leaf do not imply monotone
cross-leaf ratios or nonnegative \(2\times2\) minors. A two-row positive matrix
with determinant \(-3\) is the minimal counterexample.

### Composition

Cauchy–Binet is valid, but it propagates signs only after compatible signs have
already been proved in both factors.

### Hall

The exact fixed-endpoint problem is a fractional-knapsack/Lorenz inequality.
The finite optimizer is explicit; the uniform arithmetic inequality is not
proved.

## Disposition

```text
PR #567                              intentional retraction
stronger unpublished complete claim  withdrawn
conditional Cauchy–Binet skeleton    recovered exactly
fixed-endpoint Hall optimizer         recovered exactly
uniform GPHT* / TFPE / ACBI           open / RH-bearing
RH                                    unproved
```
