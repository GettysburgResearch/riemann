# L-92003 — The third-order safe-Xi curvature is eventually positive

Claim ID: `L-92003`  
Status: **PROPOSED COMPLETE EFFECTIVE ASYMPTOTIC THEOREM — REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-92002`; Stirling with remainder; absolute Euler convergence  
RH status: **unproved**

## 1. Curvature quantity

Retain

\[
 F(x)=\frac{\xi'}{\xi}\left(\frac12+x\right)
 \qquad(x>1/2)
\]

and

\[
 \mathfrak T_3(x)
 =x^2F F''-2x^2(F')^2+xFF'+F^2.
 \tag{L-92003.1}
\]

By `L-92002`, positivity of this scalar is exactly the missing three-node
Caratheodory curvature.

## 2. Safe-axis asymptotics

From the completed logarithmic derivative,

\[
 F(x)
 =\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\psi(s/2)+\frac{\zeta'}{\zeta}(s),
 \qquad s=x+\frac12,
\]

Stirling's expansion with remainder and the absolutely convergent Euler series
give, effectively,

\[
 \boxed{
 F(x)=\frac12\log\frac{x}{2\pi}+O(x^{-1}),
 }
 \tag{L-92003.2}
\]

\[
 \boxed{
 F'(x)=\frac1{2x}+O(x^{-2}),
 }
 \tag{L-92003.3}
\]

and

\[
 \boxed{
 F''(x)=-\frac1{2x^2}+O(x^{-3}).
 }
 \tag{L-92003.4}
\]

The prime-power contribution and each of its first two derivatives are in fact
exponentially small in `x`; the displayed polynomial errors come from the
archimedean expansion.

## 3. Cancellation of the first derivative scale

The combination appearing in (L-92003.1) has a useful cancellation:

\[
 x^2F''+xF'=O(x^{-1}).
 \tag{L-92003.5}
\]

Also

\[
 2x^2(F')^2=\frac12+O(x^{-1}).
 \tag{L-92003.6}
\]

Consequently

\[
\boxed{
 \mathfrak T_3(x)
 =F(x)^2-\frac12
 +O\left(\frac{F(x)+1}{x}\right).
}
\tag{L-92003.7}
\]

Since `F(x)` tends to infinity logarithmically, the right-hand side is
strictly positive for all sufficiently large `x`.

Thus there is an effective constant `X_0` such that

\[
 \boxed{
 \mathfrak T_3(x)>0
 \qquad(x\ge X_0).
 }
 \tag{L-92003.8}
\]

No zero hypothesis enters.

## 4. Companion curvature

The already-closed companion numerator is

\[
 \mathfrak U_3(x)=x^2F''+xF'-F.
\]

The same asymptotics give

\[
 \boxed{
 \mathfrak U_3(x)=-F(x)+O(x^{-1})<0
 }
 \tag{L-92003.9}
\]

for large `x`, consistent with the global orbitwise theorem `L-92001`.

## 5. Exact remaining compact task

The order-three problem has therefore become compact:

```text
prove T_3(x)>=0 on the finite interval (1/2,X_0].
```

Every term is a real safe-Euler quantity.  A valid completion may use:

1. directed interval evaluation of the completed logarithmic derivative and
   its first two derivatives;
2. a theta-kernel inequality implying reciprocal concavity;
3. a direct positive factorization of the scalar numerator.

A floating-point grid is diagnostic only and is not accepted as the theorem.

## 6. Exact boundary

```text
large-x asymptotic expansion                    STANDARD EFFECTIVE
large-x third-order curvature positivity        PROPOSED COMPLETE
remaining domain                                COMPACT SAFE REAL INTERVAL
compact directed sign                           OPEN
all three-node actual-Xi matrices               OPEN ONLY THROUGH COMPACT SIGN
Riemann Hypothesis                              UNPROVED
```
