# L-100000 — Centered Bernstein remainders stay positive until the unique prime-harmonic step

Claim ID: `L-100000`  
Status: **PROVED UNCONDITIONAL ALL-ORDER HIERARCHY**  
Created: 2026-08-20  
Depends on: the literal duplicate-67 source; the labelled-level estimate of PR #663  
RH status: **not assumed**

Put

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
\mathcal B(z)=\sum_{n\ge1}{\beta(n)\over n^z}
={1-67^{-z}\over\zeta(z)}\quad(\Re z>1),
\]

and use the doubly clamped boundary kernel

\[
U(y)=4(\sqrt y-1)_+.
\]

For an integer `m>=3`, define

\[
H_m(x)=\sum_{n\le x}{\beta(n)\over\sqrt n}U(x/n)^m.
\tag{L-100000.1}
\]

For `r=1,...,m-1`, define centered remainders recursively by

\[
R_{m,0}=H_m,
\]

\[
\boxed{
R_{m,r}(x)
=4^m\binom m{r-1}
 \mathcal B\!\left({m-r+2\over2}\right)
 x^{(m-r+1)/2}
-R_{m,r-1}(x).
}
\tag{L-100000.2}
\]

Every coefficient in (L-100000.2) is an absolutely convergent Euler value.

## 1. Exact positive kernel

For `t>0`, let

\[
\kappa_{m,1}(t)=1-(1-t)_+^m,
\]

and

\[
\kappa_{m,r}(t)
=\binom m{r-1}t^{r-1}-\kappa_{m,r-1}(t)
\qquad(r\ge2).
\tag{L-100000.3}
\]

Then finite substitution in (L-100000.2) gives

\[
\boxed{
R_{m,r}(x)
=4^m x^{m/2}
 \sum_{n\ge1}{\beta(n)\over n^{(m+1)/2}}
 \kappa_{m,r}\!\left(\sqrt{n/x}\right).
}
\tag{L-100000.4}
\]

The sum is absolutely convergent for every `r<=m-2`.

The kernel has the two exact polynomial forms

\[
\kappa_{m,r}(t)
=\sum_{j=r}^{m}(-1)^{j-r}\binom mj t^j,
\qquad 0<t\le1,
\tag{L-100000.5}
\]

and

\[
\kappa_{m,r}(t)
=\sum_{j=0}^{r-1}(-1)^{r-1-j}\binom mj t^j,
\qquad t\ge1.
\tag{L-100000.6}
\]

Put

\[
C_{m,r}={m!\over(r-1)!(m-r)!}.
\]

Taylor remainder gives the positive integral representations

\[
\boxed{
\kappa_{m,r}(t)
=C_{m,r}t^r
 \int_0^1(1-v)^{r-1}(1-tv)^{m-r}\,dv,
\quad0<t\le1,
}
\tag{L-100000.7}
\]

and

\[
\boxed{
\kappa_{m,r}(t)
=C_{m,r}t^{r-1}
 \int_0^1(1-v)^{m-r}(1-v/t)^{r-1}\,dv,
\quad t\ge1.
}
\tag{L-100000.8}
\]

In particular,

\[
\kappa_{m,r}(t)>0.
\tag{L-100000.9}
\]

## 2. The sharp scaling inequality

The function

\[
t\longmapsto {\kappa_{m,r}(t)\over t^r}
\]

is nonincreasing on `(0,infinity)`.

On `(0,1]` this follows immediately from (L-100000.7). For `t>=1`, put
`z=1/t` and `a=m-r>=1`. Apart from the positive constant `C_(m,r)`, the
normalized function is

\[
z\int_0^1(1-v)^a(1-zv)^{r-1}\,dv.
\]

Its derivative has the positive Bernstein expansion

\[
\sum_{j=0}^{r-1}\binom{r-1}{j}
 z^j(1-z)^{r-1-j}b_j,
\tag{L-100000.10}
\]

where

\[
b_0={1\over a+1},
\qquad
b_j={a\over(a+j)(a+j+1)}>0\quad(j\ge1).
\]

Thus the expression increases with `z` and decreases with `t`.
Consequently, for every `q>=2`,

\[
\boxed{
{\kappa_{m,r}(\sqrt q\,t)\over\kappa_{m,r}(t)}
\le q^{r/2}.
}
\tag{L-100000.11}
\]

## 3. Literal labelled Euler proof

Represent `beta` by one labelled copy of every prime and a second labelled copy
of `67`. For a finite label subset `A`, put

\[
n_A=\prod_{\ell\in A}p_\ell
\]

and

\[
w_A(x)=n_A^{-(m+1)/2}
 \kappa_{m,r}(\sqrt{n_A/x})>0.
\]

Adding a fresh label `q` and using (L-100000.11) gives

\[
\boxed{
{w_{A\cup\{q\}}(x)\over w_A(x)}
\le q^{-\sigma_{m,r}},
\qquad
\sigma_{m,r}={m-r+1\over2}.
}
\tag{L-100000.12}
\]

Let `M_k` be the total weight of the `k`-label level. Double counting removals
gives

\[
kM_k\le S_{\sigma_{m,r}}M_{k-1},
\]

where

\[
S_\sigma=\sum_{p\ {\rm prime}}p^{-\sigma}+67^{-\sigma}.
\]

For `r<=m-2`,

\[
\sigma_{m,r}\ge{3\over2}
\]

and PR #663 proves by rational inequalities that

\[
S_{3/2}<1.
\]

Therefore

\[
M_{2j+1}<M_{2j}.
\]

The absolute Euler sum converges, and pairing consecutive parity levels in
(L-100000.4) proves

\[
\boxed{
R_{m,r}(x)>0
\qquad
(x>0,\ m\ge3,\ 1\le r\le m-2).
}
\tag{L-100000.13}
\]

## 4. Exact stopping point

At the next and final centering step, `r=m-1`,

\[
\sigma_{m,m-1}=1.
\]

The controlling labelled mass is then

\[
\sum_p{1\over p}+{1\over67}=\infty.
\]

Thus the proof cancels every supercritical real carrier while preserving
positivity, and stops **exactly** at the prime-harmonic boundary. No earlier
power loss or source mismatch remains.
