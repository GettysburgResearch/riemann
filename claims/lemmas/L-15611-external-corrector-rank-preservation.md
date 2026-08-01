# L-15611 — External correctors preserve the full source-packet rank

Claim ID: `L-15611`  
Title: Exact finite-codimension source repair can be implemented as an injective graph transform rather than a dimension-losing kernel restriction  
Status: `PROPOSED`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: elementary Hilbert-space algebra; `L-14313`; `L-15303`; `L-15605`  
Scope: repaired radical packet capacity in Issue #156  
Related counterexample candidates: none

## Abstract theorem

Let `H` be a Hilbert source space, let `P subset H` be finite-dimensional, and
let

\[
 \ell:H\to\mathbb C^r
 \tag{L-15611.1}
\]

be the exact source-constraint map.  Suppose there is a bounded map

\[
 Q:\mathbb C^r\to H
 \tag{L-15611.2}
\]

such that

\[
 \boxed{\ell Q=I_{\mathbb C^r},
 \qquad \operatorname{Ran}Q\perp P.}
 \tag{L-15611.3}
\]

Define

\[
 \mathcal R=(I-Q\ell)|_P.
 \tag{L-15611.4}
\]

Then

\[
 \boxed{\ell\mathcal R=0,}
 \tag{L-15611.5}
\]

and, for every `f in P`,

\[
 \boxed{
 \|\mathcal Rf\|^2
 =\|f\|^2+\|Q\ell f\|^2.}
 \tag{L-15611.6}
\]

In particular, `mathcal R` is injective and

\[
 \boxed{\dim\mathcal R(P)=\dim P.}
 \tag{L-15611.7}
\]

### Proof

Equation (L-15611.5) follows from `ell Q=I`.  Since `f in P` and
`Q ell f in Ran Q perpendicular P`, the two summands in
`mathcal Rf=f-Qell f` are orthogonal, which proves (L-15611.6).  The norm
identity implies injectivity and hence dimension preservation. QED.

## Localized tail adapter

Let

\[
 J:H\to H_{\rm loc},
 \qquad
 T:H\to X_{\rm tail}
 \tag{L-15611.8}
\]

be the localized-vector and discarded-tail maps.  Put

\[
 \delta=\|T|_P\|,
 \qquad
 q_T=\|TQ\|,
 \qquad
 \Lambda=\|\ell|_P\|.
 \tag{L-15611.9}
\]

Then

\[
 \boxed{
 \|T\mathcal R|_P\|
 \le d:=\delta+q_T\Lambda.}
 \tag{L-15611.10}
\]

Let

\[
 g=\inf_{\substack{f\in P\\\|f\|=1}}
 \|J\mathcal Rf\|.
 \tag{L-15611.11}
\]

If `g>0`, the normalized tail-synthesis map on the repaired localized packet
satisfies

\[
 \boxed{
 \|T\mathcal R(J\mathcal R)^{-1}\|
 \le d/g.}
 \tag{L-15611.12}
\]

Thus rank preservation is useful only when the corrector tail, the packet
constraint norm, and the repaired local Gram are all controlled.  The theorem
does not infer those estimates from dimension alone.

### Orthogonal local/tail split

If

\[
 \|u\|^2=\|Ju\|^2+\|Tu\|^2,
 \tag{L-15611.13}
\]

then (L-15611.6) and (L-15611.10) give

\[
 g\ge\sqrt{1-d^2}
 \qquad(d<1),
 \tag{L-15611.14}
\]

and hence

\[
 \boxed{
 \|V_{\rm repaired}\|
 \le\frac d{\sqrt{1-d^2}}.}
 \tag{L-15611.15}
\]

## Dimension-free Schur consequence

Under the tail/form continuity constants of `L-14313` and complement moat
`h>0`, the corrected low matrix on the repaired packet obeys

\[
 \boxed{
 B-h^{-1}R^*M^{-1}R
 \succeq
 -\frac{d^2}{g^2}
 \left(C_{tt}+\frac{C_{te}^2}{h}\right)I.}
 \tag{L-15611.16}
\]

The estimate has no packet-dimension factor.  A cofinal packet closes when the
two terms on the right tend to zero relative to the threshold required in
`T-15602`.

## Exact self-dual Hermite repair

In one self-dual even Hermite sector, take

\[
 P_N=\operatorname{span}\{H_4,H_8,\ldots,H_{4N}\}.
 \tag{L-15611.17}
\]

The two Connes--Consani source functionals agree on this sector:

\[
 \widehat f(0)=\int f=f(0).
 \tag{L-15611.18}
\]

Let

\[
 \ell(f)=f(0),
 \qquad
 Qc=cH_0/H_0(0).
 \tag{L-15611.19}
\]

Since `H_0` is orthogonal to `P_N`, the theorem applies and gives

\[
 \boxed{
 \mathcal RH_{4j}
 =H_{4j}-\frac{H_{4j}(0)}{H_0(0)}H_0.}
 \tag{L-15611.20}
\]

These are the exact sources of `L-15303`.  The repaired source packet has rank
`N`, not merely the kernel lower bound `N-1` from `L-15605`.

Whether the corresponding localized arithmetic packet has a uniform growing-
rank Gram and tail/form estimate is a separate analytic gate.  The present
lemma proves only that finite source codimension need not itself consume a
packet direction.

## Relationship to `R-15601`

The external repair supplies an exact source packet and may preserve its rank.
It does not by itself prove that this packet captures a weighted-deficit
subspace or lies below the localized operator threshold.  The latter requires
the actual compression inequality of `L-15610` and the form/residual estimates
of `T-15602`.

Thus:

```text
external repair preserves candidate capacity,
but low-Rayleigh compression binds that capacity to the operator.
```

Both gates are required.

## Proof boundary

- The abstract graph repair and dimension statement are exact.
- The existence of a bounded external right inverse with controlled tails is a
  hypothesis in the general setting.
- The Hermite corrector is explicit, but no cofinal growing-rank tail/form bound
  is asserted here.
- Rank preservation alone does not imply a weighted-deficit complement floor.
- No proof of RH is claimed.
