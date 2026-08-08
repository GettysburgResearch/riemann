# L-26204 — Affine boundary lift dominates the Green–Skorokhod debt

Claim ID: `L-26204`  
Title: The canonical maximum Green displacement gives an explicit sharp nonnegative carry certificate and controls the one-sided Skorokhod debt  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Issue: #260  
Dependencies: `L-26202`, `L-26203`; PR #271 `L-26701/L-26702`; Bertrand's postulate  
Scope: exact finite comparison of two canonical carry certificates; no cofinal estimate or RH conclusion

## 1. Setting

Fix an integer endpoint `X>=2`. Let

\[
b^{(0)}=(b^{(0)}_2,\ldots,b^{(0)}_X)\ge0
\]

be any benchmark and let

\[
b^\star=(b^★_2,\ldots,b^★_X)
\]

be a signed exact equality state for the prime-power carry target:

\[
v_q^{(X)}(b^★)=w_X(q)
\qquad(q=p^a\le X).
\tag{L-26204.1}
\]

The canonical application is the endpoint-projected Green state of
`L-26203`. Define its downward displacement from the benchmark by

\[
 u_m=b^{(0)}_m-b^★_m
 \qquad(2\le m\le X)
\tag{L-26204.2}
\]

and put

\[
\boxed{
 C_X^G=\max_{2\le m\le X}(u_m)_+.
}
\tag{L-26204.3}
\]

For the Green potential `F_X` of `L-26203`,

\[
 u_m=F_X(m)-F_X(m-1),
\]

so `C_X^G` is exactly the largest positive Green edge.

Let

\[
\mathcal P_X
 =\sum_{q=p^a\le X}\Lambda(q)w_X(q),
\qquad
J_X(b)=\sum_{m=2}^Xb_m\log\frac m{m-1}.
\tag{L-26204.4}
\]

Exact equality gives

\[
J_X(b^★)=\mathcal P_X.
\tag{L-26204.5}
\]

## 2. One affine block gives an explicit nonnegative certificate

Choose a prime

\[
X<Y<2X
\tag{L-26204.6}
\]

by Bertrand's postulate. Extend `b^star` by zero to `X<m<=Y` and define

\[
\widetilde b_m=
\begin{cases}
 b^★_m+C_X^G,&2\le m\le X,\\
 C_X^G,&X<m\le Y.
\end{cases}
\tag{L-26204.7}
\]

By definition of `C_X^G`,

\[
\widetilde b_m\ge b^{(0)}_m\ge0
\quad(2\le m\le X),
\qquad
\widetilde b_m\ge0
\quad(X<m\le Y).
\tag{L-26204.8}
\]

The constant oversupport block has response

\[
v_q^{(Y)}(\mathbf1_{2\le m\le Y})=\mathbf1_{q\mid Y}.
\]

Because `Y` is prime and exceeds `X`, it creates no charge in an old
prime-power row. Hence

\[
v_q^{(Y)}(\widetilde b)=w_X(q)
\qquad(q=p^a\le X).
\tag{L-26204.9}
\]

Its only new response is the boundary charge

\[
v_Y^{(Y)}(\widetilde b)=C_X^G.
\tag{L-26204.10}
\]

The objective telescopes exactly:

\[
J_Y(\widetilde b)
 =\mathcal P_X+C_X^G\log Y.
\tag{L-26204.11}
\]

On the other hand, (L-26204.8) gives

\[
J_Y(\widetilde b)
 \ge J_X(b^{(0)})+C_X^G\log(Y/X).
\]

Subtracting the common oversupport term yields the source-bound estimate

\[
\boxed{
 \mathcal P_X
 \ge J_X(b^{(0)})-C_X^G\log X.
}
\tag{L-26204.12}
\]

Thus a subpower bound for one positive Green edge is already a complete sharp
carry minorant; physical nonnegativity needs no iterative deformation.

## 3. Comparison with the least affine charge

Let `mathcal C_X` be the least boundary charge of PR #271 `L-26702`. Since the
canonical Green equality state is one admissible signed state,

\[
\boxed{
 \mathcal C_X\le C_X^G.
}
\tag{L-26204.13}
\]

The logarithmic/von-Mangoldt dual ray gives the converse scalar firewall

\[
\boxed{
 \mathcal C_X
 \ge
 \left[
 {J_X(b^{(0)})-\mathcal P_X\over\log X}
 \right]_+.
}
\tag{L-26204.14}
\]

Consequently no proof may bound `mathcal C_X` or `C_X^G` by deleting the
logarithmic ray. That ray is the prime-ramp discrepancy itself.

## 4. The prefix Skorokhod certificate is controlled by the same edge

Define the physical negative excursion

\[
a_m=(-b^★_m)_+.
\tag{L-26204.15}
\]

Since `b^(0)_m>=0` and `b^star_m=b^(0)_m-u_m`,

\[
0\le a_m=(u_m-b^{(0)}_m)_+\le(u_m)_+\le C_X^G.
\tag{L-26204.16}
\]

Let

\[
\sigma_m=\max_{2\le k\le m}a_k,
\qquad
\lambda_j=\sigma_j-\sigma_{j-1}\ge0
\]

be the prefix Skorokhod regulator of `L-26202`. Then

\[
\sum_j\lambda_j=\max_ma_m\le C_X^G.
\tag{L-26204.17}
\]

The exact prefix contact debt satisfies

\[
\mathcal P_X-\mathcal L_X^\downarrow
 =\sum_{j=2}^X
  \lambda_j\log{j-1\over\gcd(j-1,X)}
 \le C_X^G\log X.
\tag{L-26204.18}
\]

Equation (L-26204.12) also gives

\[
J_X(b^{(0)})-\mathcal P_X\le C_X^G\log X.
\tag{L-26204.19}
\]

Adding (L-26204.18)--(L-26204.19) yields

\[
\boxed{
 J_X(b^{(0)})-\mathcal L_X^\downarrow
 \le2C_X^G\log X.
}
\tag{L-26204.20}
\]

Thus the affine and prefix-Skorokhod completions are not competing asymptotic
hinges. The affine charge is the sharper scalar; a bound for it automatically
produces a reviewable one-sided Skorokhod certificate.

## 5. Consequence for the parabolic seed

For the parabolic benchmark of `L-26203`,

\[
J_X(b^{(0)})\ge4\sqrt X-O(\log X).
\]

Either of

\[
 C_X^G=X^{o(1)}
 \qquad\text{or}\qquad
 \mathcal C_X=X^{o(1)}
\tag{L-26204.21}
\]

therefore gives

\[
\mathcal P_X\ge4\sqrt X-X^{o(1)},
\]

and the imported square-screw/Landau transfer yields RH.

The implication is complete; the estimates in (L-26204.21) are not proved in
this file.

## 6. Review boundary

Closed exactly:

- one-prime affine completion of the canonical Green equality state;
- the objective inequality (L-26204.12);
- domination of the least affine charge;
- domination of the prefix Skorokhod debt;
- the factor-two comparison (L-26204.20).

Open:

- a cofinal subpower bound for `mathcal C_X` or `C_X^G`;
- the prime-ramp asymptotic;
- RH.
