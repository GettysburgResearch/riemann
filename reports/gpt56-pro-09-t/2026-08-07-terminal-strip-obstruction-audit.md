# Terminal strip-obstruction audit

Agent: `gpt56-pro-09-t`  
Date: 2026-08-07  
Repository target: `gfreund123/riemann`, PR #202  
Frozen branch head inspected: `835828fe0fdb96ac6f0e66d6b1b16d49de2645f7`

## Verdict

The affine hybrid proposal cannot be completed from its declared high-frequency
profile estimates. `R-19846/T-19814` already prove abstractly that the final
affine gate excludes every off-line Xi-cardinal direction and therefore directly
implies RH. `L-19866` makes the obstruction quantitative: one fixed off-line
quartet creates an exponentially amplified indefinite two-mode Fourier block,
with a negative determinant independent of support phase.

Accordingly, none of the following can close the final gate:

- Riemann--von Mangoldt smooth density;
- high-ordinate support averaging;
- Bessel or Airy endpoint estimates;
- periodization-fold bounds;
- subexponential source conditioning;
- a subexponential scalar regularization.

A valid completion needs a genuinely strip-sensitive theorem at the same
exponential scale. The other active full-proposal routes encode the same object:

- Brownian variance saturation;
- fixed-ratio Mertens shell energy;
- balanced Type-II contraction;
- theta/Volterra boundary-flux positivity;
- affine central-cardinal exclusion.

Each exact final gate is currently unproved and RH-bearing. No route in the
repository presently supplies the missing strip-sensitive sign without assuming
an equivalent statement.

## New exact theorem

See `claims/lemmas/L-19866-offline-quartet-two-mode-exponential-moat.md`.

The key identities are

\[
\widehat c_{k,L}(z)
=\frac{2\sqrt2(-1)^kz\sin(zL/2)}
       {\sqrt L(z^2-(2\pi k/L)^2)},
\]

and

\[
\det\operatorname{Re}(uu^T)
=-\bigl[\operatorname{Im}(u_1\overline{u_2})\bigr]^2.
\]

For an off-line zero `Omega=gamma+i delta`, two mode frequencies tending to
distinct positive limits give

\[
\lambda_{\min}(M_{\Omega,L})
\le -c_{\Omega,a,b}\frac{e^{|\delta|L}}L.
\]

This rules out phase selection and every subexponential central-error budget.

## Status boundary

```text
T-19813 full proposal:             GAPS/BLOCKED
complete affine gate:             RH-BEARING / UNPROVED
new two-mode obstruction L-19866: PROVED
accepted proof of RH:             NO
```

The GitHub contents connector was unavailable during the final write attempt;
this bundle is a git-ready preservation of the new theorem and report.
