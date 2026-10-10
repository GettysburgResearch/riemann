# Independent review of the angular scalar and coupled component estimates

**Reviewer:** moment_structure_attack, independent of the author of centered_a2_attack.md.

**Verdict:** PASS at the source-conditional scope stated below. Sections 6–7 of the frozen note give valid deductions from its fixed-angle canonical mean-square input and the explicitly imported theta and large-sieve interfaces. The moving-conductor scalar bound and its use inside the coupled component have been checked separately. This is not a verification of the full generalized moment hierarchy or RH.

**Reviewed source:** /workspace/scratch/6ec6134c1535/centered_a2_attack.md.

**Reviewed SHA-256:** bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a.

**Scope:** Theorem 6.1, Lemmas 6.2–6.3, Corollary 6.4, Theorems 7.1 and 7.3, Corollary 7.2, the all-negative estimate (7.14), the smooth allocation convention, and the stated boundaries. Sections 2–5 are taken as the separately reviewed angular adapter; this review also checked the initial Gauss order needed when applying that adapter in Section 6.

**Imported source pins:** OpenAI/math adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 build/paper2.tex; parent PR #914 at 0cc0428fedbbfc340044c7451b3d392c1da9a103; adjacent PR #915 at 9959364671f89b86f3992ec5ed5e19f804eb607b.

The source formulas inspected directly are the initial paired Gauss identity and initial column output; the full reflection scalar; the prepared theta coefficient, coefficient bound, and transformed-weight bound; the smooth separation appendix; PR #915's exact mixed scalar, Ramanujan reindexing, and quadratic–cubic composition lemma. Their file hashes and the frozen reviewed copy are recorded in the companion manifest.

No numerical zero computation or finite experiment is used to certify an analytic assertion. No source repository was edited by this reviewer.

## 1. Initial angular mean square and extraction

The source conjugates its original inner sum before expanding the square. Consequently, inserting an angular factor \(\alpha(n)^t\) multiplies its coprime pair by

\[
\alpha(z_1/z_2)^{-t}.
\]

The source coefficient is \(a_{-1,\xi}(z)=\alpha(z)^{-1}\gamma_2(z)\xi(z)\). Thus the initial Gauss pair becomes

\[
a_{-t-1,\xi}(z_1)\overline{a_{-t-1,\xi}(z_2)}.
\]

The required reflected order is therefore \(r=-t-1\). In particular, \(t=-3\) uses \(r=2\); it does not invoke the excluded derivative order zero.

The common angular factor cancels against its conjugate in the common-divisor extraction. The source's exact masks and norm scales remain

\[
X=\frac D{BF},\qquad
\Sigma=XF=\frac DB,\qquad
\mathcal H\ll\frac{D^{1-\vartheta}}{B^2}.
\]

Hence \(\mathcal H/\Sigma\ll D^{-\vartheta}\). For sufficiently large \(D\), the constant is absorbed by the gap \(\kappa=\vartheta/2\); the source's bounded cases cover the remaining ranges. The source's zero Fourier contribution is unchanged in size because the inserted common angular factor has modulus one. Its normalization is \(1/D\), so a normalized bound \(H D^\epsilon\) gives the displayed unnormalized bound \(H D^{1+\epsilon}=D^{2+\vartheta+\epsilon}\).

The mean square includes every nonzero row, including the sixth powers used in the scalar extraction. For primary primes with \(Y/2<Np\le Y\), \(Y=D^{(1+\vartheta)/6}\), one has the literal identity

\[
\chi_n(p^6)=\mathbf1_{p\nmid n}.
\]

The difference from row \(1\) is bounded by the number of multiples of \(p\) in the fixed column annulus:

\[
|A_{1,t}(D)-A_{p^6,t}(D)|\ll_W D/Y.
\]

The fixed-field prime ideal theorem supplies \(\gg Y/\log Y\) such primes outside the fixed set \(S\). Averaging over this subset of the nonnegative row norm gives

\[
|A_{1,t}(D)|^2
\ll D^{11/6+5\vartheta/6+\epsilon}
   +D^{5/3-\vartheta/3}.
\]

Both exponents in the note are correct. Choosing the fixed positive \(\vartheta\) and the intermediate loss sufficiently small proves the exponent \(11/12+\epsilon\). No conductor-uniform constant is claimed at this stage.

## 2. Common zero-free half-plane and uniform reciprocal

### 2.1 The Mellin contradiction is valid

The primary-generator convention is multiplicative away from the fixed bad primes. On all six generators of an ideal, the compensating unit factor is periodic modulo \(3\). Consequently an arbitrary fixed integer angular power can be represented as a genuine nonzero infinity type with a periodic finite part. It is not being treated as a finite-order character.

For a hypothetical zero \(\rho\) with \(\Re\rho>11/12\), the test

\[
W(y)=y^{-\rho}\varphi(y),\qquad
\varphi\in C_c^\infty((1,2)),\quad \varphi\ge0,\quad\varphi\ne0,
\]

satisfies \(\widehat W(\rho)>0\). The Mellin integral of the scalar sum is holomorphic in that half-plane and, initially for \(\Re s>1\), equals \(\widehat W(s)/L^S(s)\). Multiplying by \(L^S(s)\), then continuing the product identity, gives the contradiction at \(\rho\). There is no lower-end divergence in the integral because a fixed compact column test vanishes for all sufficiently small \(D\).

This proves a common boundary for every fixed finite twist, even though its mean-square constant may depend on that twist. The next lemma supplies the separate uniformity argument that is necessary for moving \(k,d\).

### 2.2 The translated lattice estimate is uniform

For fixed \(t\ne0\), the ideal character sum is a bounded periodic linear combination of angular sums over translated ideal lattices. In the Eisenstein field each ideal lattice is similar to the fixed ambient lattice, with spacing comparable to \(\sqrt Q\), where \(Q\) is its norm. Thus there is no unmentioned dependence on a lattice shape parameter.

For one residue class, comparison with fundamental cells gives

\[
\sum_{\substack{z\equiv a\pmod{\mathfrak q}\\0<|z|\le R}}
\alpha(z)^t
=\frac1{\operatorname{covol}(\mathfrak q)}
\int_{|z|\le R}\alpha(z)^t\,dz
+O_t(R/\sqrt Q+1).
\]

The cells near the origin and boundary give the stated error. On the other cells, \(|\nabla\alpha(z)^t|\ll_t1/|z|\); summing the gradient errors over annuli gives another \(O_t(R/\sqrt Q+1)\). The disk integral is zero for a nonzero integer \(t\).

Summing over at most \(Q\) residue classes with bounded periodic weights yields

\[
\sum_{Nn\le x}(\eta\alpha^t)(n)
\ll_t\sqrt{Qx}+Q\ll_t Q\sqrt x,\qquad x\ge1.
\]

Excluded-prime zeros may be included in the periodic weights, so the same estimate applies to imprimitive characters. Partial summation gives holomorphy on \(\Re s>1/2\) and polynomial growth \(O_{t,a}(Q(1+|s|))\) for each fixed \(a>1/2\). This supplies the growth premise needed in the logarithm argument, without importing a conductor-uniform scalar constant from Theorem 6.1.

### 2.3 The logarithm interpolation yields a subpower bound

For the nonzero infinity type there is no pole in the half-plane, and the common zero-free statement gives a holomorphic Euler-compatible logarithm on \(\Re s>\beta=11/12\). Borel–Carathéodory on fixed disks extending to a line \(a>\beta\), with center \(2+i\tau\), bounds the logarithm there by

\[
|\log L(a+i\tau)|\ll\log[Q(2+|\tau|)].
\]

The Euler logarithm is uniformly bounded on a fixed line \(b>1\). On the strip between the two lines, multiplication by \(e^{(s-i\tau_0)^2}\) makes the three-lines theorem applicable. At any fixed positive distance to the right of \(\beta\), the resulting exponent of \(\log[Q(2+|\tau_0|)]\) is strictly below one. Exponentiation therefore gives

\[
|L(\sigma+i\tau,\eta\alpha^t)^{-1}|
\ll_{t,\delta,\epsilon}[Q(2+|\tau|)]^\epsilon,
\qquad \sigma\ge\beta+\delta.
\]

The interval \(\sigma\ge b\) follows from the Euler product. This verifies the conductor and height uniformity claimed in Lemma 6.3.

For Corollary 6.4 the finite character is \(\eta(g)\chi_k(g)^3\), with moving exclusion \(\mathfrak d\), and its modulus norm is \(O_S(Nk\,N\mathfrak d)\). The zero at \((g,k)>1\) is part of this imprimitive Euler product. Mellin shifting a fixed smooth test to \(\beta+\delta\) gives \(G^{\beta+\delta}Q^\epsilon\). Under the stated polynomial scale ceilings the small margins are absorbed into \(D^\epsilon G^\beta\). Norm modulation of the test costs only a polynomial in its Mellin frequency, measured by the displayed finite smooth seminorm.

## 3. Exact standard-face factorization and moving-mask removal

PR #915's complete scalar calculation leaves exactly

\[
\mu(g)\eta(g)\alpha(g)^{-3}\chi_k(g)^3.
\]

The angular exponent \(-3\) depends on retaining the full source scalar, including \(\overline{\alpha(c)}^2\). The local negative Ramanujan summand is present even at a prime dividing the reflected index. Consequently there is no condition \((g,n'b')=1\).

On the stated standard face, Gauss CRT factors the coefficient into separate \(e,n'\) vectors and \(\chi_{n'}(e)^4\). The latter is zero when \((e,n')>1\); that condition is retained exactly. Fixed ray restrictions and additive phases are expanded into a finite family of characters before applying the scalar lemma. All resulting \(g\)-twists remain among the finite twists covered by that lemma.

The factor \(\mathbf1_{(g,e)=1}\) must be removed before a pointwise scalar estimate can be applied independently of the \(e,n'\) vectors. The note does this with the exact identity

\[
\mathbf1_{(g,e)=1}
=\sum_{\substack{d\mid g\\d\mid e}}\mu(d),
\qquad g=dg',\quad e=de'.
\]

The factorized arithmetic expression defines an admissible extension away from the original coprime support. Inclusion–exclusion then recovers precisely the original expression; it does not require the reflected formula for a nonsquarefree original \(a\).

Squarefreeness retains \((g',d)=(e',d)=1\), and

\[
\mu(d)\mu(dg')=\mu(g').
\]

The remaining \(g'\)-exclusion is \(df\). Factors depending on \(d\) enter the separate \(e'\)-vector, \(n'\)-vector, or row multiplier. In particular, \(\chi_{n'}(d)^4\) is a column factor and \(\chi_k(d)^3\mathbf1_{(k,d)=1}\) is a row contraction. There is no surviving \((g',e')=1\) condition. The row mask \((k,e')=1\) remains in the quadratic–cubic composition.

Thus the scalar estimate at scale \(G/Nd\) is uniform for each row and independent of the two remaining column indices. Applying it before their row norm is justified.

## 4. Normalization and the factor \(G^{-1/6}\)

The source normalization before the \(n',b'\) sums is

\[
(AFG)^{-1/2}(Nb')^{-1}.
\]

After extracting \(d\), the remaining double sum is \(\sqrt{E'}\) times PR #915's normalized composition, with \(E'=E/Nd\). The factor \(1/\sqrt{Nn'}\) can be compared with \(1/\sqrt U\) on its fixed annulus and the bounded ratio retained in the \(n'\)-vector.

PR #915's lemma gives, with the surviving row mask intact,

\[
\sum_k^*|Q_k(E',U)|^2
\ll D^\epsilon\frac{H+U}{U}
\left[E'+U+(E'U)^{2/3}\right].
\]

There are \(O(F)\) frozen \(f\)-labels. Minkowski, the scalar bound, and the \(\sqrt{E'}\) normalization produce the squared factor

\[
\frac{F^2}{AFG}
\left(\frac G{Nd}\right)^{2\beta}\frac E{Nd}
\asymp G^{2\beta-2}(Nd)^{-2\beta-1}.
\]

This is the correct power of every variable. Minkowski over \(d\) costs

\[
\sum_d(Nd)^{-\beta-1/2}<\infty
\]

for \(\beta>1/2\). It does not cost a further positive power of \(E\) or \(G\). Taking \(\beta=11/12\) yields \(G^{-1/6}\).

The bounded nonempty ranges \(E'<1\) or \(G/Nd<1\) lie within fixed annuli and are absorbed into constants. Empty ranges contribute zero.

## 5. Smooth partitions, Mellin separation, and infinite tails

The frozen note explicitly uses a fixed smooth dyadic partition in \(e,f,g\). This is needed because Corollary 6.4 is a smooth scalar estimate. Its application to a sharp \(g\)-cutoff would require an additional argument. The exact smooth partition sums back to the full allocation expansion.

The source's smooth-weight appendix gives, for a kernel of the form

\[
\mathcal K_R(\mathbf x)
=\prod_j W_j(x_j)\,
F\!\left(R\prod_jx_j^{a_j}\right),
\]

an integrable Mellin majorant with arbitrarily many polynomial frequency moments and decay \((1+R)^{-A}\). This remains uniform after \(g=dg'\), \(e=de'\), because the normalized coordinates are unchanged:

\[
\frac{Ng'}{G/Nd}=\frac{Ng}{G},
\qquad
\frac{Ne'}{E/Nd}=\frac{Ne}{E}.
\]

Thus moving \(d\) introduces neither a sharp test nor a growth in the smooth seminorm. Row norm phases from Mellin separation have modulus one.

The tail argument does not require an unsupported polynomial cutoff in the dual index. With \(C\) the cube scale, its decay parameter is

\[
z=\frac{3^mUC^3}{Y},\qquad m\ge-4.
\]

Since \(Y\) is polynomially bounded and \(U\ll Yz\), every sieve loss involving \(U^\epsilon\) is absorbed by a smaller \(D^\epsilon\) loss and a small power of \(1+z\). The arbitrary decay exponent in the source majorant absorbs the latter.

For the standard face the composition bound has square-root majorant

\[
\sqrt{HE'}+\sqrt U+E'^{1/3}U^{1/3}.
\]

Summing this against \((1+UC^3/Y)^{-A}\) over dyadic \(U,C\ge1\) gives

\[
\ll \sqrt{HE'}\log^2(2+Y)+\sqrt Y+(E'Y)^{1/3}.
\]

This holds also for \(Y<1\), because all nonzero terms are then in the rapidly decreasing tail. Squaring recovers the claimed \(HE+Y+(EY)^{2/3}\) envelope with a subpower loss. The cube weight has bounded total mass on each dyad.

## 6. All cusps and the balanced standard-face range

Theorem 7.3 uses only the source's prepared coefficient bound

\[
|A_{u,m}(en',fb')|\le27.
\]

After fixed ray splitting, that coefficient is independent of \(g,k\). Fixing \(e,f\) leaves a scalar \(g\)-sum with exclusion \(ef\), independent of \(n'\). The remaining \(n'\)-vector is arbitrary bounded and therefore fits the quadratic large sieve. There is no use of standard-cusp Gauss factorization at the other cusps.

The retained row factors \(\chi_k(b')^3\mathbf1_{(k,ef)=1}\) are contractions. Squarefree parts of \(n'\) supported at the fixed bad set can be split into finitely many cases; the cube index is not deleted at those primes. Minkowski over \(O(EF)\) choices of \(e,f\) gives

\[
\frac{E^2F^2}{AFG}G^{2\beta}
\asymp EG^{2\beta-2}.
\]

The source's ramified amplitude is \(3^{-m/3}\), and its effective length is \(Y/(3^mC^3)\). Both the square-root \(H\) contribution and the square-root length contribution are summable over \(m\ge-4\). This verifies

\[
\sum_k^*|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon E G^{-1/6}(H+Y)
\]

with all three source cusp sequences present.

For the stronger standard-face estimate, when \(A=B=D\), the identities

\[
Y\asymp H^2G/F^2,\qquad EY\asymp H^2D/F^3
\]

give the three bounds

\[
G^{-1/6}HE\ll HD,\qquad
G^{-1/6}Y\ll H^2D^{5/6},\qquad
G^{-1/6}(EY)^{2/3}\ll H^{4/3}D^{2/3}.
\]

There are only logarithmically many smooth allocation blocks, so Minkowski preserves the displayed subpower loss. The limiting term at \(H=D^{7/12}\) is \(H^2D^{5/6}=D^2\). The other two terms remain below \(D^2\). Thus Corollary 7.2 is correctly restricted to the standard face.

At \(E=F=1,G=A\), the direct quadratic-sieve calculation gives

\[
D^\epsilon\left[HA^{-1/6}+\frac{H^2A^{11/6}}B\right].
\]

Its first term is not uniformly better than the earlier \(H/A\) term; the note correctly retains both available estimates.

## 7. Acceptance boundary

The statements reviewed here are valid deductions at their declared source-conditional scope. They still assume the imported scalar theta automorphy, cusp coefficient estimates, the relevant quadratic and cubic large sieves, and the finite transfer mechanism carried through the separately reviewed fixed-angle adapter.

The quantitative coupled bounds concern squarefree primary rows and completed reflected components. The stronger \(H\le D^{7/12}\) range applies to the specified standard-cusp face. The weaker all-cusp theorem does not supply that same whole-face range. Neither theorem gives the initial fourth-moment dual range of order \(D^{3-\vartheta}\) at product length \(D^2\).

The estimates are positive row norms of specified linear components. They do not by themselves control a centered sesquilinear form after signed diagonal removal or invert a complete family of completion corrections at all needed scales. No higher moment or RH claim follows without those additional theorems.

The separately authored double-reflection cutoff note is outside this review. Its contents and any later change to centered_a2_attack.md require their own exact-source review.
