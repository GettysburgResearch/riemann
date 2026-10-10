# An exact cubic A2 completion of the balanced Gauss coefficient

**Status:** proposed proved arithmetic completion, exact inverse projection, quantitative norm-transfer theorems, and an exact signed first-Poisson diagonal identity with a uniform subpower bound. These supply an explicit coefficient family for the previously missing two-factor completion and remove the entire signed dual diagonal from the remaining analytic target. They do **not** prove a reflection estimate for the literal moving sextic twists, the short-row fourth moment, 17/24, or RH.

**Scope:** the squarefree balanced two-factor Gauss family produced by row Poisson in the imported October 5 argument, over the Eisenstein field. All auxiliary ideals, moving exclusions, and character zeros are retained. The native proofs below establish the exact coefficient identities and their norm estimates. The historical identification with an A2 Weyl-group multiple Dirichlet series uses the primary source specified below; no unproved analytic adapter is attributed to that source.

**Source inspected:** Brubaker, Bump, Chinta, Friedberg and Hoffstein, *Weyl Group Multiple Dirichlet Series I*, March 30, 2006, https://chinta.ccny.cuny.edu/publ/wmd1.pdf. The relevant exact interfaces are its coprime formula (5), prime-power table (13), twisted multiplicativity (20), and Theorem 2 / functional equation (25). Its initial heuristic discussion is not being used as the proof of the coefficient identification: (13) and (20) are the rigorous definition in Section 3. The manuscript's literal theorem for its specified local data is distinguished from the moving-twist extension needed here.

**Repository dependencies:** OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, definition of `a_xi` and `eq:crt-a`; PR #913 head `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `FOURTH_MOMENT_ATTACK.md`, Sections 3–5, for the existing structured transfer and precise missing interfaces. The current work does not modify those sources.

**What was done:** read the source coefficients and exact Gauss normalizations; derived every local correction coefficient; proved a five-label global identity, its signed inverse, exact child scales, and an all-row norm inequality in both directions. Applied the existing all-row sieve to bound the completion tail. Undid the source's exact coprimality-removal bijection to identify its full signed dual diagonal as the original algebraic diagonal minus its zero Fourier term, and bounded it uniformly by smooth lattice Poisson. No numerical zero computation, new large sieve, or new automorphic continuation theorem was proved.

**Review history:** the earlier version with the weaker continuum-cancellation argument and bound \(O(D^\epsilon(H+\sqrt H))\) had SHA-256 `c29068d5797c935a9ea28580bc3fd5217f1d416c9c9364cff541e0ea97efcb97`. Section 6 below replaces that theorem by a stronger exact identity and uniform \(O(D^\epsilon)\) bound; the new argument requires its own review and does not alter what was reviewed at the earlier hash.

## 1. Why A2 is the exact candidate

Write

\[
\kappa_n(x)=\chi_n(x)^2=(x/n)_3,
\qquad
\lambda(n)=\overline{\alpha(n)}\,\xi(n),
\qquad
\gamma(n)=\frac{g_3(1,n)}{\sqrt{Nn}}.
\]

Here \(g_3\) uses the same additive character as the repository's \(\gamma_2\), so \(a_\xi(n)=\lambda(n)\gamma(n)\) on squarefree ideals. Primary generators are chosen multiplicatively outside the fixed bad-prime set \(S\). Cubic reciprocity is exact on these generators: squaring the source's sextic reciprocity factor \(\mathcal R(a,b)\in\{\pm1\}\) eliminates it.

For coprime squarefree \(a,b\),

\[
a_\xi(ab)
=a_\xi(a)a_\xi(b)\chi_b(a)^4
=a_\xi(a)a_\xi(b)\kappa_b(a)^{-1}.                 \tag{1.1}
\]

The last factor is exactly the A2 edge interaction. In the primary source's rigorous coefficient system, its coprime squarefree restriction is

\[
H_{A_2}(a,b)=g_3(1,a)g_3(1,b)\kappa_b(a)^{-1}.     \tag{1.2}
\]

Thus normalizing the two Gauss sums and multiplying by the two copies of the fixed multiplicative factor \(\lambda\) gives the literal balanced coefficient. No assertion is being made that the canonical coefficient beyond this coprime face equals \(a_\xi(n_1n_2)\): that expression is not even the source's squarefree coefficient when the product is not squarefree.

The interaction-graph diagnosis for more than two factor axes is proved separately in [INTERACTION_GRAPH.md](INTERACTION_GRAPH.md). This note concerns the fully explicit A2 arithmetic completion.

## 2. The normalized prime-power table

Let \(p\notin S\), \(q=Np\), and put

\[
g=g_3(1,p),\qquad \gamma_p=g/\sqrt q,\qquad
a_p=\lambda(p)\gamma_p,\qquad b_p=\sqrt q\,\lambda(p)^3.
\]

Define the normalized full A2 coefficient by

\[
\mathfrak a_\xi(n_1,n_2)
=\frac{\lambda(n_1n_2)H_{A_2}(n_1,n_2)}
       {\sqrt{Nn_1Nn_2}}.                               \tag{2.1}
\]

Its nonzero local values are exactly

| \((v_p(n_1),v_p(n_2))\) | \(\mathfrak a_\xi(p^{v_p(n_1)},p^{v_p(n_2)})\) |
| --- | --- |
| \((0,0)\) | \(1\) |
| \((1,0)\), \((0,1)\) | \(a_p\) |
| \((1,2)\), \((2,1)\) | \(b_p\) |
| \((2,2)\) | \(b_pa_p\) |

All other pairs have coefficient zero. In particular \((1,1)\) is absent. The normalized local polynomial is

\[
1+a_p(x+y)+b_p(xy^2+x^2y)+b_pa_px^2y^2.            \tag{2.2}
\]

### Proof of the normalization

The primary source's table (13) has unnormalized entries

\[
1,\quad g_3(1,p),\quad
g_3(1,p)g_3(p,p^2),\quad
g_3(1,p)^2g_3(p,p^2)
\]

at the corresponding six support points. The prime-power residue symbol in the second Gauss sum is \(\kappa_p^2\). Grouping its residues modulo \(p\) gives

\[
g_3(p,p^2)=q\,g_{\kappa_p^2}(1,p).
\]

The primitive Gauss-product identity and \(\kappa_p(-1)=1\) give

\[
g_{\kappa_p}(1,p)g_{\kappa_p^2}(1,p)=q.
\]

Consequently the \((1,2)\) and \((2,1)\) unnormalized entries equal \(q^2\), and the \((2,2)\) entry equals \(q^2g\). Division by \(q^{3/2}\) and \(q^2\), respectively, followed by the factors \(\lambda(p)^3\) and \(\lambda(p)^4\), gives \(b_p\) and \(b_pa_p\). This proves (2.2). In particular, the correction coefficients have magnitude \(\sqrt q\), not one. \(\square\)

## 3. Five labels recover every full coefficient exactly

The support table gives the unique representation

\[
n_1=a c d^2 e^2,\qquad
n_2=b c^2 d e^2,                                  \tag{3.1}
\]

where \(a,b,c,d,e\) are pairwise-coprime squarefree ideals outside \(S\). They record the five nonzero nonunit local patterns, respectively \((1,0),(0,1),(1,2),(2,1),(2,2)\). Put \(C=cde\).

### Proposition 3.1. Exact full-coefficient formula

\[
\boxed{
\mathfrak a_\xi(a c d^2e^2,b c^2d e^2)
=\sqrt{NC}\,\lambda(C)^3 a_\xi(abe).
}                                                   \tag{3.2}
\]

### Proof

We first reduce the source's twisted multiplicativity (20) using cubic reciprocity. If two pairs \((n_1,n_2)\), \((m_1,m_2)\) have disjoint prime supports, their twisting factor is

\[
\kappa_{m_1}(n_1)^2\kappa_{m_2}(n_2)^2
\kappa_{m_2}(n_1)^{-1}\kappa_{n_2}(m_1)^{-1}
=\kappa_{m_1m_2}(n_1n_2)^2.                       \tag{3.3}
\]

The equality uses \(-1\equiv2\pmod3\) as well as reciprocity. Normalization and \(\lambda\) are multiplicative and do not change this twisting factor.

A prime assigned to \(c\) or \(d\) has total exponent three, so all of its cross-prime cubic interactions are trivial. A prime assigned to \(e\) has total exponent four, which is congruent to one modulo three; its cross-prime interactions are exactly those of one ordinary squarefree Gauss factor. The same is true for the singletons \(a,b\). The local table supplies \(\sqrt{NC}\lambda(C)^3\), while the remaining local Gauss factors and every nontrivial cross-prime interaction combine to \(a_\xi(abe)\) by (1.1). This proves (3.2). \(\square\)

Formula (3.2) is a statement about the actual globally twisted coefficients. It is not obtained by treating the multiple Dirichlet series as an ordinary Euler product.

## 4. Exact completion of the literal row polynomial

Fix a smooth test \(V\) supported in \([a_1,b_1]\times[a_2,b_2]\subset(0,\infty)^2\). Let \(q_0\) be a moving squarefree exclusion ideal, and let \(f\) be squarefree, both outside \(S\). Define

\[
P_{q_0}(A,B;k,f)=
\sum_{\substack{ab\text{ squarefree}\\(ab,q_0S)=1}}
a_\xi(ab)\chi_{ab}(k)\chi_{ab}(f)^4
V(Na/A,Nb/B),                                      \tag{4.1}
\]

and its full arithmetic completion

\[
Q_{q_0}(A,B;k,f)=
\sum_{\substack{n_1,n_2\\(n_1n_2,q_0S)=1}}
\mathfrak a_\xi(n_1,n_2)
\chi_{n_1n_2}(k)\chi_{n_1n_2}(f)^4
V(Nn_1/A,Nn_2/B).                                  \tag{4.2}
\]

Every symbol on nonsquarefree indices means its multiplicative extension from the local sextic symbols, including zero on nonunits. These are finite physical sums. Calling \(Q\) an arithmetic completion does not assert an analytic theta transformation for it.

For pairwise-coprime squarefree \(c,d,e\) outside \(q_0S\), set

\[
A'=\frac{A}{Nc\,(Nd)^2(Ne)^2},\qquad
B'=\frac{B}{(Nc)^2Nd\,(Ne)^2},\qquad C=cde,         \tag{4.3}
\]

and, when \((C,f)=1\), define

\[
\Omega_{c,d,e}(k,f)=
\sqrt{NC}\,\lambda(C)^3 a_\xi(e)
\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f)^4.              \tag{4.4}
\]

In particular \(|\Omega_{c,d,e}(k,f)|\le\sqrt{NC}\), uniformly in every row and auxiliary ideal. Its first row phase is quadratic; its second is cubic. The zeros at \(k\) meeting any correction prime remain present.

### Theorem 4.1. Exact completion and exact inverse projection

The following two identities hold for every nonzero row \(k\):

\[
\boxed{
Q_{q_0}(A,B;k,f)=
\sum_{\substack{c,d,e\text{ disjoint squarefree}\\(C,q_0fS)=1}}
\Omega_{c,d,e}(k,f)
P_{q_0C}(A',B';k,ef).
}                                                   \tag{4.5}
\]

\[
\boxed{
P_{q_0}(A,B;k,f)=
\sum_{\substack{c,d,e\text{ disjoint squarefree}\\(C,q_0fS)=1}}
\mu_K(C)\Omega_{c,d,e}(k,f)
Q_{q_0C}(A',B';k,ef).
}                                                   \tag{4.6}
\]

Both sums are finite on the support of \(V\). The all-unit triple is the original, undilated polynomial on each right side.

### Proof of the forward identity

Insert (3.1) and (3.2) into (4.2). Its total column ideal is

\[
n_1n_2=ab\,e\,C^3.
\]

Thus its row symbol splits as

\[
\chi_{n_1n_2}(k)=\chi_{ab}(k)\chi_{cd}(k)^3\chi_e(k)^4.
\]

Its auxiliary symbol is

\[
\chi_{n_1n_2}(f)^4
=\chi_{ab}(f)^4\chi_e(f)^4\mathbf1_{(C,f)=1}.
\]

The indicator is essential: \(\chi_C(f)^{12}\) is that mask and is not the constant one. Next use

\[
a_\xi(abe)=a_\xi(e)a_\xi(ab)\chi_{ab}(e)^4.
\]

It changes the auxiliary ideal to \(ef\), which is still squarefree because the surviving terms have \((C,f)=1\). The singleton exclusion is exactly \((ab,q_0C)=1\), and the smooth scales become (4.3). These give every factor in (4.5). \(\square\)

### Proof of the inverse identity, including the twisting

The source's coefficient system permits a prime either to be on the squarefree singleton face or to have exactly one of the three correction types. Formula (4.6) is the signed inclusion–exclusion that removes all correction primes from the full family. The following check makes sure that this remains true with the nontrivial cross-symbols.

For disjoint correction triples \((c_1,d_1,e_1)\), \((c_2,d_2,e_2)\), the scales (4.3) compose by multiplying labels, and their exterior factors satisfy

\[
\Omega_{c_1,d_1,e_1}(k,f)
\Omega_{c_2,d_2,e_2}(k,e_1f)
=\Omega_{c_1c_2,d_1d_2,e_1e_2}(k,f).                \tag{4.7}
\]

All terms are restricted so their indicated auxiliary ideals are squarefree. To prove (4.7), every factor is visibly multiplicative except for \(a_\xi(e_1)a_\xi(e_2)\). The extra phase introduced by changing \(f\) to \(e_1f\) is exactly \(\chi_{e_2}(e_1)^4\), and

\[
a_\xi(e_1)a_\xi(e_2)\chi_{e_2}(e_1)^4
=a_\xi(e_1e_2).
\]

This proves the composition law, including at zero-extended rows. Insert (4.5) for each completed child on the right side of (4.6). Its new mask \(q_0C\) forces the next correction primes to be disjoint from the outer ones. For any resulting global correction set, (4.7) says that its coefficient is independent of which subset was selected at the outer stage. The sum of its signs is

\[
\sum_{E\subseteq\{p:p\mid C_{\rm global}\}}(-1)^{|E|}
=(1-1)^{\omega(C_{\rm global})}.
\]

Only the empty global correction set survives, with coefficient one. Its remaining polynomial is precisely (4.1). This proves (4.6). All expanded sums are finite, so rearrangement has no convergence obligation. \(\square\)

**What the inverse avoids.** There is no unrestricted division of a twisted Euler product, no row-dependent coefficient insertion into an imported theorem, and no replacement of \(ef\) by a nonsquarefree auxiliary ideal. The moving mask is what makes the elementary signed projection exact. It cannot be suppressed when using this identity analytically.

## 5. The exact norm inequality in both directions

For \(X=P\) or \(Q\), let

\[
\mathcal E_X(\mathcal H,A,B,F;q_0)
=\frac1{ABF}
\sum_{\substack{F\le Nf<2F\\f\text{ squarefree},\ (f,S)=1}}
\sum_{0<Nk\le\mathcal H}|X_{q_0}(A,B;k,f)|^2.
                                                            \tag{5.1}
\]

Take \(F,\mathcal H\ge1\); factor scales can be any positive values. A child that is nonzero has \(A'\ge1/b_1\), \(B'\ge1/b_2\). Write \(\Sigma=ABF\). For every triple in (4.3), the exact child auxiliary scale and normalizer are

\[
F'=FNe,\qquad
A'B'=rac{AB}{(Nc)^3(Nd)^3(Ne)^4},\qquad
\boxed{\Sigma'=A'B'F'=\frac\Sigma{(NC)^3}.}          \tag{5.2}
\]

### Theorem 5.1. Two-sided normalized energy transfer

For either ordered pair \((X,Y)=(Q,P)\) or \((P,Q)\),

\[
\boxed{
\mathcal E_X(\mathcal H,A,B,F;q_0)^{1/2}
\le
\sum_{\substack{c,d,e\text{ disjoint squarefree}\\(C,q_0S)=1}}
\frac1{NC}\,
\mathcal E_Y(\mathcal H,A',B',FNe;q_0C)^{1/2}.
}                                                   \tag{5.3}
\]

Terms whose factor rectangles are empty may be omitted. The same fixed test \(V\), the same row range \(\mathcal H\), and the displayed moving exclusion are used in every child.

### Proof

Apply Minkowski in the full Hilbert space indexed by the original pair \((f,k)\), using (4.5) or (4.6). Fix a triple. Its row multipliers have modulus at most \(\sqrt{NC}\). Restricting to \((C,f)=1\) leaves squarefree \(f'=ef\); the map \(f\mapsto f'\) is injective and sends the original annulus exactly into the annulus \([FNe,2FNe)\). The resulting nonnegative sum may be enlarged to every squarefree \(f'\) in that annulus. No signed polynomial is enlarged at this step.

The norm contribution of this triple is at most

\[
\frac{\sqrt{NC}}{\sqrt\Sigma}\,
\sqrt{\Sigma'}\,
\mathcal E_Y(\mathcal H,A',B',F';q_0C)^{1/2}
=\frac1{NC}\,
\mathcal E_Y(\mathcal H,A',B',F';q_0C)^{1/2},
\]

by (5.2). The inverse sign has modulus one on squarefree \(C\). This proves both directions of (5.3). \(\square\)

### Corollary 5.2. Explicit polylogarithmic norm stability

Set \(Z=\max(2,b_1A,b_2B)\). Every contributing correction label has norm at most \(Z\). Consequently

\[
\sum_{\rm contributing}\frac1{NC}
\le
\left(\sum_{N\mathfrak c\le Z}\frac1{N\mathfrak c}\right)^3
\ll_K (\log(2Z))^3.                                \tag{5.4}
\]

If all children on the right side of (5.3) have energy at most \(M\), then

\[
\mathcal E_X\ll_K M\,(\log(2Z))^6.                 \tag{5.5}
\]

There is no further polynomial loss from completing the coefficient or recovering its squarefree face. This assertion includes the moving masks and changed auxiliary scale; it is not an estimate for children whose energies have not been bounded.

### Corollary 5.3. Stability of the natural all-scale envelope

Suppose, uniformly at every required smaller rectangle, moving exclusion, and auxiliary scale,

\[
\mathcal E_Y(\mathcal H,A',B',F';q_0C)
\le M\,(\mathcal H+\Sigma').                       \tag{5.6}
\]

Then

\[
\boxed{
\mathcal E_X(\mathcal H,A,B,F;q_0)
\ll_K M\left(\mathcal H(\log(2Z))^6+\Sigma\right).
}                                                   \tag{5.7}
\]

In particular, after allowing arbitrary small-power losses, the families of all-scale bounds \(\mathcal E_P\ll D^\epsilon(\mathcal H+\Sigma)\) and \(\mathcal E_Q\ll D^\epsilon(\mathcal H+\Sigma)\) are equivalent on a domain closed under the displayed child maps. Constants may depend on fixed polynomial scale limits. No bound of this strength is proved here.

**Proof.** Use \(\sqrt{x+y}\le\sqrt x+\sqrt y\) and (5.2) in (5.3). The \(\sqrt\mathcal H\) term is controlled by (5.4). The \(\sqrt\Sigma\) term has coefficient

\[
\sum_{c,d,e}(NC)^{-5/2}
\le\zeta_K(5/2)^3<\infty.
\]

Squaring gives (5.7). Both directions were already established in Theorem 5.1. \(\square\)

### Fixed-auxiliary version

If one takes only the \(k\) row norm at a fixed \(f\), and normalizes by the square-root column scale \(\sqrt{AB}\), the scalar cost of a triple is

\[
\sqrt{NC}\sqrt{\frac{A'B'}{AB}}
=\frac1{Nc\,Nd\,(Ne)^{3/2}}.                       \tag{5.8}
\]

Thus a bound of the form \(\|Y(A',B';\cdot,ef)\|_2\le M\sqrt{\mathcal H A'B'}\), uniform over those masks and auxiliary ideals, transfers in both directions with a norm loss \(O((\log(2Z))^2)\). The \(e\)-sum is absolutely convergent. The extra auxiliary-annulus enlargement in (5.3) changes that exponent \(3/2\) to \(1\), explaining the third harmonic factor there.

### Theorem 5.4. A proved all-row bound and controlled completion tail

Use the refined all-row squarefree sextic sieve in PR #913, `REFINED_ALL_ROW_SIEVE.md`, Theorem 3.4. Fix polynomial bounds in a reference parameter \(D\) for all scales and moving ideals, and allow every nonempty bounded child rectangle below one as above. For every \(\epsilon>0\), both the raw face and the full arithmetic completion satisfy

\[
\boxed{
\mathcal E_P,\mathcal E_Q
\ll D^\epsilon\left(\mathcal H+\mathcal H^{1/6}L
                         +(\mathcal HL)^{2/3}\right),
\qquad L=AB.
}                                                   \tag{5.9}
\]

For either of the exact identities (4.5) and (4.6), let \(X_{\ge R}\) be its specified polynomial portion with \(NC\ge R\ge1\). Its energy uses the original normalizer \(ABF\). Then

\[
\boxed{
\mathcal E_{X_{\ge R}}
\ll D^\epsilon\left(
\mathcal H+\mathcal H^{1/6}L R^{-3}
                +(\mathcal HL)^{2/3}R^{-2}\right).
}                                                   \tag{5.10}
\]

In particular,

\[
\boxed{
R\ge\max\left(1,(L^2/\mathcal H)^{1/6}\right)
\quad\Longrightarrow\quad
\mathcal E_{X_{\ge R}}\ll D^\epsilon\mathcal H.
}                                                   \tag{5.11}
\]

This is an actual analytic estimate on the stated completion/projection tail. It does not estimate the complementary small-correction part, which contains the original all-unit balanced core.

**Proof.** At a fixed auxiliary ideal, the product-column coefficients of \(P\) are supported on squarefree ideals of norm \(O_V(L)\), with squared mass \(O(D^\epsilon L)\) by the fixed-order ideal divisor bound. Their Gauss and auxiliary factors have modulus at most one, and the moving exclusion deletes columns. The imported all-row sieve therefore gives

\[
\sum_{0<Nk\le\mathcal H}|P_{q_0}(A,B;k,f)|^2
\ll D^\epsilon\left(\mathcal HL+\mathcal H^{1/6}L^2
                                      +\mathcal H^{2/3}L^{5/3}\right).
\]

There are \(O(F)\) auxiliary ideals in the annulus. Summing this estimate and dividing by \(LF\) proves (5.9) for \(P\). Its implied constant is independent of the moving mask and auxiliary ideal.

Insert this bound for every child in (5.3). After taking square roots, the three resulting sums have factors

\[
\begin{array}{ll}
\sqrt{\mathcal H}:& (Nc)^{-1}(Nd)^{-1}(Ne)^{-1},\\
\mathcal H^{1/12}L^{1/2}:& (Nc)^{-5/2}(Nd)^{-5/2}(Ne)^{-3},\\
\mathcal H^{1/3}L^{1/3}:& (Nc)^{-2}(Nd)^{-2}(Ne)^{-7/3}.
\end{array}                                         \tag{5.12}
\]

The first costs at most \(O((\log(2Z))^3)\); the other two are absolutely convergent. This proves (5.9) for \(Q\). Only the classical sieve, coefficient counting and Theorem 5.1 have been used, with no completed mean-square premise.

For the tail, repeat the same calculation with \(NC\ge R\). The first sum is still bounded by \(O((\log(2Z))^3)\). In the other two, the slightly stronger \(e\)-powers may be dropped. For fixed \(s>1\), ideal counting and the fixed-order divisor bound imply

\[
\sum_{N(cde)\ge R}(Ncde)^{-s}
\ll_{s,\delta}R^{1-s+\delta}
\]

for every sufficiently small \(\delta>0\). Indeed grouping by \(C=cde\) gives at most the ideal divisor function \(d_{3,K}(C)\), and partial summation of its \(O(X^{1+\delta})\) summatory bound proves the assertion. The exponents \(s=5/2\) and \(s=2\) therefore give norm factors \(R^{-3/2+\delta}\) and \(R^{-1+\delta}\). Squaring gives (5.10), with their subpower losses absorbed in \(D^\epsilon\). For the inverse tail, use the just-proved bound (5.9) for \(Q\) in exactly the same argument.

Finally, if \(R^6\ge L^2/\mathcal H\), then

\[
(\mathcal HL)^{2/3}R^{-2}\le\mathcal H,
\qquad
\mathcal H^{1/6}L R^{-3}\le\mathcal H^{2/3}\le\mathcal H.
\]

This proves (5.11). \(\square\)

At the leading fourth-moment initialization \(L=D^2\), \(\mathcal H=D^{3-\theta}\), this controls the entire correction/projection tail \(NC\ge D^{(1+\theta)/6}\) at energy \(O(D^\epsilon\mathcal H)\). It does not lower the energy of the all-unit core or meet the stronger positive-gap target \(O(\Sigma)\) in this long-dual range.

## 6. A signed first-Poisson advance: the long dual diagonal cancels

The preceding completion is useful only if the short original row length is handled without forcing a false positive-energy scale. The exact first-Poisson identity has a signed cancellation that does this for its entire dual diagonal. It is lost when \(\mu(f)\) is replaced by its absolute value.

### 6.1 The literal signed formula

Let \(v(n)\) be any row-independent coefficient supported on squarefree ideals outside \(S\) with \(\ell L\le Nn\le uL\), where \(0<\ell<u\) are fixed. Assume

\[
\sum_n|v(n)|^2\ll_\epsilon L D^\epsilon              \tag{6.1}
\]

and that all relevant scales are polynomial in a reference \(D\). The balanced allocation coefficient \(v(n)=\sum_{ab=n}V(Na/A,Nb/B)\), \(L=AB\), satisfies this condition by the divisor bound. Put

\[
R_L(n)=\sqrt{L/Nn}\,\overline{v(n)}.
\]

Let \(\Phi\) be the fixed nonnegative row smoothing in the source's `prop:poisson-reduction`, and write \(\Psi=\widehat\Phi\) for its fixed smooth compactly supported radial Fourier profile. The exact source identity `eq:initial-column-output`, with this residual coefficient carried through every finite regrouping, gives

\[
\frac1L\sum_{u\in\mathcal O_K}\Phi(Nu/H)
\left|\sum_n\mu_K(n)\nu(n)\chi_n(u)v(n)\right|^2
=Z_v+\sum_\xi c_\xi\mathcal S_\xi[v],                \tag{6.2}
\]

where the fixed finite ray coefficients \(c_\xi\) are the ones from the source, \(Z_v\ll H D^\epsilon\) by (6.1), and

\[
\begin{split}
\mathcal S_\xi[v]
={}&\frac H{L^2}
\sum_{\substack{b,f\text{ squarefree}\\(b,f)=1\\(bf,S)=1}}
\mu_K(f)Nb
\sum_{k\ne0}
\sum_{\substack{m_1,m_2\text{ squarefree}\\(m_1m_2,bS)=1}}
a_\xi(m_1)\overline{a_\xi(m_2)}\,
\chi_{m_1}(kf^4)\overline{\chi_{m_2}(kf^4)}\\
&\quad\times R_L(bfm_1)\overline{R_L(bfm_2)}
\Psi\!\left(\frac{HNk}{(Nf)^2Nm_1Nm_2}\right).
\end{split}                                         \tag{6.3}
\]

This is an equality. No absolute values, Cauchy step, or smooth separation have yet been applied. The test \(v\) need not have an automorphic interpretation for (6.3): it remains a finite column coefficient during row Poisson. A scalar cutoff equal to one on \([\ell,u]\) gives the literal source derivation with \(v\) inserted as a residual factor; its combined norm weight is exactly \(R_L\).

Let \(\mathcal D[v]\) be the portion of (6.3) with \(m_1=m_2=m\). It is independent of \(\xi\), because \(|a_\xi(m)|=1\) on the supported squarefree ideals. The source's zero extensions force \((m,f)=1\) and \((k,m)=1\). Consequently

\[
\boxed{
\mathcal D[v]
=\frac HL
\sum_{\substack{b,f,m\text{ disjoint squarefree}\\(bfm,S)=1}}
\frac{\mu_K(f)}{Nf\,Nm}|v(bfm)|^2
\sum_{\substack{k\ne0\\(k,m)=1}}
\Psi\!\left(\frac{Nk}{T_{f,m}}\right),
\qquad
T_{f,m}=\frac{(Nf)^2(Nm)^2}{H}.
}                                                   \tag{6.4}
\]

The \(m=1\) row is included with precisely the displayed condition \(k\ne0\).

### 6.2 The entire dual diagonal is the original centered algebraic diagonal

Write

\[
\rho(g)=\prod_{p\mid g}(1-(Np)^{-1}).
\]

### Theorem 6.1. Exact signed diagonal identity and a uniform subpower bound

For every \(H>0\) and every finitely supported \(v\) in the squarefree class specified above, the diagonal (6.4) satisfies the exact identities

\[
\boxed{
\begin{split}
\mathcal D[v]
&=\frac HL\sum_g|v(g)|^2
  \sum_{e\mid g}\frac{\mu_K(e)}{Ne}
  \sum_{h\ne0}\Psi\!\left(\frac{HNh}{Ne}\right)\\
&=\frac1L\sum_g|v(g)|^2
\left[
  \sum_{\substack{u\in\mathcal O_K\\(u,g)=1}}\Phi(Nu/H)
  -H\Psi(0)\rho(g)
\right].
\end{split}}                                                \tag{6.5}
\]

There is a constant depending only on the fixed field and smoothing such that

\[
\boxed{
|\mathcal D[v]|
\ll_{K,\Phi}\frac1L\sum_g|v(g)|^2\tau_K(g).
}                                                            \tag{6.6}
\]

Consequently, under (6.1) and the stated polynomial column-scale bound,

\[
\boxed{|\mathcal D[v]|\ll_{K,\Phi,\epsilon}D^\epsilon}
\quad\text{uniformly for all }H>0.                           \tag{6.7}
\]

The diagonal is independent of \(\xi\). The identities include the unit ideal and the original row \(u=0\), with the convention \((0,1)=1\). They hold for every row/column ratio. No new moment estimate or quasi-Riemann hypothesis is used.

**Proof of the first identity: undoing the exact source bijection.** In (6.4), let

\[
e=(f,k),\quad t=f/e,\quad h=k/e,\quad g=be,
\qquad z=tm.
\]

These are exactly the inverse changes of variables used immediately before the source's `eq:initial-column-output`; here the source's coprimality divisor is denoted by \(t\) to distinguish it from the coefficient \(v\). Because \(f\) is squarefree, \((t,h)=1\). The ideals \(g,t,m\) are squarefree and pairwise coprime, \(e\mid g\), and the character-zero condition \((k,m)=1\) is equivalent to \((h,m)=1\). Thus the two nonunit masks combine to

\[
\mathbf1_{(t,h)=1}\mathbf1_{(m,h)=1}
=\mathbf1_{(z,h)=1}.
\]

In particular this mask is independent of the divisor \(t\mid z\). The coefficient, residual test, and kernel transform as

\[
\frac{\mu_K(f)}{Nf\,Nm}
=\frac{\mu_K(e)\mu_K(t)}{Ne\,Nz},\qquad
bfm=gz,\qquad
\frac{HNk}{(Nf)^2(Nm)^2}
=\frac{HNh}{Ne(Nz)^2}.
\]

It follows that (6.4) is exactly

\[
\begin{split}
\frac HL\sum_g\sum_{e\mid g}\frac{\mu_K(e)}{Ne}
\sum_{\substack{z\text{ squarefree}\\(z,gS)=1}}
\frac{|v(gz)|^2}{Nz}
\sum_{\substack{h\ne0\\(h,z)=1}}
\Psi\!\left(\frac{HNh}{Ne(Nz)^2}\right)
\sum_{t\mid z}\mu_K(t).
\end{split}
\]

For each fixed \(g,z\), all divisors \(t\mid z\) occur: set \(m=z/t\), \(b=g/e\), \(f=et\), and \(k=eh\). The displayed masks are precisely what makes this reconstruction bijective. Now
\(\sum_{t\mid z}\mu_K(t)=\mathbf1_{z=1}\), proving the first identity of (6.5). Equivalently, before removing \((z_1,z_2)=1\), the condition \(m_1=m_2\) can survive only at \(z_1=z_2=1\).

**Proof of the second identity and its exact normalization.** Use the principal-character case \(\mathfrak m=1\), \(\mathfrak r=g\) of the source's `lem:poisson`. In precisely its Fourier normalization,

\[
\sum_{\substack{u\in\mathcal O_K\\(u,g)=1}}\Phi(Nu/H)
=H\sum_{e\mid g}\frac{\mu_K(e)}{Ne}
  \sum_{h\in\mathcal O_K}\Psi\!\left(\frac{HNh}{Ne}\right).
\]

The \(h=0\) term is \(H\Psi(0)\rho(g)\). Subtract it and insert the result into the first identity of (6.5). Thus the signed dual diagonal is exactly the original algebraic diagonal minus its zero Fourier term; this statement has no unspecified covolume constant.

**Proof of the uniform estimate.** Set

\[
E_\Phi(T)=\sum_{u\in\mathcal O_K}\Phi(Nu/T)-T\Psi(0).
\]

We first prove

\[
\sup_{T>0}|E_\Phi(T)|\ll_{K,\Phi}1.               \tag{6.8}
\]

For \(0<T\le1\), the fixed Schwartz bounds and the convergence of \(\sum_{u\ne0}(Nu)^{-A}\) for \(A>1\) give

\[
\sum_u|\Phi(Nu/T)|
\le |\Phi(0)|+C_A T^A\sum_{u\ne0}(Nu)^{-A}
\ll_{K,\Phi}1.
\]

The subtracted term is bounded too. For \(T\ge1\), full-lattice Poisson in the same source normalization gives

\[
E_\Phi(T)=T\sum_{h\ne0}\Psi(TNh).
\]

Since \(\Psi\) is Schwartz, the absolute value is at most
\(C_A T^{1-A}\sum_{h\ne0}(Nh)^{-A}\ll1\) for any fixed \(A>1\). This proves (6.8). The stronger source assumption that \(\Psi\) has compact support even makes this expression zero for all sufficiently large fixed \(T\).

Finite inclusion–exclusion gives

\[
\sum_{(u,g)=1}\Phi(Nu/H)-H\Psi(0)\rho(g)
=\sum_{e\mid g}\mu_K(e)E_\Phi(H/Ne).
\]

It is therefore \(O_{K,\Phi}(\tau_K(g))\), uniformly in \(H>0\). Substitution in (6.5) proves (6.6). The ideal divisor bound, (6.1), and redistribution of arbitrary epsilon losses prove (6.7). \(\square\)

**Related continuum identity.** If one replaces the row sum in (6.4) by its continuum coprime density, the corresponding coefficient at a fixed squarefree \(n=bfm\) is proportional to

\[
\sum_{bfm=n}\mu_K(f)Nf\,\varphi_K(m)
=\prod_{p\mid n}\bigl[1-Np+(Np-1)\bigr]
=\mathbf1_{n=1}.
\]

This finite local cancellation is consistent with (6.5), but the exact undoing identity is stronger: it also controls the full lattice discrepancy. Both identities require the nonunit masks; replacing the coprime density by one loses the term \(Np-1\).

### 6.3 The sharper remaining signed target

Write \(\mathcal O_\xi[v]\) for the same expression as (6.3) with the strict restriction \(m_1\ne m_2\). Theorems 6.1 and (6.2) reduce the desired normalized raw moment to

\[
|\mathcal O_\xi[v]|\ll D^\epsilon H
\quad\text{for the fixed finite set of }\xi,\quad H\ge1. \tag{6.9}
\]

This is a sufficient signed off-diagonal estimate. It is not proved here. The averaging weight \(\mu_K(f)\), the original row-dependent coupled kernel, and the complete coprimality masks must remain in it. Applying an unsigned mean-square estimate to the full dual column energy puts back the much larger diagonal volume that Theorem 6.1 has just removed.

For the balanced weight, each finite factorization of \(bf\) among its two axes expresses \(R_L(bfm)\) as a two-axis profile on the smaller scales. Theorems 4.1 and 5.1 then give the exact arithmetic A2 completion/projection of each column. In a signed bilinear version of (6.9), the two independently projected columns can have different auxiliary ideals \(e_1f\) and \(e_2f\). Their phases, masks, and the reconstructed strict off-diagonal condition must all be retained. A diagonal mean square of \(Q\) is not automatically a bound for this centered signed bilinear form.

More explicitly, Theorem 5.1 transfers positive Hilbert norms. It does **not** transfer an estimate for the absolute value of a completed energy minus its product-column diagonal: the subtraction removes positivity, and the inverse formula generates cross terms between distinct correction triples. For a correction triple \(t=(c,d,e)\), put \(s_t=c^3d^3e^4\). A child pair \((n_1,n_2)\) reconstructs the original product column \(s_tn_1n_2\). Thus for left and right corrections \(t,t'\), the pulled-back diagonal condition is

\[
s_tn_1n_2=s_{t'}n'_1n'_2.
\]

It is not the equality of the two factor pairs. Already before completion, the distinct pairs \((a,b)\) and \((b,a)\) belong to the same product-column diagonal. A sufficient centered A2 theorem must control the resulting sesquilinear family with this exact covariance subtraction, or directly retain the original signed \(b,f\)-sum in (6.9). Scalar continuation, a bound for a positive completed energy, or subtraction of only the factor-pair diagonal would not supply this missing statement.

The exact cancellation above changes the analytic task in a useful way: a large positive dual diagonal is no longer a necessary part of the estimate. It does not reduce the primitive conductor or prove cancellation of the surviving nonprincipal correlations.

## 7. What the classical analytic theorem supplies, and what still needs proof

For the literal local data allowed in the primary source, its full A2 series has the meromorphic continuation and finite Weyl symmetries asserted in Theorem 2. The coefficient matching above identifies an explicit classical completion; it does not grant every twist or quantitative estimate needed by the repository.

In the source's variables \((s_1,s_2)\), the coefficient denominator is \((Nn_1)^{2s_1}(Nn_2)^{2s_2}\). For the normalized coefficients in (2.1), the untwisted norm variables are \(w_i=2s_i-1/2\). The two base changes of norm variables become

\[
R_1(w_1,w_2)=(1-w_1,w_1+w_2-1/2),\qquad
R_2(w_1,w_2)=(w_1+w_2-1/2,1-w_2).                  \tag{7.1}
\]

This is an exact change of variables in the stated untwisted source interface. Its longer Weyl element gives \((w_1,w_2)\mapsto(1-w_2,1-w_1)\). These formulas are not a proved scale or conductor map for the actual moving-row family.

The remaining adapters are concrete:

1. **The literal twists and infinity type.** The coefficient carries \(\lambda(n_1n_2)=\overline{\alpha(n_1n_2)}\xi(n_1n_2)\), and the row multiplier is the moving finite-order sextic character \(\chi_{n_1n_2}(k)\chi_{n_1n_2}(f)^4\). The quoted finite local-data theorem is not by itself a conductor-uniform theorem for these twists. In particular, enlarging its fixed set of places with every moving \(k\) would change its constants and scattering space. One must construct the required local/infinite components and bound their dependence on the moving conductors.
2. **A quantitative completed mean square.** Meromorphic continuation and Weyl functional equations do not give (5.6). Residues, the analogues of the removed theta constant mode, smooth transforms, and the full row/auxiliary mean square must be estimated for \(Q\). The present proof supplies the exact coefficient projection and its controlled norm cost once that estimate exists.
3. **The independent initial conductor ratio.** At the longest fourth-moment core, product column length is \(L=D^2\), original row length is \(H=D^{1+\theta}\), and the first row-Poisson frequency scale is \(\mathcal H\asymp D^{3-\theta}\). The original positive-gap canonical argument requires \(\mathcal H\ll LF\), whereas \(\mathcal H/(LF)\asymp D^{1-\theta}\) on its leading \(F=1\) component. Completing the coefficient does not change that primitive-conductor calculation. A new quantitative transformation or signed cancellation is still required there.

There is also an immediate domain caution for using Theorem 5.1: its child keeps \(\mathcal H\) fixed while \(\Sigma' = \Sigma/(NC)^3\). Thus the condition \(\mathcal H\le\Sigma D^{-\kappa}\) is not automatically inherited by every child. Corollary 5.3 deliberately assumes an all-scale envelope; it must not be applied from a positive-gap theorem alone.

## 8. Result of this attack

The earlier missing two-factor completion is no longer specified only as an unknown coefficient class. It has an explicit cubic A2 arithmetic candidate with six local support points, an exact global formula, the correct quadratic phases on the cube corrections, a squarefree auxiliary update, and a signed inverse projection with only polylogarithmic loss. Its large-correction tail has a proved row-diagonal energy bound. The exact first-Poisson formula identifies the full signed dual diagonal with the original algebraic diagonal minus its zero Fourier term, yielding a uniform subpower bound for every row/column ratio. These are proved pieces of the fourth-moment program and preserve the exact source throughout.

The analytic reflection/mean-square adapter for the actual sextic row twists and the long initial dual range remain unproved. The generalized moment target is not established by this packet.
