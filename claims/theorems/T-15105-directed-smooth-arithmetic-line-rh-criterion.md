# T-15105 — Directed smooth-window arithmetic-line criterion implying RH

Claim ID: `T-15105`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; COFINAL ARITHMETIC BOUND OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15117`--`L-15120`, `T-15104`, and the finite Connes--van Suijlekom real-zero theorem  
Scope: complete proof-producing version of the target-pinned positive program  
Related counterexample candidates: none

## 1. Data at level `j`

Let

\[
 \ell_j\to\infty,
 \qquad
 N_j\to\infty,
\]

and let `p_j` be the exact CCM coefficient vector of the actual smooth-window
Hermite-radical target from `L-15117`, boundary-normalized by

\[
 \eta^{\mathsf T}p_j=1.
\]

Assume every used coordinate is nonzero.  Let

\[
 f_j(z)
\]

be the compactly supported finite transform before boundary normalization, so
that nonzero scalar normalization does not change its zeros.

Let `beta_j` be the exact arithmetic special source of the truncated Weil
matrix in `L-15119`.

Construct the canonical Loewner matrix `Q_can,j` from `p_j` by `L-15118`.

## 2. Finite proof gates

Assume that, for every sufficiently large `j`, directed proof objects establish:

### A. Actual coefficient enclosure

Every exact smooth coefficient lies in a source-bound interval produced by
`L-15117`, with the CCM phase and normalization fixed.

### B. Canonical positive inertia

The exact canonical matrix satisfies

\[
 Q^{\rm can}_j\succeq0,
 \qquad
 \ker Q^{\rm can}_j=\mathbb Rp_j,
 \tag{T-15105.1}
\]

and has a directed positive moat

\[
 Q^{\rm can}_j\succeq m_j I
 \quad\text{on }p_j^\perp,
 \qquad m_j>0.
 \tag{T-15105.2}
\]

This may be certified by direct interval `LDL^T`, by the kernel-pinned transfer
`L-15113`, or by the Cauchy moat of `L-15118`.

### C. Actual arithmetic source

Every value of `beta_j` is enclosed from the exact polar, archimedean, and
complete prime-power formula `L-15119`.

### D. Scale-optimized arithmetic-line fit

There are rational values

\[
 t_j>0,
 \qquad q_j\in\mathbb Q,
\]

for which the directed upper endpoint of

\[
 \mathscr R_j(t_j,q_j)
 =\max_i\sum_{k\ne i}
 \left(1+\left|\frac{(p_j)_k}{(p_j)_i}\right|\right)
 \left|
 t_j(A_j)_{ik}-(Q^{\rm can}_j)_{ik}-q_j
 \right|
 \tag{T-15105.3}
\]

is strictly below `m_j`.  Here

\[
 (A_j)_{ik}
 =\frac{(\beta_j)_i-(\beta_j)_k}
        {(\lambda_j)_i-(\lambda_j)_k}.
\]

## 3. Finite conclusion

Put

\[
 a_j=t_j^{-1},
 \qquad
 c_j=q_j/t_j.
\]

Multiplying (T-15105.3) by `a_j` gives

\[
 \mathcal E_{p_j}(a_j,c_j)<a_jm_j.
\]

By `L-15120`, the actual arithmetic target-pinned matrix satisfies

\[
 \boxed{
 T_{p_j}(c_j)\succeq0,
 \qquad
 \ker T_{p_j}(c_j)=\mathbb Rp_j.}
 \tag{T-15105.4}
\]

The scalar update preserves the exact special divided-difference form and
parity.  The finite Connes--van Suijlekom theorem therefore makes every zero of
`f_j` real.

## 4. Cofinal conclusion

Assume additionally that

\[
 f_j\longrightarrow\Xi
\]

locally uniformly on `|Im z|<1/2`.  Corrected `L-15101` and the smooth
coefficient/tail construction provide this convergence once the finite
projection tail is sent to zero.

Then `T-15104` and Hurwitz imply that every nontrivial zero of zeta lies on the
critical line.  Hence

\[
 \boxed{\mathrm{RH}.}
\]

## 5. Compact asymptotic form

Define the exact/directed statistic

\[
 \Theta_j
 =\frac1{m_j}
  \inf_{t>0,q\in\mathbb R}\mathscr R_j(t,q).
 \tag{T-15105.5}
\]

The numerator is a two-variable convex piecewise-linear program.  Therefore

\[
 \boxed{
 \limsup_{j\to\infty}\Theta_j<1}
 \tag{T-15105.6}
\]

plus target convergence proves RH.  The stronger condition `Theta_j->0` is
sufficient but not necessary.

This is the corrected final full proof-producing program:

```text
actual smooth-window coefficient intervals
    -> directed canonical Loewner inertia and moat
    -> exact arithmetic source / residue-line data
    -> exact rational two-variable canonical-ray LP
    -> cofinal strict moat
    -> RH.
```

## 6. What has been completed

The first three arrows now have exact analytic formulas and fail-closed finite
certificate interfaces:

1. `L-15117`: actual smooth coefficient balls;
2. `L-15118/L-15113`: canonical matrix, inertia, and moat;
3. `L-15119`: actual arithmetic source;
4. `L-15120/X-15106`: scale-optimized exact finite consumer.

The remaining theorem is the zeta-specific cofinal inequality
(T-15105.6).  A finite ladder, however long, is evidence only.

## 7. Gap audit

1. Canonical positivity is already RH-bearing for a convergent target sequence;
   it cannot be obtained from approximation theory alone.
2. The canonical-ray criterion is sufficient, not necessary.  A failed LP must
   be followed by the exact residue-orthant threshold test of `L-15114`.
3. The hard-window computations on PR #173 do not replace the smooth target
   intervals.
4. The arithmetic source must include every prime power and directed
   archimedean/polar terms.
5. This theorem is an implication, not a proof that (T-15105.6) holds.