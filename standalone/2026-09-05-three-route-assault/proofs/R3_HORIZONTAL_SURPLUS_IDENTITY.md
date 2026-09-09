# Route 3: exact basis-free horizontal surplus in the Hilbert pair energy

Status: complete proof supplied, **PROPOSED / INDEPENDENT REVIEW REQUIRED**.
Scope: finite conjugation-invariant multisets, arbitrary positive integer multiplicities, a quantified horizontal Schur complement, and conditional analytic corollaries. No new zeta-zero percentage or RH conclusion.
Sources: the finite Hilbert framework summarized in PR #788 at `a9c7b44f908c90f63d2f49a5fde58face5921e42`. The proof below is self-contained and does not assume a pair-correlation theorem.
What was run: exact rational finite Hilbert models, independently reconstructed ordered-pair energies, full flag identities, Schur complements, and sharp one-pair equalities.
Smallest remaining gap: an arithmetic estimate for the **unaveraged, conditioned horizontal defect** that survives a complete zero-window/tail passage.

This is the main constructive theorem of the pass. It retains an explicit nonnegative matrix quantity before the Hilbert proof collapses to a count. The calculation uses standard projection and Schur-complement algebra; no external priority claim is made.

## R3.1. Definitions and finite source operator

Let `Z` be a finite set of distinct complex numbers stable under conjugation. Let `m_z` be positive integers with `m_bar(z)=m_z`. Let `eta` be a real even compactly supported `L^2` function with

\[
 \int\eta(t)^2dt=1,
\]

nonzero almost everywhere on some interval. Work in complex `L^2(R)`, with inner product linear in its second slot. Define

\[
 \phi_z(t)=\eta(t)e^{izt},\quad
 k(z)=\int\eta(t)^2e^{izt}dt,\quad
 A=\sum_{z\in Z}m_z|\phi_z\rangle\langle\phi_{\bar z}|.
 \tag{1}
\]

`A` is self-adjoint, finite rank, and

\[
 \operatorname{Tr}A=M:=\sum_zm_z,
\quad
 \mathcal E:=\|A\|_{HS}^2
 =\operatorname{Re}\sum_{z,w\in Z}m_zm_w k(z-w)^2.
 \tag{2}
\]

To check the second identity, expand `Tr(A^2)`. The two inner products are `k(w-z)` and `k(z-w)`, equal because `eta^2` is even. The ordered sum is real after conjugate pairing. No termwise positivity of its individual complex summands is assumed.

For one representative from each conjugate pair with `Im z>0`, put

\[
 r_z=(\phi_z+\phi_{\bar z})/2,\quad
 o_z=(\phi_z-\phi_{\bar z})/2.
\]

Then

\[
 A=\sum_{z\in Z\cap\mathbb R}m_z|\phi_z\rangle\langle\phi_z|
 +2\sum_{\Im z>0}m_z
 (|r_z\rangle\langle r_z|-|o_z\rangle\langle o_z|),
 \tag{3}
\]

and `||r_z||^2-||o_z||^2=1`.

Distinct exponentials are linearly independent on an interval. Therefore the vectors in (3), with one real vector per real support point and two vectors per nonreal pair, are linearly independent. Repeated zero multiplicity is carried by `m_z`, not by duplicating identical columns.

## R3.2. The intrinsic flag

Let

\[
 U=\operatorname{span}\{\phi_x:x\in Z\cap\mathbb R,\ m_x>1\}
       +\operatorname{span}\{r_z:\Im z>0\},
\]

\[
 V=\operatorname{span}\{\phi_x:x\in Z\cap\mathbb R\}
       +\operatorname{span}\{r_z:\Im z>0\},
 \qquad W=\operatorname{span}\{\phi_z:z\in Z\}.
\]

Let `P_U`, `P_V`, and `P_W` be their orthogonal projections and set

\[
 P_E=P_V-P_U,\qquad P_N=P_W-P_V.
\]

These are pairwise orthogonal projections resolving `P_W`. Write

\[
 u=\dim U,\quad S=\#\{x\in Z\cap\mathbb R:m_x=1\},\quad
 q=\#\{z\in Z:\Im z>0\}.
\]

Then `dim(P_E)=S`, `dim(P_N)=q`, and

\[
 d:=M-S-2u
 =\sum_{x\in Z\cap\mathbb R,\ m_x>1}(m_x-2)
    +2\sum_{\Im z>0}(m_z-1)\ge0.
 \tag{4}
\]

Define the nonnegative quantities

\[
 \ell=\sum_{x\in Z\cap\mathbb R,\ m_x=1}\|P_U\phi_x\|^2,
\quad
 h_E=\sum_{\Im z>0}m_z\|P_Eo_z\|^2,
\quad
 h_N=\sum_{\Im z>0}m_z\|P_No_z\|^2.
 \tag{5}
\]

They are basis independent. They do depend on the complete finite multiset and on the test function.

## R3.3. Exact positive-surplus identity

Write `A_ij=P_i A P_j`, for `i,j` in `{U,E,N}`, and define

\[
 \mathcal R=
 \|A_{UU}-2P_U\|_{HS}^2+
 \|A_{EE}-P_E\|_{HS}^2+
 \|A_{NN}\|_{HS}^2
 +2\sum_{i<j}\|A_{ij}\|_{HS}^2.
 \tag{6}
\]

**Theorem.** At every such finite multiset, including arbitrary multiplicities,

\[
 \boxed{
 \mathcal E-(2M-S)
 =2d+2\ell+4h_E+8h_N+\mathcal R.
 }
 \tag{7}
\]

Every term on the right is nonnegative.

### Proof

Because `A=P_W A P_W`, the Hilbert–Schmidt block decomposition is exact:

\[
 \mathcal E=\sum_i\|A_{ii}\|_{HS}^2+2\sum_{i<j}\|A_{ij}\|_{HS}^2.
\]

Complete squares on the first two diagonal blocks. This gives

\[
 \mathcal E=4\operatorname{Tr}A_{UU}-4u
             +2\operatorname{Tr}A_{EE}-S+\mathcal R.
\]

Subtract `2M-S`, using `M=Tr A_UU+Tr A_EE+Tr A_NN`, to obtain

\[
 \mathcal E-(2M-S)=2\operatorname{Tr}A_{UU}-4u
                         -2\operatorname{Tr}A_{NN}+\mathcal R.
\]

All positive vectors from (3) lie in `V`; the multiple-real and even-pair vectors lie in `U`. Therefore

\[
 \operatorname{Tr}A_{NN}=-2h_N,
\quad
 \operatorname{Tr}A_{UU}=M-S+\ell+2h_E+2h_N.
\]

Substitution gives precisely (7). No discarded boundary or finite-rank remainder is involved. QED.

## R3.4. The horizontal matrix is an explicit Schur complement

Choose any basis-column map `B` for `V` and let `C` have columns `sqrt(m_z)o_z` over nonreal pairs. Put

\[
 G_B=B^*B,\qquad
 \boxed{H=C^*C-C^*B(G_B)^{-1}B^*C=C^*P_NC.}
 \tag{8}
\]

`G_B` is positive definite. The full source columns are independent, so `H` is positive definite if `q>0`; when `q=0` it is the empty matrix. In particular,

\[
 H=0\ \Longleftrightarrow\ Z\subset\mathbb R,
\]

where the equality means no horizontal directions, not absence of multiple real points. Its traces satisfy

\[
 h_N=\operatorname{Tr}H,\qquad
 A_{NN}=-2(P_NC)(P_NC)^*,\qquad
 \|A_{NN}\|_{HS}^2=4\operatorname{Tr}(H^2).
 \tag{9}
\]

Consequently (7) implies the strengthened Hilbert inequality

\[
 \boxed{\mathcal E\ge2M-S+8\operatorname{Tr}H+4\operatorname{Tr}(H^2).}
 \tag{10}
\]

This is a concrete answer to the proposed horizontal-energy extraction problem: the extra term is explicit, nonnegative, basis independent, and vanishes exactly for real support. It is not an assumption of positive definite behavior for the original indefinite source operator.

## R3.5. Sharp simple-packet improvement

If all multiplicities equal one and `q>0`, then `u=q` and `d=0`. Also

\[
 \operatorname{Tr}(A_{UU}-2P_U)=\ell+2h_E+2h_N\ge2h_N.
\]

Cauchy–Schwarz on this `q`-dimensional block and on `H` therefore gives

\[
 \boxed{\mathcal E\ge2M-S+8h_N+8h_N^2/q.}
 \tag{11}
\]

For a single conjugate pair and no real points, `r_z` and `o_z` are orthogonal because `eta` is even. The two nonzero eigenvalues are `2(1+h_N)` and `-2h_N`, so equality holds in (11):

\[
 \mathcal E=4+8h_N+8h_N^2.
\]

Thus the one-pair constants are sharp. Formula (11) is not applied to mixed-multiplicity packets; (7) and (10) handle those.

## R3.6. Exact defect-versus-energy tradeoff

Let `b=M-S`, the total multiplicity not belonging to simple real points. Rearranging (10) gives

\[
 \boxed{b+8\operatorname{Tr}H+4\operatorname{Tr}(H^2)\le\mathcal E-M.}
 \tag{12}
\]

Thus an external analytic estimate `E<=C_eta M+o(M)` implies

\[
 b+8\operatorname{Tr}H+4\operatorname{Tr}(H^2)
 \le(C_\eta-1)M+o(M).
 \tag{13}
\]

This is a conditional analytic corollary with an exact displayed premise. In the Lamzouri application that premise comes from the pair-correlation adapter. This pass has not independently reconstructed that full analytic adapter or its error uniformity.

For orientation, near the Montgomery–Taylor constant `C_eta≈1.3274992963`, (13) pays both the ordinary count defect and an additional conditioned horizontal energy out of the same `≈0.3274992963 M` budget. The kernel must be fixed with its own admissibility and error statement. Passing through a sequence of near-extremizers does not silently give uniformity in a growing-support family.

This is not a new critical-line percentage. The additional nonnegative quantity can be arbitrarily small after screening, as the companion note proves. In particular, normalized control of it does not exclude one exceptional zero.

## R3.7. Quantitative survival under an omitted-source error

Let `R` be any self-adjoint bounded perturbation, such as a separately bounded tail error. If

\[
 \|P_N R P_N\|_{op}<2\lambda_{\max}(H),
 \tag{14}
\]

then `A+R` has a negative quadratic direction. If the norm is smaller than `2 lambda_min(H)`, all `q` negative directions of this compression survive. This is immediate from (9) and the variational principle.

Convenient sufficient bounds are

\[
 \lambda_{\max}(H)\ge\operatorname{Tr}H/q,
\]

and, for `q>=2`,

\[
 \lambda_{\min}(H)\ge
 \frac{(q-1)^{q-1}\det H}{(\operatorname{Tr}H)^{q-1}}.
 \tag{15}
\]

For (15), bound the product of the other eigenvalues by the arithmetic–geometric mean inequality. For `q=1`, the eigenvalue is simply `Tr H`.

The criterion makes the analytic debt explicit: a tail estimate must beat the **conditioned** horizontal gap. It cannot be compared merely to the raw norm of a nonreal exponential.

## R3.8. End-to-end continuation

For the zeta problem, set `z=-i(rho-1/2)` or use the parent's explicitly rescaled version. Critical-line zeros become real points and functional-equation pairs become conjugates. The exact theorem then applies to every finite invariant window.

To close RH one still needs an arithmetic theorem making any nonzero `H` impossible after localization and a complete tail passage. The theorem must either handle an arbitrary finite exceptional zero directly or give an effective all-high-zero exclusion with a fully checked finite remainder. Neither a global `o(M)` error nor a positive-density reservoir supplies that conclusion.
