# Signed singleton cancellation: two inverse factors, odd incidence ideals, and Hermitian gcd tails

Status: proposed component theorems derived from the source-pinned native second moment. No full fourth moment, generalized diagonal moment hierarchy, or new zero-free boundary is proved. The primary corollaries use only the native second moment and elementary pointwise counting. Stronger numerical corollaries explicitly require the stated uniform pointwise hypothesis.

Scope: every fixed integer k over the Eisenstein field; literal sextic symbols on every element row; exact squarefree Möbius coefficients with a fixed finite-order Hecke datum; bounded compactly supported row weights and, by an explicit annular adapter, fixed Schwartz row profiles. This includes sharp rows, the compact row majorant in PR #914's `CONDUCTOR_SECTORS.md`, and the Fourier-compact Schwartz majorant in its `A2_COMPLETION.md`. These are bounds for signed tuple sectors or signed smooth incidence blocks. They are not bounds for the sum of the absolute values of individual completed tuple contributions.

Exact sources: PR #914 at `0cc0428fedbbfc340044c7451b3d392c1da9a103`, especially `CONDUCTOR_SECTORS.md`; PR #913 at `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `FOURTH_MOMENT_ATTACK.md`, Proposition 2.1 and Section 8, and its inherited pinned October 5 source `paper2.tex`, `prop:poisson-reduction`; adjacent PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`, `ANISOTROPIC_SINGLETON_CORES.md`, for the forward correction with one long axis. The exact mixed-sign correction is proved again below, including its critical two-axis boundary. No source is silently granted a new analytic scope.

What was done: derived a two-factor row-L1 estimate with exact moving exclusions, extended the choice of inverse factors from singleton variables to odd repeated-prime incidence ideals, retained the coupled column weights by Mellin separation with finite test seminorms, and independently derived the global Hermitian gcd identity by finite Möbius inversion. No computation of zeros, new large sieve, or new automorphic continuation theorem was used. The root agent owns independent finite bookkeeping checks and publication.

Smallest remaining gap: cancellation in long incidence blocks with insufficient repeated-prime weight and at least three long eligible inverse factors. In particular the all-unit repeated core at the balanced fourth moment remains open.

## 1. Inputs, rows, and exact conventions

Fix k >= 2, theta > 0, D >= 2 and H = D^(1+theta). Put K = Q(sqrt(-3)). Let nu be a fixed finite-order Hecke character and let S contain the fixed bad primes and the primes of its conductor. Enlarging S by the latter does not change a sum using the usual imprimitive zero convention. Ideals are represented with the source's primary-generator convention. Every displayed squarefree ideal is prime to S, so nu has absolute value one on it.

For squarefree n let chi_n(u) = (u/n)_6, with its literal zero on nonunits. Negative character exponents below always mean products of conjugate character values, retaining those zeros. They never mean taking an inverse of zero.

Let W be a fixed smooth test supported in [a,b] contained in (0,infinity), and put

\[
A_u(X;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/X).
\tag{1.1}
\]

For a moving ideal q, superscript (q) adds the column restriction (n,q)=1. Initially let varpi_D(u) be any row weight of absolute value at most a fixed constant, supported on Nu <= C H for fixed C. It may be the sharp indicator of 0 < Nu <= H, or a fixed compactly supported smooth profile Phi(Nu/H). Lemma 1.1 below extends every theorem to an arbitrary fixed Schwartz profile, including the source's Fourier-compact profile; Fourier-compact support is not confused with compact row support. The zero row may be retained; its only nonzero inverse column is the unit ideal and it is covered by the bounded-scale estimates below.

### Native second-moment input

For every fixed finite-order datum lambda in the finite set needed below, every fixed compact support interval, and every epsilon > 0, use

\[
\sum_{0<Nu\le CH}|A^{(q)}_{\lambda,u}(X;V)|^2
\ll D^\epsilon H X\,\|V\|_{C^J}^2,
\quad c\le X\le C_1D,\quad Nq\le D^{C_2}.
\tag{1.2}
\]

Here c,C,C1,C2 are fixed; J and the implied constant are independent of the moving X,q,D. This is a uniform statement at every reference parameter D>=2, not only one preselected row height. Conjugated row characters have the same bound by conjugation. Empty scales below the fixed support cutoff vanish.

The smaller-scale and moving-exclusion parts are precisely the adapter in PR #913, Proposition 2.1, conditional on its imported canonical theorem and Poisson reduction. The finite test-seminorm dependence is explicit in the pinned `prop:poisson-reduction` proof: it proves the original normalized bound with a fixed C^(J') norm of the original test. The same smaller-scale argument preserves that dependence. Fixed upper-scale constants C,C1 are harmless by increasing the polynomial reference parameter by a fixed factor and using positivity of the row second moment. This note uses no estimate for arbitrary arithmetic column coefficients.

### Optional pointwise input

Fix beta in (1/2,1]. For each odd integer e with |e| <= k, use

\[
\left|\sum_{(n,qS)=1}\mu_K(n)\nu(n)^e
   \chi_n(u)^e V(Nn/X)\right|
\ll D^\epsilon X^\beta\|V\|_{C^{J_\beta}},
\quad Nu\le CH,
\tag{1.3}
\]

with the exact zero convention, polynomially bounded q, and the same smaller-scale range. As with (1.2), this hypothesis is quantified at every reference parameter D. At beta = 1 it is elementary ideal counting and adds no analytic hypothesis. At beta < 1 it is a separate uniform input. A fixed-character estimate with uncontrolled moving-conductor constants, or a pointwise assertion at only one prescribed row height, does not suffice.

PR #913, Section 8, derives this input from a common zero-free half-plane for all finite-order Hecke L-functions, through its uniform reciprocal bound. For a fixed row, raising chi_n(u) to any fixed e still gives a finite-order character in n with polynomial conductor; literal imprimitive zeros remain in its Euler factors. The exclusion q is removed exactly through

\[
A^{(q)}_{\lambda,u}(X)
=\sum_{d:\ p\mid d\Rightarrow p\mid q}
\lambda(d)\chi_d(u)^e A_{\lambda,u}(X/Nd).
\tag{1.4}
\]

The absolute geometric factor at exponent beta is at most
\(\prod_{p\mid q}(1-(Np)^{-\beta})^{-1}\ll_\eta(Nq)^\eta\).
Thus the stated uniformity survives exclusion removal. Formula (1.4) is finite on the test support and also holds when a row character vanishes at a prime. At the zero row, only the unit term survives, and its nonempty scales lie in a fixed compact interval.

### Lemma 1.1: the fixed Schwartz-row adapter

Every row-linear estimate below remains valid for varpi_D(u)=Phi(Nu/H), with Phi any fixed Schwartz profile, with constants depending on its fixed decay seminorms. The same is true for a weight bounded in absolute value by such a profile. More explicitly, for any fixed number r of inverse factors, with two eligible factors j,l obeying (1.2) and all others obeying (1.3), the underlying estimate is

\[
\sum_u|\Phi(Nu/H)|\prod_{i=1}^r|A_{i,u}(Y_i;V_i)|
\ll D^\epsilon H(Y_jY_l)^{1/2}\prod_{i\ne j,l}Y_i^\beta
\tag{1.6}
\]

with fixed finite test seminorms and all original Y_i<=C1D. This is the only row-product estimate subsequently used. In particular the source's compact Fourier support is permitted without truncating its original rows.

**Proof.** The zero row belongs to the initial bounded annulus. For j>=1, divide the nonzero rows into 2^(j-1)H < Nu <= 2^jH, with the initial annulus Nu<=H. On annulus j,

\[
|\Phi(Nu/H)|\ll_{\Phi,A}2^{-Aj}.
\]

Put h=1+theta and use the reference parameter

\[
D_j=D\,2^{j/h},\qquad H_j=D_j^h=2^jH.
\tag{1.5}
\]

Every original column scale X<=C1D is still a permitted smaller scale at reference D_j. Every moving ideal of norm at most D^C2 is also polynomially bounded in D_j, with the same exponent. Apply the uniform native and optional pointwise inputs at D_j. Their constants and finite test seminorm orders do not depend on j. A preliminary analytic loss D_j^epsilon0 becomes D^epsilon0 2^(j epsilon0/h).

Row Cauchy on j,l and the pointwise bounds on the other r-2 factors give (1.6) on annulus j with H replaced by H_j and a preliminary loss at most D_j^((r-1)epsilon0). Thus its annular bound is the fixed original column-scale expression times

\[
H D^\delta 2^{j(1+\delta/h)},\qquad \delta=(r-1)\epsilon_0.
\]

Multiplying by the Schwartz majorant and choosing a fixed A>1+delta/h yields a convergent geometric series, uniformly in D, proving (1.6). Subsequent finite arithmetic corrections, column norm factorizations, and incidence-block counts still use the original D: their indices have not changed. They therefore retain exactly their stated original-D bounds after inserting (1.6). Redistributing the preliminary losses gives the requested epsilon. This proof also shows precisely what optional pointwise uniformity is needed: (1.3) must hold throughout the smaller-scale range at every reference D_j. Its common zero-free derivation has that quantification. No bound with a constant depending on an individual row is used. All underlying tuple sums are finite, and their unrestricted Schwartz row sums are absolutely convergent, so the annular regrouping is legitimate. QED.

## 2. The mixed-sign correction at the critical two-axis boundary

Let r be fixed. For each axis i let eta_i,u(n) be a completely multiplicative finite-order row character, with its literal zero extension, and form the inverse coefficient mu(n) eta_i,u(n). The eta_i may be different powers of nu and of the sextic row symbol. Define

\[
B_{C,u}(\mathbf X;\mathbf V)
=\sum_{\substack{n_1,\ldots,n_r\ {\rm pairwise\ coprime}\ (n_1\cdots n_r,CS)=1}}
\prod_{i=1}^r\mu(n_i)\eta_{i,u}(n_i)V_i(Nn_i/X_i).
\tag{2.1}
\]

The variables are squarefree. At an allowed prime write z_i = eta_i,u(p)(Np)^(-s_i). The desired local factor is 1-sum_i z_i and the independent inverse factors have product prod_i(1-z_i). The row-independent forward correction E_C has local factors

\[
E_{C,p}(\mathbf z)=
\begin{cases}
(1-\sum_i z_i)/\prod_i(1-z_i),&p\nmid C S,\\
1/\prod_i(1-z_i),&p\mid C,\\
1,&p\in S.
\end{cases}
\tag{2.2}
\]

Write its coefficients e_C(d1,...,dr). Outside C, a nonconstant monomial of support I has coefficient 1-|I|, so the one-axis terms vanish. At a prime of C every coefficient is one. Coefficient multiplication gives the exact finite smooth identity

\[
B_{C,u}(\mathbf X;\mathbf V)
=\sum_{\mathbf d}e_C(\mathbf d)
\prod_i\eta_{i,u}(d_i)
\prod_i A_{i,u}(X_i/Nd_i;V_i).
\tag{2.3}
\]

The character multiplier prod_i eta_i,u(d_i) has absolute value at most one; the correction coefficient e_C(d) need not. If u is a nonunit at p, every nonconstant local monomial involving p vanishes on both sides. In particular conjugate factors do not turn a product of two zeros into a principal value one.

For positive alpha_i with alpha_i+alpha_j>1 for distinct i,j, the absolute weighted coefficient sum converges outside C. Indeed, with t_i=(Np)^(-alpha_i), its exact local factor is

\[
1+\sum_{|I|\ge2}(|I|-1)\prod_{i\in I}\frac{t_i}{1-t_i}.
\tag{2.4}
\]

Every nonconstant term uses two axes, so this is 1+O((Np)^(-1-delta)) for some fixed delta>0. At the mask primes the factor is prod_i(1-t_i)^(-1), whose finite product is O_eta((NC)^eta). Thus

\[
\sum_{\mathbf d}|e_C(\mathbf d)|\prod_i(Nd_i)^{-\alpha_i}
\ll_{\boldsymbol\alpha,\eta}(NC)^\eta.
\tag{2.5}
\]

Select two axes j,l and take alpha_j=alpha_l=1/2, with all other alpha_i=beta>1/2. Only their mutual pair is critical. On the finite support Nd_j,Nd_l << D, increase those two weights to 1/2+delta. Formula (2.5) then gives

\[
\sum_{\rm contributing\ \mathbf d}|e_C(\mathbf d)|
(Nd_jNd_l)^{-1/2}\prod_{i\ne j,l}(Nd_i)^{-\beta}
\ll D^{2\delta}(NC)^\eta\ll D^\epsilon.
\tag{2.6}
\]

Choose delta and eta in terms of epsilon and the fixed polynomial bound for C. This proves a subpower bound at the critical pair without a hidden convergence assertion. The forward denominator has no singularity at a fixed small prime; an inverse factor 1/(1-sum_i z_i) is not used here.

### Proposition 2.1: two inverse factors in row L1

Assume axes j,l satisfy (1.2), and the others satisfy (1.3). Then

\[
\boxed{
\sum_u |\varpi_D(u)|\,|B_{C,u}(\mathbf X;\mathbf V)|
\ll D^\epsilon H (X_jX_l)^{1/2}
\prod_{i\ne j,l}X_i^\beta.
}
\tag{2.7}
\]

The bound is uniform for moving C of polynomial norm and every nonempty smaller rectangle. Its test dependence is through a fixed product of finite seminorms.

**Proof.** First use a compactly supported row weight. For the independent product at any shifted scales Y_i, row Cauchy on j,l and the pointwise bounds on the others give

\[
\sum_u |\varpi_D(u)|\prod_i|A_{i,u}(Y_i)|
\ll D^{\epsilon_0}H(Y_jY_l)^{1/2}
\prod_{i\ne j,l}Y_i^\beta.
\]

Insert this in the L1 triangle inequality for (2.3), and use (2.6). Scales below the support cutoff contribute nothing; every remaining scale below one lies in a fixed compact interval where the same estimates hold. Redistributing the preliminary epsilon losses proves (2.7). Lemma 1.1 gives the fixed Schwartz case by applying this compact-row argument on each annulus. No row-dependent arithmetic coefficient was inserted into the native second moment. QED.

## 3. Two Hermitian singleton axes and an exact repeated-core criterion

Index the 2k original tuple entries by i=1,...,2k, with signs sigma_i=1 for the first k and -1 for the last k. Let W_i=W on the first side and W_i=conjugate(W) on the second. For every nonempty incidence set I, let q_I contain exactly the primes appearing in the tuple entries indexed by I. These ideals are squarefree and pairwise coprime.

Freeze the repeated ideals c_I=q_I with |I|>=2. Put

\[
M_i=\prod_{I\ni i,\ |I|\ge2}c_I,\quad
X_i=D/NM_i,\quad C=\prod_{|I|\ge2}c_I,
\quad
\Gamma(\mathbf c)=\prod_{|I|\ge3}(Nc_I)^{|I|-2}.
\tag{3.1}
\]

The remaining ideals a_i=q_{\{i\}} are precisely the global singleton variables. The tuple contribution is a row multiplier Z_c(u) of absolute value at most one times the disjoint inverse polynomial (2.1) in these a_i, with eta_i,u=nu^(sigma_i) chi^(sigma_i) and test W_i. Z_c retains every principal coprimality mask from the repeated primes.

Choose j,l at the two largest X_i, and write Q_per=prod_(i notin {j,l}) X_i. Applying (2.7) and using prod_i X_i=D^(2k) prod_I(Nc_I)^(-|I|) gives a fixed-core bound

\[
\ll D^\epsilon HD^k
\prod_{|I|\ge2}(Nc_I)^{-|I|/2}
Q_{\rm per}^{\beta-1/2}.
\tag{3.2}
\]

### Theorem 3.1: the repeated-core budget

For any set of complete repeated-core configurations satisfying

\[
\boxed{Q_{\rm per}^{\,2\beta-1}\le T\,\Gamma(\mathbf c),}
\tag{3.3}
\]

the absolute value of their complete signed tuple contribution is

\[
\boxed{\ll D^\epsilon H D^k\sqrt T.}
\tag{3.4}
\]

This holds for sharp rows as well as the fixed smooth majorant. The selection is of entire singleton sums at each repeated core; arbitrary further deletions inside those singleton sums are not asserted.

**Proof.** Condition (3.3) bounds the last factor in (3.2) by sqrt(T) prod_I(Nc_I)^((|I|-2)/2). Each core is therefore charged at most

\[
D^\epsilon HD^k\sqrt T\prod_{|I|\ge2}(Nc_I)^{-1}.
\]

Each c_I has norm O(D) when its original tuple support is nonempty. Dropping the pairwise coprimality only in this nonnegative accounting sum gives a fixed product of harmonic ideal sums, O((log(2D))^(2^(2k)-2k-1)). It is absorbed into D^epsilon. QED.

In particular T=1 supplies a controlled signed region. If T=D^(-delta), it gives a genuine power saving D^(-delta/2) relative to the requested moment size.

### Corollary 3.2: singleton primes confined to two axes

The entire signed sector in which all global singleton primes occur in at most two tuple entries contributes O(HD^(k+epsilon)).

To justify this as an exact tuple restriction, partition into the finitely many possible active axis sets. Freeze a_i=1 on every inactive axis; the corresponding W_i(1/X_i) forces X_i into a fixed compact interval. With two active variables, apply the two-axis form of (2.7). With one active variable, row Cauchy against the constant sequence gives O(D^epsilon H sqrt(X_i)); with no active variables the row bound is O(H). Requiring an active variable to be nonunit is handled by subtracting its unit term, a finite additional expansion with the same bound. In every case the normalized core weight is prod_I(Nc_I)^(-|I|/2), up to fixed support constants. Pair incidences are harmonic and higher incidences converge, proving the claim. This proof does not infer a bound for a selected subset from a bound for its larger signed sum.

For example, at the fourth moment the sector m1=m2=q with q coprime to n1n2, and n1,n2 coprime, has its singleton primes only in n1,n2. With all three column norms of size D, its old singleton/double complexity is of size D^(5/2), far above H for small theta. The present estimate controls this signed sector at HD^(2+epsilon).

## 4. The repeated odd primes themselves can be inverse factors

The preceding theorem only uses singleton axes as its two inverse factors. There is more signed structure. For any incidence I put

\[
m_I=|I|,\qquad e_I=\sum_{i\in I}\sigma_i.
\]

At q_I its exact coefficient is mu(q_I)^(m_I) nu(q_I)^(e_I), and its literal row factor is chi_(q_I)(u)^(r_I) conjugate(chi_(q_I)(u))^(s_I).

If m_I is odd, the Möbius coefficient is mu(q_I). If additionally e_I is congruent to 1 or 5 modulo 6, the row symbol is a native sextic character or its conjugate, including its zero. Thus **these odd repeated-prime ideals also qualify for (1.2)**, with the fixed datum nu^(e_I). Odd patterns with e_I congruent to 3 have a quadratic row character: they may use (1.3), but they are not granted the native sextic second moment.

### Smooth incidence blocks

Choose a fixed nonnegative smooth dyadic partition psi supported in (1/2,2), with sum_(j>=0) psi(x/2^j)=1 for x>=1. In the exact incidence expansion insert prod_I psi(Nq_I/Q_I), where Q_I are dyadic and at least one. Write S_Q for the resulting complete signed block. Every original tuple is recovered by summing these blocks. The partition and all its tests are fixed independently of D.

Only O((log D)^(2^(2k)-1)) blocks can meet the original compact column support. For every such block,

\[
\prod_I Q_I^{m_I}\asymp D^{2k},
\tag{4.1}
\]

with fixed support and k dependent constants. Let

\[
\mathcal O=\{I:m_I\text{ odd}\},\qquad
\mathcal E=\{I:e_I\equiv1\text{ or }5\pmod6\},
\]

\[
L_1=\prod_{m_I=1}Q_I,\qquad
\Gamma=\prod_{m_I\ge3}Q_I^{m_I-2}.
\tag{4.2}
\]

All singleton patterns belong to E, so at least two eligible labels exist. Choose J,L in E with the two largest Q_I, and put

\[
T_2=Q_JQ_L,\qquad
U=\prod_{I\in\mathcal O\setminus\{J,L\}}Q_I.
\tag{4.3}
\]

### Theorem 4.1: two eligible odd incidence ideals

For every admissible smooth block,

\[
\boxed{
|S_{\mathbf Q}|\ll D^\epsilon H
\left(\prod_{m_I\ {\rm even}}Q_I\right)
T_2^{1/2}U^\beta
\ll D^\epsilon HD^k
\sqrt{\frac{L_1}{\Gamma T_2}}\,U^{\beta-1}.
}
\tag{4.4}
\]

Consequently, the sum of the absolute values of all complete signed blocks satisfying

\[
\boxed{L_1\le Z\,\Gamma T_2 U^{2(1-\beta)}}
\tag{4.5}
\]

is O(HD^(k+epsilon) sqrt(Z)). The primary case beta=1 needs only the native second moment and controls L1 <= Gamma T2. This theorem preserves cancellation within a block; it does not take absolute values term by term in its tuple expansion.

**Proof, including the coupled tests.** Freeze every even-incidence ideal and retain their product as the exact moving exclusion C for the odd ideals. Their row multiplier has absolute value at most one, with every principal zero mask intact. All odd variables have a Möbius factor and are pairwise coprime outside C.

Perform Mellin inversion on each original W_i on real part zero before applying any row inequality. The 2k Mellin transforms are rapidly decreasing. A variable q_I receives the factor (Nq_I/Q_I)^(-i tau_I), with tau_I=sum_(i in I)t_i, while the remaining norm factors have modulus one. Its one-variable test is exactly

\[
V_{I,\mathbf t}(x)=\psi(x)x^{-i\tau_I}.
\tag{4.6}
\]

These tests are independent of the row and the frozen arithmetic ideals. Every fixed C^J seminorm is bounded by a fixed polynomial in 1+sum_i|t_i|. Thus the finite-seminorm form of (1.2), (1.3), and Proposition 2.1 applies with a uniform polynomial frequency cost, integrable against the rapid Mellin decay. No moving infinity type is being inserted into an automorphic theorem: the imaginary norm powers are part of an explicitly controlled smooth test.

Apply (2.7) to the odd variables, choosing J,L for the two second moments and applying the beta pointwise bounds to all other odd variables. This gives H D^epsilon T2^(1/2) U^beta for each frozen even tuple. There are O(prod_(even I) Q_I) such tuples; enlarge their count only after the preceding positive bound. This proves the first inequality in (4.4).

By (4.1),

\[
\prod_IQ_I\asymp D^k\sqrt{L_1/\Gamma}.
\]

Dividing this product by sqrt(T2) and multiplying by U^(beta-1) gives the second inequality. The block count is a fixed logarithmic power, so (4.5) follows after redistributing epsilon. QED.

The theorem uses smooth dyadic incidence blocks. A hard cutoff inside one of the two selected repeated-prime variables is not silently treated as a fixed smooth test. The exact hard global-gcd sector in the next section has a separate finite-inversion proof.

## 5. An exact global Hermitian gcd tail at every fixed order

Let G be the common gcd of all 2k original tuple entries. This is the incidence ideal q_{\{1,...,2k\}}. Let T_R denote their exact signed contribution with NG >= R, where R >= 1. This is a restriction across both Hermitian sides, not the norm of the part of A_u(D)^k having a large within-side common divisor.

### Theorem 5.1

Put rho=1+2(k-1)beta. Then

\[
\boxed{|T_R|\ll H D^{\rho+\epsilon}R^{1-\rho}.}
\tag{5.1}
\]

In particular, the exact global-Hermitian-gcd sector has the desired size HD^(k+epsilon) whenever

\[
\boxed{R\ge D^{(2\beta-1)/(2\beta)}.}
\tag{5.2}
\]

The threshold is independent of the fixed order k. At beta=1 it is R >= D^(1/2). If the additional uniform pointwise premise holds at beta=7/8, it is R >= D^(3/7). With the exact conditional beta=139999/160000 quoted in PR #913, Section 8, it is R >= D^(59999/139999). These optional numerical values inherit that source's zero-free premise; they are not new zero-free conclusions.

**Independent exact proof.** For squarefree q define

\[
w_R(q)=\sum_{d\mid q,\ Nd\ge R}\mu_K(q/d).
\tag{5.3}
\]

Finite Möbius inversion gives

\[
\mathbf1_{Nc\ge R}=\sum_{q\mid c}w_R(q),\quad
w_R(q)=0\ (Nq<R),\quad |w_R(q)|\le\tau_K(q).
\tag{5.4}
\]

Insert this identity with c=G and extract q from every tuple entry. Squarefreeness requires every residual entry to be coprime to q. The common factors satisfy mu(q)^(2k)=1, |nu(q)|^(2k)=1, and the literal row product is 1_((u,q)=1). Therefore

\[
\boxed{
T_R=\sum_q^*w_R(q)
\sum_u\varpi_D(u)\mathbf1_{(u,q)=1}
\left|A_u^{(q)}(D/Nq;W)\right|^{2k}.
}
\tag{5.5}
\]

This is a finite equality with no missing norm factor. The mask can now be deleted in the positive upper bound for the absolute value of its row sum. The column exclusion q must remain and is handled by the excluded native input; deleting columns is not being treated as a norm contraction.

Combining (1.2) and (1.3) gives the uniform excluded weak moment

\[
\sum_{Nu\le CH}|A_u^{(q)}(X;W)|^{2k}
\ll D^\epsilon H X^\rho.
\tag{5.6}
\]

For a fixed Schwartz row profile, Lemma 1.1 gives the same estimate with the row sum replaced by sum_u |Phi(Nu/H)| |A_u^(q)(X;W)|^(2k). The column X and exclusion q remain fixed while the reference parameter changes across row annuli.

Only q with Nq <= bD occur, so the scales X=D/Nq lie in [1/b,D]; the bounded subunit interval is legitimate. Since rho>1, ideal counting and the divisor bound yield

\[
\sum_{Nq\ge R}\frac{\tau_K(q)}{(Nq)^\rho}
\ll_{\rho,\delta}R^{1-\rho+\delta}.
\]

For a nonempty tail R <= bD, absorb R^delta into D^epsilon. Equations (5.4)-(5.6) prove (5.1). Finally (rho-k)/(rho-1)=(2beta-1)/(2beta), proving (5.2). QED.

The same bound follows from Theorem 3.1: NG>=R forces X_i<=D/R and Gamma>=R^(2k-2), so its budget parameter is at most D^((2k-2)(2beta-1)) R^(-2beta(2k-2)). The independent proof above checks the sharp cutoff and the coefficient normalization directly.

## 6. Explicit new fourth-moment ranges

### 6.1 A common prime core in all four entries

Take a common squarefree core q of norm R in every entry, with the four residual singleton factors of size D/R. The old singleton complexity is of size (D/R)^4. For theta<1, cores around R=D^(1/2) therefore lie beyond its previously controlled complexity threshold H=D^(1+theta).

The exact common-gcd theorem gives

\[
|T_R|\ll H D^{1+2\beta+\epsilon}R^{-2\beta}.
\]

At beta=1 the exponent improves from the naive HD^3 scale to HD^3/R^2, attaining HD^2 at R=D^(1/2), with a power saving beyond that threshold. This is a genuine new Hermitian sector. It is narrower than the older within-half common-divisor polynomial norm tail, so the new exponent is not a replacement for that distinct statement.

### 6.2 A triple core is itself an inverse factor

At k=2 take a repeated ideal q in entries {1,2,3}, with the remaining repeated ideals equal to one. Its incidence has m=3 and e=1, so its coefficient is mu(q)nu(q)chi_q(u): it qualifies for the native second moment. On a smooth block Nq about R, the other four odd variables have sizes

\[
(D/R,D/R,D/R,D).
\]

For R>=D^(1/2), the two largest eligible variables are the singleton D and the triple core R. Thus T2 is of size DR, U is of size (D/R)^3, L1 is of size D^4/R^3, and Gamma is of size R. Theorem 4.1 gives

\[
\boxed{|S_R|\ll H D^{3\beta+1/2+\epsilon}R^{1/2-3\beta}.}
\tag{6.1}
\]

The target HD^2 follows at

\[
R\ge D^{(6\beta-3)/(6\beta-1)},
\quad\text{provided this is in the stated ordering range }R\ge D^{1/2}.
\tag{6.2}
\]

At beta=1 this is R>=D^(3/5), improving the singleton-only repeated-core criterion R>=D^(2/3). The former PV complexity test requires R approximately D^(1-theta/3), since its singleton product is D^4/R^3. If the optional beta=7/8 premise is supplied, (6.2) is R>=D^(9/17), which exceeds D^(1/2) and therefore satisfies the ordering condition.

For completeness, below the ordering transition R=D^(1/2), the two largest eligible norms are D and D/R. In that range Theorem 4.1 instead gives

\[
|S_R|\ll H D^{1+2\beta+\epsilon}R^{-\beta-1/2}.
\]

The optimal threshold from these two orderings is therefore

\[
R\ge D^{r(\beta)},\qquad
r(\beta)=
\begin{cases}
(4\beta-2)/(2\beta+1),&1/2<\beta\le5/6,\\
(6\beta-3)/(6\beta-1),&5/6\le\beta\le1.
\end{cases}
\tag{6.3}
\]

Both expressions equal 1/2 at beta=5/6. The source-conditional beta=139999/160000 is in the upper branch and gives the exact exponent 179997/339997.

This saving uses the sign of an odd repeated prime and its residual sextic character. Replacing that coefficient by its absolute value would remove the second inverse factor used in the proof.

## 7. Remaining boundaries and precise unsuccessful extensions

1. **The balanced core remains open.** With every repeated ideal equal to one, the 2k singleton lengths are all D. Theorem 3.1 or 4.1 gives only H D^(1+2(k-1)beta+epsilon), the previously available second-moment/pointwise interpolation exponent. At the fourth moment with beta=1 it is HD^3, not HD^2. The new theorems control additional signed regions; they do not change this full-core estimate.

2. **Hölder cannot improve the two-axis exponent using only these one-variable inputs.** For norm scales at least one, interpolating the row L2 bound and the pointwise beta bound assigns an exponent beta-(beta-1/2)t_i to axis i, with 0<=t_i<=1 and sum_i t_i=2 for a row-L1 product; noneligible axes have t_i=0. Minimizing the resulting scale exponent assigns the two units of t to the two largest eligible scales. Bounded subunit scales only change fixed constants. This is precisely the choice in Theorems 3.1 and 4.1. A different Hölder allocation using only these inputs cannot manufacture the missing balanced-core power saving. This is a limitation of that specified interpolation method, not an impossibility theorem for arithmetic cancellation.

3. **Quadratic odd patterns are not silently sextic second moments.** If e_I is congruent to 3, the coefficient still has a Möbius sign, and the optional pointwise Hecke premise covers it. But the row family is quadratic and has different power-row multiplicities. The present proof never selects it for (1.2).

4. **Grouping several eligible ideals into one inverse factor does not yet close the gap.** Their product has the desired Möbius sign only because the variables are disjoint, but regrouping introduces a constrained allocation coefficient with the coupled original factor weights. The native second moment is for a fixed smooth inverse test, not that arbitrary balanced divisor coefficient. Declaring the product to be one native inverse polynomial would assume precisely the missing multilinear estimate.

5. **The global-gcd sector is signed.** Neither its indicator kernel nor its weights w_R are being asserted positive. Taking absolute values occurs only after the exact total-energy representation (5.5). The new range cannot be used as a bound for the entire norm of a one-sided polynomial tail, or for arbitrary subregions cut out of a signed smooth incidence block.

All controlled pieces can coexist with the old absolute low-complexity sector: subtracting an intersection with that sector costs its already proved absolute bound. The remaining high-complexity contribution after removing the new complete regions still requires cancellation not supplied here.

## 8. Conditional interface for a future higher-moment input

There is an exact extension of the adapter, without an automatic bootstrap conclusion. Suppose for one fixed j with 1<=j<=k that every required eligible native family, smaller scale and smooth test satisfies the uniform higher input

\[
\sum_{0<Nu\le CH}|A_{\lambda,u}(X;V)|^{2j}
\ll D^\epsilon H X^j\|V\|_{C^{J_j}}^{2j}.
\tag{8.1}
\]

This input, like (1.2), is quantified at every reference parameter; that is needed if the Schwartz-row adapter is used.

Select 2j eligible inverse factors and apply Hölder with exponent 2j to them; each contributes scale exponent 1/2. Apply the same beta pointwise bound to the remaining odd factors. The exact forward correction now has several critical pairs among the selected factors. Increasing every selected weight from 1/2 to 1/2+delta makes all those pairs convergent; its finite truncation costs at most D^(2j delta), which still fits inside D^epsilon. Moving mask factors have the same subpower bound as before.

Thus Theorem 4.1 remains valid with T2 replaced by the product T_(2j) of the 2j largest eligible Q_I and U replaced by the product of the remaining odd Q_I:

\[
|S_{\mathbf Q}|\ll D^\epsilon HD^k
\sqrt{\frac{L_1}{\Gamma T_{2j}}}
\left(\prod_{I\in\mathcal O\setminus\mathrm{selected}}Q_I\right)^{\beta-1}.
\tag{8.2}
\]

The repeated-core version selects 2j singleton axes and uses Q_per equal to the product of the other 2k-2j lengths. Its criterion is still Q_per^(2beta-1)<=T Gamma.

This describes exactly which extra regions a future uniform fourth moment would unlock. It does not establish that input, and at an all-unit balanced repeated core with k>j it leaves the peripheral factor D^((k-j)(2beta-1)). A finite ladder of moments therefore does not become the next full diagonal moment merely by this adapter.
