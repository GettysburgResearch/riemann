# T-15107 — Cofinal Rouché--cardinal exhaustion implies RH

Claim ID: `T-15107`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; COFINAL ROUCHÉ/CARDINAL BOUND OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15117`, `L-15119`, `L-15122`--`L-15124`, and the finite Connes--van Suijlekom real-zero theorem  
Scope: strongest explicit `c=0` cofinal completion theorem for the smooth Hermite-radical target  
Related counterexample candidates: none

## 1. Level data

Let

\[
 L_j\to\infty,
 \qquad
 N_j\to\infty,
 \qquad
 h_j=\frac{2\pi}{L_j}.
\]

Let `F_j` be the Xi-normalized finite transform of the actual smooth-window
Hermite-radical target, and let `P_j` be its degree-`2N_j` interpolation
polynomial in the integer node coordinate.

Let `beta_j^W` be the complete finite arithmetic source from the exact polar,
archimedean, and all-prime-power formula of `L-15119`.

## 2. Cofinal proof objects

Assume that, for every sufficiently large `j`, directed proof objects supply the
following data.

### A. Actual smooth target and convergence

The coefficients and transform of `F_j` are enclosed from `L-15117`, including
the smooth localization and finite Fourier tails, and

\[
 F_j\longrightarrow\Xi
 \tag{T-15107.1}
\]

locally uniformly on `|Im z|<1/2`.

### B. Complete Rouché exhaustion

There are exactly `2N_j` distinct proof-grade simple critical-line zeros

\[
 \gamma_{j,1},\ldots,\gamma_{j,2N_j}
\]

with pairwise disjoint conjugation-invariant disks satisfying every hypothesis
of `L-15124`:

- each disk isolates exactly its central simple `Xi` zero;
- each disk avoids the finite-transform skeleton;
- the directed Rouché boundary inequality holds;
- a directed derivative lower bound gives the node-coordinate displacement
  radius `delta_(j,k)`.

It follows that these disks contain all `2N_j` target-polynomial roots, each
simple and real.

### C. Selected-zero source and complete residual

Every selected zero gives its exact positive Cauchy source from `L-15122`.
Subtract the selected source from the complete arithmetic source:

\[
 \beta_j^{\rm rem}=\beta_j^W-\beta_j^{Z_j}.
 \tag{T-15107.2}
\]

At each target root, produce a directed residual residue radius

\[
 \left|
 -\frac{R_{j,\rm rem}(u_{j,k})}{P_j'(u_{j,k})}
 \right|
 \le E_{j,k}.
 \tag{T-15107.3}
\]

### D. Cardinal derivative control

For the root intervals `J_(j,l)` of `L-15124`, produce directed constants

\[
 B_{j,kl}
 \ge
 \sup_{r\in J_{j,l}}
 |\mathcal K_{j,k}'(r)|.
 \tag{T-15107.4}
\]

Let

\[
 A_{j,k}
 =m_{j,k}\frac{L_j}{\pi^2}
  \sin^2\left(\frac{L_j\gamma_{j,k}}2\right)
 >0.
 \tag{T-15107.5}
\]

Assume the strict finite inequalities

\[
 \boxed{
 A_{j,k}B_{j,kk}\delta_{j,k}
 +\sum_{l\ne k}
  A_{j,l}B_{j,kl}\delta_{j,l}
 +E_{j,k}
 <A_{j,k}}
 \tag{T-15107.6}
\]

for every target root `k`.

## 3. Finite conclusion

By `L-15124`, the target roots are simple and real.  The cardinal stability
bounds give

\[
 |\mathcal K_{j,k}(r_{j,k})-1|
 \le B_{j,kk}\delta_{j,k}
\]

and

\[
 |\mathcal K_{j,k}(r_{j,l})|
 \le B_{j,kl}\delta_{j,l}
 \qquad(l\ne k).
\]

Insert these estimates and (T-15107.3) into the exact residue identity of
`L-15122`.  Inequality (T-15107.6) yields

\[
 w_{j,k}(0)>0
 \qquad(1\le k\le2N_j).
\]

Therefore the **unshifted** arithmetic target-pinned matrix already satisfies

\[
 \boxed{
 T_{p_j}(0)\succeq0,
 \qquad
 \ker T_{p_j}(0)=\mathbb Rp_j.}
 \tag{T-15107.7}
\]

The finite special-matrix theorem implies that every zero of `F_j` is real.

## 4. Global conclusion

The finite transforms converge locally uniformly to `Xi` by (T-15107.1).  On
each nonreal half-strip they are zero free.  Hurwitz's theorem shows that `Xi`
is zero free there as well.  Hence every nontrivial zeta zero has real part
`1/2`, and

\[
 \boxed{\mathrm{RH}.}
\]

## 5. Compact asymptotic statement

It is sufficient to establish cofinally

\[
 \boxed{
 \max_k B_{j,kk}\delta_{j,k}
 +
 \max_k
 \frac{
  \sum_{l\ne k}A_{j,l}B_{j,kl}\delta_{j,l}
  +E_{j,k}}
 {A_{j,k}}
 \longrightarrow0.}
 \tag{T-15107.8}
\]

Together with the complete directed Rouché exhaustion, this one expression
closes both previously separate gates:

```text
canonical simple-real inertia
+
arithmetic scalar-line positivity.
```

The common boundary scalar is not needed; `c_j=0` works.

## 6. Why this is stronger than the earlier program

The earlier proof architecture required:

1. independent canonical inertia and moat;
2. a canonical-ray matrix LP;
3. an exact residue fallback.

The Rouché--cardinal theorem uses certified line zeros as a common coordinate
system for both the target roots and the arithmetic source.  Once every target
root is captured, simple real-rootedness follows by degree exhaustion, and the
same capture bounds control the exact residue weights.

The canonical-ray LP remains useful as a cheaper finite screen.  It is no
longer the logically final consumer.

## 7. Proof boundary

The theorem does not prove for the Riemann data:

- the existence of a cofinal schedule carrying `2N_j` isolated simple
  proof-grade line zeros inside skeleton-free disks;
- the simultaneous directed Rouché inequalities;
- tame cardinal derivative constants in growing dimension;
- decay of the complete prime-side residual residues;
- the asymptotic inequality (T-15107.8).

These are the full remaining cofinal statements.  They cannot be inferred from
local-uniform convergence, finite numerical trends, or an RH-positive all-zero
measure representation.  No proof of RH is claimed.