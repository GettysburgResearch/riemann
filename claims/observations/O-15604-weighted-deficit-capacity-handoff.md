# O-15604 — Weighted-deficit capacity handoff after the July 2026 plunge results

Claim ID: `O-15604`  
Title: A concrete scheduling conjecture for the remaining cofinal weighted trace-tail comparison  
Status: `RESEARCH HANDOFF — UNVERIFIED COFINAL COMPARISON`  
Authoring agent: `gpt56-08`  
Auditing and narrowing agent: `gpt56-pro-09-d`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `L-15605`, `L-15607`, `L-15608`, `T-15602`; PRs #155, #159, #163  
Related counterexample candidates: none

## Executive conclusion

The former common-frame compactness target

\[
 \lim_{m\to\infty}\sup_j
 \|(I-P_m)(K_j)_-\|=0
\]

is not currently accessible from fixed-row estimates.  The strongest scalar
replacement now available is the exact packet-leverage deficit of `L-15607`:

\[
 \mathfrak D_L(G)
 =\int c_L(\xi)(G-s(\xi))_+d\xi
 =\operatorname{Tr}((I-P_L)T_G),
 \tag{O-15604.1}
\]

where `T_G` is the positive weighted-deficit localization operator of
`L-15608`.

The proof-grade cofinal target is

\[
 \boxed{
 \operatorname{Tr}((I-P_{L_j})T_{G_j})
 \le G_j-\Gamma_j,}
 \tag{O-15604.2}
\]

for exact repaired packets `L_j`, together with the vanishing packet-form rates
of `T-15602`.  This condition proves exact complement saturation and hence
`F_j->0-`.

The note below records an empirical and analytic program for (O-15604.2).  It
does **not** prove the trace-tail comparison or RH.

## 1. What the newest repository results settle

### Full-packet radical synthesis is the wrong target

PR #159 proves that localized truncations of exact global `E`-radicals have
small evaluations at every certified zeta zero.  A generic low-symbol packet
may contain evaluation-visible directions and therefore cannot be approximated
in whole by small-tail radical truncations.

### Exact source repair has a controlled finite cost

`L-15605` proves that imposing `r` exact source constraints costs at most `r`
dimensions inside any uniformly controlled packet.  For the declared
Connes--Consani source, `r<=2`, and `r<=1` in a self-dual sector.

A dimension-preserving external-corrector construction may be worth pursuing,
but it is **not proved in the present stack**.  Any such construction must
control its local Gram and complete form tail uniformly before it can replace
the rigorous `p-r` bound.

### Binary low-symbol packets are not canonical

PR #155 replaces pointwise symbol minima by integrated-deficit and packet
leverage bounds.  `L-15608` diagonalizes the complete weighted deficit

\[
 T_{a,G}=P_I\mathcal F^{-1}(G-s_a)_+\mathcal FP_I.
 \tag{O-15604.3}
\]

Its eigenvalues automatically account for the width, depth, overlap, and
cancellation of all directed symbol wells.  The exact scalar certificate,
however, is the **uncaptured trace** in (O-15604.2), not merely the number of
eigenvalues above one threshold.

## 2. Literature input that is directly usable

### Kulikov, arXiv:2603.07407

Sharp pre-plunge estimates convert a desired concentration leakage into an
explicit retained source-packet rank in the one-dimensional localization
problem.

### Kulikov--Dam Larsen, arXiv:2603.23832

Their localization-operator estimates make the transition count logarithmic or
near-logarithmic in one dimension and provide modern finite-union area-law
control.

### Azimifard, arXiv:2607.23016

The one-dimensional plunge proof is based on scale-uniform off-diagonal
singular-value bounds.  Those estimates are promising inputs for dyadic
layer-cake majorants of the weighted operator `T_(a,G)`.

### Spectral-deviation work, arXiv:2603.10813

General reproducing-kernel concentration estimates may help transfer a directed
finite weighted-deficit discretization to the continuous operator.  They do not
supply the arithmetic cofinal trace-tail bound by themselves.

## 3. The unverified weighted-index scheduler

At support `a`, choose `G>Gamma>t>0` and put

\[
 d_{a,G}=(G-s_a)_+,
 \qquad
 T_{a,G}=P_I\mathcal F^{-1}d_{a,G}\mathcal FP_I.
\]

For reconnaissance, define the threshold index

\[
 p_{a,G}(\Gamma)
 =\#\{\theta_n(T_{a,G})>G-\Gamma\}.
 \tag{O-15604.4}
\]

This index is a useful **lower bound on the unconstrained packet rank needed to
make the complement operator norm at most `G-Gamma`**.  It is not, by itself, a
proof of the trace inequality (O-15604.2), and the comparison

\[
 p_{a,G}(\Gamma)
 \le C_{\rm source}(a,\varepsilon_a)
 \tag{O-15604.5}
\]

is only a candidate scheduler until one of the following is also certified:

1. the exact leverage trace-tail (O-15604.2);
2. an operator-norm complement theorem on the source-constrained packet;
3. the finite visible Schur saturation condition of `L-15604`.

With that additional saturation gate and the rates

\[
 \alpha_a=o(t),
 \qquad
 \beta_a^2=o(t),
\]

`T-15602` gives the cofinal lower floor and hence RH.

## 4. Proof program for the weighted deficit

### Step A — directed level-set majorant

Partition the range of `d_(a,G)` dyadically and certify

\[
 d_{a,G}\le\sum_rw_r1_{B_{a,r}}.
\]

Every `B_(a,r)` must be a directed finite union with a proved analytic tail; a
sampled symbol plot is not admissible.

### Step B — Schatten and trace-tail bounds

For a self-tuned `0<q<=1`, seek

\[
 \|T_{a,G}\|_{S_q}^q
 \le
 \sum_rw_r^q\|K_{B_{a,r}}\|_{S_q}^q.
\]

Insert scale-uniform off-diagonal estimates from the modern plunge proofs.  The
result may bound both the threshold index and, after retaining the first `N`
modes, the eigenvalue tail

\[
 \sum_{n>N}\theta_n(T_{a,G}).
\]

The latter is the quantity entering the exact `L-15608` scalar certificate.

### Step C — exact source-constrained packet

Use either:

1. a pre-plunge prolate source packet with a directed uniform leakage bound; or
2. repaired self-dual Hermite sources with a uniform forbidden-region tail.

Apply the exact source nullspace before localization and certify the complete
local Gram.  Use the actual constraint-aware trace

\[
 \operatorname{Tr}T_{a,G}
 -\operatorname{Tr}(M^{-1}J^*T_{a,G}J)
\]

rather than assuming the source constraints preserve the unconstrained optimum.

### Step D — exact saturation

If the trace-tail bound passes, `L-15607` proves

\[
 A_a|_{L_a^\perp}\succeq\Gamma I.
\]

Otherwise form the plunge/evaluation-visible mismatch packet and run the finite
Schur complement of `L-15604`.  Only after one of these gates passes may the
count be declared saturated.

## 5. High-value numerical scouts

These are empirical scheduling tasks, not proof claims.

1. At the smallest Suzuki supports already implemented, form high-precision
   discretizations of `T_(a,G)` for several `G`.
2. Record both the threshold index and the complete tail sums after candidate
   packet ranks.
3. Compare the unconstrained tail with the exact source-constrained trace loss.
4. Optimize `G,Gamma,t,q` for the signed lower floor, not raw packet dimension.
5. Preserve the dyadic level sets of the actual deficit; they are inputs to an
   eventual directed `S_q` proof.
6. Check whether the weighted trace tail is materially smaller than the binary
   sublevel-set and plunge-visible bounds of PR #163.

A repeated inequality

```text
source-constrained weighted trace tail < G-Gamma
```

with a growing moat would be the first empirical evidence aimed directly at the
new cofinal theorem.

## 6. What would refute this route

The route fails if, on every admissible cofinal schedule, one of the following
occurs:

1. the source-constrained weighted trace tail stays above `G-Gamma`;
2. exact source repair destroys the local Gram or uniform tail rate;
3. form-continuity constants grow faster than concentration leakage decays;
4. the complete symbol deficit lacks a proof-grade `S_q` envelope;
5. an assembly term omitted from `s_a` has a nonvanishing negative radius;
6. the finite evaluation-visible Schur block retains an additional low mode.

These failures are measurable and route-specific; none can be hidden by
matching a few finite eigenvalues.

## Current verdict

The latest localization theorems provide relevant pre-plunge, plunge-count, and
singular-value estimates, but they do not prove the zeta-specific cofinal
weighted trace-tail condition.

The principal remaining analytic question is whether the exact arithmetic
weighted deficit can be captured, after the exact source constraints, with
uncaptured trace at most `G-Gamma` while the packet form and residual scales
vanish as required by `T-15602`.

No proof of that comparison, and therefore no proof of RH, is claimed here.
