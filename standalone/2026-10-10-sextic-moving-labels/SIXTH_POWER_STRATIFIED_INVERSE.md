# Sixth-power stratification removes the raw all-row repetition loss

Status: proposed source-conditional deduction. This note proves a stronger raw two-axis Gauss estimate, assuming the precisely stated mixed-label completed estimate in `MIXED_LABEL_COMPLETION.md`. Its key new step is to choose a separate, exact cube-inverse cutoff on each sixth-power row stratum. The full original Möbius fourth moment, its signed comparison, and the generalized moment hierarchy remain open.

Sources: PR #923 at `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `SHORT_CUBE_RAW_GAIN.md` and `ALL_ROW_COMPLETION_AND_RAW_GAIN.md`; PR #913 at `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `REFINED_ALL_ROW_SIEVE.md`, Sections 2–3; and the literal mixed-label inverse of PR #918, `INTERFACE_COMPARISON.md`. The new mixed-label completion has its own proof, source pins and independent review. In particular, a moving exclusion is not assumed to be a norm contraction of the completed family.

## 1. Objects and hypotheses

Work in the Eisenstein field with the inherited multiplicative generator convention, six units, fixed bad-prime set S, fixed finite ray character xi, and smooth compactly supported factor weights W1,W2 on the positive norm axis. All norm scales and moving labels are bounded by a fixed power of D>=2. Every residue character has its literal zero on nonunits.

Put alpha(a)=a/|a|, lambda(a)=conj(alpha(a))xi(a), and a_xi(a)=lambda(a)gamma_2(a). Let q,f be squarefree ideals outside S, with no disjointness assumption. The normalized raw polynomial is

\[
\mathcal P_{q,f}^{[h]}(A,B;k)
=\frac1{\sqrt{AB}}
\sum_{\substack{an\ {\rm squarefree}\\(an,Sq)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
\mathbf1_{(a,h)=1}W_1(Na/A)W_2(Nn/B).
\tag{1.1}
\]

The mask involving h is only on a. In particular the inner squarefree n may overlap h. Write P without the superscript when h=1. Since the f twist already vanishes when (an,f)>1, q may be replaced exactly by q_*=q/(q,f). Set F=Nf and Q=Nq_*.

The completed family C has the same fixed data, q mask on all physical factors, f twist, and optional outer h mask. Assume the following proved mixed-label estimate, for a fixed beta in (1/2,1]:

\[
\sum_{k\asymp U}|\mathcal C_{q,f}^{[h]}(A,B;k)|^2
\ll_\epsilon D^\epsilon\left[
UA+FQ\frac{U^2A}{B}\min(A,\sqrt B)^{2\beta-1}
+F^{2/3}Q^{1/3}\left(\frac{U^2A^2}{B}\right)^{2/3}
\right].
\tag{1.2}
\]

The sum in (1.2) includes all nonzero element rows. Its constants are uniform for the stated polynomially bounded labels, including their overlaps and the original outer mask. The beta=11/12 version has the epsilon-margin convention from PR #923 and the explicit angular reciprocal input; beta=1 uses elementary counting in that scalar sum. Neither version is asserted for arbitrary replacements of its structured coefficients.

## 2. The exact sixth-power-free large sieve

For arbitrary coefficients z_n supported on squarefree columns outside S, Nn<=L, one has

\[
\boxed{
\sum_{\substack{0<Nk\le U\\k\ \text{sixth-power-free}}}
\left|\sum_n z_n\chi_n(k)\right|^2
\ll_\epsilon (UL)^\epsilon
[U+(UL)^{2/3}+L]\sum_n|z_n|^2.
}
\tag{2.1}
\]

Here sixth-power-free means every prime valuation is at most five; it does not mean squarefree. Units and the finitely many allowed bad-prime valuation patterns are included.

Proof. In the exact valuation decomposition of PR #913, Section 2, the sixth-power label v equals one. Write the five pairwise-coprime squarefree labels as a_j, put P0=prod A_j, M=max A_j, and P=prod A_j^j<=U. Its two block bounds, including all original zeros, are

\[
[P_0+P_0L/M+P_0L^{2/3}/M^{1/3}]\sum|z_n|^2,
\qquad [L+P_0^2]\sum|z_n|^2,
\]

up to the stated small power. The exact monomial inequalities from that proof give P0<=U, P0/M^(1/3)<=U^(2/3), and

\[
\min(P_0L/M,P_0^2)\le(UL)^{2/3}.
\]

Taking the minimum of the two bounds and summing their logarithmically many dyadic blocks proves (2.1). The proof of the ordinary primitive-character alternative already retains the fixed coefficient masks. Thus z_n may include any fixed q,f,h factors of modulus at most a subpower. No estimate for all rows has been restricted by falsely deleting a column mask. QED.

## 3. Exact inverse on each physical row stratum

Every nonzero row has a unique representation

\[
k=u\,v^6 k_0,
\tag{3.1}
\]

with a unit u, arbitrary ideal v, and sixth-power-free ideal k0, in the chosen generator convention. **There is no requirement that (v,k0)=1.** For each prime exponent, divide it by six with remainder in {0,...,5}; this proves uniqueness.

Complete multiplicativity, including zeros, gives

\[
\chi_n(v^6)=\mathbf1_{(n,v)=1}.
\]

Consequently, for fixed v and u, the raw polynomial at k is exactly the polynomial at row u k0 with the additional physical exclusion rad(v) outside S. After the already redundant f primes are removed, denote this exclusion by q_v. Then

\[
Q_v=Nq_v\le Q Nv,
\qquad U_v\asymp H/(Nv)^6.
\tag{3.2}
\]

If U_v<1 but its annulus is nonempty, replace it by max(1,U_v), which is at most a fixed multiple of H/(Nv)^6. Only Nv<=(2H)^(1/6) can contribute. Fixed unit factors belong to the allowed finite ray family. Factors of v supported on S do not enlarge q_v, since the physical columns already avoid S.

For this fixed v, use the exact mixed-label cube inverse. Its summation variable t is squarefree and avoids q_v f S; its coefficient is mu(t)lambda(t)^3 chi_t(uk0)^3/Nt. Its completed term has B_t=D/(Nt)^3 and the additional outer mask (a,t)=1. The proof of the mixed inverse retains the physical q_v exclusions on the squarefree and cube indices. In its long part, group d=tb exactly as in PR #923: d need not be squarefree, (t,b)=1 is not imposed, and the inner squarefree column is allowed to overlap d. Its coefficients are the actual finite divisor sums

\[
c_{R_v}(d)=\sum_{\substack{t\mid d\\Nt>R_v}}\mu(t),
\tag{3.3}
\]

with the stated q_v f exclusions on the physical d. The exterior phases are contractions. If the f-dependent cube phase is identically one on units, its nonunit zeros are still retained by these exclusions.

Choose a fixed support constant K>=1 so that Nt,Nd<=K D^(1/3) whenever the corresponding physical summand is nonempty. For a free parameter 1<=R<=D^(1/3), choose the row-stratum cutoff

\[
\boxed{R_v=\min(KD^{1/3},R Nv).}
\tag{3.4}
\]

When R_v=K D^(1/3), the long inverse is **empty**. It is not bounded by a spurious positive tail. Otherwise R_v=R Nv exactly. Different v may use different cutoffs because (3.1) partitions the original row set, and the inverse is an exact identity separately on each part.

Near this fixed support cap, B_t=D/(Nt)^3 may be below one but is bounded below by a positive support constant whenever the term is nonempty. Such scales are covered by the completed estimate at scale one with rescaled test x -> W2(x/B_t): the possible B_t lie in a fixed compact positive interval, so its required smooth seminorms and the normalization factor remain uniformly bounded. The same convention applies to nonempty raw scales D/(Nd)^3. No estimate is extrapolated to arbitrarily small positive scales.

## 4. Short and long norms; summation before the final optimization

Put eta=9/2-3beta. The completed hypothesis at B_t=D/(Nt)^3 and Minkowski in t give

\[
\|\mathcal S_v\|_2^2\ll D^\epsilon[
U_vD+FQ_v U_v^2D^{\beta-1/2}R_v^\eta
+F^{2/3}Q_v^{1/3}U_v^{4/3}D^{2/3}R_v^2].
\tag{4.1}
\]

This norm is restricted to the sixth-power-free k0 rows, so the all-row completed estimate applies by nonnegativity of the row energy. The bounds retain the moving masks. The norm-level ideal sums are the same finite harmonic/power sums as in PR #923.

For the long part, collect the squarefree product an and apply (2.1). The squared coefficient mass of the normalized polynomial is D^epsilon, uniformly in all fixed masks and twists. The identical d regrouping and ideal tails give, when the long part is nonempty,

\[
\|\mathcal L_v\|_2^2\ll D^\epsilon[
U_v+D^2R_v^{-3}+U_v^{2/3}D^{4/3}R_v^{-2}].
\tag{4.2}
\]

There is no U_v^(1/6) in front of D²: the varying rows in this step are sixth-power-free. The zero mask from v was retained in the fixed column coefficient.

Now sum the squared norms over the disjoint physical strata v. Use Q_v<=Q Nv, U_v<<H/(Nv)^6, and R_v<=R Nv for (4.1). The powers of Nv in its three terms are

\[
-6,\qquad -12+1+\eta=-13/2-3\beta,\qquad
-8+1/3+2=-17/3.
\tag{4.3}
\]

Every exponent is less than -1. For (4.2), sum only uncapped strata, on which R_v=R Nv. Its powers are -6,-3,-6, again all summable. Capped strata have no long contribution. Ideal counting proves convergence of all these sums. Any required small-power losses from labels of polynomial size are allocated a smaller preliminary epsilon and absorbed into the final D^epsilon.

We obtain the principal theorem:

\[
\boxed{
\sum_{k\asymp H}|\mathcal P_{q,f}(D,D;k)|^2
\ll_\epsilon D^\epsilon\bigl[
HD+FQH^2D^{\beta-1/2}R^{9/2-3\beta}
+F^{2/3}Q^{1/3}H^{4/3}D^{2/3}R^2
+H+D^2R^{-3}+H^{2/3}D^{4/3}R^{-2}\bigr].
}
\tag{4.4}
\]

It holds for every 1<=R<=D^(1/3), every nonzero element row, and all polynomially bounded q,f with their original masks and overlaps. Relative to the direct all-row inverse, the H^(1/6) loss in the long-cube tail has been removed. This uses an estimate for the actual mixed-label completion, not the assertion that an arbitrary column exclusion is a contraction of its norm.

## 5. Exact optimization

Let d_beta=5-2beta in [3,4), and suppose

\[
H^2FQ\le D^{d_\beta/2}.
\tag{5.1}
\]

Choose

\[
R_1=D^{4/15}H^{-4/15}F^{-2/15}Q^{-1/15},\qquad
R_2=D^{1/3}(H^2FQ)^{-2/(3d_\beta)},\qquad
R=\min(R_1,R_2).
\tag{5.2}
\]

Both R1,R2 lie in [1,D^(1/3)]. For R2 this follows immediately from (5.1); for R1 note H^4F²Q<=(H²FQ)²<=D^(d_beta)<=D^4. Also (5.1) implies H<=D since F,Q>=1 and d_beta<4.

The third increasing term in (4.4) balances D²R^-3 at R1; the second balances it at R2. Since R is their minimum, both increasing terms are at most

\[
E:=D^2R^{-3}
=\max\{D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
D H^{4/d_\beta}(FQ)^{2/d_\beta}\}.
\]

Furthermore HD<=D^(6/5)H^(4/5)F^(2/5)Q^(1/5) because H<=D. The ratio of the mixed tail to E is H^(2/3)D^(-2/3)R, which is at most its value at R1, namely (H/D)^(2/5)F^(-2/15)Q^(-1/15)<=1. The H term is also harmless. Thus

\[
\boxed{
\sum_{k\asymp H}|\mathcal P_{q,f}(D,D;k)|^2
\ll_\epsilon D^\epsilon
\max\{D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
D H^{4/(5-2\beta)}(FQ)^{2/(5-2\beta)}\}.
}
\tag{5.3}
\]

This is O(D^(2+epsilon)) throughout (5.1). The first term is bounded there since its fifth power is D^6 H^4 F²Q<=D^(6+d_beta)<=D^10. The two terms agree when

\[
H^{8\beta}F^{4\beta}Q^{5+2\beta}=D^{5-2\beta}.
\tag{5.4}
\]

### Angular specialization beta=11/12

The theorem becomes

\[
\boxed{
E_{q,f}(D,H)\ll D^\epsilon
\max\{D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
D H^{24/19}(FQ)^{12/19}\},\quad
H^2FQ\le D^{19/12}.
}
\tag{5.5}
\]

The transition is H^44 F^22 Q^41=D^19. With q=f=1 this is the piecewise bound

\[
\boxed{
E_{1,1}(D,H)\ll_\epsilon
\begin{cases}
D^{6/5+\epsilon}H^{4/5},&1\le H\le D^{19/44},\\
D^{1+\epsilon}H^{24/19},&D^{19/44}\le H\le D^{19/24}.
\end{cases}}
\tag{5.6}
\]

It now holds for all rows, not only the squarefree rows of the old note. In particular,

\[
\boxed{E_{1,1}(D,D^{1/2})\ll D^{31/19+\epsilon}.}
\tag{5.7}
\]

The old all-row exponent was 379/228; the saving over that bound is 7/228. The classical all-row envelope has exponent 25/12; the saving against that envelope is 103/228. The raw diagonal-size range has grown from H<=D^(114/151) to H<=D^(19/24), which is an arithmetic row-height range, not a zero-free boundary.

At H=D^(1/2), the second term in (5.5) always dominates because F,Q>=1. Thus the same example with moving labels is

\[
E_{q,f}(D,D^{1/2})\ll D^{31/19+\epsilon}(FQ)^{12/19},
\qquad FQ\le D^{7/12}.
\tag{5.8}
\]

### Elementary scalar specialization beta=1

Without the angular reciprocal input, (5.3) gives

\[
E_{q,f}(D,H)\ll D^\epsilon
\max\{D^{6/5}H^{4/5}F^{2/5}Q^{1/5},
D H^{4/3}(FQ)^{2/3}\},\quad H^2FQ\le D^{3/2}.
\tag{5.9}
\]

For q=f=1 the transition is H=D^(3/8), and at H=D^(1/2) the exponent is 5/3. This version retains the stated classical theta and sieve foundations but does not use the canonical angular zero-free induction.

## 6. Limits

The raw polynomial here is the exact two-factor Gauss family with moving q,f. It is not the original Möbius polynomial A_u(D). The remaining signed first-Poisson covariance has two independently corrected columns, a coupled row-dependent kernel, strict product-column off-diagonal restriction, and a signed auxiliary sum. These have not been replaced by a positive norm. The initial adverse dual height near D^(3-theta) remains outside the gained diagonal-size range. No full fourth moment, 17/24 zero-free result, new numerical zeta boundary, or all-order hierarchy follows from (5.3) alone.
