# L-105480 — The F1 Hardy variation is controlled by one square energy, and the cell L2 norm is discrete

Claim ID: `L-105480`

Status: **PROVED EXACT HILBERT REDUCTION AND UNIFORM CELL-SQUARE LOCALIZATION**

Retain the finite real coefficient sequence `(a_n)`, the derivative-outer
current

\[
H(X)=\sum_n a_n K_L(X/n),
\]

and the one-Hardy primitive of `L-105471`.  Put

\[
\delta_m=\Delta_2W(m)=\frac14H(m+).
\tag{L-105480.1}
\]

## 1. Weighted Cauchy

For one dyadic block define

\[
\mathcal L_M
 =\sum_{m=M}^{2M}\frac{|\delta_m|}{m},
\qquad
\mathcal E_M
 =\sum_{m=M}^{2M}\frac{|\delta_m|^2}{m}.
\tag{L-105480.2}
\]

Then

\[
\boxed{
\mathcal L_M^2
\le
\left(\sum_{m=M}^{2M}\frac1m\right)\mathcal E_M
\le
\left(\log2+\frac2M\right)\mathcal E_M.
}
\tag{L-105480.3}
\]

Thus the square premise

```text
F1GRAM105480:
  E_M = M^(o(1)) on every frozen dyadic source block
```

implies `F1HARDY105470`.

## 2. Exact L2 mass of one integer cell

By `L-105470`, on `m<X<m+1`,

\[
H(X)=A_m+B_m\sqrt X.
\]

Put

\[
a=\sqrt m,
\qquad b=\sqrt{m+1},
\qquad u_m=H(m+),
\qquad v_m=H((m+1)-).
\]

The exact logarithmic cell square is

\[
\boxed{
\begin{aligned}
\Xi_m
&:=\int_m^{m+1}|H(X)|^2\frac{dX}{X}\\
&=2A_m^2\log\frac ba
  +4A_mB_m(b-a)
  +B_m^2(b^2-a^2).
\end{aligned}}
\tag{L-105480.4}
\]

Since `b^2-a^2=1`, this is an elementary closed expression.

For a linear function on `[a,b]`,

\[
\int_a^b |q(t)|^2dt
=\frac{b-a}{3}(|u|^2+\operatorname{Re}(u\bar v)+|v|^2).
\]

The Hermitian form in parentheses has eigenvalues `1/2` and `3/2` relative
to `|u|^2+|v|^2`.  Using `1/b<=1/t<=1/a`, and

\[
w_m=\frac{b-a}{a}=\sqrt{1+1/m}-1,
\]

one obtains

\[
\boxed{
\frac{w_m}{3\sqrt2}(|u_m|^2+|v_m|^2)
\le\Xi_m
\le w_m(|u_m|^2+|v_m|^2).
}
\tag{L-105480.5}
\]

## 3. Endpoint jump ledger in L2

Let `e_m` be the four-term jump filter of `L-105471`, so

\[
H((m+1)-)=4(\delta_{m+1}-e_{m+1}).
\tag{L-105480.6}
\]

Define

\[
\begin{aligned}
A_M^2&=\sum_{m=M}^{2M-1}w_m
 (|\delta_m|^2+|\delta_{m+1}|^2),\\
N_M^2&=\sum_{m=M}^{2M-1}w_m
 (|\delta_m|^2+|\delta_{m+1}-e_{m+1}|^2),\\
J_M^{(2)}&=\sum_{m=M}^{2M-1}w_m|e_{m+1}|^2.
\end{aligned}
\tag{L-105480.7}
\]

The triangle inequality in the weighted endpoint Hilbert space gives

\[
\boxed{
(A_M-\sqrt{J_M^{(2)}})_+^2
\le N_M^2
\le(A_M+\sqrt{J_M^{(2)}})^2.
}
\tag{L-105480.8}
\]

The frozen coefficient energy of `L-105472` is

\[
\sum_{M/8<n\le2M}|a_n|^2=M^{o(1)}.
\]

Since `e_m` is a fixed linear combination of
`a_m,a_{m/2},a_{m/4},a_{m/8}`, and `w_m<=1/(2m)`, changing variables gives

\[
\boxed{
J_M^{(2)}
\ll\frac1M
\sum_{M/8<n\le2M}|a_n|^2
=M^{-1+o(1)}.
}
\tag{L-105480.9}
\]

Combining (L-105480.5)--(L-105480.9), and using
`w_m asymp 1/m`, proves

\[
\boxed{
\int_M^{2M}|H(X)|^2\frac{dX}{X}=M^{o(1)}
\Longleftrightarrow
\sum_{m=M}^{2M}\frac{|\delta_m|^2}{m}=M^{o(1)}.
}
\tag{L-105480.10}
\]

The equivalence uses the same frozen source and boundary convention.  It is
stronger than the L1 discretization of `T-105470`, but remains only a
sufficient route to that theorem.
