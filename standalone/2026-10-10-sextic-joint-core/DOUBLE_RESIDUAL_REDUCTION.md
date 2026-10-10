# Combining one-sided incidence control with Hermitian conductor sectors

**Status:** proved reduction combining the pinned component theorems below. The remaining signed sector is strictly smaller at higher moment orders. No full higher-moment estimate or new zero-free boundary follows without bounding that sector.

**Exact sources:** [PR 914, CONDUCTOR_SECTORS.md](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md), especially Theorem 7.1, Corollary 7.2, Theorem 8.1 and Section 10; SHA256 c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983. The other input is [PR 915, ANISOTROPIC_SINGLETON_CORES.md](https://github.com/GettysburgResearch/riemann/blob/9959364671f89b86f3992ec5ed5e19f804eb607b/standalone/2026-10-10-sextic-critical-core/ANISOTROPIC_SINGLETON_CORES.md), Sections 1–4, SHA256 4854a01c2767a1dc4d7c67c490e5502bcad8935bce3089ba5f37adb1e6d02ea8.

**Dependencies and scope:** PR 914's selected-sector bounds use elementary counting and smooth character completion. PR 915's one-sided estimate uses the inherited all-row native second moment; its optional exponent \(b<1\) also needs the explicitly stated uniform pointwise bound. The case \(b=1\) needs no additional pointwise premise. All moment orders and smooth tests are fixed; all moving masks are retained. This is a new composition of proposed component theorems, not a promotion to an integrated proof.

## 1. The two notions of singleton are different

Fix \(k\ge2\), \(H=D^{1+\theta}\), and the literal inverse polynomial
\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\]

For an ordered \(k\)-tuple \(\mathbf n=(n_1,\ldots,n_k)\) in \(A_u(D)^k\), use its exact one-sided incidence ideals
\[
n_i=\prod_{I\ni i}c_I,\qquad
X_i=\frac{D}{\prod_{\substack{I\ni i\\|I|\ge2}}Nc_I},
\qquad
P(\mathbf n)=\prod_iX_i,\qquad
Q(\mathbf n)=\frac{P(\mathbf n)}{\max_iX_i}.
\tag{1.1}
\]
The ideals \(c_I\) are squarefree and pairwise coprime. A prime in \(c_{\{i\}}\) appears once on this side; it may still appear on the other side of a Hermitian moment expansion. Nonempty supports give the same fixed lower bounds on the \(X_i\) as in PR 915.

For a full Hermitian tuple \((\mathbf n,\mathbf m)\), define \(g_1\) to contain the primes appearing exactly once among all \(2k\) factors. Define \(g_2\) to contain the nonprincipal primes appearing exactly twice; these are precisely same-side double occurrences. Put
\[
\mathcal E(\mathbf n,\mathbf m)=Ng_1\sqrt{Ng_2}.
\tag{1.2}
\]
These are the two-sided quantities from PR 914. In particular, \(g_1\) is generally not the product of the one-sided singleton ideals from (1.1).

Write \(f\) for the primitive residual conductor: it is the product of primes whose number of occurrences on the left minus their number on the right is nonzero modulo six.

## 2. Exact residual polynomial and residual Hermitian sum

For \(Q_0\ge1\), split the finite polynomial exactly as
\[
A_u(D)^k=G_{Q_0}(u)+R_{Q_0}(u),
\tag{2.1}
\]
where \(G_{Q_0}\) contains precisely the ordered tuples with \(Q(\mathbf n)\le Q_0\), and \(R_{Q_0}\) contains the remaining tuples. The coefficients, characters and all coprimality restrictions of each tuple remain unchanged.

The selector \(Q(\mathbf n)\le Q_0\) depends only on the shared ideals \(c_I\), \(|I|\ge2\). Thus \(G_{Q_0}\) is a union of complete singleton-core blocks, precisely the type of polynomial portion covered by the anisotropic theorem.

The anisotropic theorem gives, for every \(\epsilon>0\),
\[
\sum_{0<Nu\le H}|G_{Q_0}(u)|^2
\ll_\epsilon HD^{k+\epsilon}Q_0^{2b-1},
\qquad \tfrac12<b\le1,
\tag{2.2}
\]
under its stated inputs. Use \(b=1\) when only the inherited native second moment is invoked.

Choose a fixed nonnegative radial \(\Phi\in C_c^\infty(\mathbb C)\), with \(\Phi(z)\ge1\) on \(|z|\le1\), exactly as in PR 914. Write \(S_{\mathbf n,\mathbf m}^{\Phi}(H)\) for the complete smooth row character sum and
\[
c(\mathbf n,\mathbf m)
=\prod_i a_{n_i}\overline{\prod_i a_{m_i}},
\qquad
a_n=\mu_K(n)\nu(n)W(Nn/D).
\]
A fixed supremum norm of \(W\) only changes the constants.

Define the new signed remainder
\[
\begin{aligned}
\mathcal T_{k,Q_0}^{\Phi}(D,H)
=\sum_{\substack{Q(\mathbf n)>Q_0,\ Q(\mathbf m)>Q_0\\
g_1(\mathbf n,\mathbf m)\ne1\\
\mathcal E(\mathbf n,\mathbf m)>H}}
c(\mathbf n,\mathbf m)S_{\mathbf n,\mathbf m}^{\Phi}(H).
\end{aligned}
\tag{2.3}
\]
Its tuple set is invariant under exchanging the two sides, so \(\mathcal T_{k,Q_0}^{\Phi}\) is real.

**Proposition 2.1.** Uniformly in \(Q_0\ge1\),
\[
\boxed{\displaystyle
\sum_{0<Nu\le H}|A_u(D)|^{2k}
\ll_\epsilon
HD^{k+\epsilon}\bigl(1+Q_0^{2b-1}\bigr)
+2\max\{0,\mathcal T_{k,Q_0}^{\Phi}(D,H)\}.}
\tag{2.4}
\]
The notation means that the coefficient of the first term is a fixed implied constant; the last term may equivalently be replaced by \(2|\mathcal T_{k,Q_0}^{\Phi}|\).

**Proof.** First apply the norm inequality to the exact polynomial split:
\[
\sum_{0<Nu\le H}|A_u(D)|^{2k}
\le2\sum_{0<Nu\le H}|G_{Q_0}(u)|^2
+2\sum_{0<Nu\le H}|R_{Q_0}(u)|^2.
\tag{2.5}
\]
The first term is controlled by (2.2). Positivity applies to the entire second squared norm and gives
\[
\sum_{0<Nu\le H}|R_{Q_0}(u)|^2
\le\sum_{u\in\mathcal O_K}\Phi(u/\sqrt H)|R_{Q_0}(u)|^2.
\tag{2.6}
\]
Expand this last nonnegative expression. Both side tuples now satisfy \(Q>Q_0\).

PR 914 bounds the sum of absolute completed contributions over all no-singleton tuples and over all nonprincipal tuples with \(\mathcal E\le H\). These are positive accounting bounds, so they remain true after imposing the two additional tuple restrictions. All principal tuples have no singleton prime. Therefore the exact decomposition of (2.6)'s right side is
\[
\sum_u\Phi(u/\sqrt H)|R_{Q_0}(u)|^2
=\mathcal T_{k,Q_0}^{\Phi}(D,H)+O_\epsilon(HD^{k+\epsilon}).
\tag{2.7}
\]
The entire left side is nonnegative. Substituting (2.7) and (2.2) into (2.5), and increasing the controlled constant if necessary, proves (2.4). \(\square\)

This proof does not majorize a signed sharp-row sector by a smooth one. It also does not claim that every Hermitian cross-term involving \(G_{Q_0}\) has a separate diagonal-size absolute bound. Those cross-terms are handled by the norm inequality (2.5). This distinction is necessary for a legal combination of the two sources.

## 3. Quantitative consequence and the precise new target

If \(Q_0=D^{o(1)}\), then \(Q_0^{2b-1}\) is absorbed into the arbitrary small-power loss. Thus the desired moment bound follows from the single additional estimate
\[
\boxed{\displaystyle
\mathcal T_{k,Q_0}^{\Phi}(D,D^{1+\theta})
\ll_\epsilon HD^{k+\epsilon}.}
\tag{3.1}
\]
Every tuple in this new target simultaneously has:

- a value of \(Q\) exceeding the chosen subpower cutoff on each side;
- a genuine singleton prime in the full \(2k\)-tuple;
- global singleton/double complexity \(Ng_1\sqrt{Ng_2}>H\).

The original PR 914 remainder imposes only the last two conditions. The original one-sided incidence reduction imposes only the first condition on both sides before any Hermitian conductor analysis. Equation (3.1) combines them without losing signs in the remaining sum.

More generally, \(Q_0=D^q\), with fixed \(q\ge0\), makes the proved part in (2.4)
\[
\ll_\epsilon HD^{k+(2b-1)q+\epsilon}.
\tag{3.2}
\]
This is an explicit tradeoff between the size of the omitted one-sided portion and the allowed moment excess. It does not bound the new signed remainder. For \(b=1\) the excess is \(q\); the optional uniform cancellation exponent improves it to \((2b-1)q\).

The stronger fixed-block bound from PR 914 also survives all the new tuple restrictions:
\[
\sum_{\substack{Q(\mathbf n),Q(\mathbf m)>Q_0\\
L\le Ng_1<2L,\ C\le Ng_2<2C\\f\ne1}}
|c(\mathbf n,\mathbf m)S_{\mathbf n,\mathbf m}^{\Phi}(H)|
\ll_\epsilon D^{k+\epsilon}\min\{H\sqrt L,L\sqrt C\}.
\tag{3.3}
\]
This follows by taking a subset of its positive accounting quantity. No improved power in the right side of (3.3) has been derived from the additional \(Q\)-restrictions.

## 4. The restrictions are complementary

For the strictness examples, take a subpower cutoff \(Q_0(D)\to\infty\), so every support-dependent bounded value of \(Q\) is eventually included in the peripheral portion.

At \(k=3\), take left and right tuples of the respective forms
\[
(a,c,c),\qquad (a',c',c'),
\]
with all four squarefree ideals mutually coprime and with norms comparable to \(D\), within the fixed annulus. Both one-sided incidence configurations have
\(\mathbf X\asymp(D,1,1)\), hence \(Q\asymp1\). But the full tuple has
\[
Ng_1=N(aa')\asymp D^2,\qquad
Ng_2=N(cc')\asymp D^2,\qquad
\mathcal E\asymp D^3.
\]
For \(H=D^{1+\theta}\), \(0<\theta<1\), PR 914's original signed remainder retains such tuples; the residual sum (2.3) excludes them. This proves a strict refinement of the remaining tuple domain. It does not claim an absolute bound for an arbitrarily selected subset of these cross-terms.

For every \(k>3\), use \((a,c,\ldots,c)\) and \((a',c',\ldots,c')\), with \(k-1\) copies of the repeated ideal on each side. Again \(Q\asymp1\), whereas \(Ng_1\asymp D^2\). The repeated primes may be nonprincipal or principal according to \(k-1\) modulo six, but they are not singleton primes, and \(\mathcal E\ge Ng_1\asymp D^2>H\). Thus this strictness example extends to every fixed \(k\ge3\).

Conversely, let \(p,q,a,b,c\) be mutually coprime squarefree ideals, with
\[
Np,Nq\asymp D^\eta,\quad
Na,Nb\asymp D^{1-\eta},\quad Nc\asymp D,
\qquad 0<\eta<1,
\]
and use the tuples
\[
(pa,pb,c),\qquad(qa,qb,c).
\]
Their one-sided scales are
\(\mathbf X\asymp(D^{1-\eta},D^{1-\eta},D)\), so
\(Q\asymp D^{2-2\eta}\) on both sides. Nevertheless every prime appears at least twice in the full tuple. PR 914's no-singleton theorem controls it, including its nonprincipal residual primes at \(p,q\). Thus the Hermitian reduction also removes configurations left by the one-sided subpower cutoff.

For \(k>3\), append \(k-3\) copies of one additional squarefree ideal of norm comparable to \(D\), coprime to the preceding ideals, on both sides. The values of \(Q\) remain polynomially large, and no full-tuple singleton is introduced.

These witnesses are statements about feasible dyadic incidence patterns, with constants adjusted to the support annulus. They do not assert that an isolated summand is large.

At the fourth moment, the equal-length one-sided incidence reduction has \(X_1=X_2\), so the subpower periphery is already a short balanced core controlled in earlier work. This combination provides a cleaner restricted fourth-moment target, but no new fourth-moment exponent or enlarged balanced-core estimate is established.

The substantive result is the quantified reduction (2.4) and the simultaneous restrictions in (3.1). Bounding the remaining long, two-sided singleton sector still requires new arithmetic cancellation.
