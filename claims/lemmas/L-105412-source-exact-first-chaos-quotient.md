# L-105412 — The Wick quotient is the source-exact F1 Lefschetz quotient

Claim ID: `L-105412`

Status: **PROVED EXACT SOURCE DECOMPOSITION AND ONE-SIDED TRANSFER**

Freeze PR #719 at the declared head. For one labelled prime put

\[
x=p^{-1/2}U_p,
\qquad c=1-\tau.
\]

The local completion factor is

\[
(1+cx)(1-x)=1-\tau x-(1-\tau)x^2,
\]

so

\[
\boxed{
-\partial_\tau[(1+cx)(1-x)]=x-x^2.
}
\tag{L-105412.1}
\]

The degree-one tangent coefficient is exactly `+x`, independently of `tau`.
The second labelled `67` stays separate. PR #719 `L-102741` moves the complete
gauge-covariant first chaos once and defines the exact degree-at-least-two Wick
remainder; `L-102742` factors it as a continuous root-free second-chaos square.

Transport this source split through the two F1 primitive kernels:

\[
A_\tau=A^{[1]}+\widetilde A_\tau,
\qquad
B_\tau=B^{[1]}+\widetilde B_\tau.
\tag{L-105412.2}
\]

Put

\[
\widetilde L_\tau=4\widetilde A_\tau-\widetilde B_\tau,
\qquad
\widetilde J_\tau=\widetilde A_\tau+192\widetilde B_\tau,
\]

and

\[
\boxed{
\widetilde Q_\tau
=\widetilde L_\tau^2+\frac{\widetilde J_\tau^2}{48}
=\frac{769}{2}
\left(\frac{\widetilde A_\tau^2}{24}
      +2\widetilde B_\tau^2\right).
}
\tag{L-105412.3}
\]

## Integrated defect orientation

The path runs from the squared source to the native source and

\[
\Sigma_\tau=-\partial_\tau E_\tau.
\]

Hence the native-minus-completion outer current is

\[
\mathcal L_{\rm def}(X)
=-\int_0^1L_\tau(X)d\tau.
\tag{L-105412.4}
\]

Its first-chaos term is exactly the positive packet of PR #719 `L-102737`:

\[
\mathcal P_L(X)
=-\int_0^1L^{[1]}(X)d\tau
=+\kappa_0\frac{\sqrt X}{\log X}
+O\!\left(\frac{\sqrt X}{\log^2X}\right).
\tag{L-105412.5}
\]

Thus `mathcal P_L(X)>=0` for all sufficiently large `X`. Writing

\[
\widetilde{\mathcal L}(X)
=-\int_0^1\widetilde L_\tau(X)d\tau,
\]

we get the coefficient-one favorable-carrier return

\[
\boxed{
(\mathcal L_{\rm def}(X))_-
\le |\widetilde{\mathcal L}(X)|.
}
\tag{L-105412.6}
\]

Jensen in `tau` and (L-105412.3) give

\[
|\widetilde{\mathcal L}(X)|^2
\le\int_0^1\widetilde Q_\tau(X)d\tau.
\tag{L-105412.7}
\]

For `I_T=[T,T+1]`, Cauchy therefore yields

\[
\boxed{
\int_{I_T}(\mathcal L_{\rm def}(e^u))_-du
\le
\left[
\int_{I_T}\int_0^1
\widetilde Q_\tau(e^u)d\tau du
\right]^{1/2}.
}
\tag{L-105412.8}
\]

The correct cofinal theorem is consequently a physical restriction bound for
the root-free Wick/Hodge quotient, not packing of the unquotiented Hodge
energy.
