# L-106551 — The 280-point seven-gap pressure lift

Claim ID: `L-106551`  
Status: **EXACT DEDUCTION CONDITIONAL ON THE PINNED SEVEN-GAP CERTIFICATE**  
Created: 2026-08-25  
Depends on: `L-105211`, `L-106550`  
External finite premise: `ainta/zeta-simple-zeros@040c5e899e658aed7b56a2a87f501798fe10761d`  
RH status: **not assumed**

Retain the normalized Montgomery--Taylor overlap kernel \(k\), put
\(w=k^2\), and retain the pinned seven-gap inequality

\[
\frac1{3000}\sum_{i=1}^6g_i
+
\sum_{s=1}^6\frac2{7-s}
\sum_{i=1}^{7-s}
w(g_i+\cdots+g_{i+s-1})
\ge\frac{19}{5000}.
\tag{L-106551.1}
\]

For \(m\) ordered points \(y_1<\cdots<y_m\), write

\[
E_m=2\sum_{i<j}w(y_j-y_i).
\]

Summing (L-106551.1) over all consecutive seven-point windows gives, as in
`L-105211`,

\[
E_m+\frac1{500}(y_m-y_1)
\ge\frac{19}{5000}(m-6).
\tag{L-106551.2}
\]

## 1. The first block beyond the old unit cap

Choose

\[
m=280.
\]

Then the certified pressure is

\[
q_{280}
=
\frac{19}{5000}(280-6)
=
\frac{2603}{2500}
=
1.0412.
\]

Let \(G_B\) be the Gram matrix of one consecutive 280-point block and put

\[
z_B=\frac1{500}\operatorname{span}(B).
\]

Because \(E(G_B)=E_{280}\), equations (L-106551.2) and `L-106550` give

\[
\boxed{
\Delta(G_B)+z_B\ge c_{280},
}
\tag{L-106551.3}
\]

where

\[
\boxed{
c_{280}
=
2\sqrt{\frac{726237}{700000}}
-1+\frac{2603}{700000}
=
1.040855217381835479\ldots .
}
\tag{L-106551.4}
\]

The old unit-cap argument could use at most \(1\). The excess in
(L-106551.4) is obtained without changing or rerunning the external Arb
certificate.

## 2. Global averaging

Pinch the global simple-line Gram matrix into consecutive 280-point blocks.
Trace convexity under pinching gives the sum of the block defects as a lower
bound for the global defect. Average over all 280 offsets. As in `L-105211`,
each interior point is counted 280 times, while the mean total block-span
charge is

\[
\frac{279}{500\cdot280}N
=
\frac{279}{140000}N
\]

up to the standard \(o(N)\) endpoint loss.

Therefore

\[
\boxed{
\Delta(M)
\ge
\frac{c_{280}}{280}S
-\frac{279}{140000}N
-o(N),
}
\tag{L-106551.5}
\]

where \(S=N_0^s(T,2T)\) and \(N=N(T,2T)\).

Equation (L-106551.5) strictly improves the 269-point coefficient in
`L-105211`. It relies on the same finite certificate and the same analytic
normalization; only the spectral conversion of local Frobenius pressure into
the convex defect has changed.
