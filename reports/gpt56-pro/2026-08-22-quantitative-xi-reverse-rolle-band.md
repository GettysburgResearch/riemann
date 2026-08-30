# Research report — quantitative Xi reverse-Rolle band

## Summary

The continuation produces the first explicit positive answer to the
“percentage descent” question in an Xi-specific regime.

For every `c<1`, every fixed `eta>0`, and every natural growing box satisfying

\[
T_N=o\!\left(\sqrt{\frac{\eta N}{\log N}}\right),
\]

the real-zero count of consecutive Xi derivatives satisfies

\[
N_{m-1}(T_N)\ge cN_m(T_N)
\]

uniformly for every `m` in the constant-fraction band
`eta N<m<=N`, once `N` is sufficiently large.  In fact every zero in the
corresponding critical-strip box is real and simple.

The proof uses the positive Fourier kernel directly, through one canonical
one-sided analytic signal at each derivative order.  It does not infer the
claim from a global zero percentage.

## New exact source

\[
\mathscr E_m(z)
=
i^m\int_0^\infty u^m\Phi(u)e^{izu}\,du,
\qquad
\mathscr E_m'=\mathscr E_{m+1}.
\]

This removes the moving scalar companion normalization from the high-order
part of the cascade.

## Uniform concentration

The tilted measures

\[
d\nu_m=M_m^{-1}u^m\Phi(u)\,du
\]

have saddle

\[
w_m=\frac12\log m+O(\log\log m)
\]

and width

\[
\sigma_m\asymp\sqrt{\frac{\log m}{m}}.
\]

Uniform concentration across `eta N<=m<=N` gives the simultaneous cosine/sine
models and the zero-count formula.

## Hostile correction

The previous last-defect theorem treated an integral over only the two vertical
sides as an integer flux.  An open-boundary integral is not an index.  The
correct charge includes the lower horizontal side as well.

## Remaining gate

Only derivative levels below the uniform high band can be defective.  At the
last such level, either a positive residue occurs on the real axis or the
complete exterior boundary carries the missing index.

The continuation therefore supplies real partial progress while preserving the
exact RH boundary.
