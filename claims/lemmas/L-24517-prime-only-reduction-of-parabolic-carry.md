# L-24517 — The parabolic carry route reduces to ordinary primes

Claim ID: `L-24517`  
Status: `PROPOSED — complete elementary reduction`  
Scope: prime-power elimination  
Issue: #245

Put

\[
S_X=\sum_{p^a\le X}\frac{\log p}{p^{a/2}}\log\frac{X}{p^a}
\]

and let its ordinary-prime part be

\[
P_X=\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp.
\tag{L-24517.1}
\]

Then

\[
\boxed{S_X=P_X+O(\log^2X).}
\tag{L-24517.2}
\]

Moreover, for the parabolic seed `b_X^(0)` of `L-24502`, define

\[
J_{\mathbb P,X}(b)
=\sum_{p\le X}(\log p)v_p(b).
\tag{L-24517.3}
\]

Then

\[
\boxed{
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
}
\tag{L-24517.4}
\]

Consequently it is enough to repair the ordinary-prime constraints

\[
v_p(b)\le p^{-1/2}\log(X/p).
\tag{L-24517.5}
\]

No higher prime-power constraint is required for the final RH deduction.

## 1. The target higher-power tail

The square contribution is

\[
\sum_{p\le\sqrt X}\frac{\log p}{p}
\log\frac{X}{p^2}.
\]

Using the elementary Chebyshev consequence

\[
\sum_{p\le y}\frac{\log p}{p}=O(\log y),
\]

this is `O(log^2 X)`. For `a>=3`,

\[
\begin{aligned}
\sum_{a\ge3}\sum_{p^a\le X}
\frac{\log p}{p^{a/2}}\log\frac{X}{p^a}
&\le
\log X\sum_p\frac{\log p\,p^{-3/2}}{1-p^{-1/2}}\\
&=O(\log X),
\end{aligned}
\]

because the last prime sum converges. This proves (L-24517.2).

## 2. Uniform seed bound on one divisor-gradient row

Extend the seed to real `1<=x<=X` by

\[
b_X(x)=\sqrt X B(x/X),
\qquad
B(t)=2\sqrt t\,[\log(1/t)-2(1-\sqrt t)].
\]

Let

\[
g_X(x)=-b_X'(x).
\]

For `q<=X`, except for the harmless terminal equality `kq=X`,

\[
b_X(kq)-b_X(kq+1)
=\int_{kq}^{kq+1}g_X(x)dx.
\]

Compare each unit interval with the average over its containing block of length
`q`. The difference of the two averages is at most the variation of `g_X` on
that block. Summing the blocks gives

\[
\left|
v_q(b_X^{(0)})-\frac1q\int_q^Xg_X(x)dx
\right|
\le \operatorname{Var}_{[q,X]}(g_X)
+2\sup_{q\le x\le X}|g_X(x)|.
\tag{L-24517.6}
\]

Since `b_X(X)=0`,

\[
\frac1q\int_q^Xg_X(x)dx=\frac{b_X(q)}q.
\]

The exact derivatives

\[
B'(t)=4-\frac{\log t+4}{\sqrt t},
\qquad
B''(t)=t^{-3/2}\left(1+\frac12\log t\right)
\]

give, with `L=log(X/q)`,

\[
\left|\frac{b_X(q)}q\right|
\le\frac{2L+4}{\sqrt q},
\]

\[
\operatorname{Var}_{[q,X]}(g_X)
\le\frac{L+2}{\sqrt q},
\]

and

\[
\sup_{q\le x\le X}|g_X(x)|
\le\frac{L+8}{\sqrt q}.
\]

Therefore

\[
\boxed{
|v_q(b_X^{(0)})|
\le\frac{5\log(X/q)+22}{\sqrt q}
\le\frac{27(1+\log(X/q))}{\sqrt q}.
}
\tag{L-24517.7}
\]

This estimate uses no prime information.

## 3. The seed higher-power tail

From (L-24517.7),

\[
\begin{aligned}
\left|
J_X(b_X^{(0)})-J_{\mathbb P,X}(b_X^{(0)})
\right|
&\le
27\sum_{a\ge2}\sum_{p^a\le X}
\frac{\log p}{p^{a/2}}
\left(1+\log\frac{X}{p^a}\right)\\
&=O(\log^2X)
\end{aligned}
\tag{L-24517.8}
\]

by the same square/higher-power split as in section 1. Combining this with the
seed objective of `L-24502` proves (L-24517.4).

## 4. Prime-only certificate

For every real `b`,

\[
J_{\mathbb P,X}(b)=\sum_{p\le X}(\log p)v_p(b).
\]

Hence if

\[
v_p(b)\le p^{-1/2}\log(X/p)
\quad(p\le X)
\]

and

\[
J_{\mathbb P,X}(b)\ge4\sqrt X-O(\log^2X),
\]

then

\[
P_X\ge4\sqrt X-O(\log^2X).
\]

Equation (L-24517.2) gives the same bound for `S_X`, and the existing
square-screw/Landau consumer yields RH.

## 5. Structural simplification

After this reduction:

1. proper prime powers no longer participate in the transport graph;
2. the only consecutive ordinary primes are `2` and `3`;
3. every other harmful edge is an ordinary-prime affine equation
   `ad-bp=+-1`;
4. the fixed-ratio edge sieve of `L-24515` loses its `O(sqrt X)` proper-power
   term.

Thus the remaining signed transport theorem is a prime--prime problem, not a
full prime-power cluster problem.

## Dependency boundary

The only imported estimate is the elementary Chebyshev bound
`sum_(p<=y) log p/p=O(log y)`. No zero-free region or RH input is used.

## Status boundary

This lemma removes all higher prime powers at polylogarithmic cost. It does not
prove the remaining ordinary-prime signed transport theorem.
