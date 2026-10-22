# L-27901 — Global square-root rigidity of Cycle Debt duals

Claim ID: `L-27901`  
Title: Every global balanced capacity dual is a linear function minus one subadditive component of the explicit square-root capacity defect  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-27205`; elementary dyadic telescoping  
Scope: global feasible duals and pointwise limits of finite dual certificates; this lemma does not control endpoint escape

## 1. Balanced defects

Fix `0<eta<=1/3`. For a real function `F` on the positive integers and an
`eta`-balanced split

\[
 n=j+(n-j),\qquad \eta n\le j\le(1-\eta)n,
\]

write

\[
 \delta_F(n,j)=F(n)-F(j)-F(n-j).
\tag{L-27901.1}
\]

The first statement is independent of the carry capacity.

## 2. Dyadic rigidity theorem

Assume that, for one constant `C>=0`,

\[
 \boxed{0\le\delta_F(n,j)\le C\sqrt n}
\tag{L-27901.2}
\]

on every `eta`-balanced split. Then there is a real number `a` such that

\[
 \boxed{
 0\le an-F(n)\le C(\sqrt2+1)\sqrt n
 \qquad(n\ge1).}
\tag{L-27901.3}
\]

### Proof

The central split is admissible. Hence

\[
 0\le F(2n)-2F(n)\le C\sqrt{2n}.
\tag{L-27901.4}
\]

For fixed `n`, the sequence

\[
 A_k(n)=2^{-k}F(2^kn)
\tag{L-27901.5}
\]

is increasing, and

\[
 0\le A_{k+1}(n)-A_k(n)
 \le C\sqrt n\,2^{-(k+1)/2}.
\tag{L-27901.6}
\]

It therefore has a finite limit `L(n)`, with

\[
 0\le L(n)-F(n)
 \le C\sqrt n\sum_{k\ge0}2^{-(k+1)/2}
 =C(\sqrt2+1)\sqrt n.
\tag{L-27901.7}
\]

Scale any admissible split by `2^k`, divide its defect by `2^k`, and let
`k` tend to infinity. The upper bound in (L-27901.2) tends to zero and gives

\[
 L(n)=L(j)+L(n-j).
\tag{L-27901.8}
\]

Because `eta<=1/3`, the floor/ceiling split is admissible for every `n>=2`.
Induction in (L-27901.8) gives

\[
 L(n)=nL(1).
\tag{L-27901.9}
\]

Taking `a=L(1)` in (L-27901.7) proves (L-27901.3).

## 3. The explicit carry-capacity potential

Define

\[
 \mathcal G(n)=\sum_{q=2}^{n}\frac1{\sqrt q}
 \left\lfloor\frac nq\right\rfloor.
\tag{L-27901.10}
\]

Its balanced split defect is exactly the capacity of `L-27205`:

\[
 \boxed{
 \delta_{\mathcal G}(n,j)
 =\omega_{n,j}
 =\sum_{q=2}^{n}\frac{\chi_{n,j}(q)}{\sqrt q}.}
\tag{L-27901.11}
\]

Put

\[
 A=\sum_{q=2}^{\infty}q^{-3/2}=\zeta(3/2)-1
\tag{L-27901.12}
\]

and

\[
 \boxed{D_{\mathcal G}(n)=An-\mathcal G(n).}
\tag{L-27901.13}
\]

Then

\[
\begin{aligned}
D_{\mathcal G}(n)
={}&\sum_{q=2}^{n}\frac{\{n/q\}}{\sqrt q}
+n\sum_{q>n}q^{-3/2},
\end{aligned}
\tag{L-27901.14}
\]

so in particular

\[
 \boxed{0\le D_{\mathcal G}(n)\le4\sqrt n.}
\tag{L-27901.15}
\]

The first sum is at most `sum_(q<=n)q^(-1/2)<=2sqrt(n)` and the second is at
most `n integral_n^infinity x^(-3/2)dx=2sqrt(n)`.

## 4. Exact interval structure of a global Cycle Debt dual

Let `F` be normalized by `F(1)=0` and suppose

\[
 \boxed{0\le\delta_F(n,j)\le\omega_{n,j}}
\tag{L-27901.16}
\]

on every balanced split. Equivalently, both `F` and `mathcal G-F` are balanced
superadditive.

Central splitting and induction show

\[
 0\le F(n)\le\mathcal G(n).
\tag{L-27901.17}
\]

Apply the dyadic theorem to `F` and to `mathcal G-F`. There are slopes `a` and
`A-a` and nonnegative functions

\[
 D_F(n)=an-F(n),
\qquad
 D_H(n)=(A-a)n-[\mathcal G(n)-F(n)]
\tag{L-27901.18}
\]

such that

\[
 \boxed{D_F+D_H=D_{\mathcal G}.}
\tag{L-27901.19}
\]

Moreover their balanced subadditive defects are

\[
 D_F(j)+D_F(n-j)-D_F(n)=\delta_F(n,j),
\tag{L-27901.20}
\]

\[
 D_H(j)+D_H(n-j)-D_H(n)=\omega_{n,j}-\delta_F(n,j).
\tag{L-27901.21}
\]

Consequently

\[
 \boxed{
 0\le D_F(n)\le D_{\mathcal G}(n)\le4\sqrt n,}
\tag{L-27901.22}
\]

and both `D_F` and `D_mathcalG-D_F` are balanced subadditive.

Thus a global dual is not an arbitrary superadditive potential. Modulo its
invisible linear part, it is exactly one subadditive component of the fixed
capacity defect `D_mathcalG`.

## 5. Pairing with a size-zero target

Let `r` be any finitely supported node divergence satisfying

\[
 \sum_n n r(n)=0.
\tag{L-27901.23}
\]

Then the linear slope disappears and

\[
 \boxed{
 -\sum_n r(n)F(n)=\sum_n r(n)D_F(n).}
\tag{L-27901.24}
\]

For the Möbius divergence of `L-26205`, every global Cycle Debt obstruction is
therefore a correlation with a defect satisfying (L-27901.22), not a generic
high-dimensional potential.

## 6. Compactness consequence

For finite dual certificates on endpoints `X_j -> infinity`, normalize
`F_j(1)=0`. Equation (L-27901.17) gives coordinatewise compactness. Every
pointwise convergent subsequence has a global limit satisfying
(L-27901.16)--(L-27901.22).

Hence a cofinal obstruction has only two possible locations:

1. a genuine global square-root defect `D_F` inside `D_mathcalG`; or
2. mass which escapes with the moving endpoint and is invisible to every fixed
   coordinate limit.

The second alternative is the weighted shell-tail phenomenon isolated on PR
#276. This lemma does not bound it.

## 7. Proof boundary

Proved here:

- global dyadic linearization with an explicit square-root error;
- the exact capacity defect `D_mathcalG`;
- the interval decomposition `D_F + D_H = D_mathcalG`;
- elimination of the linear mode against every size-zero divergence;
- pointwise compactness of normalized finite duals.

Not proved here:

- Dyadic Commutator Debt;
- exclusion of endpoint escape;
- Cycle Debt;
- WSTS;
- RH.
