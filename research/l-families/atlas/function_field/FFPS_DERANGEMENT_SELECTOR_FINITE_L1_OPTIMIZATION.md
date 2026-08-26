# Derangement support does not cheapen the cycle selector through degree ten

Status: **exact characteristic-zero weighted-`L1` optimization for
`2<=d<=10`; the all-`d` statement is a conjecture, not a theorem; no native
FFPS adapter, asymptotic selector bound, RH, or GRH claim**

Bounded exact replay:
[`ffps_derangement_selector_finite_l1_optimization.py`](ffps_derangement_selector_finite_l1_optimization.py).
Canonical summary:
[`ffps_derangement_selector_finite_l1_optimization.json`](ffps_derangement_selector_finite_l1_optimization.json).

Source boundary:

1. the exact full-cycle mass theorem at
   `691166b8c31f9b8e3790a9687d8fce55493f6831`;
2. the closed root-incidence optimization gate at
   `961603fd0a4fd33299b94c8eaafa11ce53bd3e50`.

The replay pins all four blobs from each source packet. It imports no
uncommitted implementation.

## 0. Outcome

Let `Perm_d` be the character of the permutation representation of `S_d`.
Among class functions

\[
 Q=\sum_{\lambda\vdash d}a_\lambda\chi_\lambda
\]

subject to

\[
 Q((d))=1,
 \qquad
 \operatorname{Perm}_d(g)Q(g)=0\quad(g\in S_d),
\tag{0.1}
\]

minimize

\[
 \|Q\|_{\rm rank,1}
 =\sum_{\lambda\vdash d}f^\lambda|a_\lambda|,
 \qquad f^\lambda=\dim\lambda.
\tag{0.2}
\]

The coefficients may be real or complex. The rational dual certificates
below bound the real part of the dual pairing, so complex phases give no
additional saving.

Condition (0.1) says exactly that `Q` vanishes on every conjugacy class with
a fixed point. Its values on all other derangement classes are free. Thus
this is strictly more permissive than demanding the exact `d`-cycle
indicator on every class.

The exact finite result is:

\[
 \boxed{
  \min \|Q\|_{\rm rank,1}={2^{d-1}\over d}
  \quad\text{for }2\le d\le10.}
\tag{0.3}
\]

Moreover, the unique minimizer in every checked degree is still

\[
 \boxed{Q=1_{(d)}.}
\tag{0.4}
\]

So the freedom on the other derangement classes gives neither a strict
saving nor a second equal-cost selector through degree ten.

| `d` | irreducibles | free derangement values | exact optimum | minimum relative nonhook dual slack |
|---:|---:|---:|---:|---:|
| 2 | 2 | 0 | `1` | not applicable |
| 3 | 3 | 0 | `4/3` | not applicable |
| 4 | 5 | 1 | `2` | `1` |
| 5 | 7 | 1 | `16/5` | `1` |
| 6 | 11 | 3 | `16/3` | `2/3` |
| 7 | 15 | 3 | `64/7` | `5/7` |
| 8 | 22 | 6 | `16` | `19/31` |
| 9 | 30 | 7 | `256/9` | `63/95` |
| 10 | 42 | 11 | `256/5` | `34/55` |

Every entry is certified over the rationals after the exploratory LP. The
bounded replay does not invoke a floating-point or external LP solver: it
recomputes the character tables by Murnaghan--Nakayama and checks explicit
rational primal and strict dual certificates.

## 1. Root incidence is restriction to `S_(d-1)`

Embed `S_(d-1)` as the subgroup fixing the last letter. Every conjugacy
class of `S_d` with a fixed point meets that subgroup, and its intersection
has the same class-function value. Hence

\[
 Q=0\text{ on all fixed-point classes}
 \quad\Longleftrightarrow\quad
 \operatorname{Res}^{S_d}_{S_{d-1}}Q=0.
\tag{1.1}
\]

By the Young branching rule,

\[
 \operatorname{Res}\chi_\lambda
 =\sum_{\nu\lessdot\lambda}\chi_\nu.
\]

Writing `B` for the level-`d` to level-`d-1` Young-graph incidence matrix,
(1.1) is the exact coefficient equation

\[
 \boxed{Ba=0.}
\tag{1.2}
\]

Murnaghan--Nakayama gives

\[
 \chi_\lambda((d))=
 \begin{cases}
  (-1)^k,&\lambda=H_k=(d-k,1^k),\\
  0,&\lambda\text{ nonhook}.
 \end{cases}
\]

Therefore the normalization is

\[
 \sum_{k=0}^{d-1}(-1)^k a_{H_k}=1.
\tag{1.3}
\]

Equations (1.2)--(1.3) are the exact finite LP constraints used by the
replay. They are also a cleaner formulation of the universal-root
incidence cancellation: multiplying by `Perm_d` is `Ind Res`, so
`Perm_d Q=0` and `Res Q=0` are equivalent here.

## 2. Primal candidate and its mass

The exact cycle indicator has the unique character expansion

\[
 1_{(d)}={1\over d}\sum_{k=0}^{d-1}(-1)^k\chi_{H_k}.
\tag{2.1}
\]

It is feasible for the relaxed problem because it vanishes on every class
except `(d)`. Since `f^(H_k)=binom(d-1,k)`, its objective is

\[
 {1\over d}\sum_{k=0}^{d-1}{d-1\choose k}
 ={2^{d-1}\over d}.
\tag{2.2}
\]

This gives the upper bound in (0.3). The issue addressed here is whether
nonzero values on the other derangement classes can lower it.

## 3. Exact rational dual certificates

Let `E_d` consist of all fixed-point cycle types together with `(d)`. A
dual certificate is a rational vector `(y_mu)_(mu in E_d)` satisfying

\[
 \left|\sum_{\mu\in E_d}y_\mu\chi_\lambda(\mu)\right|
 \le f^\lambda
 \qquad(\lambda\vdash d).
\tag{3.1}
\]

For every feasible `Q`,

\[
 y_{(d)}
 =\operatorname{Re}\sum_{\mu\in E_d}y_\mu Q(\mu)
 \le\sum_\lambda f^\lambda|a_\lambda|.
\tag{3.2}
\]

The JSON records every nonzero rational `y_mu` for every `2<=d<=10`. In
each degree it verifies

\[
 y_{(d)}={2^{d-1}\over d},
\tag{3.3}
\]

so (3.2) matches the primal value (2.2). For example, at `d=6` one strict
certificate is

\[
\begin{aligned}
 y_{(6)}&=16/3,&
 y_{(4,1,1)}&=-4/3,\\
 y_{(3,2,1)}&=-32/9,&
 y_{(2,1,1,1,1)}&=5/9,
\end{aligned}
\]

with every unlisted class coefficient zero.

The replay checks (3.1) exactly for every irreducible. On every hook,

\[
 \sum_\mu y_\mu\chi_{H_k}(\mu)
 =(-1)^k f^{H_k},
\tag{3.4}
\]

while every nonhook inequality has the strictly positive relative slack
shown in the table. Complementary slackness therefore forces every
nonhook coefficient of an optimal primal solution to vanish.

With nonhooks removed, the branching equation at the hook predecessor
`(d-1-k,1^k)` gives

\[
 a_{H_k}+a_{H_{k+1}}=0.
\]

Thus `a_(H_k)=(-1)^k a_(H_0)`, and (1.3) gives
`a_(H_0)=1/d`. This proves the finite uniqueness assertion (0.4).

## 4. Why the computation is exact

For every partition `lambda` and cycle type `mu` through degree ten, the
replay computes `chi_lambda(mu)` recursively by removing connected border
strips and applying the Murnaghan--Nakayama sign. It then checks

\[
 \sum_{\mu\vdash d}{\chi_\lambda(\mu)\chi_\rho(\mu)\over z_\mu}
 =\delta_{\lambda,\rho}
\tag{4.1}
\]

and independently checks that the identity value equals the hook-length
dimension. The finite LP was used only to discover certificates. Each
floating result was rationally reconstructed, then all equalities,
inequalities, objectives, and strict slacks were rechecked in exact
`Fraction` arithmetic. The committed replay contains only this exact
verification stage.

At the largest degree there are 42 irreducibles and 31 equality constraints
(30 fixed-point classes plus the cycle normalization). Across all nine
degrees the replay checks 137 partitions, 3,581 character-table entries,
and 116,945 exact orthogonality summands.

## 5. All-`d` frontier

The finite pattern strongly suggests the deliberately fenced conjecture

\[
 \boxed{
 \text{For every }d\ge2,\quad
 \min\|Q\|_{\rm rank,1}=2^{d-1}/d,
 \text{ uniquely at }Q=1_{(d)}.}
\tag{5.1 conjecture}
\]

This packet does **not** prove (5.1).

The Young-graph dual shows exactly where a simple proof attempt fails. If
`z=2^(d-1)/d`, hook saturation forces the predecessor potentials

\[
 x_k=(-1)^k\left[
  \sum_{j=0}^k{d-1\choose j}-(k+1)z
 \right].
\tag{5.2}
\]

Setting every nonhook predecessor potential to zero satisfies all capacities
through `d=7`. At `d=8`, `k=1`, it asks the near-hook `(6,2)` of dimension
20 to absorb `|x_1|=24`, a ratio `6/5`. Thus the zero-interior ansatz fails
even though the full exact LP still has a strict certificate. Any all-`d`
proof must propagate potentials into the interior of Young's lattice or use
another global argument; the hook recurrence alone is insufficient.

No closed formula for those interior potentials is claimed here.

## 6. Scope and FFPS consequence

Proved exactly here:

- the optimization value and unique minimizer for every `2<=d<=10`;
- the equivalence between fixed-point vanishing and the branching equations;
- every displayed rational dual inequality and strict uniqueness slack;
- the failure of the zero-interior dual ansatz beginning at `d=8`.

Not proved here:

- (5.1) for `d>=11`, or any asymptotic selector lower bound;
- a native FFPS identification of its boundary with universal root incidence;
- an affordable joint `K_0` simplification after tensoring with the source;
- a trace estimate, individualization, RH, or GRH.

The finite theorem closes the proposed cheaper derangement-supported escape
only through degree ten. It does not replace the exact-cycle packet's stated
all-degree theorem for the **unrelaxed** indicator, and it does not close the
source-specific or jointly cancelled geometric escapes listed there. The
character theory and finite LP duality are classical tools; no literature
novelty is asserted.

## 7. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_derangement_selector_finite_l1_optimization.py --check
python -B -O research/l-families/atlas/function_field/ffps_derangement_selector_finite_l1_optimization.py --check
python -B -m unittest tests.test_ffps_derangement_selector_finite_l1_optimization
python -B -O -m unittest tests.test_ffps_derangement_selector_finite_l1_optimization
```

The replay performs no external LP call, floating-point step, finite-field
enumeration, curve or sheaf construction, `L`-function computation, or zero
search.
