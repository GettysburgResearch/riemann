# R-102000 — The positive cubic B-spline does not inherit the zero-moment Type-I decay

Claim ID: `R-102000`
Status: **PROVED EXACT SCOPE REFUTATION**
Created: 2026-08-21
Depends on: `L-102000`; PR #685 `L-100310--L-100311`
RH status: **not assumed**

The positive compact kernel `L-102000` and the signed extra-notch kernel of `L-100310` solve different analytic problems and cannot be interchanged.

For the positive cubic B-spline,

\[
\widehat{\mathcal K}_{a,3}(1/2)
=192(\log a)(1-a^{-1/2})(\sqrt a-1)(a-1)>0.
\tag{R-102000.1}
\]

Let

\[
\mathcal L_{\mathcal K}(Y)=\sum_{m\ge1}m^{-1/2}\mathcal K_{a,3}(Y/m).
\]

Ordinary Euler summation, or the same trapezoidal expansion used in `L-100310` without a zero continuous moment, gives

\[
\boxed{
\mathcal L_{\mathcal K}(Y)
=\widehat{\mathcal K}_{a,3}(1/2)\sqrt Y+O_{a}(Y^{-3/2}).
}
\tag{R-102000.2}
\]

Thus the Type-I contribution in the Vaughan decomposition is not power-decaying. If \(U=\lfloor X^{1/3}\rfloor\), the analogue of the `L-100311` Type-I term contains the explicit main piece

\[
\boxed{
-\widehat{\mathcal K}_{a,3}(1/2)\sqrt X
\left(\sum_{n\le U}\frac{\mu(n)}n\right)^2,
}
\tag{R-102000.3}
\]

plus a genuinely decaying remainder.

The previously proposed composition

```text
L-100310 Type-I decay
+ L-102001 parabolic Vaughan rewrite
+ L-102000 positive B-spline detector
-> RH
```

is therefore invalid: the proved Type-I decay belongs to a different signed zero-moment kernel.

## Source firewall

A second mismatch must remain visible. `L-102000` is written on the duplicate-67 source

\[
\beta=(\delta_1-\delta_{67})*\mu,
\]

whereas `L-100311/L-102001` use ordinary \(\mu\). The identity

\[
\mathcal W_\beta=(I-67^{-1/2}S_{67})\mathcal W_\mu
\]

is exact for any fixed kernel, but negative-mass control does not pass from one side to the other for free. The positive inverse works in the direction

\[
\mathcal W_\mu
=\sum_{j\ge0}67^{-j/2}S_{67^j}\mathcal W_\beta,
\]

so a future composition must state precisely which source owns the conclusion-facing estimate.

## Binding consequence

Retain:

```text
positive compact B-spline kernel        PROVED
Mellin noncancellation                   PROVED
large-divisor Vaughan identity           PROVED
parabolic divisor geometry               PROVED
```

Reject:

```text
positive B-spline inherits L-100310 Type-I decay   FALSE
ordinary-mu negative mass transfers to beta freely FALSE
```

The corrected route must either:

1. keep the signed zero-moment kernel through the Vaughan argument; or
2. explicitly subtract/pay the nonzero B-spline half-order main term before invoking the detector.