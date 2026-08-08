# Dyadic divergence commutator continuation

Date: 2026-08-08  
Agent: `gpt56-02-r`  
Branch: `agent/gpt56-02-r/262-half-pole-boundary-spline`  
Status: **EXACT NEW REDUCTION; ONE PAIRED DEBT THEOREM OPEN; RH UNPROVED**

## Why this continuation

The half-pole boundary-spline package is already published on PR #272 and was subsequently self-audited. Its boundary-jet LMI is not being promoted as a completed source identity. The current branch instead uses its exact fragmentation and Cycle Debt normal forms.

The new attack combines that normal form with PR #269's exact dyadic half-scale carry identity.

## Main exact theorem

At \(X=2Y\), the complete target divergence is

\[
r_{2Y}=2^{-1/2}\mathcal D_2r_Y+w_{2Y}(2)\partial T_2+\sum_{a<Y}r_{2Y}(2a+1)\partial E_{2a}.
\]

Here \(E_n=T_{n+1}-T_n\), and

\[
\partial E_n=e_{n+1}-e_n-e_1.
\]

The unmatched scalar is exactly \(w_{2Y}(2)\), not an unspecified boundary error. Every odd node appears exactly once.

At flow level this gives a complete exact producer and replays every carry column.

## Genuine contraction

For a doubled edge,

\[
\omega_{2n,2j}=2^{-1/2}\omega_{n,j}+\omega_{\rm odd}(2n,2j).
\]

After the coefficient scaling \(2^{-1/2}\), the even-capacity negative debt is therefore exactly one half of the lower debt. The only obstruction is the source-complete pairing of odd-column leakage with the adjacent-tree commutator.

This yields the proposed Dyadic Commutator Debt theorem:

\[
\mathfrak N_\eta(2Y)\le\frac12\mathfrak N_\eta(Y)+O(\log^A Y).
\]

The theorem itself remains open.

## Endpoint interpolation

The increment from \(X-1\) to \(X\) is \(c_Xq^{-1/2}\), with \(c_X=\log(X/(X-1))\). Its canonical central-tree flow has negative capacity debt

\[
O\!\left(\frac{\log X}{\sqrt X}\right).
\]

Thus endpoint parity is not a second cofinal obstruction.

## Conditional finish

Dyadic Commutator Debt plus endpoint interpolation gives polylogarithmic Cycle Debt. The exact balanced entropy metric then gives

\[
P_X=4\sqrt X+\operatorname{polylog}(X),
\]

and the reviewed square-screw/Landau consumer yields RH.

## Honest frontier

The new work does not prove RH. It replaces the undifferentiated Cycle Debt statement by a strict half-scale recurrence with a proved contraction and one explicit paired source:

```text
odd carry capacity
+
odd Möbius node divergence
+
adjacent central-tree commutator.
```

A reviewer can now either construct the cycle correction paying this source at polylogarithmic cost or produce a bounded-superadditive dual obstruction.

## Exact replay

`X-27206` reports:

```text
divergence cases             189
full carry-flow cases        189
doubled carry cells       43,184
commutator recursions        128
balanced commutator edges  1,298
endpoint increment cases     126
mutations                    4/4 detected
proof SHA
0d6bd92b43fcaf0a22eadbee0e013335137691ffa4779990a3417409db54d5c0
```

The replay certifies finite algebra only.
