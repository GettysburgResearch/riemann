# R-100130 — Positive floor kernels cancel the reciprocal-zeta detector

Claim ID: `R-100130`  
Status: **PROVED EXACT ALGEBRAIC/ANALYTIC REFUTATION**  
Created: 2026-08-20  
RH status: **not assumed**

Let `q_1,...,q_J>=0` and

\[
K_Q(x)=\sum_{j=1}^J q_j\left\lfloor {x\over j}\right\rfloor.
\]

Consider the Möbius transform proposed in the positive-kernel route

\[
A_N=\sum_{m\le N}\mu(m)K_Q(N/m).
\]

Then for every integer `N>=1`, finite divisor switching gives

\[
\begin{aligned}
A_N
&=\sum_{j,m,r:\,jmr\le N}q_j\mu(m)\\
&=\sum_{n\le N}\sum_{j\mid n}q_j
   \sum_{m\mid n/j}\mu(m)\\
&=\boxed{\sum_{j\le N}q_j}.
\end{aligned}
\tag{R-100130.1}
\]

Thus the positivity is genuine but tautological: Möbius inversion has removed
the complete divisor-counting zeta factor.

The Mellin calculation says the same thing. For `Re s>1`,

\[
\int_1^\infty\left\lfloor{x\over j}\right\rfloor x^{-s-1}dx
={j^{-s}\zeta(s)\over s}.
\]

Therefore

\[
\widehat K_Q(s)={\zeta(s)\over s}\sum_jq_jj^{-s},
\]

and multiplication by the Möbius Dirichlet series `1/zeta(s)` gives

\[
\boxed{
\int_1^\infty A(x)x^{-s-1}dx
={1\over s}\sum_jq_jj^{-s}.
}
\tag{R-100130.2}
\]

There is no reciprocal-zeta pole left. Consequently coefficient positivity of
this floor-kernel transform cannot imply RH, regardless of any additional
finite polynomial divisibility imposed on `Q`.

This is a statement-to-use correction to the T-100120 positive-kernel route.
It does not affect the canonical minimal-wavelet route, whose multiplier
retains `1/zeta(s+1/2)`.