# L-99700 — Generalized von Mangoldt functions form a positive graded owner Gram

Claim ID: `L-99700`  
Status: **PROVED EXACT ANALYTIC/ALGEBRAIC THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

For an integer `k>=0`, put
\[
\ell_k(n)=(\log n)^k,\qquad
\Lambda_k=\mu*\ell_k.
\tag{L-99700.1}
\]

## 1. Exact box formula and positivity

Write
\[
n=\prod_{i=1}^r p_i^{e_i},\qquad
a_i=\log p_i,\qquad L=\log n.
\]
Only squarefree divisors contribute to the Möbius convolution, hence
\[
\Lambda_k(n)
 =\sum_{S\subseteq\{1,\ldots,r\}}
 (-1)^{|S|}
 \left(L-\sum_{i\in S}a_i\right)^k.
\tag{L-99700.2}
\]
If `k<r`, this is zero.  If `k>=r`, repeated use of
\[
f(x)-f(x-a)=\int_0^a f'(x-t)\,dt
\]
gives
\[
\boxed{
\Lambda_k(n)
 =(k)_r
 \int_0^{a_1}\!\cdots\!\int_0^{a_r}
 \left(L-t_1-\cdots-t_r\right)^{k-r}
 dt_1\cdots dt_r ,
}
\tag{L-99700.3}
\]
where `(k)_r=k!/(k-r)!`.  The integrand is nonnegative because
\[
L-\sum_i t_i\ge L-\sum_i a_i
 =\sum_i(e_i-1)a_i\ge0.
\]
Therefore
\[
\boxed{\Lambda_k(n)\ge0\quad(n\ge1,\ k\ge0).}
\tag{L-99700.4}
\]

For squarefree `n` with exactly `r` prime factors,
\[
\boxed{\Lambda_r(n)=r!\prod_{p\mid n}\log p.}
\tag{L-99700.5}
\]

## 2. Positive exponential generating function

Summing (L-99700.2) gives
\[
\boxed{
\sum_{k\ge0}\Lambda_k(n)\frac{u^k}{k!}
 =n^u\prod_{p\mid n}(1-p^{-u})
 =:J_u(n)\ge0
 \qquad(u\ge0).
}
\tag{L-99700.6}
\]
Thus the generalized Jordan function is the exponential generating function
of the complete positive owner hierarchy.

## 3. Graded Gram blocks

For fixed `n` and grade `r`, define
\[
M^{(n,r)}_{ij}
 =\frac{\Lambda_{i+j+r}(n)}{(i+j+r)_r},
 \qquad i,j\ge0,
\tag{L-99700.7}
\]
when `n` has exactly `r` distinct prime factors.  By (L-99700.3),
\[
M^{(n,r)}_{ij}
 =\int_{[0,a_1]\times\cdots\times[0,a_r]}
 x(t)^{i+j}\,dt,
\quad
x(t)=L-\sum_\nu t_\nu\ge0.
\]
Hence every finite principal block is a Gram matrix:
\[
\boxed{M^{(n,r)}\succeq0.}
\tag{L-99700.8}
\]

## 4. The 5:3 row completion

Let `q` be the primitive 5:3 source of `L-99261` and put `a=q*1`.
Its coefficients are
\[
a(1)=0,\qquad a(2)=15,\qquad a(4)=3,\qquad
a(n)=6\quad(n\notin\{1,2,4\}).
\tag{L-99700.9}
\]
They are all nonnegative.  Since `1*\mu=\varepsilon`,
\[
\boxed{
q*\ell_k=(q*1)*(\mu*\ell_k)=a*\Lambda_k\ge0
\quad(k\ge0).
}
\tag{L-99700.10}
\]
Equivalently,
\[
q*\operatorname{id}^{\,u}=a*J_u\ge0\qquad(u\ge0).
\tag{L-99700.11}
\]

This is an unconditional, all-order positive completion of the unsifted
5:3 source.  The duplicate-67 boundary is treated separately in `R-99700`.
