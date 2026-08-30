# L-107403 — The frozen Riemann–Siegel companion scale is exactly adapted at the central source carrier

Claim ID: `L-107403`  
Programme aliases: `XI90.CENTRAL_SCALE_MATCH`, `XI.MESOSCOPIC_CARRIER_ADAPTATION`  
Status: **PROVED EXACT FROZEN-CARRIER IDENTITY AND SPREAD DECOMPOSITION**  
Created: 2026-08-30  
Depends on: `L-106620`, `L-106710`  
Programme issue: #744  
RH status: **not assumed**

On a mesoscopic window \(I_j\), `L-106620` freezes

\[
\lambda_j=\omega(t_j)^{-1},
\]

where \(\omega=\vartheta'\) is the Riemann–Siegel carrier frequency.

The endpoint Wronskian is a product of two carrier-bearing factors. Under the
frozen linear carrier, its central convolution frequency is

\[
\boxed{\xi_j=2\omega(t_j).}
\tag{L-107403.1}
\]

Consequently

\[
\boxed{
\lambda_j=\frac2{\xi_j}.
}
\tag{L-107403.2}
\]

Thus the physical constant scale is exactly the Fourier-adapted scale at the
central carrier; the mismatch is only the spread away from \(\xi_j\), not a
factor-of-two normalization error.

For general frequency \(\xi>0\), `L-106710.6` gives

\[
\boxed{
a_{K,\lambda_j}(\xi)
=
\left(1-\frac{\xi^2}{\xi_j^2}\right)a_{K,0}(\xi)
+
\frac4{\xi_j^2}b_K(\xi).
}
\tag{L-107403.3}
\]

At \(\xi=\xi_j\), the first term vanishes and the source constant of
`L-107401` applies. The complete off-central debt is therefore the explicit
signed spread moment

\[
\boxed{
\mathfrak S_{K,j}
=
\int
\left(1-\frac{\xi^2}{\xi_j^2}\right)
a_{K,0}(\xi)\,d\xi
}
\tag{L-107403.4}
\]

in the exact local source normalization, together with the variable-carrier
error already bounded coefficientwise in `L-106620`.

## Scope

The identity isolates the correct physical spread term. It does not prove that
the Riemann–Siegel source packet is sufficiently concentrated in the metric
needed by the all-pass/source-Pick determinant.
