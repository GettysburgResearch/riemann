# L-23015 — Exact dyadic Green path factorization

Claim ID: `L-23015`  
Title: The power-of-two sector of the endpoint-projected divisor Green matrix is an explicit weighted path Gram with a tridiagonal inverse  
Status: **PROPOSED COMPLETE EXACT FINITE ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Frozen parent: PR #236 at `1c9a749a1648c4772509eb3b056598c7044f4393`  
Dependencies: PR #248 `L-24509`; elementary finite differences  
Scope: exact dyadic component of the canonical carry correction

## 1. Green matrix at a dyadic endpoint

Fix `N>=1`, put

\[
X=2^N,
\qquad
q_a=2^a,
\quad1\le a\le N.
\]

Use the endpoint-projected divisor columns

\[
f_q(j)=\mathbf1_{q\mid j}-\frac jX\mathbf1_{q\mid X},
\qquad0\le j\le X,
\]

with `f_q(0)=0`, and the Dirichlet Gram

\[
G_X(q,d)
=
\sum_{j=0}^{X-1}
\Delta f_q(j)\Delta f_d(j).
\]

Then the power-of-two principal block satisfies

\[
\boxed{
G_X(2^a,2^b)
=
2^{N-\max(a,b)+1}-1-2^{-N}.
}
\tag{L-23015.1}

## 2. Proof of the entry formula

For `q|X`,

\[
\Delta f_q(j)
=
\mathbf1_{q\mid j+1}-\mathbf1_{q\mid j}-\frac1X,
\]

where the value at `j=0` uses `f_q(0)=0`. If `a<=b`, direct counting of the
simultaneous positive and negative jumps gives

\[
\sum_{j=0}^{X-1}
(\mathbf1_{2^a\mid j+1}-\mathbf1_{2^a\mid j})
(\mathbf1_{2^b\mid j+1}-\mathbf1_{2^b\mid j})
=
\frac{X}{2^{b-1}}-1.
\]

Both jump sequences have total sum one. Endpoint projection therefore subtracts
`1/X`, proving (L-23015.1).

## 3. Cumulative-square factorization

Define

\[
d_a=
\begin{cases}
2^{N-a},&1\le a<N,\\
1-2^{-N},&a=N.
\end{cases}
\tag{L-23015.2}
\]

For a real vector `t=(t_1,...,t_N)`, put

\[
S_a=\sum_{j=1}^a t_j.
\]

Since

\[
G_X(2^a,2^b)
=
\sum_{r=\max(a,b)}^N d_r,
\]

one obtains the exact path factorization

\[
\boxed{
 t^TG_X^{(2)}t
 =
 \sum_{a=1}^N d_a S_a^2.
}
\tag{L-23015.3}

Thus the entire dyadic correction is one positive weighted carry path. No
asymptotic argument or zeta input occurs.

## 4. Explicit inverse

Let `D=diag(d_1,...,d_N)` and let `L` be the lower-triangular matrix with
`L_(a,j)=1_(j<=a)`. Then

\[
G_X^{(2)}=L^TDL.
\]

Consequently

\[
\boxed{
(G_X^{(2)})^{-1}
=L^{-1}D^{-1}(L^{-1})^T,
}
\tag{L-23015.4}

which is tridiagonal. Explicitly,

\[
\begin{aligned}
(G^{-1})_{1,1}&=d_1^{-1},\\
(G^{-1})_{a,a}&=d_{a-1}^{-1}+d_a^{-1}\quad(2\le a\le N),\\
(G^{-1})_{a,a+1}&=(G^{-1})_{a+1,a}=-d_a^{-1},\\
(G^{-1})_{a,b}&=0\quad(|a-b|>1).
\end{aligned}
\tag{L-23015.5}

The inverse is an exact path M-matrix.

## 5. Carry interpretation

For a dyadic residual vector `r=(r_1,...,r_N)`, the canonical equality correction
in this sector is

\[
T^{(2)}=(G_X^{(2)})^{-1}r.
\]

Its energy is

\[
\boxed{
 r^T(G_X^{(2)})^{-1}r
 =
 \sum_{a=1}^{N-1}\frac{(r_a-r_{a+1})^2}{d_a}
 +\frac{r_N^2}{d_N}.
}
\tag{L-23015.6}

The dyadic sector is therefore completely coercive. Any remaining obstruction
in the full Green correction lies in its Schur complement against odd and mixed
prime-power coordinates.

## 6. Proof boundary

Closed exactly:

- every dyadic Green entry;
- the cumulative-square factorization;
- the tridiagonal inverse;
- the exact dyadic correction energy.

Not closed:

- a subpower estimate for the full odd/mixed Schur complement;
- positivity-preserving deformation of the complete correction;
- RH.
