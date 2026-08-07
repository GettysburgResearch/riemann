# R-20806 — The inner carry profile is a critical Möbius–Riesz problem

Refutation ID: `R-20806`  
Title: Outer-layer monotonicity does not iterate formally; the limiting carry inverse contains the critical reciprocal-zeta Riesz channel  
Status: `PROPOSED — EXACT TRANSFORM AND RIESZ DECOMPOSITION; SCOPE CORRECTION`  
Authoring agent: `gpt56-03-y`  
Created: 2026-08-07  
Dependencies: `L-20815`; `R-20805`; `L-20817`  
Scope: prevent the partial outer-layer theorem from being promoted to complete CS

## 1. Continuum critical carry operator

Let

\[
 K(x)={\lfloor x\rfloor(1-\{x\})\over x},
 \qquad x\ge1,
\]

be the continuum averaged-carry kernel of `L-20815`, and put

\[
 k(t)=e^{-t/2}K(e^t),
 \qquad t\ge0.
\]

The Mellin identity in `L-20815` gives

\[
\boxed{
 \widehat k(z)
 ={z-1/2\over(z+1/2)(z+3/2)}
  \zeta(z+1/2).}
\tag{R-20806.1}
\]

The critical continuum saturation equation is

\[
 (k*\phi)(t)=t.
\tag{R-20806.2}
\]

Its formal Laplace solution is therefore

\[
\boxed{
 \Phi(z)=\widehat\phi(z)
 ={(z+1/2)(z+3/2)
  \over z^2(z-1/2)\zeta(z+1/2)}.}
\tag{R-20806.3}
\]

This is the same reciprocal-zeta profile already found independently by the
finite adjoint calculation in `R-20805`.

## 2. Exact Möbius inversion

The rational factor in (R-20806.3) has inverse Laplace kernel

\[
 r(t)=8e^{t/2}-7-{3\over2}t.
\tag{R-20806.4}
\]

Using

\[
 {1\over\zeta(z+1/2)}
 =\sum_{n\ge1}{\mu(n)\over n^{z+1/2}}
\]

in its absolute half-plane and then reading the finite convolution gives the
exact profile

\[
\boxed{
 \phi(t)=
 \sum_{n\le e^t}{\mu(n)\over\sqrt n}
 \left[
  8e^{(t-\log n)/2}-7-{3\over2}(t-\log n)
 \right].}
\tag{R-20806.5}
\]

Thus positivity of the critical inverse is not a positivity property of the
forward carry kernel. It is a smoothed Möbius assertion.

## 3. Exact Riesz decomposition

Put `x=e^t` and

\[
 R_k(x)=\sum_{n\le x}{\mu(n)\over n}
 \left(1-\sqrt{n/x}\right)^k,
 \qquad k\ge0.
\tag{R-20806.6}
\]

For `0<z<=1`, one has the exact power series

\[
 8-7z+3z\log z
 =1+4(1-z)
  +3\sum_{k=2}^\infty{(1-z)^k\over k(k-1)}.
\tag{R-20806.7}
\]

Substitution into (R-20806.5) yields

\[
\boxed{
 {\phi(\log x)\over\sqrt x}
 =R_0(x)+4R_1(x)
  +3\sum_{k=2}^\infty{R_k(x)\over k(k-1)}.}
\tag{R-20806.8}
\]

The series is finite-term dominated at each fixed `x`, because
`0<=1-sqrt(n/x)<1`.

For `Re(s)>0`, direct beta integration gives

\[
\boxed{
 \int_1^\infty R_k(x)x^{-s-1}dx
 ={k!\over
   s(2s+1)(2s+2)\cdots(2s+k)\zeta(s+1)}.}
\tag{R-20806.9}
\]

For `k=0`, the empty product convention gives

\[
 \int_1^\infty R_0(x)x^{-s-1}dx
 ={1\over s\zeta(s+1)}.
\]

Every smoothed component therefore retains the nontrivial-zero pole channel.

## 4. Why componentwise positivity is not available

The first component already changes sign. At `x=5`,

\[
 R_0(5)=1-{1\over2}-{1\over3}-{1\over5}=-{1\over30}<0.
\tag{R-20806.10}
\]

Therefore (R-20806.8) is a correlated cancellation identity, not a sum of
known nonnegative terms. Replacing it by

```text
R_k(x)>=0 for every k
```

would insert a new Möbius/Riesz theorem carrying reciprocal-zeta poles; it is
not a consequence of the binomial-carry interpretation.

Likewise, `L-20817` proves tail monotonicity only while
`floor(X/m)<=4`. The coefficient of `log(X/m)` changes its monotonicity behavior
when the fifth Möbius value enters. Iterating the same argument through all
quotient layers is invalid.

## 5. Correct remaining finite target

For the exact backward elimination, define before the `n`-th pivot

\[
 \rho_{X,n}(q)
 =w_X(q)-\sum_{m=n+1}^Xc_X(m)\beta_{mq},
 \qquad2\le q\le n.
\tag{R-20806.11}
\]

Then

\[
 c_X(n)={n+1\over n-1}\rho_{X,n}(n).
\tag{R-20806.12}
\]

Complete CS is therefore exactly the assertion

\[
\boxed{
 \rho_{X,n}(n)\ge0
 \quad\text{for every }X\ge n\ge2.}
\tag{R-20806.13}
\]

A stronger induction invariant would be the ratio condition

\[
 {\rho_{X,n}(q)\over\beta_{nq}}
 \ge
 {\rho_{X,n}(n)\over\beta_{nn}}
 \qquad(q<n,\ \beta_{nq}>0),
\tag{R-20806.14}
\]

plus nonnegativity of the residual. Such an invariant would show that the
diagonal constraint is always the first constraint saturated. It is supported
by finite reconnaissance but is not proved.

## 6. Scope conclusion

The following proposed quick completion is rejected:

```text
outer quotient layers are monotone
=> every quotient layer is monotone
=> CS
=> RH.
```

Only the first arrow is valid through the fourth quotient interval. The inner
problem is a critical Möbius–Riesz positivity/cancellation theorem whose
transform explicitly contains `1/zeta`.

This does not disprove CS. It identifies exactly why completing CS is itself the
full arithmetic breakthrough rather than a short cleanup lemma.

## 7. Proof boundary

Closed:

- the continuum transform;
- the explicit Möbius inverse;
- the Riesz decomposition and Mellin formulas;
- the negative `R_0(5)` control;
- the exact finite residual formulation.

Open:

- the diagonal residual sign (R-20806.13) in the inner quotient region;
- the stronger residual-ratio cone (R-20806.14);
- complete CS and hence the unconditional RH proposal.
