# T-106000 — Auxiliary completed-family checkpoint

Claim ID: `T-106000`  
Programme aliases: `LFAM1.HYBRID_COLLISION_LINE_MOMENT`, `LFAM2.FROBENIUS_TRACE_HANDOFF`, `STRESS.LFAMILY_FRONTIER`  
Status: **PROVED EXACT FULL-SOURCE FAMILY REDUCTION; SUPERSEDED AS THE NORMATIVE FRONTIER**  
Created: 2026-08-24  
Updated: 2026-08-24  
Programme issues: #743, #736, #737  
RH status: **unproved**

## Supersession notice

This file records the first full-source auxiliary-family checkpoint. Its exact
Mellin and character identities remain valid. It is no longer the preferred
conclusion-facing theorem because:

1. PR #719 advanced from the original all-clean squareclass packet to the
   horizon-safe balanced frontier `HBCQDSP102888`;
2. `R-106001` showed that ramified completion must precede residual selection;
3. `L-106020--L-106022` identified a stronger owner-conductor family whose
   principal leverage is paid by the literal source.

The corrected auxiliary residual theorem is `T-106001`. The preferred current
frontier is `T-106020`.

## 1. Exact full-source family

For every odd auxiliary prime `ell != 67`, `L-106000` constructs

\[
\mathcal F_{\chi,\ell}
=
(I-\ell^{-1/2}S_\ell)
(I-\chi(67)67^{-1/2}S_{67})
\sum_n{\mu(n)\chi(n)\over\sqrt n}\Phi_*(X/n).
\]

Its Mellin transform is

\[
\widehat{\mathcal F}_{\chi,\ell}(z)
=
\widehat\Phi_*(z)
{(1-\ell^{-s})(1-\chi(67)67^{-s})\over L(s,\chi)},
\qquad s=z+\frac12.
\]

For the principal character,

\[
\boxed{
\widehat{\mathcal F}_{\chi_0,\ell}(z)
=
\widehat\Phi_*(z){1-67^{-s}\over\zeta(s)}.
}
\tag{T-106000.1}
\]

Thus the principal completed member is exactly the native marked-67
common-mother detector. Every finite numerator factor is zero-free for
`Re(s)>0`.

## 2. Exact collision geometry

Complete character orthogonality converts one clean squareclass pair

\[
Pc^2,\qquad Qd^2
\]

into

\[
Pc^2\equiv Qd^2\pmod\ell.
\]

If `QP^(-1)` is a nonsquare, the pair vanishes. If it is a square with root
`tau`, the pair lies on

\[
\boxed{c\equiv\tau d\quad\text{or}\quad c\equiv-\tau d\pmod\ell.}
\tag{T-106000.2}
\]

General characters retain the core through

\[
\chi(Pc^2)=\chi(P)\chi^2(c),
\]

whereas quadratic characters erase it. The finite-field Gauss prototype and
function-field algebraic mirror are proved in `L-106002--L-106003`.

## 3. Historical conditional theorem

Let `D(X)` be the **complete** native common-mother scalar, before any residual
selection. For a predeclared nonnegative family moment define

\[
\Lambda_X
=
\sum_\ell w_{\ell,\chi_0}|A_{\ell,\chi_0}|^2
\]

and

\[
\mathfrak M(Y)=
\int_2^Y\sum_{\ell,\chi}
 w_{\ell,\chi}|A_{\ell,\chi}|^2
 |\mathcal F_{\chi,\ell}(X)|^2{dX\over X}.
\]

Then the exact positivity implication remains:

```text
Lambda_X >= X^(-o(1))
and
M(Y)=Y^o(1)
 -> integral |D(X)|^2 dX/X = Y^o(1)
 -> native common-mother subpower negative mass
 -> RH.
```

This full-source condition is valid but substantially stronger and less
source-localized than the later residual and owner-conductor routes.

## 4. Binding boundaries

```text
full-source Euler-completed family             PROVED EXACT
principal recovery / reciprocal-L transform    PROVED EXACT
character collision-line geometry              PROVED EXACT
finite-field Gauss prototype                    PROVED EXACT
post-residual completion shortcut               REFUTED BY R-106001
auxiliary full-source family moment             OPEN / RH-BEARING
normative current theorem                       T-106020
Riemann Hypothesis                              UNPROVED
```
