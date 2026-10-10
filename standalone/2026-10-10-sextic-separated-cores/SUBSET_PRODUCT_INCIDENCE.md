# Estimating several singleton factors together

**Status:** proposed proved component bounds, conditional only on the analytic inputs explicitly stated below. A classical estimate for a whole product of inverse polynomials, combined with the exact Euler correction and a uniform pointwise bound, improves the known loss on some actual higher-moment incidence strata. The leading example is a sixth-moment triangle of pair overlaps. No full fourth or sixth moment, new zero-free boundary, or cofinal cancellation estimate is proved.

**Exact sources.**

- PR #916, commit 8d49acb264577f63374358c33636ebe8e05ccf70, standalone/2026-10-10-all-order-collision-removal/continuation-balanced-closure/BALANCED_CLOSURE.md, especially the finite inverse identity and the fixed-row-range absorption. Its predecessor PROOF.md gives the same local inverse coefficient.
- PR #915, commit 9959364671f89b86f3992ec5ed5e19f804eb607b, standalone/2026-10-10-sextic-critical-core/ANISOTROPIC_SINGLETON_CORES.md, for the exact masked forward correction and the earlier one-axis estimate.
- PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1, standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md, Theorem 3.4, and GENERAL_MOMENT_ATTACK.md, for the classical all-row squarefree-column estimate and the exact incidence decomposition.
- PR #919, commit 9b04a887e171b3104a66cf57296ce5b0b2920d78, standalone/2026-10-10-averaged-conductor-frontier/COFINAL_AVERAGED_REDUCTION.md, for the signed averaging interface. Its conductor accounting comes from PR #914 at 0cc0428fedbbfc340044c7451b3d392c1da9a103.

All preceding files remain unchanged. The new estimate uses a finite-horizon bound for the forward correction; it does not require the small-prime enlargement used by PR #916's positive reconstruction or its balanced absorption.

## 1. Inputs and row-range quantifiers

Fix the Eisenstein field \(K\), a fixed finite set \(S\) containing the conventional bad primes and the ramification of a fixed finite-order character \(\nu\), an integer \(k\), and fixed smooth tests \(W_i\) supported in \([\alpha_i,\beta_i]\subset(0,\infty)\). Write
\[
\eta_u(n)=\nu(n)\chi_n(u),\qquad
A_{i,u}(Y)=\sum_{(n,S)=1}\mu_K(n)\eta_u(n)W_i(Nn/Y).
\tag{1.1}
\]
The sextic symbols have their original zeros on nonunits. Set \(D\ge2\), \(1\le H\le D^{A_0}\), with fixed \(A_0\), and use every nonzero element row \(Nu\le H\) at every column scale. Empty scales vanish.

The classical input is the pinned all-row sieve: arbitrary coefficients \(z_n\) on good squarefree columns \(Nn\le L\) satisfy
\[
\sum_{0<Nu\le H}\left|\sum_nz_n\chi_n(u)\right|^2
\ll_\epsilon(HL)^\epsilon
\left[H+H^{1/6}L+(HL)^{2/3}\right]\sum_n|z_n|^2.
\tag{1.2}
\]
It is a classical-sieve deduction in the cited source, not a consequence of a quasi-Riemann zero-free claim.

For the improved mixed estimate, assume the pointwise input
\[
|A_{i,u}(Y)|\ll_\epsilon D^\epsilon Y^b,
\qquad \tfrac12<b\le1,\quad
0<Nu\le H,\quad 1/\beta_i\le Y\le D.
\tag{PW}
\]
This must be uniform in the row and in every smaller scale, with the same fixed tests. At \(b=1\) it is elementary. The case \(b<1\) is an additional analytic premise; the previously cited conductor-uniform reciprocal argument is one way to supply it from its stated zero-free input.

When comparing with the native one-axis estimate, additionally assume
\[
\sum_{0<Nu\le H}|A_{i,u}(Y)|^2
\ll_\epsilon D^\epsilon HY
\quad(1/\beta_i\le Y\le D).
\tag{NM2}
\]
This is the imported native second-moment input from PR #915. Its allowed height range is retained whenever this optional input is used. The new subset bound in Theorem 4.1 itself uses (1.2) and (PW), and does not use (NM2).

Every assertion with \(D^\epsilon\) is for each prescribed positive \(\epsilon\), with constants depending on the fixed data and on polynomial bounds for moving labels. No constant may depend arbitrarily on a moving exclusion.

## 2. A classical bound for the entire physical product

### Lemma 2.1

For a nonempty subset \(J\subseteq[k]\), put \(P_J=\prod_{j\in J}Y_j\), with \(1/\beta_j\le Y_j\le D\). Then the literal product, including every collision between its factors, satisfies
\[
\boxed{\displaystyle
\left\|\prod_{j\in J}A_{j,\cdot}(Y_j)\right\|_{2,H}^2
\ll_\epsilon D^\epsilon
\left[HP_J+H^{1/6}P_J^2+H^{2/3}P_J^{5/3}\right].
}
\tag{2.1}
\]
The fixed physical row range is \(Nu\le H\), regardless of the individual \(Y_j\).

**Proof.** Use the unique incidence ideals for an ordered tuple of squarefree factors indexed by \(J\). For every \(I\subseteq J\) with \(|I|\ge2\), let \(c_I\) contain precisely the primes occurring in those factors. These shared ideals are squarefree and pairwise coprime. Their exterior Möbius, finite-character and row-character factors have modulus at most one, with every nonunit zero retained.

After fixing the shared ideals, the singleton lengths are
\[
Z_j=Y_j\Big/\prod_{\substack{I\ni j\\|I|\ge2}}Nc_I,
\qquad
P(\mathbf c)=\prod_{j\in J}Z_j
=P_J\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\tag{2.2}
\]
The singleton ideals are pairwise coprime and avoid the product of the shared ideals. Group their squarefree product into a column \(n\). The coefficient, with its fixed test weights and exact moving mask, is independent of the row, divisor-bounded, and has squared mass
\[
\ll_\epsilon D^\epsilon P(\mathbf c).
\]
One way to verify the mass is to count the \(O(\prod Z_j)\) supported factor tuples, then bound their multiplicity at a fixed product by the fixed-order ideal divisor bound. Nonempty scales satisfy \(Z_j\ge1/\beta_j\), so bounded scales below one change only fixed constants.

Apply (1.2), with column length a fixed multiple of \(P(\mathbf c)\). The norm of this core is at most
\[
D^\epsilon\left[
\sqrt H\,P(\mathbf c)^{1/2}
+H^{1/12}P(\mathbf c)
+H^{1/3}P(\mathbf c)^{5/6}\right].
\tag{2.3}
\]
The first term's shared-ideal weights are \((Nc_I)^{-|I|/2}\). Pair incidences cost harmonic logarithms up to the physical support bound \(O(D)\), and all higher incidences have convergent sums. For the second term every exponent \(|I|\) exceeds one. For the third every exponent \(5|I|/6\) exceeds one. Minkowski therefore sums (2.3) to the same expression with \(P(\mathbf c)\) replaced by \(P_J\), up to an arbitrarily small power of \(D\). Squaring proves (2.1).

If a supported product length is bounded below one, use the fixed positive lower bound from the test supports; the column sieve may be applied with \(\max(1,O(P(\mathbf c)))\), changing only a fixed constant. Thus no squarefree-only assertion has been substituted for the full physical product. \(\square\)

In particular, if \(P_J\le H^{1/2}\), all three terms are \(O(D^\epsilon HP_J)\). The lemma also provides useful information when this inequality fails.

## 3. The exact correction at several critical weights

For a moving squarefree \(C\), \((C,S)=1\), \(NC\le D^{A_1}\), define the literal pairwise-coprime core
\[
B_{C,u}(\mathbf X)=
\sum_{\substack{n_i\ \mathrm{squarefree},\ (n_i,n_j)=1\ (i\ne j)\\
(\prod_i n_i,CS)=1}}
\prod_i\mu_K(n_i)\eta_u(n_i)W_i(Nn_i/X_i),
\quad 1/\beta_i\le X_i\le D.
\tag{3.1}
\]
The exact local correction from a product of the \(A_i\) to this core is
\[
E_{C,p}(\mathbf z)=
\begin{cases}
(1-\sum_i z_i)/\prod_i(1-z_i),&p\notin S,\ p\nmid C,\\
1/\prod_i(1-z_i),&p\mid C,\\
1,&p\in S.
\end{cases}
\tag{3.2}
\]
Let \(e_C(\mathbf d)\) be its multiplicative coefficient. Outside \(C\), every nonconstant coefficient is \(1-|\operatorname{supp}\mathbf e|\); at a prime of \(C\), it is one. The exact finite identity is
\[
B_{C,u}(\mathbf X)
=\sum_{\mathbf d}e_C(\mathbf d)\eta_u(\prod_i d_i)
\prod_iA_{i,u}(X_i/Nd_i).
\tag{3.3}
\]
Only \(Nd_i\le\beta_iX_i\) contributes. This identity includes zeros at row primes and the entire moving mask.

### Lemma 3.1. Finite-horizon coefficient bound

For fixed weights \(\alpha_i\ge1/2\), the realized horizon satisfies
\[
\boxed{\displaystyle
\sum_{Nd_i\le\beta_iX_i}|e_C(\mathbf d)|
\prod_i(Nd_i)^{-\alpha_i}\ll_\epsilon D^\epsilon.
}
\tag{3.4}
\]
Several \(\alpha_i=1/2\) are permitted. The constant is uniform in \(C\) within the stated polynomial norm bound.

**Proof.** Put \(Z=\max(1,\prod_i\beta_iX_i)\ll D^k\). For any fixed \(\delta>0\), the left side is at most
\[
Z^\delta
\sum_{\mathbf d}|e_C(\mathbf d)|
\prod_i(Nd_i)^{-(\alpha_i+\delta)}.
\tag{3.5}
\]
Outside \(C\), the local absolute sum is
\[
1+\sum_{\substack{I\subseteq[k]\\|I|\ge2}}
(|I|-1)\prod_{i\in I}
\frac{(Np)^{-(\alpha_i+\delta)}}
{1-(Np)^{-(\alpha_i+\delta)}}.
\tag{3.6}
\]
Its nonconstant part is \(O_{k,\delta}((Np)^{-1-2\delta})\) at all sufficiently large primes. Its Euler product therefore converges absolutely. No denominator \(1-k/\sqrt{Np}\) occurs: the finitely many small local factors are finite.

Replacing the good-prime factor at \(p\mid C\) costs at most
\[
\prod_{p\mid C}\prod_i
\left(1-(Np)^{-(\alpha_i+\delta)}\right)^{-1}
\ll_{\delta,k,\eta}(NC)^\eta
\quad(\eta>0).
\tag{3.7}
\]
For large primes the logarithm of the local factor is at most \(\eta\log Np\); the finitely many others contribute a fixed constant. Choose \(\delta,\eta\) sufficiently small in terms of the requested \(\epsilon,k,A_1\). Equations (3.5)–(3.7) prove (3.4).

This is a finite-horizon small-power estimate, not a claim of absolute convergence at the critical weights themselves. It needs neither a prime-distribution theorem nor an enlargement of the fixed excluded set. \(\square\)

## 4. A subset estimate for the core

Write \(P=\prod_iX_i\), \(P_J=\prod_{j\in J}X_j\), and \(a=2b-1\).

### Theorem 4.1

For every nonempty \(J\subseteq[k]\), the classical input (1.2) and (PW) imply
\[
\boxed{\begin{aligned}
\|B_{C,\cdot}(\mathbf X)\|_{2,H}^2
&\ll_\epsilon D^\epsilon
\left[HP_J+H^{1/6}P_J^2+H^{2/3}P_J^{5/3}\right]
\prod_{i\notin J}X_i^{2b}\\
&=D^\epsilon HP\left(\frac P{P_J}\right)^a
\left[1+\frac{P_J}{H^{5/6}}
+\left(\frac{P_J^2}{H}\right)^{1/3}\right].
\end{aligned}}
\tag{4.1}
\]
The first line with \(J=[k]\) needs no pointwise input.

**Proof.** Fix \(J\) for the original rectangle; do not change it when the scales shorten in (3.3). At every nonempty shorter rectangle \(\mathbf Y\), apply Lemma 2.1 to the entire product on \(J\), and (PW) to each outside factor. The resulting product norm is at most
\[
D^\epsilon\left[
\sqrt H\prod_{j\in J}Y_j^{1/2}
+H^{1/12}\prod_{j\in J}Y_j
+H^{1/3}\prod_{j\in J}Y_j^{5/6}\right]
\prod_{i\notin J}Y_i^b.
\tag{4.2}
\]
Insert this bound into (3.3) and use Minkowski. The exterior row coefficient \(\eta_u(\prod d_i)\) is a contraction. The three resulting coefficient sums have weights respectively \(1/2,1,5/6\) on \(J\) and \(b\) outside \(J\). All weights are at least \(1/2\), so Lemma 3.1 applies to each. Their supports and tests are unchanged. Square the resulting sum of three terms, absorb its fixed factor, and reassign epsilon losses. This proves (4.1) uniformly in the moving exclusion. \(\square\)

If (NM2) is also available, the older one-axis bound remains an additional option:
\[
\|B_{C,\cdot}(\mathbf X)\|_{2,H}^2
\ll_\epsilon D^\epsilon HP
\left(\frac P{X_{\max}}\right)^a.
\tag{4.3}
\]
Taking a minimum of valid upper bounds is legitimate. Define the explicit cost
\[
\mathfrak F_{H,b}(\mathbf X)=
\min\left\{
\left(\frac P{X_{\max}}\right)^a,\
\min_{\varnothing\ne J\subseteq[k]}
\left(\frac P{P_J}\right)^a
\left[1+\frac{P_J}{H^{5/6}}
+\left(\frac{P_J^2}{H}\right)^{1/3}\right]
\right\}.
\tag{4.4}
\]
Without (NM2), omit the first entry of this minimum. The combined core bound is \(D^\epsilon HP\,\mathfrak F_{H,b}(\mathbf X)\).

The whole-set choice \(J=[k]\) includes the earlier classical core bound. The new proper-subset choices can beat both it and (4.3). No averaging independence between the axes is assumed.

## 5. A strict sixth-moment improvement with only pair overlaps

Take \(k=3\), \(h=21/20\), \(H=D^h\), and \(b=7/8\), so \(a=3/4\). Assume (PW) at this exponent; for comparison with the old native bound assume (NM2) too.

In the exact one-sided incidence decomposition of \(A_u(D)^3\), take the three pair ideals \(c_{12},c_{13},c_{23}\) in dyadic blocks of norm \(D^{5/24}\), and let the triple ideal be one. They are mutually coprime and avoid \(S\). The three singleton scales are all comparable to
\[
X_i=D^{1-2(5/24)}=D^{7/12},
\qquad P\asymp D^{7/4}.
\tag{5.1}
\]
The singleton ideals may be taken in the corresponding support intervals, disjoint from each other and from the shared ideals. Thus this is a feasible incidence pattern with full common gcd one. It is not a large-common-gcd example in disguise.

The old native one-axis cost has exponent
\[
a\left(\frac74-\frac7{12}\right)=\frac78.
\tag{5.2}
\]
The full classical cost has exponent
\[
\max\left\{0,\frac74-\frac56\frac{21}{20},
\frac{2(7/4)-21/20}{3}\right\}
=\max\{0,7/8,49/60\}=\frac78.
\tag{5.3}
\]
Choose \(J\) to contain two singleton axes. Then \(P_J\asymp D^{7/6}\), and its classical normalized cost has exponent
\[
\max\left\{0,\frac76-\frac78,
\frac{2(7/6)-21/20}{3}\right\}
=\max\{0,7/24,77/180\}=\frac{77}{180}.
\]
The remaining axis costs \(a(7/12)=7/16\). Therefore (4.1) gives
\[
\boxed{\displaystyle
\|B_{C,\cdot}(\mathbf X)\|_{2,H}^2
\ll_\epsilon D^\epsilon HP\,D^{623/720},
\qquad \frac{623}{720}=\frac{77}{180}+\frac7{16}
<\frac78.
}
\tag{5.4}
\]
The saving against the smaller of the two earlier bounds is \(7/720\) in the exponent.

This gain also applies to the entire exact polynomial portion whose shared ideals lie in these three dyadic blocks. Minkowski over them multiplies the squared norm by at most a constant times \(D^{2(3\cdot5/24)}=D^{5/4}\). Since \(P\asymp D^{7/4}\), the normalization becomes exactly \(HD^3\). More generally this is a special case of Theorem 6.1 below. Thus the actual sixth-moment incidence portion \(F_\triangle\) satisfies
\[
\boxed{\displaystyle
\|F_\triangle\|_{2,H}^2
\ll_\epsilon HD^{3+623/720+\epsilon}.
}
\tag{5.5}
\]
Both previous core methods gave \(HD^{3+7/8+\epsilon}\) for this same collection. The claim concerns these proved estimates, not a lower bound on the true norm.

The improvement persists at the slightly smaller optional exponent \(b=139999/160000\), if (PW) is supplied at that exponent with an arbitrary small-power loss. The new loss is
\[
\frac{77}{180}+\frac7{12}(2b-1),
\]
while the native loss is \(\frac76(2b-1)\). Their gap is positive whenever \(2b-1>11/15\), which includes both stated values of \(b\). The classical loss remains \(7/8\).

The diagonal target \(HD^3\) has not been reached. None of these statements estimates the full sixth moment at the same loss.

## 6. Aggregate incidence control and a smaller signed target

For the full \(k\)-fold inverse product, use the exact shared incidence representation
\[
A_u(D)^k=\sum_{\mathbf c}z_{\mathbf c}(u)
B_{C,u}(\mathbf X),\qquad |z_{\mathbf c}(u)|\le1,
\]
\[
X_i=D\Big/\prod_{\substack{I\ni i\\|I|\ge2}}Nc_I,
\quad C=\prod_{|I|\ge2}c_I,\quad
P=D^k\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\tag{6.1}
\]
Take a threshold \(L\ge1\). Let \(G_L\) be the exact polynomial portion consisting of complete shared-incidence blocks with
\(\mathfrak F_{H,b}(\mathbf X)\le L\).

### Theorem 6.1

With precisely the inputs used in the selected version of (4.4),
\[
\boxed{\displaystyle
\|G_L\|_{2,H}^2\ll_\epsilon D^\epsilon HD^k L.
}
\tag{6.2}
\]
The constant is uniform in the threshold \(L\).

**Proof.** The selector depends only on the fixed shared ideals, \(D,H\), and the input exponent \(b\); it does not cut individual singleton sums. Take the square root of the core bound and apply Minkowski over the selected shared labels. It remains to bound
\[
\sum_{\mathbf c}\sqrt P
\le D^{k/2}
\prod_{|I|\ge2}\sum_{Nc_I\ll D}(Nc_I)^{-|I|/2}
\ll_k D^{k/2}(\log(2D))^{\binom{k}{2}}.
\]
Restrictions are dropped only in this nonnegative majorant. Pair incidences are harmonic and higher incidences converge. Squaring and absorbing the fixed logarithmic power proves (6.2). Every moving exclusion in the core was already uniform by Lemma 3.1. \(\square\)

With (NM2), this periphery includes the older anisotropic selection whenever \((P/X_{\max})^a\le L\). It also includes the full classical selection whenever its displayed three-term cost is at most \(L\). Proper-subset choices add further configurations, as the triangle example shows: with \(L=K D^{623/720}\), for a sufficiently large fixed support-dependent \(K\), its blocks are included, while both previous costs are of order \(D^{7/8}\).

There is a direct signed consequence. Split \(A^k=G_L+R_L\). In the smooth Hermitian expansion of the entire residual norm, keep exactly those tuples for which both one-sided costs exceed \(L\), \(g_1\ne1\), and \(Ng_1\sqrt{Ng_2}>H\). Call their real signed contribution \(\mathcal T_{k,L}^{\Phi,\mathrm{sub}}\), with the coefficients, row kernel and all zeros of PR #919 retained. PR #914's positive accounting bounds survive these additional tuple restrictions. The same triangle-before-smoothing proof gives
\[
\boxed{\begin{aligned}
M_{2k}(D,H)&\le C_\epsilon HD^{k+\epsilon}(1+L)
+2\mathcal T_{k,L}^{\Phi,\mathrm{sub}}(D,H),\\
\mathcal T_{k,L}^{\Phi,\mathrm{sub}}(D,H)
&\ge-C_\epsilon HD^{k+\epsilon}.
\end{aligned}}
\tag{6.3}
\]
This is not an assertion that a signed sum gets smaller in absolute value when its domain is reduced.

At \(H=D^h\), \(L=K D^\lambda\), \(\lambda\ge0\), an upper bound
\[
\int_X^{2X}\mathcal T_{k,KD^\lambda}^{\Phi,\mathrm{sub}}
(D,D^h)\frac{dD}{D}
\le B_\epsilon X^{h+k+e+\epsilon}
\tag{6.4}
\]
for every positive loss and every \(X\ge2\) would give averaged moment excess \(\max\{\lambda,e\}\). With the fixed universal Mellin test, the pinned PR #919/#917 extraction then gives the conditional strict boundary
\[
\Re s>\frac12+\frac{5h}{12k}
+\frac{\max\{\lambda,e\}}{2k}.
\tag{6.5}
\]
The arithmetic premise (6.4) remains open. The advance is a larger proved peripheral portion at the same prescribed excess, leaving a smaller sufficient signed domain.

## 7. An explicit all-order loss profile and its limitation

For comparable singleton scales \(X_i\asymp D^x\), set
\[
\phi_h(t)=\max\left\{0,t-\frac{5h}{6},
\frac{2t-h}{3}\right\}.
\tag{7.1}
\]
Ignoring only fixed support constants, the new cost exponent is
\[
\boxed{\displaystyle
\Gamma_{k,b}(x,h)=
\min\left\{
a(k-1)x,\
\min_{1\le m\le k}
\left[a(k-m)x+\phi_h(mx)\right]
\right\}.
}
\tag{7.2}
\]
The first entry is present only with (NM2). This is a proved finite optimization over actual subset estimates, not a heuristic independence model. The triangle improvement is \(k=3,x=7/12,h=21/20\).

The estimate does not automatically improve the worst balanced top-scale core. At \(x=1\), \(1<h\le11/10\), and \(b=7/8\), every \(m\ge2\) has
\(\phi_h(m)=m-5h/6\), and
\[
a(k-m)+\phi_h(m)-a(k-1)
=(1-a)m+a-\frac{5h}{6}
\ge2-a-\frac{5h}{6}>0.
\]
The \(m=1\) classical choice adds a nonnegative cost to the native one-axis estimate. Thus the old loss \(a(k-1)\) remains the minimum at \(x=1\). The small perturbation to the earlier source-conditional \(b\) has the same conclusion.

The new balanced-only closure in PR #916 is compatible with this limitation. Its genuinely new absorption argument shows that a balanced fixed-row envelope can control rectangles after a fixed small-prime exclusion and an arbitrarily small exponent loss. It does not assert that the arithmetic moment mass is concentrated only at balanced or only at unbalanced incidence configurations. In particular, a theorem only on \(H=X^h\) still does not supply a common fixed-\(H\) envelope for all shortened \(X\).

Here every application retains one physical row range throughout all shortenings, and the subset \(J\) remains fixed within each convolution estimate. No balanced-curve theorem is substituted for that quantifier. The new region and losses are substantive component improvements, but the nearly coprime top-scale balanced core and the remaining signed averages still require additional arithmetic cancellation.
