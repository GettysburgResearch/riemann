# O-34001 — Q=4 physical current versus the radix-four reserve increment

Claim ID: `O-34001`  
Status: **FLOATING DISCOVERY ONLY — NOT A THEOREM OR RH CLAIM**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-34001`, `L-34002`; PR #325 exact Q=4 formulas

## 1. Sharper scale-matched target

`L-34002` proves that the deterministic new reserve created in one exact radix-four step,

\[
 \Delta_4R(n,j)
 =R_4(4n,4j)-16R_4(n,j),
\]

is nonnegative and only `O(n log n)` on the quarter-balanced cone.

This suggests testing the source-matched inequality

\[
\boxed{
 |Q_4^{\rm phys}(4n,4j)|^2
 \le \Delta_4R(n,j).
}
\tag{O-34001.1}
\]

Unlike the much larger full reserve `R_4(4n,4j)~n^2`, the right side of (O-34001.1) already has the critical arithmetic scale needed for a conclusion-producing physical estimate.

## 2. Floating reconnaissance

An ordinary floating-point scan using the exact finite coefficient formulas for `Lambda_4`, `C_4`, and `c_4` found:

```text
quarter-balanced rows tested: all rows with 4 <= n <= 500;
failures of (O-34001.1):
  (9,4), (10,4), (11,5), (13,5), (14,6);
no failure for 15 <= n <= 500.
```

The same scan tested the stricter innovation current

\[
 I_4(n,j)
 =Q_4^{\rm phys}(4n,4j)-Q_4^{\rm phys}(n,j),
\]

which is the one-step compact source of `L-34003`. It found only one failure through the same range:

```text
(n,j)=(7,2).
```

Thus the numerically cleaner candidate is

\[
\boxed{
 |I_4(n,j)|^2
 \le\Delta_4R(n,j)
}
\tag{O-34001.2}
\]

outside a fixed small base.

These computations used ordinary binary floating point and are retained only as search guidance. They are not directed certificates and are not used by any theorem on this branch.

## 3. Why either inequality would be proof-closing

By `L-34002`,

\[
 \Delta_4R(n,j)=O(n\log n).
\]

Therefore either a uniform form of (O-34001.1), or a source-renewal proof based on (O-34001.2) plus the coefficient-one delayed current of `L-34003`, would put the physical pole current on the correct square-root-normalized polynomial scale.

The existing vector-valued pole criterion would then exclude every off-line zero.

Consequently these inequalities are **RH-bearing**. Their striking finite behavior may not be promoted by continuity, PNT, or the size of the full reserve.

## 4. Source structure behind the innovation test

The innovation current is not arbitrary. `L-34003` gives

\[
 (\varepsilon-\delta_4)q_4
 =q_\circ-(\log4)\delta_4*b_4,
\]

with

\[
 B_\circ(s)={1-4^{1-s}\over\zeta(s)},
 \qquad
 \mathbf1*b_\circ=\varepsilon-4\delta_4.
\]

So (O-34001.2) asks whether the **two-tap main-pole-killing innovation source**, plus one explicit delayed bare gauge, is precisely paid by the new deterministic Selberg reserve created at that radix-four step.

This is a much more source-specific target than a generic mean-square Chebyshev error.

## 5. Proof boundary

Verified on this branch:

- exact source/current identity `L-34001`;
- exact critical-scale reserve increment `L-34002`;
- exact compact innovation source `L-34003`.

Discovery only:

- (O-34001.1);
- (O-34001.2);
- any finite threshold suggested by the scan.

RH remains unproved.
