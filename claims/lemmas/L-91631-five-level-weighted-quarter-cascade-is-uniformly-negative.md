# L-91631 — The five-level weighted quarter cascade is uniformly negative on the complete reset window

Claim ID: `L-91631`  
Status: **PROVED DIRECTED-EXACT SCALAR THEOREM — PHYSICAL ONE-USE REALIZATION STILL OPEN**  
Created: 2026-08-13  
Depends on: exact Möbius and von-Mangoldt prefix identities; `X-91631`  
RH status: **unproved**

## 1. The arithmetic score defect

For `x>=1` put `n=floor(x)` and define

\[
 A(n)=\sum_{m\le n}\frac{\mu(m)}m,
 \qquad
 B(n)=\sum_{m\le n}\frac{\mu(m)}{\sqrt m},
\]

\[
 C(n)=\sum_{m\le n}\frac{\Lambda(m)}{\sqrt m},
 \qquad
 E(n)=\sum_{m\le n}\frac{\Lambda(m)\log m}{\sqrt m}.
\]

The native declared-score minus literal component-entropy defect is

\[
 \boxed{
 D(x)=5\sqrt x\,A(n)-3B(n)-\log x\,C(n)+E(n).
 }
 \tag{L-91631.1}
\]

Equivalently, if

\[
 \Sigma(x)=\sum_{m\le x}\frac{\mu(m)}{\sqrt m}
 \left(5\sqrt{x/m}-3\right)
\]

and

\[
 \mathcal P(x)=\sum_{m\le x}\frac{\Lambda(m)}{\sqrt m}
 \log\frac xm,
\]

then

\[
 \boxed{D(x)=\Sigma(x)-\mathcal P(x).}
 \tag{L-91631.2}
\]

## 2. Five-level quarter cascade

Define

\[
 \boxed{
 \mathcal Q_4D(x)
 =\sum_{j=0}^{4}2^{-j}D(4^jx).
 }
 \tag{L-91631.3}
\]

The theorem is

\[
 \boxed{
 \mathcal Q_4D(x)<0
 \qquad(1\le x\le67).
 }
 \tag{L-91631.4}
\]

The retained certificate proves the stronger uniform bound

\[
 \boxed{
 \mathcal Q_4D(x)<-2.1118392176757
 \qquad(1\le x\le67).
 }
 \tag{L-91631.5}
\]

The least negative location is the left endpoint `x=1`, with active prefix tuple

\[
 (\lfloor x\rfloor,\lfloor4x\rfloor,
   \lfloor16x\rfloor,\lfloor64x\rfloor,
   \lfloor256x\rfloor)
 =(1,4,16,64,256).
\]

## 3. Finite-cell reduction

The common activation lattice is `4^-4 Z`. On every open cell

\[
 \frac{k}{256}<x<\frac{k+1}{256},
\]

all five floor values are fixed. Therefore

\[
 \boxed{
 \mathcal Q_4D(x)
 =\alpha_k\sqrt x+\beta_k\log x+\gamma_k
 }
 \tag{L-91631.6}
\]

with coefficients determined by exact finite arithmetic prefixes.

The logarithmic coefficient is

\[
 \beta_k
 =-\sum_{j=0}^{4}2^{-j}
 C\!\left(\lfloor4^jx\rfloor\right),
\]

and the directed replay proves

\[
 \boxed{\beta_k<0}
 \tag{L-91631.7}
\]

on all `16896` open cells.

For a function

\[
 f(x)=\alpha\sqrt x+\beta\log x+\gamma,
 \qquad\beta<0,
\]

any interior critical point satisfies `alpha>0` and

\[
 f''(x)=-\frac{\beta}{2x^2}>0.
\]

Thus every interior critical point is a minimum. The maximum on a closed cell is attained at a one-sided endpoint. It is therefore sufficient to certify both one-sided endpoint values on every common cell and every activated knot separately.

## 4. Directed exact replay

`X-91631` uses only standard-library integer and rational arithmetic:

```text
Möbius and prime-power prefixes                  exact integers/rationals
square roots                                     integer-isqrt enclosures
logarithms                                       atanh series + explicit positive tail
fixed-point products and quotients               outward rounded
open-cell one-sided endpoints                    all checked
activation knots                                 all checked separately
```

The retained verdict is

```text
PASS_WEIGHTED_QUARTER_CASCADE_K4_ENDPOINT_CERTIFICATE
checks:                       50689
common cells:                 16896
cells with beta >= 0:         0
largest certified upper bound -2.111839217675784308
```

The proof is finite and reproducible; no floating-point sign decision enters.

## 5. What this closes

The scalar score obstruction on the complete factor-67 reset window is not merely negative on average. Five successive quarter scales, with weights

\[
 1,\frac12,\frac14,\frac18,\frac1{16},
\]

produce a uniform negative moat.

This is substantially stronger than the failed one-image inequalities recorded earlier: the fifth-level cascade creates enough accumulated arithmetic entropy to dominate the declared score at every quotient in the full window.

## 6. Exact remaining interface

The theorem is scalar. It does not by itself construct a physical positive row packet whose one-use ordinary and radix-four capacities realize the five terms of (L-91631.3).

The remaining theorem must prove that the weights `2^-j` arise from one positive factor-four endpoint/affine cascade without duplicating a physical target column, and that its literal entropy score is exactly the weighted sum in (L-91631.3), up to already-paid positive collars.

```text
five-level weighted scalar sign                         PROVED
uniform negative moat                                   DIRECTED EXACT
one-use positive physical factor-four realization       OPEN / LOAD BEARING
native factor-54 loss recurrence                         NOT YET CLOSED
Riemann Hypothesis                                       UNPROVEN
```
