# L-99701 — The inverse-renewal sign is a minus-one owner martingale, and phase twisting supplies the first nondegenerate square

Claim ID: `L-99701`  
Status: **PROVED EXACT PROBABILISTIC/ALGEBRAIC THEOREM**  
Created: 2026-08-20  
Depends on: `L-99271`  
RH status: **not assumed**

Use the duplicate-67 reciprocal source
\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
g(n)=v_{67}(n)+1.
\tag{L-99701.1}
\]
The exact convolution identity is `beta*g=epsilon`.  Let
\[
\Lambda_g(p^a)=
 \begin{cases}
  2\log67,&p=67,\\
  \log p,&p\ne67,
 \end{cases}
\tag{L-99701.2}
\]
and zero away from prime powers.  `L-99271` proves
\[
g(n)\log n
 =\sum_{q\mid n}\Lambda_g(q)g(n/q).
\tag{L-99701.3}
\]
Therefore
\[
\mathbb P_n(q)
 =\frac{\Lambda_g(q)g(n/q)}{g(n)\log n}
\tag{L-99701.4}
\]
is a probability law on prime-power divisors `q` of `n`.

## 1. Exact minus-one eigenfunction

Differentiate the Dirichlet identity
\[
B(z)G(z)=1,
\quad
B(z)=\sum\beta(n)n^{-z},
\quad
G(z)=\sum g(n)n^{-z}.
\]
Coefficient comparison gives
\[
\boxed{
\beta(n)\log n
 =-\sum_{q\mid n}\Lambda_g(q)\beta(n/q).
}
\tag{L-99701.5}
\]
Put
\[
a(n)=\frac{\beta(n)}{g(n)}.
\tag{L-99701.6}
\]
Combining (L-99701.3) and (L-99701.5),
\[
\boxed{
\mathbb E_n[a(n/Q)]=-a(n).
}
\tag{L-99701.7}
\]

Let `N_0=n` and repeatedly divide by an owner chosen by (L-99701.4).
The chain reaches `1` in finitely many steps.  Then
\[
M_t=(-1)^t a(N_t)
\tag{L-99701.8}
\]
is a bounded martingale, and optional stopping yields
\[
\boxed{
a(n)=\mathbb E_n[(-1)^\tau].
}
\tag{L-99701.9}
\]

## 2. Exact Doob energy and the coercivity firewall

Martingale variance decomposition gives
\[
\boxed{
1-a(n)^2
 =\mathbb E_n\sum_{t<\tau}
 \operatorname{Var}\!\left(a(N_{t+1})\mid N_t\right).
}
\tag{L-99701.10}
\]
For every squarefree `n` with `v_67(n)<=1`,
\[
|a(n)|=1
\]
and every admissible owner child satisfies
\[
a(n/q)=-a(n).
\]
Consequently every variance in (L-99701.10) is zero.

Thus an untwisted variance, spectral-gap, or ordinary Doob-energy argument has
**no coercivity at all on the principal squarefree Möbius sector**.  This is a
source-level obstruction, not a weakness of a particular norm.

## 3. Phase-adaptive square

For real `gamma`, define
\[
a_\gamma(n)=a(n)n^{-i\gamma}
\]
and
\[
\boxed{
\mathcal V_\gamma(n)
 =\mathbb E_n
 \left|
 a_\gamma(n/Q)+a_\gamma(n)
 \right|^2\ge0.
}
\tag{L-99701.11}
\]
On the squarefree sector with `67` absent,
\[
\boxed{
\mathcal V_\gamma(n)
 =\sum_{p\mid n}
 \frac{\log p}{\log n}|1-p^{i\gamma}|^2.
}
\tag{L-99701.12}
\]
When `67` is present, the same formula holds with the exact doubled-67 owner
weight prescribed by (L-99701.2)--(L-99701.4).

The phase square is the first owner energy which does not vanish identically
on native squarefree histories.  A global source-weighted Carleson estimate for
this square would be genuinely phase-sensitive; it is not supplied by the
untwisted renewal algebra.
