# Standalone proof — F1 Hardy–Gram and signed near-collision frontier

## Frozen packet

```text
F1/Hardy parent:
  PR #730
  74a4f6dcad0eabdc98c954ce0e7b46d39875cf32

Boolean/energy parent:
  PR #719
  e56c981e2d0639a988f8f54aa362724eb00d9131

same-half-source/family parent:
  PR #751
  98af0db6ec7f77d6333a77a3dac53c4698852f43
```

The classical Riemann Hypothesis is not assumed and is not proved here.

## 1. The terminal Hardy samples

For the recombined finite physical coefficient sequence `(a_n)`, let

\[
H(X)=\sum_n a_nK_L(X/n).
\]

The exact discretization of `T-105470` gives

\[
\delta_m=\Delta_2W(m)=\frac14H(m+),
\]

where

\[
W(x)=2\sum_{n\le x}a_n-\sqrt x\sum_{n\le x}\frac{a_n}{\sqrt n}
\]

and

\[
\Delta_2=(I-S)^2(I-\sqrt2S),\qquad (Sf)(x)=f(x/2).
\]

The conclusion-facing Hardy quantity is

\[
\mathcal L_M=\sum_{m=M}^{2M}\frac{|\delta_m|}{m}.
\]

Weighted Cauchy gives

\[
\mathcal L_M^2
\le\left(\sum_{m=M}^{2M}\frac1m\right)
   \sum_{m=M}^{2M}\frac{|\delta_m|^2}{m}
\le\left(\log2+\frac2M\right)\mathcal E_M.
\]

Thus the square condition `mathcal E_M=M^(o(1))` implies the Hardy condition.

## 2. Exact cell-square localization

On every open integer cell `m<X<m+1`,

\[
H(X)=A_m+B_m\sqrt X.
\]

Put `a=sqrt(m)`, `b=sqrt(m+1)`.  The substitution `X=t^2` gives

\[
\begin{aligned}
\Xi_m
&=\int_m^{m+1}|H(X)|^2\frac{dX}{X}\\
&=2|A_m|^2\log\frac ba
 +4\operatorname{Re}(A_m\overline{B_m})(b-a)
 +|B_m|^2(b^2-a^2).
\end{aligned}
\]

If `u=H(m+)` and `v=H((m+1)-)`, then

\[
\int_a^b|(1-s)u+sv|^2dt
=\frac{b-a}{3}(|u|^2+\operatorname{Re}(u\bar v)+|v|^2).
\]

The middle quadratic form lies between one half and three halves of
`|u|^2+|v|^2`.  Since `1/b<=1/t<=1/a`,

\[
\frac{w_m}{3\sqrt2}(|u|^2+|v|^2)
\le\Xi_m
\le w_m(|u|^2+|v|^2),
\]

where `w_m=(b-a)/a asymp 1/m`.

## 3. Endpoint jumps cost no square energy

The endpoint identity from `T-105470` is

\[
H((m+1)-)=4(\delta_{m+1}-e_{m+1}),
\]

with

\[
e_m=a_m-(2+\sqrt2)\mathbf1_{2\mid m}a_{m/2}
 +(1+2\sqrt2)\mathbf1_{4\mid m}a_{m/4}
 -\sqrt2\mathbf1_{8\mid m}a_{m/8}.
\]

In the weighted endpoint Hilbert space, reverse and ordinary triangle
inequalities give

\[
(A_M-\sqrt{J_M^{(2)}})_+^2\le N_M^2
\le(A_M+\sqrt{J_M^{(2)}})^2,
\]

where `A_M` is the right-endpoint norm, `N_M` the right/left endpoint norm, and

\[
J_M^{(2)}=\sum_{m=M}^{2M-1}w_m|e_{m+1}|^2.
\]

The frozen coefficient diagonal gives

\[
\sum_{M/8<n\le2M}|a_n|^2=M^{o(1)}.
\]

Changing variables in the four dyadic terms and using `w_m<<1/M` yields

\[
J_M^{(2)}\ll M^{-1}\sum_{M/8<n\le2M}|a_n|^2
=M^{-1+o(1)}.
\]

Therefore

\[
\int_M^{2M}|H(X)|^2\frac{dX}{X}=M^{o(1)}
\quad\Longleftrightarrow\quad
\mathcal E_M=M^{o(1)}.
\]

## 4. Exact discrete Gram

Since `delta_m=H(m+)/4`, finite expansion gives

\[
\mathcal E_M
=
\sum_{n,r}a_n\overline{a_r}G_M(n,r),
\]

where

\[
G_M(n,r)=\frac1{16}
\sum_{m=M}^{2M}\frac{K_L(m/n)K_L(m/r)}m.
\]

For every finite `(c_n)`,

\[
\sum_{n,r}c_n\overline{c_r}G_M(n,r)
=\frac1{16}\sum_{m=M}^{2M}
 {\left|\sum_nc_nK_L(m/n)\right|^2\over m}\ge0.
\]

Thus `G_M` is positive semidefinite.  A common nonzero term requires
`1<=m/n<8` and `1<=m/r<8`, hence

\[
G_M(n,r)=0\quad\text{unless}\quad1/8<n/r<8.
\]

Also `||K_L||_infinity=8sqrt(2)`, so

\[
G_M(n,n)\le8\sum_{m=M}^{2M}\frac1m\ll1.
\]

The frozen coefficient energy therefore makes

\[
D_M=\sum_n|a_n|^2G_M(n,n)=M^{o(1)}.
\]

Writing

\[
\mathcal N_M=\sum_{n\ne r}a_n\overline{a_r}G_M(n,r),
\]

one has `mathcal E_M=D_M+mathcal N_M>=0` and

\[
(\mathcal N_M)_+\le\mathcal E_M
\le D_M+(\mathcal N_M)_+.
\]

Consequently

\[
\mathrm{F1HCNC}_{105481}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480},
\]

where `F1HCNC105481` is the subpower positive-part estimate for the signed
distinct-product off-diagonal.

## 5. Mellin--Plancherel coordinate

Put `k(u)=K_L(e^u)` and

\[
A(t)=\sum_na_nn^{-it}.
\]

Then

\[
H(e^x)=\sum_na_nk(x-\log n),
\qquad
\widehat H(t)=\widehat k(t)A(t).
\]

Plancherel gives

\[
\int_0^\infty|H(X)|^2\frac{dX}{X}
=\frac1{2\pi}\int_{\mathbb R}
 |\widehat k(t)|^2|A(t)|^2dt.
\]

Equivalently the kernel autocorrelation vanishes for log-separations at least
`log 8`, giving the same ratio-eight near-collision geometry.

## 6. Positive critical analytic-square coordinate

The latest PR #719 head proves

\[
\widehat{e^{-x/4}P(D)j_U}(t)
=P(1/4+it)e^{-2it\log2}r_A(t)^2\mathscr Q_U(t),
\]

where `r_A(t)>0` and

\[
\mathscr Q_U(t)
=\int_0^1(1-\theta)S_{U,\theta}(t)^2d\theta.
\]

Hence Plancherel gives

\[
\int e^{-x/2}|P(D)j_U(x)|^2dx
={1\over2\pi}\int
 |P(1/4+it)|^2r_A(t)^4|\mathscr Q_U(t)|^2dt.
\]

On the output of a source packet with `M/8<n<=2M`, the critical weight is
comparable to `M^(-1/2)`.  Thus the packet Gram is equivalent, across its fixed
finite collection of output blocks, to `M^(1/2)` times this positive spectral
norm.

Finally,

\[
|\mathscr Q_U(t)|^2
\le\frac12\int_0^1(1-\theta)|S_{U,\theta}(t)|^4d\theta.
\]

This gives the stronger sufficient route

```text
F1FOURTH105483 -> F1ASQ2_105483 <=> F1GRAM105480.
```

It keeps the full Beta assembly before the modulus square.

## 7. A source-blind square theorem is false

Let `M` be divisible by four, `N=M/4`, and

\[
a_n=N^{-1/2}\mathbf1_{M\le n<5M/4}.
\]

Then `sum|a_n|^2=1` and `2<=a_n sqrt(n)<sqrt(5)`.  For
`3M/2<=m<7M/4`, every ratio `m/n` lies in `(6/5,7/4)`, so

\[
K_L(m/n)\ge\kappa=8-4\sqrt{7/4}>0.
\]

There are `N` such integers, and therefore

\[
\mathcal E_M
=\sum_{m=M}^{2M}\frac{|H(m+)|^2}{16m}
\ge\frac{\kappa^2}{448}M.
\]

Unit coefficient energy can thus produce linear Gram energy.  No universal
Schur, Bessel, Hodge, or diagonal-energy estimate closes physical collapse.

## 8. Final implication matrix

```text
F1FOURTH105483 -> F1ASQ2_105483
                       <=> F1GRAM105480

F1HCNC105481
  <=> F1GRAM105480
  -> F1HARDY105470
  <=> F1VAR105460
  <=> REFSIG106150
  <=> SFSC106150
  -> WKSFSC106150
  -> BCI102990
  -> RH.
```

The first two nodes are the optional square route.  The canonical endpoint
remains the sharper `l1` Hardy gate.  A completion must exploit the literal
signed Boolean source—such as its least-prime Calderon difference or connected
Kummer incidence—rather than a source-free physical Gram bound.

`F1FOURTH105483`, `F1ASQ2_105483`, `F1HCNC105481`, `F1GRAM105480`,
`F1HARDY105470`, `BCI102990`, and RH remain unproved.
