# T-90009 — Endpoint monotonicity is a weighted-Chebyshev lower-barrier gate

Claim ID: `T-90009` (provisional range; allocate before integration)  
Title: The logarithmic derivative of the prime endpoint is exactly a deterministic negative moat minus the weighted Chebyshev fluctuation; eventual monotonicity implies RH  
Status: **PROPOSED COMPLETE EXACT REDUCTION / CONDITIONAL RH THEOREM — MONOTONICITY OPEN**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90004`, `L-90009`, `T-90008`; Landau's one-sign theorem through `T-90008`  
Scope: derivative and integer-decrement gates; no unconditional monotonicity claim

## 1. Logarithmic derivative of the endpoint

Let

\[
 \mathcal D_X=X\frac{d}{dX}.
\]

For a noninteger \(X\), put \(N=\lfloor X\rfloor\), and write

\[
 \ell(m)=\log\operatorname{rad}(m),\qquad
 d(m)=\ell(m)-\ell(m-1).
\tag{T-90009.1}
\]

Define the three finite prefixes

\[
 S_{1/2}(N)=\sum_{m\le N}\sqrt m\,d(m),
\]

\[
 S_1(N)=\sum_{m\le N}m\,d(m),
\]

and

\[
 \vartheta_{1/2}(N)
 =\sum_{p\le N}\frac{\log p}{\sqrt p}.
\tag{T-90009.2}
\]

The parabolic seed satisfies the exact identity

\[
\boxed{
 \mathcal D_X b_X(m)
 =2\sqrt m-\frac{2m}{\sqrt X}
 =2m\left(m^{-1/2}-X^{-1/2}\right).
}
\tag{T-90009.3}
\]

Using the radical-switching formula of `L-90004` and differentiating the prime
ramp gives

\[
\boxed{
 \mathcal D_X A(X)
 =
 2S_{1/2}(N)
 -\frac{2}{\sqrt X}S_1(N)
 -\vartheta_{1/2}(N).
}
\tag{T-90009.4}
\]

This is exact on every open interval \((N,N+1)\).  In particular, on one such
interval the derivative is affine in \(X^{-1/2}\), so its maximum occurs at one
of the two endpoint limits.

Equation (T-90009.3) also shows that the derivative seed is precisely the
square-root hinge multiplied by its node size.  This connects the gate to the
SHARP/carry family, but the extra node factor prevents any termwise import of
SHARP positivity.

## 2. Exact separation of the zero-sensitive coordinate

Let

\[
 E_{1/2}(X)
 =\psi_{1/2}(X)-2\sqrt X,
\qquad
 \psi_{1/2}(X)
 =\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}.
\tag{T-90009.5}
\]

`L-90009` proves the exact identity

\[
\boxed{
 \mathcal D_X A(X)
 =
 \mathcal D_X\mathfrak M(X)-E_{1/2}(X),
}
\tag{T-90009.6}
\]

where every original zeta-zero pole has canceled from
\(\mathcal D_X\mathfrak M\).  Unconditionally,

\[
\boxed{
 \mathcal D_X\mathfrak M(X)
 =
 a\log X+\mu_1+o(1),
\qquad
 a=\frac{1+\zeta(1/2)}2
 =-0.23017725440479340644\ldots.
}
\tag{T-90009.7}
\]

Therefore endpoint monotonicity is exactly the lower-barrier inequality

\[
\boxed{
 \mathcal D_X A(X)\le0
 \iff
 E_{1/2}(X)\ge\mathcal D_X\mathfrak M(X).
}
\tag{T-90009.8}
\]

At leading order the barrier is

\[
\boxed{
 \psi_{1/2}(X)-2\sqrt X
 \ge
 -0.23017725440479340644\ldots\,\log X+O(1).
}
\tag{T-90009.9}
\]

The right side is deterministic and eventually negative.  The entire
RH-sensitive content is the one-sided lower envelope of the classical weighted
Chebyshev fluctuation.

## 3. Eventual monotonicity implies RH

Assume

\[
 \mathcal D_X A(X)\le0
\tag{T-90009.10}
\]

for every sufficiently large noninteger \(X\).  Then \(A\) is eventually
nonincreasing.  A real nonincreasing function can cross zero at most once, so it
is eventually one-signed.  `T-90008` then gives RH.

Thus

\[
\boxed{
 \mathcal D_X A(X)\le0\text{ eventually}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-90009.11}
\]

The same conclusion follows from eventual strict decrease.

This is a genuine strengthening of the endpoint sign gate, not a proof of it.
No converse from RH is asserted.

## 4. A sufficient zero-sum estimate

From (T-90009.7),

\[
 E_{1/2}(X)=o(\log X)
\tag{T-90009.12}
\]

implies

\[
 \mathcal D_X A(X)
 =(a+o(1))\log X<0
\]

eventually.  Hence

\[
\boxed{
 E_{1/2}(X)=o(\log X)
 \Longrightarrow
 \mathcal D_XA(X)<0\text{ eventually}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-90009.13}
\]

The first implication supplies the exact amount of cancellation required in
the weighted Chebyshev explicit formula.  The standard pointwise consequence
of RH,

\[
 E_{1/2}(X)=O(\log^2X),
\]

does not establish (T-90009.12) or the lower barrier (T-90009.9).  Thus this
route must not be labeled a consequence of RH without an additional
Montgomery-class zero-sum estimate.

## 5. Exact integer decrement

Let \(M\ge2\), \(X=M+1\), and put

\[
 L_M=\log\left(1+\frac1M\right).
\]

At every old node \(m\le M\),

\[
 b_{M+1}(m)-b_M(m)
 =
 2\sqrt m\,L_M
 +4m\left((M+1)^{-1/2}-M^{-1/2}\right).
\tag{T-90009.14}
\]

The new endpoint contributes zero, and a prime \(M+1\), if present, also has
zero ramp weight.  Therefore

\[
\boxed{
\begin{aligned}
 A(M+1)-A(M)
={}&L_M\bigl(2S_{1/2}(M)-\vartheta_{1/2}(M)\bigr)\\
&+4\left((M+1)^{-1/2}-M^{-1/2}\right)S_1(M).
\end{aligned}
}
\tag{T-90009.15}
\]

This is an exact finite arithmetic inequality involving only radical-prefix
moments and the prime half-Chebyshev prefix.

Consequently,

\[
\boxed{
 A(M+1)\le A(M)\text{ eventually}
 \Longrightarrow\mathrm{RH}.
}
\tag{T-90009.16}
\]

Indeed an eventually nonincreasing real sequence is eventually one-signed, and
the integer form of `T-90008` applies.

## 6. Finite reconnaissance

`X-90009` evaluates (T-90009.4) and (T-90009.15) from one sieve.

Through the retained endpoint \(5\,000\,000\):

```text
A(M+1)-A(M) < 0 at every tested M;
D_X A(X) < 0 throughout every interval (N,N+1).
```

The largest integer increment was

```text
-6.270389820674203e-7 at M=4,409,886,
```

and the largest interval derivative maximum was

```text
-0.0064383486728724695 on (222,223).
```

This is discovery evidence only.  The margins shrink at large endpoints, and
neither table is extrapolated.

## 7. Relation to the prime-power moat

The monotonicity experiment is now correctly decomposed as

```text
unconditional:
    D_X M(X) = a log X + O(1), a<0;

RH-sensitive:
    E_1/2(X)=psi_1/2(X)-2sqrt(X);

open inequality:
    E_1/2(X) >= D_X M(X).
```

This explains why the finite sign is so stable while remaining conclusion
producing.  The prime-square moat creates a growing negative allowance, but the
weighted Chebyshev coordinate retains a first-order \(1/(\rho-1/2)\) zero
response rather than the absolutely summable second-order response of \(A\)
itself.

A generic absolute-value estimate therefore loses exactly the cancellation
needed for the gate.

## 8. Proof boundary

Closed exactly, subject to review:

1. the finite derivative formula;
2. the square-root-hinge derivative identity;
3. isolation of the weighted Chebyshev fluctuation;
4. the explicit asymptotic lower barrier;
5. eventual real monotonicity implies RH;
6. the sufficient \(E_{1/2}=o(\log X)\) condition;
7. the exact integer decrement;
8. eventual integer monotonicity implies RH.

Open:

1. the lower barrier (T-90009.9);
2. eventual real or integer monotonicity;
3. whether RH alone implies either monotonicity statement;
4. RH.
