# L-102740 — The outer-ray current factors through the first-order critical scale current

Claim ID: `L-102740`  
Status: **PROVED EXACT DIFFERENTIAL AND POSITIVE-RESOLVENT THEOREM**  
Created: 2026-08-22  
Depends on: PR #715 `L-102500`; `L-102724`, `L-102739`  
RH status: **not assumed**

Let `sigma` be any finite source to which the fixed common mother is applied,
and put

\[
H_\sigma(X)
=
\sum_n\frac{\sigma(n)}{\sqrt n}\Phi_*(X/n).
\]

Let

\[
\mathcal A_\sigma
=
\sum_n\frac{\sigma(n)}{\sqrt n}\delta_{\log n},
\qquad
H^{\rm SHARP}_\sigma(X)
=
\sum_n\frac{\sigma(n)}{\sqrt n}T(X/n),
\]

and define the filtered Lorentz current

\[
\mathcal L_\sigma
=
5JP_2\mathcal A_\sigma
-
JP_2H^{\rm SHARP}_\sigma.
\tag{L-102740.1}
\]

This includes the completion-tangent source, the completion defect, and every
exact regional source of PR #719.

## 1. Exact multiplier factorization

Write

\[
q_2(s)
=(1-\sqrt2\,2^{-s})(1-2^{-s})^2.
\]

The common mother has multiplier

\[
m_\Phi(s)=\frac{2q_2(s)}{s^2(s-1/2)}.
\]

The active SHARP carrier has multiplier

\[
\widehat T(s)=\frac{s+3/2}{s(s-1/2)}.
\]

Since `J` contributes `1/s`, the multiplier of (L-102740.1) is

\[
\begin{aligned}
\frac{q_2(s)}s
\left[
5-\frac{s+3/2}{s(s-1/2)}
\right]
&=
\frac{q_2(s)(s-1)(5s+3/2)}{s^2(s-1/2)}\\
&=
\frac12(s-1)(5s+3/2)m_\Phi(s).
\end{aligned}
\]

Therefore, as logarithmic distributions,

\[
\boxed{
\mathcal L_\sigma
=
\frac12(D-1)(5D+3/2)H_\sigma.
}
\tag{L-102740.2}
\]

This is the differential form of the outer-ray identity in `L-102739`.

## 2. Stable first-order factor

Put

\[
Y_\sigma=(D-1)H_\sigma.
\]

Then

\[
\boxed{
\mathcal L_\sigma
=
\frac52(D+3/10)Y_\sigma.
}
\tag{L-102740.3}
\]

In logarithmic coordinate `u=log X`, every finite source satisfies the causal
boundary condition `Y_sigma(u)=0` for all sufficiently negative `u`. Hence

\[
\boxed{
Y_\sigma(u)
=
\frac25
\int_{-\infty}^{u}
 e^{-3(u-v)/10}
\mathcal L_\sigma(v)\,dv.
}
\tag{L-102740.4}
\]

The resolvent kernel is positive.

## 3. One-sided mass transfer

From (L-102740.4),

\[
(Y_\sigma(u))_-
\le
\frac25
\int_{-\infty}^{u}
 e^{-3(u-v)/10}
(\mathcal L_\sigma(v))_-\,dv.
\]

Fubini gives, for every `U`,

\[
\boxed{
\int_{-\infty}^{U}(Y_\sigma(u))_-\,du
\le
\frac43
\int_{-\infty}^{U}(\mathcal L_\sigma(u))_-\,du.
}
\tag{L-102740.5}
\]

Thus the outer-ray theorem implies the first-order critical-variation theorem
with no loss beyond the fixed factor `4/3`.

## Matrix consequence

The filtered three-ray, radial-SDP, outer-ray and first-order scale-current
formulations are now one chain:

```text
three filtered rays
  -> outer ray w=-8
  -> stable resolvent
  -> first-order critical scale current.
```

The remaining arithmetic difficulty is therefore first-order and one-sided.
The second differential factor introduces no new unstable inverse or critical
mass.