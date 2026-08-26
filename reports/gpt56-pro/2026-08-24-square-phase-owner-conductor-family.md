# Square-phase owner-conductor L-family continuation

Date: 2026-08-24  
Programme issues: #743, #736, #737  
Execution PR: #751  
Arithmetic parent audited: PR #719 at `c2e82cfdd254a478731f005b3d83b49d3e1e33ea`  
RH status: **unproved**

## Executive summary

This pass found and repaired a source-order defect in the first auxiliary-family
adapter, resynchronized the branch with the horizon-safe pair gauge of the
moving CV/XD parent, and proved an exact additive-to-multiplicative transform
which removes the apparent phase-cardinality loss from every square-supported
owner packet.

The central identity is

\[
\sum_{h=1}^{p-1}\|F_h\|^2
={p+1\over p-1}\|F_0\|^2
+{2p\over p-1}
\sum_{\substack{\eta(-1)=1\\\eta\ne1}}\|M_\eta\|^2,
\]

where

\[
F_h=\sum_n v_n e_p(hun^2),
\qquad
M_\eta=\sum_n v_n\eta(n).
\]

It follows that

\[
\|F_0\|^2
\le{p-1\over p+1}\sum_{h\ne0}\|F_h\|^2.
\]

Generic Cauchy would pay `p-1`. The exact square-phase geometry instead gives a
strict factor smaller than one.

The multiplicative transform is a family of even Dirichlet characters
`eta=chi^2`. When the conductor is a literal opposite owner prime, the native
untwisted core has coefficient `(p+1)/(p-1)>1` inside the positive family
moment. Principal leverage is therefore source-paid at this local interface.

The same identity proves that the **local physical observation operator** from
one squareclass phase packet to its unphased field has sharp norm squared
`(p-1)/(p+1)`. Local occupancy is closed. The remaining open problem is the
coherent assembly of different owner packets after physical identification.

## 1. Moving-parent synchronization

The current PR #719 head introduces:

- a dyadic-frozen Vaughan cutoff, eliminating moving-cutoff transfer atoms from
  the negative-mass proof;
- a horizon-safe deterministic owner pair;
- completion of every nonowner prime;
- an owner-excluded Vaughan monoid `(n,pq)=1`;
- a power-small Type-I row;
- no largest-two smooth-boundary current.

The current arithmetic frontier is therefore

```text
HBCQDSP102888:
  coherent balanced distinct-product physical restriction in the
  horizon-safe owner-excluded gauge.
```

PR #751 is now synchronized to this source rather than the superseded
`SLCD102890` packet.

## 2. Binding order correction

The identity

\[
(I-\ell^{-1/2}S_\ell)
\sum_{\ell\nmid n}{\mu(n)\over\sqrt n}\Phi(X/n)
=
\sum_n{\mu(n)\over\sqrt n}\Phi(X/n)
\]

belongs to the complete Möbius source. It does not commute automatically with
an arbitrary residual projection.

A one-atom counterexample supported at `n=ell` proves that applying ramified
completion after residual selection can lose the source completely. The valid
order is:

```text
complete native source
 -> character twist
 -> ramified completion
 -> full carrier recombination
 -> Wick/owner/Vaughan source functor
 -> balanced residual
 -> positive family moment.
```

`R-106001` makes this firewall binding, while `L-106004` gives the corrected
commuting diagram and exact principal recovery of `HBCQDSP102888`.

## 3. Exact square-phase Gauss--Mellin identity

For an odd prime `p`, aggregate an arbitrary Hilbert-valued finite packet on
`F_p^*`. The nonzero additive square phases have kernel

\[
\sum_{h\ne0}e_p(h(c^2-d^2))
=p\mathbf1_{c^2=d^2}-1.
\]

Passing to sign-pairs `{c,-c}` gives the positive operator

\[
pI-J.
\]

Equivalently, multiplicative Fourier inversion gives the Gauss decomposition
through the square map on the character group. Its kernel is the principal and
quadratic pair; its image is the even-character subgroup. This proves
`L-106020` and its tensor product over any selected owner moduli.

The same theorem has three simultaneous readings:

1. a sharp finite Fourier inequality;
2. a positive family moment for even Dirichlet characters;
3. a Kummer--Artin--Schreier Fourier transform over finite fields.

## 4. Improved owner-packet estimate

For

\[
N=pq a^2,
\qquad M=rs b^2,
\]

choose opposite owner phases modulo `rho in {r,s}` and
`pi in {p,q}`. Combining the exact contraction with the existing phase-energy
bounds yields

\[
|\mathcal C_{P,Q}|
\ll{1\over\sqrt{pqrs}}
\left(1+{\rho\over A}\right)^{1/2}
\left(1+{\pi\over B}\right)^{1/2}.
\]

Choosing the smaller opposite owners gives

\[
\boxed{
|\mathcal C_{P,Q}|
\ll{1\over\sqrt{pqrs}}
\left(1+{s\over A}\right)^{1/2}
\left(1+{q\over B}\right)^{1/2}.
}
\]

All four owner coefficients survive. The former phase-cardinality factors are
not intrinsic. The theorem is fixed-packet and does not yet sum all owner
quadruples.

## 5. Owner-conductor L-functions

For an opposite owner conductor `rho`, the multiplicative transform of one
physical core is

\[
\chi(Pa^2)=\chi(P)\eta(a),
\qquad\eta=\chi^2.
\]

The owner-excluded Möbius core has Dirichlet series

\[
\sum_{(n,pq)=1}{\mu(n)\eta(n)\over n^{2s}}
={L(2s,\eta)^{-1}
 \over(1-\eta(p)p^{-2s})(1-\eta(q)q^{-2s})}.
\]

Hence the existing additive owner phases are exactly a family of reciprocal
even Dirichlet `L(2s,eta)` channels, with only two explicit owner Euler factors
removed.

The principal and quadratic square roots both map to `eta=1`. Their combined
Gauss weight produces the coefficient `(rho+1)/(rho-1)`. Deleting the
quadratic root deletes most of the local principal leverage; calling it an
independent core-oscillating channel is equally false.

## 6. Local physical occupancy is exactly closed

Let the source/phase norm be

\[
\|v\|_{\rm ph}^2=\sum_{h\ne0}\|F_h\|^2
\]

and let the local physical observation map the phase packet to

\[
F_0=\sum_n v_n.
\]

In sign-pair coordinates the phase Gram is `pI-J`. For fixed physical sum, its
energy is minimized when every sign-pair sum is equal. Therefore

\[
\boxed{
\|\mathscr O_{p,u}^{\rm sq}\|^2={p-1\over p+1}.
}
\]

This value is attained, so the theorem is sharp. For several selected phases,
the squared norm is the product of these factors.

The reviewed `BPOE103300` also includes collisions between **different**
source-owned occurrences after physical collapse. Thus the new theorem closes
one squareclass at a time, but does not prove global BPOE.

The occupancy factorization is now

```text
source/phase amplitude                    CLOSED
 -> local squareclass observation         SHARP CONTRACTION, CLOSED
 -> coherent owner-packet assembly        OPEN
 -> physical shell.
```

## 7. Function-field mechanism

Over `F_Q`, the same identity is exact and does not use geometric RH. The local
sheaf-theoretic object is the Fourier transform of the square map

\[
[2]:G_m\to G_m
\]

with Kummer multiplicative sheaves and an Artin--Schreier additive phase.

The sharpened geometric target is not generic purity. It is to control the
incomplete degree-restricted and Möbius/Vaughan-weighted Kummer--Artin--Schreier
traces and their assembly as owner irreducibles vary, including the
principal/quadratic root fibre and all resonant strata.

## 8. New frontier

Define

```text
SOCM106020:
  after the sharp local occupancy contraction, the source-weighted coherent
  assembly of the surviving short-core horizon-safe owner packets, expressed
  in the complete even owner-conductor character basis, is subpower.
```

Then

```text
SOCM106020
 -> HBCQDSP102888
 -> derivative common-mother subpower negative mass
 -> RH.
```

The corresponding function-field discovery target is `FFSOCM106023`.
Neither target is proved.

## 9. Exact replay

```text
PASS_X_106020_SQUARE_PHASE_OWNER_CONDUCTOR_FAMILY
exact_checks=6426
proof_object_sha256=63f7cbba47dea60cf308b26e46162b4dc23f54798f7ce408424bf7f1058f4872
```

The checker uses exact integer and rational arithmetic for Hilbert-valued
fixtures. It authenticates the finite Fourier identities, fixed-owner algebra,
character-square fibres and sharp local occupancy equality cases. It does not
evaluate any `L`-function, prove the coherent assembly, or prove RH.

## Boundary

```text
full-source completion order                         CORRECTED / PROVED EXACT
horizon-safe balanced residual adapter               PROVED EXACT
square-phase Gauss--Mellin identity                  PROVED EXACT
phase-cardinality removal                            PROVED EXACT
all-owner-weight fixed-packet estimate               PROVED
owner-conductor even reciprocal-L family             PROVED EXACT
local source-paid principal leverage                 PROVED EXACT
local squareclass physical occupancy                 PROVED SHARP
Kummer--Fourier finite-field mechanism               PROVED EXACT
long-core coherent phase packing                     INHERITED PROVED
SOCM106020 coherent owner-packet assembly             OPEN / RH-BEARING
FFSOCM106023 geometric trace assembly                 OPEN / EXPLORATORY
BPOE103300 global physical occupancy                 OPEN / RH-BEARING
HBCQDSP102888                                        OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
