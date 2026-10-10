# Complete signed cross-gcd graph sectors at every fixed moment order

Status: proposed source-conditional component theorems, with complete proofs below. The estimates apply to entire unions of overlapping graph sectors, including all near-perfect cross matchings. A spanning-forest theorem gives additional diagonal-size domains, and a fractional cycle charge improves a specified family at every fixed order. No full higher moment, new zero-free boundary, or cofinal cancellation theorem is asserted.

Scope: the actual zero-extended inverse Möbius/sextic family over the Eisenstein field; every nonzero element row; fixed even order; fixed smooth original tests. The required native second moment and optional pointwise exponent retain the uniformity and height assumptions of the previous graph packet. Selectors may depend arbitrarily on the full tuple's **shared incidence ideals**, but not on the remaining singleton ideals. This is a substantive restriction, not an arbitrary-tuple-selector theorem.

Exact sources and dependencies:

- PR #924, commit `725b2d25ab47e57500049d93985560098c7ef3fa`, `standalone/2026-10-10-sextic-moving-labels/CROSS_GCD_GRAPH_AND_MATCHING_SECTORS.md`, SHA-256 `9dc37104e3a06c11d11f48d4e3cb2a6653b64c844aa4c316c8bf1f2cd93d9d05`: the precise native inputs, fixed-matching theorem, and prior fourth-moment union bound. The native inputs are restated below.
- PR #926, commit `086bf0560c0c2679a1fe41418f583d2c5ca743c3`, `standalone/2026-10-10-mobius-overlaps-and-sampled-moments/MOBIUS_OVERLAP_TAILS.md`, Section 6: the mixed-sign forward correction with several critical half weights. Its relevant algebra and finite-horizon argument are rederived below, so that no unmentioned odd-power pointwise input is imported.
- PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/SUBSET_PRODUCT_INCIDENCE.md`, Section 3: the finite-horizon critical-weight correction. The full shared-incidence factorization was already used in the earlier moment packets.
- PR #925, commit `506e3808d2f1e86a31a6d1f70cc7da58367c9918`, `standalone/2026-10-10-joint-divisor-covariance/SIGNED_CONDUCTOR_PROGRESS.md`, and PR #924, Section 7: their positive complete-kernel accounting can be combined with the new signed estimates as explained in Section 7. Those conductor estimates are not premises of Sections 1–6.

## 1. The native inputs and a mixed singleton core

Fix \(k\ge2\), \(K=\mathbb Q(\sqrt{-3})\), the usual finite bad set \(S\), a fixed finite-order datum \(\nu\), and fixed smooth tests \(W_v\), \(1\le v\le2k\), supported in \([\alpha_v,\beta_v]\subset(0,\infty)\). Ideals use the pinned primary-generator convention. Put

\[
\eta_u(n)=\nu(n)\chi_n(u),\qquad
A_{v,u}^{(q)}(X)=\sum_{(n,qS)=1}\mu_K(n)\eta_u(n)W_v(Nn/X).
\tag{1.1}
\]

All characters retain their literal zeros on nonunits. For the last \(k\) positions the physical coefficient uses the complex conjugate of (1.1). The conjugate estimates follow from the same native estimates, with no additional character premise.

Let \(D\ge2\), \(H=D^h\), with \(h>1\) fixed. Use one fixed nonnegative compact smooth radial row test \(\Phi\), supported after scaling in \(Nu\le c_\Phi H\). Assume, at this same physical row range for every shorter scale,

\[
\sum_{0<Nu\le c_\Phi H}|A_{v,u}^{(q)}(X)|^2
\ll_\epsilon D^\epsilon HX,
\quad 1/\beta_v\le X\le D,\quad Nq\le D^{A_0},
\tag{NM2}
\]

uniformly for each fixed \(A_0\). For \(1/2<b\le1\), also assume

\[
|A_{v,u}^{(1)}(X)|\ll_\epsilon D^\epsilon X^b
\quad(0<Nu\le c_\Phi H,\ 1/\beta_v\le X\le D).
\tag{PW}
\]

At \(b=1\), (PW) is elementary counting. At \(b<1\) it is an additional conductor-uniform premise. All constants may depend on the fixed data and on positive losses. Empty scales vanish. Set \(a=2b-1>0\). No higher-moment input is assumed.

The present theorems are deductions under the displayed (NM2) and (PW) premises. The source pins specify their intended interfaces; this manuscript does not independently establish their analytic validity over the stated uniform ranges. Every numerical specialization at \(b=7/8\) retains (PW) at that exponent.

For \(v\le k\), use \(\xi_{v,u}(n)=\eta_u(n)\) and \(V_v=W_v\); for \(v>k\), use \(\xi_{v,u}(n)=\overline{\eta_u(n)}\) and \(V_v=\overline{W_v}\). Let \(C\) be a good squarefree ideal with polynomially bounded norm, and define

\[
\mathcal B_C(\mathbf X;u)=
\sum_{\substack{a_v\ \mathrm{squarefree},\ (a_v,a_w)=1\ (v\ne w)\\
(\prod_v a_v,CS)=1}}
\prod_{v=1}^{2k}\mu_K(a_v)\xi_{v,u}(a_v)V_v(Na_v/X_v).
\tag{1.2}
\]

### Lemma 1.1. Two native axes with an arbitrary bounded row multiplier

Choose any two distinct indices \(p,q\), and set

\[
\gamma_p=\gamma_q=\tfrac12,\qquad \gamma_v=b\quad(v\ne p,q).
\tag{1.3}
\]

For any row function \(\omega\) with \(|\omega(u)|\le1\),

\[
\boxed{
\left|\sum_{u\ne0}\Phi(u/\sqrt H)\omega(u)\mathcal B_C(\mathbf X;u)\right|
\ll_\epsilon D^\epsilon H\prod_v X_v^{\gamma_v}.}
\tag{1.4}
\]

This is an integrated signed core estimate. The multiplier may depend on already frozen arithmetic labels. It may not depend on the free singleton tuple inside (1.2).

**Proof.** The exact local forward correction is

\[
E_{C,\mathfrak p}(\mathbf z)=
\begin{cases}
(1-\sum_v z_v)/\prod_v(1-z_v),&\mathfrak p\notin S,\ \mathfrak p\nmid C,\\
1/\prod_v(1-z_v),&\mathfrak p\mid C,\\
1,&\mathfrak p\in S.
\end{cases}
\tag{1.5}
\]

This is a formal identity. Substitute \(z_v=\xi_{v,u}(\mathfrak p)x_v\), including the conjugated values on the barred side. At a nonunit every involved nonconstant monomial vanishes; no character is divided out.

Let \(e_C(\mathbf d)\) be the row-independent multiplicative coefficient of (1.5). Outside \(C S\), a nonconstant prime-power monomial with support \(J\) has coefficient \(1-|J|\), so all one-axis coefficients vanish. At a prime of \(C\) its coefficient is one. The resulting finite identity is

\[
\mathcal B_C(\mathbf X;u)
=\sum_{\mathbf d}e_C(\mathbf d)
\prod_v\xi_{v,u}(d_v)
\prod_v\mathcal A_{v,u}(X_v/Nd_v),
\tag{1.6}
\]

where \(\mathcal A_{v,u}=A_{v,u}^{(1)}\) or its conjugate according to the side. Only \(Nd_v\le\beta_vX_v\) contributes. Intermediate \(d_v\) may have prime powers; the formal convolution restores the squarefree core.

For any fixed weights \(\gamma_v\ge1/2\),

\[
\sum_{Nd_v\le\beta_vX_v}|e_C(\mathbf d)|\prod_v(Nd_v)^{-\gamma_v}
\ll_\epsilon D^\epsilon.
\tag{1.7}
\]

To verify this, add a fixed positive \(\delta\) to every weight. The unmasked nonconstant local absolute mass is

\[
\sum_{|J|\ge2}(|J|-1)
\prod_{v\in J}\frac{(N\mathfrak p)^{-\gamma_v-\delta}}
{1-(N\mathfrak p)^{-\gamma_v-\delta}}
=O_{k,\delta}((N\mathfrak p)^{-1-2\delta}).
\]

Its Euler product converges. The masked local products cost at most \((NC)^\eta\) for each fixed \(\eta>0\), with the finitely many small-prime factors left intact. Returning to the original finite-horizon weights costs at most \((\prod_v\beta_vX_v)^\delta\ll D^{2k\delta}\). Choose \(\delta,\eta\) in terms of the required loss and the fixed polynomial bound on \(C\). This proves (1.7); it is not an assertion of infinite absolute convergence at the critical weights.

For each product in (1.6), retain its exterior row phase as part of \(\omega\). Take the pointwise bounds on every axis except \(p,q\), and apply Cauchy–Schwarz and (NM2) to those two axes. The result is

\[
D^\epsilon H\prod_v(X_v/Nd_v)^{\gamma_v}.
\]

The fixed bound for \(\Phi\) is absorbed in the constant. Sum by (1.7), with smaller preliminary losses. The same two native axes are used at every shortening. This proves (1.4). \(\square\)

Only the unmasked special case of (NM2) was needed in this proof; retaining its full source formulation avoids changing the inherited regime. The mixed signs were handled algebraically, without asking (PW) for a new odd incidence character.

## 2. Exact shared incidences and the permitted selectors

Write the (2k) physical squarefree columns as \(n_1,\ldots,n_k;m_1,\ldots,m_k\), or collectively \(n_v\). For each subset \(I\subseteq[2k]\) with \(|I|\ge2\), let \(c_I\) be the product of primes occurring in exactly the positions \(I\). Let \(a_v\) be the singleton ideal occurring only at \(v\). Then

\[
n_v=a_v\prod_{I\ni v}c_I.
\tag{2.1}
\]

The \(a_v,c_I\) are good squarefree ideals and are pairwise coprime. Conversely every such collection gives exactly one physical tuple. In particular, for distinct positions \(v,w\),

\[
\gcd(n_v,n_w)=\prod_{I\supseteq\{v,w\}}c_I.
\tag{2.2}
\]

A **shared-incidence selector** is any function \(\Psi(\mathbf c)\) of the ideals \(c_I\), the fixed data, and \(D\), with \(|\Psi|\le1\). It may be discontinuous and signed. Every condition on any collection of pairwise gcds qualifies, including all within-side cutoffs and every Boolean function of the cross-gcd graph. A selector on a singleton ideal, or on the residual conductor involving unfrozen singleton ideals, is not covered merely by this definition.

Define the literal complete signed sector

\[
\mathcal S_\Psi(D,H)=
\sum_{u\ne0}\Phi(u/\sqrt H)
\sum_{\mathbf n,\mathbf m}\Psi(\mathbf c)
\prod_{i=1}^k\mu(n_i)\eta_u(n_i)W_i(Nn_i/D)
\prod_{i=1}^k\overline{\mu(m_i)\eta_u(m_i)W_{k+i}(Nm_i/D)}.
\tag{2.3}
\]

After fixing every \(c_I\), put

\[
C=\prod_Ic_I,\qquad
X_v=D\Big/\prod_{I\ni v}Nc_I.
\tag{2.4}
\]

The residual singleton sum is exactly (1.2). Its exterior row factor is

\[
\Omega_{\mathbf c}(u)
=\prod_I\mu(c_I)^{|I|}\eta_u(c_I)^{r_I}
\overline{\eta_u(c_I)}^{s_I},
\quad r_I=|I\cap[k]|,\ s_I=|I\setminus[k]|.
\tag{2.5}
\]

It has modulus at most one. Even when \(r_I=s_I\), (2.5) retains the principal coprimality mask; it is not replaced by an everywhere-one zeroth power. All phases and Möbius signs remain in the exact identity before a bound is taken.

Physical support gives \(Nc_I\le B D\), for a fixed \(B\), and \(NC\le(BD)^{2k}\). Thus every mask in Lemma 1.1 has a fixed polynomial bound. Nonempty singleton scales satisfy \(X_v\ge1/\beta_v\); empty collections contribute zero.

## 3. A finite graph charge gives an analytic sector estimate

Fix the native indices \(p,q\) and their weights (1.3). Let \(G\) be a fixed simple graph on the (2k) positions. The applications use only cross edges, but the next estimate permits any edges. Assign each edge \(e\) a nonnegative real charge \(w_e\), and suppose

\[
\boxed{
\sum_{v\in I}\gamma_v-\sum_{e\in E(G),\ e\subseteq I}w_e\ge1
\quad\text{for every }I\subseteq[2k],\ |I|\ge2.}
\tag{3.1}
\]

These are finitely many explicit graph inequalities, not an assumed arithmetic cancellation estimate.

### Theorem 3.1. Weighted graph sectors

Suppose \(\Psi\) vanishes unless \(N\gcd(n_v,n_w)\ge T_e\) for every edge \(e=\{v,w\}\) of positive charge, with \(T_e\ge1\). Then

\[
\boxed{
|\mathcal S_\Psi(D,H)|
\ll_\epsilon H D^{1+2b(k-1)+\epsilon}\prod_eT_e^{-w_e}.}
\tag{3.2}
\]

Additional restrictions of any permitted shared-incidence kind remain inside \(\Psi\). They are not dropped by a monotonicity assertion about signed sums.

**Proof.** Fix the shared ideals, and use Lemma 1.1 with multiplier (2.5). The modulus of their complete row contribution is at most

\[
D^\epsilon H D^{\sum_v\gamma_v}
\prod_{|I|\ge2}(Nc_I)^{-\sum_{v\in I}\gamma_v}.
\tag{3.3}
\]

On the selector's support, (2.2) gives the exact inequality

\[
\prod_I(Nc_I)^{\sum_{e\subseteq I}w_e}
=\prod_eN\gcd(n_v,n_w)^{w_e}
\ge\prod_eT_e^{w_e}.
\tag{3.4}
\]

Use (3.4) only in the positive majorant obtained after (3.3). The remaining exponent on every \(c_I\) is at least one by (3.1). Remove their pairwise coprimality and all other constraints in this positive majorant. Elementary ideal counting gives

\[
\sum_{Nc\le BD}(Nc)^{-\lambda}\ll\log(2D)
\qquad(\lambda\ge1),
\tag{3.5}
\]

uniformly for the fixed list of exponents used here. There are only \(2^{2k}-2k-1\) shared-label axes. Their fixed logarithmic power is absorbed into \(D^\epsilon\), together with the preliminary core loss. Finally \(\sum_v\gamma_v=1+2b(k-1)=k+a(k-1)\). This proves (3.2). \(\square\)

The same proof permits a product threshold \(\prod_eN\gcd(n_v,n_w)^{w_e}\ge L\), with factor \(L^{-1}\), even without separate thresholds on its factors. The charges are chosen before the singleton correction.

## 4. Every forest, including those meeting the native axes

Let \(F\) be any forest on the (2k) positions, including isolated vertices. Give its edges the explicit charges

\[
w_{vw}=\gamma_v+\gamma_w-1
=a\left(1-\frac{{\bf1}_{v\in\{p,q\}}+{\bf1}_{w\in\{p,q\}}}{2}\right).
\tag{4.1}
\]

All charges are nonnegative.

### Lemma 4.1. Forest charges satisfy (3.1)

For a connected nontrivial component \(J\) of the induced forest (F[I]),

\[
\sum_{v\in J}\gamma_v-\sum_{vw\in E(F[J])}(\gamma_v+\gamma_w-1)
=1+\sum_{v\in J}(\deg_{F[J]}v-1)(1-\gamma_v)\ge1.
\tag{4.2}
\]

Indeed a tree has \(|J|-1\) edges, every displayed degree is at least one, and \(\gamma_v\le1\). Each isolated induced vertex contributes \(\gamma_v\ge1/2\). Thus if \(I\) has a nontrivial component its total contribution is at least one; if all its vertices are isolated, \(|I|\ge2\) gives the same result. This proves (3.1).

Consequently, if every forest edge has gcd norm at least \(T=D/R\), with \(1\le R\le D\), then

\[
\boxed{
|\mathcal S_\Psi|
\ll_\epsilon HD^{k+a(k-1-\tau_F)+\epsilon}R^{a\tau_F},\qquad
\tau_F=|E(F)|-\frac{\deg_Fp+\deg_Fq}{2}.}
\tag{4.3}
\]

This applies with every additional shared selector retained. A zero-charge edge can be retained as a selector without being used in the charge estimate.

## 5. The entire graph union and its rank

For a physical tuple define its cross-gcd graph \(G_T\) on \(k\) left and \(k\) right vertices by

\[
ij\in E(G_T)\quad\Longleftrightarrow\quad N\gcd(n_i,m_j)\ge T.
\tag{5.1}
\]

Let \(r(G)=2k-c(G)\) be its spanning-forest rank, counting isolated vertices among its (c(G)) connected components. Let (z(G)) be its number of isolated vertices. Define

\[
\tau(G)=r(G)-1+\min\{1,z(G)/2\}
=\begin{cases}
r(G),&z(G)\ge2,\\
r(G)-1/2,&z(G)=1,\\
r(G)-1,&z(G)=0.
\end{cases}
\tag{5.2}
\]

In particular \(\tau(G)=0\) for the empty graph. In a spanning forest, choose two isolated vertices if possible, otherwise one isolated vertex and one leaf, or two leaves if there are no isolated vertices. These choices exist, and their total degree is respectively \(0,1,2\). Formula (4.3) then uses exactly \(\tau_F=\tau(G)\).

### Theorem 5.1. Arbitrary unions supported on a graph domain

Let \(\mathcal G\) be any specified collection of bipartite graphs on the fixed labeled vertices. If \(\Psi\) is a permitted shared-incidence selector supported on \(G_T\in\mathcal G\), and \(\tau(G)\ge\tau_0\) throughout that collection, then

\[
\boxed{
|\mathcal S_\Psi(D,H)|
\ll_\epsilon HD^{k+a(k-1-\tau_0)+\epsilon}R^{a\tau_0},
\qquad T=D/R,\quad1\le R\le D.}
\tag{5.3}
\]

**Proof.** Partition the selector exactly according to the complete labeled graph \(G_T\). There are at most \(2^{k^2}\) pieces, a constant for fixed \(k\). On each piece choose one deterministic spanning forest and the two vertices described above. That forest's edges all have gcd norm at least \(T\), and its omitted edges and nonedges are still part of the bounded shared selector. Theorem 4.3 therefore bounds this piece with charge \(a\tau(G)\). Since \(T\ge1\), this is at most the bound with charge \(a\tau_0\). Sum the finitely many absolute bounds. This is an exact partition of signed sectors; no overlapping union is replaced by a positive tuple count. \(\square\)

### Corollary 5.2. Forest rank and the near-perfect-matching union

For \(0\le m\le k-1\), any permitted selector supported on \(r(G_T)\ge m\) satisfies

\[
\boxed{
|\mathcal S_\Psi|
\ll_\epsilon HD^{k+a(k-1-m)+\epsilon}R^{am}.}
\tag{5.4}
\]

One direct proof chooses an \(m\)-edge forest from each supported graph. It touches at most \(2m\le2k-2\) vertices, so the two native vertices can be outside it and every forest edge has charge \(a\). The finite graph partition again keeps every other selector intact. Equivalently, (5.2) gives \(\tau(G)\ge m\) whenever \(r(G)\ge m\) and \(m\le k-1\).

If \(G_T\) has a matching of size at least \(m\), it has rank at least \(m\). Thus (5.4) controls the **entire union over all such matchings**, including every intersection among them. In particular,

\[
\boxed{
G_T\text{ has a matching of size }k-1
\quad\Longrightarrow\quad
|\mathcal S_\Psi|\ll_\epsilon HD^{k+\epsilon}R^{a(k-1)}.}
\tag{5.5}
\]

The implication in this display means that the selector is supported on that condition, not an estimate for individual tuple contributions. The larger rank-at-least-(k-1) union has the same bound. At \(k=3\), it includes every graph having any two edges, including a two-edge star. At \(k=4\), it includes every graph having any three edges.

### Full perfect matchings

The union of all perfect matchings is contained in (5.5) and therefore has the same bound. Directly, for a fixed perfect matching choose the two native vertices to be the endpoints of one matching edge. That edge has charge zero; the remaining (k-1) edges have charge \(a\). Formula (4.3) gives

\[
|\mathcal S_\Psi|\ll_\epsilon HD^{k+\epsilon}R^{a(k-1)}
\tag{5.6}
\]

with every additional shared selector retained. A graph partition handles the full union. No extra \(k\)-th saving is asserted just because every coordinate is matched.

### Fourth-moment union for the full cutoff range

For \(k=2\), the event that at least one of the four cross gcds has norm at least \(D/R\) has rank at least one. With arbitrary original within-side gcd cutoffs, (5.4) gives

\[
\boxed{
|\mathcal U_C(D/R)|\ll_\epsilon HD^{2+\epsilon}R^{2b-1},
\qquad C\ge1,\quad1\le R\le D.}
\tag{5.7}
\]

This extends the sharper union cost of #924 from \(R\le D^{1/(3-2b)}\) to all \(R\le D\). At \(b=7/8\), the upper range extends from \(D^{4/5}\) to \(D\), while keeping the cost \(R^{3/4}\). The estimate covers all stars, paths, and cycles through the same bounded-selector mechanism.

### Connected graph sectors

If \(G_T\) is connected, then \(r=2k-1\), \(z=0\), and \(\tau=2k-2\). Hence the entire connected graph sector, with additional shared selectors, satisfies

\[
\boxed{
|\mathcal S_\Psi|
\ll_\epsilon HD^{k-a(k-1)+\epsilon}R^{2a(k-1)}.}
\tag{5.8}
\]

It is diagonal-size \(O(HD^{k+\epsilon})\) whenever \(R\le D^{1/2}\), uniformly at every fixed order. This is a polynomial cutoff range for an entire graph domain, not merely for one prescribed matching. It still leaves disconnected and far-separated configurations.

## 6. Fractional cycle charges and an all-order strict gain

The forest prescription is an explicit feasible choice in (3.1), not always the optimum. Here is one stronger cycle choice whose feasibility has a short proof.

Suppose a prescribed simple cycle has length \(\ell\ge4\), and the two native vertices lie outside it. Give each cycle edge the same charge

\[
w_\ell=\min\{a,\ b-1/\ell\}.
\tag{6.1}
\]

Every proper induced subgraph of the cycle is a forest of paths and isolated vertices. A path component of \(t\ge2\) vertices contributes

\[
bt-w_\ell(t-1)\ge2b-w_\ell\ge1,
\]

since \(w_\ell\le a\le b\). The full cycle contributes \(\ell(b-w_\ell)\ge1\). Isolated induced vertices have weight at least \(1/2\). Thus (3.1) holds. It also holds for disjoint unions of such cycles and forests with charges (4.1), by summing the component contributions. Every nontrivial induced component contributes at least one, and an entirely isolated induced set of at least two vertices contributes at least one.

The total charge of the cycle is

\[
\Lambda_\ell=\min\{a\ell,\ b\ell-1\},
\tag{6.2}
\]

which improves the charge \(a(\ell-1)\) of a spanning path by

\[
\Lambda_\ell-a(\ell-1)
=\min\{a,\ (1-b)(\ell-2)\}.
\tag{6.3}
\]

This gain is strictly positive when \(b<1\). It is a graph inequality feeding the proved analytic core, not a new analytic hypothesis.

### Corollary 6.1. A four-cycle with the remaining cross matches

Let \(k\ge3\), \(3/4\le b\le1\), and prescribe a four-cycle on two left and two right positions. Prescribe another (k-3) disjoint cross edges on other positions, leaving one left and one right native vertex unused. Impose gcd norm at least \(T=D/R\) on all those edges. Any additional shared-incidence selector is allowed, as is the entire union over all labeled placements of this configuration.

Give each cycle edge charge \(b-1/4\) and each disjoint edge charge \(a\). The total charge is

\[
4b-1+a(k-3)=a(k-1)+1.
\]

Theorem 3.1 therefore proves

\[
\boxed{
|\mathcal S_\Psi|
\ll_\epsilon HD^{k-1+\epsilon}R^{a(k-1)+1},
\qquad 1\le R\le D.}
\tag{6.4}
\]

The union follows by a deterministic first-configuration partition, whose pieces remain shared-incidence selectors. Its bound is smaller than (5.5) by the factor \(R/D\). It improves the corresponding spanning-forest charge by the factor \((R/D)^{2-2b}\). At \(b=7/8\) and \(k=3\), the complete selected sixth-moment sector has the explicit bound

\[
\boxed{|\mathcal S_\Psi|\ll_\epsilon HD^{2+\epsilon}R^{5/2}.}
\tag{6.5}
\]

It is diagonal-size throughout \(R\le D^{2/5}\). At general fixed \(k\), (6.4) is diagonal-size for \(R\le D^{1/(a(k-1)+1)}\). These are specified cycle-containing portions of the moment; the estimate does not control their complement.

## 7. Combining the graph sector with adjacent work

The graph bounds apply to complete row sums before any hard-conductor selector is inserted. The earlier conductor accounting bounds the positive sum of absolute complete kernels on its controlled region by \(O(HD^{k+\epsilon})\), and this accounting survives every additional tuple restriction. Therefore one may first prove any complete signed graph estimate above and then remove such a region. The resulting signed graph sector in its complement has the same bound **plus** \(O(HD^{k+\epsilon})\). When a graph bound is smaller than the diagonal scale, this added diagonal term must not be silently omitted.

In particular, #925's additional conductor regions can be combined in this way. Their selectors involve singleton conductor data and so are not automatically eligible for Lemma 1.1; their own positive complete-kernel accounting is the reason this combination is valid.

For the fourth moment, every within-side gcd cutoff is an allowed shared selector. Thus #926's improved common-factor tail, at \(b=7/8\) under its stated uniform smooth pointwise premise, can be used to select its smaller cutoff \(C=D^{(9-2h)/11}\) for \(1<h\le11/10\), and (5.7) applies at that cutoff through the full range \(1\le R\le D\). The remaining literal signed sector then has both smaller within-side gcds and every cross gcd below \(D/R\), after subtracting the separately accounted conductor regions. This narrows the sufficient remainder, but no bound on that remaining signed sum is supplied by merely reducing its tuple set.

When \(T>1\), the fully singleton graph is empty: all shared ideals are one and every long physical factor is mutually coprime to every other. Here \(\tau=0\), and the method still gives only

\[
HD^{k+a(k-1)+\epsilon}.
\tag{7.1}
\]

At the endpoint \(T=1\), equivalently \(R=D\), every gcd threshold is automatic and the graph is complete, including for mutually coprime tuples. There is then no factor \(T^{-\sum w_e}\) saving, so the same base bound (7.1) remains.

The excess is linear in \(k\) for fixed \(b>1/2\). Consequently these theorems do not establish the full fourth moment needed for \(17/24\), a cofinal hierarchy with sublinear losses, or a shrinking zeta-zero band. \(H\) throughout is the arithmetic row height, not the ordinate of a zeta zero.

The new progress is that shared graph conditions, however they overlap, can be kept inside exact signed native cores. This closes the fixed-matching-union limitation, proves stronger forest-rank domains, and permits explicit fractional cycle gains. All of these deductions use the same two native averaged axes, with a finite correction that keeps signs, exclusions, and principal masks intact.

## 8. Validation scope

The mathematical proof is the exact incidence identity, mixed-sign finite correction, two-axis native estimate, and graph inequalities above. Finite diagnostics can check the local formal coefficients, zero/sixth-root phases, graph partitions, and rational charges. They cannot establish (NM2), (PW), the infinite arithmetic estimates, or the external conductor inputs. The assembling packet must bind the exact source files, this manuscript's final content hash, and its independent review separately.
