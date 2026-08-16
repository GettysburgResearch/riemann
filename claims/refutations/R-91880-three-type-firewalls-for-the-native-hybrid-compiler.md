# R-91880 — Three mandatory type firewalls for a native hybrid factor-67 compiler

Claim ID: `R-91880`  
Status: **PROVED EXACT SUPERSESSION / NORMALIZATION FIREWALL**  
Created: 2026-08-16  
Frozen predecessor: PR #506 at `3d44cf10f8b5f36fd06a57a745550a25142e3658`  
Comparison inputs: PR #507 at `dfaa70cd2eefcabbf6717e3da060792904c7f357`; PR #509 at `e01daee9cdfea35d2a7d2591f1df6c8080084119`; review PR #503 at `db77e5792966edf080604fd4b69fb00f07739681`  
RH status: **unproved**

## 1. The forced `x=2` Hall edge has negative declared-score correction

At the compact fibre `x=2`, the target-Hall graph has the forced edge

\[
 o=2\longrightarrow e=1.
\]

With `z=sqrt(x/k)`, the target and declared score per source unit are

\[
 T(z)=4z-3,
 \qquad
 S(z)=5z-3,
\]

so the score per target unit is

\[
 g(z)=\frac{5z-3}{4z-3},
 \qquad
 g'(z)=-\frac3{(4z-3)^2}<0.
\]

Hence

\[
\boxed{
 g(\sqrt2)-g(1)
 =\frac{3(1-\sqrt2)}{4\sqrt2-3}<0.
}
\tag{R-91880.1}

Therefore a nonzero Hall edge cannot simultaneously be target-null, exact in declared score, nonnegative in every component row, and positive in one complete target/score/row packet cone.

The valid output is two-sorted:

```text
positive target-bearing residual source;
current-only nonnegative physical row bonus.
```

The residual is target-exact and score-superordinate. The bonus has zero source target and no inherited declared-score coordinate.

## 2. The Volterra infinitesimal row is not a canonical causal source packet

The exact directed witness from the frozen review of PR #495 is

```text
p = 67,
child endpoint = 15,
parent endpoint = 1005,
row = 14,
```

with

\[
-\frac{184291}{10^9}
< p_{1005}(14)-67^{-1/2}p_{15}(14)
< -\frac{184290}{10^9}<0.
\tag{R-91880.2}
\]

Thus the positive infinitesimal Volterra row `p_s` may not be fed into the canonical causal-difference theorem. In the successor it is used only as an outer positive row-valued endpoint feature. All rough ownership and causal children live in the exact finite native source-tree sector.

## 3. The row-first `P_61` rough lift is not the native input marginal

The native construction splits the paired arithmetic source before observation. The row-first rough lift observes first and then adds a positive response reservoir. These operations do not commute after labels are erased.

At detail column `q=2`, the complete rough lift has the exact lower separator

\[
\Theta_{P,X}(2)-\Omega_X(2)
\ge\frac{\log4}{\sqrt{134}}
>\frac19
>\frac{109}{1200}
\qquad(X\ge536).
\tag{R-91880.3}

The first strict inequality follows from `log 4>4/3` and `sqrt(134)<12`. Therefore the parent marginal in the successor is the exact hybrid native Möbius marginal, never the row-first rough lift.

## 4. Consequence

The only admissible composition is:

```text
inner exact finite native occurrences
    -> stopping-line / first-owner / causal tree
    -> positive residual source + row-only leaf bonus;

outer exact Volterra native occurrences
    -> rank-one common-feature cancellation
    -> positive row-valued residual, with no causal split;

signed finite/continuum defect
    -> observation ledger only.
```

Any successor that violates one of the three firewalls is rejected before its capacity estimates are considered.

```text
complete target-null Hall packet                false
Volterra p_s canonical causal difference        false
P61 row-first rough lift as native parent        false
native finite source tree                        retained
outer rank-one positive row                      retained
Riemann Hypothesis                               unproved
```
