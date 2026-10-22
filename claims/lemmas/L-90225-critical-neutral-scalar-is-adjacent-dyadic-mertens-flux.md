# L-90225 — The critical-neutral scalar is one adjacent-dyadic Mertens flux

Claim ID: `L-90225`  
Status: **PROPOSED COMPLETE EXACT FLUX LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: `T-90206` three-source identity; elementary partial summation  
Scope: exact compression of the remaining arithmetic sign; no bound for the flux and no RH conclusion

## 1. Multiples state

Let

\[
 h_X(q)=\left(q^{-1/2}-X^{-1/2}\right)\mathbf1_{2\le q\le X},
\]

with `h_X(1)=0`, and put

\[
 U_X(m)=\sum_{k\le X/m}\mu(k)h_X(mk).
\]

Write

\[
 M(x)=\sum_{n\le x}\mu(n),
 \qquad
 I(x)=\int_1^x M(t)t^{-3/2}\,dt,
\]

with `I(x)=0` for `x<=1`.

## 2. Exact state formula, including the unit correction

For `m>=2`, partial summation gives

\[
 \sum_{k\le y}\frac{\mu(k)}{\sqrt k}
 =\frac{M(y)}{\sqrt y}+\frac12I(y).
\]

With `y=X/m`, the two `M(y)` terms cancel, yielding

\[
\boxed{
 U_X(m)=\frac1{2\sqrt m}I(X/m)
 \qquad(m\ge2).
}
\tag{L-90225.1}
\]

At `m=1`, the formal hinge has the nonzero unit value `1-X^{-1/2}`, while
the target declares that coordinate zero. Therefore

\[
\boxed{
 U_X(1)=\frac12I(X)-\left(1-X^{-1/2}\right).
}
\tag{L-90225.2}
\]

This unit correction is load-bearing.

## 3. Three-source identity

For

\[
 b_\star=(\varepsilon-(1+\sqrt2)\delta_2+\sqrt2\delta_4)*\mu,
\]

define

\[
 \mathcal K_\star(X)
 =-\sum_{2\le q\le X}b_\star(q)
  (q^{-1/2}-X^{-1/2}).
\]

Finite switching gives

\[
\boxed{
 \mathcal K_\star(X)
 =(1+\sqrt2)U_X(2)-U_X(1)-\sqrt2U_X(4).
}
\tag{L-90225.3}
\]

Equivalently,

\[
 \sqrt2\,\mathcal K_\star(X)
 =2(U_X(2)-U_X(4))
 -\sqrt2(U_X(1)-U_X(2)).
\]

## 4. Adjacent-dyadic flux identity

Substituting (L-90225.1)--(L-90225.2) into (L-90225.3) gives

\[
\begin{aligned}
\mathcal K_\star(X)
={}&1-X^{-1/2}
 +\frac{1+\sqrt2}{2\sqrt2}I(X/2)\\
&-\frac1{2\sqrt2}I(X/4)-\frac12I(X).
\end{aligned}
\]

Now

\[
\begin{aligned}
&\int_{X/4}^{X/2}[M(t)-M(2t)]t^{-3/2}\,dt\\
&\qquad=(1+\sqrt2)I(X/2)-I(X/4)-\sqrt2 I(X).
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal K_\star(X)
=1-X^{-1/2}
+\frac1{2\sqrt2}
 \int_{X/4}^{X/2}
 \frac{M(t)-M(2t)}{t^{3/2}}\,dt.
}
\tag{L-90225.4}
\]

This holds for every real `X>=4`, with the standard right-continuous Mertens
prefix.

## 5. Shell form

Because

\[
 M(t)-M(2t)=-\sum_{t<n\le2t}\mu(n),
\]

one also has

\[
\boxed{
\mathcal K_\star(X)
=1-X^{-1/2}
-\frac1{2\sqrt2}
 \int_{X/4}^{X/2}t^{-3/2}
 \sum_{t<n\le2t}\mu(n)\,dt.
}
\tag{L-90225.5}
\]

Thus every policy, Pascal, and finite-filter layer has disappeared. The live
arithmetic theorem is the constant one-sided shell estimate

\[
\boxed{
 \int_{X/4}^{X/2}
 \frac{M(t)-M(2t)}{t^{3/2}}\,dt
 \ge-2\sqrt2(1-X^{-1/2}).
}
\tag{L-90225.6}
\]

## 6. Relationship to the odd annulus

Switching the finite integral in (L-90225.5) over the integers `n` recovers
exactly the compact odd-annulus kernel of `L-90223`. Therefore the following
are identical coordinates:

```text
three multiples states U_X(1),U_X(2),U_X(4);
odd squarefree annulus [X/8,X];
adjacent-dyadic Mertens flux [X/4,X/2].
```

## 7. Proof boundary

Proved exactly:

- the partial-summation state formula;
- the exceptional unit correction;
- the three-source identity;
- the adjacent-dyadic flux formula;
- equivalence with the compact odd-annulus coordinate.

Not proved:

- the one-sided flux bound (L-90225.6);
- eventual sign of `K_star`;
- RH.
