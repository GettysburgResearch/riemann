# T-99970 — Balanced surface correction and atom-free critical frontier

Claim ID: `T-99970`  
Status: **BINDING CORRECTION + EXACT RH-EQUIVALENT FRONTIER**  
Created: 2026-08-20  
Frozen base: PR #669 at `898f5baa42ed3bdfe9de2794eb1d4aea5a5c26b0`  
RH status: **unproved**

## 1. Disposition of `UPBF67`

`R-99970` proves, independently of the priority ordering,

\[
 \mathcal U_X\gg(\log X)^{-3}
\]

and therefore

\[
 \int_2^Y\sqrt X\,\mathcal U_X{dX\over X}
 \gg {\sqrt Y\over(\log Y)^3}.
\]

Thus the open statement `UPBF67` in `T-99920` is **false**.  It cannot be the
final proof obligation.

## 2. Exact repair

`L-99970` restores the even surface and the empty-set survival term:

\[
 \boxed{
 \mathscr A_\Phi
 =s_k\Phi(\varnothing)+\mathcal V_\Phi-\mathcal U_\Phi.
 }
\]

Its signed coarea is exactly

\[
 \mathscr A_\Phi=\int E(t)d\nu(t),
 \qquad
 E(t)=\sum_{n\le t}{\beta(n)\over n}.
\]

Hence the large pair shell used in `R-99970` is cancelled inside the native
scalar by even surface and survival.  Any proof that keeps only positive
upward loss necessarily pays a power-sized false majorant.

## 3. A cleaner critical observable

`L-99971` proves a full shifted quadratic positivity family.  Its
activation-zero member gives

\[
 G_{-1}(u)=e^{-u}
 \sum_{n\le e^u}{\beta(n)\over\sqrt n}
 [4(\sqrt{e^u/n}-1)]^2\ge0
\]

and the atom-free identity

\[
 dG_{-1}(u)=4e^{-u}L_{-1}(e^u)du,
\]

where

\[
 L_{-1}(X)
 =\sum_{n\le X}{\beta(n)\over\sqrt n}
 4(\sqrt{X/n}-1).
\]

Define

\[
 \boxed{
 \mathrm{AFCD}_{99970}(Y):
 \quad
 \int_1^Y(L_{-1}(X))_-{dX\over X}=Y^{o(1)}.
 }
\tag{T-99970.1}
\]

The Mellin transform is

\[
 {2(1-67^{-(s+1/2)})
  \over s(s-1/2)\zeta(s+1/2)}.
\]

It is holomorphic at every positive real point and has a genuine pole at
`s=rho-1/2` for every zeta zero with `Re rho>1/2`.  The one-sided Landau
argument therefore gives

\[
 \boxed{\mathrm{AFCD}_{99970}\Longrightarrow RH.}
\tag{T-99970.2}
\]

Conversely, RH and the standard Littlewood criterion imply

\[
 \sum_{n\le X}\beta(n)=O_\varepsilon(X^{1/2+\varepsilon}),
\]

hence, by partial summation,

\[
 \sum_{n\le X}{\beta(n)\over n}
 =O_\varepsilon(X^{-1/2+\varepsilon}),
 \qquad
 \sum_{n\le X}{\beta(n)\over\sqrt n}
 =O_\varepsilon(X^\varepsilon).
\]

Therefore `L_-1(X)=O_epsilon(X^epsilon)` and

\[
 \boxed{RH\Longrightarrow\mathrm{AFCD}_{99970}.}
\tag{T-99970.3}
\]

Thus the repaired atom-free critical variation is **equivalent to RH**.  It is
a cleaner formulation than `UPBF67`, but it is not an unconditional proof.

## Exact boundary

```text
native priority Hasse identity                  PROVED
positive upward-flux subpower estimate          FALSE
balanced signed priority surface                 PROVED EXACT
shifted quadratic family                         PROVED GLOBALLY POSITIVE
activation atoms in the critical descent         REMOVED EXACTLY
atom-free critical negative-mass condition       RH-EQUIVALENT
Riemann Hypothesis                               UNPROVEN
```
