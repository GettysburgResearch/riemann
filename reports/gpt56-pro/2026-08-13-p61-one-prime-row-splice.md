# `P_61` one-prime row-splice attack

## Frozen source

- repository: `gfreund123/riemann`
- live parent: PR #399
- reviewed head: `4b8b4306142e92d66bc27f7eda10f64a703ed3d8`
- current first gate in that head: `P_61` plus one rough prime

## Result

The inherited-row part of the preferred `P_61` gate is now closed:

\[
\mathscr R^{(61)}_{p,y}(j)>0
\qquad
(p\ge67,\ 2\le j\le y<67).
\]

The proof uses the Green decomposition of `L-91344`, a directed `2^18` scan of the `P_61` divisor spline, and two rational margin comparisons:

```text
p=67 margin:        2489/3250  > 0
all p>=71 margin:   9973/81250 > 0
```

The worst retained floating row in reconnaissance occurred near

```text
p=67, y=67, j=66,
```

and was still positive by approximately `0.01221428` before the larger normalized analytic margins were applied.

## Consequence

The preferred one-prime packet now has:

```text
target positivity              L-91345
score > target                 L-91345
all inherited rows positive    L-91347
```

The next theorem is not another row inequality. It is a **simultaneous cone-realization theorem**: construct one positive object—or a rigorously compatible target-source plus canonical-row pair—whose target is exact, whose actual row entropy is sufficient for the native score, and whose physical capacity is charged once.

No RH claim is made.
