# L-93302 — Vaughan decomposition closes all Type-I ranges and localizes the hard hyperbola arbitrarily deeply

Claim ID: `L-93302`  
Status: **PROVED UNCONDITIONAL REDUCTION THEOREM**  
Created: 2026-08-16  
Depends on: `L-93300`, `L-93301`; Vaughan's identity; elementary Chebyshev/divisor bounds  
RH status: **unproved**

Fix `r>=1` and write

\[
S_r(N)=\sum_{n\le N}\Lambda(n)W_r(n/N).
\]

Put

\[
U=V=\lfloor N^{1/3}\rfloor.
\]

## 1. Scaled cell estimates

For real `y>=4`, define

\[
G_r(y)=\sum_{m\le y}W_r(m/y),
\qquad
F_r(y)=\sum_{m\le y}(\log m)W_r(m/y).
\]

The compact piecewise polynomial, its zero endpoints, and the derivative regularity at `1/4` give

\[
|G_r(y)|\le C_r/y,
\qquad
|F_r(y)|\le C_r\log(2y)/y.
\tag{L-93302.1}
\]

For `r>=2`, the extra smoothness at `1/4` gives stronger Euler remainders, but the displayed uniform estimate is sufficient. The logarithmic estimate uses both moments of `L-93301.2` and a separate treatment of the first cell near zero.

For the cubic normalization and integer `y=4q+a`, one has the exact check

\[
\sum_{m=1}^yW(m/y)=
\begin{cases}
0,&a=0,\\
-8q(q+1)/y^3,&a=1,3,\\
-4q(q+1)/[3(2q+1)^3],&a=2.
\end{cases}
\tag{L-93302.2}
\]

## 2. Exact Vaughan identity

Write `mu=mu_(<=U)+mu_(>U)` and `Lambda=Lambda_(<=V)+Lambda_(>V)`. Since `log=Lambda*1` and `mu*1=epsilon`,

\[
\boxed{
\Lambda
=\mu_{\le U}*\log
-\mu_{\le U}*\Lambda_{\le V}*1
+\Lambda_{\le V}
+\mu_{>U}*\Lambda_{>V}*1.
}
\tag{L-93302.3}
\]

Projecting by `W_r(n/N)` gives

\[
S_r(N)=T_{r,1}(N)+T_{r,2}(N)+T_{r,3}(N)+B_r(N),
\tag{L-93302.4}
\]

where

\[
B_r(N)=
\sum_{m>V}\Lambda(m)
\sum_{q\ge1}a_U(q)W_r(mq/N),
\qquad
a_U(q)=\sum_{\substack{d\mid q\\d>U}}\mu(d).
\tag{L-93302.5}
\]

Every nonzero term has `m,q>N^(1/3)` and `mq<=N`.

## 3. All Type-I terms are below square-root scale

From (L-93302.1),

\[
T_{r,1}(N)\ll_r N^{-1/3}\log(2N),
\tag{L-93302.6}
\]

\[
T_{r,2}(N)\ll_r N^{1/3},
\tag{L-93302.7}
\]

and, using `W_r(x)=O_r(x^r)` at zero,

\[
T_{r,3}(N)\ll_r N^{-(2r-1)/3}.
\tag{L-93302.8}
\]

No cancellation of `mu` or a PNT power saving is used.

## 4. Arbitrarily deep hyperbola localization

Let `Y<=N/4` and let `B_r^{<=Y}` denote the terms with `mq<=Y`. Since `|a_U(q)|<=tau(q)`, `|W_r(x)|<=C_rx^r`, and

\[
\sum_{m\le z}m^r\Lambda(m)\ll_r z^{r+1},
\]

one obtains

\[
|B_r^{\le Y}(N)|
\ll_r
\frac{Y^{r+1}}{N^r}
\sum_{q\le Y}\frac{\tau(q)}q
\ll_r
\frac{Y^{r+1}}{N^r}\log^2(2Y).
\tag{L-93302.9}
\]

Choose

\[
\eta_r=1-\frac1{2(r+1)}.
\]

Then

\[
\boxed{
B_r^{\le N^{\eta_r}}(N)
\ll_r\sqrt N\log^2(2N).
}
\tag{L-93302.10}
\]

Consequently the only remaining term is

\[
\boxed{
B_r^\sharp(N)=
\sum_{\substack{m,q>N^{1/3}\\N^{\eta_r}<mq\le N}}
\Lambda(m)a_U(q)W_r(mq/N).
}
\tag{L-93302.11}
\]

and

\[
\boxed{
A_r(N)=r!B_r^\sharp(N)+O_r(\sqrt N\log^2(2N)).
}
\tag{L-93302.12}
\]

For the cubic, `eta_1=3/4`. For the quintic, `eta_2=5/6`. As `r` increases, every product outside an arbitrarily thin exponent-neighborhood of the hyperbola `mq=N` is paid unconditionally.

The remaining estimate is still RH-bearing; increasing endpoint order does not make it automatic.
