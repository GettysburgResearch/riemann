# L-91442 — The missing Green-knot reserve is an exact sum of positive prime-influence energies

Claim ID: `L-91442`  
Status: **EXACT PRODUCT-MARTINGALE DECOMPOSITION; QUANTITATIVE LOWER BOUND OPEN**  
Created: 2026-08-12  
Depends on: `L-91022/L-91023`, `L-91402`, `R-91401`  
RH status: **unproved**

## 1. The pre-knot scalar

Fix `a>0`, put

\[
 s=2a,
 \qquad
 c_s=\zeta(1+s)^{-1},
 \qquad
 \kappa=\sqrt{275/14}.
\]

For an integer `N>=2`, define the decreasing nonnegative weight

\[
 h_{a,N}(m)
 =\left[\kappa a+4a^2\log\frac Nm\right]
  \mathbf1_{m<N}.
\tag{L-91442.1}
\]

The exact pre-knot density of `L-91402` is

\[
\boxed{
 B_a(\log N-)
 =-c_s+
  \sum_{m<N}\frac{F_s(m)}m h_{a,N}(m)
  -c_s I_{a,N},
}
\tag{L-91442.2}
\]

where

\[
 F_s(m)=\prod_{p\mid m}(1-p^{-s}),
 \qquad
 I_{a,N}=\kappa a\log N+2a^2(\log N)^2.
\tag{L-91442.3}
\]

## 2. Logarithmic-integer product model

Let `P_N={p_1,...,p_r}` be the primes not exceeding `N`. Let the independent coordinates `E_p` have geometric law

\[
 \Pr(E_p=k)=(1-p^{-1})p^{-k},
 \qquad k\ge0,
\tag{L-91442.4}
\]

and put

\[
 M=\prod_{p\le N}p^{E_p},
 \qquad
 C_N=\prod_{p\le N}(1-p^{-1}).
\tag{L-91442.5}
\]

Define

\[
 G=F_s(M),
 \qquad
 H=h_{a,N}(M).
\tag{L-91442.6}
\]

Both are coordinatewise nonincreasing. Directly from the product law,

\[
 \mathbb E G
 =P_s(N):=\prod_{p\le N}(1-p^{-1-s}),
\tag{L-91442.7}
\]

\[
 \mathbb EH
 =C_N\sum_{m<N}\frac{h_{a,N}(m)}m,
\tag{L-91442.8}
\]

and

\[
 \mathbb E[GH]
 =C_N\sum_{m<N}\frac{F_s(m)}m h_{a,N}(m).
\tag{L-91442.9}
\]

Hence the exact excess over the one-sided FKG envelope is

\[
\boxed{
 \mathcal C_{a,N}
 :=\sum_{m<N}\frac{F_s(m)}m h_{a,N}(m)
   -P_s(N)\sum_{m<N}\frac{h_{a,N}(m)}m
 =\frac{\operatorname{Cov}(G,H)}{C_N}.
}
\tag{L-91442.10}
\]

## 3. Doob influence decomposition

Reveal the prime coordinates in any fixed order and put

\[
 \mathcal F_j=\sigma(E_{p_1},...,E_{p_j}),
\]

\[
 G_j=\mathbb E[G\mid\mathcal F_j],
 \qquad
 H_j=\mathbb E[H\mid\mathcal F_j],
\]

\[
 \Delta_jG=G_j-G_{j-1},
 \qquad
 \Delta_jH=H_j-H_{j-1}.
\]

Orthogonality of martingale differences gives

\[
\boxed{
 \operatorname{Cov}(G,H)
 =\sum_{j=1}^{r}
  \mathbb E[\Delta_jG\,\Delta_jH].
}
\tag{L-91442.11}
\]

Each summand is nonnegative. Indeed, condition on `F_(j-1)` and define

\[
 g_j(k)=\mathbb E[G\mid\mathcal F_{j-1},E_{p_j}=k],
\]

\[
 h_j(k)=\mathbb E[H\mid\mathcal F_{j-1},E_{p_j}=k].
\]

Both are nonincreasing in `k`. If `pi_j` is the geometric law of `E_(p_j)`, then

\[
\boxed{
\begin{aligned}
 &\mathbb E[\Delta_jG\Delta_jH\mid\mathcal F_{j-1}]\\
 &\quad=
 \frac12\sum_{k,\ell\ge0}
  \pi_j(k)\pi_j(\ell)
  [g_j(k)-g_j(\ell)]
  [h_j(k)-h_j(\ell)]
 \ge0.
\end{aligned}}
\tag{L-91442.12}
\]

This is an exact positive prime-influence energy, not merely the qualitative Harris inequality.

## 4. Exact decomposition of the Green density

Define the explicit FKG envelope

\[
\boxed{
\begin{aligned}
 B_a^{\rm FKG}(N)
 ={}&-c_s+
 P_s(N)\sum_{m<N}\frac{h_{a,N}(m)}m
 -c_sI_{a,N}.
\end{aligned}}
\tag{L-91442.13}
\]

Equations (L-91442.2), (L-91442.10), and (L-91442.11) give

\[
\boxed{
 B_a(\log N-)
 =B_a^{\rm FKG}(N)
 +\frac1{C_N}
  \sum_{j=1}^{r}
   \mathbb E[\Delta_jG\Delta_jH].
}
\tag{L-91442.14}
\]

Every term in the second line is nonnegative.

`R-91401` proves that `B_a^FKG(N)` can remain asymptotically near `-c_s` in the small-scale middle window. Equation (L-91442.14) identifies exactly what the scalar FKG estimate discarded: the complete sum of prime-coordinate influence energies.

## 5. Relation to martingale shadows

For a two-point coordinate, the conditional term in (L-91442.12) is a positive adjacent butterfly. For a geometric coordinate it is the monotone limit of finite adjacent birth-death edge energies.

Thus the missing Green reserve has the same finite-to-continuum architecture as:

```text
factor-54 martingale butterflies;
beta-binomial/Hahn shadow chains;
Beta(2,2) Jacobi carré du champ.
```

The next legitimate theorem is a quantitative lower bound

\[
\boxed{
 \frac1{C_N}
  \sum_j\mathbb E[\Delta_jG\Delta_jH]
 \ge[-B_a^{\rm FKG}(N)]_+.
}
\tag{L-91442.15}
\]

A proof may use a block of prime influences, an exact finite Hahn compression, or a polarized Hardy square. Another one-sided FKG application cannot see this term.

## 6. Boundary

```text
pre-knot scalar                                      EXACT
product-measure representation                       EXACT
covariance excess over FKG                           EXACT
Doob prime-influence decomposition                    EXACT
positivity of every influence term                    EXACT
identification with shadow/butterfly energy           EXACT STRUCTURE
quantitative influence lower bound                    OPEN / RH-BEARING
full Green-removal density                            OPEN
Riemann Hypothesis                                    UNPROVED
```
