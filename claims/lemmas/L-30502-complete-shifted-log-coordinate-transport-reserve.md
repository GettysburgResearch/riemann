# L-30502 — Complete shifted log-coordinate transport reserve

Claim ID: `L-30502`  
Title: Before any endpoint or divisor-source splitting, the exact shifted central operator has a strict normalized current-value reserve with one logarithmic derivative  
Status: **PROPOSED COMPLETE EXACT ANALYTIC LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: elementary mean-value estimates  
Scope: the complete finite shifted operator, including zero extension and the `-1` lattice shift; no RH conclusion

## 1. Exact normalized operator

Fix `X` and write

\[
q=Xe^{-t},
\qquad
z=q^{-1}=e^t/X.
\tag{L-30502.1}
\]

Let `F` be causal, so `F(u)=0` for `u<0`, and sample

\[
r(q)=q^{-1/2}F(\log(X/q)).
\tag{L-30502.2}
\]

For the exact finite central residual

\[
(\mathcal T_Xr)(q)
=\sum_{k\ge1}
[r(2kq-1)-r((2k+1)q)],
\tag{L-30502.3}
\]

zero extension is already encoded by causality.  Multiplication by `sqrt(q)`
gives the exact log-coordinate operator

\[
\boxed{
\begin{aligned}
(\mathcal A_zF)(t)
=\sum_{k\ge1}\Big[&
(2k-z)^{-1/2}
F(t-\log(2k-z))\\
&-(2k+1)^{-1/2}
F(t-\log(2k+1))
\Big].
\end{aligned}}
\tag{L-30502.4}

For every active integer coordinate `q>=2`,

\[
0\le z\le\frac12.
\tag{L-30502.5}
\]

No infinite/finite boundary subtraction has been made.

## 2. Residual plus adjacent transport

Put

\[
a_k(z)=(2k-z)^{-1/2},
\qquad
b_k=(2k+1)^{-1/2},
\tag{L-30502.6}
\]

and

\[
\delta_k(z)=\log\frac{2k+1}{2k-z}.
\tag{L-30502.7}
\]

Each pair decomposes exactly as

\[
\begin{aligned}
a_kF(t-\log(2k-z))-b_kF(t-\log(2k+1))
={}&(a_k-b_k)F(t-\log(2k-z))\\
&+b_k\big[F(t-\log(2k-z))-F(t-\log(2k+1))\big].
\end{aligned}
\tag{L-30502.8}

For bounded Lipschitz `F`,

\[
\boxed{
\|\mathcal A_zF\|_\infty
\le R(z)\|F\|_\infty+C(z)\|F'\|_\infty,
}
\tag{L-30502.9}
\]

where

\[
R(z)=\sum_{k\ge1}[a_k(z)-b_k],
\qquad
C(z)=\sum_{k\ge1}b_k\delta_k(z).
\tag{L-30502.10}
\]

Both functions increase with `z`, so it is enough to use `z=1/2`.

## 3. Exact rational reserve below one

For every `k`, the mean-value theorem and `log(1+x)<=x` give

\[
a_k(1/2)-b_k
\le\frac34(2k-1/2)^{-3/2},
\tag{L-30502.11}
\]

\[
b_k\delta_k(1/2)
\le\frac32(2k-1/2)^{-3/2}.
\tag{L-30502.12}
\]

For the first two pairs use the rational radical bounds

\[
\sqrt{2/3}<817/1000,
\qquad
577/1000<1/\sqrt3<578/1000,
\tag{L-30502.13}
\]

\[
\sqrt{2/7}<535/1000,
\qquad
447/1000<1/\sqrt5<448/1000.
\tag{L-30502.14}
\]

For the tail `k>=3`,

\[
\sum_{k\ge3}(2k-1/2)^{-3/2}
\le (11/2)^{-3/2}+(11/2)^{-1/2}
=\frac{13}{11}\sqrt{\frac2{11}},
\tag{L-30502.15}
\]

and

\[
\sqrt{2/11}<427/1000.
\tag{L-30502.16}
\]

Consequently

\[
\begin{aligned}
R(1/2)+\frac18C(1/2)
<&\frac{817-577}{1000}+rac{578}{8000}\\
&+\frac{535-447}{1000}
 +\frac{448\cdot3}{1000\cdot56}\\
&+\frac{15}{16}\frac{13}{11}\frac{427}{1000}\\
=&\frac{157933}{176000}
<\frac9{10}.
\end{aligned}
\tag{L-30502.17}

Every inequality is certified by integer squares; no floating estimate is part
of the proof.

Since both `R` and `C` are nonnegative, (L-30502.17) implies separately

\[
R(z)<\frac9{10},
\qquad
C(z)<\frac{36}{5}.
\]

Substitution in (L-30502.9) yields the strict reserve

\[
\boxed{
\|\mathcal A_zF\|_\infty
\le\frac9{10}
\left(\|F\|_\infty+8\|F'\|_\infty\right),
\qquad0\le z\le\frac12.
}
\tag{L-30502.18}

## 4. Why this differs from the rejected boundary split

Equation (L-30502.18) is applied to the complete logarithmic endpoint profile.
It retains simultaneously:

```text
the shifted argument 2kq-1;
the odd argument (2k+1)q;
the zero-extension cutoff;
the endpoint logarithm;
all cancellation between neighboring dilation legs.
```

The macroscopic stopped-power atomic source of `R-30501` never appears.  The
operator is bounded before Möbius inversion, divisor-source typing, Euler
transformation, or a positive part.

## 5. The next derivative channel

Differentiation is explicit.  With `z=e^t/X`,

\[
\begin{aligned}
\frac d{dt}\left[
(2k-z)^{-1/2}F(t-\log(2k-z))
\right]
={}&\frac z2(2k-z)^{-3/2}F(\cdot)\\
&+2k(2k-z)^{-3/2}F'(\cdot).
\end{aligned}
\tag{L-30502.19}

Thus the derivative bank is upper triangular:

```text
current derivative
 -> paired derivative at the same level
    + a positive faster-decaying power channel.
```

This is exactly the structure behind the `6/7` Dirichlet–Taylor reserve of PR
#286, but now the zeroth row retains the complete finite endpoint cancellation.

## 6. Proof boundary

Closed exactly:

1. the normalized finite shifted operator;
2. residual-plus-transport decomposition;
3. a uniform rational reserve `9/10` for the complete current-value channel;
4. exact inclusion of the cutoff rather than a separate boundary norm;
5. the explicit upper-triangular derivative formula.

Open:

1. a closed weighted all-jet or measure-valued norm combining
   (L-30502.18)--(L-30502.19) with the faster-power channels;
2. a direct bound for the signed central-cascade objective in `L-30501`;
3. RH.
