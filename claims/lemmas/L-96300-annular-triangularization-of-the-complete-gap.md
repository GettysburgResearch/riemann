# L-96300 — A scaled second difference localizes the complete prime-power gap to one compact multiplicative annulus

Claim ID: `L-96300`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: the complete-gap renewal identity of PR #353, especially `L-90021`  
RH status: **not assumed**

## 1. Complete gap and renewal state

Let

\[
F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
\]

be the complete prime-power parabolic gap, and put

\[
Y(t)=-e^{-t/2}F_\Lambda(e^t),\qquad t\ge0.
\]

The exact renewal representation is

\[
Y(t)=\int_{[0,t]}K(t-u)\,dR_\Lambda(u),
\qquad
K(v)=v e^{-v/2}\mathbf 1_{v\ge0},
\tag{L-96300.1}
\]

where

\[
dR_\Lambda(u)
=
\sum_{q=p^a}\frac{\Lambda(q)}q\,\delta_{\log q}(du)
-e^{-u}S_\Lambda(\lfloor e^u\rfloor)\,du
\tag{L-96300.2}
\]

and

\[
S_\Lambda(N)=(N+1)\log N-\log(N!).
\]

## 2. Scaled second difference

Fix `h>0` and define

\[
(\Delta_h^{(2)}Y)(t)
=Y(t)-2e^{-h/2}Y(t-h)+e^{-h}Y(t-2h),
\tag{L-96300.3}
\]

with `Y(v)=0` for `v<0`.

Substituting (L-96300.1) and writing `v=t-u`, the common exponential factor gives

\[
\begin{aligned}
&K(v)-2e^{-h/2}K(v-h)+e^{-h}K(v-2h)\\
&\quad=e^{-v/2}
\bigl[v-2(v-h)_+ +(v-2h)_+\bigr].
\end{aligned}
\]

Therefore

\[
\boxed{
\kappa_h(v)=
\begin{cases}
ve^{-v/2},&0\le v<h,\\
(2h-v)e^{-v/2},&h\le v<2h,\\
0,&v\ge2h,
\end{cases}}
\tag{L-96300.4}
\]

is nonnegative and compactly supported, and

\[
\boxed{
(\Delta_h^{(2)}Y)(t)
=
\int_{[t-2h,t]}\kappa_h(t-u)\,dR_\Lambda(u).
}
\tag{L-96300.5}
\]

Thus the complete RH-sensitive gap is converted into one fixed-width prime-power quadrature discrepancy. No tail outside the annulus survives.

## 3. Arithmetic form

Using (L-96300.2),

\[
\boxed{
\begin{aligned}
(\Delta_h^{(2)}Y)(t)
={}&
\sum_{e^{t-2h}<q=p^a\le e^t}
\frac{\Lambda(q)}q\,
\kappa_h(t-\log q)\\
&-
\int_{t-2h}^{t}
\kappa_h(t-u)e^{-u}
S_\Lambda(\lfloor e^u\rfloor)\,du.
\end{aligned}}
\tag{L-96300.6}
\]

Both terms are individually nonnegative. The remaining arithmetic problem is their discrepancy on one compact multiplicative annulus.

## 4. Translation to the original endpoint

Since

\[
e^{-h/2}Y(t-h)=-e^{-t/2}F_\Lambda(e^{t-h}),
\]

(L-96300.3) becomes

\[
\boxed{
(\Delta_h^{(2)}Y)(t)
=-e^{-t/2}
\left[
F_\Lambda(e^t)-2F_\Lambda(e^{t-h})+F_\Lambda(e^{t-2h})
\right].
}
\tag{L-96300.7}
\]

For `X=e^t`, define

\[
\mathfrak A_h(X)
=F_\Lambda(X)-2F_\Lambda(e^{-h}X)+F_\Lambda(e^{-2h}X).
\tag{L-96300.8}
\]

Then (L-96300.5)--(L-96300.7) are an exact compact-annulus formula for `mathfrak A_h`.

## 5. Mellin multiplier

Whenever the Mellin integrals converge absolutely,

\[
\boxed{
\widehat{\mathfrak A_h}(s)
=(1-e^{-hs})^2\widehat{F_\Lambda}(s).
}
\tag{L-96300.9}
\]

If `Re(s)>0`, then `|e^{-hs}|<1`, so

\[
1-e^{-hs}\ne0.
\tag{L-96300.10}
\]

The annular filter therefore does not cancel any pole corresponding to a zero with `Re(rho)>1/2`.

## 6. Scope

This lemma proves the localization identity and pole-safe multiplier. It does not estimate the quadrature discrepancy in (L-96300.6). The load-bearing producer is a polylogarithmic or subpower bound for `mathfrak A_h` at one fixed `h>0`.
