# L-23717 — Endpoint atoms, exact shell decomposition, and upper-half negativity

Claim ID: `L-23717`  
Title: Every parabolic shell is a sum of explicit endpoint residual atoms, and each atom is already under target on the whole upper half  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: PR #265 `L-26201`; PR #276 `T-27501`; elementary finite algebra and calculus  
Scope: exact endpoint/shell geometry; no prime-tail theorem and no RH conclusion

## 1. Parabolic seed and endpoint atom

For an integer endpoint `X>=2`, put

\[
b_X(m)=2\sqrt m\left[\log\frac Xm-2\left(1-\sqrt{\frac mX}\right)\right]
\qquad(2\le m\le X),
\tag{L-23717.1}
\]

and extend `b_X(m)=0` for `m>X`. Retain the divisor-gradient response

\[
v_q(b_X)=\sum_{kq\le X}\bigl[b_X(kq)-b_X(kq+1)\bigr]
\qquad(q\ge2),
\tag{L-23717.2}
\]

and the logarithmic target

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X}.
\tag{L-23717.3}
\]

For `T>=3`, define the endpoint increments

\[
\Gamma_T(q)=v_q(b_T)-v_q(b_{T-1}),
\tag{L-23717.4}
\]

\[
\delta_T(q)=\frac{\ell_T}{\sqrt q}\mathbf 1_{q<T},
\qquad
\ell_T=\log\frac T{T-1},
\tag{L-23717.5}
\]

and the endpoint residual atom

\[
\boxed{e_T(q)=\Gamma_T(q)-\delta_T(q).}
\tag{L-23717.6}
\]

The target increment is exact:

\[
w_T(q)-w_{T-1}(q)=\delta_T(q).
\tag{L-23717.7}
\]

PR #265 proves that the associated row atom

\[
a_T=d_T-d_{T-1}
\]

is coefficientwise nonnegative. Hence `Gamma_T` is the response of one genuine nonnegative average-binomial carry atom. This positivity is useful but is not used to infer the sign of `e_T`.

## 2. Closed endpoint profile

Put

\[
N=T-1,
\qquad
\eta_T=4\left(\frac1{\sqrt T}-\frac1{\sqrt N}\right)<0,
\tag{L-23717.8}
\]

and define

\[
F_T(m)=2\ell_T\sqrt m+\eta_Tm
\qquad(2\le m\le N),
\tag{L-23717.9}
\]

with `F_T(T)=0`. Direct subtraction of (L-23717.1) gives

\[
\boxed{b_T(m)-b_{T-1}(m)=F_T(m)\qquad(2\le m\le N).}
\tag{L-23717.10}
\]

Therefore, for every `2<=q<T`,

\[
\boxed{
\Gamma_T(q)=
\sum_{kq\le N}\bigl[F_T(kq)-F_T(kq+1)\bigr],
}
\tag{L-23717.11}
\]

where the convention `F_T(T)=0` handles the entering right endpoint exactly. No continuum approximation or prime theorem occurs in this formula.

## 3. Exact shell telescope

For integers `2<=Y<X`, extend every response and target by zero above its endpoint and put

\[
r_X(q)=v_q(b_X)-w_X(q),
\qquad
s_{X,Y}(q)=r_X(q)-r_Y(q).
\tag{L-23717.12}
\]

Then the endpoint increments telescope without a boundary remainder:

\[
\boxed{
s_{X,Y}(q)=\sum_{T=Y+1}^{X}e_T(q).
}
\tag{L-23717.13}
\]

For a real lower cutoff `z>=2`, define the ordinary-prime atom tail

\[
\mathcal A_T(z)
=
\sum_{\substack{z\le p<T\\p\,\text{prime}}}
(\log p)e_T(p)
\tag{L-23717.14}
\]

and the finite shell tail

\[
\mathcal S_{X,Y}(z)
=
\sum_{\substack{z\le p\le X\\p\,\text{prime}}}
(\log p)s_{X,Y}(p).
\tag{L-23717.15}
\]

Equation (L-23717.13) gives the exact decomposition

\[
\boxed{
\mathcal S_{X,Y}(z)
=
\sum_{T=Y+1}^{X}\mathcal A_T(z).
}
\tag{L-23717.16}
\]

Consequently, atomwise upper-tail order would imply every fixed-ratio and dyadic `WSTS` charge with the strongest possible value zero.

## 4. Radical-tail formula

For `m>=1`, define the truncated radical logarithm

\[
L_z(m)=
\sum_{\substack{p\mid m\\p\ge z}}\log p,
\qquad L_z(1)=0.
\tag{L-23717.17}
\]

Swap the two finite sums in (L-23717.11). The positive occurrence `p|m` and the negative occurrence `p|m-1` give

\[
\boxed{
\sum_{\substack{z\le p<T\\p\,\text{prime}}}
(\log p)\Gamma_T(p)
=
\sum_{m=2}^{N}
F_T(m)\,[L_z(m)-L_z(m-1)].
}
\tag{L-23717.18}
\]

Thus the atomwise weighted-tail assertion is the explicit finite radical inequality

\[
\boxed{
\sum_{m=2}^{N}
F_T(m)\,[L_z(m)-L_z(m-1)]
\le
\ell_T
\sum_{\substack{z\le p\le N\\p\,\text{prime}}}
\frac{\log p}{\sqrt p}.
}
\tag{L-23717.19}
\]

This identity is a useful proof firewall: a proposed proof may not replace `L_z` by `log m`, delete squarefull corrections, or take absolute values before the two neighboring divisor ledgers are combined.

## 5. The whole upper half is closed termwise

For every integer

\[
\frac N2<q<N,
\]

only the first multiple occurs. Equation (L-23717.11) gives

\[
\Gamma_T(q)
=
4\left(\frac1{\sqrt N}-\frac1{\sqrt T}\right)
-
\frac{2\ell_T}{\sqrt q+\sqrt{q+1}}.
\tag{L-23717.20}
\]

The elementary inequality

\[
\log t\ge1-\frac1t
\qquad(t\ge1)
\]

with `t=sqrt(T/N)` gives

\[
4\left(\frac1{\sqrt N}-\frac1{\sqrt T}\right)
\le\frac{2\ell_T}{\sqrt N}.
\tag{L-23717.21}
\]

Because `q<N`,

\[
\frac1{\sqrt q}
+
\frac2{\sqrt q+\sqrt{q+1}}
\ge\frac2{\sqrt N}.
\tag{L-23717.22}
\]

Combining (L-23717.20)--(L-23717.22),

\[
\boxed{e_T(q)\le0\qquad(N/2<q<N).}
\tag{L-23717.23}
\]

At the possible endpoint `q=N`, equation (L-23717.11) gives `Gamma_T(N)=F_T(N)`. Put `x=1/N`. The required inequality is

\[
(2-x)\log(1+x)
\le
4\left(1-(1+x)^{-1/2}\right).
\tag{L-23717.24}
\]

To prove it, write `t=sqrt(1+x)` and

\[
\Phi(t)=2(1-t^{-1})-(3-t^2)\log t.
\]

Then `Phi(1)=0`, and after multiplication by `t^2`, the derivative numerator is

\[
2+2t^3\log t-3t+t^3.
\]

It vanishes at one and has derivative

\[
t^2(5+6\log t)-3>0
\qquad(t>1).
\]

Hence `Phi>=0`, proving (L-23717.24) and therefore

\[
\boxed{e_T(N)\le0.}
\tag{L-23717.25}
\]

We have proved the unconditional scale statement

\[
\boxed{
e_T(q)\le0
\qquad
\left(\frac{T-1}{2}<q<T\right).
}
\tag{L-23717.26}
\]

Every positive endpoint-atom violation is thus forced below half scale before any prime-distribution estimate is used.

## 6. Proof boundary

Closed exactly in this lemma:

1. the endpoint profile (L-23717.9)--(L-23717.11);
2. the complete shell telescope;
3. the radical-tail formula;
4. termwise negativity throughout the upper half.

Open:

1. the atomwise prime-tail inequality (L-23717.19) below half scale;
2. a cofinal shell-tail theorem;
3. RH.
