# Joint cubic pair ideals and a stronger higher-moment incidence frontier

Status: proposed component theorems for the actual finite-order Möbius/sextic family. The counting version uses only classical cubic large sieves and elementary ideal counting. Improved versions separately assume the stated uniform pointwise bound; the hybrid versions additionally assume the inherited native second moment. No complete fourth moment, complete sixth moment, cofinal diagonal hierarchy, or new zero-free boundary is proved.

Scope: every fixed moment order over the Eisenstein field; every nonzero element row, including units, cube and sixth-power copies, repeated good primes and all fixed bad-prime powers; exact moving column exclusions; complete one-sided incidence portions and complete signed Hermitian incidence blocks. Hard dyadic cutoffs on the positive cubic pair variables are permitted. No unsupported hard truncation of a native inverse test is used.

Exact sources:

- PR #921, commit 4e6d4aa57ae4cb04d76b2b31279ac367951b469a, standalone/2026-10-10-sextic-centered-covariance/HERMITIAN_INCIDENCE.md, SHA-256 5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9: exact mixed-character forward correction, finite critical-weight regularization, and the native inputs with test seminorms.
- PR #923, commit 1a1152008706f7e24fa1efe4990588f8f99c5d8d, standalone/2026-10-10-sextic-separated-cores/SUBSET_PRODUCT_INCIDENCE.md, Git blob f3e4eb59a3f8ffb1c742de5a627704f169d7cc00: the previous proper-subset selector and its sixth-moment triangle example. That theorem freezes the shared ideals before applying its subset estimate.
- PR #917, commit 6b4723042b3d250024eef45cb1924f88f28e902c, standalone/2026-10-10-oscillating-overlaps-and-averaged-moments/OSCILLATING_OVERLAPS.md, Git blob aa3137869abcee4b380bb0b621e56e93e2072d71: Theorem 2.1, the all-row cubic sieve, and Theorem 4.1, which retains one designated overlap ideal. The present work retains the joint product of all pair ideals, and its proof below identifies the extra correction required to combine that operation with singleton Möbius cancellation.
- PR #913, commit 6498d6cc2eded03159c7332b25fd224ad07f89c1, standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md, SHA-256 6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8: the general incidence coefficient-mass argument and its classical inputs.
- Blomer, Goldmakher and Louvel, *L-functions with n-th order twists*, arXiv:1112.1650v1, Theorem 1.3, used only at order three. The primary theorem was read at https://arxiv.org/html/1112.1650v1; it is a squarefree-row and squarefree-column theorem. The extension to every row is explicitly retained below.

Smallest remaining gap: the pair product is one in the completely coprime balanced core. There the new selector reduces to the old native second-moment/pointwise estimate. The new mechanism does not give cancellation in that core or in the strict long-scale signed covariance.

## 1. Family and separate analytic inputs

Fix an integer \(k\ge2\), \(D\ge2\), a finite-order Hecke datum \(\nu\), and a finite excluded-prime set \(S\) containing the good-prime normalization exceptions and the ramification of \(\nu\). Use the source's primary generators outside \(S\). Let \(W_i\) be fixed smooth functions supported in compact intervals \([a_i,b_i]\subset(0,\infty)\). Put

\[
A_{i,u}(Y;V)
=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)V(Nn/Y),
\qquad
\chi_n(u)=\left(\frac un\right)_6.
\tag{1.1}
\]

The characters always have their literal zero at a nonunit. At a good prime, \(\chi_p(u)^0\) in an incidence expression means the principal zero extension \(\mathbf1_{p\nmid u}\), not the number one. When multiplicative character values are evaluated on nonsquarefree correction ideals, they are extended prime by prime, with this same zero convention.

Let \(1\le H\le D^{A_0}\), with \(A_0\) fixed. All column and exclusion labels below are bounded by fixed powers of \(D\). Constants may depend on fixed \(k,A_0,S,\nu\), the test supports and seminorms, and each prescribed positive loss. They do not depend arbitrarily on the moving labels.

The classical input, already established with all row classes in PR #917, is

\[
\sum_{0<Nu\le H}
\left|\sum_{\substack{n\ {\rm squarefree}\\(n,S)=1\\Nn\le L}}
z_n\chi_n(u)^2\right|^2
\ll_\epsilon (HL)^\epsilon
\left[H+H^{1/3}L+(HL)^{2/3}\right]\sum_n|z_n|^2.
\tag{C3}
\]

It holds for arbitrary fixed coefficients \(z_n\); the conjugate power four has the same bound. A row-independent moving column mask is part of \(z_n\).

For \(1/2<b\le1\), the optional pointwise premise is

\[
|A_{i,u}(Y;V)|
\ll_\epsilon D^\epsilon Y^b\|V\|_{C^{J_b}},
\qquad 0<Nu\le H,\quad c\le Y\le C_1D.
\tag{PW}
\]

The smooth family must have a uniform finite seminorm, and the constants must cover every smaller scale in the same physical row range. At \(b=1\), this is elementary ideal counting and does not add a nonclassical hypothesis. The example \(b=7/8\) below is source-conditional on the uniform reciprocal/zero-free premise explicitly identified in the pinned earlier papers. It is not obtained from (C3).

The hybrid improvement separately uses

\[
\sum_{0<Nu\le H}|A_{i,u}(Y;V)|^2
\ll_\epsilon D^\epsilon HY\|V\|_{C^J}^2
\tag{NM2}
\]

in its imported allowed height range, with the same finite-seminorm and smaller-scale quantifiers as PR #921. In particular, for \(H=D^h\), the fixed \(h>1\) must lie in that input's allowed range. It is not an arbitrary-coefficient large sieve.

For a fixed Schwartz row profile, all source-conditional inputs are required at every reference scale. Section 8 gives the annular passage. Every statement preceding that section concerns the literal sharp norm ball.

## 2. The cubic input includes every row

For completeness, the exact all-row mechanism in (C3) is short enough to reproduce.

Choose generators multiplicatively for all ideals, including those at \(S\). Every nonzero element has a unique representation

\[
u=\varepsilon v^3 a b^2,
\tag{2.1}
\]

where \(\varepsilon\) is one of six units, \(v\) is arbitrary, and \(a,b\) are coprime squarefree ideals. There is no restriction \((v,ab)=1\). The literal identity is

\[
\chi_n(u)^2
=\chi_n(\varepsilon)^2
\mathbf1_{(n,v)=1}
\chi_n(a)^2\chi_n(b)^4.
\tag{2.2}
\]

Split the finitely many squarefree bad-prime parts of \(a,b\), and absorb them and the unit into the fixed column coefficient. On a dyadic block let \(Nv\asymp V\), \(Na\asymp A\), \(Nb\asymp B\), put

\[
P=V^3AB^2\ll_S H,\quad F=VAB,\quad M=\max(A,B).
\]

Freeze \(v\) and the smaller of \(a,b\). There are \(O(F/M)\) frozen choices. The squarefree cubic large sieve on the remaining coordinate gives the block cost

\[
(HL)^\epsilon\left[
F+\frac{FL}{M}+\frac{FL^{2/3}}{M^{1/3}}
\right]\sum_n|z_n|^2.
\tag{2.3}
\]

The exact inequalities

\[
F\le P,\qquad
\frac{(F/M)^3}{P}=\frac{A^2B}{M^3}\le1,\qquad
\frac{(F/M^{1/3})^3}{P^2}
=\frac{A}{MV^3B}\le1
\]

give (C3) after summing a fixed power of logarithmically many blocks. The coefficient mask \(\mathbf1_{(n,v)=1}\) is never dropped. The only discarded coprimality restriction is between squarefree row labels in a positive outer square-sum. Fixed bad-prime powers are already included in arbitrary \(v\). This proves the stated all-row scope from the classical squarefree theorem.

### Lemma 2.1. The full physical product of cubic polynomials

For a fixed number \(s\ge1\), let

\[
U_{j,u}(Y_j)=
\sum_{(n,S)=1}
\mu_K(n)^2\lambda_j(n)\chi_n(u)^2V_j(Nn/Y_j),
\qquad
R=\prod_{j=1}^sY_j.
\tag{2.4}
\]

Here each \(\lambda_j\) is a fixed unit-modulus completely multiplicative datum on good ideals, and each \(V_j\) is a bounded test in a fixed compact subinterval of \((0,\infty)\). The tests may have hard interval endpoints; only their sup norms are used. Nonempty scales have a fixed positive lower bound and are polynomially bounded in \(D\). Then

\[
\boxed{
\left\|\prod_{j=1}^sU_{j,\cdot}(Y_j)\right\|_{2,H}^2
\ll_\epsilon D^\epsilon
\left[HR+H^{1/3}R^2+H^{2/3}R^{5/3}\right].
}
\tag{2.5}
\]

The dependence on the tests is through \(\prod_j\|V_j\|_\infty^2\).

**Proof.** Apply the unique incidence decomposition to the squarefree tuple in the physical product. For each repeated incidence \(I\), \(|I|\ge2\), freeze its squarefree ideal \(c_I\). Every exterior character multiplier, including one whose exponent is a multiple of three, has modulus at most one and retains its zero. The singleton scales become

\[
Z_j=Y_j\Big/\prod_{\substack{I\ni j\\|I|\ge2}}Nc_I,
\qquad
R(\mathbf c)=R\prod_{|I|\ge2}(Nc_I)^{-|I|}.
\]

The product of the disjoint singleton ideals is squarefree. Its coefficient is independent of the row, is bounded by a fixed-order ideal divisor function, and has squared mass \(O(D^\epsilon R(\mathbf c))\): count the supported factor tuples, then use the divisor bound for their maximum multiplicity at a fixed product. Their fixed moving exclusion remains part of that coefficient. Apply (C3) at column length \(O(R(\mathbf c))\).

Taking square roots gives three norm terms with powers \(R(\mathbf c)^{1/2},R(\mathbf c),R(\mathbf c)^{5/6}\). Minkowski over the frozen repeated labels costs harmonic logarithms at the pair incidences in the first term; every other such sum converges. In the second and third terms all repeated-ideal exponents exceed one. Thus the resulting bound is the same three norm terms with \(R(\mathbf c)\) replaced by \(R\), up to a small power of \(D\). Squaring proves (2.5). A nonempty scale below one lies in a fixed compact interval and changes only the support-dependent constant. This proof includes every collision in the physical product. \(\square\)

For every fixed integer \(q\ge1\), applying the lemma to \(q\) literal copies of each factor gives

\[
\boxed{
\left\|\prod_jU_{j,\cdot}(Y_j)\right\|_{2q,H}^{2q}
\ll_\epsilon D^\epsilon
\left[HR^q+H^{1/3}R^{2q}+H^{2/3}R^{5q/3}\right].
}
\tag{2.6}
\]

This is a classical estimate for positive squarefree cubic coefficients. It is not an assumed higher native Möbius moment. The constant may depend on the fixed integer \(q\).

## 3. A forward correction for mixed squarefree signs

The singleton coefficients are \(\mu_K\); the pair coefficients are \(\mu_K^2\). Their coprimality correction must therefore be written with both signs.

For each of a fixed number of axes \(j\), let \(s_j\in\{-1,+1\}\). Let the individual coefficient at a good prime be \(s_j\eta_{j,u}(p)\), where \(\eta_{j,u}\) is completely multiplicative with literal row zeros. The independent one-axis Euler factor is \(1+s_jz_j\). Pairwise coprimality permits at most one axis at that prime, so its desired factor is \(1+\sum_js_jz_j\).

For a moving excluded ideal \(C\), the exact forward correction is

\[
E_{C,p}(\mathbf z)=
\begin{cases}
\displaystyle\frac{1+\sum_js_jz_j}{\prod_j(1+s_jz_j)},
&p\nmid CS,\\[6pt]
\displaystyle\prod_j(1+s_jz_j)^{-1},&p\mid C,\ p\notin S,\\
1,&p\in S.
\end{cases}
\tag{3.1}
\]

Let \(e_{C,\mathbf s}(\mathbf d)\) be its multiplicative coefficient, with the row characters factored out. For a good nonmask prime, the coefficient of a nonconstant exponent vector \(\mathbf e\) is

\[
(1-|\operatorname{supp}\mathbf e|)
\prod_j(-s_j)^{e_j}.
\tag{3.2}
\]

At a mask prime it is just \(\prod_j(-s_j)^{e_j}\). Thus its absolute coefficient is exactly the same as in the all-Möbius forward correction. In particular, one-axis terms vanish outside the mask.

For fixed weights \(\alpha_j\ge1/2\), every finite supported horizon \(Nd_j\ll D^{C_j}\) satisfies

\[
\boxed{
\sum_{\rm supported\ \mathbf d}
|e_{C,\mathbf s}(\mathbf d)|
\prod_j(Nd_j)^{-\alpha_j}
\ll_\epsilon D^\epsilon,
\qquad NC\le D^{C_0}.
}
\tag{3.3}
\]

Indeed, increase all weights by a fixed \(\delta>0\). The horizon costs only \(D^{\delta\sum C_j}\). Outside the mask, every nonconstant monomial uses at least two axes, so the resulting absolute Euler factor is \(1+O((Np)^{-1-2\delta})\). At mask primes, its cost is a finite product of factors \((1-(Np)^{-\alpha_j-\delta})^{-1}\), bounded by \((NC)^\eta\) for each fixed \(\eta>0\). Choose \(\delta,\eta\) sufficiently small. This is finite-horizon regularization, not absolute convergence asserted at \(1/2\).

The coefficient identity therefore writes the exact pairwise-coprime mixed polynomial as

\[
B_{C,u}(\mathbf Y)
=\sum_{\mathbf d}e_{C,\mathbf s}(\mathbf d)
\prod_j\eta_{j,u}(d_j)
\prod_jF_{j,u}(Y_j/Nd_j),
\tag{3.4}
\]

where \(F_j\) is the physical one-axis polynomial with prime sign \(s_j\). It is finite on the test support. At a row prime, every nonconstant affected monomial on both sides vanishes. A pair of zero factors is never replaced by a principal value one.

The correction (3.4), followed by (3.3), will be applied only after legitimate norms of the entire physical product have been established. It does not assert that deleting arithmetic columns is a contraction of a native moment.

## 4. Retain all pair ideals at once

In the ordinary \(k\)-fold product \(\prod_{i=1}^kA_{i,u}(D;W_i)\), write the unique incidence ideals \(q_I\), \(\varnothing\ne I\subseteq[k]\), so that

\[
n_i=\prod_{I\ni i}q_I.
\tag{4.1}
\]

All \(q_I\) are squarefree, pairwise coprime, and outside \(S\).

Freeze only the higher incidence ideals \(c_I=q_I\), \(|I|\ge3\). Put

\[
C=\prod_{|I|\ge3}c_I,\qquad
M_i=\prod_{\substack{I\ni i\\|I|\ge3}}c_I,\qquad
T=\prod_{|I|\ge3}(Nc_I)^{|I|}.
\tag{4.2}
\]

For each pair \(i<j\), choose a hard dyad
\(R_{ij}\le Nq_{\{i,j\}}<2R_{ij}\), with \(R_{ij}\) a power of two at least one. Define

\[
R=\prod_{i<j}R_{ij},\qquad
X_i=\frac{D}{NM_i\prod_{j\ne i}R_{\min(i,j),\max(i,j)}},
\qquad X=\prod_iX_i.
\tag{4.3}
\]

These scales satisfy the exact identity

\[
\boxed{R^2XT=D^k.}
\tag{4.4}
\]

Let \(F_{\mathbf c,\mathbf R}(u)\) be the complete portion with exactly those higher incidence ideals and pair dyads. No singleton terms are selected or discarded inside it. The varying singleton ideals have coefficients
\(\mu_K(a_i)\nu(a_i)\chi_{a_i}(u)\). The varying pair ideals have coefficients

\[
\mu_K(q_{ij})^2\nu(q_{ij})^2\chi_{q_{ij}}(u)^2.
\tag{4.5}
\]

The latter are cubic polynomials of the precise class in Lemma 2.1. The higher-incidence row multiplier has modulus at most one, retaining every zero.

### Coupled weights and hard pair endpoints

Write \(x_{ij}=Nq_{ij}/R_{ij}\in[1,2)\). The original test at position \(i\) is

\[
W_i\!\left((Na_i/X_i)\prod_{j\ne i}x_{ij}\right).
\tag{4.6}
\]

On its support, \(Na_i/X_i\) lies in the fixed interval
\([a_i2^{-(k-1)},b_i]\). Insert a fixed smooth cutoff \(\Psi_i\) equal to one on this interval and supported in a slightly larger compact interval. Mellin inversion of every \(W_i\) on real part zero separates the axes. The singleton test is
\(\Psi_i(x)x^{-it_i}\), with a finite \(C^J\) norm bounded by a fixed polynomial in \(\sum_i|t_i|\). The pair test is

\[
\mathbf1_{[1,2)}(x)x^{-i(t_i+t_j)}.
\tag{4.7}
\]

Its sup norm is one; no derivative is needed by Lemma 2.1. Rapid decay of the Mellin transforms integrates every fixed polynomial frequency cost. Therefore hard pair intervals are legitimate, while the inverse Möbius tests remain smooth and uniformly controlled.

### Theorem 4.1. Joint cubic-pair estimate

Put \(a=2b-1\) and

\[
\rho_q(H,R)=
R^{-q}+H^{-2/3}+H^{-1/3}R^{-q/3},
\qquad q\ge1.
\tag{4.8}
\]

Assuming only (C3) and (PW),

\[
\boxed{
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll_\epsilon
H D^{k+\epsilon}T^{-1}\,
X^a\rho_1(H,R).
}
\tag{4.9}
\]

At \(b=1\), (4.9) is a classical theorem without the imported canonical or zero-free theorem.

If (NM2) is also supplied, then for each fixed integer \(q\ge2\) and every singleton axis \(i\),

\[
\boxed{
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll_\epsilon
H D^{k+\epsilon}T^{-1}
X^aX_i^{-a(1-1/q)}
\rho_q(H,R)^{1/q}.
}
\tag{4.10}
\]

The old native option
\[
\|F_{\mathbf c,\mathbf R}\|_{2,H}^2
\ll_\epsilon
H D^{k+\epsilon}T^{-1}(X/X_{\max})^a
\tag{4.11}
\]
also follows from the same correction with all pair factors bounded by counting. For (4.10), the best axis is \(X_i=X_{\max}\).

**Proof.** After the Mellin separation, apply (3.4) to all singleton and pair variables together. Use \(s=-1\) on singleton axes, \(s=+1\) on pair axes, and the exact moving exclusion \(C\). For each realized correction vector the shortened singleton scales are \(Y_i=X_i/Nd_i\) and the shortened pair product is \(R'=R/\prod_{i<j}Nd_{ij}\).

For (4.9), bound all singleton factors by (PW). Apply Lemma 2.1 to the entire product of physical pair polynomials. Its resulting norm bound is

\[
D^\epsilon
\left[
H^{1/2}(R')^{1/2}
+H^{1/6}R'
+H^{1/3}(R')^{5/6}
\right]\prod_iY_i^b.
\tag{4.12}
\]

For every term, the correction weights on pair variables are respectively \(1/2,1,5/6\), and those on singleton variables are \(b\). All are at least \(1/2\), so (3.3) and the norm triangle inequality sum the correction at cost \(D^\epsilon\). Square, integrate the separated tests with their finite seminorms, and use (4.4). The result is

\[
D^\epsilon
\left[HR+H^{1/3}R^2+H^{2/3}R^{5/3}\right]X^{2b}
=H D^{k+\epsilon}T^{-1}X^a\rho_1(H,R).
\]

For (4.10), keep axis \(i\) in a row norm. Interpolating the native second moment with (PW) gives

\[
\|A_{i,\cdot}(Y_i)\|_{2q/(q-1),H}
\ll_\epsilon
D^\epsilon
H^{(q-1)/(2q)}
Y_i^{1/2+a/(2q)}.
\tag{4.13}
\]

Apply Hölder to this factor and the whole cubic-pair product in \(L^{2q}\); their reciprocal exponents add to \(1/2\). Use (2.6) for the latter and (PW) on all other singleton factors. Upon expanding the sum of its three norm terms, the pair-variable weights remain \(1/2,1,5/6\). The selected singleton weight is \(1/2+a/(2q)\), and the others have weight \(b\). Thus (3.3) again sums the exact mixed correction, uniformly at every shortened scale.

Before (4.4), the resulting energy is

\[
D^\epsilon H R
\left[
1+\frac{R^q}{H^{2/3}}
+\left(\frac{R^{2q}}H\right)^{1/3}
\right]^{1/q}
X_i^{1+a/q}\prod_{j\ne i}X_j^{2b}.
\tag{4.14}
\]

Since
\[
R^{-1}
\left[1+\frac{R^q}{H^{2/3}}
+\left(\frac{R^{2q}}H\right)^{1/3}\right]^{1/q}
=\rho_q(H,R)^{1/q},
\]
normalization gives (4.10). The same argument with pair factors counted and one native \(L^2\) factor gives (4.11). All arithmetic restrictions were present in the coefficient identity before norms were taken. \(\square\)

## 5. Two strict sixth-moment improvements

Take \(k=3\), the triple ideal \(c_{123}=1\), and the three pair ideals in dyads of size \(D^r\). If needed use the neighboring dyadic scales; they change only fixed constants. The singleton scales satisfy

\[
X_1\asymp X_2\asymp X_3\asymp D^x,
\quad x=1-2r,\quad R\asymp D^{3r},\quad X\asymp D^{3x}.
\tag{5.1}
\]

This is the actual one-sided triangle portion of \(A_u(D)^3\). Its norm includes every overlap between its two Hermitian copies. Its full one-sided common gcd is exactly one.

### 5.1 A larger diagonal-size triangle range using only classical inputs

Take \(b=1\), \(H=D^h\), \(1<h\le11/10\). From (4.9), the excess exponent is

\[
\lambda_{\rm cub}(r)
=3(1-2r)-
\min\left\{3r,\frac{2h}{3},r+\frac h3\right\}.
\tag{5.2}
\]

For
\[
r\ge\frac12-\frac h9,
\tag{5.3}
\]
all three error terms are at most the diagonal scale. One direct check is that the threshold in (5.3) lies above \(h/3\), because \(h\le11/10<9/8\). In that range the minimum in (5.2) is \(2h/3\), and (5.3) is exactly \(3(1-2r)\le2h/3\). The remaining terms decrease with \(r\).

Consequently the sum of all such triangle dyads satisfies

\[
\boxed{
\|F_{\triangle,\ r\ge1/2-h/9}\|_{2,H}^2
\ll_\epsilon H D^{3+\epsilon}.
}
\tag{5.4}
\]

The number of dyads is logarithmic. The statement also permits any complete collection of triangle dyads satisfying the equivalent cost bound in (4.9).

The earlier estimate that freezes the three pair ideals reaches diagonal size only when \(X_1X_2X_3\le H^{1/2}\), namely \(r\ge1/2-h/12\). Thus the new range extends downward by \(h/36\) in the pair-ideal exponent. At \(h=21/20\), its cutoff is

\[
\boxed{\frac{23}{60}\quad\text{instead of}\quad\frac{33}{80};}
\tag{5.5}
\]

their difference is \(7/240\). This comparison concerns proved bounds for the same complete one-sided triangle portion.

### 5.2 Improve the explicit triangle from PR #923

Now use precisely that source's parameters

\[
h=\frac{21}{20},\qquad
b=\frac78,\qquad
a=\frac34,\qquad
r=\frac5{24},\qquad x=\frac7{12}.
\tag{5.6}
\]

The earlier native and whole-singleton-classical methods both have excess \(7/8\). PR #923's proper-singleton-subset estimate lowers it to \(623/720\).

Here \(R\asymp D^{5/8}\), \(X\asymp D^{7/4}\), and
\[
\min\left\{\frac58,\frac7{10},\frac{5/8+21/20}{3}\right\}
=\frac{67}{120}.
\]
The new classical cubic pool combined with (PW), without using (NM2), gives

\[
\lambda_{q=1}
=\frac34\frac74-\frac{67}{120}
=\frac{181}{240}.
\tag{5.7}
\]

This already improves \(623/720\) by exactly \(1/9\).

With the additional source-pinned (NM2), choose the fixed integer \(q=2\). Then \(R^2\asymp D^{5/4}>H\), so the dominant term of \(\rho_2(H,R)\) is \(H^{-2/3}\). Formula (4.10) gives

\[
\begin{aligned}
\lambda_{q=2}
&=\frac34\frac74
-\frac12\frac34\frac7{12}
-\frac h3\\
&=\frac{21}{16}-\frac7{32}-\frac7{20}
=\boxed{\frac{119}{160}}.
\end{aligned}
\tag{5.8}
\]

Thus for the literal sixth-moment triangle polynomial,

\[
\boxed{
\|F_\triangle\|_{2,H}^2
\ll_\epsilon H D^{3+119/160+\epsilon}.
}
\tag{5.9}
\]

The saving over the published \(623/720\) is
\[
\boxed{\frac{623}{720}-\frac{119}{160}=\frac{35}{288}.}
\tag{5.10}
\]

This is not diagonal size and is not a bound for the full sixth moment. It is a strict improvement for the exact portion used in the source comparison, under the same optional pointwise and native inputs. Fixed smooth pair-block tests can be inserted without changing any exponent; hard dyads are already valid by Section 4.

### 5.3 The pointwise improvement enlarges the diagonal triangle range further

For \(b=7/8\), the \(q=1\) bound alone is diagonal when

\[
r\ge
\begin{cases}
\displaystyle\frac12-\frac{4h}{27},&1<h\le27/26,\\[5pt]
\displaystyle\frac{27-4h}{66},&27/26\le h\le11/10.
\end{cases}
\tag{5.11}
\]

The first interval is the \(R\ge H\) branch of the cubic pool cost; the second is its \(H^{1/2}\le R\le H\) branch. Substitution into (5.2) with the leading \(3\) replaced by \(3a=9/4\) verifies both, including the common endpoint. At \(h=21/20\), the cutoff becomes \(r\ge19/55\). This corollary needs (PW) at \(7/8\), but it does not need (NM2).

## 6. A complete general-order periphery

Choose once and for all a finite integer \(q_*\ge1\). If (NM2) is supplied, define

\[
\mathfrak C_{H,b,q_*}(R,\mathbf X)
=\min\left\{
(X/X_{\max})^a,\
\min_{1\le q\le q_*}
X^aX_{\max}^{-a(1-1/q)}\rho_q(H,R)^{1/q}
\right\}.
\tag{6.1}
\]

At \(q=1\) the \(X_{\max}\) factor is one. Without (NM2), keep only this \(q=1\) entry. The integer \(q_*\) is fixed independently of \(D,H\). No infimum over moments with uncontrolled order constants is used.

For \(L>0\), let \(G_L\) be the exact polynomial portion obtained by selecting complete pairs \((\mathbf c,\mathbf R)\) of higher-ideal configurations and pair dyads for which
\[
\mathfrak C_{H,b,q_*}(R,\mathbf X)\le L.
\tag{6.2}
\]

### Theorem 6.1

With precisely the inputs used in the selected version of (6.1),

\[
\boxed{\|G_L\|_{2,H}^2
\ll_\epsilon H D^{k+\epsilon}L.}
\tag{6.3}
\]

The implied constant is uniform in the threshold \(L\).

**Proof.** Apply Theorem 4.1 to each complete selected portion and take square roots. The sum over the pair dyads has at most a fixed power of \(\log D\) terms. The higher incidence ideals contribute

\[
\sum_{\mathbf c}T^{-1/2}
\le
\prod_{m=3}^k
\zeta_K(m/2)^{\binom{k}{m}}
<\infty.
\tag{6.4}
\]

Restrictions on those ideals are dropped only in this nonnegative norm majorant. Thus Minkowski yields
\(\|G_L\|_{2,H}\ll D^\epsilon\sqrt{HD^kL}\). Squaring and reallocating losses gives (6.3). The selector depends only on the fixed higher ideals, pair dyads and resulting scale vector; it never cuts an individual singleton sum. \(\square\)

One useful classical consequence applies throughout every fixed order: when \(R\ge H\), (4.8) gives \(\rho_1(H,R)\ll H^{-2/3}\). Hence all complete configurations with

\[
R\ge H,\qquad X\le H^{\,2/(3a)}
\tag{6.5}
\]

have diagonal-size total energy. At counting \(a=1\), this allows \(X\le H^{2/3}\); the previously frozen-pair classical criterion allowed only \(X\le H^{1/2}\). At optional \(b=7/8\), it allows \(X\le H^{8/9}\). The product relation (4.4) and the individual factor supports must still hold; the theorem does not assert that every such numerical vector is realized by a tuple.

## 7. A Hermitian version retaining two native odd axes

The mixed correction also applies to the full \(2k\)-position Hermitian incidence expansion. This section records the extra frontier without identifying it with a positive one-sided norm.

For every nonempty incidence \(I\), let
\[
m_I=|I|,\qquad
e_I=\#(I\text{ on the left})-\#(I\text{ on the right}).
\]
On a complete smooth block write \(Nq_I\asymp Q_I\). Then
\(\prod_IQ_I^{m_I}\asymp D^{2k}\). Put \(\mathcal O=\{I:m_I\text{ odd}\}\) and \(\mathcal E=\{I:m_I\text{ even}\}\). Retain (PW) for the fixed finite set of odd row powers, as in PR #921, and (NM2) only when \(e_I\equiv\pm1\pmod6\).

Choose two eligible odd incidences \(J,L\). Choose a nonempty group \(\mathcal P\subseteq\mathcal E\) all of whose exponents are \(2\bmod6\), or all \(4\bmod6\). Set
\[
R=\prod_{I\in\mathcal P}Q_I.
\]
All other even variables will be bounded by counting.

### Proposition 7.1

For each fixed integer \(q\ge1\), the complete signed Hermitian block satisfies

\[
\boxed{
\begin{aligned}
|S_{\mathbf Q}|
&\ll_\epsilon D^\epsilon H\,
Q_J^{1/2}\,
Q_L^{1/2+a/(2q)}\,
R^{1/2}\\
&\quad\times
\left[1+\frac{R^q}{H^{2/3}}
+\left(\frac{R^{2q}}H\right)^{1/3}\right]^{1/(2q)}
\prod_{\substack{I\in\mathcal O\\I\ne J,L}}Q_I^b
\prod_{I\in\mathcal E\setminus\mathcal P}Q_I.
\end{aligned}
}
\tag{7.1}
\]

At \(q=1\), axis \(L\) is merely pointwise and the bound uses one native axis plus the cubic group. At each \(q\ge2\), both native axes contribute cancellation, with the second partially interpolated. This requires no new native moment.

**Proof.** Perform the same Mellin separation of the coupled original tests and the smooth incidence partition as in PR #921. The exact coefficient on an odd axis has prime sign \(-1\); on an even axis it has prime sign \(+1\). Apply (3.4) to all the varying axes. The fixed finite-order twist on an axis is \(\nu^{e_I}\), and the row character retains its nonunit zero.

Use the full \(L^2\) native norm on \(J\), the interpolated \(L^{2q/(q-1)}\) native norm on \(L\), and the \(L^{2q}\) norm of the physical cubic group. Their reciprocal exponents add to
\[
\frac12+\frac{q-1}{2q}+\frac1{2q}=1.
\]
Use (PW) on other odd axes and counting on remaining even axes. Lemma 2.1 also permits different finite coefficient twists among the cubic factors, because after grouping the squarefree singleton product its coefficient is arbitrary and independent of the row. Their common residue exponent is essential: powers two and four are not silently mixed into one cubic column.

The correction weights are \(1/2\) on \(J\), \(1/2+a/(2q)\) on \(L\), \(1/2,1,5/6\) on each cubic axis in its three norm terms, \(b\) on other odd axes, and one on the other even axes. All satisfy (3.3). Sum the correction and the integrable Mellin frequencies. This proves (7.1) with every local zero intact. \(\square\)

Relative to the old two-native-axis block bound, the factor in (7.1) is exactly

\[
\boxed{
\left[Q_L^a\,\rho_q(H,R)\right]^{1/(2q)}.
}
\tag{7.2}
\]

Thus the cubic pool gives a strict improvement whenever \(Q_L^a\rho_q(H,R)<1\) by a fixed power. For a suitable finite \(q\), this may hold even if the \(q=1\) exchange is worse than keeping the two native axes. There is no third full native \(L^2\) saving for free; the formula explicitly accounts for the Hölder budget.

## 8. Row profiles, boundaries, and the remaining balanced core

### Schwartz rows

For a fixed Schwartz weight \(\Phi(Nu/H)\), split rows into annuli \(Nu\asymp2^jH\), with the initial ball \(Nu\le H\). The classical terms used above have positive row-height powers at most one before their appropriate norm roots. In the squared one-sided hybrid estimate, the three powers are
\[
1,\qquad 1-\frac{2}{3q},\qquad 1-\frac1{3q};
\]
in the Hermitian bound they are at most one as well. Thus replacing \(H\) by \(2^jH\) costs at most \(2^j\), apart from a preliminary subpower loss.

When native or pointwise inputs are used at \(H=D^h\), take reference \(D_j=D\,2^{j/h}\). Every original column scale and moving exclusion remains a permitted smaller polynomial scale at \(D_j\). The finite test seminorms are unchanged. Apply the source-uniform inputs there and (C3) to the same fixed column labels. Choosing a fixed Schwartz decay power larger than the resulting row-growth exponent makes the annular sum converge. The selectors and original arithmetic cutoffs remain those at the original \(D,H\); only a positive norm majorant is enlarged on each annulus. This proves the same upper bounds with the sharp row norm replaced by the fixed Schwartz-weighted norm.

### What is new and what remains open

The new ingredient is the joint cubic pair product and its exact mixed-sign correction. The all-row cubic sieve itself is inherited, and the optional pointwise/native premises are not re-proved here. The new component theorems retain all pair variables inside the cubic norm before summing higher overlaps. This creates an actual sixth-moment improvement and a strictly larger diagonal-size periphery at every fixed order.

In the completely coprime balanced core, \(R=1\), all higher ideals are one, and \(X_i=D\). Since \(\rho_q(H,1)\ge1\), each finite-\(q\) hybrid cost is at least
\[
D^{ak-a(1-1/q)}=D^{a(k-1)+a/q}.
\]
The old native option remains the minimum, with cost \(D^{a(k-1)}\). Thus the current inputs still give only
\[
M_{2k}(D,H)\ll H D^{1+2(k-1)b+\epsilon}
\]
when used without additional arithmetic control of that balanced region.

Theorem 6.1 permits an exact residual split \(A^k=G_L+R_L\). An upper bound for the signed scale-averaged Hermitian residual after the conductor reductions can be combined with it using the pinned PR #919 extraction, but that arithmetic average is unproved here. The new selector must be inserted as a whole one-sided portion; one cannot infer an absolute bound for an arbitrary subset of a signed block.

No claim in this note identifies these bounds with the missing original long-dual-scale covariance estimate, and no finite choice of the classical cubic moment parameter \(q\) closes the all-singleton region.
