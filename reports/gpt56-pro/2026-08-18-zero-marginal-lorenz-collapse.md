# Factor-67 advance: canonical source order and eventual zero-marginal Lorenz collapse

## Freeze

```text
base PR #596   40bfd7e70521f4205e95d3960812a6cef6073c05
PR #591        5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111
PR #590        4f1283c67f0d4a4b504badd4c4113ba227521162
PR #594        ef76157a516c520a0f829ea4ee346c62759743ed
```

RH remains unproved.

## Headline

The completed-parity scalar Lorenz problem is asymptotically simpler than the
full all-threshold Bellman profile suggests.

The unsieved scalar-to-target ratio

\[
\rho_*(Y)=Q_*(Y)/(4\sqrt Y-3)
\]

is zero through `Y=2`, strictly increases thereafter, and tends to six. Hence
every completed-source atom is ordered by its ordinary source index:

\[
k_1<k_2
\Longrightarrow
r_X(k_1)/t_X(k_1)
\ge r_X(k_2)/t_X(k_2).
\]

The finite Lorenz optimizer is therefore a single increasing-index prefix, with
at most one fractional atom. No endpoint-dependent sorting remains.

## Exact analytic ratio theorem

On `N<Y<N+1`, write `Q_*(Y)=A_N log Y-B_N`. The derivative numerator of
`Q_*/T` is

\[
G_N(Y)=A_N(4\sqrt Y-3)-2\sqrt Y Q_*(Y).
\]

As a function of `sqrt(Y)`, `G_N` is strictly concave. The six finite right-cell
endpoints through eight are directed positive. For the tail, elementary bounds
on `sum m^(-1/2)` yield

\[
G_N(Y)\ge\sqrt Y[2c\log Y-K]+3d,
\]

and the directed constant

```text
2c log 8-K > 0.6515026909363199
```

closes every `Y>=8`. Integrating the same bounds gives

\[
Q_*(Y)=24\sqrt Y+O(\log Y),
\]

so the ratio tends to six.

## Canonical one-switch Lorenz envelope

For the weighted atom coordinates

\[
t_X(k)=k^{-1/2}T(X/k),
\qquad r_X(k)=k^{-1/2}Q_*(X/k),
\]

the ratio is exactly `rho_*(X/k)`. If the even source indices are
`k_1<...<k_M`, put

\[
A_j=\sum_{i\le j}t_X(k_i),
\qquad B_j=\sum_{i\le j}r_X(k_i).
\]

If `A_(j-1)<=T_O<=A_j`, then

\[
\Phi_X(T_O)
=B_{j-1}
+\rho_*(X/k_j)(T_O-A_{j-1}).
\]

Thus every finite Lorenz failure has a canonical source-index prefix separator.
The continuous dual variable is only a coordinate for this one switch.

## New squarefree-shell theorem

Let `T_(E,+)` be the target capacity of the even atoms with positive scalar.
Because `Q_*(Y)>0` exactly for `Y>2`, these are exactly `k<X/2`.

The parity indicator identities give

\[
2(T_O-T_{E,+})
=
\sum_{X/2\le k\le X}\mu(k)^2t_X(k)
-\sum_{k\le X}\mu(k)t_X(k)
-\sum_{k<X/2}\mu(k)t_X(k).
\]

PNT makes the two signed sums `o(sqrt X)`. Squarefree density gives the positive
main term

\[
T_O-T_{E,+}
=
{3\over\pi^2}(4\log2+3\sqrt2-6)\sqrt X+o(\sqrt X).
\]

The constant in parentheses is approximately `1.0152294093` and is strictly
positive. Hence the odd target eventually lies beyond every even atom carrying
positive scalar.

## Eventual collapse

If total target capacity holds, the optimizer must saturate every positive-scalar
even atom and fill the remaining target from the zero-scalar shell. Therefore

\[
\Phi_X(T_O)=R_E
\]

at every sufficiently large endpoint. Completed scalar feasibility is exactly

\[
T_E\ge T_O,
\qquad R_E\ge R_O.
\]

Equivalently,

\[
\boxed{
CPSL67
\Longleftrightarrow
GTC67\wedge GPC67
}
\]

at eventual-uniform scope, and the Lorenz marginal is `lambda=0`.

## Both zero hinges retain RH strength

The scalar implication `GPC67 -> RH` is the frozen Mellin-Landau consumer. The
new target transform is

\[
\int_1^\infty (T_E-T_O)X^{-s-1}dX
=
{s+3/2\over s(s-1/2)\zeta(s+1/2)}.
\]

Its positive-real singularities are removable, while every zeta zero to the
right of the critical line survives. Landau therefore gives `GTC67 -> RH`.

This explains why the target sign is not routine, even though the interior
Lorenz geometry disappears.

## Strategic consequence

The project should stop treating the all-`lambda` Lorenz cone as the minimal
closure theorem. It remains a valid sufficient route, but the asymptotic
conclusion-producing work is concentrated at two root zero hinges. For RH it is
enough to prove the native scalar sign, so the strongest next attack is the
largest-prime identity and balanced Type-II/root-tail frontier in PRs #590/#594.

## Replay

```bash
cd experiments/X-98000-zero-marginal-lorenz
python3 verify.py
```

Expected:

```text
PASS_T98000_ZERO_MARGINAL_LORENZ_COLLAPSE
58d3191b80bd7f4763733423b5f94671f2626a19b2a81ce4547170e27e6ee7bc
```

## Boundary

```text
ordered ratio rho_* in [0,6)                PROVED
canonical one-switch source prefix           PROVED
positive zero-scalar squarefree shell        PROVED ASYMPTOTIC
marginal lambda=0 eventually                 PROVED IF TARGET CAPACITY
CPSL67 <-> GTC67 and GPC67 eventually        PROVED
GTC67                                        OPEN / RH-BEARING
GPC67                                        OPEN / RH-BEARING
RH                                           UNPROVEN
```