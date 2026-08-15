# L-93922 — The hybrid direct row has native `Y_4` deficit below 3457

Claim ID: `L-93922`  
Status: **PROPOSED COMPLETE DIRECT NATIVE-COST THEOREM ON FROZEN SPARSE-DUAL INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-93921`; exact native dual `L-91378`; sparse `Y_4` bounds; elementary Chebyshev bound `J_Lambda(X)<16(log2)sqrt(X)`  
Does not depend on: `J_Lambda(X)-4sqrt(X)`  
RH status: **unproved**

Let

\[
\Delta_X=J_\Lambda(X)-\mathcal H(d_X)
=\langle Y_4,\Omega_X-\Xi_{d_X}\rangle.
\]

By `L-93920.9` and `L-93921.7`,

\[
\Omega_X-\Xi_{d_X}
=(1-\tau_K)\Omega_X
+\tau_K\mathcal D_4v(E_X^I).
\]

The left side is nonnegative by `L-93921`; for an upper bound use the absolute value only on the signed defect:

\[
\Delta_X
\le
(1-\tau_K)J_\Lambda(X)
+\sum_qY_4(q)|\mathcal D_4v_q(E_X^I)|.
\tag{L-93922.1}
\]

## 1. Thinning cost

Since

\[
1-\tau_K<\frac{24}{\sqrt K},
\qquad
K>\frac X{67},
\]

and

\[
J_\Lambda(X)<16(\log2)\sqrt X,
\]

one obtains

\[
\boxed{
(1-\tau_K)J_\Lambda(X)
<384(\log2)\sqrt{67}<3456.
}
\tag{L-93922.2}
\]

Only `log2<1` and `sqrt(67)<9` are used in the final numerical bound.

## 2. Signed mismatch cost

The sparse dual estimate gives, with `L=log(2X)`,

\[
\sum_{q\le X}\frac{Y_4(q)}q
\le3+2L+2L^2.
\]

Using `L-93921.3`,

\[
\sum_qY_4(q)|\mathcal D_4v_q(E_X^I)|
<\frac{171}{4\sqrt K}(3+2L+2L^2).
\tag{L-93922.3}
\]

For `X>=10^12`, `1/sqrt(K)<9/sqrt(X)`. Put `L=log(2X)` and

\[
f(X)=X^{-1/2}(3+2L+2L^2).
\]

Differentiation with respect to `log X` gives

\[
X^{1/2}\frac{df}{d\log X}
=\frac12+3L-L^2<0
\]

throughout this range. Moreover the rational partial sum

\[
\sum_{n=0}^{29}\frac{29^n}{n!}>2\cdot10^{12}
\]

proves `log(2*10^12)<29` without a floating-point logarithm. Consequently

\[
\boxed{
\sum_qY_4(q)|\mathcal D_4v_q(E_X^I)|
<\frac{1539\cdot1743}{4\cdot10^6}<1.
}
\tag{L-93922.4}

## 3. Uniform native deficit

Combining (L-93922.1), (L-93922.2), and (L-93922.4),

\[
\boxed{
0\le J_\Lambda(X)-\mathcal H(d_X)<3457
\qquad(X\ge10^{12}).
}
\tag{L-93922.5}

The priced classes are now only:

```text
one common thinning                 <3456;
one signed retained-cell mismatch      <1.
```

There is no child payment, quantizer collar, terminal comparison, positive omission, auxiliary port, or finite base packet.
