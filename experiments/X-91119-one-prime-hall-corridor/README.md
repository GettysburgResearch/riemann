# X-91119 — One-rough-prime Hall corridor

Directed exact finite-window regression for `L-91331`.

For every reset cell and every active odd threshold, it checks both endpoints of
the parameter intervals

```text
reserve:  a in [1, 1+1/sqrt(67)], support e <= o
equality: a in [2, 2(1+1/sqrt(67))], support e <= o+1
```

and certifies margins

```text
reserve  > 8/25
equality > 1/400.
```

Hall margins are affine in `a` and in `sqrt(x)` on each activation cell, so the
endpoint checks certify the full rectangles. The theorem is deliberately scoped
to one new rough prime at one reset boundary; it is not a distinct-prime scalar
tensorization claim.
