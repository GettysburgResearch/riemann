# L-97912 — The critical factor-67 sign localizes to almost-full rough products

Claim ID: `L-97912`  
Status: **PROVED EXACT DECOMPOSITION + UNCONDITIONAL BULK ESTIMATE**  
Created: 2026-08-18  
Depends on: `L-97910`; exact finite-prime recurrence  
RH status: **not assumed**

Fix `0<kappa<1/2` and use

\[
 Z=(\kappa\log X\log\log X)^2.
\]

Put

\[
 P_Z=\prod_{67\le p\le Z}(1-p^{-1}),
 \qquad
 E_Z=\prod_{67\le p\le Z}(1+p^{-1/2}),
 \qquad A_Z=a_*P_Z.
\]

The proof of `L-97910` gives, uniformly for every `Y>0`,

\[
 \boxed{
 U_Z(Y)=A_Z+\varepsilon_Z(Y),
 \qquad
 |\varepsilon_Z(Y)|\le C_b\frac{E_Z}{\sqrt Y}.
 }
\tag{L-97912.1}
\]

Let `Q_L` be the finite product of active rough primes `Z<p<=X/2`. Exact
Euler expansion gives

\[
 \boxed{
 U_{\rm full}(X)
 =A_Z\prod_{Z<p\le X/2}(1-p^{-1})
 +\sum_{v\mid Q_L}\frac{\mu(v)}v
  \varepsilon_Z(X/v).
 }
\tag{L-97912.2}
\]

The first term is the deterministic positive Euler main

\[
 \boxed{
 \mathfrak M(X)=
 a_*\prod_{67\le p\le X/2}(1-p^{-1})
 \asymp\frac1{\log X}.
 }
\tag{L-97912.3}
\]

Fix `beta` with

\[
 0<\beta<1-2\kappa
\]

and split the error in (L-97912.2) at `v=X^beta`. Define

\[
 \mathfrak E_{\kappa,\beta}^{\le}(X)=
 \sum_{\substack{v\mid Q_L\\v\le X^\beta}}
 \frac{\mu(v)}v\varepsilon_Z(X/v).
\]

Then

\[
 \boxed{
 \mathfrak E_{\kappa,\beta}^{\le}(X)
 =o\!\left(\frac1{\log X}\right).
 }
\tag{L-97912.4}
\]

The complementary boundary is

\[
 \boxed{
 \mathfrak R_{\kappa,\beta}(X)=
 \sum_{\substack{v\mid Q_L\\v>X^\beta}}
 \frac{\mu(v)}v\varepsilon_Z(X/v),
 }
\tag{L-97912.5}
\]

whose histories all have child endpoint

\[
 X/v<X^{1-\beta}.
\]

In particular, for every fixed `delta` with `0<delta<1`, choose `kappa<delta/2` and
`beta=1-delta`. Then the complete sign obstruction is localized to histories
with

\[
 \boxed{v>X^{1-\delta},\qquad X/v<X^\delta.}
\tag{L-97912.6}
\]

## Proof of the bulk estimate

By (L-97912.1),

\[
 \left|
 \sum_{\substack{v\mid Q_L\\v\le X^\beta}}
 \frac{\mu(v)}v\varepsilon_Z(X/v)
 \right|
 \le
 \frac{C_bE_Z}{\sqrt X}
 \sum_{\substack{v\mid Q_L\\v\le X^\beta}}v^{-1/2}.
\]

Since `v<=X^beta`,

\[
 \sum_{v\le X^\beta}v^{-1/2}
 \le X^{\beta/2}\sum_{v\mid Q_L}v^{-1}
 =X^{\beta/2}\prod_{Z<p\le X/2}(1+p^{-1})
 \ll X^{\beta/2}\frac{\log X}{\log Z}.
\]

Also `E_Z=X^{kappa+o(1)}`. Thus the left side is

\[
 \ll X^{\kappa+(\beta-1)/2+o(1)}\frac{\log X}{\log Z},
\]

which is power-saving because `beta<1-2kappa`. This proves (L-97912.4).

## Firewall

The positive Euler main is not asserted to be the asymptotic of the native
scalar. The product-boundary term is forced to cancel it to very high accuracy
in general; its one-sided sign is precisely the critical arithmetic issue.
This theorem localizes that issue but does not estimate it.
