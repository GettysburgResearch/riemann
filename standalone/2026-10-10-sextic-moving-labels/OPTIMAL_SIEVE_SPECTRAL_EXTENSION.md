# A 4/7 spectral threshold from the fixed-order large sieve

Status: proposed source-conditional analytic deduction. With an additional, explicitly credited external large-sieve input, the canonical Gauss spectral mean now holds on every strict strip Re(u)>4/7, for every nonzero arithmetic row. The previous 5/8 proof is preserved in `ALL_ROW_SPECTRAL_MEAN.md`. This result improves a spectral mean domain; it does not prove an inverse-Mobius higher moment or a new zero-free boundary.

New external input: Alexandre de Faveri, *Optimal large sieve for fixed order characters*, [arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), posted October 2, 2026, Theorem 1.1. Its statement, definitions of the sixth-power-free sums, residue-symbol zero convention and fixed-family construction were read at the primary HTML source. This theorem is imported, not independently reconstructed here. The associated repository adapter is PR #916, commit `f5c089e33ccce4eae4307d4f6475b9977485cb78`, `standalone/2026-10-10-all-order-collision-removal/continuation-integrated-window/OPTIMAL_SIEVE_AUDIT.md`. Its all-row adapter is rederived below with the required conventions.

Other exact inputs: the imported October 5 Proposition R at OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`; the canonical definitions and holomorphic reconstruction in `ALL_ROW_SPECTRAL_MEAN.md`; and, only for the final reflected-series corollary, PR #922 commit `f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32`, `SECOND_REFLECTION_BOOTSTRAP.md`, `FINITE_RAY_REUNION.md`, `FINITE_CUBE_HOMOGENEITY.md`, `ALL_CUSP_COEFFICIENT_ADAPTER.md`, and `FULL_CUSP_DESCENT.md`. Their inherited theta foundation and exact character-family conditions remain explicit assumptions.

## 1. The external operator and our precise all-row adapter

In the fixed Eisenstein field and a fixed admissible Hecke-character family, the n=6 specialization of de Faveri's Theorem 1.1 is

\[
 \Theta_6(U,L)\ll_\epsilon(UL)^\epsilon
 \left[U+L+U^{5/6}L^{1/3}+U^{1/3}L^{5/6}\right].
\tag{1.1}
\]

Both indices in Theta are sixth-power-free ideals outside a fixed set S; arbitrary complex column coefficients are allowed. Squarefree columns are a subset and can be selected by setting all other coefficients to zero.

The family data in that theorem are fixed. To compare with our primary-generator symbol chi_n(k)=(k/n)_6, one makes only fixed finite partitions. For an ideal a outside S, its Kummer representative in the source family and a generator of a differ, modulo sixth powers, by an S-unit. The S-unit group modulo sixth powers is finite. Partition rows by that class and put its residue symbol into the fixed column coefficients. If reversing the character orientation, the reciprocity discrepancy in source Section 2.5.2 depends only on two classes of its fixed finite ray group; partition those classes before applying the operator bound. On a sixth-power-free row, every occurring good-prime exponent is in {1,...,5}, so the local character is nontrivial and its primitive conductor retains that prime. Thus this comparison preserves exactly the zeros on common row/column primes. The six element units cost another fixed partition.

These operations do not ask for uniformity in a varying construction of the external character family. The fixed set S contains the primes above 6, the ray conductor, and the fixed data needed by the family comparison. The Eisenstein field contains the sixth roots of unity and is a PID, so it meets the stated field and fixed S-class-group hypotheses.

### Lemma 1.1. Every nonzero element row

For coefficients z_n supported on squarefree ideals outside S of norm at most L, and H,L>=1,

\[
\boxed{
 \sum_{0<Nk\le H}\left|\sum_n z_n\chi_n(k)\right|^2
 \ll_\epsilon(HL)^\epsilon
 \left[H+H^{1/6}L+H^{5/6}L^{1/3}+H^{1/3}L^{5/6}\right]
 \sum_n|z_n|^2.
}
\tag{1.2}
\]

Any subset of these rows obeys the same bound. Every fixed column mask or bounded coefficient twist is permitted, provided it is fixed before an individual use of the large sieve.

Proof. Write uniquely k=epsilon z v^6 r, with z supported on S, v and r outside S, r sixth-power-free, and epsilon a unit, using the fixed multiplicative generator convention. No condition (v,r)=1 is imposed. For each fixed epsilon,z,v,

\[
 \chi_n(k)=\chi_n(\epsilon z)\mathbf1_{(n,v)=1}\chi_n(r).
\tag{1.3}
\]

Insert the first two factors into z_n. They are a coefficient contraction and retain the sixth-power-prime zeros even when v meets r. Apply (1.1) to r at height U=H/(Nz(Nv)^6), retaining only nonempty ranges U>=1. For fixed z, the four sums over Nv<=(H/Nz)^(1/6) are bounded respectively by

\[
 \frac H{Nz}\sum_v(Nv)^{-6},\qquad
 L\,\#\{v:Nv\le(H/Nz)^{1/6}\},
\]

\[
 \left(\frac H{Nz}\right)^{5/6}L^{1/3}\sum_v(Nv)^{-5},
 \qquad
 \left(\frac H{Nz}\right)^{1/3}L^{5/6}\sum_v(Nv)^{-2}.
\tag{1.4}
\]

Ideal counting and convergent ideal sums give exactly the four terms in (1.2), with H replaced by H/Nz. Their positive H exponents are 1,1/6,5/6,1/3. Thus summing all S-supported z costs four convergent geometric products over a fixed finite set of primes. Restoring units and the fixed family partitions costs a fixed constant. Preliminary small powers are absorbed in the final epsilon. This proves (1.2).

The H^(1/6)L term has not been deleted. It is the cost of sixth-power copies in a general coefficient family and is present throughout the spectral proof.

## 2. Canonical completed blocks

Keep exactly G_{k,d}, T_{k,d}, c_k(b) and the zero-masked cube Euler product from `ALL_ROW_SPECTRAL_MEAN.md`, equations (1.1)--(1.3). Put F=Nd. The auxiliary d is squarefree outside S and may overlap the row k. The physical completed block is

\[
 T_W(X;k,d)=X^{-1/2}\sum_n^*\sum_{(b,Sd)=1}
 a_\xi(n)\chi_n(k)\chi_n(d)^4c_k(b)\sqrt{Nb}
 W\!\left(\frac{Nn(Nb)^3}{X}\right).
\tag{2.1}
\]

Only n is squarefree; n and b may overlap. The old completed estimate still is

\[
 \sum_{k\in K_H}|T_W(X;k,d)|^2
 \ll(2HFX)^\epsilon\|W\|_{C^J}^2
 \left[H+\frac{H^2F}{X}\right],
\tag{2.2}
\]

for any subset K_H of the nonzero rows in a fixed multiple of the H-ball. This uses the imported all-row Proposition R and no angular reciprocal.

Lemma 1.1 gives the alternative

\[
\boxed{
 \sum_{k\in K_H}|T_W(X;k,d)|^2
 \ll(2HX)^\epsilon\|W\|_\infty^2
 \left[H+H^{1/6}X+H^{5/6}X^{1/3}+H^{1/3}X^{5/6}\right].
}
\tag{2.3}
\]

For completeness, put L_b=X/(Nb)^3. The normalized raw n block at L_b has squared coefficient mass O(1), uniformly in d. At bounded nonempty L_b below one, enlarge to a fixed support-dependent norm cutoff. Apply Lemma 1.1 to this block, then use weighted Cauchy for the exact cube expansion with coefficient c_k(b)/(Nb). The H term incurs a harmonic logarithm. Each term H^r L_b^t, with t in {1,1/3,5/6}, is summable with weight 1/Nb since sum_b(Nb)^(-1-3t) converges. This proves (2.3), after absorbing logarithms. Every row zero and the d-mask in the cube sum survives.

## 3. The improved spectral mean

### Theorem 3.1

For every strict closed strip

\[
 \frac47<a_0\le a=\Re u\le a_1<1
\tag{3.1}
\]

and every epsilon>0, there is a finite M such that

\[
\boxed{
 \sum_{k\in K_H}|G_{k,d}(a+i t)|^2
 \ll H^{1+\epsilon}F^{1-a+\epsilon}(2+|t|)^M.
}
\tag{3.2}
\]

The same statement holds for the exact completion T_{k,d}. The row set may be every nonzero element in the H-ball, including all sixth-power copies and bad-prime valuations. Constants are uniform in d, the row subset, and the fixed finite ray-character family. The estimate adds de Faveri's external theorem to the analytic inputs of the 5/8 baseline; it does not claim to derive that theorem.

Proof. The baseline holomorphic reconstruction is unchanged:

\[
 \mathcal T_{k,d}(u)=\sum_{X=2^j}X^{1/2-u}T_{W_u}(X;k,d).
\tag{3.3}
\]

It converges normally on every compact subset of Re(u)>1/2 by (2.2), and its cube reciprocal is uniformly bounded in the absolute Euler half-plane there. It therefore suffices to bound (3.3) in the row Hilbert space.

Taking the minimum of (2.2) and (2.3), the base term costs H^(1/2) after summation. For each of the three remaining monomials H^r X^t, use

\[
 \min(H^rX^t,H^2F/X).
\tag{3.4}
\]

The minimum of the sums is at most the sum of these individual minima plus H. The crossover and its Mellin-weighted square root are

\[
 X_{r,t}=H^{(2-r)/(1+t)}F^{1/(1+t)},
\tag{3.5}
\]

\[
 H^{1-a(2-r)/(1+t)}F^{1/2-a/(1+t)}.
\tag{3.6}
\]

Indeed the lower dyadic summand is H^(r/2)X^((1+t)/2-a), while the upper summand is HF^(1/2)X^(-a). When the lower exponent is positive, both geometric sums are controlled by (3.6). When it is negative, the lower sum is O(H^(r/2)); when it is zero there is only a logarithm. Uniformly across those interior transition values, a sufficient bound is the sum of (3.6) and H^(r/2), times log(2HF).

The three explicit calculations are:

| (r,t) | Crossover X | Crossover contribution to the row norm | Required row threshold |
|---|---|---|---|
| (1/6,1) | H^(11/12)F^(1/2) | H^(1-11a/12)F^((1-a)/2) | a>=6/11 |
| (5/6,1/3) | H^(7/8)F^(3/4) | H^(1-7a/8)F^(1/2-3a/4) | a>=4/7 |
| (1/3,5/6) | H^(10/11)F^(6/11) | H^(1-10a/11)F^(1/2-6a/11) | a>=11/20 |

Every t is at most one, so

\[
 \frac12-\frac{a}{1+t}\le\frac{1-a}{2}.
\tag{3.7}
\]

Every r is less than one, so H^(r/2)<=H^(1/2). The largest of the three required thresholds is 4/7. Thus on the strict strip (3.1) all terms have the claimed envelope H^(1/2)F^((1-a)/2).

As in the baseline proof, choose preliminary powers small compared with the strip margins. At the polynomial crossovers they cost only arbitrarily small H,F powers; the dyadic tails remain geometrically summable, including the smooth-test vertical polynomial. Absorb the displayed logarithms and square. The uniformly bounded cube reciprocal transfers the estimate to G. This proves (3.2). No endpoint assertion is made.

### What limits this particular block comparison

At F=1 and X=H^(7/8), the monomial H^(5/6)X^(1/3) and the reflected term H^2/X both have size H^(9/8). The other terms in the new generic bound have smaller powers there. Multiplying the square root by X^(1/2-a) gives H^(1-7a/8). Thus this comparison of the displayed envelopes cannot reach a row norm H^(1/2+epsilon) for a fixed a<4/7. This is a limitation of the available estimates, not a lower bound for the actual canonical Gauss series.

## 4. The exact squarefree-row reflected series inherits the new mean domain

This corollary uses the existing complete identity in PR #922 and does not assert that identity for nonsquarefree rows. Use its notation

\[
 u=v-s,\quad a=\Re u,\quad \tau=\Re v,
 \qquad \mathscr R_k(w,s)=H_\Gamma(s)(Nk)^{1-2s}\mathcal Y_k(s,v).
\tag{4.1}
\]

Here H_Gamma is its explicit gamma factor, not the arithmetic row cutoff. The actual complete cusp expansion of Y is a normally convergent sum of the canonical Z functions, with its prescribed cube characters and all ramified/bad labels retained.

### Corollary 4.1

On strict bounded real subregions of

\[
\boxed{
 \frac47<a=\Re(v-s)<1,
 \qquad \tau<\frac{3a-1}{2},
}
\tag{4.2}
\]

the exact squarefree-row family of PR #922 satisfies

\[
 \sum_{k\asymp H}^{*}|\mathcal Y_k(s,v)|^2
 \ll H^{1+\epsilon}
 (2+|\Im s|+|\Im v|)^M.
\tag{4.3}
\]

Proof. The conditioned divisor representation in SECOND_REFLECTION_BOOTSTRAP.md is exact on its initial overlap. Its divisor coefficient h(d) has the uniform magnitude bound (Nd)^(-(1-tau)+epsilon) in the stated chamber, and the scalar coefficient multiplying each G_{k,d}(u) is a row contraction. Theorem 3.1, restricted to the source's squarefree row set, bounds the norm of the d-term by

\[
 H^{1/2+\epsilon}(Nd)^{-a-(1-\tau)+(1-a)/2+\epsilon}
\tag{4.4}
\]

times a fixed vertical polynomial. The ideal sum converges precisely under the sufficient strict inequality tau<(3a-1)/2. Its cube Euler product is still in an absolute half-plane. This proves the corresponding bound for each canonical Z. The actual finite-ray/cusp sum and every bad/ramified label are then summed by the same absolutely bounded coefficient mass in FULL_CUSP_DESCENT.md, equation (2.6). Cross terms are controlled by Minkowski, not discarded. This proves (4.3).

The holomorphic domain of Y from PR #922 is unchanged; the part of that domain with this square-root row mean has enlarged from a>5/8 to a>4/7.

## 5. Physical meaning and explicit non-improvement boundary

The balanced Mellin scalar in PR #922 is D^(v-2s), of real exponent 2a-tau. Under (4.2), its infimum becomes

\[
 \inf(2a-\tau)=\frac{11}{14},
\tag{5.1}
\]

approached from above at a=4/7, tau=5/14, Re(s)=-3/14. These are limiting values only. The former infimum was 13/16, so the scalar difference is 3/112. This is not a zeta zero-free constant.

Even if the required physical contour composition is supplied, the candidate squarefree-row completion energy would be H D^(11/7+epsilon). It does not improve the older physical envelope. For H<=D^(4/7), the factorwise bound D(H+H^2) is at most twice that candidate. For H>=D^(3/7), the classical squarefree-row bound H+D^2+(HD^2)^(2/3) is at most a fixed multiple of that candidate. These ranges cover every H>=1, since 3/7<4/7. The stronger raw estimates proved elsewhere in this packet cannot make this comparison more favorable.

The new results are the all-row spectral estimate at a>4/7 and its exact squarefree-row cusp-mean corollary. The original Mobius moment, the signed moving-auxiliary comparison, the adverse long initial dual height and the generalized diagonal hierarchy remain separate open requirements.
