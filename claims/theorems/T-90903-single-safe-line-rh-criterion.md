# T-90903 — A single-safe-line derivative hierarchy is an RH criterion

Claim ID: `T-90903`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT CRITERION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-90905`; the standard zero count; the terminal-pair argument reproduced below  
RH status: **unproved**

## 1. The scalar

Let

\[
 s_x=\frac12+ix,
 \qquad
 \mathscr X(s)=-\xi'(s)/\xi(s),
\]

and let `H_k` be the one-safe-line differential expression of `L-90905`.
Define

\[
 \boxed{
 \mathfrak S_k(x)=-\Re\mathcal H_k(s_x).
 }
\tag{T-90903.1}
\]

Equivalently, if

\[
 \kappa_k(z)
 =-2(k+2)!\frac{z^2}{(1-z^2)^{k+3}},
\tag{T-90903.2}
\]

then the absolutely convergent zero expansion is

\[
 \boxed{
 \mathfrak S_k(x)
 =\sum_{\xi(1/2+i\gamma)=0}m_\gamma
   \kappa_k(i(\gamma-x))
 +2\sum_{\Re\rho>1/2}m_\rho
   \Re\kappa_k(\rho-s_x).
 }
\tag{T-90903.3}
\]

The first sum runs over critical-line zeros; the second chooses one member of
each reflected pair in the right half of the strip.  Formula (T-90903.3) follows
either by confluent passage from PR #378 or directly from the partial fractions in
`L-90905` and the functional equation of `xi`.

## 2. RH gives positivity

On the critical line `z=iu`,

\[
 \boxed{
 \kappa_k(iu)
 =2(k+2)!\frac{u^2}{(1+u^2)^{k+3}}\ge0.
 }
\tag{T-90903.4}
\]

Therefore

\[
 \mathrm{RH}\Longrightarrow
 \mathfrak S_k(x)\ge0
 \qquad(k\ge0,\ x\in\mathbb R).
\tag{T-90903.5}
\]

## 3. Terminal pair exists under false RH

Represent a right-side zero by `(t,y)` when

\[
 \rho=\frac12+y+it,
 \qquad 0<y<\frac12.
\]

For distinct right-side zeros define a threat edge

\[
 (t,y)\longrightarrow(u,d)
 \quad\Longleftrightarrow\quad
 d^2-(u-t)^2\ge y^2.
\tag{T-90903.6}
\]

Every edge strictly increases depth and satisfies

\[
 (u-t)^2\le d^2-y^2.
\]

If every vertex had an outgoing edge, a chain would obey

\[
 \sum_n(t_{n+1}-t_n)^2<\frac14,
 \qquad
 |t_N-t_0|<\frac12\sqrt N.
\]

The first `N` distinct zeros would lie in an ordinate interval of length
`O(sqrt(N))`, contradicting the standard `O(R log R)` zero count.  Hence a
terminal pair exists.

## 4. Large order isolates the terminal pair

Let `(t,y)` be terminal and evaluate at `x=t`.  Its reflected pair contributes

\[
 2m\kappa_k(y)
 =-4m(k+2)!\frac{y^2}{(1-y^2)^{k+3}}<0.
\tag{T-90903.7}
\]

For every nuisance right-side zero `z=d+ir`, terminality gives

\[
 d^2-r^2<y^2.
\]

Therefore

\[
 \Re(1-z^2)=1-d^2+r^2>1-y^2>0,
\]

and hence

\[
 \boxed{|1-z^2|>1-y^2.}
\tag{T-90903.8}
\]

Every fixed nuisance is exponentially smaller than (T-90903.7) as `k` grows.
Critical-line terms have denominator `1+u^2>1-y^2`.  A far-zero bound

\[
 |\kappa_k(d+ir)|
 \ll (k+2)!(1+r^2)^{-k-2}
\]

and the local zero count provide a summable majorant, so dominated convergence
upgrades the pointwise separation to the complete zero sum.  Thus

\[
 \boxed{
 \mathfrak S_k(t)<0
 \quad\text{for every sufficiently large }k.
 }
\tag{T-90903.9}
\]

## 5. Criterion and countable reduction

Combining the two directions,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathfrak S_k(x)\ge0
 \quad\text{for every }k\in\mathbb Z_{\ge0},\ x\in\mathbb R.
 }
\tag{T-90903.10}
\]

The false-RH witness is strict, and `mathfrak S_k` is continuous in `x`.
Therefore rational centres suffice:

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathfrak S_k(r)\ge0
 \quad(k\ge0,\ r\in\mathbb Q).
 }
\tag{T-90903.11}
\]

## 6. Finite linear prime witnesses

By `L-90905`, each `mathfrak S_k(x)` is one absolutely convergent prime-power
series on `Re(s)=3/2`, plus explicit rational and polygamma terms.  The elementary
tail (L-90905.16) is uniform on real `x`.  Hence

```text
false RH
 -> finite order k
 -> rational centre x
 -> finite prime-power cutoff P
 -> strict outward-rounded negative interval.
```

Conversely any such rigorously negative interval disproves RH by the exact
explicit formula.  No negative Riemann-data instance is claimed here.

## 7. Advance over the parent hierarchies

The criterion removes both continuous auxiliary parameters of the terminal
families:

```text
PR #375: centre x, depth y, heat q;
PR #378: centre x, depth y, derivative order k;
PR #379: centre x, heat q;
this theorem: centre x, integer order k.
```

More importantly, every finite stage is evaluated at one fixed safe Euler line,
not three moving sample points.  The remaining sign is still RH-equivalent.
