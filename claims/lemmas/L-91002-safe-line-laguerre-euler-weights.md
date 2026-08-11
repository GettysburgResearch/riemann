# L-91002 — Safe-line Hausdorff differences are Laguerre filters of first-Hermite heat

Claim ID: `L-91002`  
Status: **EXACT SOURCE-SIDE TRANSFORM IDENTITY**  
Created: 2026-08-11  
Depends on: `L-90905`, `L-90906`, and `L-91001`  
RH status: **unproved**

## 1. One-line Euler polynomials

Let `P_k(t)` be the one-safe-line Euler polynomial of `L-90905`, so that the prime part of the normalized scalar `a_k` is

\[
 -\Re\sum_{n\ge2}
 \frac{\Lambda(n)}{n^{3/2+ix}}
 \frac{P_k(\log n)}{(k+2)!}.
\]

For `k,m>=0`, define the beta Euler polynomial

\[
\boxed{
 \Pi_{k,m}(t)
 =\sum_{j=0}^m(-1)^j\binom mj
 \frac{P_{k+j}(t)}{(k+j+2)!}.
}
\tag{L-91002.1}
\]

Then `D_(k,m)` is still evaluated on the single safe line `Re(s)=3/2`; its prime part is obtained by replacing `P_k/(k+2)!` with `Pi_(k,m)`.

## 2. Gamma-Bessel representation

`L-90906` gives

\[
 e^{-t}P_j(t)
 =\frac1{\sqrt\pi}\int_0^\infty
 q^{j+1/2}e^{-q-t^2/(4q)}
 \left(1-\frac{t^2}{2q}\right)dq.
\tag{L-91002.2}
\]

Substituting into (L-91002.1), interchanging the finite sum and integral, and using

\[
\begin{aligned}
\sum_{j=0}^m(-1)^j\binom mj
 \frac{q^j}{(k+j+2)!}
&=\frac1{(k+2)!}
 {}_1F_1(-m;k+3;q)\\
&=\frac{m!}{(k+m+2)!}
 L_m^{(k+2)}(q),
\end{aligned}
\tag{L-91002.3}
\]

one obtains

\[
\boxed{
\begin{aligned}
 e^{-t}\Pi_{k,m}(t)
 ={}&\frac{m!}{\sqrt\pi\,(k+m+2)!}
 \int_0^\infty
 q^{k+1/2}e^{-q-t^2/(4q)}\\
 &\qquad\cdot L_m^{(k+2)}(q)
 \left(1-\frac{t^2}{2q}\right)dq.
\end{aligned}}
\tag{L-91002.4}
\]

Thus discrete Hausdorff differentiation in the safe-line order is exactly generalized-Laguerre filtering in first-Hermite heat time.

## 3. Interpretation

The three live terminal descriptions are now one transform chain:

```text
first-Hermite heat q
 -> Gamma moments in q
 -> integer safe-line order k
 -> Hausdorff finite differences in k
 -> generalized Laguerre filters in q.
```

The zero side is positive under RH because the beta kernel is

\[
 \lambda^k(1-\lambda)^m,
 \qquad 0\le\lambda\le1.
\]

The prime side is one absolutely convergent Euler series with weight `Pi_(k,m)(log n)` plus the same finite rational/polygamma combination. Equation (L-91002.4) supplies the exact source-side basis for a future sum-of-squares, variation-diminishing, or total-positivity proof.

It does not itself prove the RH-equivalent sign.