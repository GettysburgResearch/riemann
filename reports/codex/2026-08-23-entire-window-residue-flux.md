# Entire-window critical-residue flux

## Executive result

The finite-polynomial checkpoint T-105100 computed a global second-residue
ledger but left height localization open. L-105101 supplies the direct
entire-function fixed-window identity.

For

\[
Q_F(z)=\frac{F(z)^2}{F'(z)F''(z)}
\]

and a regular counterclockwise rectangle
\(\Omega_{T,\eta}=\{|\Re z|<T,\ |\Im z|<\eta\}\),

\[
M_{2,F}(T)
=\frac1{2\pi i}\int_{\partial\Omega_{T,\eta}}Q_F(z)\,dz
-C_F(T,\eta)-D_F(T,\eta).
\]

The two corrections are exact: \(C_F\) collects algebraic squared residues at
nonreal \(F'\)-zeros and \(D_F\) collects residues at \(F''\)-zeros. Schwarz
reflection and parity reduce the complete four-edge charge to

\[
\frac2\pi\left[
\int_0^\eta\Re Q_F(T+iy)\,dy
-\int_0^T\Im Q_F(x+i\eta)\,dx
\right].
\]

## Advance and boundary

For \(F=\Xi^{(k-1)}\), \(k\ge1\), this gives the exact height-truncated second
moment from the draft PR #720 programme at any window satisfying the explicit
simplicity and boundary hypotheses. It is self-contained at fixed
\((T,\eta)\) and uses no polynomial or canonical-product exhaustion.

This is not a transport of the global \(V_2,V_4\) ledger. The price of the
direct route is an unevaluated boundary charge plus nonreal and
adjacent-derivative corrections. Quantitative control along an admissible
height/strip sequence, Xi simplicity and common-zero handling, RCMV104530,
and RH remain open.

The individual \(F'\)-pole residue was already in draft PR #720 L-104523.3.
The new content is the complete finite-rectangle closure, including every
\(F''\)-pole, the real/nonreal/debt split, and the orientation-explicit
two-edge reduction.

## Exact hostile replay

The standard-library replay uses rational and Gaussian-rational arithmetic.
It checks:

- narrow and wide real cubic windows;
- an asymmetric quartic partial window;
- a nonreal critical pair, distinguishing algebraic \(1/6\) from absolute
  \(5/18\);
- both numerator-removable residue cases;
- strict finite-segment boundary membership;
- counterclockwise, reversed, and parity-paired edge signs;
- incomplete, duplicate, wrong-kind, and nonsimple root manifests;
- an independent \(V_2,V_4\) reconstruction of every global polynomial
  ledger;
- load-bearing content hashes and fail-closed scientific scope.

No Xi evaluation, numerical contour quadrature, high-precision scan, or heavy
campaign was run.
