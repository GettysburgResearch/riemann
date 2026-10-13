# A conjugate-pair conductor sieve in every fixed order

**Status:** proposed source-qualified mathematical deduction, with a finite diagnostic companion. This is an extension of a conductor argument to a larger family. It does not prove the native generalized moment, a new zeta zero-free boundary, or RH.

**Scope:** every fixed order \(n\geq3\) over a fixed number field containing \(\mu_n\); a fixed standard power-residue Hecke family. The application to native moments specializes to the Eisenstein sextic family, fixed finite ray data, literal character zeros, and arbitrary bounded column phases. All arithmetic conductor dependencies are displayed.

**Exact sources:** de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1 (2 October 2026), Theorem 1.1, Lemmas 2.4, 3.1 and 3.3, and the Poisson rearrangement in the proof of Proposition 8.1; the primary HTML source was read. For the native tuple interface use PR #929, commit `97bf40329489992e9384c34d7595af6d01a40774`, `standalone/2026-10-10-conductor-averages/CUBIC_CONDUCTOR_AVERAGE.md`, Sections 3–4. The explicit old one-label comparison is that commit's `EXPLORATION_SINGLETON_SIEVE.md`. The exact return of the signed completion to native covariance is PR #927, commit `f9939c957f5aac6b2099b591e4988991700a152b`, `SMALL_W_CORE_AUDIT.md`.

**What was actually run:** a new standard-library exact diagnostic checks finite residue identities, nonunit masks, the complete rational exponent transfer, and the feasible incidence comparison. It is not an analytic proof checker and does not independently verify the external sieve.

**Smallest remaining gap:** the long-singleton signed conductor average. The theorem below averages absolute \(L\)-values. Even a perfect absolute conductor mean leaves a term \((H L)^{1/2}D^k\), which is too large when the singleton conductor \(L\) exceeds \(H\).

## 1. The useful connection

The cubic conductor method applies Poisson summation to one member of a conjugate pair
\[
\chi_q(a)\overline{\chi_q(b)}.
\]
After reflection, the two surviving factors have the same orientation and combine into \(\chi_q(ae)\). That mechanism is not tied to order three. In order \(n\), it is precisely the family with conductor labels \(a b^{n-1}\).

For \(n=6\), the pair is \(a b^5\), not \(a b^2\). These are the two signs of the native singleton conductor. Averaging them jointly avoids treating the entire opposite sign as part of a frozen moving background.

This distinction does not extend automatically to all order-\(n\) characters ordered by conductor: their prime exponents may occupy every residue \(1,\ldots,n-1\), whereas the family here uses only \(1\) and \(n-1\). For \(n=3\) these are all the nonzero residues; for \(n\geq4\) they are a strict subfamily.

## 2. The all-row norm supplied by the fixed-order sieve

Fix the field, the bad-prime set \(S\), the ray modulus and the choices defining the standard family \(\chi_q\). Write \(I(S)\) for the good integral ideals and \(N\) for the ideal norm. All character values are extended by zero on nonunits. Put
\[
\mathcal C_n(U,V)=
\sup_{\|\lambda\|_2=1}
\sum_{\substack{x\in I(S)\\Nx\leq U}}
\left|\sum_{\substack{q\in I(S)\\Nq\leq V\\q\text{ squarefree}}}
\lambda_q\chi_q(x)\right|^2.
\]
Then, for \(U,V\geq1\),
\[
\boxed{\mathcal C_n(U,V)\ll (UV)^\epsilon
\left[
U+U^{1/n}V+
U^{1-1/n}V^{2/n}+U^{2/n}V^{1-1/n}
\right].}
\tag{2.1}
\]

Indeed write \(x=e^n x_0\), with \(x_0\) \(n\)-th-power-free. This is unique; \(e\) and \(x_0\) need not be coprime. For fixed \(e\), the factor from \(e^n\) is exactly the coefficient mask \(\mathbf1_{(q,e)=1}\). Reciprocity is handled in the fixed finite ray partition before applying Theorem 1.1. Summing its four terms over \(Ne\leq U^{1/n}\) gives respectively
\[
U\sum_e(Ne)^{-n},\quad
V U^{1/n},\quad
U^{1-1/n}V^{2/n}\sum_e(Ne)^{-(n-1)},\quad
U^{2/n}V^{1-1/n}\sum_e(Ne)^{-2}.
\]
The three displayed ideal series converge for \(n\geq3\). This proves (2.1). A fixed factor in the support endpoints has no effect. Empty subunit row ranges are omitted.

The complete-residue density, any imprimitive column exclusion, and the shorter index's nonunit zero have not been replaced by one.

## 3. A two-label theorem for every \(n\geq3\)

For \(A,B,Q\geq1\), define
\[
\mathcal K_n(A,B,Q;\lambda)=
\sum_{\substack{a\in I(S)\\a\sim A}}
\sum_{\substack{b\in I(S)\\b\sim B}}
\left|\sum_{\substack{q\in I(S)\\q\sim Q\\q\text{ squarefree}}}
\lambda_q\chi_q(a)\overline{\chi_q(b)}\right|^2.
\tag{3.1}
\]
The outer ideals need not be squarefree or coprime. Let \(M=\min(A,B)\) and \(N_0=\max(A,B)\).

### Theorem 3.1

For every fixed family and every \(\epsilon>0\),
\[
\boxed{
\mathcal K_n(A,B,Q;\lambda)
\ll (ABQ)^\epsilon\|\lambda\|_2^2
\left[
AB+
M^{1/n}N_0^{1-1/n}Q^{2/n}
+M^{1-1/n}N_0^{1/n}Q
+M^{2/n}N_0^{1-2/n}Q^{3/n}
\right].
}
\tag{3.2}
\]
Any subset of the outer pairs can be retained. A fixed finite ray restriction is allowed on either outer variable or on \(q\).

**Proof.** Conjugating the inner sum exchanges \(A\) and \(B\), while replacing \(\lambda\) by \(\overline\lambda\). Thus assume \(A\leq B\).

Here is the Poisson reduction, including the features which make it valid for every fixed order. Smoothly majorize the \(b\) annulus, split \(q\) into the fixed finite ray classes, open the square, and write \(q_1=d h_1,\ q_2=d h_2\). Because the \(q_i\) are squarefree, \(d,h_1,h_2\) are squarefree and pairwise coprime. The factor from \(d\) is
\[
\mathbf1_{(a,d)=1}\mathbf1_{(b,d)=1}.
\tag{3.3}
\]
On each ray class, the residual character
\(\widetilde\chi_{h_1,h_2}\) is primitive of conductor \(h_1h_2\), except for the bounded diagonal range \(Nh_i\asymp1\). That range contributes
\[
\ll (ABQ)^\epsilon AB\|\lambda\|_2^2.
\tag{3.4}
\]

For the other ranges remove \((b,\mathfrak c d)=1\) with the exact divisor \(r\mid\mathfrak c d\), and apply primitive-character Poisson to
\(\overline{\widetilde\chi_{h_1,h_2}}\) in \(b\). Its normalization is
\[
\frac{B}{Nr\,\sqrt{N(h_1h_2)}},
\tag{3.5}
\]
and its dual ideal has length \(N(h_1h_2)Nr/B\). The root number splits as a fixed finite ray scalar times a factor of \(h_1\) and the conjugate factor of \(h_2\): the higher-power coupling of the general source lemma is absent because the \(h_i\) are squarefree.

Separate the dual bad-prime part, writing the dual ideal as \(s e\), where \(s\mid\mathfrak c^\infty\) and \(e\in I(S)\). All resulting coefficient phases and masks depend on \(h_i,d,r,s\), and are independent of \(a,e\). Their moduli are at most one. Reflection has changed the orientation of the \(e\)-character, so its product with the surviving \(a\)-character is exactly
\[
\chi_{h_i}(a)\chi_{h_i}(e)=\chi_{h_i}(ae),
\tag{3.6}
\]
including zeros. The common \(d\)-mask in (3.3) is still retained until a nonnegative square is available.

Dyadically localize \(Nd\asymp\Delta,\ Nr\asymp P,\ Ne\asymp E\). The rapid decay of the reflected smooth transform permits
\[
E\ll (ABQ)^\eta\frac{Q^2P}{B\Delta^2 Ns}.
\tag{3.7}
\]
Mellin separation contributes only an arbitrarily small power. Remove \((h_1,h_2)=1\) by its exact Möbius divisor \(g\) before taking the nonnegative square. The new coefficients are still independent of \(a,e\). The factor \(1/Ng\) from the two norm denominators combines with their shorter length \(Q/N(dg)\); the total normalization is \(B\Delta/(QP)\). The sum over \(g\), the divisors \(r\), the bad-prime labels \(s\), and the dyadic ranges costs an arbitrarily small power: the first two are divisor sums, and the third has only a fixed number of prime generators.

Combine \(a,e\) into \(u=ae\). The number of decompositions is at most \(\tau(u)\), so the resulting nonnegative expression is bounded by the all-row norm (2.1), with
\[
U=\frac{AQ^2P}{B\Delta^2},\qquad V=\frac Q\Delta.
\tag{3.8}
\]
All harmless factors \((ABQ)^{O(\eta)}\) are absorbed by choosing \(\eta\) after the requested \(\epsilon\). More explicitly, the off-diagonal is bounded by
\[
(ABQ)^\epsilon\|\lambda\|_2^2
\sup_{\substack{1\ll P\ll\Delta\ll Q\\\text{nonempty dual ranges}}}
\frac{B\Delta}{QP}\,\mathcal C_n(U,V).
\tag{3.9}
\]
The norms in (3.9) can be interpreted with dyadic rather than initial intervals, differing only by fixed support constants. If (3.7) has no \(E\geq1\), that range is empty. No clamping of an empty range is needed.

For completeness the four substitutions in (3.9) are
\[
\begin{array}{c|c|c|c}
\text{term in }\mathcal C_n&
\text{term in }A,B,Q&\Delta\text{ power}&P\text{ power}\\ \hline
U&AQ&-1&0\\
U^{1/n}V&A^{1/n}B^{1-1/n}Q^{2/n}&-2/n&-1+1/n\\
U^{1-1/n}V^{2/n}&A^{1-1/n}B^{1/n}Q&-1&-1/n\\
U^{2/n}V^{1-1/n}&A^{2/n}B^{1-2/n}Q^{3/n}&-3/n&-1+2/n .
\end{array}
\tag{3.10}
\]
Every auxiliary exponent is nonpositive. Thus they can be discarded in this upper bound. Finally \(AQ\leq A^{1-1/n}B^{1/n}Q\) since \(A\leq B\). Adding (3.4) proves (3.2).

The source proof of Proposition 8.1 provides the same intermediate reduction (3.9) in its cubic specialization. Above, the replacement is not an unsupported appeal to “the same proof”: the two places involving the order were identified explicitly. The pair is defined by conjugation from the outset, and the all-row norm in (3.10) is the order-\(n\) norm. The primitive product conductor and the squarefree root-number splitting are precisely the general-order source lemmas. \(\square\)

For \(n=3\), the last and third terms coincide, giving the source cubic proposition. For \(n=6\), the result is
\[
\boxed{
\mathcal K_6\ll (ABQ)^\epsilon\|\lambda\|_2^2
\left[
AB+M^{1/6}N_0^{5/6}Q^{1/3}
+M^{5/6}N_0^{1/6}Q
+M^{1/3}N_0^{2/3}Q^{1/2}
\right].
}
\tag{3.11}
\]

## 4. Uniform moving-background \(L\)-means

Specialize to the Eisenstein field and the sixth-order family. Let \(\psi\) be a finite-order Hecke character of trivial infinity type, whose good conductor \(\mathfrak r\) has norm \(R\). Its local data at \(S\) belong to a fixed finite family. Restrict \(a,b\) to squarefree coprime good ideals and impose \((ab,\mathfrak r)=1\). Write
\[
\xi_{a,b}=(\psi\chi_{a b^5})^{\mathrm{prim}}.
\]
The conductor outside \(S\) has norm exactly \(R\,Na\,Nb\). At \(S\), the values are the actual primitive values, not automatically the products of the imprimitive factors.

### Theorem 4.1

For \(A,B,R\geq1\), uniformly in this moving \(\psi\),
\[
\boxed{
\begin{aligned}
\sum_{\substack{a\sim A,\ b\sim B\\ab\text{ squarefree}\\(ab,\mathfrak r)=1}}
|L(\tfrac12+it,\xi_{a,b})|^2
\ll &(RAB)^\epsilon(2+|t|)^{C_\epsilon}AB\\
&\times\left[
1+R^{1/6}M^{-2/3}
+R^{1/2}(M/N_0)^{1/3}
+R^{1/4}M^{-5/12}N_0^{-1/12}
\right].
\end{aligned}}
\tag{4.1}
\]
In particular this is
\[
\ll (RAB)^\epsilon(2+|t|)^{C_\epsilon}AB R^{1/2}.
\tag{4.2}
\]
For fixed background, it gives the tight bound \((AB)^{1+\epsilon}\) up to the vertical polynomial.

**Proof.** The primitive conductor and the fixed complex gamma factor give a common approximate-functional-equation length
\[
Q_{\max}\ll (RAB)^{1/2+\eta}(2+|t|)^{C_\eta}.
\tag{4.3}
\]
Its direct and dual pieces can be separated with \(|P+\varepsilon Q|^2\leq2|P|^2+2|Q|^2\); the root number has modulus one. Mellin separation of the smooth weights places the \(a,b\)-dependent conductor factor outside the polynomial with modulus at most \((RAB)^{O(\eta)}\). The gamma ratios have polynomial vertical growth and integrable Mellin decay.

For each piece write the unrestricted ideal index uniquely as
\[
m=s q r_0^2,\qquad s\mid S^\infty,\quad q\text{ squarefree},\quad q,r_0\in I(S).
\tag{4.4}
\]
There is no condition \((q,r_0)=1\). Fixing \(s,r_0\), their character factor has modulus at most one and is independent of the remaining \(q\). Weighted Cauchy is valid because
\[
\sum_{s\mid S^\infty}\sum_{r_0\in I(S)}
(N(s r_0^2))^{-1/2-\eta}<\infty.
\tag{4.5}
\]
At the fixed bad primes, retain the primitive \(\xi_{a,b}(s)\). This is a bounded outer multiplier after (4.5). On the good \(q\)-index the coefficient is
\(\psi(q)(Nq)^{-1/2-\eta-i\tau}\), and its squared norm on every dyad is bounded by a constant depending on \(\eta\). Its zero extension retains the moving \(\mathfrak r\)-exclusion.

On fixed finite ray classes reciprocity transforms the remaining family into the kernel of (3.11). The factors depending on the \(q\)-class are incorporated in its coefficient vector; any \(a,b\)-dependent scalar has modulus one and is outside its own square. Thus the constants do not depend on a moving background beyond the coefficient norm and the explicit length (4.3). The restrictions on the outer pair can be dropped only at this nonnegative stage.

Apply (3.11) on each dyad \(Q\leq Q_{\max}\). The powers of \(Q\) are nonnegative. Substituting \(Q=(RAB)^{1/2}\), dividing by \(AB\), and absorbing the \(\eta\)-losses yields exactly
\[
1,\quad R^{1/6}M^{-2/3},\quad
R^{1/2}(M/N_0)^{1/3},\quad
R^{1/4}M^{-5/12}N_0^{-1/12}.
\]
This proves (4.1). Each is at most \(R^{1/2}\) because \(R,M,N_0\geq1\) and \(M\leq N_0\). The only principal case has \(\mathfrak r=a=b=1\), up to the fixed bad data; its bounded number of extra approximate-functional-equation residue terms is absorbed in the displayed vertical polynomial. \(\square\)

The same argument gives the following general-order mean ratio:
\[
1+
R^{1/n}M^{2/n-1}
+R^{1/2}(M/N_0)^{1/2-1/n}
+R^{3/(2n)}M^{7/(2n)-1}N_0^{-1/(2n)}.
\tag{4.6}
\]
For \(n\geq3\) this is \(O(R^{1/2})\). This is a conjugate-pair family theorem, not a theorem for all conductor exponent patterns.

## 5. Native all-order accounting with both singleton signs

Fix \(k\), a support constant, the native bad and ray data, and a smooth nonnegative radial majorant of the sharp element-row ball. Let
\[
A_u=\sum_{n\text{ good squarefree}}c_n\chi_n(u),\qquad
|c_n|\leq1,\quad Nn\ll D.
\]
A \(2k\)-tuple has signed prime multiplicities \(r_p-s_p\). Let \(g_m\) be the product of nonprincipal primes appearing exactly \(m\) times; let \(q_0\) be the product of principal-mask primes. The exact row character and its principal mask are those of #929, Section 3.

Separate the singleton signs:
\[
g_1=a_+a_-,\qquad
a_+=\prod_{r_p=1,s_p=0}p,\qquad
a_-=\prod_{r_p=0,s_p=1}p.
\tag{5.1}
\]
Take a dyadic block
\[
Na_+\asymp X,\qquad Na_-\asymp Y,\qquad Ng_2\asymp G.
\]
Write \(L=XY,\ M=\min(X,Y),\ N_0=\max(X,Y)\). These are the actual tuple labels; no balance is assumed.

For this block let \(\mathcal Q^\Phi_{X,Y,G}\) be the sum of the absolute values of the exact nonprincipal tuple kernels, multiplied by the absolute values of the column coefficients. Arbitrary additional tuple selectors are permitted.

### Theorem 5.1

For every fixed \(k\) and every \(\epsilon>0\),
\[
\boxed{
\begin{aligned}
\mathcal Q^\Phi_{X,Y,G}
\ll D^{k+\epsilon}H^{1/2}L^{1/2}
\left[
1+G^{1/12}M^{-1/3}
+G^{1/4}(M/N_0)^{1/6}
+G^{1/8}M^{-5/24}N_0^{-1/24}
\right].
\end{aligned}}
\tag{5.2}
\]
All higher nonprincipal multiplicities, every principal mask, all physical rows, and all allowed coefficient phases are included.

**Proof.** Unit averaging first kills non-unit-trivial residual characters. On each remaining fixed ray class of \(a_+,a_-\), the residual ideal character is
\[
\psi_{\mathrm{bg}}\chi_{a_+a_-^5},\qquad
N\operatorname{cond}^{S}(\psi_{\mathrm{bg}})
=G\prod_{m\geq3}Ng_m.
\tag{5.3}
\]
The finite bad/unit correction depends only on the fixed ray classes, so after partitioning it belongs to the background and is independent of the varying singleton labels. This is the sextic version of the exact unit correction in #929, Lemma 3.1. The good conductors are pairwise disjoint.

The exact smooth row kernel is bounded, after its Mellin contour is shifted to \(\Re s=1/2\), by
\[
H^{1/2}\int_{\mathbb R}
|\widehat\phi(\tfrac12+it)|\,
|L(\tfrac12+it,\psi_{\mathrm{bg}}\chi_{a_+a_-^5})|
\prod_{p\mid q_0}(1+(Np)^{-1/2})\,dt.
\tag{5.4}
\]
There is no crossed pole: the tuple is nonprincipal. The product is \((Nq_0)^\eta\); this keeps the exact principal mask within an upper bound.

The physical column budget gives
\[
(Nq_0)^2 (Na_+)(Na_-)(Ng_2)^2
\prod_{m\geq3}(Ng_m)^m\ll_k D^{2k}.
\tag{5.5}
\]
Counting \(q_0\) and prime-position assignments therefore costs
\[
D^{k+\epsilon}L^{-1/2}G^{-1}
\prod_{m\geq3}(Ng_m)^{-m/2}.
\tag{5.6}
\]
The assignment multiplicity is a fixed-\(k\) divisor bound. All signs of the background prime exponents are frozen before the singleton family mean.

Cauchy over \(a_+,a_-\), followed by (4.1), gives \(XY=L\) times the square roots of its four displayed ratios. Combine this with (5.6). The positive sum over \(g_2\asymp G\) has \(O(G^{1+\eta})\) choices, including its finitely many exponent assignments at each prime, and cancels \(G^{-1}\). For every \(m\geq3\), each resulting conductor power is at most \(1/4\), so its ideal sum converges with exponent at least \(m/2-1/4\geq5/4\). The Mellin transform in (5.4) absorbs the vertical polynomial. Choosing all preliminary losses below the final \(\epsilon\) proves (5.2). \(\square\)

Consequently the following region has diagonal-size cost \(O(HD^{k+\epsilon})\):
\[
\boxed{
\begin{gathered}
L\leq H,\qquad L^6G\leq H^6M^4,\\
L^6G^3M^2\leq H^6N_0^2,\qquad
L^{12}G^3\leq H^{12}M^5N_0.
\end{gathered}}
\tag{5.7}
\]
These are simply the four conditions in (5.2), with denominators cleared. Dyadic summation costs only powers of \(\log D\). An inherited positive controlled region can be united with this one, counting overlaps once. No stronger signed full-block comparison is inferred.

## 6. A feasible strict gain over the frozen one-sign route

At \(H=D^{21/20}\), take pairwise coprime good squarefree labels and the fourth-tuple incidence
\[
(n_1,n_2;m_1,m_2)
=(c e a_1,\ c f a_2;\ d e b_1,\ d f b_2),
\tag{6.1}
\]
with norm exponents
\[
Nc\asymp D^{3/40},\quad Nd\asymp D^{17/40},\quad
Ne,Nf\asymp D^{41/80},
\quad Na_1,Na_2\asymp D^{33/80},
\quad Nb_1,Nb_2\asymp D^{1/16}.
\tag{6.2}
\]
Every original column has scale \(D\). One can use disjoint rational prime supports to avoid any implicit conjugate-prime reduction. The named scales are feasible ideal sizes, not a lower bound on any signed arithmetic sum.

Here
\[
L=D^{19/20},\quad M=D^{1/8},\quad N_0=D^{33/40},
\quad G=D^{1/2},\quad Nq_0=D^{41/40}.
\tag{6.3}
\]
The four exponents in (5.2), after division by \(HD^2\), are
\[
-\frac1{20},\qquad-\frac1{20},\qquad
-\frac1{24},\qquad-\frac{23}{480}.
\tag{6.4}
\]
Therefore
\[
\boxed{\mathcal Q^\Phi\ll HD^{2-1/24+\epsilon}.}
\tag{6.5}
\]

The unpromoted one-sign exploration in #929 has four corresponding excesses
\[
-\frac1{20},\quad-\frac1{10},\quad
+\frac1{480},\quad-\frac{11}{480}.
\tag{6.6}
\]
It does not certify this block at diagonal size. The three terms of that packet's established anisotropic cubic-conductor accounting have excesses
\[
-\frac1{20},\quad+\frac{19}{120},\quad+\frac{23}{240}.
\tag{6.7}
\]
The older classical-completion condition also fails, with excess
\(L\)'s exponent plus half \(G\)'s exponent minus \(h=3/20\).
The older balanced-divisor comparison \((4\log_D L+\log_D G)/3-h\) is \(23/60\), and the stated Wu-conductor branch has excess \(495/2048\).

Thus this is a new positive accounting region relative to those explicitly compared branches. This is not a claim of improvement over every previous signed estimate on the unselected complete smooth incidence block. Those bounds measure a different object and may use its cancellations.

## 7. The long-singleton obstruction remains visible

For \(2k\) mutually coprime columns of norm about \(D\),
\[
X\asymp Y\asymp D^k,\qquad L\asymp D^{2k},\qquad G=1.
\]
The first term in (5.2) is
\[
H^{1/2}D^{2k+\epsilon}.
\tag{7.1}
\]
It exceeds \(HD^{k+\epsilon}\) when \(H<D^{2k}\). This is the cost of the displayed upper bound, not an arithmetic lower bound.

Even if the full moving-background second mean were strengthened to perfect conductor-size cost \(AB\), the same positive tuple counting would leave the term in (7.1). Therefore further improvement of the positive conductor mean alone cannot reach the nearly-coprime leading core. It must be combined with signed cancellation across singleton assignments, or with a method that reorganizes those assignments before taking their absolute values.

This identifies exactly what the generalization has achieved: it improves how the two singleton signs interact with the background conductor. It does not create the missing cancellation among the longest singleton products.

## 8. Validation scope and source integrity

The finite checker accompanying this note is newly written. It covers the local identities
\(\chi(ab^5)=\chi(a)\overline{\chi(b)}\), including nonunits; common-gcd mask extraction; recombination \(\chi(a)\chi(e)=\chi(ae)\); all auxiliary exponent identities for sampled integer orders; general-order moving-background exponents; and the exact feasible comparison in Section 6. Negative controls deliberately use the cubic power \(2\) in order \(6\), replace a nonunit zero by one, and remove the common-prime mask.

No finite computation proves (2.1), (3.9), the approximate functional equation, or the native Mellin source. The new analytic content requiring an independent mathematical review is the general-order Poisson reduction and its uniform moving-background composition. The fixed source theorem is credited rather than re-certified here.

