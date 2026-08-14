# Target-Lorenz vector primal/dual theorem and quotient-five closure

## Freeze

```text
repository:       gfreund123/riemann
parent PR:        #468
parent head:      a41f81466f85d52597c97b41505756a8860698d0
parent base:      d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6
review date:      2026-08-14
```

**RH remains unproved.** This packet converts the Target-Lorenz frontier into an
exact common-source vector primal/dual theorem and closes every row cell below
quotient five.

## Main exact theorem

Let the even source atoms carry target, score and every component row. Assume
score-per-target is increasing in divisor order and every row-per-target
profile is decreasing, exactly as supplied by `L-91682/L-91684`.

Then the leftmost target submeasure `U` simultaneously:

```text
minimizes used score;
maximizes every component row;
uses one literal coefficient on each even source atom.
```

Therefore

```text
Target-Lorenz is feasible
iff
some common-source submeasure is feasible.
```

This eliminates a large apparent search space. A more complicated source
allocation cannot repair a failed Target-Lorenz row while staying inside the
same literal source box.

The complete finite dual is

\[
 \sum_e
 [\tau T_e-\beta S_e+\sum_\alpha\lambda_\alpha R_e^\alpha]_+
 \ge
 \tau O_T-\beta O_S+\sum_\alpha\lambda_\alpha O_R^\alpha,
\]

for every real `tau` and nonnegative `beta,lambda`. At a failed row the cutoff
multiplier `tau=-R_c/T_c` is already a strict Farkas separator. Thus the primal
row margin and the dual obstruction are exactly the same finite object.

## Stronger sufficient route

The proportional target submeasure is a legal comparison point. Hence the
cutoff-free determinant

\[
 O_TE_R^{(j)}-E_TO_R^{(j)}\ge0
\]

is sufficient for the Target-Lorenz row gate. This gives a cleaner analytic
campaign with one full determinant per row, while the cutoff form remains the
sharp necessary-and-sufficient primal test.

## Exact quotient-five theorem

For `x=py<5j`, child rows are inactive and the only possible row-active source
indices are

```text
even: 1;
odd:  2,3.
```

The target atoms satisfy exactly

\[
 T_1>T_2+T_3.
\]

The proof is split at `y=2,3`; its two nontrivial radical lower bounds are above
`5` and `8`. Since the row-per-target profile is decreasing, the target mass
used at `d=1` dominates every active odd row. Therefore

\[
 \boxed{R_j(U)-O_R^{(j)}>0\quad(py<5j).}
\]

The first unresolved quotient is where divisor `5` becomes row active.

## Reconnaissance

The deterministic NumPy scan covers

```text
15 rough-p values from 67 through 5003;
133 y-values per p;
65 component rows;
129,675 row tests.
```

No negative Target-Lorenz margin or full target determinant was found. The
smallest sampled margin is in the already-closed first cell. After removing the
exact `py<5j` region, the smallest sampled margin is approximately
`0.00670597` near row `66` and quotient `5.0757`.

These values are discovery evidence only; the JSON labels them floating
reconnaissance.

## Corrected parameter warning

The causal target atom is piecewise at `d=y`: child-active atoms and
parent-only frontier atoms have different formulas. Consequently the full
Target-Lorenz cutoff does **not** globally collapse to a function of
`sqrt(y)(sqrt(p)+1)` alone. Any analytic cell proof must retain the child/frontier
activation split.

## Remaining route

```text
1. certify the row family for py>=5j;
2. lift the stopped-leaf primal through the exact least-prime source partition;
3. charge native ordinary/detail reservoir, collars, omissions and shared port once;
4. apply the subcritical child-mass envelope and positive Y4 dual;
5. invoke the reviewed one-sided endpoint consumer.
```

The first item is now a sharp primal-or-dual arithmetic theorem. The second and
third are the native-root crosswalk and must not be inferred from separate
coordinate feasibility.

## Replay

```text
PASS_TARGET_LORENZ_VECTOR_PRIMAL_DUAL
f4ee167558901914b9a637333719b19f31f593b3c61141ac1f87e9cc1329e6d4

PASS_FLOATING_TARGET_LORENZ_RECONNAISSANCE
cdea6b256e970b3d26d5200b244e21e95f6a4ce62bfde35ca6bd09776b781a6c
```

## Honest boundary

```text
common-source vector primal/dual theorem        PROVED EXACT
failed-row cutoff Farkas separator              PROVED EXACT
full determinant sufficient route               PROVED EXACT
Target-Lorenz row gate for py<5j                PROVED EXACT
remaining row family py>=5j                     OPEN / ARITHMETIC
native one-use root crosswalk                    OPEN / COMPOSITION
full RH implication                             NOT YET ESTABLISHED
Riemann Hypothesis                              UNPROVEN
```
