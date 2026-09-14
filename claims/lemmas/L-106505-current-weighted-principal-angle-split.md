# L-106505 — Current-weighted principal-angle split

Claim ID: `L-106505`  
Status: **PROVED EXACT FINITE OPERATOR IDENTITY**  
Created: 2026-08-25  
Depends on: `L-106504`; standard Toeplitz–Hankel identities for finite inner functions  
RH status: **not assumed**

Let a reduced rational unimodular symbol have the inner quotient form

\[
U=\omega B_+\overline{B_-}
=\omega{B_+\over B_-},
\]

where `B_+` and `B_-` are finite upper-half-plane inner functions with no
common factor.  Put

\[
Q_-=P_{K_{B_-}},
\qquad K_{B_-}=H^2\ominus B_-H^2.
\]

For any positive contraction `0<=R<=I` on the positive-frequency Hardy space,
define the weighted principal-angle collision

\[
\boxed{
\mathcal C_R(B_+,B_-)
=\operatorname{tr}
\left(T_{B_+}^*Q_-RQ_-T_{B_+}\right).
}
\tag{L-106505.1}

## 1. Exact Hankel realization

The scalar inner identity

\[
H_{\overline{B_-}}^*H_{\overline{B_-}}=Q_-
\]

and analyticity of `B_+` give

\[
H_U=\omega H_{\overline{B_-}}T_{B_+}.
\]

Therefore

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=\operatorname{tr}(T_{B_+}^*Q_-T_{B_+}).
}
\tag{L-106505.2)

This is the exact principal-angle trace between the numerator inner range and
the denominator bad model space.

## 2. Current/reserve split

Insert `I=R+(I-R)` between the two model projections.  One obtains the exact
identity

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
=\mathcal C_R(B_+,B_-)
+\operatorname{tr}
\left(T_{B_+}^*Q_-(I-R)Q_-T_{B_+}\right).
}
\tag{L-106505.3)

Since `T_(B_+)T_(B_+)^*<=I` and `Q_-(I-R)Q_-` is positive finite rank,
cyclicity gives

\[
\boxed{
\operatorname{tr}
\left(T_{B_+}^*Q_-(I-R)Q_-T_{B_+}\right)
\le\operatorname{tr}_{K_{B_-}}(I-R).
}
\tag{L-106505.4)

Consequently

\[
\boxed{
\|H_U\|_{\mathcal S_2}^2
\le
\mathcal C_R(B_+,B_-)
+\operatorname{tr}_{K_{B_-}}(I-R).
}
\tag{L-106505.5)

No commutation of `R` with the variable all-pass phase is assumed.  The
numerator phase can only reduce the positive reserve trace; all noncommuting
geometry is retained in the single collision `C_R`.

## 3. Saturating Xi current

Choose `R=R^sharp_(K,h)` from `L-106502`.  Equations `L-106503--L-106504`
then give, for the odd endpoint denominator of a degree-`n` truncation,

\[
\boxed{
\|H_{U_{K,\lambda}}\|_{\mathcal S_2}^2
\le
\mathcal C_{K,h,\lambda}
+C_{K,h}
\left(
\mathfrak h_+(p)
+\mathfrak h_+(p^{(K)})
+\lambda(n-K)
\right),
}
\tag{L-106505.6)

where

\[
\mathcal C_{K,h,\lambda}
=\mathcal C_{R^\sharp_{K,h}}(B_+,B_-).
\]

Common-factor reduction only lowers the pole-height reserve.

## 4. Exact boundary

The second term of (L-106505.6) is now source-explicit and separation free.
The remaining conclusion-bearing quantity is one positive weighted
principal-angle trace.  It is not equal to the diagonal source ratio and is
not removed by denominator multiplication.  Any proof of its smallness must
use the actual endpoint numerator/denominator geometry on the same finite
window.
