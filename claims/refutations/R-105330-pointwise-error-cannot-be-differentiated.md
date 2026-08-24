# R-105330 — Pointwise or shrinking-real-interval error does not control the Pick derivative

Claim ID: `R-105330`  
Status: **PROVED EXACT ANALYTIC FIREWALL**  
Created: 2026-08-23

It is invalid to differentiate an unshifted `O(T^-delta)` explicit-formula
error without uniform complex-alpha control.

For an integer `N>=1`, let

\[
e_N(\alpha)=N\alpha.
\]

On the shrinking real interval `|alpha|<=N^-2`,

\[
|e_N(\alpha)|\le N^{-1},
\]

but

\[
e_N'(0)=N.
\]

Thus even an entire error can be tiny on a shrinking real interval and have a
large derivative.  A fixed or quantitatively controlled complex disk and a
Cauchy estimate are load bearing.

A second firewall is reflection typing. Since

\[
E_\alpha(1-s)=-E_{-\alpha}(s),
\]

one shifted field does not satisfy the xi-prime reflection axiom.  The
oriented pair must be proved directly; silently reusing the unshifted
ZeroConfig theorem is not a valid continuation.
