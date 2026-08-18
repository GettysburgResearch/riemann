# T-98060 — Multiplicative curvature and adaptive cutoffs leave only the post-logarithmic product boundary

Claim ID: `T-98060`  
Status: **UNCONDITIONAL REDUCTION; PRODUCT-BOUNDARY SIGN OPEN**  
Created: 2026-08-18  
Depends on: `L-98060--L-98063`, `R-98060/R-98061`; PRs #605/#608  
RH status: **unproved**

The source-faithful root attack now has the following exact disposition.

## 1. The scalar ratio is not the invariant

For the first root edge `p=67`, the proposed profile ratio

\[
Q(Y,67)={U(Y/67,71)\over U(Y,71)}
\]

is not cellwise monotone.  `R-98060` gives directed sign changes already near
`Y=435`.  A one-crossing or derivative-sign proof of `PRMP67` is therefore
impossible.

Adjoining a future prime `q` changes the ratio by the exact cross-ratio of
`L-98060`.  The sign is the opposite of

\[
\mathcal K_{p,q}[V](Y)
=V(Y)V(Y/(pq))-V(Y/p)V(Y/q).
\]

Moreover `L-98061` proves that the complete `P_61` base has
`mathcal K_(p,q)<0` eventually for every fixed pair.  Thus future primes have
the adverse projective sign in the base asymptotic.  They do not form a hidden
TP2 contraction.

## 2. The complete future profile is necessary abstractly

After `m` future primes, the exact ratio contains two Boolean hypercubes of
profile values.  `R-98061` proves that no source-blind fixed finite ratio or
curvature state determines the result.  Any genuine compression must use a new
native arithmetic identity.

The Stieltjes source identity of PR #605 is such a compression.  Prime Bellman
recursion commutes with it:

\[
\int S_p(X/y)dU(y)
=
\int S_{p^+}(X/y)dU(y)
-{1\over p}\int S_{p^+}(X/(py))dU(y).
\tag{T-98060.1}
\]

Thus the dynamic finite-block problem in PR #608 is not a second independent
criterion.  After the bulk reductions of PR #605, it is the same common-source
object as

\[
\mathcal J_\epsilon(X)
=
\int_2^{(\log X)^{4+\epsilon}}
S_Z(X/y)dU_Z(y).
\tag{T-98060.2}
\]

## 3. Adaptive cutoff changes are boundary coboundaries

`L-98062` proves that moving a prime between the tail and finite cube on a
truncated child interval creates no bulk term.  It creates only the upper and
lower multiplicative boundary strips.  At the natural switch `Y=X/q`, the
change is exactly

\[
{1\over q}
\left[U_{<q}(X/q)-U_{<q}(X/q^2)\right].
\tag{T-98060.3}
\]

This gives a rigorous adaptive-cutoff calculus: a proposed schedule is valid if
and only if every retained boundary strip is paid with its literal source and
sign.

## 4. The fully activated sector is closed

For every fixed `epsilon>0`, `L-98063` proves uniformly

\[
U_{<q}(X/q)-U_{<q}(X/q^2)>0
\]

for all primes

\[
67\le q\le(1-\epsilon)\log X
\]

and all sufficiently large `X`.  Therefore every adaptive prime switch below
the logarithmic primorial wall has nonnegative cost.

The proof uses the negative finite part of the exact `P_61` base:

\[
h(Y)=a_*+c_*Y^{-1/2}+O(Y^{-2}),
\qquad c_*<0.
\]

Below the logarithmic wall every finite-cube colour is fully active at the
bottom switch endpoint, and the `c_*` increment dominates uniformly.

## 5. Exact remaining frontier

The first possible adverse switch occurs only when

\[
q\ge(1-o(1))\log X,
\]

where the primorial of the installed source reaches the active child endpoint.
This is the genuine product-boundary regime.  It is the same regime isolated,
in complementary coordinates, by

```text
PR #592: growing-prime two-row wall near log X;
PR #599: near-critical product-boundary histories;
PR #605: logarithmic-four Stieltjes boundary;
PR #590/#604: one-sided Type-II / C4MBI root kernels.
```

No theorem in this packet signs the post-wall strips.  The conclusion-producing
remaining assertion may be stated without inventing another equivalent name:
prove that the exact sum of the source-owned post-wall boundary strips, together
with the explicit PR #605 endpoint debt, is nonnegative.  By `L-98062` this is
exactly `PLST67`, hence exactly the native root zero hinge after the retained
`o(1/log X)` accounting.

The surviving chain is

\[
\boxed{
\text{post-logarithmic product-boundary sign}
\Longrightarrow
\mathrm{PLST}_{67}
\Longrightarrow
\mathrm{GPC}_{67}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-98060.4}

## Scientific boundary

```text
cellwise scalar-ratio maximum principle       REFUTED
source-blind TP2 ratio damping                 REFUTED
exact future-prime curvature debt              PROVED
universal fixed-dimensional ratio state        REFUTED
Bellman/Stieltjes commutation                   PROVED EXACT
prime-cutoff boundary-strip coboundary          PROVED EXACT
all switches below (1-eps)log X                 PROVED POSITIVE
post-logarithmic product-boundary strips        OPEN / RH-BEARING
GPC67 / Riemann Hypothesis                      UNPROVEN
```

This pass removes a false candidate mechanism and closes a new uniform sector.
It does not relabel the remaining product-boundary sign as a proof.