# T-97901 — The unfiltered root problem is confined to a quasipolylogarithmic owner corridor

Claim ID: `T-97901`  
Status: **UNCONDITIONAL REDUCTION; ONE ROOT CORRELATION OPEN**  
Created: 2026-08-18  
Depends on: `L-97901`--`L-97904`; PR #594 zero-hinge map; the frozen annular Mellin--Landau consumer  
Supersedes as a frontier: `T-97900`  
RH status: **unproved**

Put

\[
 \ell=\log\log X,
 \qquad
 Z_X=(\log X)^2\ell,
 \qquad
 H_X=\exp(\ell^4).
 \tag{T-97901.1}
\]

Let `U_Z` be the complete native cube through `Z_X`. Split the exact
largest-prime Bellman budget as

\[
 \mathfrak C_X=
 \sum_{Z_X<p<H_X}\frac1pU_{Z,<p}(X/p),
 \tag{T-97901.2}
\]

\[
 \mathfrak H_X=
 \sum_{H_X\le p\le X/2}\frac1pU_{Z,<p}(X/p).
 \tag{T-97901.3}
\]

Then

\[
 \boxed{
 U_{\rm full}(X)=U_Z(X)-\mathfrak C_X-\mathfrak H_X.
 }
 \tag{T-97901.4}
\]

The preceding theorems give

\[
 \boxed{
 U_Z(X)=a_*\prod_{67\le q\le Z_X}(1-q^{-1})
 +o(\ell^{-1})\asymp\ell^{-1}>0
 }
 \tag{T-97901.5}
\]

and

\[
 \boxed{|\mathfrak H_X|\ll\ell^{-2}.}
 \tag{T-97901.6}
\]

Thus every owner below the quadratic-logarithmic cutoff is resummed into a
positive complete cube, while every owner above the quasipolylogarithmic cutoff
is lower order by exact top completion, PNT cancellation, and an upper-bound
sieve at the activation boundary.

## Exact remaining form

Expanding the corridor state by literal largest-prime ownership gives

\[
 \boxed{
 \mathfrak C_X=
 \sum_{Z_X<p<H_X}\frac1p
 \sum_{\substack{v\ {m squarefree}\\
                  Z_X<P^-(v),\ P^+(v)<p}}
 \frac{\mu(v)}vU_Z(X/(pv)).
 }
 \tag{T-97901.7}
\]

The only remaining owner primes satisfy

\[
 \boxed{
 (\log X)^2\log\log X<p<
 \exp((\log\log X)^4).
 }
 \tag{T-97901.8}
\]

Both endpoints are `X^o(1)`. No fixed-power owner range survives.

## Minimal root theorem

Define the **Quasipolylogarithmic Corridor Bellman estimate** `QPCB67` by

\[
 \boxed{
 \mathfrak C_X\le U_Z(X)-\mathfrak H_X
 }
 \tag{T-97901.9}
\]

for every sufficiently large real root endpoint. By (T-97901.4), this is
exactly equivalent to eventual nonnegativity of the native scalar. Consequently

\[
 \boxed{\mathrm{QPCB67}\Longrightarrow\mathrm{RH}.}
 \tag{T-97901.10}
\]

A convenient sufficient margin is

\[
 \mathfrak C_X\le U_Z(X)-C\ell^{-2}
 \tag{T-97901.11}
\]

with `C` larger than the effective constant in (T-97901.6).

## Scientific boundary

```text
complete cube through (log X)^2 loglog X       PROVED POSITIVE
owners above exp((loglog X)^4)                 PROVED LOWER ORDER
all fixed-power owner ranges                    CLOSED
root-only zero hinge                            RETAINED AS MINIMAL CONSUMER
quasipolylogarithmic corridor QPCB67            OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```

The remaining theorem is still a signed Möbius correlation. The reduction does
not authorize rowwise absolute values or a source-blind large sieve.