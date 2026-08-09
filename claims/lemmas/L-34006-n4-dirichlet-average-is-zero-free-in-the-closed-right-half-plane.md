# L-34006 — The N=4 Dirichlet-average Mellin factor is zero-free in the closed right half-plane

Claim ID: `L-34006`

Status: **PROPOSED COMPLETE EXACT HALF-PLANE THEOREM — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-34003`

Scope: exact `N=4` Brownian raw stability; no cofinal theorem and no RH claim

## 1. Explicit numerator

For `N=4`, `L-34003` gives, up to a positive constant and a zero-free gamma factor,

\[
\boxed{
\begin{aligned}
H_4(z)={}&\frac{64}{25}\left(z-\frac1{20}\right)
+\frac{16}{25}\,4^{-z}\left(z+\frac75\right)\\
&+\frac{64}{1225}\,9^{-z}\left(z+\frac{599}{140}\right)
+\frac1{1225}\,16^{-z}\left(z+\frac{363}{35}\right).
\end{aligned}}
\tag{L-34006.1}
\]

We prove

\[
\boxed{H_4(z)\ne0\qquad(\Re z\ge0).}
\tag{L-34006.2}
\]

This is the first case where the leading shift is negative:

\[
\alpha_{4,1}=-\frac1{20}.
\]

Thus the `N=3` proof does not extend by simply declaring every summand to have positive real part.

## 2. Exterior disk: first-term domination

Write

\[
T_1=\frac{64}{25}\left(z-\frac1{20}\right)
\]

and let `R=T_2+T_3+T_4` be the remaining three terms.

For `Re z>=0`,

\[
|4^{-z}|,|9^{-z}|,|16^{-z}|\le1.
\]

Hence

\[
|T_1|\ge \frac{64}{25}\left(|z|-\frac1{20}\right).
\tag{L-34006.3}
\]

The total coefficient of `|z|` in the tail is

\[
\frac{16}{25}+\frac{64}{1225}+\frac1{1225}
=\frac{849}{1225}.
\tag{L-34006.4}
\]

The tail constant is

\[
\frac{16}{25}\frac75
+\frac{64}{1225}\frac{599}{140}
+\frac1{1225}\frac{363}{35}
=\frac{141}{125}.
\tag{L-34006.5}
\]

Therefore

\[
|R|
\le \frac{849}{1225}|z|+\frac{141}{125}.
\tag{L-34006.6}
\]

Comparing (L-34006.3) and (L-34006.6), strict domination holds as soon as

\[
\left(\frac{64}{25}-\frac{849}{1225}\right)|z|
>
\frac{64}{25}\frac1{20}+\frac{141}{125}.
\]

The exact threshold is

\[
\boxed{
R_4:=\frac{7693}{11435}<\frac7{10}.
}
\tag{L-34006.7}
\]

Thus

\[
\boxed{|T_1|>|T_2|+|T_3|+|T_4|}
\tag{L-34006.8}
\]

whenever `Re z>=0` and `|z|>R_4`.  Hence `H_4` has no zero there.

## 3. Interior disk: the middle frequencies stay in a positive sector

It remains to consider

\[
z=x+iy,
\qquad x\ge0,
\qquad |z|\le R_4.
\tag{L-34006.9}
\]

We use only the elementary inequalities

\[
R_4<\frac7{10},
\qquad
R_4<\frac{15}{22},
\qquad
\log4<\frac75,
\qquad
\log9<\frac{11}{5},
\qquad
\pi>3.
\tag{L-34006.10}
\]

For a term

\[
e^{-\lambda z}(z+b),\qquad b>0,
\]

one has

\[
\Re[e^{-\lambda z}(z+b)]
=e^{-\lambda x}
\big[(x+b)\cos(\lambda y)+y\sin(\lambda y)\big].
\tag{L-34006.11}
\]

If `|lambda y|<pi/2`, both displayed contributions are nonnegative and the first is strictly positive.

For the `4^{-z}` term,

\[
|y|\log4
<\frac{15}{22}\frac75<1<\frac\pi2.
\tag{L-34006.12}
\]

For the `9^{-z}` term,

\[
|y|\log9
<\frac{15}{22}\frac{11}{5}
=\frac32<\frac\pi2.
\tag{L-34006.13}
\]

Hence

\[
\boxed{\Re T_2>0,\qquad \Re T_3>0}
\tag{L-34006.14}
\]

throughout the complete half-disk.  The final `16^{-z}` term is so small that we may bound it only by absolute value.

## 4. A uniform positive moat from the second term

Since `x<R_4<7/10`,

\[
4^{-x}>\frac13.
\tag{L-34006.15}
\]

Indeed `x\log4<49/50<1`, and `e<3` gives `4^x<3`.

Also (L-34006.12) gives `|y|log4<1`, hence

\[
\cos(y\log4)>\frac12.
\tag{L-34006.16}
\]

Using `y\sin(y\log4)>=0`, equation (L-34006.11) yields the completely uniform lower bound

\[
\boxed{
\Re T_2
>
\frac{16}{25}\cdot\frac13\cdot\frac75\cdot\frac12
=\frac{56}{375}.
}
\tag{L-34006.17}
\]

On the other hand

\[
|T_4|
\le
\frac1{1225}
\left(\frac7{10}+\frac{363}{35}\right)
=\frac{31}{3430}.
\tag{L-34006.18}
\]

The only possibly negative contribution besides `T_4` is `T_1`, and only when `0<=x<1/20`.  In that range

\[
-\Re T_1
\le\frac{64}{25}\frac1{20}
=\frac{16}{125}.
\tag{L-34006.19}
\]

But exactly

\[
\frac{56}{375}
-rac{16}{125}
-rac{31}{3430}
=rac{3163}{257250}>0.
\tag{L-34006.20}
\]

Therefore, when `0<=x<1/20`, the positive second term alone dominates the entire possible negative contribution of `T_1+T_4`; `T_3` supplies additional positive slack.

When `x>=1/20`, `Re T_1>=0`, so (L-34006.17)--(L-34006.18) already give a strict positive moat, again with `Re T_3>0` extra.

Consequently

\[
\boxed{\Re H_4(z)>0}
\tag{L-34006.21}
\]

throughout the remaining half-disk.

Sections 2--4 prove (L-34006.2).

## 5. Brownian consequence

By `L-34001/L-34003`, the omitted prefactor relating `H_4` to

\[
M_4(z)=\mathbb E[Q_4^z]
\]

has no zeros.  Hence

\[
\boxed{
M_4(z)\ne0\qquad(\Re z\ge0).
}
\tag{L-34006.22}
\]

Equivalently, the raw `N=4` Brownian factor is zero-free in the complete closed right half-plane.

## 6. What the N=4 proof teaches

The mechanism has now survived two mutations beyond the trivial one-term picture:

```text
N=2: two-term exact Rouché;
N=3: first-term exterior domination + all-tail interior sector;
N=4: first-term exterior domination +
     a negative leading shift +
     one high-frequency tail allowed outside the positive sector,
     paid by a quantitative middle-frequency moat.
```

This makes a grouped all-`N` sector/Rouché theorem more plausible, but it also identifies the correct difficulty: as `N` grows, the number of negative low-index shifts and the effective number of non-negligible gamma weights both grow on the `sqrt(N)` scale.  A cofinal proof must therefore group a growing low-frequency packet; fixed-term domination cannot be the final mechanism.

## 7. Proof boundary

Closed exactly:

1. explicit `N=4` numerator;
2. exterior first-term domination;
3. positive-sector control of the `i=2,3` terms;
4. absolute absorption of the high-frequency `i=4` tail;
5. zero-freeness on the complete closed right half-plane.

Open:

1. a growing-packet sector theorem uniform in `N`;
2. cofinal Brownian stability;
3. RH.
