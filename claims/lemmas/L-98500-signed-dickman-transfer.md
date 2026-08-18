# L-98500 — Signed Dickman transfer for a source-complete annular base

Claim ID: `L-98500`  
Status: **UNCONDITIONAL QUANTITATIVE SOURCE THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

Let \(b:(0,\infty)\to\mathbb R\) be zero below \(1\). Put
\[
\beta(w)=e^{-w/2}b(e^w)\qquad(w\ge0).
\]
Assume:

1. \(\beta\) is bounded and of finite total variation;
2. for some \(a>0\),
   \[
   \beta(w)=a+\eta(w);
   \]
3. there are constants \(C_b,c_b>0\) such that
   \[
   |\eta(w)|+{\rm Var}_{[w,w+1]}(\eta)\le C_b e^{-c_bw}.
   \tag{L-98500.1}
   \]

For \(Y\ge z\ge3\), put
\[
L=\log z,\qquad u=\frac{\log Y}{L},
\]
and define the literal squarefree rough source
\[
\mathcal F_b(Y,z)=
\sum_{\substack{m\le Y\\\mu^2(m)=1\\P^-(m)\ge z}}
\frac{\mu(m)}{\sqrt m}\,b(Y/m).
\tag{L-98500.2}
\]

Let
\[
\nu_z=\sum_{p\ge z}\frac1p\,
\delta_{\log p/L},
\qquad
\lambda(dt)=\mathbf1_{t\ge1}\frac{dt}{t},
\]
and
\[
\Delta_z(u)=
\sup_{1\le v\le u}
\left|
\nu_z([1,v])-\log v
\right|.
\tag{L-98500.3}
\]

Then
\[
\boxed{
\begin{aligned}
\frac{\mathcal F_b(Y,z)}{\sqrt Y}
={}&a\rho(u)+\eta(Lu)\\
&+\frac1L\int_0^{Lu}
\eta(w)\rho'\!\left(u-\frac wL\right)\,dw
+\mathcal E_b(Y,z),
\end{aligned}}
\tag{L-98500.4}
\]
where \(\rho\) is the Dickman function and
\[
\boxed{
|\mathcal E_b(Y,z)|
\le
C_b'(1+u)^3
\left(
\Delta_z(u)+\sum_{p\ge z}\frac1{p^2}
\right).
}
\tag{L-98500.5}
\]

The constant \(C_b'\) is effective from the bound and variation in
(L-98500.1).

## 1. Exact rough-history expansion

For \(r\ge0\), the history of length \(r\) contributes
\[
(-1)^r
\sum_{\substack{z\le p_1<\cdots<p_r\\
\log p_1+\cdots+\log p_r\le\log Y}}
\frac1{p_1\cdots p_r}
\,
\beta\!\left(
\log Y-\sum_{j=1}^r\log p_j
\right).
\tag{L-98500.6}
\]
This is obtained from
\[
Y^{-1/2}m^{-1/2}b(Y/m)
=
m^{-1}\beta(\log(Y/m)).
\]
Thus every coefficient, activation, first owner and cumulative parity is
literal.

## 2. Distinct-prime product versus the product measure

Replace the ordered distinct-prime sum in (L-98500.6) by
\[
\frac1{r!}
\int_{\substack{t_1,\ldots,t_r\ge1\\
t_1+\cdots+t_r\le u}}
\beta\!\left(L(u-t_1-\cdots-t_r)\right)
\,d\nu_z(t_1)\cdots d\nu_z(t_r).
\tag{L-98500.7}
\]
The total mass of tuples containing a repeated prime is at most
\[
\binom r2
\left(\sum_{p\ge z}\frac1{p^2}\right)
\nu_z([1,u])^{r-2}.
\tag{L-98500.8}
\]

For the remaining product measures, apply one-dimensional Stieltjes
integration by parts in one coordinate at a time. The test has variation at
most a fixed multiple of
\[
\|\beta\|_\infty+{\rm Var}(\beta).
\]
After division by \(r!\), the \(r\)-th error is bounded by
\[
C_b r\Delta_z(u)
\frac{(\log u+1)^{r-1}}{r!}.
\]
Summing the finite history series and using
\[
e^{\log u+1}\ll1+u
\]
proves (L-98500.5), with the harmless cubic factor absorbing the first few
cells and the repeated-coordinate term.

## 3. Continuum convolution exponential

The signed convolution exponential
\[
\mathfrak d=
\delta_0+
\sum_{r\ge1}\frac{(-1)^r}{r!}\lambda^{*r}
\tag{L-98500.9}
\]
has cumulative distribution
\[
\mathfrak d([0,u])=\rho(u).
\tag{L-98500.10}
\]
Indeed its finite simplex expansion is the standard alternating Dickman
series; equivalently its Laplace transform is
\[
\int_{[0,\infty)}e^{-st}\,\mathfrak d(dt)
=e^{-E_1(s)},
\]
where \(E_1(s)=\int_1^\infty e^{-st}dt/t\).

Consequently the continuum form of (L-98500.7) is
\[
\int_{[0,u]}\beta(L(u-t))\,d\rho(t).
\]
Splitting \(\beta=a+\eta\), using the atom of size \(1\) at \(0\), and changing
variables \(w=L(u-t)\), gives exactly the first three terms of
(L-98500.4).

## 4. Relative size of the signed boundary term

A standard de Bruijn estimate gives
\[
-\frac{\rho'(v)}{\rho(v)}
\le C(1+\log(2v))
\qquad(v\ge1).
\tag{L-98500.11}
\]
Hence, whenever
\[
L\ge4C\log(2u+2),
\tag{L-98500.12}
\]
the exponential decay in (L-98500.1) yields
\[
\boxed{
\left|
\eta(Lu)+\frac1L\int_0^{Lu}
\eta(w)\rho'\!\left(u-\frac wL\right)dw
\right|
\le
C_b''\rho(u)\frac{\log(2u+2)}L
+C_b''e^{-c_bLu/2}.
}
\tag{L-98500.13}
\]

Thus the bounded annular remainder is not intrinsically an unsigned
\(1/\log z\) loss. Its leading effect is a signed derivative of the Dickman
profile.
