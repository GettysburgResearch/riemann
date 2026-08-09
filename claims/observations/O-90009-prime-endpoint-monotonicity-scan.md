# O-90009 — Prime endpoint monotonicity and moat reconnaissance through five million

Claim ID: `O-90009` (provisional range; allocate before integration)  
Status: **FINITE RECONNAISSANCE + EXACT FORMULA REGRESSION; NO COFINAL SIGN CLAIM**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90009`, `T-90009`  
Scope: retained computation only

## 1. Objects checked

For the prime endpoint scalar

\[
 A(X)=\sum_{p\le X}(\log p)r_X(p),
\]

the checker evaluates:

```text
the exact radical-switching formula for A;
the full prime-power deficit Delta_Lambda;
the zero-insensitive moat M=A-Delta_Lambda;
the logarithmic derivatives D A and D M;
the exact integer decrement A(N+1)-A(N).
```

All formulas are computed from one prime sieve and the prefix moments of

\[
 d(m)=\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1).
\]

Small endpoints are independently recomputed by the unsummed radical-switching
formula.

## 2. Monotonicity observation

For every integer

\[
 2\le N<5\,000\,000,
\]

the retained scan found

\[
 A(N+1)-A(N)<0.
\]

The largest increment was

\[
 -6.270389820674203\cdot10^{-7}
\]

at

\[
 N=4\,409\,886.
\]

For a real endpoint \(X\in(N,N+1)\), `T-90009` gives

\[
 \mathcal D_XA(X)
 =2S_{1/2}(N)-2X^{-1/2}S_1(N)-\vartheta_{1/2}(N),
\]

which is affine in \(X^{-1/2}\).  Checking both endpoint limits of every
interval therefore checks the whole interval.  No nonnegative derivative was
found through \(X=5\,000\,000\).  The largest interval maximum was

\[
 -0.0064383486728724695
\]

on \((222,223)\).

## 3. Moat samples

Representative rows are:

```text
X          A(X)          Delta_Lambda(X)      M(X)          D M(X)
100000    -12.5490751       34.6658448       -47.2149199    -5.0725239
1000000   -18.7364392       40.8473910       -59.5838302    -5.6891463
5000000   -23.8551935       45.1895689       -69.0447624    -6.1069942
```

The moat is already much larger in magnitude than the RH-sensitive complete
deficit at these endpoints.  Its normalized ratios are still far from the
asymptotic constants, so the table is not used to estimate the Laurent
coefficients.

## 4. Interpretation

The scan originally suggested a direct monotonicity conjecture.  `L-90009`
shows why this is not a routine positivity statement:

\[
 \mathcal D_XA
 =\mathcal D_X\mathfrak M
  -(\psi_{1/2}-2\sqrt X).
\]

The first term is unconditionally negative with linear logarithmic drift.  The
second term is the first-order zero-sensitive weighted Chebyshev fluctuation.
Thus the finite monotonicity is consistent with a strong zero-sum estimate but
cannot be promoted from the size of the deterministic moat alone.

## 5. Boundary

The retained finite statements authenticate no endpoint beyond five million.
In particular they do not prove:

```text
eventual monotonicity;
the weighted-Chebyshev lower barrier;
RH.
```

Replay: `experiments/X-90009-prime-power-moat/verify.py`.
