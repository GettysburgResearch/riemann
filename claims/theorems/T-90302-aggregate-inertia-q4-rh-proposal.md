# T-90302 — Aggregate-inertia Q4 recurrence as a complete RH proof proposal

Claim ID: `T-90302`  
Title: The exact two-state Q4 reflected ledger, combined with aggregate inertia elimination, yields a coefficient-one fixed-delay recurrence and the Riemann Hypothesis  
Status: **FULL PROPOSED PROOF COMPOSITION — DEPENDENCIES AND ASSEMBLY REQUIRE INDEPENDENT REVIEW; RH NOT ACCEPTED**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-10  
Dependencies: `L-90301`–`L-90305`; PR #341 `L-34007/L-34008/L-34009`; PR #345 `L-34401/L-34406/L-34409/L-34410`; PR #346 `L-34401/L-34402`; PR #350 corrected source order and `L-34412`; resident vector-valued pole-energy criterion  
Scope: corrected compact Q4 / critical-Haar route

## 1. Exact state and physical block

Use the compact relative source

\[
B_\sharp(s)=\frac{1-4^{1-s}}{\zeta(s)}
\]

and the source-complete relative Jordan state of PR #345. On every sufficiently deep balanced physical row its bare coordinate vanishes exactly, and its curvature matrix is

\[
K_e=
\begin{pmatrix}
R_e&-\frac12(T_e-2E_eI_e)\\[1mm]
-\frac12\overline{(T_e-2E_eI_e)}&|I_e|^2
\end{pmatrix}.
\tag{T-90302.1}
\]

Here:

\[
R_e=\Delta_4R_\sharp(e)\asymp n\log n
\]

is the deterministic source-matched moat;

\[
E_e=O(\log n)
\]

is the relative generalized-prime score;

\[
I_e
\]

is the sole RH-sensitive current innovation;

and

\[
T_e=O(n\log n)
\]

is the source second-current coordinate.

The exact continuous physical/carry placement aggregates these matrices with nonnegative cell weights. Denote the resulting unit-logarithmic-block matrix by

\[
K_J.
\]

## 2. The former final gap is closed at aggregate level

The Claude-inspired inertia theorem `L-90301` showed that full polarized positivity was unnecessary, but `T-90301` still left the negative spectral mass

\[
\delta(J)=\operatorname{tr}(K_J)_-
\]

as an open arithmetic estimate.

`L-90304/L-90305` prove unconditionally from the declared source estimates that

\[
\boxed{
\delta(J)\ll (1+J)^A
}
\tag{T-90302.2}
\]

for one fixed exponent `A`; the written proof gives `A=1` under the conservative second-current bound.

This estimate is independent of the unknown current energy. It follows from the exact aggregate determinant inequality

\[
\delta(K_J)
\le
\frac{|U_J|^2}{4(A_J-F_J)},
\]

with

\[
A_J\gg J,\qquad
F_J\ll J^2e^{-J},\qquad
U_J\ll J.
\]

Thus the RH-sensitive current can be arbitrarily large without increasing the bad spectral direction beyond polynomial size.

## 3. Current-scale synthesis

The compact Q4/parity synthesis is parameter independent and has strict current-scale charge. In the normalization of PR #346,

\[
W^*W\le qI,
\qquad
q<\frac25.
\tag{T-90302.3}
\]

For the complete block curvature,

\[
K_{WV}=WK_JW^*.
\]

`L-90301` therefore gives

\[
\operatorname{tr}K_{WV}
\le
q\left[\operatorname{tr}K_J+\delta(J)\right].
\tag{T-90302.4}
\]

Every source species in this inequality is already typed in the existing exact ledger:

- the compact current is reconstructed by the parity pair;
- the derivative gauge is a strict-delay ordinary Möbius boundary;
- the Q4 bare gauge is delayed by `log 4`;
- the adaptive critical-Haar bank has only the current state and one predecessor state;
- all higher generalized-prime channels affect forcing but not dynamic source dimension;
- product and individual reflected terms form the same two-state curvature;
- endpoint collars have fixed width and polynomial cost.

No source term is discarded before the reflected subtraction.

## 4. Coefficient-one fixed-delay recurrence

Insert (T-90302.2) into the exact two-state reflected/all-pass block telescope of PR #341 and the compact/parity synthesis of PRs #345/#346. The strict current-scale charge is absorbed by the unused paired reserve; the only coefficient-one return is the declared predecessor state.

Consequently the RH-sensitive block energy satisfies

\[
\boxed{
\mathcal E(J)
\le
\mathcal E(J-\log2)
+
C(1+J)^B
}
\tag{T-90302.5}
\]

for every sufficiently large `J`, with one fixed `B`.

The polynomial term contains:

1. the aggregate inertia defect (T-90302.2);
2. fixed endpoint collars;
3. delayed Möbius/bare gauges;
4. the finite low-row table;
5. unbalanced rows routed by the existing strict-scale ledger.

There is no current-scale coefficient exceeding one and no source-blind strict contraction of the principal zeta mode.

## 5. Polynomial energy

Iterating (T-90302.5) over

\[
O(J)
\]

fixed predecessor steps gives

\[
\boxed{
\mathcal E(J)=O((1+J)^{B+1}).
}
\tag{T-90302.6}
\]

In particular,

\[
\mathcal E(J)=e^{o(J)}.
\]

## 6. Pole exclusion

The compact source multiplier

\[
1-4^{1-s}
\]

has zeros only on `Re s=1`, and therefore cancels no nontrivial zeta zero in the open critical strip. The resident vector-valued Mellin/Hardy pole criterion converts

\[
\mathcal E(J)=e^{o(J)}
\]

into exclusion of every zeta zero with real part greater than one half.

Functional-equation symmetry then gives

\[
\boxed{\mathrm{RH}.}
\tag{T-90302.7}
\]

Thus the proposed proof chain is

\[
\boxed{
\begin{aligned}
&\text{exact compact Q4 source and two-state reflected ledger}\\
&+\text{critical }n\log n\text{ reserve}\\
&+\text{aggregate current-free inertia estimate}\\
&+\text{strict current-scale parity synthesis}\\
&+\text{coefficient-one predecessor telescope}\\
&\Longrightarrow
\text{polynomial pole-current energy}\\
&\Longrightarrow\mathrm{RH}.
\end{aligned}}
\tag{T-90302.8}
\]

## 7. Why this is not the old circular local Schur gate

The previous local target was

\[
|I_e|^2\le R_e
\]

for every row. That statement directly controls the RH-sensitive current and is itself RH-bearing.

The aggregate proof never establishes it. It allows arbitrary local failures and arbitrary indefinite row matrices. Its only new estimate concerns

\[
\operatorname{tr}\left(\sum_e w_eK_e\right)_-,
\]

and that estimate is derived from source-only quantities after the current-dependent correlation is optimized out.

Similarly, the proof does not claim that the Q4 all-pass factor contracts an off-line functional-equation pair. `R-90301` correctly refutes that shortcut.

## 8. Exact review frontier

This file is presented as a complete **proof proposal**, not as an accepted proof. A reviewer should reconstruct the chain in this order:

1. `L-90304` aggregate determinant theorem;
2. `L-90305` physical-block estimates and weights;
3. `L-90301` inertia-tolerant synthesis;
4. PR #350 `L-34412` exact curvature congruence;
5. PR #346 finite synthesis and strict charge;
6. PR #341 two-state product/individual ledger;
7. PR #345 compact relative source, zero bare coordinate, and critical moat;
8. fixed collars and delayed gauges;
9. the resident pole-energy consumer.

Reject the proposal if any of the following occurs:

- the physical row weights are not nonnegative or not the declared `n^{-2}` normalization;
- a row-dependent centering shear is used;
- `T_e` lacks the stated source-bound polynomial estimate;
- the synthesis acts before the aggregate in a way that prevents `K_{WV}=WK_JW^*`;
- the strict current-scale reserve is spent twice;
- a delayed gauge is silently returned at current scale;
- the pole criterion uses a source zero that cancels an off-line zeta pole.

## 9. Status

```text
Claude-style inertia synthesis                    PROPOSED COMPLETE EXACT
aggregate determinant/current elimination         PROPOSED COMPLETE EXACT
balanced Q4 block negative inertia                PROPOSED COMPLETE COFINAL
compact/parity strict current-scale synthesis      IMPORTED / REVIEW
complete Q4 two-state reflected ledger             IMPORTED / REVIEW
collar and delayed-state composition               IMPORTED / REVIEW
coefficient-one recurrence                         PROPOSED COMPLETE COMPOSITION
recurrence -> polynomial energy -> RH              PROPOSED COMPLETE
accepted proof of RH                               NO — INDEPENDENT REVIEW REQUIRED
```
