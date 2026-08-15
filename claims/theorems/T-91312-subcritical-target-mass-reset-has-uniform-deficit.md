# T-91312 — A hereditary target-mass reset with child mass below one eighth has uniformly bounded deficit

Claim ID: `T-91312`  
Status: **PROVED CONDITIONAL CONSUMER — HEREDITARY ENTRY OPEN**  
Created: 2026-08-14  
Depends on: `L-91375`; packet homogeneity/subadditivity; endpoint loss-to-RH consumer  
RH status: **conditional**

## 1. Packet mass

For a positive typed packet `P` at endpoint `X`, use the exact SHARP target mass

\[
 m_X(P)=T_X(P)\ge0.
\tag{T-91312.1}
\]

Let `Delta_X(P)` be its optimal literal endpoint-score deficit.  Assume positive homogeneity and subadditivity.

## 2. Hereditary reset hypothesis

Suppose every sufficiently large positive typed packet has an exact one-use decomposition

\[
\boxed{
 P=P_{\rm cur}+\sum_b\alpha_bA_bP_b
}
\tag{T-91312.2}
\]

such that:

1. every child endpoint obeys
   \[
   Y_b\le X/67+C_0;
   \]
2. `P_cur` is a positive sum of causal generators and terminal positive packets;
3. the child coefficients satisfy
   \[
   \alpha_b\ge0,
   \qquad
   \sum_b\alpha_b<\frac18;
   \tag{T-91312.3}
   \]
4. each child target is nonexpansive:
   \[
   m_{Y_b}(A_bP_b)\le m_X(P);
   \]
5. the identity holds simultaneously in source, row, ordinary capacity, radix-four capacity, literal score, and every retained port coordinate.

This is the **Hereditary Typed Reset** (`HTR`).

## 3. Local debt

By `L-91375`, every causal current generator has deficit at most twice its own exact target mass.  Terminal positive packets satisfy the same crude inequality.  Since the current and child targets form a one-use target partition,

\[
\boxed{
 \Delta_X(P_{\rm cur})
 \le2m_X(P).
}
\tag{T-91312.4}
\]

The child mass satisfies

\[
\boxed{
 \sum_b\alpha_bm_{Y_b}(A_bP_b)
 <\frac18m_X(P).
}
\tag{T-91312.5}
\]

## 4. Envelope recurrence

Let

\[
 \Lambda(X)=
 \sup_{Y\le X}
 \sup_{m_Y(P)=1}
 \max(0,\Delta_Y(P)).
\]

Subadditivity gives

\[
\begin{aligned}
 \Delta_X(P)
 &\le2m_X(P)
   +\sum_b\alpha_b\Delta_{Y_b}(A_bP_b)\\
 &\le m_X(P)
  \left[2+\frac18\Lambda(X/67+C_0)\right].
\end{aligned}
\]

Therefore

\[
\boxed{
 \Lambda(X)
 \le2+\frac18\Lambda(X/67+C_0).
}
\tag{T-91312.6}
\]

Iteration yields

\[
\boxed{
 \Lambda(X)
 \le\frac{2}{1-1/8}+O_{\rm base}(1)
 =\frac{16}{7}+O_{\rm base}(1).
}
\tag{T-91312.7}
\]

In particular the deficit is `O(1)`, hence `o(log^2 X)`.

## 5. Consequence and exact boundary

Once a native arithmetic packet is placed in the positive typed cone with bounded target mass, HTR and the resident endpoint consumer imply RH.

This theorem resolves the reviewer’s Route B normalization question:

```text
mass                              exact SHARP target T;
child contraction                 same mass, <1/8;
current physical generator debt   <=2 times the same mass;
consumer                           uniform O(1) deficit.
```

The remaining theorem is not the abstract recurrence.  It is HTR: an exact source-faithful positive entry/decomposition for the native signed arithmetic packet.

```text
subcritical target-mass consumer     COMPLETE CONDITIONAL
physical current-generator theorem   COMPLETE / L-91375
same mass in both estimates           EXACT
hereditary typed arithmetic reset     OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN ABSENT HTR
```
