# Integration handoff — PR #297 source-binding correction

## Frozen parent

PR #297 before this continuation:

```text
99ab5a6264762d428dfea09d8d246a73b5458c33
```

## New disposition

```text
L-29001 atomized pole frame                    RETAINED
L-29002 ordinary row reserve                   RETAINED AT ROW SCOPE
R-29002 row-to-source automatic lift           REFUTED
R-29002 generalized-prime pointwise lift       REFUTED
L-29003 endpoint tree commutator                RETAINED
L-29005 individual filtered fiber reserve      RETAINED
L-29006 complete prime endpoint source binding PROPOSED COMPLETE
T-29001 endpoint-tree hinge                     SUPERSEDED
T-29001 coupled interior CISR                  ACTIVE / OPEN
RH                                              UNPROVED
```

## Load-bearing exact counterexamples

A future integration must retain both mutations:

```text
(n,j,alpha)=(4,2,1/2):
4 defect=-log(3/2)^2-4log(2)^2<0;

(n,j)=(6,2):
P_omega^2-S_omega=log(3)log(25/32)<0.
```

They prevent diagonal row positivity from being mistaken for source-matrix
coercivity.

## Positive endpoint import

The endpoint restriction of the ordinary-prime Jensen field should now import
`L-29006`, not an open endpoint first-variation theorem:

```text
sum_r Delta A_x(r)D_r=sum_m Lambda(m)W_m,
Lambda(m)>=0.
```

The aggregate endpoint reserve and annular physical-frame bound are explicit.
Do not re-expand the complete `W_m` fiber into its Möbius/dyadic siblings before
taking a sign or norm.

## Remaining production target

A future child PR should emit one `CISR` object containing:

1. the complete two-frequency ordinary-prime source matrix;
2. every linear and convolution Selberg block;
3. a coupled interior Schur complement;
4. the already-closed endpoint form from `L-29006`;
5. all dyadic annulus and block boundaries;
6. a fixed lower-scale recurrence with total coefficient at most one;
7. the prime-annulus and `2/3` Mertens mutations.

A diagonal-only LMI, `P_omega^2>=S_omega`, or scalar weighting of `L-29002` is
an automatic rejection.
