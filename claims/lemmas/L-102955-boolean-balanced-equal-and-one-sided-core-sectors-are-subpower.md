# L-102955 — Boolean balanced equal-core and one-sided-core sectors are absolutely subpower

Claim ID: `L-102955`  
Status: **PROVED UNCONDITIONAL REGIME CLOSURE**  
Created: 2026-08-25  
Depends on: PR #751 `L-106080`; `L-102884`, `L-102887`  
RH status: **not assumed**

Work on one dyadic physical horizon

\[
Y\le X<2Y
\]

with the frozen Boolean Vaughan cutoff

\[
U\asymp Y^{1/6}.
\]

Every nonzero balanced Boolean representation has two disjoint factors

\[
r>U,
\qquad s>U,
\qquad(r,s)=1.
\]

Therefore its literal squarefree core `a` satisfies

\[
\boxed{a\ge rs>U^2\gg Y^{1/3}.}
\tag{L-102955.1}
\]

Consider two balanced physical terms

\[
N=P c^2,
\qquad
M=Qd^2,
\]

and write

\[
g=(c,d),
\qquad c=gc_1,
\qquad d=gd_1,
\qquad(c_1,d_1)=1.
\]

The exact common-square extraction gives

\[
\langle v_N,v_M\rangle
=g^{-2}
\langle v_{Pc_1^2},v_{Qd_1^2}\rangle.
\]

The source-blind reduced physical bound of `L-102887` yields, on one dyadic
block,

\[
\boxed{
\mathcal C_{g\ge G}(Y)
\ll
Y^{1+o(1)}G^{-3+o(1)}.
}
\tag{L-102955.2}

## 1. Equal reduced cores

If

\[
c_1=d_1=1,
\]

then `c=d=g`. By (L-102955.1),

\[
g\gg Y^{1/3}.
\]

Substituting `G` equal to a fixed multiple of `Y^(1/3)` in
(L-102955.2) gives

\[
\boxed{
\mathcal C_{\rm equal}(Y)=Y^{o(1)}.
}
\tag{L-102955.3}

This is an absolute estimate. The equal-core packet may therefore be removed
before a negative part is taken.

## 2. One-sided reduced-core discrepancy

Suppose, after orientation,

\[
c_1>1,
\qquad d_1=1.
\]

Then the entire second core is the common core:

\[
d=g.
\]

Because the second source atom is Boolean balanced, (L-102955.1) again gives

\[
g\gg Y^{1/3}.
\]

Hence

\[
\boxed{
\mathcal C_{\rm one-sided}(Y)=Y^{o(1)}
}
\tag{L-102955.4}

absolutely on every dyadic horizon.

## 3. Exact remaining core geometry

Only the sector

\[
\boxed{c_1>1,\qquad d_1>1}
\tag{L-102955.5}

can remain conclusion-bearing. Since `(c_1,d_1)=1`, it supplies two distinct
literal discrepancy primes and therefore the two source-owned nonzero internal
phases of `L-102888`.

## Consequence for the all-chaos firewall

`R-102869` remains binding for the ordinary stopped-Vaughan coordinate. In the
Boolean balanced coordinate, however, the equal-core and one-sided packets
have now acquired an independent absolute estimate. They no longer have to be
retained to cancel the two-sided packet.

Thus the final Boolean physical restriction may be confined to the coprime,
two-sided, internally phased sector.
