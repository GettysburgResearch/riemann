# A further controlled sector: cross-side factors with small multiplicative separation

Status: proposed source-conditional signed-sector theorems, with complete proofs below. This removes an additional family from the fourth-moment small-gcd, large-conductor remainder. It uses the imported native inverse second moment through a precisely stated moving-exclusion adapter. The optional uniform pointwise exponent \(b>1/2\) further improves a cross-gcd tail to \(HD^{2+\epsilon}R^{2b-1}\). These results do not improve the classical one-sided large-gcd cutoff, prove the remaining arithmetic average, or attain a new zero-free half-plane.

Scope: the actual zero-extended Möbius/sextic family over \(K=\mathbb Q(\sqrt{-3})\), all nonzero element rows, fixed finite-order \(\nu\), fixed bad primes \(S\), fixed smooth factor and row tests. No sixth-power or other exceptional row is omitted.

Exact dependencies:

- PR #913 at 6498d6cc2eded03159c7332b25fd224ad07f89c1, FOURTH_MOMENT_ATTACK.md, Proposition 2.1: the uniform moving-exclusion second moment at every smaller column scale. Its SHA-256 is 354e8f7f5f81d0f8821ea6e821f55546f9c9641ac0690def1ae373000b4b3d08. This retains the imported canonical theorem and Poisson reduction.
- PR #914 at 0cc0428fedbbfc340044c7451b3d392c1da9a103, CONDUCTOR_SECTORS.md, Theorem 8.1 and Corollary 7.2: positive absolute accounting for the controlled full-tuple sectors. SHA-256 c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983.
- PR #919 at 9b04a887e171b3104a66cf57296ce5b0b2920d78, SMALL_GCD_CONDUCTOR_REDUCTION.md: the signed reduction with \(C=D^{(6-h)/7}\). SHA-256 9a371bd84f63b7fae2a3983c05829f2d69e2bbed918ab3eed119a2e7a11125a2.
- Its scale-averaged extraction is the separately audited PR #917 theorem at 6b4723042b3d250024eef45cb1924f88f28e902c, SCALE_AVERAGED_CRITERION.md, SHA-256 c6c543037312480fae6154f7a059248fe14658ecff6251aaecb80fe0fdbfd9c0.

No new computation or proof-assistant verification is claimed. No published source is modified.

## 1. Data and the exact analytic premise

Fix \(h>1\), \(H=D^h\), \(D\ge2\), and
\(W\in C_c^\infty((0,\infty))\) supported in \([\alpha,\beta]\).
Write
\[
a_n=\mu_K(n)\nu(n)W(Nn/D),\qquad
A_u(D)=\sum_{(n,S)=1}a_n\chi_n(u),
\quad \chi_n(u)=(u/n)_6.
\tag{1.1}
\]
Every symbol has its original zero at a nonunit residue. Ideal indices use the fixed primary-generator convention. The coefficients vanish unless \(n\) is squarefree.

The exact native premise used here is, for any fixed \(c_0>0\), polynomial exclusion bound, and fixed constant \(c_\Phi\ge1\),
\[
\sum_{0<Nu\le c_\Phi H}
\left|
 \sum_{(a,qS)=1}\mu_K(a)\nu(a)\chi_a(u)W(Na/X)
\right|^2
\ll_\epsilon D^\epsilon H X
\tag{1.2}
\]
uniformly for \(1/\beta\le X\le D\) and \(Nq\ll D^{c_0}\). Bounded scales below one are included. Constants may depend on the fixed data and \(c_\Phi\), but not the moving \(q,X,D\).

This is the smaller-scale moving-exclusion adapter in the first source. Its proof retains the same physical row range when the column shortens. Replacing \(H\) by a fixed larger multiple changes the initial ratio \(X/H\) only by a fixed constant and is allowed by that proof. It is equally possible to take (1.2), with precisely these quantifiers, as the explicit conditional input to this note.

Fix a nonnegative compact smooth radial \(\Phi\) on \(\mathbb C\), at least one on the unit disk. Its support is contained in the disk \(|z|\le\sqrt{c_\Phi}\). Write
\[
\|F\|_{\Phi,H}^2
=\sum_{u\in\mathcal O_K}\Phi(u/\sqrt H)|F(u)|^2.
\]
For all sufficiently large \(D\), no unit ideal lies in the factor support, so the \(u=0\) row of every original polynomial here vanishes. The remaining bounded interval of \(D\) can be absorbed in constants. Thus (1.2) bounds these smooth norms by positivity and the fixed upper bound for \(\Phi\).

## 2. A threshold on a gcd is compatible with the native second moment

For a good squarefree ideal \(n\) of norm at most \(\beta D\), and any real \(C\ge1\), define
\[
B_{n,C}(u)
=\sum_{\substack{(m,S)=1\\N\gcd(m,n)<C}}
a_m\chi_m(u).
\tag{2.1}
\]

### Lemma 2.1

For every \(\epsilon>0\),
\[
\boxed{\|B_{n,C}\|_{\Phi,H}^2
\ll_\epsilon D^\epsilon HD,}
\tag{2.2}
\]
uniformly in both \(n\) and \(C\).

**Proof.** Each original \(m\) is squarefree. Its exact common divisor with \(n\) is some \(d\mid n\), and then \(m=da\) with \((a,n)=1\). Therefore
\[
B_{n,C}(u)
=\sum_{\substack{d\mid n\\Nd<C}}
 \mu_K(d)\nu(d)\chi_d(u)
 \sum_{(a,nS)=1}
 \mu_K(a)\nu(a)\chi_a(u)
 W\!\left(\frac{Na}{D/Nd}\right).
\tag{2.3}
\]
This identity retains all zero extensions. In particular, multiplying by \(\chi_d(u)\) is a contraction and never divides by a zero character.

Every nonempty scale \(X=D/Nd\) lies in \([1/\beta,D]\). Apply (1.2) with the exclusion \(q=n\), then Minkowski, to obtain
\[
\|B_{n,C}\|_{\Phi,H}
\ll D^{\epsilon_0}\sqrt{HD}
 \sum_{d\mid n}(Nd)^{-1/2}.
\]
The divisor sum equals \(\prod_{p\mid n}(1+(Np)^{-1/2})\), which is
\(\ll_\eta(Nn)^\eta\) for every \(\eta>0\). Since \(Nn\ll D\), choose \(\eta,\epsilon_0\) small enough, then square. The cutoff only omits terms from this positive norm majorant, so the constant is independent of \(C\). \(\square\)

This lemma concerns a gcd threshold in an actual one-variable Möbius polynomial. It does not assert a second-moment estimate for arbitrary divisor-weighted coefficients.

## 3. One cross-side pair can vary through a subpower family

For two ideals \(n,m\), set
\[
\Delta(n,m)=
\max\!\left\{
N\!\left(\frac{n}{\gcd(n,m)}\right),
N\!\left(\frac{m}{\gcd(n,m)}\right)
\right\}.
\tag{3.1}
\]
Thus \(\Delta(n,m)=1\) exactly when \(n=m\). This quantity measures multiplicative separation, not additive distance or proximity of generators in the complex plane.

For \(R\ge1\), let \(\mathcal P_{11}(D,H;C,R)\) be the complete smooth signed covariance of the small-gcd polynomial, restricted by
\(\Delta(n_1,m_1)\le R\):
\[
\mathcal P_{11}
=\sum_{\substack{
N\gcd(n_1,n_2)<C,\ N\gcd(m_1,m_2)<C\\
\Delta(n_1,m_1)\le R}}
a_{n_1}a_{n_2}\overline{a_{m_1}a_{m_2}}\,
S^\Phi_{(n_1,n_2;m_1,m_2)}(H),
\tag{3.2}
\]
where \(S^\Phi\) is the literal complete row sum from #919. No conductor restriction has yet been imposed.

### Theorem 3.1

Uniformly in \(C,R\ge1\),
\[
\boxed{|\mathcal P_{11}(D,H;C,R)|
\ll_\epsilon D^\epsilon HD^2R.}
\tag{3.3}
\]

**Proof.** Freeze \(n=n_1\) and \(m=m_1\). The exact contribution of the two remaining factors is
\[
a_n\overline{a_m}
\sum_u\Phi(u/\sqrt H)\chi_n(u)\overline{\chi_m(u)}
B_{n,C}(u)\overline{B_{m,C}(u)}.
\tag{3.4}
\]
No coprimality between \(n\) and \(m\) is assumed or introduced. The row multiplier has modulus at most one. Cauchy–Schwarz and Lemma 2.1 bound the absolute value of (3.4) by
\(O_\epsilon(D^\epsilon HD)\), uniformly in the frozen pair.

There are \(O_\epsilon(D^{1+\epsilon}R)\) possible ordered pairs in the support with \(\Delta(n,m)\le R\). Indeed, for each \(n\), write
\(n=da\), \(m=db\), where \(d=\gcd(n,m)\), \(a\mid n\), \(Na\le R\), and \(Nb\le R\). For each divisor \(a\mid n\), there are \(O_K(R)\) possible \(b\). The extra coprimality, squarefreeness and support constraints can only reduce this count. Summing \(\tau_K(n)\ll_\epsilon D^\epsilon\) over the \(O(D)\) choices for \(n\) proves the assertion. Multiply the pair count by the bound for (3.4), reassigning positive losses. \(\square\)

For \(R=1\), the expression has the particularly transparent nonnegative form
\[
\mathcal P_{11}(C,1)
=\sum_n|a_n|^2
 \sum_u\Phi(u/\sqrt H){\bf1}_{(u,n)=1}|B_{n,C}(u)|^2.
\tag{3.5}
\]
The conclusion is not obtained by bounding each expanded off-diagonal term in absolute value. It preserves the native cancellation in the full remaining Möbius sum.

## 4. Impose the hard conductor conditions only after the estimate

Use #919's exact full-tuple definitions: \(g_1\) is the product of singleton primes, \(g_2\) the product of nonprincipal double primes, and
\(\mathcal E=Ng_1\sqrt{Ng_2}\). Let \(\mathcal U_C^\Phi\) be the small-gcd signed remainder with
\[
g_1\ne1,\qquad \mathcal E>H.
\tag{4.1}
\]
For a fixed cross position \((i,j)\in\{1,2\}^2\), let
\(\mathcal P_{ij}^{\rm hard}\) be (3.2) with these hard conditions added and with \(\Delta(n_i,m_j)\le R\).

The complement of (4.1) is precisely a subset of the two controlled accounting regions in #914. The estimates there bound sums of absolute contributions and remain valid under any additional tuple restriction. Therefore
\[
\mathcal P_{ij}^{\rm hard}
=\mathcal P_{ij}+O_\epsilon(HD^{2+\epsilon})
\]
and Theorem 3.1 implies
\[
\boxed{|\mathcal P_{ij}^{\rm hard}|
\ll_\epsilon D^\epsilon HD^2R.}
\tag{4.2}
\]
This order of operations matters. Applying a new conductor-dependent selector inside \(B_{n,C}\) would invalidate the preceding direct appeal to its native second moment. The proof instead bounds the complete covariance first and removes the already controlled complement afterward.

## 5. All four cross positions can be removed together

Let \(\mathcal N_{C,R}^\Phi\) be the signed part of \(\mathcal U_C^\Phi\) for which at least one of the four inequalities
\[
\Delta(n_i,m_j)\le R,\qquad i,j\in\{1,2\},
\tag{5.1}
\]
holds. This selector is invariant under interchanging the tuple sides, so \(\mathcal N_{C,R}^\Phi\) is real.

### Lemma 5.1

Any intersection of at least two distinct conditions in (5.1) contains
\[
O_\epsilon(D^{2+\epsilon}R^2)
\tag{5.2}
\]
supported four-tuples. Its total absolute smooth contribution is therefore
\(O_\epsilon(HD^{2+\epsilon}R^2)\).

**Proof.** For two disjoint edges in the bipartite four-vertex graph, the pair count from Theorem 3.1 gives (5.2) immediately. If the edges share a vertex, choose its ideal in \(O(D)\) ways. Each neighbor has at most \(O_\epsilon(D^\epsilon R)\) possibilities by the fixed-ideal divisor argument in that proof. The unused fourth ideal has \(O(D)\) possibilities. This again gives (5.2). Any further conditions only restrict a positive count. The tuple coefficients are bounded, and the complete smooth row sum has absolute value \(O_\Phi(H)\), including its zero conventions. \(\square\)

Finite inclusion–exclusion, using (4.2) for each single edge and Lemma 5.1 for intersections, now yields the new aggregate estimate
\[
\boxed{
|\mathcal N_{C,R}^\Phi|
\ll_\epsilon D^\epsilon HD^2(R+R^2).
}
\tag{5.3}
\]
There is a sharper bound when the hard-domain conditions make the four events disjoint.

### Lemma 5.2. Exact exclusion of event intersections

If two disjoint cross edges satisfy (5.1), then
\[
\mathcal E\le R^4.
\tag{5.5}
\]
If two edges share a vertex, then
\[
\mathcal E\le\beta DR^3.
\tag{5.6}
\]
In addition, such a star cannot occur under the two small-gcd restrictions if
\[
CR^2\le\alpha D.
\tag{5.7}
\]

**Proof.** For disjoint edges, say \((n_1,m_1)\) and \((n_2,m_2)\), the residual character at every prime is principal if both matched pairs contain the prime equally. More quantitatively, the exponent of that prime in \(\mathcal E\) is at most the sum of its exponents in the four reduced ideals
\[
n_1/(n_1,m_1),\quad m_1/(n_1,m_1),\quad
n_2/(n_2,m_2),\quad m_2/(n_2,m_2).
\]
A singleton contributes one to both sides; a nonprincipal double contributes \(1/2\) to the left and two to the right; other multiplicities contribute zero to the left. Their product norm is at most \(R^4\), proving (5.5).

For a star centered at \(n_1\), use
\[
\mathcal E\le
Nn_2\,
N\!\left(\frac{n_1}{(n_1,m_1)}\right)
N\!\left(\frac{m_1}{(n_1,m_1)}\right)
N\!\left(\frac{m_2}{(n_1,m_2)}\right)
\le\beta DR^3.
\]
To check the first inequality prime by prime, let \(x,w,y,z\in\{0,1\}\) be its indicators in \(n_1,n_2,m_1,m_2\). The exponent on the right is
\(w+x(1-y)+y(1-x)+z(1-x)\). It is at least one at every singleton and at least \(1/2\) at each same-side double. At triples, quadruples and principal doubles the exponent of \(\mathcal E\) is zero. This proves (5.6); the other star shapes follow by symmetry.

Finally the ideals are squarefree, so
\[
N(n_1,m_1,m_2)
\ge
\frac{Nn_1}{
 N(n_1/(n_1,m_1))\,N(n_1/(n_1,m_2))}
\ge\frac{\alpha D}{R^2}.
\]
The common ideal on the left divides \((m_1,m_2)\). Under (5.7) this contradicts \(N(m_1,m_2)<C\). The same argument applies to a star on the other side. \(\square\)

Thus if
\[
R^4\le H,\qquad
\bigl(CR^2\le\alpha D\ \text{or}\ \beta DR^3\le H\bigr),
\tag{5.8}
\]
every pairwise intersection is empty inside the hard small-gcd domain. The union is literally a disjoint sum of four signed sectors. Equation (4.2) then proves the stronger inequality
\[
\boxed{|\mathcal N_{C,R}^\Phi|
\ll_\epsilon D^\epsilon HD^2R.}
\tag{5.9}
\]
This conclusion uses exact local exponent and divisor inequalities, not an assumption that near-match events behave independently.

In particular, for any fixed measurable subpower function \(R(D)\ge1\), meaning
\(R(D)\le D^\eta\) eventually for every \(\eta>0\),
\[
\boxed{
|\mathcal N_{C,R(D)}^\Phi|
\ll_\epsilon HD^{2+\epsilon}.
}
\tag{5.10}
\]
Its implied constant can depend on the chosen function through its eventual bounds. This result allows \(R(D)\to\infty\); it is not restricted to a finite set of exact coincidences.

## 6. A stricter sufficient remainder

Now restrict \(1<h\le11/10\) and use the classical cutoff
\[
C(D)=D^{(6-h)/7}.
\]
Define
\[
\mathcal V_{h,R}(D)
=\mathcal U_{C(D)}^\Phi(D,D^h)
-\mathcal N_{C(D),R(D)}^\Phi(D,D^h).
\tag{6.1}
\]
It is the exact real signed sum over tuples satisfying all of
\[
\begin{gathered}
N\gcd(n_1,n_2),N\gcd(m_1,m_2)<D^{(6-h)/7},\\
g_1\ne1,\qquad Ng_1\sqrt{Ng_2}>D^h,\\
\Delta(n_i,m_j)>R(D)\quad\text{for every }i,j.
\end{gathered}
\tag{6.2}
\]
For subpower \(R\), the proved signed inequality from #919 and (5.10) give
\[
\boxed{
M_4(D,D^h)
\le K_{\epsilon,h}D^{h+2+\epsilon}
  +2\mathcal V_{h,R}(D),
\qquad
\mathcal V_{h,R}(D)\ge-K_{\epsilon,h}D^{h+2+\epsilon}.
}
\tag{6.3}
\]
The lower bound follows from the old remainder's lower bound and (5.10). No positivity is attributed to the new selected signed sum.

Consequently a one-sided averaged upper bound
\[
\int_X^{2X}\mathcal V_{h,R}(D)\frac{dD}{D}
\le B_{\epsilon,h,e}X^{h+2+e+\epsilon}
\tag{6.4}
\]
for every \(\epsilon>0\) and every sufficiently large \(X\), with \(e\ge0\), would imply the same strict conditional boundary
\[
\Re s>\frac12+\frac{5h}{24}+\frac e4
\tag{6.5}
\]
for the source's fixed-row twist family, when the factor test is the fixed universal Mellin detector. Unlike #919's classical-only fourth reduction, (6.3) now explicitly retains the native premise (1.2). Equation (6.4) is unproved; it has not been inferred from the signed-sector bound.

A polynomial choice has a stronger range than the general intersection count alone suggests. Let \(R=D^r\), with
\[
0\le r<\frac{1+h}{14},\qquad 1<h\le11/10.
\tag{6.6}
\]
Since \(C=D^{(6-h)/7}\), the strict inequality in (6.6) ensures \(CR^2\le\alpha D\) for all sufficiently large \(D\). Also
\((1+h)/14<h/4\) in this range, so \(R^4\le H\). Lemma 5.2 applies. Consequently the union cost is only \(r\), and a signed average for \(\mathcal V_{h,R}\) with excess \(e\) would give total moment excess
\[
\boxed{\max(e,r)}
\tag{6.7}
\]
and boundary \(1/2+5h/24+\max(e,r)/4\). For one specified cross position the cost \(r\) holds without (6.6); for the union outside the disjoint-event range, the generally proved cost remains \(2r\). None of these statements bounds the residual average itself.

## 7. A stronger cross-gcd tail from the pointwise exponent

The preceding results use only the native second moment. This section adds, explicitly and separately, the uniform pointwise premise
\[
|A_u(Y;W)|\ll_{\epsilon,b}D^\epsilon Y^b,
\qquad \frac12<b\le1,
\quad 0<Nu\le c_\Phi H,\quad 1/\beta\le Y\le D.
\tag{7.1}
\]
At \(b=1\), it is elementary counting. At \(b<1\), it requires the row-uniform estimate, such as the separately proved uniform reciprocal adapter with its zero-free premise; a fixed-character estimate with uncontrolled conductor constants is insufficient.

The precise inherited core consequence is PR #915 at
9959364671f89b86f3992ec5ed5e19f804eb607b,
ANISOTROPIC_SINGLETON_CORES.md, Theorem (3.1), SHA-256
4854a01c2767a1dc4d7c67c490e5502bcad8935bce3089ba5f37adb1e6d02ea8.
For the actual two-factor coprime core
\[
\mathcal B_{\ell,u}(Y,Z)=
\sum_{\substack{(a,m)=1\\(am,\ell S)=1}}
\mu_K(a)\mu_K(m)\nu(am)\chi_{am}(u)
W(Na/Y)W(Nm/Z),
\]
it gives
\[
\|\mathcal B_{\ell,\cdot}(Y,Z)\|_{\Phi,H}
\ll_\epsilon D^\epsilon\sqrt H\, Z^{1/2}Y^b
\quad (Y\le Z),
\tag{7.2}
\]
uniformly for polynomial-sized \(\ell\) and smaller nonempty scales. The source estimate is initially over nonzero rows. At the zero row a shortened core can retain the two unit ideals, but that single contribution is \(O_W(1)\); it is absorbed in (7.2) because \(H\ge1\) and both nonempty scales have fixed positive lower bounds. Thus the displayed complete smooth norm is legitimate even when the shortening introduces unit columns. It keeps all moving exclusions through the exact forward Euler correction. The weights \(b,1/2\) have sum greater than one, so its absolute weighted correction norm converges. This is the analytic input of the next lemma, in addition to the literal finite identities.

### Lemma 7.1. The two-factor polynomial with its original gcd threshold

For a good squarefree \(q\), \(Nq\le\beta D\), put \(X=D/Nq\) and
\[
F_{q,C}(u)
=\sum_{(a,qS)=1}
 \mu_K(a)\nu(a)\chi_a(u)W(Na/X)B_{qa,C}(u).
\tag{7.3}
\]
Then uniformly in \(q,C\),
\[
\boxed{
\|F_{q,C}\|_{\Phi,H}^2
\ll_\epsilon D^\epsilon HD\,X^{2b}.
}
\tag{7.4}
\]

**Proof.** In the long inner factor \(m\), set
\[
t=(q,m)\mid q,\qquad d=(a,m),\qquad
a=da_0,\quad m=dtm_0.
\]
Since \(a\) is coprime to \(q\), the ideals \(d,t\) are coprime. The original squarefree conditions imply that \(a_0,m_0\) are pairwise coprime and both prime to \(dqS\). Conversely these conditions reconstruct exactly the original squarefree pair, with
\[
(qa,m)=td.
\]
With \(\eta_u(n)=\nu(n)\chi_n(u)\), coefficient multiplication therefore gives the exact finite identity
\[
F_{q,C}(u)
=
\sum_{\substack{t\mid q,\ d\ {\rm squarefree}\\
(d,qS)=1,\ N(td)<C}}
 \mu_K(t)\eta_u(t)\eta_u(d)^2
 \mathcal B_{dq,u}
 \left(\frac{X}{Nd},\frac{D}{Nd\,Nt}\right).
\tag{7.5}
\]
The exterior multipliers have modulus at most one, including at their zeros. No character division is used. The Möbius factors from the common \(d\) occur twice and square to one, which explains the absence of a Möbius sign on \(d\).

The second core scale is at least the first, since their ratio is \(Nq/Nt\ge1\). Thus (7.2) applies in the stated order. Every nonempty term has \(Nd\ll X\), so \(N(dq)\ll D\); all masks remain polynomially bounded. Minkowski yields
\[
\begin{aligned}
\|F_{q,C}\|_{\Phi,H}
&\ll D^\epsilon\sqrt{HD}\,X^b
 \sum_{t\mid q}(Nt)^{-1/2}
 \sum_d(Nd)^{-b-1/2}\\
&\ll D^\epsilon\sqrt{HD}\,X^b.
\end{aligned}
\]
The ideal \(d\)-sum converges because \(b+1/2>1\); the \(t\)-sum is a subpower divisor factor. The condition \(Ntd<C\) is dropped only from this positive norm majorant. Reassign the losses and square. \(\square\)

### Theorem 7.2. An actual small-gcd covariance with a large cross gcd

Let \(\mathcal G_{11}(D,H;C,T)\) be the same complete smooth small-gcd covariance as in (3.2), but with the cross condition
\[
N(n_1,m_1)\ge T,\qquad T\ge1,
\]
instead of \(\Delta(n_1,m_1)\le R\). Under (7.1),
\[
\boxed{
|\mathcal G_{11}(D,H;C,T)|
\ll_\epsilon D^\epsilon HD^{1+2b}T^{1-2b}.
}
\tag{7.6}
\]
In particular, \(T=D/R\), \(1\le R\le D\), gives
\[
\boxed{
|\mathcal G_{11}(D,H;C,D/R)|
\ll_\epsilon D^\epsilon HD^2R^{2b-1}.
}
\tag{7.7}
\]

**Proof.** Write the exact cross gcd as \(c=(n_1,m_1)\), so \(n_1=ca\), \(m_1=cb\), where \(a,b,c\) are squarefree and pairwise coprime. Freeze \(c\) but retain both of the original within-side gcd thresholds in \(B_{ca,C}\) and \(B_{cb,C}\).

Remove only \((a,b)=1\) by its finite identity
\({\bf1}_{(a,b)=1}=\sum_{e\mid(a,b)}\mu_K(e)\). Reindex \(a=ea_0\), \(b=eb_0\). Here \(e\) is squarefree, \((e,cS)=1\), and \(a_0,b_0\) are each coprime to \(ceS\), with no remaining mutual coprimality requirement. The result is exactly
\[
\mathcal G_{11}
=\sum_{\substack{c\ {\rm squarefree}\\(c,S)=1\\Nc\ge T}}
 \sum_{\substack{e\ {\rm squarefree}\\(e,cS)=1}}
 \mu_K(e)
 \sum_u\Phi(u/\sqrt H)
 {\bf1}_{(u,ce)=1}|F_{ce,C}(u)|^2.
\tag{7.8}
\]
Only \(N(ce)\le\beta D\) can contribute. To check the scalar in this identity, \(\mu_K(c)^2=\mu_K(e)^2=1\), and the norms of the good finite-order character values are one. The two sextic factors at \(ce\) multiply to their literal coprimality indicator. The remaining \(\mu_K(e)\) comes from inclusion–exclusion. It has not been replaced by a positive coefficient before the identity.

Apply (7.4) to the full square in (7.8), then bound the resulting positive majorant:
\[
\begin{aligned}
|\mathcal G_{11}|
&\ll D^\epsilon HD^{1+2b}
 \sum_{Nc\ge T}(Nc)^{-2b}\sum_e(Ne)^{-2b}\\
&\ll D^\epsilon HD^{1+2b}T^{1-2b}.
\end{aligned}
\]
Both sums are over ideals; the second converges for \(2b>1\), and elementary ideal counting gives the first tail. All support and coprimality restrictions may be removed in these positive majorants. This proves (7.6) and (7.7). \(\square\)

The use of a cross-gcd tail rather than a sharp upper bound on each reduced factor is deliberate: the reindexed tests in (7.8) remain the original smooth \(W\) at shorter scales. No interval-maximal bound or uniform control of discontinuous moving tests is being presumed.

### Corollary 7.3. The union has the same improved cost in the disjoint range

Adding the hard conductor conditions to a single \(\mathcal G_{ij}\) changes it by at most \(O_\epsilon(HD^{2+\epsilon})\), by the same controlled accounting argument as Section 4. Let \(\mathcal L_{C,T}^{\rm hard}\) be the hard small-gcd sum in which at least one cross gcd has norm at least \(T\). If
\[
\left(\frac{\beta D}{T}\right)^4\le H,
\qquad
T^2\ge\beta DC,
\tag{7.9}
\]
these four events are pairwise disjoint inside the hard domain.

For disjoint edges, each reduced ideal has norm at most \(\beta D/T\), so (5.5) excludes their intersection. For a star centered at \(n_1\),
\[
N(n_1,m_1,m_2)
=\frac{N(n_1,m_1)N(n_1,m_2)}
 {N\,\operatorname{lcm}((n_1,m_1),(n_1,m_2))}
\ge\frac{T^2}{Nn_1}
\ge\frac{T^2}{\beta D}.
\]
This divides \((m_1,m_2)\), contradicting its strict upper bound \(C\) under (7.9). The other stars are symmetric.

Consequently, for \(T=D/R\), \(1\le R\le D\), satisfying (7.9),
\[
\boxed{
|\mathcal L_{C,D/R}^{\rm hard}|
\ll_\epsilon D^\epsilon HD^2R^{2b-1}.
}
\tag{7.10}
\]
At \(C=D^{(6-h)/7}\), \(1<h\le11/10\), every fixed
\(R=D^r\) with \(0<r<(1+h)/14\) satisfies (7.9) for all sufficiently large \(D\). Any fixed bounded \(R\), and any chosen growing subpower \(R\), also satisfies the inequalities eventually. Support constants affect the endpoints, not these strict exponents.

If \(\mathcal V_{h,R}^{(b)}\) is obtained by subtracting precisely this union from the old remainder, a signed averaged upper bound with excess \(e\ge0\) would give total moment excess
\[
\boxed{\lambda=\max\{e,(2b-1)r\}}
\tag{7.11}
\]
at polynomial \(R=D^r\), in the stated range. The corresponding conditional extraction threshold is
\(1/2+5h/24+\lambda/4\). For subpower \(R\), the new controlled cost is zero in the exponent.

Thus a supplied uniform \(b=7/8\) gives the proved sector factor \(R^{3/4}\), improving the \(R\) factor from native second moment alone. This is an actual sharper inequality for the selected signed sector. It is not an estimate for the remainder after removal. No numerical zero-free improvement is claimed.

## 8. Strictness and the surviving obstruction

Take three pairwise coprime squarefree ideals \(n,a,b\) on the supported scale \(D\), and form
\[
(n_1,n_2;m_1,m_2)=(n,a;n,b).
\tag{8.1}
\]
Both one-sided gcds are one. In the full tuple \(n\) is a principal mask, \(g_1=ab\), \(g_2=1\), and
\(\mathcal E\asymp D^2>D^h\) for every fixed \(h<2\). Thus these feasible supported patterns lie inside the old hard remainder. Their one-sided singleton parameter is of scale \(D\), so they are not removed by a subpower one-sided periphery either. But \(\Delta(n_1,m_1)=1\), and (5.10) controls the aggregate containing them. For any nonzero test with an open interval of nonzero values, large admissible distinct prime ideals supply such patterns; only nonempty support is needed for this domain comparison.

This is a strict removal of additional signed configurations. It does not say their individual contributions are large or that deleting them decreases the absolute value of the remaining sum. The full covariance, followed by controlled accounting and a finite inclusion–exclusion argument, is what justifies the reduction.

Four mutually disjoint long factors have all four separations of size \(D\). They remain in (6.2) for every subpower \(R\), and retain the large-conductor obstruction. The proof supplies additional actual signed-sector inequalities, including the improved cross-gcd tail (7.10). It neither improves the one-sided cubic common-factor cutoff nor resolves that balanced, far-separated remainder.
