# Factor-67 Bellman hardening: exact maps, the first `p=67` separator, and a fixed-angle no-go

## Freeze

```text
main at research start   f789265569013ebff254b082c2e0428970bdaf57
base PR #591             5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111
NCBI PR #581             62aaa54ac49f0aa89fd58f14a539cc53089f884c
CPSL PR #584             e919c6afd1e95fffa505f7ba3f532cb12b8c410c
future profile PR #582   699f9f119a66823702e96fba95cc8b14b8251c60
P61 bias PR #576         0f6ea6eae813c1d867ae50744cf5fd57e2720bb7
```

RH remains unproved.

## Exact common state

For a paired positive source, the source-faithful state is the pair of oriented
Lorenz slacks

\[
D^+(\lambda)=\lambda T_O+\sum_{E}a_i(r_i-\lambda t_i)_+-R_O,
\]

\[
D^-(\lambda)=\lambda T_E+\sum_{O}a_i(r_i-\lambda t_i)_+-R_E.
\]

CPSL feasibility is exactly `D^+(lambda)>=0` for all real lambda. Adjoining a
rough prime gives

\[
D_{Qp}^+(X,\lambda)=D_Q^+(X,\lambda)+p^{-1/2}D_Q^-(X/p,\lambda),
\]

\[
D_{Qp}^-(X,\lambda)=D_Q^-(X,\lambda)+p^{-1/2}D_Q^+(X/p,\lambda).
\]

Therefore the smallest exact Markov state is the two-orientation profile at all
activated future products. PR #591 proves this recurrence and the exact
non-equivalence of NCBI67 and CPSL67.

## New failure: the repaired base bias is not an invariant cone

At lambda zero, the target cushion vanishes and the two slacks are opposite.
For the annular source define signed scalar `F_P` and unsigned mass `M_P`.
PR #576 proves `F>=M/42` at the `P_61` base.

After the single literal rough prime `67`, the directed replay proves

```text
42F_67(N)-M_67(N) > 0       for every integer 67<=N<=160;
42F_67(160)                 > 0.2262223247633235;
42F_67(161)                 < -0.3757404915589003.
```

Every breakpoint is integral and the expression is affine in `log X` on each
unit cell. The first real crossing is bracketed by

```text
160.37507 < X_* < 160.37508.
```

At `X=161`, `F_67>9.65189`, so this is not scalar negativity. It is an exact
separator for the fixed `1/42` mass-angle Bellman cone.

## Generic no-go

For either the logarithmic `Q_*` kernel or its scale-four annulus, a fixed finite
prime state has

\[
{F_P(X)\over M_P(X)}\to\prod_{p\mid P}{p-1\over p+1}.
\]

The rough-prime product on the right tends to zero because the sum of prime
reciprocals diverges. Thus every fixed positive scalar-to-mass aperture fails
for some finite actual future-prime state, even though its scalar is eventually
positive.

This closes a mechanism class. It does not close RH.

## Exact theorem map after the no-go

```text
LBP67 -> CPSL67 -> scalar positivity -> RH
NCBI67 -> scalar positivity -> RH
```

The two producer statements are not equivalent. The failed mass-angle cone is
neither one of them. A successful proof must control the unnormalized
Euler-minus quotient profile, an exact completed Lorenz dual, the nonlocal NCBI
current, or the root zero-hinge future tail.

## Replay

```bash
cd experiments/X-97900-fixed-angle-bellman-no-go
python3 verify.py
```

Expected:

```text
PASS_T97900_FIXED_ANGLE_BELLMAN_NO_GO
21de8b6bf98825f73a9a159fce0beebd25e591760f82684026a890ed8eda9d44
```

## Boundary

```text
source-faithful Lorenz recurrence            PROVED
NCBI/CPSL theorem-level maps                 PROVED
future quotient profile                      NECESSARY
base P61 1/42 bias                           PROVED
1/42 cone after p=67                         REFUTED
all fixed positive mass-angle cones          REFUTED
LBP67 / CPSL67 / NCBI67 / root zero hinge    OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
