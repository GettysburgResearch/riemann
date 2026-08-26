# L-103008 — The radial middle prefix has an exact midpoint–Peano pair decomposition

Claim ID: `L-103008`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-25  
Depends on: `R-103002`; `L-102746--L-102749`; `T-102990`  
RH status: **not assumed**

Let `R` be a finite set of labelled prime coordinates and put

\[
F_R(t)=\prod_{r\in R}(1-tx_r).
\]

The radial middle prefix appearing in the actual-owner difference is

\[
H_R=\int_0^1F_R(t)\,dt.
\]

The midpoint rule is exact on affine functions. Its second-order Peano kernel is

\[
K(t)=
\begin{cases}
\frac12t^2,&0\le t\le\frac12,\\[1mm]
\frac12(1-t)^2,&\frac12\le t\le1.
\end{cases}
\tag{L-103008.1}
\]

Indeed, for every twice differentiable scalar function `f`,

\[
\int_0^1f(t)\,dt-f(1/2)
=
\int_0^1K(t)f''(t)\,dt.
\]

The identity is polynomial and therefore remains coefficient-exact in the finite commuting Euler algebra.

Now

\[
F_R''(t)
=
2\sum_{\{r,s\}\subset R}
x_rx_s
\prod_{q\in R\setminus\{r,s\}}(1-tx_q).
\]

Consequently

\[
\boxed{
\begin{aligned}
H_R
={}&
\prod_{r\in R}(1-x_r/2)\\
&+
\int_0^1
\min(t^2,(1-t)^2)
\sum_{\{r,s\}\subset R}
 x_rx_s
 \prod_{q\ne r,s}(1-tx_q)
\,dt.
\end{aligned}
}
\tag{L-103008.2}
\]

## 1. Exact source interpretation

The first row is the arithmetic midpoint prefix.

The second row is a positive Peano-weighted equal-pair source current:

```text
one literal unordered pair {r,s};
positive homotopy weight min(t^2,(1-t)^2);
complete remaining Euler prefix;
no pair chosen after physical observation.
```

Thus the signed singleton coefficient in `R-103002` is not an isolated defect. It belongs to one exact midpoint-plus-pair decomposition.

## 2. Relation to the harmonic midpoint

At one prime,

\[
1-x/2
=
M(x)+x^2/2,
\qquad
M(x)=1-x/2-x^2/2.
\]

Therefore the arithmetic midpoint prefix and the critical Hodge midpoint differ only through terms containing at least one squared label. At the frozen primewise gauge scope, those terms belong to the existing squared/higher-prime-power ledger.

## 3. Relation to the Boolean equal-pair current

The Peano remainder begins at one actual unordered pair and uses the same complete remaining prefix as the canonical Duhamel/equal-pair source. After the inherited carrier, common-core, equal-product, repeated-label and one-sided-core closures, its conclusion-bearing component is the coprime two-sided Boolean pair current of `BCI102990`.

Hence the signed middle-prefix obstruction of `T-103040` introduces no new arithmetic species:

\[
\boxed{
\text{middle prefix}
=
\text{harmonic midpoint}
+
\text{positive equal-pair current}
+
\text{squared-activity transfer}.
}
\tag{L-103008.3}
\]

The identity does not prove the orientation of the midpoint or pair current.