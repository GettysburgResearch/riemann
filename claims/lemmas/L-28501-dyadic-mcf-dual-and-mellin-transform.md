# L-28501 — The MCF menu has an exact dyadic dual with an eta denominator

Claim ID: `L-28501`  
Title: The binary-window/Mersenne-edge carry menu admits a dyadic superadditive potential whose critical pairing has Mellin transform `2^{-s}/eta(s)`  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #285 at `61d0b66196f308981d36dbb8723d5e64d7a27533`  
Dependencies: the atomized carry identity; elementary Dirichlet convolution; Landau is used only in `R-28501`  
Scope: exact finite dual algebra, Mellin transform, and interpolation estimate; no RH conclusion

## 1. The MCF edge menu

For an integer `n>=2`, let

\[
L(n)=2^{\lfloor\log_2 n\rfloor}.
\]

The Mersenne-Collar Fragmentation menu of `T-28001` permits:

- if `n` is not of the form `2L(n)-1`, every split
  \[
  n-L(n)<j<L(n);
  \tag{L-28501.1}
  \]
- if `n=2L(n)-1`, only the two extreme splits `j=1` and `j=n-1`.

For one split put

\[
\chi_{n,q}(j)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor.
\tag{L-28501.2}
\]

## 2. A dyadic superadditive potential

Define

\[
\boxed{
\Phi(1)=0,
\qquad
\Phi(n)=L(n)-1\quad(n\ge2).
}
\tag{L-28501.3}
\]

Then every MCF edge has nonnegative dual defect:

\[
\boxed{
\Phi(n)-\Phi(j)-\Phi(n-j)\ge0.
}
\tag{L-28501.4}
\]

### Proof

Let `L=L(n)`.

If `n` is not Mersenne and (L-28501.1) holds, both children are strictly below
`L`. Hence

\[
L(j),L(n-j)\le L/2
\]

and

\[
\Phi(j)+\Phi(n-j)
\le(L/2-1)+(L/2-1)
=L-2<\Phi(n).
\tag{L-28501.5}
\]

The harmless child `1` convention only decreases the left side.

If `n=2L-1` and `j=1`, then `n-j=2L-2` has largest dyadic scale `L`, so

\[
\Phi(n)-\Phi(1)-\Phi(n-1)
=(L-1)-0-(L-1)=0.
\tag{L-28501.6}
\]

The other orientation is identical.

## 3. Exact divisor coefficient

Put

\[
\Delta\Phi(m)=\Phi(m)-\Phi(m-1),
\qquad \Phi(0)=0.
\]

Then

\[
\boxed{
\Delta\Phi(m)
=\begin{cases}
2^{r-1},&m=2^r,\
0,&\text{otherwise},
\end{cases}
\qquad r\ge1.
}
\tag{L-28501.7}
\]

Let

\[
a=\mu*\Delta\Phi.
\tag{L-28501.8}
\]

Since `1*a=Delta Phi`, finite divisor switching gives

\[
\boxed{
\Phi(m)=\sum_{q\le m}a(q)\left\lfloor\frac mq\right\rfloor.
}
\tag{L-28501.9}
\]

The Dirichlet series of `Delta Phi` is

\[
\sum_{r\ge1}\frac{2^{r-1}}{(2^r)^s}
=\frac{2^{-s}}{1-2^{1-s}}.
\tag{L-28501.10}
\]

Consequently

\[
\boxed{
A(s):=\sum_{q\ge1}\frac{a(q)}{q^s}
=\frac{2^{-s}}{(1-2^{1-s})\zeta(s)}
=\frac{2^{-s}}{\eta(s)},
}
\tag{L-28501.11}
\]

initially for `Re(s)>1`, where

\[
\eta(s)=(1-2^{1-s})\zeta(s)
=\sum_{n\ge1}\frac{(-1)^{n-1}}{n^s}.
\]

Equivalently, if `b_eta` denotes the coefficient of `1/eta(s)`, then

\[
\boxed{
a(2m)=b_\eta(m),\qquad a(2m+1)=0.}
\tag{L-28501.12}

Using the exact eta inverse of `L-28001`, if `m=2^v u` with `u` odd, then

\[
b_\eta(m)=
\begin{cases}
\mu(u),&v=0,\\
2^{v-1}\mu(u),&v\ge1.
\end{cases}
\tag{L-28501.13}
\]

## 4. The exact MCF dual scalar

For real `X>=2`, define the critical target

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}
\tag{L-28501.14}
\]

and the scalar

\[
\boxed{
\mathfrak D(X)
=\sum_{q\le X}a(q)w_X(q).
}
\tag{L-28501.15}
\]

Suppose a nonnegative MCF flow `d_X(n,j)` saturates every carry column. Then

\[
\begin{aligned}
\mathfrak D(X)
&=\sum_q a(q)\sum_{n,j}d_X(n,j)\chi_{n,q}(j)\\
&=\sum_{n,j}d_X(n,j)
 [\Phi(n)-\Phi(j)-\Phi(n-j)]\\
&\ge0.
\end{aligned}
\tag{L-28501.16}
\]

Thus

\[
\boxed{
\mathrm{MCF}(X)\Longrightarrow\mathfrak D(X)\ge0.
}
\tag{L-28501.17}
\]

This implication is finite and exact. It uses neither asymptotics nor separation.

## 5. Mellin transform

For `Re(z)>1/2`, absolute convergence permits termwise integration:

\[
\int_q^\infty
\log(X/q)X^{-z-1}\,dX
=\frac{q^{-z}}{z^2}.
\tag{L-28501.18}
\]

Hence

\[
\boxed{
\int_1^\infty
\mathfrak D(X)X^{-z-1}\,dX
=
\frac{2^{-(z+1/2)}}{z^2\eta(z+1/2)}.
}
\tag{L-28501.19}
\]

The right side has a pole at every

\[
\boxed{
z_k=\frac12+\frac{2\pi i k}{\log2},
\qquad k\in\mathbb Z\setminus\{0\},}
\tag{L-28501.20}
\]

because `1-2^{1-s}` vanishes at `s=1+2pi i k/log 2`, while zeta is finite there. If zeta also vanished, the pole order would only increase.

For every real `z>0`, the right side of (L-28501.19) is regular. Indeed the alternating-series representation gives

\[
\eta(s)>0\qquad(s>0),
\tag{L-28501.21}
\]

and the removable value at `s=1` is `eta(1)=log 2`.

## 6. Integer interpolation does not remove the poles

The proposed MCF theorem is stated at integer endpoints. Let

\[
\mathfrak D_{\rm lin}(X)
\]

be the piecewise-linear interpolation of the values `mathfrak D(N)` at positive integers.

On one interval `[N,N+1]`, the continuous function in (L-28501.15) is

\[
f_N(X)=\sum_{q\le N}\frac{a(q)}{\sqrt q}\log(X/q);
\]

the new `q=N+1` term vanishes at the right endpoint. Thus

\[
f_N''(X)
=-\frac1{X^2}\sum_{q\le N}\frac{a(q)}{\sqrt q}.
\tag{L-28501.22}
\]

From (L-28501.12)--(L-28501.13),

\[
\sum_{q\le N}\frac{|a(q)|}{\sqrt q}
\le
\sqrt N\left(1+\frac12\log_2N\right).
\tag{L-28501.23}
\]

The standard linear-interpolation remainder therefore gives

\[
\boxed{
|\mathfrak D_{\rm lin}(X)-\mathfrak D(X)|
\le
\frac18N^{-3/2}
\left(1+\frac12\log_2N\right)
\quad(N\le X\le N+1).
}
\tag{L-28501.24}
\]

Consequently the Mellin transform of the interpolation error is holomorphic in

\[
\operatorname{Re}z>-\frac32.
\tag{L-28501.25}
\]

In particular, passing from the continuous source to the integer interpolation cannot cancel any pole (L-28501.20), and it creates no positive-real singularity.

## 7. Proof boundary

Established exactly:

1. the dyadic potential is dual-feasible on every declared MCF edge;
2. its divisor coefficient has Dirichlet series `2^{-s}/eta(s)`;
3. exact MCF feasibility forces `mathfrak D(X)>=0`;
4. the Mellin transform is (L-28501.19);
5. the transform has nonreal boundary poles but no positive-real pole;
6. integer piecewise-linear interpolation changes the transform only by a function holomorphic far across the critical boundary.

The Landau contradiction and the disposition of MCF are stated in `R-28501`.