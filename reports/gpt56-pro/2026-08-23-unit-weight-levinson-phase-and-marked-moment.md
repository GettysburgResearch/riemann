# Unit-weight Levinson phase and marked-moment continuation

## Main advance

The critical-value amplitudes are no longer an unavoidable interface. The
adaptive weight

\[
(f^2+\lambda^2f'^2)^{-1/2}
\]

equals `1/|f|` at every critical point and therefore turns the weighted
total-variation identity into an exact **unweighted** good-minus-wrong count.

This produces

\[
G-W
=
\Delta\arg(f-i\lambda f')/\pi+O(1)
\]

uniformly in `lambda`.

For `f=Xi''`, the parameter may be set to `a/log T`, so the complete
fixed-order reverse-Rolle count is encoded by the standard mollifiable
combination

\[
\xi''+\frac{a}{\log T}\xi'''.
\]

The alternative two-moment route uses the exact signed weighted variation and
one discrete second moment. That second moment is a thin-strip contour of

\[
m^2\Xi''^2\,\Xi''''/\Xi'''.
\]

## Why this is stronger than T104580

`AMPREG104580` required a coefficient-of-variation estimate for the critical
amplitudes. `T-104590` offers two routes which do not require that premise:

1. count directly through phase;
2. use only a signed first moment and one marked second moment.

## Honest boundary

Neither the required positive phase drift nor the marked two-moment inequality
has been proved. The work converts both into standard fixed-order analytic
objects and preserves Conrey's `alpha_3` input as load bearing.

RH remains unproved.
