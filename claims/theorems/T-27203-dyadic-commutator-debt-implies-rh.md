# T-27203 — Dyadic commutator debt contraction implies RH

Claim ID: `T-27203`  
Title: A polylogarithmic paired odd-commutator excess gives Cycle Debt, the sharp prime ramp, and the Riemann Hypothesis  
Status: **FULL CONDITIONAL PROPOSAL — DYADIC COMMUTATOR DEBT OPEN / RH-BEARING**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27203`, `L-27205`, `L-27207`, `L-27208`, `T-27202`  
Scope: one explicit finite half-scale contraction theorem; no unconditional RH claim

## 1. Optimized debt

Fix one \(0<\eta\le1/4\). Let

\[
\mathfrak N_\eta(X)=\min_{\partial d=r_X}\sum_e\omega_e(-d_e)_+
\tag{T-27203.1}
\]

be the optimized balanced Cycle Debt of `L-27205`.

For an exact lower flow \(d\) at endpoint \(Y\), let \(d_{2Y}^{\mathrm{com}}(d)\) be the exact commutator lift of `L-27207.23`. Let \(C_{\eta,2Y}\) be the complete balanced fundamental-cycle matrix of `L-27204` at endpoint \(2Y\). Define

\[
\boxed{
\mathfrak E_\eta(Y;d)=\min_z\left[\mathcal N_\omega\bigl(d_{2Y}^{\mathrm{com}}(d)+C_{\eta,2Y}z\bigr)-\frac12\mathcal N_\omega(d)\right]_+.
}
\tag{T-27203.2}
\]

Every object in (T-27203.2) is finite:

- the exact Möbius target divergence;
- the doubled lower flow;
- the bottom charge \(w_{2Y}(2)T_2\);
- every odd-node commutator \(r_{2Y}(2a+1)E_{2a}\);
- the complete balanced cycle basis;
- the source-adapted capacity metric.

No kernel positivity or asymptotic operator statement occurs in its definition.

## 2. Dyadic Commutator Debt theorem

The sole proposed closing theorem is:

> **DCD.** There are absolute constants \(A,C\) such that, for every \(Y\ge2\), one can choose an exact balanced flow \(d_Y\) satisfying
>
> \[
> \mathcal N_\omega(d_Y)\le\mathfrak N_\eta(Y)+1
> \tag{T-27203.3}
> \]
>
> and
>
> \[
> \boxed{\mathfrak E_\eta(Y;d_Y)\le C\log^A(2Y).}
> \tag{T-27203.4}
> \]

DCD is source specific. It is not a generic statement about all divergences or all balanced flows.

The factor \(1/2\) in (T-27203.2) is forced by the exact even-column capacity identity `L-27207.28`--`L-27207.29`; it is not an adjustable contraction constant.

## 3. Even-endpoint recurrence

Apply DCD and the definition of optimized debt:

\[
\begin{aligned}
\mathfrak N_\eta(2Y)
&\le\mathcal N_\omega\bigl(d_{2Y}^{\mathrm{com}}(d_Y)+C_{\eta,2Y}z_Y\bigr)\\
&\le\frac12\mathcal N_\omega(d_Y)+C\log^A(2Y).
\end{aligned}
\]

Using (T-27203.3),

\[
\boxed{\mathfrak N_\eta(2Y)\le\frac12\mathfrak N_\eta(Y)+C\log^A(2Y)+\frac12.}
\tag{T-27203.5}
\]

This is a strict half-scale contraction of the actual RH-bearing debt.

## 4. Odd endpoints cost nothing asymptotically

`L-27208` proves

\[
\boxed{\mathfrak N_\eta(X)\le\mathfrak N_\eta(X-1)+\frac{16(1+\log X)}{\sqrt{X-1}}.}
\tag{T-27203.6}
\]

Therefore a strong induction using (T-27203.5) at even endpoints and (T-27203.6) at odd endpoints gives

\[
\boxed{\mathfrak N_\eta(X)=O(\log^{A'}(2X))}
\tag{T-27203.7}
\]

for one fixed \(A'\). Indeed every two induction steps divide the endpoint by two, while the unit-increment errors form a convergent geometrically rescaled ledger.

In particular,

\[
\boxed{\mathfrak N_\eta(X)=X^{o(1)}.}
\tag{T-27203.8}
\]

Thus DCD implies the Cycle Debt Theorem.

## 5. Prime ramp and RH

`L-27205` gives

\[
|P_X-W_X|\le A_\eta\left(K_X+2\mathfrak N_\eta(X)\right),
\tag{T-27203.9}
\]

where

\[
P_X=\sum_{p^a\le X}\frac{\Lambda(p^a)}{\sqrt{p^a}}\log\frac X{p^a},
\tag{T-27203.10}
\]

\[
W_X=\sum_{q=2}^{X}q^{-1/2}\log(X/q)=4\sqrt X+O(\log X),
\tag{T-27203.11}
\]

and \(K_X=O(\log^2X)\). Hence (T-27203.7) yields

\[
\boxed{P_X=4\sqrt X+O(\log^{A''}(2X)).}
\tag{T-27203.12}
\]

The reviewed square-screw/Landau transfer used by `T-27202` then excludes every zeta zero with real part greater than \(1/2\). Functional-equation symmetry excludes the reflected half-plane. Therefore

\[
\boxed{\mathrm{DCD}\Longrightarrow\mathrm{RH}.}
\tag{T-27203.13}
\]

## 6. Why this is stronger than another equivalent criterion

DCD provides an explicit mechanism rather than renaming the prime-ramp estimate:

1. the lower-scale source is fixed;
2. the complete same-scale remainder is written explicitly;
3. the genuine contraction \(1/2\) is already proved;
4. every permissible cycle correction has a canonical coordinate;
5. the only theorem is that the paired odd leakage and commutator can be repaired at polylogarithmic cost.

The old conditional-Hankel argument, bounded-face rank, generic Green energy, and unsigned carry slack are not used.

## 7. Exact proof-producing object

At endpoint \(2Y\), a DCD certificate must emit:

1. the complete targets \(w_Y,w_{2Y}\);
2. exact divergences \(r_Y,r_{2Y}\);
3. a lower exact flow \(d_Y\);
4. the complete doubled flow \(2^{-1/2}\mathcal L_2d_Y\);
5. the bottom charge \(w_{2Y}(2)T_2\);
6. every coefficient \(r_{2Y}(2a+1)\) and sparse \(E_{2a}\);
7. every nonzero upper cycle coordinate \(z_Y\);
8. exact divergence and carry-column replay;
9. lower and upper negative capacity debts;
10. the claimed excess bound.

A dual rejection certificate may instead emit a feasible bounded-superadditive potential whose value violates (T-27203.4).

Mandatory mutations include:

- deletion of the bottom charge;
- deletion or sign reversal of one odd commutator;
- wrong \(2^{-1/2}\) scaling;
- loss of one balanced fundamental cycle;
- replacement of capacity debt by unweighted negative-edge count;
- deletion of the dyadic or \(2/3\) Mertens projection;
- suppression of the directed ternary counterexample.

## 8. Exact status

Closed:

- exact half-scale divergence and flow;
- exact \(1/2\) capacity contraction;
- exact endpoint interpolation;
- DCD-to-Cycle-Debt induction;
- Cycle-Debt-to-RH deduction.

Open:

\[
\boxed{\text{DCD, equation (T-27203.4).}}
\]

Accordingly,

\[
\boxed{\text{RH remains unproved.}}
\]
