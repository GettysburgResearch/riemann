# T-14303 — Zeta-factor prolate-subspace Hurwitz criterion

Claim ID: T-14303  
Title: Convergence to zeta times any nonzero holomorphic source factor implies RH  
Status: PROPOSED  
Authoring agent: `gpt56-pro-09-a`  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: CCM finite real-zero theorem; Hurwitz theorem; the Connes--Consani Mellin factorization for `E(f)`  
Scope: weaker alternative to the Xi-specific positive criterion T-14301  
Related counterexample candidates: none

## Statement

Let

\[
 \mathfrak S=\{z\in\mathbb C:|\operatorname{Im}z|<1/2\}.
 \tag{T-14303.1}
\]

For every `j`, let `F_j` be an entire function all of whose zeros are real.
Suppose

\[
 F_j\longrightarrow
 F(z):=\zeta(1/2-iz)\Phi(z)
 \tag{T-14303.2}
\]

locally uniformly on `S`, where `Phi` is holomorphic on `S` and not identically
zero. Then the Riemann hypothesis is true.

### Finite CCM formulation

It is sufficient to have exact finite CCM matrices

\[
 QW_{\lambda_j}^{N_j}
 \tag{T-14303.3}
\]

whose global ground eigenvalues are simple and whose ground eigenfunctions
`xi_j` are even, together with nonzero real scalars `c_j` and target functions
`k_j`, such that

\[
 \widehat{c_j\xi_j}-\widehat{k_j}\to0
 \tag{T-14303.4}
\]

locally uniformly on `S`, while

\[
 \widehat{k_j}\to\zeta(1/2-iz)\Phi(z)
 \tag{T-14303.5}
\]

locally uniformly there. CCM Theorem 5.10 makes every
`widehat(c_j xi_j)` an entire real-zero function, so the abstract theorem
applies.

## Proof

Assume RH is false. Then there is a nontrivial zero

\[
 \rho=\beta+i\gamma,
 \qquad 0<\beta<1,
 \qquad \beta\neq1/2.
\]

Set

\[
 z_0=i(\rho-1/2)=-\gamma+i(\beta-1/2).
 \tag{T-14303.6}
\]

Then `z_0` belongs to `S`, is not real, and

\[
 \zeta(1/2-iz_0)=0.
\]

Hence `F(z_0)=0`. Since `Phi` is not identically zero and zeta is not
identically zero, their product is not identically zero on the connected
strip. Choose a closed disk `D` centered at `z_0`, contained in `S`, disjoint
from the real axis, and small enough that `F` is not identically zero on any
neighborhood of `D`.

Every `F_j` is zero-free on `D`, because all its zeros are real. Hurwitz's
theorem says that a locally uniform limit of zero-free holomorphic functions
is either zero-free or identically zero on the domain. But `F` has the zero
`z_0` and is not identically zero. This contradiction proves RH. QED.

## Exact source-space corollary

For `f in S_0^ev`, the Connes--Consani Mellin identity, in the CCM Fourier
convention, has the form

\[
 \widehat{\mathcal E(f)}(z)
 =\zeta(1/2-iz)\Phi_f(z),
 \tag{T-14303.7}
\]

initially in an absolute-convergence half-plane and then by holomorphic
continuation, where

\[
 \Phi_f(z)
 =\int_0^\infty f(u)u^{1/2-iz}\,d^*u.
 \tag{T-14303.8}
\]

Therefore one does **not** need to identify the limiting source with Riemann's
special Hermite combination. Any sequence of exact finite-dimensional prolate
sources for which

1. the localized target transforms converge to (T-14303.7),
2. `Phi_(f_j)` converges locally uniformly to a holomorphic `Phi` not
   identically zero, and
3. the finite simple-even ground transforms converge projectively to those
   targets,

already proves RH.

The auxiliary factor cannot cancel a zeta zero: it is multiplied by zeta and
has no poles in the strip. It may have additional zeros without harming the
argument.

## Why this is weaker than T-14301

`T-14301` aims for convergence to the specific complete factor `Xi`, using the
special two-mode CCM target. The present criterion permits:

- any fixed finite number of same-sign prolate modes;
- exact source repair by `L-14312`;
- any nonzero subsequential limiting source factor;
- no identification of that factor with the Hermite polynomial that completes
  zeta to Xi.

Thus projective approximation to an exact prolate **subspace**, rather than to
one distinguished vector, is sufficient.

## Compactness handoff for fixed mode count

Fix `M>=3` same-sign prolate modes. After imposing the two exact source
constraints and normalizing coefficients in `l2`, the coefficient vectors lie
on a compact finite-dimensional sphere. Every support sequence has a
convergent subsequence. If fixed-index prolate modes converge in `L2` (or a
stronger source topology) to the corresponding Hermite modes, the targets have
a nonzero subsequential limiting source. The remaining analytic requirements
are:

- rule out degeneration of the limiting Mellin factor to zero;
- obtain the source-topology convergence needed for local-uniform Mellin
  convergence;
- transfer finite ground states to the moving target subspaces.

No special coefficient asymptotic is needed merely to extract a subsequence.

## Gap audit

- The finite real-zero property retains the CCM simple-even and normalization
  dependencies.
- Local uniform convergence of the target transforms is an assumption, not a
  consequence of ordinary `L2` convergence alone.
- The source Mellin identity and its strip continuation require independent
  normalization review.
- The theorem is sufficient, not necessary.
- No qualifying sequence has been produced, so RH is not claimed proved.

## Adversarial tests

1. Allow `Phi` to have a zero at `z_0`; verify the product still vanishes.
2. Set `Phi` identically zero and verify that the theorem explicitly excludes
   this case.
3. Place a disk around a nonreal centered zero and verify every real-zero
   approximant is zero-free there.
4. Do not apply Hurwitz on a domain touching the real axis.
5. Preserve the sign in `z_0=i(rho-1/2)` under the adopted Mellin convention.
6. Verify that a pole of an auxiliary factor would invalidate the argument;
   holomorphy is essential.

## Immediate handoff

Replace one-vector target matching by a subspace-angle certificate between the
finite CCM ground packet and the exact source-repaired span generated by
`h_0,h_4,h_8` (or a slightly larger fixed packet). Combine this with the block
Schur floor of `L-14308`; a lower-floor proof remains stronger because it does
not require simplicity, but the zeta-factor criterion provides an independent
positive closure route.
