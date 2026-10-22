# L-91410 — The Jordan-weighted knot packet is an exact monotone prime-deletion transport with a computable log budget

Claim ID: `L-91410`  
Status: **EXACT FINITE-PRIME COUPLING AND KNOT NORMAL FORM**  
Created: 2026-08-12  
Depends on: `L-91402`; elementary independent geometric prime exponents  
RH status: **unproved**

## 1. Base and Jordan-tilted prime laws

Fix a finite prime set `P` and `s>0`. Under the base product law, let the prime exponents be independent with

\[
 \mathbb P(E_p=k)=(1-p^{-1})p^{-k},
 \qquad k\ge0.
\]

Put

\[
 M=\prod_{p\in P}p^{E_p},
 \qquad
 F_s(M)=\prod_{p\mid M}(1-p^{-s}).
\]

The exact normalizing constant is

\[
 \mathbb E F_s(M)=P_s(\mathcal P)
 :=\prod_{p\in\mathcal P}(1-p^{-1-s}).
\tag{L-91410.1}
\]

Let `Q_s` be the tilted law

\[
 \frac{d\mathbb Q_s}{d\mathbb P}
 =\frac{F_s(M)}{P_s(\mathcal P)}.
\]

At one prime, writing `r=p^-1` and `u=p^-s`,

\[
 \mathbb Q_s(E_p=0)=\frac{1-r}{1-ru},
\]

\[
 \mathbb Q_s(E_p=k)
 =\frac{(1-u)(1-r)r^k}{1-ru},
 \qquad k\ge1.
\tag{L-91410.2}
\]

Conditioned on positivity, the exponent law is unchanged. Only the activation probability is thinned.

## 2. Exact monotone coupling

There is a coordinatewise coupling `(E_p^0,E_p^s)` with the base and tilted marginals such that

\[
 \boxed{E_p^s\le E_p^0\quad\text{almost surely}.}
\tag{L-91410.3}
\]

Indeed, sample one shifted geometric positive exponent and nested activation Bernoulli variables with probabilities

\[
 r_s=\frac{r(1-u)}{1-ru}<r.
\]

Put

\[
 X=\log M_0,
 \qquad
 Y=\log M_s.
\]

Then

\[
 \boxed{Y\le X\quad\text{almost surely}.}
\tag{L-91410.4}
\]

The expected deleted logarithmic mass is exact:

\[
 \boxed{
 \mathbb E(X-Y)
 =\sum_{p\in\mathcal P}
  \frac{\log p}{p^{1+s}-1}.
 }
\tag{L-91410.5}
\]

This is the finite Euler truncation of

\[
 -\frac{\zeta'}{\zeta}(1+s).
\]

## 3. Exact ramp-gain identity

For `a>0`, `t>0`, and `kappa>0`, define the decreasing stopped affine ramp

\[
 h_{a,t}(x)
 =\kappa a\,\mathbf1_{x<t}
  +4a^2(t-x)_+.
\tag{L-91410.6}
\]

The monotone coupling gives the pointwise identity

\[
\boxed{
\begin{aligned}
 h_{a,t}(Y)-h_{a,t}(X)
={}&\kappa a\,\mathbf1_{Y<t\le X}\\
&+4a^2[(X\wedge t)-(Y\wedge t)].
\end{aligned}}
\tag{L-91410.7
}
\]

Hence

\[
\boxed{
\begin{aligned}
 \mathbb E_{\mathbb Q_s}h_{a,t}(Y)
 -\mathbb E_{\mathbb P}h_{a,t}(X)
={}&\kappa a\,\mathbb P(Y<t\le X)\\
&+4a^2\mathbb E[(X\wedge t)-(Y\wedge t)]
\ge0.
\end{aligned}}
\tag{L-91410.8
}
\]

This is a quantitative refinement of the Harris–FKG sign. It records exactly which part of the full logarithmic deletion budget survives the cutoff.

## 4. Exact pre-knot representation

Take `t=log n` and let `P` be all primes below `n`. Every integer `m<n` is `P`-smooth, while the ramp vanishes at and above `n`. Put

\[
 Z_0(n)=\prod_{p<n}(1-p^{-1}),
 \qquad
 P_s(n)=\prod_{p<n}(1-p^{-1-s}).
\]

Then

\[
 \sum_{m<n}\frac{F_s(m)}m h_{a,t}(\log m)
 =\frac{P_s(n)}{Z_0(n)}
  \mathbb E_{\mathbb Q_s}h_{a,t}(Y),
\tag{L-91410.9}
\]

and

\[
 \sum_{m<n}\frac1m h_{a,t}(\log m)
 =\frac1{Z_0(n)}
  \mathbb E_{\mathbb P}h_{a,t}(X).
\tag{L-91410.10}
\]

For the Green-removal packet, set `s=2a` and `kappa=sqrt(275/14)`. The exact knot scalar of `L-91402` is

\[
 B_a(t-)
 =-c_s+
 \sum_{m<n}\frac{F_s(m)}m h_{a,t}(\log m)
 -c_s\int_0^t h_{a,t}(x)dx.
\tag{L-91410.11}
\]

Adding and subtracting the base harmonic sum gives

\[
\boxed{
\begin{aligned}
 B_a(t-)
={}&-c_s
 +\frac{P_s(n)}{Z_0(n)}\,\mathcal G_{a,n}\\
&+(P_s(n)-c_s)
  \sum_{m<n}\frac{h_{a,t}(\log m)}m\\
&+c_s\left[
  \sum_{m<n}\frac{h_{a,t}(\log m)}m
  -\int_0^t h_{a,t}(x)dx
 \right],
\end{aligned}}
\tag{L-91410.12
}
\]

where the transport gain is the explicit nonnegative quantity

\[
\boxed{
\begin{aligned}
 \mathcal G_{a,n}
={}&\kappa a\,\mathbb P(Y<t\le X)\\
&+4a^2\mathbb E[(X\wedge t)-(Y\wedge t)].
\end{aligned}}
\tag{L-91410.13
}
\]

The last two lines of (L-91410.12) are nonnegative: `P_s(n)>c_s`, and the left harmonic sum dominates the logarithmic integral.

Therefore

\[
 \boxed{
 B_a(\log n-)
 \ge-c_s+\frac{P_s(n)}{Z_0(n)}\mathcal G_{a,n}.
 }
\tag{L-91410.14}
\]

## 5. Exact surviving transport theorem

A sufficient and source-faithful completion of the compact Green density is now

\[
 \boxed{
 \frac{P_s(n)}{Z_0(n)}\mathcal G_{a,n}\ge c_s
 \qquad(s=2a)
 }
\tag{L-91410.15}
\]

for every unresolved knot.

The full untruncated slope budget is

\[
 4a^2\mathbb E(X-Y)
 =4a^2\sum_{p<n}
  \frac{\log p}{p^{1+2a}-1},
\tag{L-91410.16}
\]

which has exactly the critical scale needed to pay `c_(2a)`. The only loss is now explicit:

```text
log deletion occurring entirely above the cutoff t;
and the part of a crossing overshoot not covered by the kappa-a jump.
```

Thus the missing Green-removal mechanism is an overshoot estimate for one monotone prime-deletion coupling, not an unspecified arithmetic sign.

This theorem does not prove (L-91410.15). It replaces the failed scalar FKG closure by an exact quantitative transport target retaining every prime activation and the contact atom.
