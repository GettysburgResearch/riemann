# L-106050 — Character-square twists preserve the complementary-temperature flat connection

Claim ID: `L-106050`  
Programme aliases: `LFAM1.TWISTED_TEMPERATURE_CONNECTION`, `LFAM2.KUMMER_TEMPERATURE_FAMILY`, `STRESS.CHARACTER_SQUARE_FLATNESS`  
Status: **PROVED EXACT FINITE-HORIZON SOURCE THEOREM**  
Created: 2026-08-24  
Depends on: PR #719 `L-102898--L-102900`; `L-106020--L-106023`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Work in the finite labelled Euler algebra before physical collapse. Let `chi`
be a unitary multiplicative character on every unramified labelled prime in the
finite horizon. Put

\[
x_{\ell,\chi}
=\chi(p_\ell)p_\ell^{-1/2}U_\ell
\]

and define

\[
\boxed{
\sigma_{t,\chi}
=
\prod_\ell
(1-x_{\ell,\chi})(1+x_{\ell,\chi})^t.
}
\tag{L-106050.1}
\]

Ramified labels, where `chi(p)=0`, are omitted and must be restored at the full
source before any residual projection. The two labelled copies of `67` retain
the same literal character value.

## 1. Twisted flat factorization

At one label,

\[
(1-x)(1+x)^t(1-x)(1+x)^{1-t}
=(1-x)(1-x^2).
\]

Therefore

\[
\boxed{
\sigma_{t,\chi}*\sigma_{1-t,\chi}
=E_\chi*S_{\chi^2},
}
\tag{L-106050.2}
\]

where

\[
E_\chi=\prod_\ell(1-x_{\ell,\chi})
\]

is the character-twisted native Euler source and

\[
S_{\chi^2}
=
\prod_\ell
\left(1-\chi(p_\ell)^2p_\ell^{-1}U_\ell^2\right)
\]

is the squared completion twisted by the **character square**.

Thus the complementary product depends on the ordered pair

\[
(\chi,\chi^2),
\]

not on `chi` alone. At the midpoint,

\[
\boxed{
\sigma_{1/2,\chi}*\sigma_{1/2,\chi}
=E_\chi*S_{\chi^2}.
}
\tag{L-106050.3}
\]

This is exactly the source map `chi -> eta=chi^2` that appears in the
owner-conductor family `L-106022`.

## 2. Flat tangent identity

Put

\[
\Lambda_\chi
=
\sum_\ell\log(1+x_{\ell,\chi}).
\]

Then

\[
\partial_t\sigma_{t,\chi}
=
\sigma_{t,\chi}*\Lambda_\chi.
\tag{L-106050.4}
\]

Differentiating (L-106050.2) gives

\[
\boxed{
(\partial_t\sigma_{t,\chi})*\sigma_{1-t,\chi}
=
\sigma_{t,\chi}*
(\partial_s\sigma_{s,\chi})|_{s=1-t}.
}
\tag{L-106050.5}
\]

Hence the antisymmetric tensor temperature current lies in the kernel of
arithmetic convolution in every character channel, just as in the untwisted
parent connection.

Every fixed kernel, scale derivative, dyadic filter, deterministic owner
projection and source-owned regional projection commutes with this finite
identity when applied after the full source has been formed.

## 3. Simultaneous midpoint energy minimization

Write

\[
(1-x)(1+x)^t=\sum_{k\ge0}a_k(t)x^k.
\]

At an unramified prime the twisted coefficient is

\[
a_k(t)\chi(p)^k.
\]

Since `|chi(p)|=1`, its squared magnitude is exactly `|a_k(t)|^2`. Therefore
the source-energy exponents of PR #719 `L-102899` are unchanged in every
unitary character channel:

\[
\|\sigma_{t,\chi}\|_{\rm src}^2
\|\sigma_{1-t,\chi}\|_{\rm src}^2
\ll
(\log(2Y))^{(1-t)^2+t^2}.
\tag{L-106050.6}
\]

Consequently

\[
\boxed{t=\frac12}
\]

is the unique free-energy-minimizing and carrier-balanced temperature
simultaneously across the complete unramified character family. Ramified local
factors change only the declared finite completion ledger.

## 4. Function-field reading

Over `F_q[T]`, (L-106050.2) is the product of a Kummer-twisted native Euler
source with its character-square completion. The map `chi -> chi^2` is the
same finite étale square map whose Fourier decomposition gives
`L-106023`.

No purity, monodromy or function-field RH enters the identity.

## Scope

This theorem proves an exact character-family extension of the parent flat
completion-temperature connection and identifies the owner-conductor square
map inside it. It proves no physical assembly, twisted positive inverse,
`SOCM106020`, `GMBC102893`, or RH.
