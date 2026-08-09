# L-32313 — The continuum SHARP scalar is the exact carry-law Volterra deconvolution

Claim ID: `L-32313`  
Title: After the critical half-power normalization, the all-depth SHARP scalar convolved with the exact continuum carry law is the elementary positive kernel `4(e^{-t/2}-e^{-t})`  
Status: **PROPOSED COMPLETE EXACT CROSS-ROUTE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `T-32302/L-32312`; PR #335 `L-33101` exact carry law  
Scope: exact transform/probability bridge; no positivity theorem and no RH claim

## 1. Critical normalization of the SHARP scalar

Retain

\[
 \Psi(x)=4\sqrt x\sum_{n\le x}{\mu(n)\over n}
 -3\sum_{n\le x}{\mu(n)\over\sqrt n}.
\]

Put

\[
\boxed{
 \varphi(t)=e^{-t/2}\Psi(e^t),
 \qquad t\ge0.
}
\tag{L-32313.1}
\]

Positivity of `varphi` is equivalent pointwise to positivity of `Psi`.

`T-32302` gives

\[
 \int_0^\infty \Psi(e^t)e^{-zt}\,dt
 ={z+3/2\over z(z-1/2)\zeta(z+1/2)}.
\]

Therefore for `Re w>0`,

\[
\boxed{
 \widehat\varphi(w)
 :=\int_0^\infty\varphi(t)e^{-wt}\,dt
 ={w+2\over w(w+1/2)\zeta(w+1)}.
}
\tag{L-32313.2}

## 2. Exact continuum carry law

Let `T` denote the nonnegative continuum carry random variable of PR #335 `L-33101`. Its Laplace transform is

\[
\boxed{
 P(w)=\mathbb E[e^{-wT}]
 ={2w\zeta(w+1)\over(w+1)(w+2)}.
}
\tag{L-32313.3}

Multiplication with (L-32313.2) cancels the complete zeta factor:

\[
\begin{aligned}
 \widehat\varphi(w)P(w)
 &={w+2\over w(w+1/2)\zeta(w+1)}
   {2w\zeta(w+1)\over(w+1)(w+2)}\\
 &=\boxed{
 {2\over(w+1/2)(w+1)}.
 }
\end{aligned}
\tag{L-32313.4}

But

\[
 {2\over(w+1/2)(w+1)}
 =4\left({1\over w+1/2}-{1\over w+1}\right),
\]

whose inverse Laplace transform is the strictly positive function

\[
\boxed{
 h(t)=4(e^{-t/2}-e^{-t}),
 \qquad t>0.
}
\tag{L-32313.5}

## 3. Exact Volterra equation

Let `nu_T` be the probability law of `T`. Uniqueness of Laplace transforms on the positive half-line gives

\[
\boxed{
 \int_{[0,t]}\varphi(t-u)\,d\nu_T(u)
 =4(e^{-t/2}-e^{-t})
 \qquad(t\ge0).
}
\tag{L-32313.6}

Equivalently,

\[
\boxed{
 \mathbb E\!\left[
  \varphi(t-T)\mathbf1_{T\le t}
 \right]
 =4(e^{-t/2}-e^{-t}).
}
\tag{L-32313.7}

Thus the all-depth reciprocal-zeta obstruction is exactly the causal deconvolution of one elementary positive forcing by the continuum average-carry delay law.

No asymptotic or RH assumption enters this identity.

## 4. Explicit carry density

PR #335 gives, for `x=e^t in [m,m+1)`,

\[
 \mathbb P(T>t)
 ={1\over m+1}
 +{u_x^2\over m(m+1)},
 \qquad
 u_x={m(m+1-x)\over x}.
\]

Differentiating inside a logarithmic cell gives the density

\[
\boxed{
 f_T(t)
 =2m(m+1-e^t)e^{-2t},
 \qquad
 \log m<t<\log(m+1).
}
\tag{L-32313.8}

It decreases from `2/m` to zero inside each cell and jumps upward to `2/(m+1)` at the next logarithmic integer boundary. Hence (L-32313.6) is a completely explicit scalar Volterra equation.

## 5. Exponential comparator

`L-33101` proves

\[
 T\le_{\rm st}E,
 \qquad E\sim\operatorname{Exp}(1).
\]

The same forcing `h` has the elementary deconvolution through the exponential law

\[
\boxed{
 f_E*\varphi_E=h,
 \qquad
 \varphi_E(t)=2e^{-t/2}.
}
\tag{L-32313.9}

Indeed the Laplace transform is

\[
 {1\over w+1}{2\over w+1/2}
 ={2\over(w+1/2)(w+1)}.
\]

Thus the exact SHARP solution is the carry-law analogue of the manifestly positive exponential solution.

The stochastic domination alone does **not** imply positivity of a Volterra deconvolution; no such inference is made here.

## 6. Relation to the Gamma convex-order theorem

PR #335 proves the stronger centered convex order

\[
 T+C\le_{\rm cx}G,
 \qquad
 G\sim\Gamma(2,1/2).
\]

Equations (L-32313.6)--(L-32313.9) identify the precise place where that probability theorem would have to enter a completion: one needs a variation-diminishing, resolvent-positive, or martingale comparison principle which transfers the positive exponential/Gamma deconvolution to the actual carry law.

Any such principle must be proved for this source-specific Volterra kernel; generic stochastic or convex order does not invert convolution inequalities.

## 7. Why this is a genuine cross-route reduction

Before this identity the two programmes were phrased differently:

```text
SHARP / carry inverse:
    sign of a zero-safe Mobius scalar Psi;

Gamma-carry programme:
    probability law of the continuum carry delay T.
```

They are now one equation:

```text
carry-law convolution * critical SHARP state
    = elementary positive two-exponential forcing.
```

The complete reciprocal-zeta factor is exactly the reciprocal of the zeta factor in the carry-law Laplace transform.

This does not make the inverse positive automatically; proving that positivity would close the all-depth SHARP/RH route.

## 8. Proof boundary

Closed exactly here:

1. critical normalization of `Psi`;
2. exact Laplace product with the carry law;
3. complete cancellation of `zeta(w+1)`;
4. positive elementary forcing;
5. explicit Volterra probability equation;
6. exact carry density;
7. exponential comparator and its positive solution.

Still open:

1. a resolvent-positivity / variation-diminishing theorem for the exact carry kernel;
2. positivity of `varphi` / `Psi`;
3. full SHARP;
4. RH.
