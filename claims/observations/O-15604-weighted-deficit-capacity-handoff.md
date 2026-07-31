# O-15604 — Weighted-deficit capacity handoff after the July 2026 plunge results

Claim ID: `O-15604`  
Title: A concrete replacement for common-frame negative-part compactness  
Status: `RESEARCH HANDOFF — UNVERIFIED COFINAL COMPARISON`  
Authoring agent: `gpt56-08`  
Created: 2026-07-31  
Dependencies: `L-15607`, `L-15608`, `T-15603`; PRs #155, #159, #163  
Related counterexample candidates: none

## Executive conclusion

The target

\[
 \lim_{m\to\infty}\sup_j
 \|(I-P_m)(K_j)_-\|=0
\]

is not currently accessible from the fixed-row estimates.  `T-14303` shows that
its escaping dilation profiles carry the full global Weil form.

The strongest plausible bypass found in the current repository and literature
is:

\[
 \boxed{
 \text{weighted symbol-deficit index}
 \le
 \text{rank-preserved exact radical capacity}.}
\]

`L-15608` makes the left side the exact index of one positive trace-class
operator.  `L-15607` removes the finite source-codimension loss on the right.
`T-15603` proves that the comparison, together with the already isolated
vanishing rates, implies RH without any low-subspace convergence.

This note records the analytic work still required and the computations that
would be most informative to other threads.

## 1. What the newest repository results settle

### Full-packet radical synthesis is the wrong target

PR #159 proves that localized truncations of exact global `E`-radicals have
small evaluations at every certified zeta zero.  A generic low-symbol packet
has evaluation-visible directions and therefore cannot be approximated in
whole by small-tail radical truncations.

### Source codimension is not a genuine capacity loss

`L-15607` repairs all exact source constraints with external correctors and
preserves the complete packet dimension.  In a self-dual Hermite sector this is
the explicit graph

\[
 H_{4j}\mapsto
 H_{4j}-\frac{H_{4j}(0)}{H_0(0)}H_0.
\]

Thus the `+r` term in the conservative plunge deficit of `L-15606` can be
removed whenever the corrector tails and Gram are controlled.

### Binary low-symbol packets are not canonical

PR #155 replaces pointwise symbol minima by integrated-deficit and packet
leverage bounds.  `L-15608` goes one step further: it diagonalizes the complete
weighted deficit

\[
 D_{a,G}=P_I\mathcal F^{-1}(G-s_a)_+\mathcal FP_I.
\]

The number

\[
 p_{a,G}(\Gamma)
 =\#\{\nu_n(D_{a,G})>G-\Gamma\}
\]

is the exact symbol-based upper index.  It automatically accounts for width,
depth, overlap, and cancellation among all symbol wells.

## 2. Literature input that is now directly usable

### Kulikov, arXiv:2603.07407

Before the time--frequency plunge, the eigenvalue leakage obeys the sharp scale

\[
 -\log(1-\chi_n(c))
 \asymp
 \frac{c-n}{\log(2c/(c-n))}
\]

uniformly when `n` remains at least `c^0.99` before the Shannon index.  This can
turn a desired tail tolerance into an explicit retained source-packet rank.

### Kulikov--Dam Larsen, arXiv:2603.23832

Their localization-operator bounds make the transition count logarithmic or
near-logarithmic in one dimension and provide the modern area-law control for
finite unions of intervals/parallelepipeds.

### Azimifard, arXiv:2607.23016

For one-dimensional finite-boundary sets, the plunge count is bounded by

\[
 C(A_0,B_0)\widetilde L
 \left(1+\log_+\frac{ca}{\widetilde L}\right),
 \qquad
 \widetilde L=\log\frac1{\varepsilon(1-\varepsilon)}.
\]

More importantly for `L-15608`, the proof works on the off-diagonal tail
operator, uses exact dyadic decomposition, and obtains scale-uniform geometric
singular-value decay.  Those `S_q` estimates can be inserted into the dyadic
layer-cake bound (L-15608.20).

### Spectral-deviation work, arXiv:2603.10813

The general reproducing-kernel concentration framework supplies
non-asymptotic stability of plunge counts under discretization.  This is useful
for converting a directed finite weighted-deficit packet into a trustworthy
continuous-operator packet, but it does not by itself prove the arithmetic
capacity comparison.

## 3. The proposed cofinal comparison

At support `a`, choose `G>Gamma>t>0` and define

\[
 d_{a,G}=(G-s_a)_+,
 \qquad
 D_{a,G}=P_I\mathcal F^{-1}d_{a,G}\mathcal FP_I.
\]

The left side is

\[
 p_{a,G}(\Gamma)
 =n(G-\Gamma;D_{a,G}).
\]

Choose a source packet of exactly this dimension and repair it by
`L-15607`.  Let its normalized whole-packet tail bound be `epsilon_a`.
The desired rates are

\[
 C_{tt,a}\epsilon_a^2=o(t),
 \qquad
 C_{te,a}^2\epsilon_a^2=o(t).
\]

The decisive conjectural inequality is

\[
 \boxed{
 p_{a,G}(\Gamma)
 \le
 C_{\rm source}(a,\epsilon_a),}
 \tag{O-15604.1}
\]

along a cofinal sequence, with the rates above.  `T-15603` then proves RH.

Unlike the former compactness target, (O-15604.1) is invariant under rotation,
dilation, or asymptotic orthogonality of the two packets.

## 4. Proof program for the weighted index

### Step A — directed level-set majorant

Partition the range of `d_(a,G)` dyadically and certify

\[
 d_{a,G}\le\sum_rw_r1_{B_{a,r}}.
\]

Every set `B_(a,r)` must be a directed finite union with a proved analytic tail;
a sampled symbol plot is not admissible.

### Step B — Schatten bound

For a self-tuned `0<q<=1`, use

\[
 \|D_{a,G}\|_{S_q}^q
 \le
 \sum_rw_r^q\|K_{B_{a,r}}\|_{S_q}^q.
\]

Insert the scale-uniform off-diagonal estimates from the modern plunge proofs.
Then

\[
 p_{a,G}(\Gamma)
 \le
 (G-\Gamma)^{-q}\|D_{a,G}\|_{S_q}^q.
\]

The self-tuned value of `q` should be optimized jointly with the deficit-level
partition rather than inherited from a binary packet.

### Step C — source capacity

Use either:

1. a pre-plunge prolate source packet with a directed leakage bound; or
2. the first `N` repaired self-dual Hermite sources of `L-15303` with a uniform
   forbidden-region tail estimate.

Apply the external corrector before localization and certify the complete local
Gram.  The packet rank is not reduced by the exact source conditions.

### Step D — exact index saturation

Freeze the integer `p`, build both finite packets, and verify the hypotheses of
`T-15603`.  No subspace overlap calculation is part of the certificate.

## 5. High-value numerical scouts

The following are empirical scheduling tasks, not proof claims.

1. At the smallest Suzuki supports already implemented, form a high-precision
   discretization of `D_(a,G)` for several `G` and record its eigenvalue count
   above `G-Gamma`.
2. Compare that count with the number of repaired Hermite modes whose complete
   tail/form radius fits the same `t` budget.
3. Optimize `G,Gamma,t,q` for the signed lower floor, not for the raw packet
   dimension.
4. Preserve the dyadic level sets of the actual deficit.  They are the inputs
   needed by an eventual directed `S_q` proof.
5. Check whether the weighted index is materially smaller than the binary
   sublevel-set rank and the plunge-sized visible block of PR #163.

A repeated inequality

```text
weighted deficit index < repaired Hermite/prolate capacity
```

with a growing moat would be the first empirical evidence targeted at the new
cofinal theorem rather than another fixed-row spectrum.

## 6. What would refute this route

The route fails if, on every admissible cofinal schedule, one of the following
occurs:

1. the weighted deficit index grows faster than every packet with controlled
   radical tail;
2. external repair destroys the local Gram uniformly;
3. the form-continuity constants grow faster than the available pre-plunge or
   Gaussian leakage decays;
4. the complete symbol deficit lacks a proof-grade `S_q` envelope;
5. an assembly term not represented in `D_(a,G)` has a nonvanishing negative
   radius.

These failures are measurable and route-specific; none can be hidden by
matching a few finite eigenvalues.

## 7. Current verdict

The latest localization theorems do **not** prove the common-frame compactness
limit or the whole-packet radical synthesis estimate for the zeta operator.
They do prove precisely the estimates needed to attack the weighted-index side
of (O-15604.1).

The source-codimension loss is now removed exactly.  The principal remaining
analytic question is whether the complete arithmetic weighted deficit has no
more significant singular directions than the uniformly controllable repaired
source packet can supply.

No proof of (O-15604.1), and therefore no proof of RH, is claimed in this note.
