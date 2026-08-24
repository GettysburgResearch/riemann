# L-106004 — Full-source completion recovers the horizon-safe balanced residual

Claim ID: `L-106004`  
Programme aliases: `LFAM1.HBC_RESIDUAL_ADAPTER`, `STRESS.HORIZON_SAFE_FAMILY_FUNCTOR`  
Status: **PROVED EXACT ORDERED SOURCE DIAGRAM**  
Created: 2026-08-24  
Base: PR #719 at `c2e82cfdd254a478731f005b3d83b49d3e1e33ea`  
Depends on: `L-106000`; `R-106001`; PR #719 `L-102741--L-102749`, `L-102886--L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `D_(chi,ell)` denote the complete marked-67 Dirichlet-family source of
`L-106000`, including the ramified two-scale completion, before any carrier,
owner or Vaughan projection.

On one dyadic horizon let `R_HBC` be the following deterministic linear source
pipeline:

1. recombine the complete native/completion carrier;
2. pass to the exact Wick carrier quotient;
3. allocate the canonical pair owner and transfer to the horizon-safe pair
   gauge of `L-102887`;
4. remove owner/core overlaps by the existing finite-Euler renewals;
5. use the blockwise fixed cutoff of `L-102886`;
6. apply the owner-excluded Vaughan identity of `L-102888`;
7. discard only the already-proved power-small Type-I row;
8. retain the balanced distinct-product physical current.

Every operation above is applied before a negative part or source-blind norm.
The output is the current parent frontier `HBCQDSP102888`; the largest-two
smooth-boundary row is absent in this gauge.

Define

\[
\boxed{
\mathcal R_{\chi,\ell}
:=R_{\rm HBC}(\mathcal D_{\chi,\ell}).
}
\tag{L-106004.1}
\]

For the principal character, `L-106000` gives the coefficientwise full-source
identity

\[
\mathcal D_{\chi_0,\ell}=\mathcal D_{\rm native}.
\tag{L-106004.2}
\]

Applying the same deterministic pipeline to both sides yields

\[
\boxed{
\mathcal R_{\chi_0,\ell}(X)
=R_{\rm HBC}(X)
}
\tag{L-106004.3}
\]

for every finite endpoint `X`, every dyadic block and every auxiliary prime
`ell != 67`.

## Character moment after the correct ordering

After (L-106004.1), every clean physical monomial still has the form

\[
N=P a^2,
\qquad (a,P)=1,
\]

with a deterministic two-prime squarefree kernel `P`. Character orthogonality
may therefore be expanded at this final **linear** stage exactly as in
`L-106001`, including the two ramified scale sectors. The principal recovery
comes from (L-106004.2), not from applying the elementary Möbius restoration to
an arbitrary residual coefficient sequence.

## Consequence

For a predeclared nonnegative family moment,

\[
\mathfrak M_{\rm HBC}(Y)
=
\int_2^Y
\sum_{\ell,\chi}w_{\ell,\chi}|A_{\ell,\chi}|^2
|\mathcal R_{\chi,\ell}(X)|^2{dX\over X},
\]

the principal members satisfy

\[
\mathfrak M_{\rm HBC}(Y)
\ge
\int_2^Y\Lambda_X|R_{\rm HBC}(X)|^2{dX\over X}.
\tag{L-106004.4}
\]

This validates the auxiliary-family implication after the order correction. It
does not prove the family moment, the balanced physical current or RH.