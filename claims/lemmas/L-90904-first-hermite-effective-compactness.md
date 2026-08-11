# L-90904 — Effective compactness of the first-Hermite RH search

Claim ID: `L-90904`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PARTIAL SIGN THEOREM**  
Created: 2026-08-11  
Depends on: the exact first-Hermite prime formula of PR #379; standard effective lower bounds for the real digamma factor

Let \(\mathcal M_\zeta(q,x)\) be the scalar of PR #379:

\[
 \mathcal M_\zeta(q,x)
 =\sum_\rho m_\rho(\gamma_\rho-x)^2e^{-q(\gamma_\rho-x)^2}.
\tag{L-90904.1}
\]

Its exact Guinand--Weil formula is a pole term plus a gamma integral minus an absolutely convergent prime sum.

## 1. Uniform prime envelope

Define

\[
 P(q)=\frac1{2\sqrt\pi q^{3/2}}
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \left(1+\frac{(\log n)^2}{2q}\right)
 e^{-(\log n)^2/(4q)}.
\tag{L-90904.2}
\]

Then the absolute value of the prime contribution is at most \(P(q)\), uniformly in \(x\).  It is finite for every \(q>0\), and an elementary integral majorant using \(\Lambda(n)\le\log n\) is effective.

The pole contribution obeys the uniform bound

\[
 |h_{q,x}(i/2)+h_{q,x}(-i/2)|
 \le P_0(q)
 :=2e^{q/4}\left(\frac1{eq}+\frac14\right).
\tag{L-90904.3}
\]

## 2. Gamma drift at large centre

There are effective absolute constants \(c_0,C_0>0\) such that the archimedean density satisfies

\[
 \mu(\tau)\ge -C_0,
 \qquad
 \mu(\tau)\ge c_0\log(2+|\tau|)-C_0.
\tag{L-90904.4}
\]

Using the interval \(1\le\sqrt q\,|\tau-x|\le2\) on the side pointing away from the origin, one obtains

\[
 \Gamma_{q,x}
 \ge q^{-3/2}\big[c_1\log(2+|x|)-C_1(1+|\log q|)\big]
\tag{L-90904.5}
\]

with effective constants.

Consequently, for every fixed \(q>0\),

\[
 \boxed{
 \mathcal M_\zeta(q,x)>0
 \qquad(|x|\ge X(q)),
 }
\tag{L-90904.6}
\]

where one may take an explicit

\[
 X(q)=2\exp\!\left(
 \frac{C_1(1+|\log q|)+q^{3/2}[P(q)+P_0(q)]}{c_1}
 \right).
\tag{L-90904.7}
\]

Thus each fixed-\(q\) inequality needs to be checked only on a compact real interval.

## 3. An unconditional small-heat regime

For every real \(x\), one of the two scaled bands

\[
 1\le \pm\sqrt q\,(\tau-x)\le2
\]

lies at \(|\tau|\gg q^{-1/2}\).  Equation (L-90904.4) then gives, uniformly in \(x\),

\[
 \Gamma_{q,x}
 \ge q^{-3/2}\big[c_2\log(1/q)-C_2\big].
\tag{L-90904.8}
\]

As \(q\downarrow0\), the pole bound is only polynomial in \(q^{-1}\), while the prime envelope is exponentially suppressed by

\[
 e^{-(\log2)^2/(4q)}.
\]

Therefore there is an effective \(q_0>0\) such that

\[
 \boxed{
 \mathcal M_\zeta(q,x)>0
 \qquad(0<q\le q_0,\ x\in\mathbb R).
 }
\tag{L-90904.9}
\]

This is an unconditional positive portion of the first-Hermite criterion.

## 4. Operational consequence

Combining PR #379 with (L-90904.6)--(L-90904.9), RH is equivalent to checking

```text
q in a countable unbounded set with q >= q0;
x in the finite interval [-X(q), X(q)].
```

The prime tail and the derivative in \(x\) have explicit Gaussian envelopes, so each finite \(q\)-slice admits a finite directed interval-mesh certificate.  The unresolved issue is the unbounded \(q\)-direction, exactly where a terminal off-line pair would dominate.
