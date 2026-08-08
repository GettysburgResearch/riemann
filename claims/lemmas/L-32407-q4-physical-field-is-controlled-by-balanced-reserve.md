# L-32407 — The true Q=4 interval-kernel physical field is controlled by its balanced Selberg reserve

Claim ID: `L-32407`  
Status: **PROPOSED COMPLETE SOURCE-BOUND TRANSFERENCE THEOREM — CORRECTED 2026-08-09; INDEPENDENT REVIEW REQUIRED**

## 1. Correct physical coordinate

Let `e_4(1)=1`, `e_4(4^r)=-3`, and define

\[
 c_4=e_4*\Lambda_4.
\]

The Dirichlet series of `c_4` is the pole-preserving current `E_4(s)L_4(s)`. After cancellation of the zeta factor in the atomized carry transform, `c_4` multiplies the **centered-interval kernel**, not a second carry indicator.

Define the prefix

\[
 G_4(x)=\sum_{m\le x}c_4(m),
\]

and for integer `n=j+k`

\[
 \boxed{
 Q_4^{\rm phys}(n,j)=G_4(n)-G_4(j)-G_4(k).
 }
 \tag{L-32407.1}
\]

This is the exact integer specialization of the physical pole field. The former version of this file incorrectly wrote `sum c_4(q) chi_(n,q)(j)`, applying one extra divisor/floor transform. `R-32403` records that scope correction.

## 2. Exact sparse coefficient law

Writing `ell=log 2`, direct convolution gives, for odd prime `p`,

\[
 c_4(p^a)=\log p,
 \qquad
 c_4(4^r p^a)=-3\log p\ (r\ge1),
 \qquad
 c_4(2\,4^r p^a)=0.
\]

On the pure dyadic tower,

\[
 c_4(2^{2r})=(3r+4)\ell\quad(r\ge1),
\]

\[
 c_4(2^{2r+1})=(1-3r)\ell\quad(r\ge0).
\]

No integer containing two distinct odd prime factors occurs.

## 3. Linear absolute coefficient mass

Let

\[
 M_4(x)=\sum_{m\le x}|c_4(m)|.
\]

The odd-prime-power/dilation part is bounded by

\[
 \psi(x)+3\sum_{r\ge1}\psi(x/4^r)
 \le4x\log2<\frac{20}{7}x.
\]

The explicit pure-dyadic formulas give, for `K=floor(log_2 x)`,

\[
 \sum_{2^k\le x}|c_4(2^k)|
 \le\log2\left(\frac34K^2+\frac{19}{4}K\right)
 \le x
\]

for `x>=64`. Hence

\[
 \boxed{M_4(x)<4x\qquad(x\ge64).}
 \tag{L-32407.2}
\]

## 4. Large balanced rows

If `n>=4735` and `n/4<=j<=3n/4`, then `j,k>=64`; therefore

\[
 |Q_4^{\rm phys}(n,j)|
 \le M_4(n)+M_4(j)+M_4(k)
 <8n.
 \tag{L-32407.3}
\]

By `L-32405`,

\[
 \mathcal R_4(n,j)
 >\frac1{20}P_4(n,j)^2
 \ge\frac{n^2(\log2)^2}{320}.
\]

Thus

\[
 \frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
 <\frac{20480}{(\log2)^2}
 <44000,
\]

using `log2>69/100`. Consequently

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2<44000\,\mathcal R_4(n,j)
 }
 \tag{L-32407.4}
\]

through the infinite balanced tail.

## 5. Exact finite range

The corrected `X-32402` verifier constructs directed intervals for `c_4`, then forms the **prefix defect** (L-32407.1). It verifies simultaneously with `L-32405` that for all

\[
 4\le n\le4734,
 \qquad
 \lceil n/4\rceil\le j\le\lfloor n/2\rfloor,
\]

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2<11\,\mathcal R_4(n,j).
 }
 \tag{L-32407.5}
\]

The worst row is `(8,4)`. The rigorous upper ratio is

```text
20023262563043128709139365197287413026201889175625
-----------------------------------------------------------------
1982153862092292642942383343265608318216102562329
```

which is about `10.1017700724` and is strictly below eleven.

The exact replay covers `2,803,709` balanced rows and records digest

```text
b66e793d5f7000399f634f0dbc1cab61d70bb7f0e132c22cd5fe9d903c392248
```

Combining finite and infinite ranges,

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2
 <44000\,\mathcal R_4(n,j)
 \quad(n\ge4,\ n/4\le j\le3n/4).
 }
 \tag{L-32407.6}
\]

## 6. Proof boundary

Closed here:

1. the correctly typed interval-kernel physical coordinate;
2. the sparse `c_4` coefficient law;
3. linear absolute coefficient mass;
4. an analytic all-large-row physical-to-reserve bound;
5. rigorous finite transference for every remaining balanced row.

Open:

1. independent-frequency reflected reserve accounting/no-double-spend;
2. the coefficient-one scattering recurrence;
3. RH.
