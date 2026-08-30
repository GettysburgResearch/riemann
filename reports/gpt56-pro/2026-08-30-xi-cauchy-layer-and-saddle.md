# Xi Cauchy-layer and saddle checkpoint

## Scientific advance

This checkpoint closes the positive-frequency saddle target left by PR #767
and replaces the previous depth/separation counting interface by an exact
Cauchy-screened curvature measure.

The key identity is

\[
\mathfrak R_I(f)
=
\sum_c(\operatorname{ord}_c f'-1)
+
\frac2\pi\lim_{\varepsilon\downarrow0}
\int
\frac{\varepsilon(Q_f)_-}
     {(f'/f)^2+\varepsilon^2}.
\]

The scale in the denominator is intrinsic.  It automatically gives unit
weight to an upward crossing, zero to a downward crossing and half weight to
an even tangency.

For Xi derivatives, the explicit standard kernel gives a unique logarithmic
saddle and natural width \(a_m\asymp\sqrt{\log m/m}\).  The weighted measure
\(u^m\Phi_\Xi(u)du\) has Gaussian tails at that width, so the general
concentration theorem on PR #767 yields simple real zeros in the full
critical strip up to height \(c\sqrt{m/\log m}\).

## What did not close

The fixed-order five-rung integral

\[
\sum_{k=0}^4
\lim_{\varepsilon\downarrow0}
\frac1\pi\int_T^{2T}
\frac{\varepsilon(Q_{\Xi^{(k)}})_-}
     {(\Xi^{(k+1)}/\Xi^{(k)})^2+\varepsilon^2}
\]

is not bounded here.  A bound below \(97/2000\) of the zeta zero count,
together with the pinned \(R_5/N>997/1000\) input and the regularization
ledger, would prove more than \(90\%\).

The packet therefore makes genuine unconditional progress on the high-order
entry and an exact improvement to the low-order interface, but it does not
establish \(90\%\), density one or RH.
