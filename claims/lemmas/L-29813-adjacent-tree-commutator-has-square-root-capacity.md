# L-29813 — Adjacent-tree commutators have square-root negative capacity

Claim ID: `L-29813`  
Title: The negative carry-capacity debt of the canonical reverse adjacent dipole is bounded by an explicit constant times the square root of its source level  
Status: **PROPOSED COMPLETE EXACT/ANALYTIC LEMMA**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: PR #272 `L-27207`; elementary carry-capacity bound  
Scope: one canonical adjacent-tree commutator; no source summation or RH conclusion

## 1. Commutator and debt

Let

\[
 E_n=T_{n+1}-T_n
\]

be the canonical adjacent-tree commutator of `L-27207`, and let

\[
 \mathcal C(n)=\mathcal N_\omega(E_n)
 =\sum_e\omega_e[-E_n(e)]_+.
\tag{L-29813.1}
\]

Here

\[
 \omega_{N,j}=\sum_{q=2}^{N}{\chi_{N,j}(q)\over\sqrt q}.
\]

The elementary estimate

\[
 \boxed{\omega_{N,j}\le2\sqrt N}
\tag{L-29813.2}
\]

holds for every split.

## 2. Sparse recursion

`L-27207` gives

\[
 E_{2m}=[2m+1,m]-[2m,m]+E_m,
\tag{L-29813.3}
\]

\[
 E_{2m+1}=[2m+2,m+1]-[2m+1,m]+E_m.
\tag{L-29813.4}
\]

For `m>=2`, the two new parent levels exceed every parent in `E_m`; no new
edge overlaps the recursive support.  Hence

\[
 \mathcal C(2m)
 =\omega_{2m,m}+\mathcal C(m),
\tag{L-29813.5}
\]

\[
 \mathcal C(2m+1)
 =\omega_{2m+1,m}+\mathcal C(m).
\tag{L-29813.6}
\]

The exceptional initial values are

\[
 \mathcal C(1)=\mathcal C(2)=0,
 \qquad
 \mathcal C(3)=\omega_{3,1},
\]

because `- [2,1]+E_1=0` in `E_2`.

In particular, without using equality at the exceptional level,

\[
 \mathcal C(n)
 \le2\sqrt n+\mathcal C(\lfloor n/2\rfloor).
\tag{L-29813.7}
\]

## 3. Explicit square-root bound

Iterating (L-29813.7),

\[
\begin{aligned}
\mathcal C(n)
&\le2\sqrt n\sum_{h\ge0}2^{-h/2}\\
&=2(2+\sqrt2)\sqrt n.
\end{aligned}
\]

Thus

\[
 \boxed{
 \mathcal N_\omega(E_n)
 \le(4+2\sqrt2)\sqrt n.}
\tag{L-29813.8}
\]

The logarithmic support size of `E_n` does not produce a logarithmic capacity
loss, because the parent scales decrease geometrically.

## 4. Scaled reverse source

A reverse adjacent source coefficient `t>=0` is realized canonically by `tE_n`.
Its negative capacity debt obeys

\[
 \boxed{
 \mathcal N_\omega(tE_n)
 \le(4+2\sqrt2)t\sqrt n.}
\tag{L-29813.9}
\]

This is the correct local price for the right-to-left orientations which cannot
be nonnegative by `R-29805`.

## 5. Proof boundary

Proved here:

- exact debt recursion outside the finite base case;
- an explicit uniform square-root bound;
- absence of a logarithmic commutator penalty.

Not proved here:

- summability over the complete Euler boundary bank;
- cancellation with the lower-flow odd leakage;
- DCD;
- RH.
