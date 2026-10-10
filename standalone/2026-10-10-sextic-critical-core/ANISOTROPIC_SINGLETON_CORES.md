# One long singleton axis: a further controlled incidence range

Status: new source-conditional norm theorem for the actual inverse family. It uses the imported second moment, not a new higher-moment hypothesis. The optional improved exponent also uses an explicitly stated uniform pointwise bound. No full fourth or higher moment is proved.

Exact dependencies: PR 913 at 6498d6cc2eded03159c7332b25fd224ad07f89c1, standalone/2026-10-10-sextic-moment-descent/FOURTH_MOMENT_ATTACK.md, Proposition 2.1 and Section 8; its GENERAL_MOMENT_ATTACK.md, exact incidence identity and normalized overlap cost; and [PR 912 at 6afd64e042ce7b59d550c3d76e9e2cca8b2c7379, MASKS_AND_EULER_FACTORS.md](https://github.com/GettysburgResearch/riemann/blob/6afd64e042ce7b59d550c3d76e9e2cca8b2c7379/standalone/2026-10-10-generalized-inverse-moments/MASKS_AND_EULER_FACTORS.md), especially the local coefficient formula (3.4). The proof below gives the anisotropic weighted norm and combines the moving mask with the forward correction directly. No reciprocity or contour transformation is added.

## 1. Precisely quantified analytic inputs

Fix \(k\ge2\), \(\theta>0\), \(H=D^{1+\theta}\), fixed finite-order \(\nu\), bad-prime set \(S\), and fixed smooth tests \(W_i\) supported in \([a_i,b_i]\subset(0,\infty)\). Put
\[
\eta_u(n)=\nu(n)\chi_n(u),\qquad
A_u(Y;W_i)=\sum_{(n,S)=1}\mu_K(n)\eta_u(n)W_i(Nn/Y).
\]
The row set is every nonzero element with \(Nu\le H\), at every smaller column scale. Assume the native second-moment input
\[
\sum_{0<Nu\le H}|A_u(Y;W_i)|^2
\ll_{\epsilon,W_i,\theta,\nu,S}D^\epsilon H Y,
\quad 1/b_i\le Y\le D.
\tag{1.1}
\]
This is the uniform smaller-scale adapter in PR 913, Proposition 2.1; it depends on the imported canonical theorem and Poisson reduction. Empty scales below \(1/b_i\) vanish.

For an exponent \(1/2<b\le1\), also use
\[
|A_u(Y;W_i)|\ll_{\epsilon,W_i,\theta,\nu,S,b}D^\epsilon Y^b
\quad(0<Nu\le H,\ 1/b_i\le Y\le D).
\tag{1.2}
\]
At \(b=1\), this is elementary ideal counting, so it adds no analytic premise. For \(b<1\), it must be supplied uniformly in the row. The reciprocal-L argument in PR 913, Section 8, supplies (1.2) from a uniform zero-free boundary \(b\), with an arbitrarily small \(D^\epsilon\) loss. A fixed-character estimate with uncontrolled conductor constants is insufficient.

## 2. Exact forward correction, with its moving mask retained

For a moving squarefree \(C\) prime to \(S\), define
\[
B_{C,u}(\mathbf X)=
\sum_{\substack{(n_i,n_j)=1\ (i\ne j)\\(n_1\cdots n_k,CS)=1}}
\prod_{i=1}^k\mu_K(n_i)\eta_u(n_i)W_i(Nn_i/X_i),
\quad 1/b_i\le X_i\le D.
\]
Let \(P_u(\mathbf X)=\prod_i A_u(X_i;W_i)\). The Euler factors for the multivariable coefficient series of these two objects are respectively \(1-\sum_i z_i\) and \(\prod_i(1-z_i)\) at an allowed prime, with \(z_i=\eta_u(p)(Np)^{-s_i}\).

Define row-independent coefficients \(e_C(\mathbf d)\) multiplicatively by the following local formal power series:
\[
E_{C,p}(\mathbf z)=
\begin{cases}
\displaystyle\frac{1-\sum_i z_i}{\prod_i(1-z_i)},&p\not\mid C,\ p\notin S,\\[6pt]
\displaystyle\frac1{\prod_i(1-z_i)},&p\mid C,\\
1,&p\in S.
\end{cases}
\tag{2.1}
\]
At \(p\not\mid C\), every nonconstant monomial \(\mathbf z^{\mathbf e}\) has coefficient
\[
1-|\operatorname{supp}\mathbf e|;
\tag{2.2}
\]
at \(p\mid C\), its coefficient is one. Thus all single-axis correction terms vanish outside \(C\), while the mask is accounted for exactly at its primes. Coefficient multiplication gives the finite smooth identity
\[
B_{C,u}(\mathbf X)=
\sum_{\mathbf d}e_C(\mathbf d)\eta_u(d_1\cdots d_k)
P_u(X_1/Nd_1,\ldots,X_k/Nd_k).
\tag{2.3}
\]
Only \(Nd_i\le b_iX_i\) can contribute. If a row character vanishes at a prime, its nonconstant local terms vanish in the same formal identity. No zero extension is dropped.

For positive weights \(\alpha_i\) with \(\alpha_i+\alpha_j>1\) for \(i\ne j\), set
\[
\|e_C\|_{\boldsymbol\alpha}
=\sum_{\mathbf d}|e_C(\mathbf d)|\prod_i(Nd_i)^{-\alpha_i}.
\]
With \(t_i=(Np)^{-\alpha_i}\), the unmasked local absolute coefficient sum is exactly
\[
1+\sum_{\substack{I\subseteq[k]\\|I|\ge2}}
(|I|-1)\prod_{i\in I}\frac{t_i}{1-t_i}.
\tag{2.4}
\]
Every nonconstant contribution involves at least two axes. The product of (2.4) over \(p\notin S\) converges under the stated pairwise conditions; call it \(\mathfrak N_{S,\boldsymbol\alpha}\). Consequently
\[
\boxed{
\|e_C\|_{\boldsymbol\alpha}
\le\mathfrak N_{S,\boldsymbol\alpha}
\prod_{p\mid C}\prod_i(1-(Np)^{-\alpha_i})^{-1}
\ll_{\boldsymbol\alpha,S,\eta}(NC)^\eta
\quad(\eta>0).}
\tag{2.5}
\]
The inequality uses that each unmasked local absolute sum is at least one. The subpower estimate follows by bounding the logarithm of each large-prime factor by \(\eta\log Np\); the finitely many smaller primes give a fixed constant. This is uniform in \(C\).

In the application, one \(\alpha_j=1/2\) and all others equal \(b>1/2\). Then (2.4) is \(1+O_{k,b}((Np)^{-1/2-b})\), so the seminorm is finite. Its constant need not stay bounded as \(b\downarrow1/2\). Unlike the inverse-correction argument, this direct forward identity requires no enlargement of \(S\) to remove small primes: all denominators in (2.1) are single-coordinate factors with positive real weight.

## 3. The anisotropic core theorem

Write
\[
X_{\max}=\max_iX_i,\qquad P=\prod_iX_i,\qquad Q=P/X_{\max}.
\]
Assume \(NC\le D^{C_0}\), for fixed \(C_0\). Then (1.1)–(1.2) imply
\[
\boxed{
\|B_{C,\cdot}(\mathbf X)\|_2^2
\ll D^\epsilon H X_{\max}\!\prod_{i\ne j}X_i^{2b}
=D^\epsilon H P Q^{2b-1},}
\tag{3.1}
\]
where \(j\) is any index attaining \(X_{\max}\).

**Proof.** At every smaller nonempty rectangle \(\mathbf Y\), retain the same fixed axis \(j\), even if it is no longer the largest after shifting scales. Use its second moment and the other factors' pointwise bounds:
\[
\|P_\cdot(\mathbf Y)\|_2
\ll D^{\epsilon_0}\sqrt H\,Y_j^{1/2}\prod_{i\ne j}Y_i^b.
\tag{3.2}
\]
The tests are unchanged; only their scale arguments shift. Thus no uncontrolled seminorm of a new test is introduced.

Apply Minkowski to (2.3). Multiplication by \(\eta_u(d_1\cdots d_k)\) is a contraction in the full row norm. Inserting (3.2) leaves precisely \(\|e_C\|_{\boldsymbol\alpha}\), for \(\alpha_j=1/2\) and \(\alpha_i=b\) otherwise. Use (2.5) with \(\eta\) small enough that \(D^{C_0\eta}\), the preliminary losses, and their squares fit inside the requested \(D^\epsilon\). This proves (3.1), with no constant depending on the moving \(C\) or row. \(\square\)

At \(b=1\), (3.1) reads \(D^\epsilon HPQ\) and depends only on the native second moment. A direct verification is to freeze the other \(k-1\) singleton factors, retain their primes together with \(C\) as the exact inner exclusion, apply the uniform excluded second moment, and use Minkowski over their \(O(\prod_{i\ne j}X_i)\) tuples.

## 4. A strictly additional part of the general moment

Use the exact shared-prime incidence representation of PR 913:
\[
X_i=D\Big/\prod_{I\ni i,\ |I|\ge2}Nc_I,\qquad
A_u(D)^k=\sum_{\mathbf c}z_{\mathbf c}(u)B_{C,u}(\mathbf X),
\quad |z_{\mathbf c}(u)|\le1.
\]
For \(Q_0\ge1\), let \(F_{\mathrm{per},Q_0}\) be precisely the portion with
\(\prod_iX_i/\max_iX_i\le Q_0\). Then
\[
\boxed{
\|F_{\mathrm{per},Q_0}\|_2^2
\ll D^\epsilon H D^k Q_0^{2b-1}.}
\tag{4.1}
\]
Indeed, take square roots in (3.1), use \(Q^{b-1/2}\le Q_0^{b-1/2}\), and sum by Minkowski. The remaining normalized overlap sum is exactly
\[
\sum_{\mathbf c}\prod_{|I|\ge2}(Nc_I)^{-|I|/2}
\ll_k(\log(2D))^{\binom{k}{2}},
\]
since pair incidences are harmonic and higher incidences converge. Squaring and absorbing this fixed logarithmic power proves (4.1).

In particular, if \(Q_0=R(D)\) is subpower, meaning \(R(D)\le D^\eta\) eventually for every \(\eta>0\), then this entire portion has the desired diagonal scale \(D^{k+\epsilon}H\). This conclusion already holds with \(b=1\), hence without an additional zero-free premise beyond the imported second-moment theorem.

The range is not contained in the two previously controlled ranges. At \(k=3\), take \(c_{\{2,3\}}\asymp D\) and every other shared incidence ideal equal to one, with the annulus chosen inside the fixed support of \(W\). Then \(\mathbf X\asymp(D,1,1)\), \(P\asymp D\), and \(Q\asymp1\), while the common gcd is one. For \(H=D^{1+\theta}\), \(0<\theta<1\), this lies outside \(P\le H^{1/2}\) and outside every growing common-gcd tail. The whole collection of these configurations is controlled by (4.1), including its interference.

For \(k=2\), the equal-length common-gcd reduction has \(X_1=X_2=X\), so \(Q=X\). Its new diagonal portion has \(X=D^{o(1)}\), already covered by the refined sieve. Thus this theorem enlarges the known general-\(k\) incidence range but does not solve or enlarge the balanced fourth-moment range. Long configurations with at least two genuinely large singleton axes remain the unresolved target.
