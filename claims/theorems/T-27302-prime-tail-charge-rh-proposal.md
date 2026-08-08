# T-27302 — Prime residual suffix-charge proposal for RH

Claim ID: `T-27302`  
Title: A subpower maximum suffix of the parabolic ordinary-prime residual would imply RH, but the proposed suffix bound has positive density drift  
Status: **REJECTED AS A COMPLETION — `PTC` PROPOSED REFUTED BY `R-27302`**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: `L-27301`--`L-27303`; `R-27302`; PR #248 `L-24517/L-24520`; PR #265 `L-26202`; PR #271 boundary lift

## 1. Conditional implication retained

Let \(p_1<\cdots<p_N\le X\) be the primes through \(X\), and define

\[
r_i
=
v_{p_i}(b_X^{(0)})
-
\frac1{\sqrt{p_i}}\log\frac X{p_i}.
\tag{T-27302.1}
\]

The exact greedy prime-incidence construction in `L-27303` has exterior charge

\[
C_X^{\uparrow}
=
\max_{1\le k\le N}
\left(\sum_{j=k}^{N}r_j\right)_+.
\tag{T-27302.2}
\]

If one had

\[
C_X^{\uparrow}=X^{o(1)},
\tag{T-27302.3}
\]

then the proper-power-neutral prime blocks and the affine boundary lift would
give

\[
P_X\ge4\sqrt X-X^{o(1)},
\]

and the inherited square-screw/Landau chain would imply RH. This conditional
calculation is retained.

## 2. The proposed rate is false

`R-27302` computes the full ordinary-prime residual sum:

\[
\boxed{
\sum_{p\le X}r_X(p)
=
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
}
\tag{T-27302.4}
\]

The full suffix beginning at \(2\) is one of the suffixes in (T-27302.2).
Therefore

\[
\boxed{
C_X^{\uparrow}
\ge
\left(4(1-\gamma)+o(1)\right)
\frac{\sqrt X}{\log^2X}.
}
\tag{T-27302.5}
\]

Hence (T-27302.3) fails. Prime-to-prime upward blocks alone cannot preserve the
sharp constant.

The exact greedy algebra and proper-power neutrality in `L-27303` remain valid;
only their proposed asymptotic closure is rejected.

## 3. Corrected frontier

The positive drift is a sampling-density effect. A viable proper-power-neutral
repair must use squarefree composite collector endpoints. Such a collector can
reduce several ordinary-prime residuals at once while remaining invisible to
every proper prime power.

The corrected full proposal is `T-27303`.

## 4. Status

```text
prime-incidence greedy algebra        RETAINED EXACT
PTC conditional implication           RETAINED
PTC all-scale rate                     PROPOSED REFUTED
T-27302 as full completion             REJECTED
squarefree composite collector route  OPEN
Riemann Hypothesis                     UNPROVED
```
