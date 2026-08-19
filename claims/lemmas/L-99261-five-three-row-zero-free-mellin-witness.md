# L-99261 — One positive 5:3 component-row combination has an exact zero-free Mellin numerator

Claim ID: `L-99261`  
Status: **PROVED EXACT ANALYTIC THEOREM**  
Created: 2026-08-20  
Depends on: the canonical row formulas; `L-99240` for the positive SHARP kernels  
RH status: **not assumed**

## 1. One conclusion-facing row

Put

\[
 W_X:=5c_X(2)+3c_X(3),
 \qquad
 Q_*(Y):=5Q_Y(2)+3Q_Y(3).
\]

The canonical logarithmic coefficients collapse to

\[
 \boxed{
 Q_*(Y)
 =15h_Y(2)+6h_Y(3)+3h_Y(4)
  +6\sum_{m\ge5}h_Y(m),
 }
 \tag{L-99261.1}
\]

so every coefficient in the unsieved canonical row is positive. Moreover

\[
 \kappa_*(t):=5\kappa_2(t)+3\kappa_3(t)>0
\]

and

\[
 \boxed{
 Q_*(Y)=\int_1^YT(Y/t)\kappa_*(t)\frac{dt}{t}.
 }
 \tag{L-99261.2}
\]

## 2. Exact Mellin numerator

For `z=s+1/2`, the two row numerators are

\[
 P_2(z)=2\,2^{-z}-1-3^{-z},
\]

and

\[
 3P_3(z)=5\,3^{-z}-2^{-z}-1-3\,4^{-z}.
\]

Writing `a=2^{-z}` and adding gives

\[
\begin{aligned}
 5P_2(z)+3P_3(z)
 &=9a-6-3a^2\\
 &=\boxed{-3(a-1)(a-2)}.
\end{aligned}
\tag{L-99261.3}
\]

Therefore

\[
 \boxed{
 \int_1^\infty W_X X^{-s-1}dX
 =\frac6{s^2}
  -\frac{3(2^{-z}-1)(2^{-z}-2)}{s^2\zeta(z)}.
 }
 \tag{L-99261.4}
\]

If `0<Re z<1`, then neither factor can vanish:

```text
2^(-z)=1  would force Re z=0;
2^(-z)=2  would force Re z=-1.
```

Thus every open-strip zero of zeta survives in this **single positive linear
combination**. No large-row asymptotic or zero-dependent row selection is
needed.

## 3. Exact primitive-prefix identity

Let

\[
 q(n)=6\mathbf1_{n=1}-6\mu(n)
 +9\mathbf1_{2\mid n}\mu(n/2)
 -3\mathbf1_{4\mid n}\mu(n/4)
\tag{L-99261.5}
\]

and

\[
 C_*(x)=\sum_{n\le x}\frac{q(n)}{\sqrt n}.
\]

Finite divisor switching gives

\[
 \boxed{
 W_X=\int_1^X C_*(t)\frac{dt}{t}.
 }
 \tag{L-99261.6}
\]

This identifies the 5:3 row with the integrated primitive-prefix source of the
C4MBI programme. Pointwise positivity of `C_*` is stronger than needed.

## 4. Landau consequence

Eventual nonnegativity of the single function `W_X` is sufficient for RH. A
compact initial interval contributes an entire Mellin correction. Landau's
one-sign theorem then applies to the eventual nonnegative tail, while
(L-99261.4) is analytic at every positive real `s` and retains every hypothetical
nonreal pole with `Re s>0`.
