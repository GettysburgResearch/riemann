# L-27902 — Uniform dyadic-shell floor error and reduction to two bounded crossing gates

Claim ID: `L-27902`  
Title: Dyadic subtraction removes the logarithmic floor-error growth, so finite shell sign failure is confined to one bounded transition collar and finitely many low coordinates  
Status: **PROPOSED COMPLETE REDUCTION — FINITE GATES REMAIN TO BE CERTIFIED COFINALLY**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Dependencies: `L-27901`; PR #240 `L-23825`  
Scope: exact finite-to-continuum shell reduction; it does not prove finite one-crossing, WSTS, or RH

## 1. The exact shell seed

Retain

\[
B(u)=2\sqrt u[\log(1/u)-2(1-\sqrt u)],
\qquad 0<u\le1,
\]

and

\[
b_X(m)=\sqrt X\,B(m/X),
\qquad 2\le m\le X.
\]

Let

\[
Y=\lfloor X/2\rfloor,
\qquad c=Y/X.
\]

With zero extension above each endpoint, define the complete shell seed

\[
\Sigma_{X,Y}(m)=b_X(m)-b_Y(m).
\tag{L-27902.1}
\]

Put

\[
\boxed{
B_c(u)
=B(u)-\sqrt c\,B(u/c)\mathbf1_{u\le c}.}
\tag{L-27902.2}
\]

Then exactly

\[
\boxed{
\Sigma_{X,Y}(m)=\sqrt X\,B_c(m/X).}
\tag{L-27902.3}
\]

For `u<=c`, the two logarithmic singularities cancel:

\[
\boxed{
B_c(u)
=2\sqrt u\log(1/c)
+4u(1-c^{-1/2}).}
\tag{L-27902.4}
\]

This cancellation is the reason the shell floor error is better than the error of either endpoint separately.

## 2. Uniform shell derivative bound

Let

\[
g_c(u)=-B_c'(u).
\]

For `u<c`, (L-27902.4) gives

\[
g_c(u)
=-{\log(1/c)\over\sqrt u}
+4(c^{-1/2}-1),
\]

and

\[
|g_c'(u)|
={\log(1/c)\over2u^{3/2}}.
\tag{L-27902.5}
\]

For `u>c`, `B_c=B`, so

\[
|g_c'(u)|
\le C u^{-3/2}[1+\log(1/u)].
\]

But `u>=c`, and for the dyadic floor ratio

\[
1/3\le c\le1/2.
\]

Therefore one absolute constant satisfies

\[
\boxed{
|g_c'(u)|\le C_0u^{-3/2}
\qquad(0<u<1),}
\tag{L-27902.6}
\]

uniformly for every integer dyadic shell. The formulas join continuously at `u=c`, because `B(1)=B'(1)=0`.

## 3. Exact shell response and improved floor error

For an integer `q>=2`, the shell divisor-gradient response is

\[
v_q(\Sigma_{X,Y})
=\sum_{kq\le X}
 [\Sigma_{X,Y}(kq)-\Sigma_{X,Y}(kq+1)].
\]

By (L-27902.3),

\[
\Sigma_{X,Y}(kq)-\Sigma_{X,Y}(kq+1)
=X^{-1/2}\int_0^1
 g_c((kq+t)/X)\,dt.
\tag{L-27902.7}
\]

The mean-value estimate and (L-27902.6) give

\[
\left|
 v_q(\Sigma_{X,Y})
-X^{-1/2}\sum_{kq\le X}g_c(kq/X)
\right|
\le
C_1q^{-3/2}
\sum_{k\ge1}k^{-3/2}.
\]

Thus

\[
\boxed{
\left|
 v_q(\Sigma_{X,Y})
-X^{-1/2}F_c(q/X)
\right|
\le C q^{-3/2},}
\tag{L-27902.8}
\]

where

\[
F_c(\theta)=\sum_{k\le1/\theta}g_c(k\theta).
\]

Unlike the single-endpoint estimate in `L-23825`, there is no factor `1+log(X/q)`.

## 4. The target shell and exact defect formula

The target response is

\[
w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X}.
\]

Its shell difference is

\[
w_X(q)-\mathbf1_{q\le Y}w_Y(q)
=X^{-1/2}h_c(q/X),
\tag{L-27902.9}
\]

where

\[
h_c(\theta)
=\theta^{-1/2}\log(1/c)\mathbf1_{\theta\le c}
+\theta^{-1/2}\log(1/\theta)\mathbf1_{\theta>c}.
\]

The continuum shell defect is

\[
E_c(\theta)=F_c(\theta)-h_c(\theta).
\]

It is exactly the fixed-ratio defect of `L-23823`:

\[
E_c(\theta)
=E(\theta)-c^{-1/2}E(\theta/c)\mathbf1_{\theta\le c}.
\tag{L-27902.10}
\]

For the finite shell residual

\[
s_{X,Y}(q)
=r_X(q)-\mathbf1_{q\le Y}r_Y(q),
\]

we therefore have the sharpened uniform formula

\[
\boxed{
 s_{X,Y}(q)
=X^{-1/2}E_c(q/X)+\varepsilon_{X,Y}(q),
\qquad
|\varepsilon_{X,Y}(q)|\le Cq^{-3/2}.}
\tag{L-27902.11}
\]

This is an exact source-specific improvement over the logarithmic error budget used in the first WSTS consolidation.

## 5. Stability of the one-crossing interface

For `Y=floor(X/2)`,

\[
|c-1/2|\le {1\over2X}.
\]

The cell formula in `L-27901` and the explicit dependence on `c` imply that the unique continuum root moves by `O(1/X)`. Since the root `theta_*` of the exact half shell is simple, there are absolute constants `C_2,X_0` such that every finite residual with

\[
|q-\theta_*X|>C_2
\tag{L-27902.12}
\]

and `q` in a fixed-ratio neighborhood of the crossing has the continuum sign.

The quantitative lower-sector estimate in `L-27901`, combined with (L-27902.11), similarly gives constants `q_0,X_1` such that

\[
\boxed{
q_0\le q\le\theta_*X-C_2
\quad\Longrightarrow\quad
s_{X,Y}(q)>0,}
\tag{L-27902.13}
\]

and

\[
\boxed{
q\ge\theta_*X+C_2
\quad\Longrightarrow\quad
s_{X,Y}(q)<0}
\tag{L-27902.14}
\]

for every `X>=X_1`.

Thus a cofinal proof of finite one-crossing no longer requires control of an `X`-sized sign table. It requires only:

1. a fixed finite set of low coordinates `2<=q<q_0`;
2. a bounded-width moving collar around `q=theta_*X`.

Both retain exact floor arithmetic and are suitable for symbolic or interval certification.

## 6. The finite shell-crossing theorem

Define **FSCR** to be the statement that, for every sufficiently large `X`, there is an integer `q_*(X)` such that

\[
\boxed{
s_{X,\lfloor X/2\rfloor}(q)\ge0\quad(q\le q_*(X)),
\qquad
s_{X,\lfloor X/2\rfloor}(q)\le0\quad(q>q_*(X)).}
\tag{FSCR}
\]

Equations (L-27902.13)--(L-27902.14) reduce `FSCR` to the two bounded gates above. This file does not certify those gates for all `X`.

The discovery replay checks them through `X=10^7`, with no sign-order violation and crossing ratio converging to `theta_*`. That evidence is explicitly non-cofinal.

## 7. Proof boundary

Closed here, subject to review:

- exact shell-profile cancellation;
- uniform `O(q^-3/2)` floor error;
- exact finite defect formula;
- reduction of finite sign failure to a bounded transition collar and finitely many low coordinates.

Open:

- cofinal certification of the two bounded gates;
- `FSCR` itself;
- the total weighted shell sign;
- WSTS or RH.
