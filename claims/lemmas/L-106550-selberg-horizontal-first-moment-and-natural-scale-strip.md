# L-106550 — Selberg zero density gives a sublinear horizontal first moment

Claim ID: `L-106550`  
Status: **PROVED UNCONDITIONALLY FROM THE CLASSICAL SELBERG ZERO-DENSITY ESTIMATE**  
Created: 2026-08-25  
Depends on: Selberg's zero-density theorem, in the explicit modern form of A. Simonič, *Explicit zero density estimate for the Riemann zeta-function near the critical line*, arXiv:1910.08274  
RH status: **not assumed**

Let

\[
N(\sigma;T,2T)
 =\#\{\rho=\beta+i\gamma:\zeta(\rho)=0,
       \ \beta>\sigma,\ T<\gamma\le2T\},
\]

with multiplicity, and define the horizontal first moment

\[
\boxed{
\mathfrak h_\zeta(T)
 =\sum_{T<\gamma\le2T}
  \left|\beta-\frac12\right|.
}
\tag{L-106550.1}
\]

## 1. Exact layer cake

The functional equation pairs every zero at real part `beta` with one at
`1-beta`, with the same ordinate and multiplicity. Therefore

\[
\boxed{
\mathfrak h_\zeta(T)
 =2\int_{1/2}^{1}N(\sigma;T,2T)\,d\sigma.
}
\tag{L-106550.2}
\]

This identity includes multiple zeros and requires no zero-separation or
simplicity hypothesis.

## 2. Selberg integration

Selberg's estimate, uniformly for `1/2<=sigma<=1`, is

\[
N(\sigma,X)
 \ll X^{1-\frac14(\sigma-1/2)}\log X.
\tag{L-106550.3}
\]

Since `N(sigma;T,2T)<=N(sigma,2T)`, put `u=sigma-1/2` and integrate:

\[
\begin{aligned}
\mathfrak h_\zeta(T)
&\ll T\log T
 \int_0^{1/2}T^{-u/4}\,du\\
&\le
 {4T\log T\over\log T}
 =O(T).
\end{aligned}
\]

Hence

\[
\boxed{
\mathfrak h_\zeta(T)=O(T)
 =o\!\left(N(T,2T)\right),
}
\tag{L-106550.4}
\]

because Riemann--von Mangoldt gives `N(T,2T) asymp T log T`.

In the centered Xi coordinate

\[
\Xi(z)=\xi\!\left(\frac12+iz\right),
\]

a zeta zero `beta+i gamma` corresponds to

\[
z=\gamma+i\left(\frac12-\beta\right).
\]

Thus (L-106550.4) is exactly an `O(T)` total vertical-height theorem for the
Xi zeros in the dyadic real window.

## 3. Natural-scale consequences

For any positive `eta`, Markov's inequality gives

\[
\boxed{
\#\left\{\rho:T<\gamma\le2T,
 \ \left|\beta-\frac12\right|\ge\eta\right\}
 \le {\mathfrak h_\zeta(T)\over\eta}.
}
\tag{L-106550.5}
\]

Consequently, for every function `A(T)->infinity`, all but `o(N(T,2T))`
zeros lie in

\[
\left|\beta-\frac12\right|
 <{A(T)\over\log T}.
\tag{L-106550.6}
\]

The original density estimate gives the sharper exponential natural-scale
form

\[
\boxed{
N\!\left(\frac12+{A\over\log T};T,2T\right)
 \ll e^{-A/4}N(T,2T)
}
\tag{L-106550.7}
\]

for fixed positive `A`, with the absolute implied constant inherited from
(L-106550.3). In particular, taking `A=A_0 log log T` gives a power saving in
`log T`.

## 4. What this proves and what it does not

The theorem pays any conclusion-facing error that is bounded by the **sum of
horizontal displacements** of the zeta zeros. It also shows that every
power-sized population away from the line must live at the microscopic
`1/log T` scale.

It does not bound the number of zeros whose displacement is much smaller than
`1/log T`. A topological all-pass or Hermite--Bézout charge counts such a zero
with unit multiplicity even when its displacement tends to zero. The exact
firewall is recorded in `R-106550`.