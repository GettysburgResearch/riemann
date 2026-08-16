# L-95180 — The scale-four reciprocal has a positive coefficient-one channel swap

Claim ID: `L-95180`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95050` at `d2984600a848aca04f27b46bda86bd92229a4a0b`; the scale-four source dictionary on PR #474  
Scope: multiplicative two-channel source dynamics; no centered Q4 curvature or RH conclusion

## 1. Reciprocal pair

Put

\[
A_4(s)={1-4^{1-s}\over(1-4^{-s})\zeta(s)},
\qquad
G_4(s)={1\over A_4(s)}
=\zeta(s){1-4^{-s}\over1-4^{1-s}}.
\]

Write

\[
G_4(s)=\sum_{n\ge1}{g_4(n)\over n^s},
\qquad
A_4(s)=\sum_{n\ge1}{a_4(n)\over n^s}.
\]

For `n=2^e m`, `m` odd,

\[
\boxed{g_4(n)=4^{\lfloor e/2\rfloor}>0.}
\tag{L-95180.1}
\]

If `m` is odd squarefree, then

\[
a_4(2^e m)=
\begin{cases}
\mu(m),&e=0,\\
-\mu(m),&e=1,\\
3(-1)^{e+1}\mu(m),&e\ge2,
\end{cases}
\tag{L-95180.2}
\]

and `a_4(n)=0` otherwise. Hence

\[
\boxed{|a_4(n)|\le g_4(n).}
\tag{L-95180.3}
\]

Define

\[
\boxed{u_4^\pm(n)=g_4(n)\pm a_4(n)\ge0.}
\tag{L-95180.4}
\]

## 2. Nonnegative generalized primes

Let

\[
-{G_4'(s)\over G_4(s)}
=\sum_{n\ge2}{\Lambda_4(n)\over n^s}.
\]

Then

\[
\Lambda_4(p^r)=\log p\quad(p\text{ odd}),
\tag{L-95180.5}
\]

and

\[
\Lambda_4(2^r)=
\begin{cases}
\log2,&r\text{ odd},\\
(2^{r+1}-1)\log2,&r\text{ even}.
\end{cases}
\tag{L-95180.6}
\]

Thus `Lambda_4>=0`.

## 3. Exact channel swap

Coefficient comparison in

\[
-G_4'=\left(-{G_4'\over G_4}\right)G_4,
\qquad
-A_4'=-\left(-{G_4'\over G_4}\right)A_4
\]

gives

\[
g_4(n)\log n
=\sum_{d\mid n,d>1}\Lambda_4(d)g_4(n/d),
\tag{L-95180.7}
\]

\[
a_4(n)\log n
=-\sum_{d\mid n,d>1}\Lambda_4(d)a_4(n/d).
\tag{L-95180.8}
\]

Therefore

\[
\boxed{
u_4^+(n)\log n
=\sum_{d\mid n,d>1}\Lambda_4(d)u_4^-(n/d),
}
\tag{L-95180.9}
\]

\[
\boxed{
u_4^-(n)\log n
=\sum_{d\mid n,d>1}\Lambda_4(d)u_4^+(n/d).
}
\tag{L-95180.10}
\]

This is a positive descending divisor Markov compiler. Every coefficient is used once; the sign is carried by the channel label rather than by a signed physical weight.

## 4. Matrix form

The coefficient matrix

\[
\Sigma_4(n)=
\begin{pmatrix}
g_4(n)&a_4(n)\\a_4(n)&g_4(n)
\end{pmatrix}
\]

is PSD, with eigenvalues `u_4^+(n)` and `u_4^-(n)`. The signed reciprocal state is its off-diagonal channel.

## 5. Boundary

```text
positive reciprocal g_4                   EXACT
signed inverse a_4 and |a_4|<=g_4          EXACT
nonnegative generalized-prime source       EXACT
positive coefficient-one channel swap      EXACT
centered additive/Q4 extraction            OPEN
Riemann Hypothesis                         UNPROVED
```
