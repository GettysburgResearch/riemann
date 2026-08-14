# Native-root compiler, exact separator, and the source-owned thinning frontier

Date: 2026-08-14  
Review cutoff: `2026-08-14T16:57:25Z`  
Status: **exact advance and exact obstruction; RH unproved**

## Executive verdict

The pass did not produce `PASS_NATIVE_ROOT_CAPACITY_THEOREM`. It produced a sharper fail-closed result:

1. PR `#464` genuinely supplies the fixed-window Hall algebra, formal response commutation, same-index child placement, and subcritical recursive coefficient budget.
2. That algebra does **not** compile into every clause of `T-91314`, because the finite source-owned endpoint/port/current realization is absent. The repository's exact finite-versus-continuum defect is strictly positive.
3. PR `#469` closes terminal raw row and response signs, but its unthinned current-plus-child basis is exactly outside native capacity. The obstruction is an infinite asymptotic family, not merely a small-base anomaly.
4. PR `#467`'s leftmost target-Lorenz cutoff is the exact optimum of the full stopped-leaf box LP. Arbitrary basis discovery can be removed.
5. The direct radix-four formulation exposes a large cone of `Y_4`-zero, score-free repair directions. The next load-bearing object is a source-owned current-thinning/realization certificate.

The new frozen top-level classification is

```text
EXACT_NATIVE_ROOT_COMPILATION_DISCREPANCY_AND_SEPARATOR
```

## Repository freeze and genealogy

At the recorded cutoff:

```text
main:     9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
PR #454: a0409d54250bc211d62718a1aedb6fa020d7f091
PR #464: 2eb70463f3d0ae791a9f140694d2ace7032ae864
PR #467: d5e03a3a63bd05b43abf4b5e37905f86e9ec59d6
PR #468: a41f81466f85d52597c97b41505756a8860698d0
PR #469: 3cf685181bd367b92cdcfeef9249e0b9b542a09e
```

PR `#469` is the live descendant of the requested PR `#468` head. The present packet is stacked on `#469` because it retains the latest terminal raw-generator theorem and the native-capacity firewall.

## I. Clause-by-clause compilation of PR #464

### Compiles exactly or formally

The fixed-window root Hall transport uses one coefficient set for score, target, and all component rows. The child reset supplies endpoints at most `X/67` and total recursive coefficient below `1/8`. The formal endpoint theorem correctly commutes positive sums, ordinary responses, radix-four responses formed from the two ordinary columns, same-index placement, and one global quantizer.

These are real advances. They remove several historical color, Schur, and double-scaling ambiguities.

### Does not compile into NRCT

The missing bridge is not another abstract linearity lemma. It is the finite arithmetic packet itself.

The continuum Volterra packet and finite equality seed differ. At `X=3,m=2`, the exact defect is

\[
4\sqrt2-4\sqrt3+
\frac{5\sqrt2}{2}\log\frac32
>\frac1{10}.
\]

Therefore the formal Hall fiber cannot be identified with the finite native row until a source-owned mismatch/current realization is supplied.

The same missing realization leaves the following `T-91314` clauses unresolved:

```text
one-use ordinary capacity;
one-use detail capacity;
one shared port and every boundary reserve;
current deficit <=2 exact target mass;
atomwise ownership of finite corrections;
immutable nonnegative Y4 slack.
```

The detailed audit is deposited at

```text
audits/gpt56-pro/2026-08-14-t91314-native-root-clause-compiler.tsv
```

## II. Exact separator for the raw PR #469 basis

At

\[
X=136,
\qquad p=67,
\qquad y=136/67,
\qquad q=2,
\]

only the rough integers `1,67` occur in the canonical ordinary response at `X/q=68`. Thus

\[
\Gamma(D_{P_{61},136};2)
=w_{136}(2)+
\frac1{\sqrt{134}}
\log\frac{68}{67}.
\]

The terminal child is exactly the positive excess. Hence the raw current alone saturates the native ordinary column, and current plus child overdraws it. The same calculation at `q` and `4q` gives an identical detail overdraw.

The exact one-column Farkas multipliers are

```text
equality multiplier y=-1;
capacity multiplier z=1;
dual value=-log(68/67)/sqrt(134)<0.
```

### Infinite family

For every prime `p>=71`, choose

\[
X=2(p+1),
\qquad y=2(p+1)/p<3,
\qquad q=2.
\]

The child removes only the `m=p` rough term. The `m=67` reservoir remains in the raw current, so

\[
\Gamma(G_{p,y};2)-w_X(2)
\ge
\frac1{\sqrt{134}}
\log\frac{p+1}{67}
>\frac5{834}.
\]

Thus the raw current itself is ordinarily infeasible at arbitrarily large endpoints. This rules out the hope that the PR `#469` basis becomes native merely in the asymptotic regime.

The correct response is not to add another positive current packet. It is to thin or replace current usage with source ownership.

## III. The stopped-leaf LP has one exact basis

The reviewer requested that the LP not be restricted to the leftmost cutoff unless optimality is proved. That optimality is now exact.

When score per target increases with divisor order and every row per target decreases, the leftmost target fill simultaneously:

```text
minimizes score;
maximizes every row.
```

Threshold duals prove both assertions. Therefore the full LP is feasible exactly when that basis satisfies every score and row constraint. A negative leftmost margin is itself an exact Farkas separator; no alternative basis can repair it.

The historically hostile point `(p,y,j)=(67,13,66)` is positive at the exact basis, with cutoff `123` and margin greater than `0.0083815482754633380`. The remaining campaign is a deterministic activation-cell sign census over the `185` possible cutoff nodes, not a basis search.

## IV. Direct radix-four slack and score-free repair

Let `B` be the triangular ordinary carry matrix and `R_4` the positive inverse of the radix-four difference. After fixing a source-owned recursive child detail packet `R^(4)`, define

\[
 d(s)=B^{-1}R_4[\Omega_X-R^{(4)}-s].
\]

Then

\[
0\le s\le\Omega_X-R^{(4)},
\qquad d(s)\ge0
\]

implies both detail and ordinary one-use capacity. The exact objective is

\[
\min\sum_qY_4(q)s(q).
\]

For a unit slack at column `q`, the reconstructed row column has

\[
h_q=\frac{q+1}{q-1},
\qquad
h_{q-1}=-\frac{q(q-3)}{(q-1)(q-2)}.
\]

Increasing slack therefore decreases the top row and increases the next row. If `Y_4(q)=0`, the transfer costs no literal endpoint score. There are `3962` such columns below `5000`.

This is a promising repair cone, but it is not yet source-owned and its lower triangular tail can create fresh deficits.

## V. Most ambitious credible closure path

The shortest path now appears to be a hybrid of PRs `#454`, `#467`, and the direct slack theorem:

1. Export the live stopped-line source occurrences and exact child packet.
2. Fix the target-Lorenz basis using `L-91686`; do not search arbitrary bases.
3. Parameterize current thinning by detail slack `s` and reconstruct the row exactly.
4. Include every ordinary/detail/port coordinate and every correction owner in the atomwise matrix of `L-91671`.
5. Partition parameter space only by arithmetic activation and cutoff changes.
6. On each cell, first solve using `Y_4`-zero columns; then admit positive-cost columns only as needed.
7. Certify the stable basis by directed intervals over the full cell.
8. If infeasible, export the exact dual and derive the minimal missing target-null thinning generator from its support.

This is the `SONTR` theorem stated in `T-91659`.

## Verification

```bash
cd experiments/X-91686-native-root-compiler-separator
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Retained proof-object digest:

```text
1e12626cf83dc908d5638de4f472a6b5fe3bc38515fa23abe0555fd58cea61be
```

## Exact boundary

```text
root fixed-window Hall algebra                  VALID ON FROZEN INPUTS
subcritical child budget                        VALID
finite source-owned endpoint realization        OPEN / EXACT DEFECT EXPOSED
raw terminal current+child native placement      FALSE / EXACT SEPARATOR
raw current native placement asymptotically      FALSE / INFINITE FAMILY
leftmost stopped-leaf LP basis                  EXACT OPTIMUM
hostile p=67,y=13,row=66 cell                   POSITIVE
all activation cells                            OPEN / DIRECTED
score-free triangular repair cone               EXACT
source-owned native thinning SONTR              OPEN / RH-BEARING
Native-Root Capacity Theorem                    OPEN
Riemann Hypothesis                              UNPROVEN
```
