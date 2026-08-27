# T-105400 — Remote-tail moment frontier for complete fixed-order Xi capacity

Claim ID: `T-105400`  
Status: **EXACT CONDITIONAL FIXED-ORDER COMPLETION; REMOTE XI TAIL OPEN**  
Created: 2026-08-23  
Depends on: `T-105390`, `L-105400`, `L-105401`  
RH status: **unproved**

## 1. The remote-tail gate at order k

Fix a parity and a finite matrix order `k>=1`. Put

\[
d_k=3k(k-1)+4
\]

and choose

\[
0<\gamma_k<{1\over2(3k(k-1)+5)},
\qquad
J_r=\lfloor r^{\gamma_k}\rfloor.
\]

Define:

```text
RTMH105400(k) — remote-tail moment matching at order k

For all sufficiently high derivative orders r of the chosen parity:

1. every critical point omitted beyond the first J_r positive pairs is real,
   simple, and has nonpositive residue;

2. if sigma_(r,J_r) is the signed difference between the normalized actual
   omitted critical measure and the unit tangent/cotangent tail after J_r,
   then

       max_(0<=n<=2k-1) | integral s^n d sigma_(r,J_r)(s) |
          = o(J_r^(-d_k)).
```

This gate is source specific and remains open for Xi.

## 2. Complete order-k capacity

`T-105390` proves that the first `J_r` actual critical pairs are real,
negative-residue, and leave a positive order-`k` source reserve. `L-105401`
shows that `RTMH105400(k)` makes the omitted-tail perturbation smaller than the
unused trigonometric tail matrix. Therefore

\[
\boxed{
\mathrm{RTMH105400}(k)
\Longrightarrow
\mathsf C_{k,r}^{(0)}
\preceq
\mathsf A_{k,r}^{(0)}
\quad\text{and}\quad
\mathsf C_{k,r}^{(1)}
\preceq
\mathsf A_{k,r}^{(1)}
}
\tag{T-105400.1}
\]

for every sufficiently high derivative order of that parity.

Thus the complete critical measure, not merely its central prefix, satisfies
the source-capacity inequality at the prescribed finite order.

## 3. Arbitrarily deep finite truncations

Suppose `RTMH105400(k)` holds for every fixed `k`. Then for every finite
ceiling `K` there is a derivative threshold `R_K` such that all high
derivatives of the specified parity satisfy

\[
\boxed{
\mathsf C_{k,r}^{(a)}
\preceq
\mathsf A_{k,r}^{(a)}
\qquad
(1\le k\le K,\ a=0,1,\ r\ge R_K).
}
\tag{T-105400.2}
\]

The proof takes the maximum of the finitely many thresholds. Hence arbitrarily
deep finite origin Stieltjes truncations can be completed in the high
derivative tail once the corresponding finite remote moments are controlled.

## 4. Exact quantifier barrier

The conclusion in Section 3 is

\[
\boxed{
\forall K<\infty\ \exists R_K\ \forall r\ge R_K\ \forall k\le K.
}
\tag{T-105400.3}
\]

It is not

\[
\exists R\ \forall r\ge R\ \forall k<\infty.
\tag{T-105400.4}
\]

The latter simultaneous all-order statement is what `OSCC105371` requires at
one derivative level. No uniform control of the trigonometric smallest
eigenvalues, source approximation, critical cells, or remote moments as
`k->infinity` is supplied here.

Consequently, even the complete family of fixed-order remote-tail theorems does
not by itself prove `BRP105220` or RH.

## 5. Strong total-variation sufficient lane

A stronger but simpler sufficient form of `RTMH105400(k)` is

\[
\boxed{
\int
\left(1+s+s^2+\cdots+s^{2k-1}ight)
\,d|\sigma_{r,J_r}|(s)
=
o(J_r^{-d_k}).
}
\tag{T-105400.5}
\]

By `L-105400`, this weighted total variation condition pays both Stieltjes
blocks. It requires no atom-by-atom pairing, but is generally stronger than
matching only the first `2k` signed moments.

## 6. Relation to the sharp RH graph

The sharp conclusion remains

\[
\mathrm{CRVH105330}
\wedge
\mathrm{OSCC105371}
\Longrightarrow
\mathrm{RH}.
\]

`RTMH105400(k)` discharges the complete order-`k` high-tail capacity burden.
To enter the sharp graph one still needs:

```text
simultaneous all-order control at one derivative level;
transport/descent to the last low defective derivative;
and the exact multiplicity and exhaustion interfaces.
```

## 7. Exact frontier

```text
first 2k remote moments -> order-k matrix error   PROVED EXACT
RTMH105400(k) -> complete order-k capacity        PROVED CONDITIONAL
all k<=K at sufficiently high derivatives         PROVED CONDITIONAL
RTMH105400(k) for actual Xi remote tails           OPEN
uniform all-order capacity at one derivative       OPEN
low-order reverse-Rolle descent                     OPEN
Riemann Hypothesis                                  UNPROVEN
```
