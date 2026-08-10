# L-33805 — Q=4 physical prefix is filtered Chebyshev plus a quadratic four-adic staircase

Claim ID: `L-33805`  
Title: The complete pole-preserving Q=4 physical prefix simplifies exactly to one four-adically filtered ordinary Chebyshev function plus an explicit quadratic logarithmic staircase  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32407/L-32412`; finite geometric summation  
Scope: exact physical-prefix simplification; no prime-error estimate, energy bound, or RH conclusion

## 1. Q=4 physical coefficient and prefix

Retain the Q=4 generalized-prime sequence

\[
\Lambda_4
=\Lambda+D,
\]

where

\[
D(4^r)=(4^r-1)\log4\qquad(r\ge1)
\]

and `D` vanishes elsewhere.  Retain also the local source

\[
 e_4(1)=1,
 \qquad
 e_4(4^r)=-3\quad(r\ge1),
\]

with zero coefficients off the four-adic tower.

The true pole-preserving interval coefficient is

\[
 c_4=e_4*\Lambda_4,
\]

and its prefix is

\[
 \boxed{
 G_4(x)=\sum_{m\le x}c_4(m).
 }
 \tag{L-33805.1}
\]

Let

\[
 \psi(x)=\sum_{m\le x}\Lambda(m)
\]

with the convention `psi(x)=0` for `0<=x<1`.

## 2. Prefix as a four-adic convolution

Because `e_4` is supported on `4^r`, finite divisor switching gives for every real `x>=1`

\[
 \boxed{
 G_4(x)
 =\Psi_4(x)-3\sum_{r\ge1}\Psi_4(x/4^r),
 }
 \tag{L-33805.2}
\]

where

\[
 \Psi_4(x)=\sum_{m\le x}\Lambda_4(m).
\]

Only finitely many terms occur.

PR #325 `L-32412` gives, with

\[
 R=R(x):=\lfloor\log_4x\rfloor,
\]

the exact generalized-prime prefix

\[
 \boxed{
 \Psi_4(x)
 =\psi(x)
 +(\log4)
 \left[
 {4^{R+1}-4\over3}-R
 \right].
 }
 \tag{L-33805.3}
\]

## 3. Exact cancellation of the exponential four-adic mass

Put

\[
 A_R={4^{R+1}-4\over3}-R,
 \qquad R\ge0.
\]

For `r<=R`, one has `R(x/4^r)=R-r` except on harmless exact endpoints, where the same floor identity is literal.  Hence the deterministic contribution in (L-33805.2) is

\[
 A_R-3\sum_{k=0}^{R-1}A_k.
\]

Now

\[
\begin{aligned}
 \sum_{k=0}^{R-1}A_k
 &=\frac13\sum_{k=0}^{R-1}(4^{k+1}-4)
   -\sum_{k=0}^{R-1}k\\
 &=\frac{4(4^R-1)}9-\frac{4R}3-\frac{R(R-1)}2.
\end{aligned}
\]

Therefore

\[
\begin{aligned}
 A_R-3\sum_{k=0}^{R-1}A_k
 &={4^{R+1}-4\over3}-R
   -\left[{4(4^R-1)\over3}-4R-{3R(R-1)\over2}\right]\\
 &=\boxed{{3\over2}R(R+1)}.
\end{aligned}
 \tag{L-33805.4}
\]

The complete exponentially large four-adic generalized-prime correction cancels exactly.

## 4. Closed physical-prefix formula

Combining (L-33805.2)--(L-33805.4),

\[
 \boxed{
 G_4(x)
 =\psi(x)
 -3\sum_{r\ge1}\psi(x/4^r)
 +{3\over2}R(x)(R(x)+1)\log4.
 }
 \tag{L-33805.5}
\]

Every sum is finite and every endpoint convention is inherited from the real-prefix convention for `psi`.

Thus the Q=4 pole current is not an opaque generalized-prime prefix.  It is exactly

```text
ordinary Chebyshev prefix
- 3 times all strict four-adic ancestors
+ one explicit quadratic log_4 staircase.
```

No prime estimate or zero-free region enters this identity.

## 5. Jensen/carry field decomposition

For real `x>=1` and `0<=theta<=1`, define

\[
 \mathcal Q_4(x,\theta)
 =G_4(x)-G_4(\theta x)-G_4((1-\theta)x).
\]

Put

\[
 \mathcal J_\psi(x,\theta)
 =\psi(x)-\psi(\theta x)-\psi((1-\theta)x)
\]

and

\[
 B_4(x)={3\over2}R(x)(R(x)+1)\log4.
\]

Then (L-33805.5) gives exactly

\[
 \boxed{
 \mathcal Q_4(x,\theta)
 =\mathcal J_\psi(x,\theta)
 -3\sum_{r\ge1}
   \mathcal J_\psi(x/4^r,\theta)
 +\mathcal J_{B_4}(x,\theta).
 }
 \tag{L-33805.6}
\]

Again only finitely many terms are nonzero.

The deterministic staircase term is completely explicit and has size `O(log^2 x)` pointwise.  All nontrivial arithmetic fluctuation is carried by the ordinary Chebyshev Jensen defects across the nested four-adic scales.

## 6. Compatibility with the exact four-adic renewal

PR #325 `L-32412` proves

\[
 G_4(x)=G_4(x/4)+H_4(x),
\]

where

\[
 H_4(x)=\psi(x)-4\psi(x/4)+3R(x)\log4.
\]

Equation (L-33805.5) independently reproduces this identity: subtracting the same formula at `x/4` leaves

\[
 \psi(x)-4\psi(x/4)+3R(x)\log4.
\]

Thus the filtered-Chebyshev representation and the coefficient-one four-adic renewal are exactly the same source in two coordinates.

## 7. Consequence for the proof search

The proof-closing Q=4 energy target may now be stated without generalized-prime notation:

> control the balanced `L^2` Jensen energy of the nested filtered Chebyshev field in (L-33805.6) at polynomial/subexponential scale.

This identity does **not** make that estimate elementary.  A bound strong enough to give RH remains an RH-strength statement.  Its value is structural:

1. all local-Euler generalized-prime growth has been removed exactly;
2. the only arithmetic source is the ordinary Chebyshev function at nested four-adic scales;
3. the deterministic correction is explicit and polylogarithmic;
4. the exact renewal and all-pass descriptions can now be compared directly to classical prime-error/Jensen identities.

## 8. Proof boundary

Closed exactly, subject to review:

- the four-adic prefix convolution;
- cancellation of the full generalized-prime exponential correction;
- the closed formula (L-33805.5);
- the corresponding Jensen-field decomposition;
- exact compatibility with the existing four-adic renewal.

Open:

- any RH-scale mean-square estimate for the filtered Chebyshev Jensen field;
- SQFD or its averaged version;
- the final neutral recurrence;
- RH.
