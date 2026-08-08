# L-23704 — Möbius-adjoint collapse of the carry inverse

Claim ID: `L-23704`  
Title: Möbius transformation turns every carry row into one affine tail kernel, and Carry Saturation is exactly discrete convexity of an explicit adjoint sequence  
Status: **PROPOSED EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Dependencies: `L-23701`; elementary Möbius inversion  
Scope: every finite target vector; no RH input

## 1. Exact row collapse

For `2<=m<=n`, put

\[
\mathcal K(n,m)
=
\sum_{k\le n/m}\mu(k)\beta_{n,mk}.
\tag{L-23704.1}
\]

The carry count has the floor representation

\[
(n+1)\beta_{nq}
=
(n+1)\left\lfloor\frac nq\right\rfloor
-2\sum_{j=0}^n\left\lfloor\frac jq\right\rfloor.
\tag{L-23704.2}
\]

Use the elementary identity

\[
\sum_{k\le y}\mu(k)\left\lfloor\frac yk\right\rfloor
=1
\qquad(y\ge1).
\tag{L-23704.3}
\]

The first term of the Möbius sum in (L-23704.2) contributes `n+1`. For fixed
`j`, the inner Möbius sum in the second term equals one exactly when `j>=m` and
zero otherwise. Hence it contributes `2(n-m+1)`. Therefore

\[
\boxed{
\mathcal K(n,m)
=
\frac{2m-n-1}{n+1}.}
\tag{L-23704.4}
\]

The complicated floor matrix has become one affine kernel.

## 2. Adjoint transform of an arbitrary target

Let `w(q)` be any finite target on `2<=q<=X`, and let `c(n)` be its unique
upper-triangular carry inverse:

\[
w(q)=\sum_{n=q}^Xc(n)\beta_{nq}.
\tag{L-23704.5}
\]

Define the multiples-Möbius transform

\[
\boxed{
 u_m
 =
 \sum_{k\le X/m}\mu(k)w(mk),
 \qquad2\le m\le X,}
\tag{L-23704.6}
\]

and put `u_(X+1)=u_(X+2)=0`. Interchanging the finite sums and using
(L-23704.4) gives

\[
\boxed{
 u_m
 =
 \sum_{n=m}^X
 c(n)\frac{2m-n-1}{n+1}.}
\tag{L-23704.7}
\]

Thus the carry inverse is equivalent to a triangular affine-tail transform.

## 3. Exact inverse formula

For `2<=j<=X`, define

\[
U_j=\sum_{m=j}^Xu_m,
\qquad
A_j=\frac{U_j}{j-1},
\tag{L-23704.8}
\]

with `A_(X+1)=A_(X+2)=0` under the zero extension.

Then

\[
\boxed{
 c(j)
 =
 \frac{
 (j+1)\bigl[j u_j-(j-2)u_{j+1}\bigr]
 +2\sum_{m=j+2}^Xu_m
 }{j(j-1)}.}
\tag{L-23704.9}
\]

Equivalently,

\[
\boxed{
 c(j)
 =(j+1)\bigl(A_j-2A_{j+1}+A_{j+2}\bigr).}
\tag{L-23704.10}
\]

### Verification

Substitute (L-23704.7) into the numerator of (L-23704.9). The coefficient of
`c(j)` is `j(j-1)`. The coefficient of `c(j+1)` is zero. For every `n>=j+2`,
the first two terms contribute

\[
\frac{2(j+1)(j-n+1)}{n+1},
\]

while the tail contributes its negative because

\[
\sum_{m=j+2}^n(2m-n-1)
=(j+1)(n-j-1).
\]

All off-diagonal coefficients vanish, proving (L-23704.9). Rewriting with
`u_j=U_j-U_(j+1)` gives (L-23704.10).

## 4. Exact convexity criterion

Equation (L-23704.10) proves

\[
\boxed{
 c(j)\ge0\text{ for every }j
 \quad\Longleftrightarrow\quad
 A_j-2A_{j+1}+A_{j+2}\ge0\text{ for every }j.}
\tag{L-23704.11}
\]

Thus full Carry Saturation for a target is exactly discrete convexity of one
explicit Möbius-adjoint sequence.

For the prime-ramp target

\[
w_X(q)=q^{-1/2}\log(X/q),
\]

one has

\[
\boxed{
 u_m
 =
 \frac1{\sqrt m}
 \sum_{k\le X/m}
 \frac{\mu(k)}{\sqrt k}
 \log\frac{X/m}{k}.}
\tag{L-23704.12}
\]

The reciprocal-zeta channel is therefore visible, but only through the second
difference of its normalized cumulative adjoint.

## 5. Exact relation to the greedy blockers

Suppose the exact inverse coefficients are nonnegative. After the greedy
algorithm has removed rows `X,X-1,...,n+1`, its residual is

\[
\rho_X^{(n)}(q)
=
\sum_{m=q}^nc(m)\beta_{mq}.
\tag{L-23704.13}
\]

For the diagonal constraint,

\[
\frac{\rho_X^{(n)}(n)}{\beta_{nn}}=c(n).
\]

For every other active `q`,

\[
\frac{\rho_X^{(n)}(q)}{\beta_{nq}}
=
c(n)
+
\frac{\sum_{m=q}^{n-1}c(m)\beta_{mq}}{\beta_{nq}}
\ge c(n).
\tag{L-23704.14}
\]

Therefore the diagonal is a minimizer at every stage, and the greedy vector
equals the exact inverse.

Conversely, if the greedy algorithm chooses the diagonal at every stage, it
solves every triangular row with equality and produces the unique inverse with
nonnegative coefficients. Hence

\[
\boxed{
\text{all greedy blockers are diagonal}
\quad\Longleftrightarrow\quad
\text{Carry Saturation}
\quad\Longleftrightarrow\quad
(A_j)\text{ is discretely convex}.}
\tag{L-23704.15}
\]

## 6. Consequence for the full proposal

DBT does not require (L-23704.11). It remains valid even if some blockers are
off diagonal. The exact collapse nevertheless gives two sharper possible
closures:

1. prove discrete convexity of `A_j` and recover full Carry Saturation;
2. bound the aggregate failure of convexity and transfer it to the greedy
   blocker debt in DBT.

The second route is weaker and is the preferred fail-closed target.

## 7. Proof boundary

Closed exactly:

- the Möbius collapse of every carry row;
- the adjoint tail representation;
- the explicit inverse formula;
- the discrete-convexity criterion;
- equivalence of diagonal greedy blocking and Carry Saturation.

Open:

- convexity for the logarithmic prime-ramp target;
- aggregate control of its convexity defects;
- DBT;
- RH.