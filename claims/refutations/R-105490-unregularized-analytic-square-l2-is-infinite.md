# R-105490 — The unregularized analytic-square \(L^2\) gate is infinite

Claim ID: `R-105490`

Status: **BINDING EXACT REFUTATION OF `L-105483.3--L-105483.7`**

Created: 2026-08-26

Depends on: `L-105490--L-105491`, historical `L-105483`, `L-103070--L-103071`

RH status: **unproved**

Historical `L-105483` used

\[
\Omega_A(t)=|P(\tfrac14+it)|^2r_A(t)^4,
\]

where

\[
r_A(t)=
\frac{2(\cosh((\log2)/4)-\cos(t\log2))}
{t^2+1/16}.
\]

## 1. The old weight does not decay

The numerator of \(r_A\) is bounded above and bounded strictly away from zero.
Moreover,

\[
|P(\tfrac14+it)|\asymp (1+t^2)^2,
\qquad
r_A(t)\asymp(1+t^2)^{-1}.
\]

Therefore

\[
\boxed{
\Omega_A(t)\asymp1.
}
\tag{R-105490.1}
\]

Let

\[
Q(t)=\sum_{j=1}^Nq_je^{-it\lambda_j}
\]

be any nonzero finite Dirichlet polynomial with distinct real frequencies.
Its mean square satisfies

\[
\frac1{2T}\int_{-T}^T|Q(t)|^2dt
\longrightarrow
\sum_{j=1}^N|q_j|^2>0.
\tag{R-105490.2}
\]

Combining (R-105490.1) and (R-105490.2),

\[
\boxed{
\int_{\mathbb R}\Omega_A(t)|Q(t)|^2dt=\infty.
}
\tag{R-105490.3}
\]

Thus historical `F1ASQ2_105483` is false for every nonzero finite packet, not
merely unproved.

## 2. What remains valid

The distributional identity

\[
\widehat{e^{-x/4}P(D)J}(t)
=
P(\tfrac14+it)e^{-2it\log2}r_A(t)^2Q(t)
\]

remains valid. Its right side is generally bounded rather than square
integrable, exactly as expected for a compact distribution carrying boundary
atoms.

Ordinary Plancherel may be applied only after the missing resolvent of
`L-105490--L-105491` is inserted. That produces the decaying weight of
`L-105492`.

## 3. Disposition

```text
normal-ordered analytic source square Q             RETAINED EXACT
distributional differential-square identity         RETAINED EXACT
old unregularized Omega_A L2 integral                INFINITE / REFUTED
old F1ASQ2_105483                                    WITHDRAWN
old F1FOURTH105483 -> F1GRAM                         WITHDRAWN
correct bounded-detector weight                      L-105492
correct Beta fourth-moment route                     L-105493
```
