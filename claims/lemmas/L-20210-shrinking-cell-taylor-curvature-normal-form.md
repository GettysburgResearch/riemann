# L-20210 — Shrinking-cell Taylor and bounded-curvature normal form

Claim ID: `L-20210`  
Title: On the tiled shrinking schedule the renormalized archimedean barrier has a uniform fixed-width normal form and bounded curvature distortion  
Status: `PROPOSED — COMPLETE TAYLOR/CURVATURE ESTIMATE`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the explicit smooth prime-free function `F` used in `T-20205`; `T-20207`  
Scope: fixed `0<a<log 2`, `T in [ra,(r+1)a]`

## 1. Fixed-width coordinates

Write

\[
 T=ra+u,
 \qquad 0\le u\le a.
 \tag{1}

Then

\[
 {T\over r}=a+{u\over r}
 \tag{2}

and

\[
 H_r(T)=F(T)-r^2F(T/r).
 \tag{3}

All derivatives of `F` are bounded on one fixed neighbourhood of `[a,2a]`.

## 2. Uniform Taylor normal form

Taylor's theorem at the fixed base point `a` gives

\[
\boxed{
\begin{aligned}
 r^2F\left(a+{u\over r}\right)
 ={}&r^2F(a)+ruF'(a)+{u^2\over2}F''(a)\\
 &+{u^3\over6r}F'''(a)
 +\mathcal R_{r,4}(u),
\end{aligned}}
 \tag{4}

with

\[
\boxed{
 |\mathcal R_{r,4}(u)|
 \le {a^4\over24r^2}
 \sup_{a\le x\le2a}|F^{(4)}(x)|.}
 \tag{5}

Therefore

\[
\boxed{
\begin{aligned}
 H_r(ra+u)
 ={}&F(ra+u)-r^2F(a)-ruF'(a)\\
 &-{u^2\over2}F''(a)
 -{u^3\over6r}F'''(a)
 +O_a(r^{-2}),
\end{aligned}}
 \tag{6}

uniformly for `0<=u<=a`.

The large source term is now an explicit polynomial in `r` and the fixed local coordinate `u`; only the first term samples the large physical scale.

## 3. Derivative normal forms

Differentiating before expanding gives

\[
 H_r'(T)=F'(T)-rF'(T/r)
 \tag{7}

and

\[
 H_r''(T)=F''(T)-F''(T/r).
 \tag{8}

Uniformly on the tiled cell,

\[
\boxed{
\begin{aligned}
 H_r'(ra+u)
 ={}&F'(ra+u)-rF'(a)-uF''(a)\\
 &-{u^2\over2r}F'''(a)+O_a(r^{-2}),
\end{aligned}}
 \tag{9}

and

\[
\boxed{
 H_r''(ra+u)
 =F''(ra+u)-F''(a)-{u\over r}F'''(a)
 +O_a(r^{-2}).}
 \tag{10}

These formulas provide direct interval centres for the mass mismatch and curvature terms in `L-20209`.

## 4. Bounded curvature distortion

The explicit function `F` has

\[
 F''(T)>0
\]

and its leading large-`T` term is proportional to `e^(T/2)`. The remaining Lerch and reflected-pole derivatives are exponentially smaller. Consequently, for every fixed `a`, there are effective constants

\[
 0<c_a<C_a<\infty
\]

and `r_a` such that for all `r>=r_a` and `0<=u<=a`,

\[
\boxed{
 c_a e^{(ra+u)/2}
 \le H_r''(ra+u)
 \le C_a e^{(ra+u)/2}.}
 \tag{11}

In particular,

\[
\boxed{
 {\sup_{T\in J_r}H_r''(T)
  \over
  \inf_{T\in J_r}H_r''(T)}
 \le {C_a\over c_a}e^{a/2},}
 \tag{12}

uniformly in `r`.

This is the improvement over a fixed base interval `[a,b]`: its dilated physical width grows like `r(b-a)` and the corresponding curvature ratio can grow exponentially in `r`. The tiled cell has fixed width `a` and a uniform distortion constant.

## 5. Local Bregman equivalence

Let

\[
 m_r=\inf_{T\in J_r}H_r''(T),
 \qquad
 L_r=\sup_{T\in J_r}H_r''(T).
\]

For any `T,tau in J_r`,

\[
 {m_r\over2}(T-\tau)^2
 \le D_{H_r}(T,\tau)
 \le {L_r\over2}(T-\tau)^2.
 \tag{13}

By (12), the upper and lower quadratic models are uniformly comparable. In dual mass coordinates,

\[
 {1\over2L_r}|H_r'(T)-H_r'(\tau)|^2
 \le D_{H_r}(T,\tau)
 \le {1\over2m_r}|H_r'(T)-H_r'(\tau)|^2.
 \tag{14}

Thus the exact Bregman penalty and the centered prime-mass square differ only by a fixed cell-dependent condition number, not a growing one.

## 6. Production consequence

At each level `r`, a proof object may use the fixed coordinate `u in [0,a]` and store:

1. directed `F(ra+u)`, `F'(ra+u)`, and `F''(ra+u)` intervals;
2. the exact cubic base polynomial from (4), with the explicit `O(r^-2)` remainder;
3. the complete prime-power prefix moments inside the multiplicative window
   \[
   e^{ra}\le q\le e^{(r+1)a};
   \]
4. transport reserves and curvature-normalized discrepancy squares.

No expanding profile grid or exponentially ill-conditioned curvature comparison is required.

## 7. Proof boundary

- The Taylor estimates are elementary and uniform.
- The effective constants in (11) must be instantiated from the explicit `F` formula in a production certificate.
- Bounded curvature distortion does not prove the transport reserve or the centered-mass square bound.
- The cofinal arithmetic sign remains open.
