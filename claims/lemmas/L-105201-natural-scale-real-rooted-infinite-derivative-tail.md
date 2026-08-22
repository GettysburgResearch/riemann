# L-105201 — The complete high-derivative Xi tail is real-rooted on one common natural-scale box

Claim ID: `L-105201`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105200`; PR #720 `L-104516`  
RH status: **not assumed**

## 1. Statement

Fix constants `C,H>0`.  For every sufficiently large integer `M`, put

\[
T_M=C\sqrt{M/\log M}.
\tag{L-105201.1}
\]

For every integer `m>=M`, let `w_m,s_m` be the saddle and Gaussian width from
`L-105200`, and define the model lattice

\[
\Lambda_m=
\begin{cases}
\{(j+\tfrac12)\pi/w_m:j\in\mathbb Z\},&m\text{ even},\\
\{j\pi/w_m:j\in\mathbb Z\},&m\text{ odd}.
\end{cases}
\tag{L-105201.2}
\]

Then there is a deterministic sequence `delta_M -> 0` such that, simultaneously
for every `m>=M`, every zero of `Xi^(m)` in

\[
\mathcal R_M=\{z:|\Re z|\le T_M,\ |\Im z|\le H\}
\tag{L-105201.3}
\]

is real and simple, and every such zero lies within `delta_M/w_m` of a unique
point of `Lambda_m`.  Conversely every lattice point whose
`2 delta_M/w_m` neighbourhood is contained in `mathcal R_M` has exactly one
Xi-derivative zero in that neighbourhood.

Consequently, uniformly for every `m>=M`,

\[
\boxed{
N_m(T_M)
=\#\{x\in[-T_M,T_M]:\Xi^{(m)}(x)=0\}
={2w_mT_M\over\pi}+O(1).
}
\tag{L-105201.4}
\]

The `O(1)` is absolute once `C,H` are fixed.

## 2. Common Gaussian factor

By `L-105200`, uniformly for `m>=M` and `z in mathcal R_M`,

\[
A_m(\pm z)
=\exp\!\left(\pm iw_mz-{s_m^2z^2\over2}\right)
(1+\epsilon_{m,\pm}(z)),
\tag{L-105201.5}
\]

with

\[
\epsilon_M:=
\sup_{m\ge M,\ z\in\mathcal R_M,\ \pm}
|\epsilon_{m,\pm}(z)|\longrightarrow0.
\tag{L-105201.6}
\]

The exact companion identity gives

\[
\Xi^{(m)}(z)
=i^mM_m e^{-s_m^2z^2/2}
\left[
 e^{iw_mz}(1+\epsilon_{m,+})
 +(-1)^m e^{-iw_mz}(1+\epsilon_{m,-})
\right].
\tag{L-105201.7}
\]

The Gaussian factor never vanishes.  Thus the zero problem is a uniform small
relative perturbation of `2 cos(w_m z)` for even `m`, and of
`2i sin(w_m z)` for odd `m`.

## 3. Rouché cells at a shrinking relative radius

Choose

\[
\delta_M=\epsilon_M^{1/3}
\tag{L-105201.8}
\]

after increasing `M` so that `delta_M<pi/8`.  Around each model zero
`lambda in Lambda_m`, take

\[
D_{m,\lambda}=\{z:|z-\lambda|<\delta_M/w_m\}.
\]

On its boundary the unperturbed bracket in (L-105201.7) has modulus

\[
2|\sin(\delta_M e^{i\theta})|
\ge c\delta_M,
\]

whereas the perturbation is at most

\[
2\epsilon_M e^{\delta_M}
=o(\delta_M).
\]

Rouché therefore gives exactly one zero in every complete disk.

For the complement of the disks, factor the larger of `e^(iw_m z)` and
`e^(-iw_m z)`.  If `w_m|Im z|>=delta_M/2`, the two-exponential model has a
uniform lower bound comparable to the larger exponential.  If
`w_m|Im z|<delta_M/2`, exclusion from the disks gives a lower bound
`c delta_M` after the same factorization.  In both cases the relative error
`epsilon_M=o(delta_M)` excludes additional zeros.

The disks are conjugation invariant and disjoint.  Since `Xi^(m)` is real
entire, a nonreal zero would bring a distinct conjugate into the same disk,
contradicting the Rouché count one.  Every disk zero is therefore real.  The
same count excludes multiplicity greater than one.

## 4. Uniformity over the infinite derivative tail

The point of the theorem is the quantifier `m>=M`, not merely a fixed-fraction
band.  The natural width satisfies

\[
\sup_{m\ge M}s_mT_M=O_C(1)
\]

because `log m/m` is eventually decreasing.  Thus one common physical box
works for the entire infinite derivative tail.  No diagonal choice of `m`
after observing a zero is used.

## 5. Scope

This is a local-in-height theorem on a box growing like
`sqrt(M/log M)`.  It neither descends to a fixed derivative order nor proves
that a fixed Xi derivative is globally real-rooted.  Its conclusion-facing
use is the uniform critical-residue theorem `L-105202`.
