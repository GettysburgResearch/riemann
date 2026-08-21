# L-100713 — Three positive carrier removals leave one dyadic Harnack factor

Claim ID: `L-100713`  
Status: **PROVED EXACT POSITIVE BRIDGE; FINAL HARNACK ESTIMATE OPEN**  
Created: 2026-08-21  
Depends on: `L-100001`; `L-100511`; `L-100712`  
RH status: **not assumed**

Let

\[
A_\lambda=I-2^\lambda S_2,
\qquad (S_2f)(X)=f(X/2),
\]

and write

\[
\mathscr D_4=A_0A_{1/2}A_1A_{3/2}.
\]

Recall the cubic critical identities

\[
C_3(X)=192\mathcal B(3/2)X-R_{3,1}(X),
\tag{L-100713.1}
\]

\[
(D-3/2)R_{3,1}=-6H_2^U,
\qquad D={d\over d\log X},
\tag{L-100713.2}
\]

where

\[
H_2^U(X)=\sum_n\frac{\beta(n)}{\sqrt n}U(X/n)^2,
\qquad U(y)=4(\sqrt y-1)_+.
\]

The mixed quadratic theorem gives

\[
Q_{0,2}(X)
=\sum_n\frac{\beta(n)}{\sqrt n}S_+(X/n)^2\ge0,
\qquad S_+(y)=4\sqrt y\,\mathbf1_{y\ge1}.
\tag{L-100713.3}
\]

## 1. Two finite differences of the quadratic packet are positive

The differential identity

\[
D H_2^U=Q_{1,1}\ge0
\tag{L-100713.4}
\]

and the second mixed identity

\[
(D-\tfrac12)D H_2^U
=\frac12Q_{0,2}\ge0
\tag{L-100713.5}
\]

hold distributionally without activation atoms: `U^2` and `US_+` vanish to
the required order at activation.

Using

\[
A_\lambda f(u)
=\int_0^{\log2}e^{\lambda t}(D-\lambda)f(u-t)\,dt,
\tag{L-100713.6}
\]

we obtain

\[
\boxed{
A_0A_{1/2}H_2^U(X)\ge0.
}
\tag{L-100713.7}
\]

More explicitly,

\[
A_0A_{1/2}H_2^U(e^u)
=\frac12\int_{[0,h]^2}e^{t_2/2}
Q_{0,2}(e^{u-t_1-t_2})\,dt_1dt_2,
\quad h=\log2.
\tag{L-100713.8}
\]

## 2. A globally positive three-factor packet

Apply `A_(3/2)` to (L-100713.2). Equation (L-100713.6) gives

\[
-A_{3/2}R_{3,1}(e^u)
=6\int_0^he^{3t/2}H_2^U(e^{u-t})\,dt.
\]

Define

\[
\boxed{
F_+(X):=-A_0A_{1/2}A_{3/2}R_{3,1}(X).
}
\tag{L-100713.9}
\]

Combining the last display with (L-100713.8) yields the literal positive
representation

\[
\boxed{
\begin{aligned}
F_+(e^u)
=3\int_{[0,h]^3}
&e^{t_2/2+3t_3/2}\\
&\times Q_{0,2}(e^{u-t_1-t_2-t_3})
\,dt_1dt_2dt_3\ge0.
\end{aligned}
}
\tag{L-100713.10}
\]

Thus three of the four cubic carrier factors are paid entirely by already
proved mixed-quadratic positivity.

## 3. The compact detector is one Harnack difference

The missing fourth factor is `A_1=I-2S_2`. Since `A_1X=0`, (L-100713.1)
gives

\[
\begin{aligned}
\mathscr D_4C_3
&=-\mathscr D_4R_{3,1}\\
&=A_1F_+.
\end{aligned}
\]

By `L-100712`, the left side is exactly the compact positive-kernel scalar
`mathcal B_16`. Hence

\[
\boxed{
\mathcal B_{16}(X)
=F_+(X)-2F_+(X/2).
}
\tag{L-100713.11}
\]

This is an exact bridge between two previously separate routes:

```text
all-scale mixed quadratic positivity
 -> a globally positive F_+
 -> one dyadic Harnack defect
 -> compact zero-safe cubic detector.
```

## 4. Exact remaining implication

Since `F_+>=0`, the only remaining estimate is the one-sided normalized
Harnack debt

\[
\boxed{
\int_1^Y[2F_+(X/2)-F_+(X)]_+\frac{dX}{X}=Y^{o(1)}.
}
\tag{L-100713.12}
\]

By (L-100713.11) and `L-100712`, this implies RH.

The theorem does not claim that `F_+(X)/X` is monotone. Indeed
`F_+(X)/X` is a positive smoothing of the signed exponent-`3/2` Euler prefix;
positivity of the prefix does not imply monotonicity of its increments. The
new result is the reduction of the entire critical route to **one Harnack
factor of a globally positive function**, with the other three carrier factors
proved unconditionally.