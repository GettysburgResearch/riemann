# General inverse moments: residual conductors and the singleton remainder

Status: proposed proved partial moment theorems and an exact reduction. The requested short-row generalized inverse moment is not proved. No new zero-free boundary is asserted.

Scope: every fixed integer moment order over the Eisenstein field; arbitrary bounded squarefree coefficients for the controlled sectors; the exact Möbius coefficient for the sign identity. All local zero extensions and principal masks are retained. The completed-character estimates concern a smooth positive majorant of the full row moment. They are not asserted for individually selected pieces of the sharp row sum.

Dependencies: elementary ideal counting and prime-incidence algebra; the primitive finite-field Gauss-sum identity; Euclidean Poisson summation with a fixed smooth radial test. The proof does not use the imported quasi-Riemann theorem or an unproved inverse moment. The primitive-character completion argument is also resident in [PR #912, LONG_ROW_AND_OBSTRUCTION.md, Section 1.1](https://github.com/GettysburgResearch/riemann/blob/6afd64e042ce7b59d550c3d76e9e2cca8b2c7379/standalone/2026-10-10-generalized-inverse-moments/LONG_ROW_AND_OBSTRUCTION.md), frozen head `6afd64e042ce7b59d550c3d76e9e2cca8b2c7379`; it is reproved here to expose the exact mask and smoothing contracts.

Source context read: `AGENTS.md`, the current scientific-status material, PR #913 at `6498d6cc2eded03159c7332b25fd224ad07f89c1`, specifically `GENERAL_MOMENT_ATTACK.md`, `REFINED_ALL_ROW_SIEVE.md`, `MOMENT_OBSTRUCTIONS.md`, and the #912 generalized inverse-moment packet at the exact head above. This note is additional proposed mathematics, not a promotion of any branch to the integrated record.

What was actually run: the author's initial local-pattern enumeration and the packet's independently written `checks/check_local_structure.py`. The latter exhausts every left/right incidence pattern through k = 7, checks finite-field symbols and exact zero extensions, and reconstructs five finite full-row moments from the new disjoint regions. The sharp finite tests authenticate algebra; they do not test the asymptotic smooth completion bound. The proofs below establish the quantified analytic statements.

Smallest remaining gap: the signed smooth contribution from tuples that contain singleton primes and whose singleton/double complexity exceeds the row length. The complete estimate for that contribution remains open.

## 1. Main findings

Write the Hermitian expansion of the 2k-th moment over tuples

\[
\mathbf t=(n_1,\ldots,n_k,m_1,\ldots,m_k).
\]

For each occurring prime ideal p let r_p be its number of occurrences on the n side, s_p its number on the m side, e_p = r_p-s_p, and m_p = r_p+s_p. Its residual character is determined by e_p modulo 6, with a principal coprimality mask when that residue is zero.

The following controlled regions are unconditional.

1. **Low primitive conductor.** The sum of the absolute values of completed off-diagonal tuple contributions with primitive conductor norm at most F is

   \[
   \ll D^{k+\epsilon}F.
   \]

   It therefore has the desired moment size when F <= H.

2. **Residual-type refinement.** If f_j is the product of primes with residual exponent j, and Nf_j lies in a dyadic block F_j, the corresponding absolute completed contribution is

   \[
   \ll D^{k+\epsilon}(F_1F_5)(F_2F_4)^{1/2}.
   \]

   Quadratic residual primes, j = 3, cost only logarithms. Thus the entire pure quadratic off-diagonal sector is O(D^{k+epsilon}), independently of H >= 1.

3. **Actual multiplicity is stronger than residual type.** Let g_1 be the product of primes occurring exactly once in the full 2k tuple. Let g_2 be the product of nonprincipal primes occurring exactly twice; these necessarily occur twice on the same side and give cubic residual characters. Then every region with

   \[
   \boxed{(Ng_1)\sqrt{Ng_2}\le H}
   \]

   has absolute completed contribution O(HD^{k+epsilon}). All nonprincipal primes occurring three times cost logarithms; those occurring at least four times have a convergent normalized cost.

4. **Every tuple with no singleton prime is already controlled**, for every fixed k and every H >= 1, even with the sharp row cutoff. Their number is O(D^{k+epsilon}), and their total absolute row contribution is O(HD^{k+epsilon}). This includes the entire sector with no residual primes of type j = 1 or 5, at every moment order. It is stronger than only checking that sector at the fourth moment.

These statements narrow the open Hermitian moment problem to an explicit class of terms with genuine singleton primes. They do not bound that class in full.

## 2. Exact source, coefficients, and row majorant

Let K = Q(sqrt(-3)), O = Z[omega], and let S be the fixed excluded primes, including the primes above 2 and 3. Use the established primary-generator convention. For a squarefree good ideal n write

\[
\chi_n(u)=(u/n)_6,
\]

with its exact zero extension when (u,n) is nontrivial.

Fix k >= 1 and b >= 1. Let a_n be arbitrary complex coefficients, |a_n| <= 1, supported on squarefree ideals prime to S with Nn <= bD. Put

\[
F_u(D)=\sum_n a_n\chi_n(u).
\]

The inverse polynomial is obtained by taking

\[
a_n=\mu_K(n)\nu(n)W(Nn/D)
\]

and rescaling by the fixed supremum norm of W if needed. Only the support and supremum norm enter the controlled-sector bounds.

Choose a fixed nonnegative radial Phi in C_c^infinity(C) with Phi(z) >= 1 for |z| <= 1. Define

\[
\mathcal M_{2k}^{\Phi}(D,H)
=\sum_{u\in O}\Phi(u/\sqrt H)|F_u(D)|^{2k},\qquad H\ge1.
\tag{2.1}
\]

The possible u = 0 term is harmless and nonnegative; it is retained only to use lattice Poisson summation. The requested moment satisfies

\[
\sum_{0<Nu\le H}|F_u(D)|^{2k}\le\mathcal M_{2k}^{\Phi}(D,H).
\tag{2.2}
\]

This inequality is applied to the **full nonnegative moment**. It is not applied to a signed subset of its expansion.

For a tuple t let

\[
c(\mathbf t)=a_{n_1}\cdots a_{n_k}
\overline{a_{m_1}\cdots a_{m_k}},
\]

and let S_t^Phi(H) be its complete smooth row character sum. Then

\[
\mathcal M_{2k}^{\Phi}(D,H)
=\sum_{\mathbf t}c(\mathbf t)S_{\mathbf t}^{\Phi}(H).
\tag{2.3}
\]

For a selected collection T of tuples define the positive accounting quantity

\[
\mathcal Q_{\mathcal T}^{\Phi}
=\sum_{\mathbf t\in\mathcal T}|c(\mathbf t)|
|S_{\mathbf t}^{\Phi}(H)|.
\tag{2.4}
\]

Every controlled-sector theorem below bounds (2.4). Consequently it bounds the absolute value of the actual signed sector contribution.

All constants may depend on K, k, b, S, Phi and epsilon, but not D, H, or moving conductor/mask ideals. We assume D >= 2. Empty parameter ranges contribute zero.

## 3. Primitive residual conductor and the exact principal mask

At a good prime p occurring in the tuple, define

\[
r_p=\#\{i:p\mid n_i\},\quad
s_p=\#\{i:p\mid m_i\},\quad
e_p=r_p-s_p,\quad m_p=r_p+s_p.
\]

Let

\[
q=\operatorname{rad}(n_1\cdots n_km_1\cdots m_k),
\quad f=\prod_{p\mid q:\ e_p\not\equiv0\ (6)}p,
\quad q_0=q/f.
\tag{3.1}
\]

At a prime p | f the nontrivial local character chi_p^{e_p mod 6} is primitive modulo p. Their product psi_t is primitive modulo f. The complete row factor is exactly

\[
\psi_{\mathbf t}(u)\mathbf1_{(u,q_0)=1}.
\tag{3.2}
\]

When f = 1, psi_t is the constant function one, and (3.2) is purely the principal mask. Negative exponents are used only on units: the literal original factor at a nonunit is zero. Formula (3.2) keeps that zero at every prime of q, including the primes where the residual exponent is a multiple of six.

The exact primitive conductor is f because every local component at a prime of f is nontrivial modulo that prime. Raising a sextic character to a nonzero power modulo six can reduce its order but does not remove that prime from its conductor.

## 4. Smooth completion bound, including all masks

### Lemma 4.1

For every nonprincipal primitive character psi modulo a nonunit good squarefree ideal f, and every T > 0,

\[
\left|\sum_{u\in O}\psi(u)\Phi(u/\sqrt T)\right|
\ll_{\Phi,K}\sqrt{Nf}.
\tag{4.1}
\]

For every squarefree q_0 coprime to f,

\[
\boxed{
|S_{\mathbf t}^{\Phi}(H)|
\ll_{\Phi,K}d_K(q_0)\sqrt{Nf}\qquad(f\ne1).
}
\tag{4.2}
\]

**Proof.** Split the first sum into residue classes modulo f and apply Euclidean Poisson summation. Since O is a fixed planar lattice and its principal ideal f is a rotation and dilation of that lattice, the primitive Gauss-sum identity and rapid Fourier decay give, for any fixed A > 2,

\[
\left|\sum_u\psi(u)\Phi(u/\sqrt T)\right|
\ll_{\Phi,A,K}\frac{T}{\sqrt{Nf}}
\sum_{0\ne v\in O}
(1+\sqrt{T/Nf}|v|)^{-A}.
\tag{4.3}
\]

The zero frequency vanishes because psi is nonprincipal. All nonzero-frequency Gauss sums have absolute value at most sqrt(Nf). For every r > 0, planar lattice counting gives

\[
\sum_{v\ne0}(1+\sqrt r|v|)^{-A}\ll_{A,K}r^{-1}.
\]

For r <= 1 this follows from the planar integral and a bounded central contribution; for r >= 1 use the convergent sum of |v|^{-A} and r^{-A/2} <= r^{-1}. Substitution into (4.3) proves (4.1).

For (4.2), inclusion-exclusion and u = dv give

\[
S_{\mathbf t}^{\Phi}(H)
=\sum_{d\mid q_0}\mu_K(d)\psi_{\mathbf t}(d)
\sum_v\psi_{\mathbf t}(v)
\Phi\!\left(v/\sqrt{H/Nd}\right).
\tag{4.4}
\]

The radiality of Phi removes the rotation caused by the chosen generator of d. The scale H/Nd is allowed to be below one, since (4.1) holds for every positive scale. There are d_K(q_0) terms, and their exterior factors have modulus at most one. This proves (4.2). No principal mask has been dropped. QED.

The trivial bound, for principal or nonprincipal tuples, is

\[
|S_{\mathbf t}^{\Phi}(H)|\ll_{\Phi,K}H,
\tag{4.5}
\]

because H >= 1. The corresponding sharp-row sum also has absolute value O_K(H).

## 5. Counting tuples with specified residual ideals

For each nonempty incidence pattern (I,J), with I,J subsets of [k], put in q_{I,J} all primes occurring in exactly the n factors indexed by I and the m factors indexed by J. These ideals are squarefree and pairwise coprime. They determine the tuple uniquely.

There are at most 2^{2k}-1 available patterns. For a fixed squarefree ideal q, assigning each prime to a pattern gives at most

\[
(2^{2k}-1)^{\omega_K(q)}\ll_{k,\delta}(Nq)^\delta
\tag{5.1}
\]

choices for every delta > 0. To see the last inequality directly, choose a fixed norm threshold above which the constant 2^{2k}-1 is at most (Np)^delta. The finitely many smaller primes contribute only a fixed constant, since q is squarefree.

Also

\[
\prod_iNn_i\prod_iNm_i
=\prod_{p\mid q}(Np)^{m_p}\le(bD)^{2k}.
\tag{5.2}
\]

Every prime of the principal mask q_0 has m_p >= 2: a single occurrence has residual exponent 1 or 5 and cannot be principal.

### Proposition 5.1: fixed conductor count

For a fixed nonunit squarefree primitive conductor f, the number of compatible tuples is

\[
\ll_{k,b,\epsilon}D^{k+\epsilon}(Nf)^{-1/2}.
\tag{5.3}
\]

**Proof.** Every prime of f occurs at least once, and every prime of q_0 occurs at least twice. Therefore

\[
(Nf)(Nq_0)^2\le(bD)^{2k},
\quad Nq_0\le(bD)^k(Nf)^{-1/2}=:Z.
\]

If Z < 1 there are no tuples. Otherwise there are O_K(Z) possible ideals q_0. For each f q_0, (5.1) bounds all allocations to the 2k factors by D^epsilon after decreasing the preliminary exponent. Dropping the individual factor-support constraints only enlarges this count. This gives (5.3). QED.

The same argument permits the extra factor d_K(q_0) from (4.2), at a further arbitrary small-power cost. This is uniform in the moving f and q_0.

### Theorem 5.2: complete low-conductor sector

For every F >= 1,

\[
\boxed{
\sum_{\substack{\mathbf t:\1<Nf(\mathbf t)\le F}}
|c(\mathbf t)|\,|S_{\mathbf t}^{\Phi}(H)|
\ll_{k,b,\Phi,\epsilon}D^{k+\epsilon}F.
}
\tag{5.4}
\]

**Proof.** Fix f. In the counting proof, weight each tuple by the right side of (4.2). The d_K(q_0) factor is absorbed by (5.1)'s small-power allowance, and sqrt(Nf) cancels the factor (Nf)^{-1/2} in (5.3). Thus each f costs O(D^{k+epsilon}). There are O_K(F) ideals with norm at most F. QED.

Taking F = H controls this entire off-diagonal sector at the desired scale, independently of the original inverse coefficient. Taking F = (bD)^{2k} recovers the earlier general O(D^{3k+epsilon}) completed off-diagonal bound. The low-conductor statement is a more precise version of that bound, not a proof that the high-conductor portion is small.

## 6. Residual type: sextic, cubic, and quadratic costs

Write

\[
f_j=\prod_{p\mid q:\e_p\equiv j\ (6)}p,
\qquad 1\le j\le5.
\]

Then f = f_1...f_5. The minimum possible multiplicities are

| Residual j | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Minimum m_j | 1 | 2 | 3 | 2 | 1 |
| Character order | 6 | 3 | 2 | 3 | 6 |

At orders k too small for a displayed residue, that sector is empty. In particular j = 3 is absent at k = 1,2.

Consequently, for fixed pairwise-coprime f_1,...,f_5,

\[
\#\{\text{compatible tuples}\}
\ll D^{k+\epsilon}
\bigl(Nf_1\,Nf_5\bigr)^{-1/2}
\bigl(Nf_2\,Nf_4\bigr)^{-1}
(Nf_3)^{-3/2}.
\tag{6.1}
\]

This follows from the same q_0 count, now using

\[
(Nq_0)^2(Nf_1)(Nf_5)(Nf_2)^2(Nf_4)^2(Nf_3)^3
\le(bD)^{2k}.
\]

### Theorem 6.1: residual-type block bound

On a dyadic block F_j <= Nf_j < 2F_j, omitting the principal conductor,

\[
\boxed{
\mathcal Q_{\mathbf F}^{\Phi}
\ll D^{k+\epsilon}(F_1F_5)(F_2F_4)^{1/2}.
}
\tag{6.2}
\]

**Proof.** Multiply (6.1) by the completion cost sqrt(Nf_1...Nf_5), absorbing the mask divisor count. Sum over each f_j in its block. The j = 1,5 weights become one and their ideal counts give F_1,F_5. The j = 2,4 weights are (Nf_j)^{-1/2}, whose block sums are O(F_j^{1/2}). The j = 3 weight is (Nf_3)^{-1}, whose block sum is O(1). Dropping all pairwise-coprimality and coupled norm restrictions is legitimate in this positive majorant. QED.

There are O_k((log(2D))^5) nonempty blocks. It follows that the entire region

\[
(Nf_1Nf_5)\sqrt{Nf_2Nf_4}\le H
\tag{6.3}
\]

has contribution O(HD^{k+epsilon}). The pure quadratic nonprincipal sector, f_1 = f_2 = f_4 = f_5 = 1, has contribution O(D^{k+epsilon}), because only the harmonic f_3 sum remains.

The criterion (6.3) is stronger than merely Nf <= H: its left side is at most Nf. A large primitive conductor arising from sufficiently repeated cubic or quadratic primes need not be part of the hard remainder.

## 7. Actual incidences leave only two sources of power loss

For 1 <= m <= 2k define g_m to be the product of primes with

\[
m_p=m,\qquad e_p\not\equiv0\pmod6.
\]

These are the nonprincipal residual primes, grouped by **actual total multiplicity**. The ideals g_m are squarefree and pairwise coprime, and f = product_m g_m. The principal-mask primes remain in q_0. **All completed accounting quantities in this section restrict to f != 1.** Principal tuples, for which every g_m is the unit ideal, are handled separately in Section 8; they cannot be bounded by the nonprincipal completion estimate.

Every singleton prime belongs to g_1. A nonprincipal double belongs to g_2 and has pattern (r,s) = (2,0) or (0,2), hence a cubic residual. A double with pattern (1,1) is principal and belongs to q_0.

For fixed g_1,...,g_{2k}, (5.2) gives

\[
Nq_0\le(bD)^k\prod_{m=1}^{2k}(Ng_m)^{-m/2}.
\]

The allocation count therefore gives, with the mask divisor weight included,

\[
\sum_{\text{compatible tuples}}|c(\mathbf t)|d_K(q_0)
\ll D^{k+\epsilon}\prod_{m=1}^{2k}(Ng_m)^{-m/2}.
\tag{7.1}
\]

If the right side's unrounded norm cutoff is below one, there are no tuples.

Combining (7.1) with (4.2), then summing g_m in dyadic blocks G_m, gives

\[
\mathcal Q_{\mathbf G}^{\Phi}
\ll D^{k+\epsilon}\prod_{m=1}^{2k}G_m^{(3-m)/2}.
\tag{7.2}
\]

This follows from the elementary block sum

\[
\sum_{G\le Ng<2G}(Ng)^{(1-m)/2}\ll_m G^{(3-m)/2}.
\]

The powers have a sharp structural interpretation for this proof:

| Actual nonprincipal multiplicity m | 1 | 2 | 3 | At least 4 |
|---|---:|---:|---:|---|
| Block cost | G | sqrt(G) | 1 | A negative power of G |
| Summation over scales | Power loss | Power loss | Logarithm | Convergent |

There is no claim that these bounds are lower bounds on the actual signed contribution.

### Theorem 7.1: singleton/double block bound

For L <= Ng_1 < 2L and C <= Ng_2 < 2C, sum over every other nonprincipal multiplicity and every principal mask, retaining the restriction f != 1. Then

\[
\boxed{
\mathcal Q_{L,C}^{\Phi}
\ll D^{k+\epsilon}\min\{H\sqrt L,\ L\sqrt C\}.
}
\tag{7.3}
\]

The first term also bounds the corresponding sharp-row accounting quantity.

**Proof.** For the completion bound, sum (7.2) over m >= 3. At m = 3 there are O_k(log(2D)) possible scales, each costing one. For m >= 4, the geometric sum of G_m^{(3-m)/2} over dyadic G_m >= 1 converges. There are finitely many multiplicities for fixed k. Absorb the one logarithm and the previous finite-pattern losses in D^epsilon. This proves D^{k+epsilon}L sqrt(C).

For the trivial-row bound, use (4.5) instead of (4.2) in (7.1). The g_1 block then costs sqrt(L), the g_2 block costs one, and every m >= 3 has a convergent normalized sum: its block cost is G_m^{1-m/2}, whose exponent is negative. This gives HD^{k+epsilon}sqrt(L). The sharp cutoff has the same O(H) trivial row bound. Both estimates hold for the same positive accounting quantity, proving their minimum. QED.

### Corollary 7.2: a larger complete controlled region

Define the tuple complexity

\[
\mathcal E(\mathbf t)=(Ng_1)\sqrt{Ng_2}.
\tag{7.4}
\]

Then the nonprincipal region E(t) <= H satisfies

\[
\boxed{
\mathcal Q_{\{f\ne1,\ \mathcal E\le H\}}^{\Phi}
\ll HD^{k+\epsilon}.
}
\tag{7.5}
\]

**Proof.** Partition by L,C. Every block meeting the selected region has L sqrt(C) <= H. The second bound in (7.3) is consequently at most HD^{k+epsilon}. Only O_k((log(2D))^2) such blocks can be nonempty. Apply (7.3) to each selected subset of a block; its positive accounting quantity is at most that of the full block. Absorb the logarithms. QED.

This improves (6.3), because g_1 divides f_1f_5 and g_2 divides f_2f_4. Primes of type 1 or 5 which occur three or more times are no longer charged as singleton primes. Repeated cubic primes of multiplicity four or more are no longer charged as double primes.

### Corollary 7.3: all nonprincipal primes repeated at least three times

If g_1 = g_2 = 1 and f != 1, the entire sector has

\[
\mathcal Q^{\Phi}\ll D^{k+\epsilon},
\tag{7.6}
\]

uniformly for H >= 1. This includes more than the pure quadratic residual sector: sextic or cubic residual primes can also be included when their actual multiplicity is sufficiently large.

## 8. Every no-singleton tuple is already diagonal-size

### Theorem 8.1

The number of tuples in which every occurring prime appears at least twice is O(D^{k+epsilon}). Their total absolute contribution with either the sharp cutoff or the smooth row test is O(HD^{k+epsilon}), for every fixed k and H >= 1.

**Proof.** For these tuples, (5.2) gives (Nq)^2 <= (bD)^{2k}, so Nq <= (bD)^k. There are O(D^k) possible ideals q. Assigning each prime of q to one of the finitely many nonempty incidence patterns costs only D^epsilon by (5.1). This bounds the tuple count. Multiply by |c(t)| <= 1 and the O(H) trivial row bound. QED.

Thus all principal algebraic diagonals are included, but the theorem controls a strictly larger class than principal diagonals: it includes all nonprincipal tuples whose total product is powerful. It also controls the entire sector with f_1 = f_5 = 1 at every k, because residues 2,3,4 require at least two occurrences, as do principal-mask primes.

The statement that the principal diagonal count is O(D^{k+epsilon}) was already present in the earlier packet. The additional content here is the explicit enlargement to every no-singleton tuple and its use alongside the completed singleton/double region.

## 9. The exact Möbius sign lives only on odd residual primes

Return to a_n = mu_K(n) nu(n) W(Nn/D). At a prime p in the tuple the product of its left and right Möbius signs is (-1)^{r_p+s_p}. Since

\[
r_p+s_p\equiv r_p-s_p\equiv e_p\pmod2,
\]

and 6 is even,

\[
\boxed{
\prod_i\mu_K(n_i)\prod_i\mu_K(m_i)
=\mu_K(f_1f_3f_5).
}
\tag{9.1}
\]

The ideals f_1,f_3,f_5 are pairwise coprime and squarefree. Principal-mask primes make no contribution to this sign, including the extra residual-zero patterns with e_p = +/-6, +/-12, ... at high orders.

This identity is independent of W and nu. If W is real and nonnegative and nu is principal, all remaining tuple weights are nonnegative after the sign in (9.1) is factored out. The same positivity holds after extracting the residual nu phase if nu has order dividing 6. For a general finite-order nu, the phase nu(p)^{e_p} can depend on the lift of the residual class, so no unconditional coefficient positivity is asserted for that enlarged scope.

Identity (9.1) does not prove cancellation. It shows exactly where the Möbius sign survives after Hermitian collisions: it is carried by odd residual conductor primes. The principal masks and even residual classes cannot supply an additional hidden Möbius sign. In particular, a proof which replaces that surviving coefficient by an arbitrary nonnegative envelope would discard the arithmetic that the requested short-row theorem must use.

## 10. A precise remaining signed moment estimate

Define the controlled tuple set

\[
\mathcal C=
\{\mathbf t:g_1=1\}
\ \cup\
\{\mathbf t:f\ne1,\ \mathcal E(\mathbf t)\le H\}.
\tag{10.1}
\]

Use the union literally; overlapping tuples are counted once. Theorems 7.2 and 8.1 give

\[
\left|\sum_{\mathbf t\in\mathcal C}
c(\mathbf t)S_{\mathbf t}^{\Phi}(H)\right|
\ll HD^{k+\epsilon}.
\tag{10.2}
\]

All remaining tuples have g_1 != 1 and E(t) > H; in particular they are nonprincipal. Let

\[
\mathcal R_{k}^{\Phi}(D,H)=
\sum_{\substack{\mathbf t:g_1\ne1\\\mathcal E(\mathbf t)>H}}
c(\mathbf t)S_{\mathbf t}^{\Phi}(H).
\tag{10.3}
\]

The set is invariant under interchanging the n and m sides, which conjugates the summand. Therefore R_k^Phi is real. The exact decomposition is

\[
\mathcal M_{2k}^{\Phi}(D,H)
=\mathcal R_k^\Phi(D,H)+O(HD^{k+\epsilon}).
\tag{10.4}
\]

Consequently the desired short-row theorem follows from the single additional estimate

\[
\boxed{
\mathcal R_k^\Phi(D,D^{1+\theta})
\ll_{k,\theta,\epsilon}D^{k+1+\theta+\epsilon}
}
\tag{10.5}
\]

for the **actual inverse coefficients**. This is an upper bound on a signed quantity. The full smooth moment's nonnegativity already supplies the matching lower bound for this remainder up to the controlled term. Thus the new region accounting does not hide a possible large negative term.

For a fixed k, (10.5) is equivalent, up to the proved controlled error and arbitrary small-power losses, to the smooth full-moment bound. To infer the original sharp moment only the forward direction (2.2) is needed. Conversely a sharp estimate throughout a fixed constant multiple of the row range also bounds the fixed compact smooth majorant. No isolated sharp sector has been justified by positivity.

Theorems 5.2, 6.1, 7.1 and 8.1 are genuine controlled-sector results. They show that low primitive conductor, all no-singleton tuples, and a larger class with manageable singleton/double complexity are already harmless at every fixed moment. The terms beyond that region still require a new signed cancellation theorem. Neither (10.5), the fourth moment, 17/24, nor the cofinal 2k-th hierarchy has been proved here.

## 11. Finite checks and what they do not establish

For k = 1,2,3,4,6,8, enumerate r,s in {0,...,k}, omit r=s=0, and weight each pair by binom(k,r)binom(k,s). The total is 2^{2k}-1. The computation checked:

- (-1)^{r+s} = (-1)^{(r-s) mod 6};
- every principal nonempty pattern has multiplicity at least two;
- multiplicity one gives residual 1 or 5;
- a nonprincipal multiplicity-two pattern is on one side and gives residual 2 or 4;
- for k >= 3, the nonprincipal minimum multiplicities are exactly (1,2,3,2,1).

The largest run covered the 65,535 nonempty local patterns at k = 8 through their exact binomial multiplicities. This check guards the finite bookkeeping. It is not a numerical test of the arithmetic moment conjecture and is not evidence for an unproved global cancellation estimate.
