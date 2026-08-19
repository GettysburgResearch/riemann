# L-99271 — The factor-67 SHARP defect has a positive inverse renewal and an exact logarithmic owner martingale

Claim ID: `L-99271`  
Status: **PROVED EXACT SOURCE IDENTITY**  
Created: 2026-08-20  
Depends on: the scalar definitions in `L-99270`  
RH status: **unproved**

Define

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\tag{L-99271.1}
\]

Then

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\tag{L-99271.2}
\]

For `Re(z)>1`,

\[
B(z):=\sum_{n\ge1}\frac{\beta(n)}{n^z}
=\frac{1-67^{-z}}{\zeta(z)}.
\tag{L-99271.3}
\]

Put

\[
g(n)=v_{67}(n)+1.
\tag{L-99271.4}
\]

Its Dirichlet series is positive coefficientwise and satisfies

\[
G(z):=\sum_{n\ge1}\frac{g(n)}{n^z}
=\frac{\zeta(z)}{1-67^{-z}}.
\tag{L-99271.5}
\]

Therefore `B(z)G(z)=1`, so finite Dirichlet convolution gives

\[
\boxed{\beta*g=\varepsilon.}
\tag{L-99271.6}
\]

## 1. Positive inverse renewal

Substitute (L-99271.2), change variables `m=dn`, and use (L-99271.6).  Every
sum is finite at fixed `x`.  One obtains

\[
\boxed{
T(x)=\sum_{d\le x}\frac{g(d)}{\sqrt d}\,h(x/d).
}
\tag{L-99271.7}
\]

All renewal weights are positive.  This is the exact positive inverse of the
local-square Möbius source; it is not an unsigned bound on (L-99271.2).

At a point where `h(x)<0`, write `h=h_+-h_-` in (L-99271.7).  The `d=1`
term gives the exact overshoot identity

\[
\boxed{
h_-(x)
+\sum_{2\le d\le x}\frac{g(d)}{\sqrt d}h_-(x/d)
=
\sum_{2\le d\le x}\frac{g(d)}{\sqrt d}h_+(x/d)-T(x).
}
\tag{L-99271.8}
\]

Thus every negative current must be paid by a strict, source-specific positive
renewal overshoot at smaller arguments.  No absolute-value large sieve appears.

## 2. Exact logarithmic owner

Define the generalized von Mangoldt weight

\[
\Lambda_g(q)=
\begin{cases}
2\log67,&q=67^a,\ a\ge1,\\
\log p,&q=p^a,\ p\ne67,\ a\ge1,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-99271.9}
\]

The logarithmic derivative of (L-99271.5) is

\[
-\frac{G'(z)}{G(z)}
=\sum_{q\ge1}\frac{\Lambda_g(q)}{q^z}.
\tag{L-99271.10}
\]

Comparing coefficients in `-G'=(-G'/G)G` gives

\[
\boxed{
g(n)\log n
=\sum_{q\mid n}\Lambda_g(q)g(n/q)
\qquad(n\ge2).}
\tag{L-99271.11}
\]

Hence

\[
\boxed{
\mathbb P_n(q)
=\frac{\Lambda_g(q)g(n/q)}{g(n)\log n},
\qquad q\mid n,
}
\tag{L-99271.12}
\]

is a probability distribution.  It assigns every positive inverse-renewal
source atom to one prime-power logarithmic owner.

## 3. New source-faithful frontier

Equations (L-99271.8) and (L-99271.12) prescribe a narrower arithmetic target
than pointwise positivity:

> Prove that the logarithmic-owner charge of renewal overshoots has subpower
> total negative mass on multiplicative blocks.

By `L-99270`, that estimate alone implies RH.  It permits local negative
histories and retains the exact prime-power owner, the duplicated 67 factor,
and the sign of the live scalar.

```text
positive inverse renewal                 PROVED EXACT
negative-current overshoot identity       PROVED EXACT
logarithmic owner probabilities           PROVED EXACT
subpower owner-Carleson estimate           OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```
