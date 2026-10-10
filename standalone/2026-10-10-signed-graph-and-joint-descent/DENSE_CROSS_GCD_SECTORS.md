# Dense cross-gcd sectors at every fixed moment order

**Status:** proposed conditional analytic theorem, with an all-order rational
inequality proof. This is an extension of the shared-incidence charge lemma
in the companion `ARBITRARY_GRAPH_SECTORS.md`. It controls a specified entire
signed sector of the actual inverse-coefficient moment. It does not estimate
the complementary tuples or prove a full moment, 17/24, or RH.

**Scope:** the Eisenstein field, the source's good squarefree column ideals,
every nonzero element row, fixed smooth column tests, every fixed integer
order `k >= 3`, and every `1 <= R <= D`. All constants can depend on the
fixed order and tests. The hypotheses are precisely the moving-mask native
second moment `NM2` and the smooth inverse pointwise premise `PW_b` stated
in the companion note. In particular `H = D^h` has fixed `h > 1`. The
counting choice `b = 1` is available; any smaller `b` retains its separate
pointwise premise.

**Exact dependencies:** the companion shared-incidence charge lemma; the
native hypotheses as specified in PR #924, commit
`725b2d25ab47e57500049d93985560098c7ef3fa`,
`standalone/2026-10-10-sextic-moving-labels/CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md`;
the finite disjointness correction of PR #926, commit
`086bf0560c0c2679a1fe41418f583d2c5ca743c3`,
`standalone/2026-10-10-mobius-overlaps-and-sampled-moments/MOBIUS_OVERLAP_TAILS.md`,
Lemma 6.1. No new external analytic input is used here.

## 1. The actual signed sector

There are `k` unbarred positions and `k` barred positions, with column
ideals `n_1,...,n_k;m_1,...,m_k` in fixed annuli of scale `D`. Expand the
literal Hermitian inverse-coefficient moment, retaining its Möbius signs,
fixed twists, zero-extended characters and original smooth column tests.
Let `q_I`, for nonempty subsets `I` of these `2k` positions, be the unique
squarefree, mutually coprime incidence ideals: a prime belongs to `q_I`
exactly when it divides the coordinates indexed by `I` and no others.

Let `Theta` be any complex multiplier of modulus at most one depending
only on the shared incidence ideals `q_I` with `|I| >= 2`. Require it to
vanish unless

\[
 N\gcd(n_i,m_j)\ge D/R\qquad(1\le i,j\le k).       \tag{1.1}
\]

Denote this signed tuple-row sum by `S_Theta(D,H,R)`. A bounded row
multiplier supported on `0 < Nu <= c H` is allowed, as in the companion
lemma. The choice `Theta` equal to the indicator of (1.1) gives the whole
complete-cross-gcd sector. Further restrictions based solely on the
shared incidence data are allowed, including bounded complex signs.
Restrictions depending on the singleton cores are not part of the theorem.

### Theorem 1.1

For every fixed `k >= 3` and

\[
\frac{k}{2(k-1)}\le b\le1,
\]

under `NM2` and `PW_b`,

\[
\boxed{
 |S_\Theta(D,H,R)|
 \ll_{k,b,h,\epsilon} H D^{1+\epsilon}R^{2b(k-1)}.
}                                                        \tag{1.2}
\]

The constants also depend on the fixed field, bad set, twists, tests and
support constants. Consequently this entire signed sector is of diagonal
size,

\[
\boxed{
 |S_\Theta(D,H,R)|\ll H D^{k+\epsilon}
 \quad\hbox{if}\quad R\le D^{1/(2b)}.
}                                                        \tag{1.3}
\]

The threshold in (1.3) is independent of the fixed moment order. Under
`PW_{7/8}`, it is `R <= D^(4/7)` at every `k >= 3`, or equivalently

\[
 N\gcd(n_i,m_j)\ge D^{3/7}\quad\hbox{for every cross pair}.
                                                               \tag{1.4}
\]

This is a gcd condition on arithmetic column ideals. It is not a statement
about the ordinate of a zeta zero.

## 2. Why graph charges apply to a signed sum

Here is the exact interface to the companion theorem. Choose two distinct
positions to receive native second-moment weights `alpha_i = 1/2`, and
put `alpha_i = b` at all other positions. Assign nonnegative real charges
`c_ij` to the edges of a fixed cross graph. Suppose every subset `I` with
`|I| >= 2` satisfies

\[
 \sum_{\{i,j\}\subseteq I}c_{ij}
 \le \sum_{i\in I}\alpha_i-1.                    \tag{2.1}
\]

Write `T = sum c_ij`. On the sector where every charged edge has gcd
at least `D/R`, the companion theorem proves

\[
 |S_\Theta|\ll H D^{\sum_i\alpha_i-T+\epsilon}R^T.
                                                               \tag{2.2}
\]

For clarity, this step does not put absolute values on the original
Möbius coefficients first. Freeze the shared ideals; their contribution
and `Theta` become bounded row multipliers. The finite forward Euler
correction removes pairwise coprimality between the remaining singleton
cores. Native row Cauchy on the two selected cores, and the pointwise
bounds on the others, give the weights `alpha_i`. For a shared ideal
`q_I`, the resulting denominator is `(Nq_I)^(sum_{i in I} alpha_i)`.
The gcd restrictions multiply it by at most

\[
 (R/D)^T\prod_{|I|\ge2}(Nq_I)^{
                 \sum_{\{i,j\}\subseteq I}c_{ij}}.
\]

Condition (2.1) leaves each shared-ideal exponent at least one. Finite
ideal harmonic sums cost only a fixed power of `log D`, absorbed into
`D^epsilon`. All singleton row cancellation occurs before this positive
accounting. This ordering permits the stated shared-incidence selector;
it gives no monotonicity for deleting arbitrary singleton tuples.

## 3. An explicit complete-bipartite charge

Choose both native second-moment positions on the unbarred side, say
`n_1,n_2`. For the complete bipartite graph on all cross pairs, put

\[
 B=b-\frac12,\qquad
 A=\frac{k-2b}{k(k-2)}.                            \tag{3.1}
\]

Assign charge `B` to every edge incident to `n_1` or `n_2`, and charge
`A` to all remaining cross edges. Both are nonnegative in the stated
range. There is no edge between the two selected positions, since they
are on the same side. The total charge is

\[
 T=2kB+k(k-2)A=2b(k-1).                            \tag{3.2}
\]

Meanwhile

\[
 \sum_i\alpha_i=1+2b(k-1).                         \tag{3.3}
\]

It remains to verify (2.1) for **every** subset, not only edges or the
whole graph. Let a subset contain `r` of the two selected positions,
`n` of the `k-2` other unbarred positions, and `t` barred positions.
Its slack in (2.1) is

\[
 F_r(n,t)=b(n+t)+\frac r2-1-t(nA+rB).              \tag{3.4}
\]

If it has no cross edge, its total vertex weight is at least one whenever
its cardinality is at least two. Thus those subsets satisfy (2.1).
Otherwise `t >= 1` and `n+r >= 1`. For each fixed `r`, (3.4) is bilinear
in `(n,t)`, so its minimum on the relevant rectangle occurs at a corner.
The complete corner list is as follows. Coincident corners when `k=3`
cause no problem.

| `r` | `(n,t)` | `F_r(n,t)` |
| --- | --- | --- |
| 0 | `(1,1)` | `(k-1)(2b(k-1)-k)/(k(k-2))` |
| 0 | `(1,k)` | `(k-1)(bk-2)/(k-2)` |
| 0 | `(k-2,1)` | `b(k-1+2/k)-2` |
| 0 | `(k-2,k)` | `k(2b-1)-1` |
| 1 | `(0,1)` | `0` |
| 1 | `(0,k)` | `(k-1)/2` |
| 1 | `(k-2,1)` | `b(k-2+2/k)-1` |
| 1 | `(k-2,k)` | `(k(2b-1)-1)/2` |
| 2 | `(0,1)` | `1-b` |
| 2 | `(0,k)` | `k(1-b)` |
| 2 | `(k-2,1)` | `b(k-3+2/k)` |
| 2 | `(k-2,k)` | `0` |

Every entry is nonnegative for `k >= 3` and
`k/(2(k-1)) <= b <= 1`. Here is a direct check of the less immediate
ones. At the lower endpoint `b_0 = k/(2(k-1))`, the first entry is zero,
and

\[
 b_0k-2=\frac{(k-2)^2}{2(k-1)}\ge0,
\]

\[
 b_0(k-1+2/k)-2
 =\frac{(k-2)(k-3)}{2(k-1)}\ge0,
\]

\[
 k(2b_0-1)-1=\frac1{k-1}>0,
\]

\[
 b_0(k-2+2/k)-1
 =\frac{(k-2)^2}{2(k-1)}\ge0.
\]

These expressions increase with `b`; the entries involving `1-b` remain
nonnegative up to `b=1`. This proves all the corner inequalities, hence
all subset constraints (2.1), for every fixed order in the stated range.
It is an algebraic proof with arbitrary `k`, not extrapolation from a
finite enumeration.

Insert (3.2)--(3.3) into (2.2) to prove (1.2). Finally,
`R^(2b(k-1)) <= D^(k-1)` under the condition in (1.3), proving that
corollary. This completes the proof.

## 4. What the new sector adds, and what it leaves

The forest corollary in the companion note controls any connected
cross-gcd graph at diagonal size for `R <= D^(1/2)`. The present theorem
uses the additional edges of a complete cross graph to reach
`R <= D^(1/(2b))`. At `b=7/8`, this enlarges the cutoff exponent from
`1/2` to `4/7`, a difference of `1/14`. The underlying gcd threshold
falls from `D^(1/2)` to `D^(3/7)`. No power of `D` depending unfavorably
on the moment order has been hidden in this statement.

The sector can contain tuples without a global common prime, even within
the stated diagonal-size range. To see the incidence pattern, take `2k`
mutually coprime squarefree labels `c_v` of comparable norm `L`, and put
the column at position `v` equal to the product of all labels except
`c_v`. The column norms have scale `D = L^(2k-1)` and every pairwise gcd
has scale `D^((2k-2)/(2k-1))`, while the gcd of all columns is one. These
gcds exceed the threshold `D^(1-1/(2b))` for the parameter range here,
up to the fixed support constants. Thus the proof cannot be replaced by
extracting one common factor from all `2k` columns. The weighted subset
constraints account for this possibility. This example describes a
compatible incidence pattern; it is not used as an analytic input.

The requirement that all cross gcds be large is substantial. In
particular, when `R < D`, a tuple whose `2k` columns are pairwise coprime
is outside this sector and has no charged edge. At the endpoint `R = D`,
every gcd condition is automatic and (1.2) reduces to the original
two-axis bound `H D^(1+2b(k-1)+epsilon)`. The generalized moment requires a
signed estimate for that complementary region and the other retained
conductor pieces. Neither the sector bound nor the fact that it holds at
every fixed order supplies this missing estimate.

The result is compatible with the repository's cofinal-moment route but
does not complete it: the constants here may depend on `k`, and the
whole-moment defect still has no sublinear all-order bound. The current
source-conditional zero-free boundary remains unchanged.

## 5. Verification boundary

`checks/check_graph_charges.py` checks the corner identities and every
subset inequality in declared finite examples using exact rational
arithmetic. Its finite coverage is diagnostic only. The all-order proof
is Sections 2--3, with the analytic singleton-cancellation input supplied
by the explicitly stated companion lemma and its pinned sources. No
proof-assistant verification, human peer review, or RH certification is
claimed.
