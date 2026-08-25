# Genus-one q-versus-symmetric-power phase diagram

## Status and scope

**Status:** exact bounded exploration from source-locked histograms, with a
separate analytic Haar comparator.

**Scope:** the uniform-model genus-one family at exactly `q=3,5,7` and
symmetric powers `0<=r<=32`.  No finite field, curve, polynomial, or fresh
model is enumerated.

**Exact sources or dependencies:** `genus1_cubic_family_laws.json` and
`ELLIPTIC_SYMMETRIC_POWER_HIGH_RANK_HAAR_LIMIT.md`, pinned by LF-normalized
SHA-256 in the producer and payload.  The primitive genus-one payload hash is
also pinned and internally replayed.

**What was actually run:** exact Dickson recurrences on the 27 locked source
histogram atoms, producing 891 rank-atom visits, plus exact integer and
rational aggregations.

**Smallest remaining gap:** any genuine arithmetic interchange of `q` and
`r` would require a q-aspect equidistribution theorem uniform enough for
growing `r`; none is asserted here.

The frozen finite facts below and the compact-Haar asymptotics are deliberately
separate.  In particular, no trend through three fields is promoted to an
all-q statement.

## 1. Exact normalization and diagnostics

For a locked geometric trace

\[
 t=a_D=q+1-\#E_D(\mathbf F_q),\qquad
 L_D(T)=1-tT+qT^2,
\]

put

\[
 S_0=1,\quad S_1=t,\quad
 S_r=tS_{r-1}-qS_{r-2},\qquad
 x_r=q^{-r/2}S_r.
\]

Thus `x_r=U_r(t/(2sqrt(q)))` is the normalized `Sym^r` trace.  Although
`x_r` itself can involve `sqrt(q)`, every square

\[
 x_r^2={S_r(t,q)^2\over q^r}
\]

is rational.  This lets the producer compute, without rounding:

- the negative, zero, and positive masses;
- strict tails `|x_r|>1,2,3,4`;
- the bounded transforms
  `E[min(x_r^2,1)]`, `E[min(x_r^2,4)]`, and
  `E[min(x_r^2,16)]`;
- raw moments of orders `2,4,6`;
- endpoint-trimmed moments, where both observed source classes
  `t=+/-t_max` are deleted and the remaining mass is renormalized;
- the unrenormalized endpoint contribution and its share of each raw moment.

Here “endpoint” always means the two **extreme observed trace classes**, not a
Hasse endpoint.  All fractions in the JSON are reduced pairs
`[numerator,denominator]`; it contains no binary floats.

## 2. The fixed-q phase has a hard character cutoff

The complete consumed supports are:

| q | model mass | trace atoms | `t_max` | mass at `|t|=t_max` | uniform bound on `x_r^2` |
|---:|---:|---:|---:|---:|---:|
| 3 | 18 | 7 | 3 | `1/9` | `4` |
| 5 | 100 | 9 | 4 | `1/10` | `5` |
| 7 | 294 | 11 | 5 | `1/21` | `28/3` |

Indeed every atom has `t^2<4q`.  Writing `t=2sqrt(q)cos(theta)` gives the
rank-uniform exact bound

\[
 |x_r|^2
 ={\sin^2((r+1)\theta)\over\sin^2\theta}
 \le {4q\over4q-t^2}
 \le {4q\over4q-t_{\max}^2}.
 \tag{1}
\]

Consequently `P_q(|x_r|>4)=0` for every rank, simultaneously at all three
locked fields.  At `q=3` the sharper strict tail `P_3(|x_r|>2)` is always
zero.  These are exact support statements, not observations from the rank
cap.

## 3. One exact cross-q slice

At `r=2`, the diagnostics are already sharply endpoint-sensitive:

| q | `E[min(x^2,1)]` | `E[min(x^2,4)]` | count with `|x|>2` | raw `E[x^4]` | endpoint share of `E[x^4]` | endpoint-trimmed `E[x^4]` |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | `14/27` | `23/27` | `0/18` | `503/243` | `432/503` | `71/216` |
| 5 | `71/125` | `217/250` | `10/100` | `8459/3125` | `1331/1538` | `253/625` |
| 7 | `86/147` | `877/1029` | `14/294` | `48047/16807` | `34992/48047` | `1119/1372` |

Thus the small extreme-trace masses contribute respectively about 86%, 87%,
and 73% of the fourth moment in this one slice.  The capped transforms remain
bounded by construction.  The exact fractions, rather than those display-only
percentages, are the claims.

Across the entire declared cap the largest endpoint shares of the fourth
moment are:

| q | rank | exact endpoint share | display approximation |
|---:|---:|---:|---:|
| 3 | 9 | `1162261467/1163419244` | `0.999005` |
| 5 | 22 | `113569194615186406896871905621841/126405984394988239400887513953418` | `0.898448` |
| 7 | 12 | `12467261263346438421601/13371541175844726981621` | `0.932373` |

This is the finite-family analogue of the endpoint warning in the Haar note:
raw high moments can be almost entirely determined by a tiny source class.
The trimmed columns in the payload show what remains after that class is
removed; no robustness claim is inferred from any single trim rule.

## 4. Exact finite-q resonances

There are two visible mechanisms.

First, `t=0` occurs with masses `2/9`, `1/5`, and `1/7`.  Pointwise,

\[
 S_r(0,q)=0\quad(r\text{ odd}),\qquad
 x_{2k}(0)^2=1.
 \tag{2}
\]

Because the source histograms are centrally symmetric and
`S_r(-t,q)=(-1)^rS_r(t,q)`, every odd-rank row in the declared cap has equal
positive and negative mass.  Its zero mass is exactly the `t=0` mass, except
for the following `q=3` resonance.

At `q=3`, the two extreme traces `t=+/-3` have angles `pi/6` and `5pi/6`.
Their combined mass is `1/9`, and their squared character is periodic in
`N=r+1`:

| `N mod 6` | 0 | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|---:|
| `x_r^2` | 0 | 1 | 3 | 4 | 3 | 1 |

Hence the extreme class is annihilated at
`r=5,11,17,23,29` within the cap (and, from the displayed identity, whenever
`r=5 mod 6`).  At `r=5` its fourth-moment share is exactly zero, in contrast
with `432/503` at `r=2`.  The `q=3` odd-rank zero mass therefore jumps from
`2/9` to `1/3` on this congruence class.

The bounded exact scan finds no other nonzero trace atom with `S_r=0` through
`r=32` at `q=5` or `q=7`.  That last sentence is only a bounded scan result,
not a cyclotomic classification.

Even-rank signs oscillate rather than obeying a q-monotone pattern.  For
example, the `(negative,zero,positive)` counts at `r=32` are respectively
`(8,0,10)`, `(30,0,70)`, and `(70,0,224)` for `q=3,5,7`.  These are frozen
counts, not evidence for a limiting sign law.

## 5. Raw moments do not enter the Haar high-rank phase at fixed q

Equation (1) proves more than the bounded scan.  For every real `p>3` and
each one of the three fixed histograms,

\[
 {\mathbb E_q|x_r|^p\over(r+1)^{p-3}}\longrightarrow0.
 \tag{3}
\]

By contrast, character orthogonality together with the pinned Haar note gives

\[
 \mathbb E_{SU(2)}\chi_r^4=r+1,
 \qquad
 \mathbb E_{SU(2)}|\chi_r|^6\sim\tfrac12(r+1)^3,
 \tag{4}
\]

and `chi_r` converges weakly to the unbounded law
`W=sin(U)/sin(Theta)`, whose tail is asymptotic to
`16/(9pi^2)x^(-3)`.  Therefore each fixed locked histogram is in a genuinely
different high-rank phase: its scaled raw moments vanish and every
subsequential distribution remains inside a fixed compact interval, while
the Haar boundary law is unbounded and has positive scaled moment constants.
The exact fourth-moment identity in (4) is also immediate from
`chi_r^2=chi_0+chi_2+...+chi_(2r)` and character orthonormality, so it does not
depend on a numerical Haar calculation.

This is a rigorous **fixed-histogram versus Haar high-rank nonuniformity**.
It is not, by itself, an arithmetic order-of-limits theorem.  A hypothetical
fixed-rank q-aspect equidistribution theorem would make the q-first route
inherit the Haar fourth-moment ratio `1`.  This packet establishes only that
the rank-first ratio is `0` separately for each of its three locked
histograms; three fields do not define the remaining outer q-limit.  Thus no
pair of arithmetic iterated limits is evaluated here.  No q-aspect premise,
and especially no uniform growing-r version, is proved or assumed.

## 6. Bounded-cap phase diagram and firewall

Raw fourth moments are visibly nonmonotone within the cap.  For display only,
their exact rational ranges are summarized by decimals:

| q | minimum (rank) | maximum (rank) | first adjacent decrease |
|---:|---:|---:|---:|
| 3 | `0.065265` (29) | `2.959292` (20) | `2 -> 3` |
| 5 | `0.179863` (25) | `3.443174` (23) | `2 -> 3` |
| 7 | `0.394064` (17) | `5.903370` (32) | `4 -> 5` |

The payload retains the exact fractions, all 99 rank rows, capped-transform
extrema, sign and tail counts, trimmed moments, endpoint contributions, and
the fourth- and sixth-moment Haar scalings at `r=8,16,32`.

Nothing here proves an all-q law, convergence in q, a rate, uniform
equidistribution, monodromy, automorphy, a compatible family, an Euler-product
statement, or any conclusion about zeros, RH, or GRH.  The Haar theorem is an
analytic compact-group comparator; the `q=3,5,7` tables are exact finite facts.

## 7. Replay

From the repository root, the deterministic fixture and tests replay in both
normal and optimized Python modes with explicit paths:

```text
python research/l-families/atlas/function_field/genus1_qr_symmetric_power_phase_diagram.py --check research/l-families/atlas/function_field/genus1_qr_symmetric_power_phase_diagram.json
python -O research/l-families/atlas/function_field/genus1_qr_symmetric_power_phase_diagram.py --check research/l-families/atlas/function_field/genus1_qr_symmetric_power_phase_diagram.json
python tests/test_genus1_qr_symmetric_power_phase_diagram.py
python -O tests/test_genus1_qr_symmetric_power_phase_diagram.py
```
