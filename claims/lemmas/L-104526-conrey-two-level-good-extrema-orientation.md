# L-104526 — The Conrey bounds orient at least 97.8932% of line Xi''' zeros

Claim ID: `L-104526`  
Status: **PROVED FROM L-104500 AND THE IMPORTED CONREY BOUNDS**  
Created: 2026-08-23  
Depends on: `L-104500`, `L-104525`  
RH status: **not assumed**

Let

\[
F=\Xi'',
\qquad
F'=\Xi'''.
\]

At a simple real zero `c` of `F'`, call the critical point **good** when

\[
{F(c)\over F''(c)}<0,
\]

so that it is a Rolle-generating extremum of `F`; call it **wrong** when the
residue is positive.

Let `R_3(T)` be the line-zero count of `xi'''` in Conrey's short window and let
`E_2(T)` be the number of wrong extrema among those zeros.  The factor-two
reverse-Rolle conservation law gives, after the standard regular-boundary
perturbation,

\[
2E_2(T)
\le
N_{\rm off}(\xi'';T,T+U)
+o(UL).
\]

Conrey's `alpha_2` bound gives

\[
N_{\rm off}(\xi'';T,T+U)
\le
(1-0.9584){UL\over2\pi}+o(UL),
\]

while the `alpha_3` bound gives

\[
R_3(T)
\ge
0.9873{UL\over2\pi}+o(UL).
\]

Therefore

\[
\limsup {E_2(T)\over R_3(T)}
\le
{1-0.9584\over 2\cdot0.9873}
={208\over9873}.
\]

Hence the lower proportion of good critical-line zeros of `xi'''` is at least

\[
\boxed{
1-{208\over9873}
={9665\over9873}
=0.9789324420\ldots .
}
\]

So at least **97.8932%** of the critical-line zeros certified for `xi'''` are
Rolle-generating extrema of `xi''`.

## Critical firewall

This theorem uses the independently proved `alpha_2>0.9584` bound.  It is an
orientation consequence of the two-level table; it is not a proof of
`alpha_2` from `alpha_3`.
