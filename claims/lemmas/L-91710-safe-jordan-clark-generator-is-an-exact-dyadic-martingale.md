# L-91710 — The safe Jordan–Clark generator is an exact dyadic martingale

Claim ID: `L-91710`  
Status: **PROVED EXACT SAFE-SOURCE COCYCLE AND POSITIVE DYADIC INNOVATIONS**  
Created: 2026-08-13  
Depends on: `L-91323/L-91324`, `L-91610`  
RH status: **unproved**

## 1. Safe normalized Jordan channel

For `a>0`, `Re s>1`, put

\[
Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}
\]

and, for a safe vertical line `sigma>1`,

\[
M_{a,\sigma}(t)
=\frac{Q_a(\sigma+it)}{Q_a(\sigma)}.
\]

The anchor is `M_(a,sigma)(0)=1`. Since the safe Euler product is zero free,
the anchored analytic logarithm

\[
\boxed{\ell_{a,\sigma}(t)=-\log M_{a,\sigma}(t)}
\tag{L-91710.1}
\]

is unambiguous.

Expanding the Euler logarithm gives

\[
\boxed{
\ell_{a,\sigma}(t)
=
\sum_{p}\sum_{r\ge1}
\frac{p^{-r\sigma}(1-p^{-2ar})}{r}
\left(1-e^{-irt\log p}\right).
}
\tag{L-91710.2}
\]

Therefore `Re ell_(a,sigma)(t)>=0`; it is a compound-Poisson/Clark
positive-real generator.

## 2. Exact coefficient-one cocycle

The generalized-Jordan quotient obeys

\[
Q_{a+b}(s)=Q_a(s)Q_b(s+2a).
\]

The anchor factors with the same coefficient, hence

\[
\boxed{
M_{a+b,\sigma}(t)
=
M_{a,\sigma}(t)
M_{b,\sigma+2a}(t)
}
\tag{L-91710.3}
\]

and, because all logarithms vanish at `t=0`,

\[
\boxed{
\ell_{a+b,\sigma}
=
\ell_{a,\sigma}
+
\ell_{b,\sigma+2a}.
}
\tag{L-91710.4}
\]

No branch multiple of `2 pi i` is possible.

## 3. Dyadic innovation

Put `b_j=2^j a`. Then

\[
\boxed{
\ell_{b_{j+1},\sigma}
-
\ell_{b_j,\sigma}
=
\ell_{b_j,\sigma+2b_j}.
}
\tag{L-91710.5}
\]

The `j`-th innovation has the explicit positive atomic measure

\[
\boxed{
d\nu_{j;a,\sigma}(u)
=
\sum_{p}\sum_{r\ge1}
\frac{
p^{-r(\sigma+2b_j)}
(1-p^{-2b_jr})
}{r}
\delta_{r\log p}(du).
}
\tag{L-91710.6}
\]

Indeed

\[
\ell_{b_j,\sigma+2b_j}(t)
=
\int_0^\infty
(1-e^{-itu})\,d\nu_{j;a,\sigma}(u).
\tag{L-91710.7}
\]

Thus every dyadic innovation is positive real and its polarized Clark kernel

\[
\boxed{
\begin{aligned}
\mathscr D_j(t,u)
={}&
\ell_{b_j,\sigma+2b_j}(t)
+\overline{\ell_{b_j,\sigma+2b_j}(u)}\\
&-
\ell_{b_j,\sigma+2b_j}(t-u)
\end{aligned}
}
\tag{L-91710.8}
\]

is positive semidefinite.

## 4. Base-section expansion

Iterating the cocycle gives the exact decomposition

\[
\boxed{
\ell_{2^J a,\sigma}
=
\sum_{k=0}^{2^J-1}
\ell_{a,\sigma+2ka}.
}
\tag{L-91710.9}
\]

Equivalently, successive dyadic differences are the positive generators in
(L-91710.5).

As `J->infinity`,

\[
Q_{2^J a}(s)\longrightarrow\zeta(s)
\]

locally uniformly on `Re s>1`, and therefore

\[
\boxed{
-\log\frac{\zeta(\sigma+it)}{\zeta(\sigma)}
=
\sum_{k\ge0}
\ell_{a,\sigma+2ka}(t).
}
\tag{L-91710.10}
\]

The safe zeta Clark generator is an all-generation sum of positive
coefficient-one innovations.

## 5. Atomic-isolation geometry

At a prime-power atom `u_0`, a carrier satisfying `t u_0 in 2 pi Z` has

\[
1-e^{-itu_0}=0.
\]

That atom emits no innovation detail. Its amplitude remains in the returned
Euler state and is passed to the next radial section. Hence Fejer isolation is
absorbed by the martingale rather than compared against a continuous measure.

## 6. Relation to the annular route

`L-91520/L-91620` put the crossed-zero obstruction into an additive dyadic
entropy telescope. Equations (L-91710.5)--(L-91710.10) put the arithmetic prime
source into the same dyadic additive coordinate.

The remaining issue is not additivity. It is generation-by-generation
source-to-model identification.

## 7. Exact boundary

```text
safe Jordan logarithm                           EXACT POSITIVE REAL
coefficient-one scale cocycle                   EXACT
dyadic prime innovation measures                EXPLICIT POSITIVE
full carrier innovation kernels                 EXACT PSD
all-generation safe-zeta decomposition          EXACT
generationwise annular source identification    OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
