# L-90021 — The complete prime-power source is a decreasing-cell renewal with prime-power jumps

Claim ID: `L-90021` (provisional branch range)  
Title: After critical normalization, the complete von-Mangoldt occupancy source decreases strictly between consecutive integers and jumps upward exactly at prime powers  
Status: **PROPOSED COMPLETE EXACT FINITE-STATE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-90016/L-90017`; elementary divisor switching  
Scope: exact complete-prime-power source dynamics; no subquadratic gap estimate or RH conclusion

## 1. Complete source

Put

\[
 \mathcal Q_\Lambda(t)
 =e^{-t/2}
  \sum_{q\le e^t}\Lambda(q)\Delta_q(e^t),
\tag{L-90021.1}
\]

and critically normalize it by

\[
\boxed{
 R_\Lambda(t)=e^{-t/2}\mathcal Q_\Lambda(t)
 =e^{-t}\sum_{q\le e^t}\Lambda(q)\Delta_q(e^t).
}
\tag{L-90021.2}

The source is positive. The normalized state is right-continuous and locally of bounded variation.

## 2. Integer endpoint formula

For an integer `N>=2`, `L-90016.21` gives

\[
\boxed{
 R_\Lambda(\log N)
 =\sum_{q\le N}{\Lambda(q)\over q}
  -{\log(N!)\over N}+{\log N\over N}.
}
\tag{L-90021.3}

Indeed

\[
 \sum_{q\le N}\Lambda(q)\left\{\frac Nq\right\}
 =N\sum_{q\le N}{\Lambda(q)\over q}-\log(N!),
\]

and the endpoint-divisor correction is

\[
 \sum_{q\mid N}\Lambda(q)=\log N.
\]

## 3. Exact cell law

Fix an integer `N>=2` and let

\[
 N<X<N+1,
 \qquad t=\log X.
\]

Define

\[
 P_\Lambda(N)=\sum_{q\le N}{\Lambda(q)\over q}
\tag{L-90021.4}
\]

and

\[
\boxed{
 S_\Lambda(N)=(N+1)\log N-\log(N!).
}
\tag{L-90021.5}
\]

The general occupancy slope calculation of `L-90017` uses

\[
 \sum_{q\mid N}\Lambda(q)=\log N
\]

and gives

\[
\boxed{
 \mathcal Q_\Lambda(t)
 =e^{t/2}[P_\Lambda(N)-\log N]
  +e^{-t/2}S_\Lambda(N).
}
\tag{L-90021.6}

Therefore

\[
\boxed{
 R_\Lambda(t)
 =P_\Lambda(N)-\log N
  +e^{-t}S_\Lambda(N).
}
\tag{L-90021.7}

The cell curvature is particularly simple:

\[
\boxed{
 R_\Lambda'(t)
 =-e^{-t}S_\Lambda(N)<0.
}
\tag{L-90021.8}

Strict positivity of `S_Lambda` follows from

\[
 \log(N!)<N\log N<(N+1)\log N.
\]

Thus the critically normalized complete source decreases strictly on every open interval between consecutive integer endpoints.

## 4. Prime-power jumps

Every old occupancy deficit is continuous at an integer. A new column `q=N` activates only when `Lambda(N)>0`, and its initial occupancy deficit is one. Hence

\[
\boxed{
 R_\Lambda(\log N^+)-R_\Lambda(\log N^-)
 =\frac{\Lambda(N)}N.
}
\tag{L-90021.9}

The jump is positive and occurs exactly at prime powers.

Consequently the complete normalized source is an exact sawtooth renewal:

```text
between integers:
    deterministic strict decay with rate e^(-t) S_Lambda(N);

at N=p^a:
    positive jump Lambda(N)/N;

at every other integer:
    no jump.
```

## 5. Signed flux

Equations (L-90021.8)--(L-90021.9) give the measure identity

\[
\boxed{
 dR_\Lambda(t)
 =\sum_{q=p^a}{\Lambda(q)\over q}\,
   \delta_{\log q}(dt)
  -e^{-t}S_\Lambda(\lfloor e^t\rfloor)\,dt.
}
\tag{L-90021.10}

The positive atomic and negative continuous masses have an exact common arithmetic origin: the divisor identity `sum_(q|n)Lambda(q)=log n`.

## 6. Gamma-potential endpoint

Define the complete prime-power residual

\[
 F_\Lambda(X)=\sum_{q\le X}\Lambda(q)r_X(q).
\tag{L-90021.11}
\]

By `L-90019` at `sigma=2`,

\[
\boxed{
 -e^{-t/2}F_\Lambda(e^t)
 =\int_{[0,t]}(t-u)e^{-(t-u)/2}\,dR_\Lambda(u).
}
\tag{L-90021.12}

Substituting the flux gives the exact positive-kernel quadrature formula

\[
\boxed{
\begin{aligned}
 -e^{-t/2}F_\Lambda(e^t)
 ={}&\sum_{q=p^a\le e^t}{\Lambda(q)\over q}
  (t-\log q)e^{-(t-\log q)/2}\\
 &-\sum_{N<e^t}S_\Lambda(N)
  \int_{\log N}^{\min(\log(N+1),t)}
  e^{-u}(t-u)e^{-(t-u)/2}\,du.
\end{aligned}}
\tag{L-90021.13}

Every kernel is nonnegative. The unresolved cancellation is exactly the quadrature error between the prime-power atoms and the deterministic cell density.

## 7. Direct carry/entropy identity

The complete von-Mangoldt dual switches through the carry columns:

\[
\begin{aligned}
 \sum_q\Lambda(q)v_q(b_X)
 &=\sum_{m=2}^Xb_X(m)
   \left[
    \sum_{q\mid m}\Lambda(q)
    -\sum_{q\mid m-1}\Lambda(q)
   \right]\\
 &=\sum_{m=2}^Xb_X(m)\log\frac m{m-1}.
\end{aligned}
\]

Therefore

\[
\boxed{
 F_\Lambda(X)
 =J_\Lambda(X)-P_\Lambda(X),
}
\tag{L-90021.14}
\]

where

\[
\boxed{
 J_\Lambda(X)
 =\sum_{m=2}^Xb_X(m)\log\frac m{m-1}
}
\tag{L-90021.15}
\]

is the deterministic parabolic entropy score and

\[
 P_\Lambda(X)
 =\sum_{q\le X}{\Lambda(q)\over\sqrt q}
  \log{X\over q}
\tag{L-90021.16}
\]

is the complete prime-power ramp.

Thus the complete occupancy renewal is exactly the positive-carry primal/dual gap of the elementary programme.

## 8. Proof boundary

Closed exactly:

1. the integer complete-source formula;
2. the two-exponential cell law;
3. strict decrease on every open cell;
4. positive jumps exactly at prime powers;
5. the signed flux measure;
6. the Gamma-potential quadrature formula;
7. the exact parabolic-score minus prime-ramp identity.

Open:

1. a subquadratic bound for `F_Lambda`;
2. a cancellation theorem for the renewal quadrature;
3. RH.