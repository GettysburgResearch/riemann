# L-106040 — Squarefree composite conductors carry an exact tensor Kummer frame

Claim ID: `L-106040`  
Programme aliases: `LFAM1.COMPOSITE_KUMMER_FRAME`, `STRESS.MULTI_OWNER_LOCAL_OCCUPANCY`, `LFAM2.PRODUCT_KUMMER_MODEL`  
Status: **PROVED EXACT HILBERT-VALUED TENSOR THEOREM**  
Created: 2026-08-24  
Audited: 2026-08-24  
Depends on: `L-106020`, `L-106024`, `L-106027`; `R-106040`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let

\[
q=\prod_{j=1}^k p_j,
\qquad (q,67)=1,
\]

be odd and squarefree. The exclusion of `67` keeps the auxiliary/composite
conductor disjoint from the literal marked-prime source. Sectors containing a
physical `67` label remain in their explicit finite local ledger and are not
silently absorbed into `q`.

Let `H` be a complex Hilbert space. For every local quadratic-class vector

\[
\sigma=(\sigma_{p_j})_{j=1}^k\in\{+1,-1\}^k,
\]

fix representatives `u_(sigma,p)` of the corresponding square classes in
`F_p^*`. Let `(v_n)` be a finite `H`-valued packet whose nonzero residues lie
in that fixed class at every `p|q`.

For

\[
\mathbf h=(h_p)_{p\mid q}\in\prod_{p\mid q}\mathbf F_p
\]

define the tensor square-phase field

\[
F_{\sigma,\mathbf h}
=
\sum_n v_n
\prod_{p\mid q}e_p(h_pu_{\sigma,p}n^2).
\tag{L-106040.1}
\]

Repeated residue vectors are aggregated before applying the theorem.

## 1. Exact sector contraction

Applying the one-prime identity `L-106020` successively gives

\[
\boxed{
\|F_{\sigma,\mathbf0}\|^2
\le
c(q)
\sum_{\substack{h_p\ne0\\p\mid q}}
\|F_{\sigma,\mathbf h}\|^2,
\qquad
c(q)=\prod_{p\mid q}\frac{p-1}{p+1}.
}
\tag{L-106040.2}
\]

The constant is sharp on each sector. In sign-pair coordinates the positive
phase operator is the tensor product

\[
\boxed{
\bigotimes_{p\mid q}(pI-J).
}
\tag{L-106040.3}
\]

Its constant tensor mode has eigenvalue

\[
\prod_{p\mid q}\frac{p+1}{2},
\]

while every other tensor eigenvalue is obtained by replacing one or more local
factors `(p+1)/2` by `p`.

## 2. Character-square diagonalization

Via the Chinese remainder theorem, multiplicative characters modulo `q` are
tuples `(chi_p)_(p|q)`. Put

\[
\eta_p=\chi_p^2.
\]

The image of the square map is the product of the local even-character
subgroups. For a locally even tuple `eta`, define

\[
w_q(\eta)
=
\prod_{p\mid q}
\begin{cases}
\dfrac{p+1}{p-1},&\eta_p=1,\\[2mm]
\dfrac{2p}{p-1},&\eta_p\ne1.
\end{cases}
\tag{L-106040.4}
\]

The tensor phase energy has the exact positive decomposition

\[
\boxed{
\sum_{\substack{h_p\ne0\\p\mid q}}
\|F_{\sigma,\mathbf h}\|^2
=
\sum_{\eta\in\operatorname{im}[2]}
 w_q(\eta)\|M_{\sigma,\eta}\|^2.
}
\tag{L-106040.5}
\]

Here `M_(sigma,eta)` is the corresponding locally-even multiplicative
transform. In particular the principal even-character fibre has weight

\[
\boxed{
w_q(1)=c(q)^{-1}.}
\tag{L-106040.6}
\]

There are exactly

\[
2^k
\]

square roots of the principal even character, one for each local quadratic
character choice. Their Gauss weights combine to (L-106040.6).

## 3. Recombining quadratic-class sectors

For a general packet, split it by the full local class vector `sigma`. Then

\[
F_{\mathbf0}
=
\sum_{\sigma\in\{\pm1\}^k}F_{\sigma,\mathbf0}.
\]

Consequently

\[
\boxed{
\|F_{\mathbf0}\|^2
\le
2^k c(q)
\sum_{\sigma}
\sum_{\substack{h_p\ne0\\p\mid q}}
\|F_{\sigma,\mathbf h}\|^2.
}
\tag{L-106040.7}
\]

The factor `2^k` is only a sector-recombination cost. Keeping the sectors
source-owned until the final physical observation avoids paying it earlier.
For the CV/XD owner packets, `k` is bounded by the number of selected physical
owner labels, so this cost is absolute or subpower.

## 4. Composite principal Euler completion

Let `chi_0` be the principal character modulo `q`. Then

\[
L(s,\chi_0)
=
\zeta(s)\prod_{p\mid q}(1-p^{-s}).
\tag{L-106040.8}
\]

Therefore the full-source operator

\[
\boxed{
\prod_{p\mid q}(I-p^{-1/2}S_p)
}
\tag{L-106040.9}
\]

restores the native Möbius source coefficientwise. The literal marked-67
filter is then applied exactly as in `L-106000`; it is not one of the conductor
completion factors. The completed principal member is again the native marked
common-mother detector.

The completion must precede carrier, Wick, owner and Vaughan residual
selection, as required by `R-106001`.

## 5. Function-field reading

For a squarefree polynomial conductor

\[
\mathfrak q=\prod_j\mathfrak p_j,
\]

the same theorem is the tensor product of the local Kummer--Fourier transforms
on the residue fields `A/mathfrak p_j`. Any distinguished marked irreducible is
kept outside the conductor exactly as `67` is above. The local class vector and
all principal/quadratic roots remain explicit. No geometric RH is used.

## Scope

This theorem proves the exact local and tensor frame, its character-square
spectral decomposition, sector cost, and principal source completion. It does
not control coherent assembly over different physical owner packets, prove
`CCSOCM106040`, `HBCQDSP102888`, or RH.
