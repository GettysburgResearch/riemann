# L-99815 — Four-regime proof of global active weighted pair positivity

Claim ID: `L-99815`  
Status: **PROVED EXACT FINITE-REGIME THEOREM**  
Created: 2026-08-20  
Depends on: `L-99813`; PR #658 `L-99703`  
RH status: **not assumed**

For an active pair `67<=p<q` and `y>=pq`, the four arguments

```text
y,
y/p,
y/q,
y/(pq)
```

can occupy only the following activation patterns relative to the box kernel's three regions `0` (`<1`), `1` (`[1,67)`), and `2` (`>=67`):

```text
(2,2,1,0),
(2,2,2,0),
(2,2,2,1),
(2,2,2,2).
```

No other pattern is compatible with `y>=pq`, `p<q`, and `p,q>=67`.

Let

\[
\mathcal B_{p,q}\Phi(y)
=\Phi(y)-p^{-1/2}\Phi(y/p)-q^{-1/2}\Phi(y/q)+(pq)^{-1/2}\Phi(y/(pq)).
\]

`L-99813` proves positivity in the last two patterns. The first two are also strictly positive.

## Pattern `(2,2,2,0)`

Here `y,y/p,y/q>=67` and `y/(pq)<1`. With

\[
\Phi(t)=A-Bt^{-1/2},\quad A=8(1-67^{-1/2}),\quad B=3\log67,
\]

one obtains

\[
\mathcal B_{p,q}\Phi(y)
=A(1-p^{-1/2}-q^{-1/2})+B\,y^{-1/2}.
\]

Since `p>=67`, `q>=71`, and `A>0`,

\[
1-p^{-1/2}-q^{-1/2}>1-67^{-1/2}-71^{-1/2}>0.75,
\]

so the block is positive.

## Pattern `(2,2,1,0)`

Write `u=y/q`. Then `1<=u<67`, while `qu=y>=67` and `(q/p)u=y/p>=67`; moreover `u/p=y/(pq)<1`. Exact substitution gives

\[
\mathcal B_{p,q}\Phi(qu)
=A(1-p^{-1/2})
-q^{-1/2}\Phi(u)
+\frac{B}{\sqrt{qu}}\left(1-\sqrt p\,p^{-1/2}\right).
\]

The half-order tail cancels in the `p`-difference, leaving simply

\[
\mathcal B_{p,q}\Phi(qu)
=A(1-p^{-1/2})-q^{-1/2}\Phi(u).
\]

Because `0<=Phi(u)<A` and `q^{-1/2}<1`,

\[
\mathcal B_{p,q}\Phi(qu)
>A\left(1-p^{-1/2}-q^{-1/2}\right)>0.
\]

Therefore

\[
\boxed{\mathcal B_{p,q}\Phi(y)>0\qquad(y>=pq)}
\]

for every rough prime pair. The proof uses only the four possible activation regimes and elementary inequalities.

The remaining many-prime question is compositional: whether successive pair operators preserve a cone on which the next pair remains positive. This theorem does not assume that closure.
