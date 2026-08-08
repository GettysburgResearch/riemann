# R-30402 — The zeroth Euler common tail has square-root atomic mass

Claim ID: `R-30402`  
Title: The positive stopped-power layer cake contributes an explicit `Omega(sqrt X)` zeroth-jet source to the terminal adjacent-commutator norm, so the polylogarithmic composition in `L-30403/T-30401` is false as written  
Status: **EXACT HYPOTHESIS-MATCHING REFUTATION OF THE FROZEN TERMINAL-NORM CLAIM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Primary targets: `L-30403.6--.9`, `T-30401.4--.8`  
Dependencies: PR #286 `L-28402`; PR #301 `L-29801/L-29808`; PR #303 `L-30202`; elementary inequalities  
Scope: the proposed absolute terminal lift of the complete Euler boundary source; it does not refute the adjacent-commutator identity itself or every possible coupled repair

## 1. The claimed polylogarithmic source norm

PR #304 defines, at every cascade depth, a divisor-source vector

\[
 \sigma_a=(\sigma_a(m))_{m\ge2}
\]

and the atomic norm

\[
 \|\sigma_a\|_{\rm at}
 =\sum_m\sqrt m\,|\sigma_a(m)|.
\tag{R-30402.1}
\]

Its proposed completion requires

\[
 \sum_a\|\sigma_a\|_{\rm at}
 =O((1+\log X)^B).
\tag{R-30402.2}
\]

Every emitted source is then terminated by the signed adjacent-tree map

\[
 \Phi(\sigma)=\sum_m\sigma(m)E_{m-1}.
\]

The adjacent-tree map is exact. The failure is earlier: the complete boundary source placed into (R-30402.1) is not polylogarithmic.

## 2. Positive stopped-power resolution

The critical target has the exact positive decomposition

\[
 q^{-1/2}\log(X/q)
 =\sum_{Y=q}^{X-1}\ell_Y q^{-1/2},
 \qquad
 \ell_Y=\log\frac{Y+1}{Y}>0.
\tag{R-30402.3}
\]

It is therefore enough to inspect the first boundary generation of one stopped pure-power layer at endpoint `Y` and then sum with the positive weights `ell_Y`.

For the actual shifted parity source used in PRs #303--#304, put

\[
 A_k(q)=\frac{(2kq-1)^{-1/2}}{2k},
 \qquad
 B_k(q)=\frac{((2k+1)q)^{-1/2}}{2k+1}.
\tag{R-30402.4}
\]

The source pair at index `k` is

\[
 A_k(q)e_{2k}-B_k(q)e_{2k+1}.
\tag{R-30402.5}
\]

## 3. A macroscopic family with common first omitted index two

For each integer `Y`, define

\[
 I_Y=
 \left\{
 q\in\mathbb Z:
 \left\lfloor\frac{Y+1}{4}\right\rfloor+1
 \le q\le
 \left\lfloor\frac Y3\right\rfloor
 \right\}.
\tag{R-30402.6}
\]

For every `q in I_Y`,

\[
 2q-1\le Y,
 \qquad
 3q\le Y,
 \qquad
 4q-1>Y,
 \qquad
 5q>Y.
\tag{R-30402.7}
\]

Hence the shifted-even and unshifted-odd omitted tails start together at

\[
 K_e=K_o=2.
\tag{R-30402.8}
\]

This is not an unmatched collar. It is part of the common Hausdorff tail which `L-30403/T-30401` places into the terminal source ledger.

## 4. The zeroth Euler jet

The exact Euler transformation has zeroth coefficient `1/2`. Thus the first common-tail jet contains

\[
 \frac12A_2(q)e_4
 -\frac12B_2(q)e_5.
\tag{R-30402.9}
\]

Here

\[
 B_2(q)=\frac1{5\sqrt{5q}}.
\tag{R-30402.10}
\]

The contribution of its odd source coordinate to the atomic norm is therefore exactly

\[
 \sqrt5\,\frac12 B_2(q)
 =\frac1{10\sqrt q}.
\tag{R-30402.11}
\]

All stopped-layer weights are positive. Every occurrence in this family has the same negative sign at source node `5`; common-destination recombination adds these coefficients and cannot cancel them. Therefore the complete first-generation source obeys

\[
 \boxed{
 \|\sigma_0\|_{\rm at}
 \ge
 \sum_{Y=\lceil X/2\rceil}^{X-1}
 \ell_Y
 \sum_{q\in I_Y}\frac1{10\sqrt q}.
 }
\tag{R-30402.12}
\]

This lower bound uses only one Euler order, one source node, and the upper half of the positive stopped-endpoint layer cake.

## 5. Explicit square-root lower bound

For `Y>=48`,

\[
 |I_Y|
 =\left\lfloor\frac Y3\right\rfloor
  -\left\lfloor\frac{Y+1}{4}\right\rfloor
 \ge\frac Y{24}.
\tag{R-30402.13}
\]

Also

\[
 \ell_Y=\log(1+1/Y)
 \ge\frac1{Y+1}
 \ge\frac1{2Y},
\tag{R-30402.14}
\]

and for `q<=Y/3`,

\[
 \frac1{\sqrt q}\ge\sqrt{\frac3Y}.
\tag{R-30402.15}
\]

Consequently each endpoint in the upper half contributes

\[
 \ell_Y\sum_{q\in I_Y}\frac1{10\sqrt q}
 \ge
 \frac{\sqrt3}{480\sqrt Y}.
\tag{R-30402.16}
\]

For `X>=96`, summing over `ceil(X/2)<=Y<X` gives

\[
 \boxed{
 \|\sigma_0\|_{\rm at}
 \ge c\sqrt X,
 \qquad
 c=\frac1{1000}.
 }
\tag{R-30402.17}
\]

The displayed constant is deliberately weaker than the preceding elementary bounds.

In particular, for every fixed `B`,

\[
 \|\sigma_0\|_{\rm at}
 \ne O((\log X)^B).
\tag{R-30402.18}
\]

This contradicts `L-30403.6/.8` and therefore invalidates `T-30401.4--.8`.

## 6. Why the divisor-switch estimate does not cover this channel

`L-30403.3` assigns every complete boundary coefficient the decay

\[
 n^{-3/2}\operatorname{polylog}(X/n).
\tag{R-30402.19}
\]

The zeroth common-tail odd coefficient above is instead

\[
 B_2(q)\asymp q^{-1/2}
\tag{R-30402.20}
\]

at fixed parity index `k=2`. It lacks the extra factor `q^{-1}` required by the proposed divisor switch.

Finite differences of positive order and the damped Euler remainder may have additional decay, but the zeroth Euler jet is always present with coefficient `1/2`. It cannot be assigned the bound (R-30402.19).

## 7. The adjacent-commutator lemma survives at its true scope

This refutation does not contradict

\[
 L_q(E_{m-1})=\mathbf1_{q\mid m}
\]

or

\[
 \mathcal N_\omega(\Phi(\sigma))
 \le24\|\sigma\|_{\rm at}.
\]

Those are useful exact theorems. They show precisely why the proposed completion fails: applying the absolute lift to the entire zeroth common-tail source costs at least square-root scale.

A successful proof must treat that channel before the atomic absolute value, for example by an exact source-bound relative capacity, a coupled Pascal-cycle cancellation, or another complete signed recombination. Calling the remaining check a finite manifest replay is insufficient.

## 8. Corrected status

```text
adjacent-tree divisor-source identity          RETAINED
24 sqrt(m) absolute lift                       RETAINED
polylog norm for the complete boundary source  FALSE
terminal lift of every emitted source           REJECTED AS COMPLETION
T-30401 as a proof of RH                        REJECTED
source-bound zeroth-jet cancellation            OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```

## 9. Proof boundary

Refuted exactly:

1. the claim that the complete first-generation Euler source has polylogarithmic atomic norm;
2. the all-generation consequence obtained by summing those norms;
3. the complete terminal-commutator proof at the frozen PR #304 head.

Not refuted:

1. a coupled repair which does not take the zeroth common-tail atomic norm;
2. Cycle Debt as an abstract criterion;
3. RH.
