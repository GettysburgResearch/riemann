# L-23716 — Centered digital energy descent

Claim ID: `L-23716`  
Title: Linear centered boundary energy gives a square-root error in the base-five Abel recurrence and therefore forces eventual positivity  
Status: **PROPOSED COMPLETE CONDITIONAL LEMMA; CENTERED ENERGY BOUND OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23715`, `L-23713`  
Scope: correct energy scale and eventual-positivity transfer

## 1. Centered digital Abel identity

Let

\[
Z(y)=C(y)-a_5\log y
\]

and, for `M=floor(y)`, put

\[
Z_m(y)=m^{-1/2}Z(y/m).
\tag{L-23716.1}
\]

The centered convolution from `L-23715` is

\[
F_5(y)=
\sum_{m\le y}\frac{c_5(m)}{\sqrt m}Z(y/m),
\]

where `F_5(y)=O(1)`. Finite Abel summation gives

\[
\boxed{
\begin{aligned}
Z(y)={}&F_5(y)+2^{-1/2}Z(y/2)-s_5(M)Z_M(y)\\
&-\sum_{m=2}^{M-1}s_5(m)[Z_m(y)-Z_{m+1}(y)].
\end{aligned}}
\tag{L-23716.2}

## 2. Centered endpoint charge

Because `1<=y/M<2`, the shell on that interval contains only its first source atom:

\[
C(y/M)=p(y/M).
\]

Thus

\[
Z(y/M)=p(y/M)-a_5\log(y/M)
\]

is uniformly bounded. Hence

\[
\boxed{
|s_5(M)Z_M(y)|
\ll\frac{1+\log M}{\sqrt M}=o(1).
}
\tag{L-23716.3}

## 3. Centered discrete energy

Define

\[
\boxed{
\mathcal E_{5,c}(y)
=
\sum_{m=2}^{M-1}
 m^2|Z_m(y)-Z_{m+1}(y)|^2.
}
\tag{L-23716.4}

With

\[
\kappa_5^2=\sum_{m=2}^{\infty}\frac{s_5(m)^2}{m^2}<\infty,
\]

Cauchy--Schwarz in (L-23716.2) gives

\[
\boxed{
Z(y)
\ge
2^{-1/2}Z(y/2)
-\kappa_5\sqrt{\mathcal E_{5,c}(y)}
-O(1).
}
\tag{L-23716.5}

The bounded forcing and endpoint have been absorbed in the absolute constant.

## 4. Linear energy implies eventual positivity

Assume

\[
\boxed{
\mathcal E_{5,c}(y)=O(1+\log y).
}
\tag{L-23716.6}

Then

\[
Z(y)
\ge
qZ(y/2)-C\sqrt{1+\log y},
\qquad q=2^{-1/2}<1.
\tag{L-23716.7}

Iterate until `y/2^J` lies in one fixed compact interval. Since

\[
\sum_{j=0}^{J-1}q^j
\sqrt{1+\log(y/2^j)}
\ll\sqrt{1+\log y},
\]

and the compact terminal value is bounded below, one obtains

\[
\boxed{
Z(y)\ge-O(\sqrt{1+\log y}).
}
\tag{L-23716.8}

Therefore

\[
\boxed{
C(y)
=a_5\log y+Z(y)
\ge
a_5\log y-O(\sqrt{\log y})>0
}
\tag{L-23716.9}

for every sufficiently large `y`.

The `O(log y)` energy scale is compatible with nonzero critical-line oscillations; unlike the refuted little-`o` targets, it does not force their boundary Hardy mass to vanish.

## 5. Continuous centered boundary energy

Put

\[
\mathcal Z(t)=Z(e^t)=Q(t)-a_5t
\]

and define

\[
\boxed{
V(t)=\mathcal Z'(t)+\frac12\mathcal Z(t).
}
\tag{L-23716.10}

For the continuous interpolation

\[
\mathcal Z_y(x)=x^{-1/2}Z(y/x),
\]

one has

\[
\mathcal Z_y'(x)=-x^{-3/2}V(\log(y/x)).
\]

The same cellwise Cauchy--Schwarz argument as in `L-23713` gives

\[
\boxed{
\mathcal E_{5,c}(e^T)
\le
\int_0^{T-\log2}|V(t)|^2dt.
}
\tag{L-23716.11}

Hence the continuous sufficient theorem is

\[
\boxed{
\int_0^T|V(t)|^2dt=O(T).
}
\tag{L-23716.12}

## 6. Exact Hardy multiplier

From

\[
\widehat Q(z)=\frac{h(z)}{z^2},
\qquad
\widehat{\mathcal Z}(z)=\frac{h(z)-a_5}{z^2},
\]

and `mathcal Z(0)=0`,

\[
\boxed{
\widehat V(z)
=(z+1/2)\widehat{\mathcal Z}(z)
=rac{(z+1/2)(h(z)-a_5)}{z^2}.
}
\tag{L-23716.13}

The double zero subtraction removes the forbidden cubic-energy main mode. Since `h(z)-a_5=O(z)`, the multiplier has only a permitted simple pole at `z=0`, corresponding to a constant physical mode.

Laplace Plancherel and the elementary bounded Abel--Cesaro comparison give

\[
\boxed{
\int_0^T|V(t)|^2dt=O(T)
}
\]

if and only if

\[
\boxed{
\sup_{0<\sigma\le\sigma_0}
\sigma
\int_{-\infty}^{\infty}
\left|
\frac{(z+1/2)(h(z)-a_5)}{z^2}
\right|^2d\tau
<\infty,
\qquad z=\sigma+i\tau.
}
\tag{L-23716.14}

The factor `1/(2pi)` is again immaterial.

## 7. Proof boundary

Closed conditionally:

```text
centered O(log y) discrete energy
-> centered residual >= -O(sqrt(log y))
-> eventual positivity of C;

uniform centered Hardy bound
-> centered O(log y) discrete energy.
```

Open:

- the uniform centered Hardy bound (L-23716.14);
- its source-specific reflected-Selberg proof;
- Greedy Slack/DCRS;
- RH.
