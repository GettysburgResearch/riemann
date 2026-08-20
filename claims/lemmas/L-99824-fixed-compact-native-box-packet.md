# L-99824 — A fixed compact native box packet with uniformly bounded diagonal

Claim ID: `L-99824`  
Status: **PROVED EXACT COMPACTIFICATION THEOREM**  
Created: 2026-08-20  
Depends on: `L-99820`; PR #658 `L-99703`  
RH status: **not assumed**

Let

\[
B(X)=(\mathcal S_{67}h)(X)
     =\sum_{n\le X}\frac{\beta(n)}{\sqrt n}W(X/n),
\qquad
\phi(y)=\frac{W(y)}{\sqrt y}.
\]

Thus

\[
\frac{B(X)}{\sqrt X}
 =\sum_{n\le X}\frac{\beta(n)}n\phi(X/n).
\tag{L-99824.1}
\]

Define the normalized scale filter

\[
\mathcal C=(I-S_2)\left(I-\frac12S_4\right),
\qquad
(S_a f)(y)=f(y/a),
\tag{L-99824.2}
\]

and put

\[
K(y)=(\mathcal C\phi)(y),
\qquad
\widetilde K(y)=\sqrt y\,K(y).
\tag{L-99824.3}
\]

Then

\[
\boxed{
\widetilde K(y)
 =W(y)-\sqrt2\,W(y/2)-W(y/4)+\sqrt2\,W(y/8).
}
\tag{L-99824.4}
\]

## 1. Exact fixed support

For `y>=67`, the normalized box potential has the two-mode form

\[
\phi(y)=A-By^{-1/2},
\qquad
A=8(1-67^{-1/2}),\quad B=3\log67.
\]

The first factor in (L-99824.2) kills the constant mode and the second factor
kills the `y^{-1/2}` mode:

\[
(1-1)\,A=0,
\qquad
\left(1-\frac12\sqrt4\right)y^{-1/2}=0.
\]

If `y>=8*67=536`, every argument in (L-99824.4) lies in the deep formula.
Consequently

\[
\boxed{K(y)=\widetilde K(y)=0\qquad(y\ge536).}
\tag{L-99824.5}
\]

Both kernels are zero below one and are continuous at the lower and upper
activation boundaries. Hence their support is contained in the fixed annulus

\[
\boxed{1\le y\le536.}
\tag{L-99824.6}
\]

## 2. Critical source and zero-safe Mellin multiplier

Define the unnormalized compact density

\[
G(X)
 =B(X)-\sqrt2\,B(X/2)-B(X/4)+\sqrt2\,B(X/8).
\tag{L-99824.7}
\]

Finite source substitution gives

\[
\boxed{
G(X)=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}\,
\widetilde K(X/n).
}
\tag{L-99824.8}
\]

Its Mellin transform is the transform of `h` multiplied by

\[
\boxed{
\frac{1-67^{-s}}s
(1-\sqrt2\,2^{-s})(1-4^{-s}).
}
\tag{L-99824.9}
\]

The three additional factors have zeros only on `Re(s)=0` or
`Re(s)=1/2`. Therefore none cancels a reciprocal-zeta pole with

\[
0<\Re(s)<\frac12.
\]

Subpower logarithmic negative mass for `G` is consequently sufficient for RH
by the specialized Landau theorem of PR #653.

## 3. Uniform diagonal bound

For fixed `X`, let

\[
d_X(n)=\frac{\beta(n)}{\sqrt n}\widetilde K(X/n).
\tag{L-99824.10}
\]

By (L-99824.6),

\[
d_X(n)\ne0
\quad\Longrightarrow\quad
\frac{X}{536}\le n\le X.
\tag{L-99824.11}
\]

Since `|\beta(n)|<=2` and `\widetilde K` is bounded on its compact support,

\[
\begin{aligned}
\sum_n|d_X(n)|^2
&\le4\|\widetilde K\|_\infty^2
 \sum_{X/536\le n\le X}\frac1n\\
&\le4\|\widetilde K\|_\infty^2(1+\log536).
\end{aligned}
\tag{L-99824.12}
\]

Thus

\[
\boxed{\sup_X\sum_n|d_X(n)|^2<\infty.}
\tag{L-99824.13}
\]

The fixed compactification removes every forward, inverse, and support-growth
cost from the diagonal. It does not estimate the signed off-diagonal shell
tails.
