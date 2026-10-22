# L-90905 — The confluent terminal resolvent lives on one safe Euler line

Claim ID: `L-90905`  
Status: **PROPOSED COMPLETE EXACT TRANSFORM LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the exact safe-Euler resolvent family of PR #378; the completed logarithmic derivative  
RH status: **unproved**

## 1. Purpose

PR #378 evaluates its finite-order terminal detector at three points in
`Re(s)>1`.  In the confluent depth limit these three points coalesce.  This
note computes that limit exactly and shows that every order is a finite linear
combination of derivatives of

\[
 \mathscr X(s)=-\frac{\xi'(s)}{\xi(s)}
\]

at the **single line** `Re(s)=3/2`.

The resulting formula uses one absolutely convergent prime-power series and
explicit rational/polygamma terms.  No moving depth parameter and no second
Euler sample remain.

## 2. The three-point family

For `alpha>0`, `0<y<1/2`, put

\[
 r=\sqrt\alpha,
 \qquad q=\sqrt{\alpha+y^2},
\]

and

\[
 \mathcal F_{\alpha,y}(s)
 =\frac{\mathscr X(s+r)}r
 -\frac{\mathscr X(s+q-y)+\mathscr X(s+q+y)}{2q}.
\tag{L-90905.1}
\]

For `k>=0`, PR #378 defines

\[
 F_{k,y}(s)=(-\partial_\alpha)^k
 \mathcal F_{\alpha,y}(s)\big|_{\alpha=1}.
\tag{L-90905.2}
\]

## 3. Exact confluent limit

Uniformly on compact subsets on which the displayed samples avoid zeros of
`xi`,

\[
 q-r=\frac{y^2}{2r}+O(y^4),
 \qquad
 q^{-1}=r^{-1}-\frac{y^2}{2r^3}+O(y^4).
\]

Taylor expansion of the symmetric pair in (L-90905.1) gives

\[
 \boxed{
 \lim_{y\downarrow0}\frac{\mathcal F_{\alpha,y}(s)}{y^2}
 =\mathcal D_\alpha\mathscr X(s),
 }
\tag{L-90905.3}
\]

where

\[
 \boxed{
 \mathcal D_\alpha\mathscr X(s)
 =\frac{\mathscr X(s+r)}{2r^3}
 -\frac{\mathscr X'(s+r)}{2r^2}
 -\frac{\mathscr X''(s+r)}{2r}.
 }
\tag{L-90905.4}
\]

Analyticity in `(alpha,y^2)` permits every fixed number of alpha derivatives
to pass through the limit.  Hence

\[
 \boxed{
 \mathcal H_k(s)
 :=\lim_{y\downarrow0}\frac{F_{k,y}(s)}{y^2}
 =\left(-\frac1{2r}\frac d{dr}\right)^k
 \frac12\left[
 r^{-3}\mathscr X(s+r)
 -r^{-2}\mathscr X'(s+r)
 -r^{-1}\mathscr X''(s+r)
 \right]_{r=1}.
 }
\tag{L-90905.5}
\]

Thus `H_k(s_x)` reads only `mathscr X` and its derivatives at

\[
 s_x+1=\frac32+ix.
\]

## 4. Rational derivative coefficients

There are rational numbers `c_(k,j)`, `0<=j<=k+2`, such that

\[
 \boxed{
 \mathcal H_k(s)
 =\sum_{j=0}^{k+2}c_{k,j}\,
   \mathscr X^{(j)}(s+1).
 }
\tag{L-90905.6}
\]

They are generated without symbolic differentiation of `mathscr X`.  Put

\[
 c_{0,0}(r)=\frac1{2r^3},\quad
 c_{0,1}(r)=-\frac1{2r^2},\quad
 c_{0,2}(r)=-\frac1{2r},
\]

and recursively

\[
 c_{k+1,j}(r)
 =-\frac1{2r}\left(c'_{k,j}(r)+c_{k,j-1}(r)\right),
\tag{L-90905.7}
\]

with missing indices interpreted as zero.  Then
`c_(k,j)=c_(k,j)(1)`.  The first rows are

\[
\begin{array}{c|rrrrrr}
 k&c_{k,0}&c_{k,1}&c_{k,2}&c_{k,3}&c_{k,4}&c_{k,5}\\ \hline
 0&1/2&-1/2&-1/2\\
 1&3/4&-3/4&0&1/4\\
 2&15/8&-15/8&3/8&1/4&-1/8\\
 3&105/16&-105/16&15/8&5/16&-5/16&1/16.
\end{array}
\tag{L-90905.8}
\]

## 5. Independent partial-fraction formula

Let

\[
 a_{k,j}
 =[w^{k+3-j}]\frac{(1-w)^2}{(2-w)^{k+3}}
 \qquad(1\le j\le k+3).
\tag{L-90905.9}
\]

Then

\[
 \frac{z^2}{(1-z^2)^{k+3}}
 =\sum_{j=1}^{k+3}a_{k,j}
 \left[(1-z)^{-j}+(1+z)^{-j}\right],
\tag{L-90905.10}
\]

and

\[
 \boxed{
 c_{k,n}
 =\frac{4(k+2)!(-1)^{n+1}}{n!}\,a_{k,n+1}.
 }
\tag{L-90905.11}
\]

This gives an independent derivation of (L-90905.6) from the zero expansion and
the functional equation.

## 6. One absolutely convergent Euler series

For `Re(w)>1`,

\[
 \mathscr X(w)
 =\sum_{n\ge2}\frac{\Lambda(n)}{n^w}
 -\frac1w-\frac1{w-1}
 +\frac12\log\pi
 -\frac12\psi(w/2).
\tag{L-90905.12}
\]

Consequently, for every `j>=0`,

\[
 \mathscr X^{(j)}(w)
 =\sum_{n\ge2}\Lambda(n)(-\log n)^j n^{-w}
 +\mathcal A_j(w),
\tag{L-90905.13}
\]

where `A_j` is the explicit rational/polygamma derivative of the last four
terms.  At `w=3/2+ix` the series is absolutely convergent.

Define

\[
 P_k(t)=\sum_{j=0}^{k+2}c_{k,j}(-t)^j.
\tag{L-90905.14}
\]

Then

\[
 \boxed{
 -\Re\mathcal H_k(s_x)
 =-\Re\left[
 \sum_{n\ge2}\frac{\Lambda(n)}{n^{3/2+ix}}P_k(\log n)
 +\sum_{j=0}^{k+2}c_{k,j}\mathcal A_j(3/2+ix)
 \right].
 }
\tag{L-90905.15}
\]

The prime tail is elementary: with a constant `C_k` depending only on the
finite coefficient row,

\[
 \sum_{n>P}\frac{\Lambda(n)}{n^{3/2}}|P_k(\log n)|
 \le C_k\sum_{n>P}\frac{(1+\log n)^{k+3}}{n^{3/2}},
\tag{L-90905.16}
\]

and the latter is bounded by one endpoint term plus the explicit incomplete-
Gamma integral after `v=log u`.

## 7. Boundary

Proved here:

```text
three safe Euler samples -> one safe Euler line;
exact confluent differential operator;
rational all-order coefficient recurrence;
partial-fraction cross-check;
one absolutely convergent prime-power series per order.
```

Not proved here:

```text
nonnegativity of the resulting scalar hierarchy;
Riemann Hypothesis.
```
