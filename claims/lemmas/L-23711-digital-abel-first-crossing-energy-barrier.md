# L-23711 — Digital Abel first-crossing energy barrier

Claim ID: `L-23711`  
Title: A first negative fifth-aligned cumulative-shell value requires quadratic logarithmic boundary energy  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23708`--`L-23710`  
Scope: exact digital Abel identity and a first-crossing lower bound; no energy upper bound

## 1. Digital convolution equation

Let

\[
C(y)=\mathfrak S_5(y),
\qquad
c_5(m)=1-4v_5(m),
\]

and retain the positive forcing

\[
R_5(y)=p(y)-\sqrt5\,p(y/5).
\]

By `L-23709`,

\[
\boxed{
R_5(y)=
\sum_{m\le y}\frac{c_5(m)}{\sqrt m}C(y/m).
}
\tag{L-23711.1}
\]

The partial sums of `c_5` are the nonnegative base-five digit sums:

\[
\boxed{
\sum_{m\le M}c_5(m)=s_5(M)\ge0.
}
\tag{L-23711.2}
\]

## 2. Exact finite Abel identity

Fix real `y>=1`, put `M=floor(y)`, and define

\[
Y_m(y)=m^{-1/2}C(y/m)
\qquad(1\le m\le M).
\tag{L-23711.3}
\]

Finite Abel summation in (L-23711.1) gives

\[
R_5(y)
=s_5(M)Y_M(y)
+\sum_{m=1}^{M-1}s_5(m)
 [Y_m(y)-Y_{m+1}(y)].
\tag{L-23711.4}
\]

Since `s_5(1)=1` and `Y_1(y)=C(y)`, this is equivalently

\[
\boxed{
\begin{aligned}
C(y)={}&R_5(y)+Y_2(y)-s_5(M)Y_M(y)\\
&-\sum_{m=2}^{M-1}s_5(m)
 [Y_m(y)-Y_{m+1}(y)].
\end{aligned}}
\tag{L-23711.5}
\]

Every term and endpoint in this identity is explicit and finite.

## 3. Endpoint charge

Because `1<=y/M<2`, only the `n=1` source atom occurs in `C(y/M)`. Hence

\[
Y_M(y)=M^{-1/2}p(y/M)\ge0.
\tag{L-23711.6}
\]

Moreover `p'(x)<=1` on `1<=x<=2`, so

\[
\boxed{
0\le s_5(M)Y_M(y)
\le \frac{s_5(M)}{M^{3/2}}.
}
\tag{L-23711.7}
\]

This is an explicit digital endpoint charge, not an omitted terminal term.

## 4. The logarithmic Dirichlet energy

Define

\[
\boxed{
\mathcal E_5(y)
=
\sum_{m=2}^{M-1}
 m^2\left|Y_m(y)-Y_{m+1}(y)\right|^2.
}
\tag{L-23711.8}
\]

The base-five digit sum obeys

\[
s_5(m)\le4(1+\log_5m).
\]

Therefore the absolute constant

\[
\boxed{
\kappa_5^2
=
\sum_{m=2}^{\infty}\frac{s_5(m)^2}{m^2}
<\infty
}
\tag{L-23711.9}
\]

is well defined. Cauchy--Schwarz in (L-23711.5) gives

\[
\boxed{
\left|
\sum_{m=2}^{M-1}s_5(m)[Y_m-Y_{m+1}]
\right|
\le\kappa_5\sqrt{\mathcal E_5(y)}.
}
\tag{L-23711.10}
\]

## 5. First-crossing barrier

Assume that `y_0>1` is the first zero after a positive interval:

\[
C(y)>0\quad(1<y<y_0),
\qquad
C(y_0)=0.
\tag{L-23711.11}
\]

Then

\[
Y_2(y_0)=2^{-1/2}C(y_0/2)\ge0.
\]

Equations (L-23711.5) and (L-23711.10) imply

\[
\boxed{
\mathcal E_5(y_0)
\ge
\frac{
 [R_5(y_0)+Y_2(y_0)-s_5(M)Y_M(y_0)]_+^2
}{\kappa_5^2}.
}
\tag{L-23711.12}
\]

For `y>=5`,

\[
R_5(y)
=4(\sqrt5-1)+(\sqrt5-1)\log y-\sqrt5\log5.
\]

Using (L-23711.7), there are explicit absolute constants `y_*` and `c_*>0` such that every first zero with `y_0>=y_*` satisfies

\[
\boxed{
\mathcal E_5(y_0)\ge c_*(\log y_0)^2.
}
\tag{L-23711.13}
\]

`L-23710` permits the review-facing choice `y_*=100`: the complete preceding annulus is already certified positive.

## 6. Exact meaning for the reflected route

The energy in (L-23711.8) is the multiplicative finite-difference Dirichlet energy of the lower-scale-subtracted source. It is the correct object to map into:

1. the endpoint-projected Green frame of PR #248;
2. the two-frequency physical reflected block of PR #241.

The global Green norm is not used. The critical scalar mode has already been removed into the positive forcing `R_5`, the lower argument `Y_2`, and the explicit endpoint charge.

Consequently, a source-specific upper estimate

\[
\boxed{
\mathcal E_5(y)=o((\log y)^2)
\quad(y\to\infty)
}
\tag{L-23711.14}
\]

would exclude a first zero and prove `C(y)>=0` globally.

## 7. Proof boundary

Closed exactly:

- the digital Abel identity;
- the endpoint charge;
- the finite Dirichlet-energy bound;
- the quadratic energy cost of a first zero.

Open:

- the reflected/local upper estimate (L-23711.14);
- the global sign of `C`;
- `DGB(5)` and Greedy Slack/DCRS;
- RH.
