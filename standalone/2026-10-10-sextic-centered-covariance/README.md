# All-row theta bounds, exact divisor support, and generalized Hermitian moment sectors

**Status:** proposed standalone research, stacked on PR #914. This packet proves new component estimates and an exact finite obstruction. Its analytic results are deductions from the explicitly pinned imported theta, sieve, and second-moment inputs. The full fourth moment, the generalized diagonal moment hierarchy, the boundary 17/24, and RH remain open. No new numerical zero-free boundary for zeta is asserted.

**What advances:** a second theta reflection restores the original compactly supported weight and proves an exact cutoff for every reunited negative-divisor component, at every nonzero row. Explicit classical cusp formulas give a quantitative bound for the entire coupled completion. A fixed angular derivative extension supplies cancellation in two actual Möbius factors, allowing the cube completion to be removed completely in a stated range. An additional mixed-scalar calculation and summation over repeated row primes extend both bounds to all nonzero rows and give explicit costs for a moving auxiliary twist. Separately, a general-order Hermitian incidence argument can use an odd repeated-prime ideal as a native inverse factor. All statements retain their arithmetic coefficients, signs, and nonunit zeros.

**Source boundary:** this packet does not independently reconstruct the imported scalar theta automorphy or its underlying large sieves. It does prove the new derivative, Mellin, conductor-uniformity, incidence, and moving-mask adapters, and records independent scoped reviews. The local checks authenticate specified finite identities; they are not an asymptotic proof or a Lean formalization.

## 1. The exact target

Over K = Q(sqrt(-3)), with its primary-generator convention, write

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6.
\]

Here nu is fixed and finite order, S is fixed, W is a fixed smooth compactly supported test, and every symbol has its literal zero at nonunits. The desired estimate is

\[
\sum_{0<Nu\le H}|A_u(D)|^{2k}
\ll_{k,\nu,S,W,\theta,\epsilon}HD^{k+\epsilon},
\qquad H=D^{1+\theta},
\tag{1.1}
\]

for every fixed k and arbitrarily small fixed positive theta, with the test and scale quantifiers required by Mellin extraction. All nonzero element rows, including sixth powers and all their units, belong to the target.

The letter H in (1.1) denotes the original row scale. Below, mathcal H denotes the different dual row scale in the coupled reflection. The angular calculation's own note uses H for that dual scale; these quantities must not be identified.

## 2. New analytic cancellation in the reflected angular factor

The full proof is [ANGULAR_THETA.md](ANGULAR_THETA.md). It starts from the actual coefficient isolated in the adjacent coupled reflection:

\[
\mu_K(g)\eta(g)\alpha(g)^{-3}\chi_k(g)^3,
\qquad \alpha(g)=g/|g|.
\tag{2.1}
\]

The angular factor in (2.1) cannot be absorbed into a finite-order ray character. The new proof extends the theta argument itself.

For a fixed nonzero integer r, put m=|r| and use the pure horizontal derivative of order m. At the center of cusp inversion it becomes exactly the opposite pure derivative, with factor

\[
(-1)^m\alpha(c)^{2r}N(c)^{-m}v^{-2m}.
\]

There are no lower derivatives or height derivatives. Choosing the Mellin measure v^(2s+m-2)dv makes the conductor factor exactly N(c)^(1-2s), independent of m. The two gamma factors become

\[
\Gamma(s+m/2-1/6)\Gamma(s+m/2+1/6).
\]

The derivative removes the constant mode at every cusp, and the source's finite local transformation and two-Poisson iteration keep the same norm powers. The canonical theorem is retained on its exact domain Sigma=XF and mathcal H <= Sigma D^(-kappa). The missing derivative-order-zero case is explicitly excluded.

For the original inverse coefficient mu(n)nu(n)alpha(n)^t, the initial reflected order is r=-t-1. Thus t=-3 is admissible, with r=2. The argument derives the native angular second moment, extracts the exponent 11/12 for every fixed finite twist of this angular type, and proves a conductor-uniform reciprocal bound using an explicit angular lattice estimate and the analytic logarithm. The resulting uniform scalar estimate is

\[
\left|\sum_{(g,Sq)=1}\mu(g)\eta(g)\alpha(g)^{-3}
\chi_k(g)^3V(Ng/G)\right|
\ll D^\epsilon G^{11/12}\|V\|_{C^J},
\tag{2.2}
\]

for polynomially bounded moving k,q,G and fixed smooth support. The exponent 11/12 here is newly derived for the fixed angular family. The stronger finite-order exponent elsewhere in the repository is not substituted for it.

### The second reflection gives an exact support cutoff

[REUNITED_SUPPORT_CUTOFF.md](REUNITED_SUPPORT_CUTOFF.md) proves an exact result before any component norm is taken. Reunite the positive Ramanujan choices into h and retain the negative label g:

\[
\prod_{p\mid a}(Np)^{-1/2}[-1+Np\mathbf1_{p\mid x}]
=\sum_{hg=a}\mu(g)\sqrt{Nh/Ng}\,\mathbf1_{h\mid x}.
\tag{2.3}
\]

For fixed h,g, the full theta frequency multiplier has period dividing Mkh, with fixed M. The first reflected scale contains (Nk Nh Ng)^2/B. A second reflection has reduced denominator norm at most N(M)NkNh, so its restored test argument is bounded below by a fixed positive multiple of (Ng)^2/B. Every nonzero cusp frequency has norm at least 1/81. Consequently,

\[
\boxed{(Ng)^2>C_*B\quad\Longrightarrow\quad
\text{the complete reunited }(h,g)\text{ term is exactly zero}.}
\tag{2.4}
\]

The original proof establishes (2.4) at every cusp and for every squarefree primary row outside S, with no bound on its norm. [ARBITRARY_ROW_SUPPORT.md](ARBITRARY_ROW_SUPPORT.md) extends this exact support assertion to every nonzero Eisenstein row, including arbitrary prime powers, units, and bad-prime valuations. It keeps each active local row factor inside a finite periodic multiplier. Its period divides Mrh, where r is the active good row radical; the factors Nr and Nh cancel from the restored test argument. Good-prime exponents congruent to zero modulo six retain their literal nonunit masks through the source's active/inactive decomposition. Bad-prime and unit factors range through a fixed finite family. The quantitative extension in Section 4 below requires an additional argument.

The proof keeps the full theta frequency sum. Individual e,f allocations need not vanish separately. A smooth cutoff is inserted into the reunited expression before splitting those allocations again.

The exact outgoing test in raw-frequency normalization is V_*(27x). The factor 27 comes from the different normalization constants of the two gamma transforms. The Mellin contour stays inside the transformed test's holomorphy strip, and the horizontal derivatives kill the constant modes. The specialization in [DOUBLE_REFLECTION.md](DOUBLE_REFLECTION.md) shows that the entire all-negative standard-cusp corner vanishes when A^2 is sufficiently larger than B, in particular at A=B=D for large D.

### The quantitative estimate now covers every cusp

[ALL_CUSP_GAUSS_FACTORIZATION.md](ALL_CUSP_GAUSS_FACTORIZATION.md) checks the explicit Dunn–Radziwiłł cusp formulas against the source normalization. After conjugation, every relevant coefficient has the same cubic Gauss factor, times fixed ray and unit factors and the stated ramified amplitude. The fixed bad-prime squarefree part is treated with a cubic Gauss sum; no sextic symbol at the prime above 2 is introduced. All cube valuations are retained.

Here the coupled object is

\[
\mathcal C_{A,B}(k)=\frac1{\sqrt A}
\sum_a^*a_\xi(a)\chi_a(k)W_1(Na/A)T(B;k,a),
\qquad a_\xi(a)=\alpha(a)^{-1}\gamma_2(a)\xi(a),
\]

where T is the source's complete squarefree/cube theta sum and the asterisk restricts primary indices to squarefree ideals outside S. The quantitative row sum in this section has the same squarefree restriction.

For a=efg with smooth norm scales E,F,G and EFG comparable to A, put

\[
Y=\frac{\mathcal H^2EG^2}{BF}.
\]

From a uniform scalar exponent beta in (1/2,1], the full-cusp component estimate is

\[
\sum_{k\sim\mathcal H}^{*}|\mathcal C_{E,F,G}(k)|^2
\ll D^\epsilon G^{2\beta-2}
[\mathcal H E+Y+(EY)^{2/3}].
\tag{2.5}
\]

Its moving restriction (g,e)=1 is expanded before the scalar estimate. The resulting square-root divisor cost (Nd)^(-beta-1/2) is summable. The cubic interaction and row mask are retained. There is no artificial restriction (g,n'b')=1.

After inserting the exact cutoff G at most a constant times sqrt(B), the entire coupled completion satisfies

\[
\sum_{k\sim\mathcal H}^{*}|\mathcal C_{A,B}(k)|^2
\ll D^\epsilon\left[
\mathcal H A+\frac{\mathcal H^2A}{B}
\min(A,\sqrt B)^{2\beta-1}
+\left(\frac{\mathcal H^2A^2}{B}\right)^{2/3}
\right].
\tag{2.6}
\]

At A=B=D this becomes

\[
\boxed{
\sum_{k\sim\mathcal H}^{*}|\mathcal C_{D,D}(k)|^2
\ll D^\epsilon[
\mathcal H D+\mathcal H^2D^{\beta-1/2}
+\mathcal H^{4/3}D^{2/3}].}
\tag{2.7}
\]

| Scalar input for this angular family | Proved dual-row range at target D^(2+epsilon) | Additional dependence |
|---|---|---|
| beta=1, elementary ideal counting | mathcal H <= D^(3/4) | Classical theta reflection and quadratic/cubic upper sieves; no imported canonical induction |
| beta=11/12, equation (2.2) | mathcal H <= D^(19/24) | Source-conditional fixed-angular canonical and moving-conductor adapter |

The exponents 3/4 and 19/24 describe the dual-row norm range. They are not zero-free boundaries. Section 4 removes the squarefree-row restriction without changing these exponents. The finite-order pointwise beta used in the separate incidence results below is a different premise.

## 3. Removing the cube completion completely

[CUBE_INVERSE.md](CUBE_INVERSE.md) gives a bound for the literal polynomial

\[
P_{A,B}(k)=\frac1{\sqrt{AB}}
\sum_{\substack{a,n\ \mathrm{squarefree}\\(a,n)=1}}
a_\xi(an)\chi_{an}(k)W_1(Na/A)W_2(Nn/B).
\tag{3.1}
\]

Every original ideal is primary and outside S. There is no completion on the left side of the theorem below.

The exact cube inverse is

\[
P_{A,B}(k)=\sum_h
\frac{\mu(h)\alpha(h)^{-3}\xi(h)^3\chi_h(k)^3}{Nh}
\mathcal C^{(h)}_{A,B/(Nh)^3}(k),
\tag{3.2}
\]

where the only extra column exclusion in C^(h) is (a,h)=1. In this section h denotes the inverse cube variable; it is distinct from the reunited positive label in (2.3). There is no exclusion between h and the reflected squarefree or cube indices.

The exact cutoff is inserted before separating the positive Ramanujan choices. For smooth norm scales Ng about G and Nh about Z, it becomes

\[
G^2Z^3\ll B.
\tag{3.3}
\]

Both g and h have angular type -3, so both admit the uniform scalar bound (2.2). Their coprimality is removed by the exact finite identity

\[
\mathbf1_{(g,h)=1}=\sum_{\ell\mid g,\ \ell\mid h}\mu(\ell).
\]

After separating the two intersections with the positive squarefree variable e, the norm costs are

\[
(Nd)^{-\beta-1/2},\qquad
(Nj)^{-\beta-1/2},\qquad
(N\ell)^{-2\beta}.
\]

All three sums converge for beta>1/2. The residual positive variable may share primes with ell; the proof does not insert a false additional exclusion. The smooth cutoffs have uniform rescaled derivatives after every divisor extraction.

The resulting bound, for squarefree primary rows outside S, is

\[
\boxed{
\sum_{k\sim\mathcal H}^{*}|P_{A,B}(k)|^2
\ll D^\epsilon\left[
\mathcal H A+\mathcal H^2 A B^{(2\beta-2)/3}
+\mathcal H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right].}
\tag{3.4}
\]

In particular, the source-conditional angular exponent beta=11/12 gives

\[
\boxed{
\sum_{k\sim\mathcal H}^{*}|P_{D,D}(k)|^2
\ll D^\epsilon[
\mathcal H D+\mathcal H^2D^{17/18}
+\mathcal H^{4/3}D^{23/18}]
\ll D^{2+\epsilon},\qquad
\mathcal H\le D^{19/36}.}
\tag{3.5}
\]

Elementary counting, beta=1, gives the corresponding range mathcal H <= D^(1/2). The larger completed range D^(19/24) in Section 2 does not transfer through the present inverse. The worst remaining cube block has G bounded, Z comparable to B^(1/3), and a bounded positive cube-allocation scale F. Equation (3.5) records the gain that survives the complete inverse.

## 4. All nonzero rows and a moving auxiliary

[ARBITRARY_ROW_MOMENTS.md](ARBITRARY_ROW_MOMENTS.md) supplies the additional quantitative adapter. Write a row uniquely as

\[
k=u k_S\tau k_0,
\]

where u is a unit, k_S is supported on the fixed bad set, k_0 contains exactly the good primes of valuation one, and every prime in tau has valuation at least two. Put

\[
T=N(k_S\tau),\quad \mathcal H_0=\mathcal H/T,\quad
R=N(\operatorname{rad}\tau),\quad
\Lambda(\tau)^2=\prod_{v_p(\tau)\equiv4\ (6)}Np.
\]

The full source scalar has local c/p exponent 2j+2 at every active row exponent j. After multiplying by the outer Gauss coefficient, the cross-symbol exponent becomes 3j. This exposes the same angular Möbius variable with a quadratic twist by the odd row radical. The complete row radical remains in the moving exclusion, including primes whose exponent is zero modulo six.

After the original exclusion (a,k)=1 is retained, a row exponent-four Ramanujan factor depends only on the squarefree theta index and the frozen cube index. It has squared amplitude at most Np. The other row factors separate into bounded column vectors. Thus the fixed-row-sector estimates have the same three terms as before, multiplied respectively by weights proportional to

\[
\frac{b(\tau)\Lambda(\tau)^2}{T},\qquad
\frac{b(\tau)\Lambda(\tau)^2R^2}{T^2},\qquad
\frac{b(\tau)\Lambda(\tau)^2R^{4/3}}{T^{4/3}},
\]

where b(tau) counts the squared active/inactive branching. Their prime-ideal Euler factors are respectively 1+O((Np)^(-2)), 1+O((Np)^(-2)), and 1+O((Np)^(-4/3)). All three sums converge. The row sectors are disjoint, so their energies add directly.

Consequently (2.6) and (3.4) hold over **every nonzero element row**, with the asterisk removed. All units, repeated good primes, and arbitrary bad-prime valuations are included. The proof also gives sharp norm balls and fixed Schwartz row profiles, retaining uniform smooth-test seminorms. The original coupled row-dependent covariance kernel is still a separate object.

### Explicit moving-auxiliary bounds

For a squarefree primary auxiliary q outside S, put Q=Nq and insert the original fourth-power twist. The exact identities are

\[
P_{A,B}(k;q)=P_{A,B}(kq^4),\qquad
\mathcal C_{A,B}(k;q)=\mathcal C_{A,B}(kq^4).
\]

No coprimality between the row and q is assumed. At an auxiliary prime with reflected exponent four, retain the negative choice, the positive squarefree choice, and the positive cube choice separately. Their pairs of squared amplitude and effective-length multiplier are

\[
((Np)^{-1},(Np)^2),\qquad (1,Np),\qquad
((Np)^{-1},(Np)^{-1}).
\]

Summing all row valuations and these allocations gives the stronger auxiliary factors 1, Q, Q^(2/3) in the three energy terms. With M=min(A,sqrt(B)) and delta=(2beta-2)/3, the resulting all-row estimates are

\[
\boxed{
\sum_{k\sim\mathcal H}|\mathcal C_{A,B}(k;q)|^2
\ll D^\epsilon\left[
\mathcal H A+\frac{Q\mathcal H^2 A}{B}M^{2\beta-1}
+Q^{2/3}\left(\frac{\mathcal H^2A^2}{B}\right)^{2/3}
\right],}
\tag{4.1}
\]

\[
\boxed{
\sum_{k\sim\mathcal H}|P_{A,B}(k;q)|^2
\ll D^\epsilon\left[
\mathcal H A+Q\mathcal H^2 A B^\delta
+Q^{2/3}\mathcal H^{4/3}A^{4/3}B^\delta
\right].}
\tag{4.2}
\]

The auxiliary may vary polynomially with D. At A=B=D, the sufficient row ranges are mathcal H <= D^((5-2beta)/4)/sqrt(Q) for the completion and mathcal H <= D^((5-2beta)/6)/sqrt(Q) for the literal polynomial, whenever the range contains mathcal H >= 1. Finite allocation counts and the resulting mild prime products cost a subpower; they are not falsely asserted to be uniformly bounded Euler products. These are positive norms for the stated auxiliary twist. They do not estimate the signed auxiliary average or the centered bilinear form with two independently corrected columns.

## 5. Every fixed moment: signed incidence regions

The complete general-order proof is [HERMITIAN_INCIDENCE.md](HERMITIAN_INCIDENCE.md). Its primary analytic premise is the source-pinned native second moment with uniform moving exclusions. An optional exponent beta in (1/2,1] denotes a separate uniform pointwise bound for the finite-order inverse family. Taking beta=1 uses elementary counting and adds no pointwise analytic premise.

For each nonempty subset I of the 2k tuple positions, let q_I contain exactly the primes appearing at those positions. These ideals are squarefree and pairwise coprime. Put

\[
m_I=|I|,\qquad e_I=\#(I\text{ on the left})-\#(I\text{ on the right}).
\]

If m_I is odd, its coefficient retains a Möbius sign. If also e_I is congruent to plus or minus one modulo six, that variable is itself a native sextic inverse factor. It can receive a second-moment bound even when its primes occur in three or more tuple entries. Odd quadratic patterns are not granted this input.

On a complete smooth incidence block Nq_I about Q_I, define

\[
L_1=\prod_{m_I=1}Q_I,\qquad
\Gamma=\prod_{m_I\ge3}Q_I^{m_I-2}.
\]

Choose the two largest eligible scales Q_J,Q_L. Write T_2=Q_JQ_L and let U be the product of the other odd-incidence scales. The theorem is

\[
\boxed{
|S_{\mathbf Q}|\ll HD^{k+\epsilon}
\sqrt{\frac{L_1}{\Gamma T_2}}\,U^{\beta-1}.}
\tag{5.1}
\]

Thus all complete blocks with L_1 <= Gamma T_2 U^(2(1-beta)) contribute at most the desired order HD^(k+epsilon). A smaller budget gives a quantitative power saving. Mellin separation of the original 2k smooth column tests occurs before any row inequality; its frequency costs are controlled by fixed seminorms.

The proof also gives an exact repeated-core criterion when the singleton variables are left unsplit, and controls the entire signed sector whose singleton primes occupy at most two tuple entries. The critical pair of correction exponents 1/2+1/2=1 is handled by a finite subpower estimate, not falsely declared absolutely convergent. A proved annular adapter covers both sharp rows and the Fourier-compact Schwartz majorant of PR #914.

### A sharp global-gcd theorem

Let T_R be the signed Hermitian contribution from tuples whose common gcd across all 2k entries has norm at least R. For rho=1+2(k-1)beta,

\[
\boxed{|T_R|\ll H D^{\rho+\epsilon}R^{1-\rho}.}
\tag{5.2}
\]

The proof uses the exact finite identity

\[
T_R=\sum_q^*w_R(q)\sum_u\varpi_D(u)\mathbf1_{(u,q)=1}
|A_u^{(q)}(D/Nq)|^{2k},\qquad
w_R(q)=\sum_{d\mid q,\ Nd\ge R}\mu_K(q/d).
\]

Only after this equality is an absolute value taken. The moving column exclusion remains in A^(q); it is not deleted as though a column restriction were a norm contraction.

The sufficient cutoff for diagonal size is independent of k:

\[
R\ge D^{(2\beta-1)/(2\beta)}.
\]

| Fourth-moment sector | From native M2 and counting, beta=1 | With additional uniform beta=7/8 premise |
|---|---:|---:|
| Common gcd across all four entries | R >= D^(1/2) | R >= D^(3/7) |
| One triple-incidence core, on complete smooth blocks | R >= D^(3/5) | R >= D^(9/17) |

The triple-core improvement uses that repeated ideal itself as one of the two inverse factors. Using only singleton factors gives the weaker cutoff D^(2/3) when beta=1. The global-gcd sector is distinct from a one-sided polynomial common-divisor norm tail; its new cutoff does not replace the older theorem for that different object.

## 6. An exact obstruction with the genuine coefficients

[CENTERED_NATIVE_SIGN.md](CENTERED_NATIVE_SIGN.md) proves that the correctly product-diagonal-centered A2 covariance can have either sign with the trivial finite-order ray datum and nonnegative fixed smooth factor weights.

The construction uses the ideals (53), (71), and (55)=(5)(11), all squarefree and pairwise coprime. A direct finite-field calculation gives a_1((p))=-1 for each inert rational prime p, so their coefficients are -1,-1,+1. A single fixed smooth window selects them with weights 1,1,t. The full A2 completion equals its squarefree coprime face exactly in this window.

On all six unit rows the three product columns have coefficients 2,-2t,-2t and their sextic symbols are one. The exact centered covariance is

\[
48t(t-2),
\]

which equals -36 at t=1/2 and +144 at t=3. This refutes universal positivity after the correct product-diagonal subtraction. It does not refute an asymptotic upper bound, and does not turn the entire signed first-Poisson expression into one of these individual centered blocks.

## 7. What is still required

At the balanced fourth-moment core, A=B=D and the first Poisson row scale is mathcal H about D^(3-theta). The all-row coupled-completion ranges D^(3/4) and D^(19/24), and the all-row literal polynomial range D^(19/36), are far smaller. The cutoff itself is uniform for every nonzero row at any norm, but that exact vanishing statement does not imply a corresponding quantitative bound for the surviving terms in the required long range. The moving auxiliary now has an explicit positive-norm envelope. Its signed average and the centered signed bilinear form with two independently corrected columns remain uncontrolled.

The sufficient strict off-diagonal estimate remains equation (6.9) of the parent [A2 completion note](../2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md): preserve its full signed b,f sum, its Möbius factor, all nonunit masks, the row-dependent coupled kernel, and strict product-column inequality, and prove |O_xi[v]| << H D^epsilon for the required balanced divisor weights. The uniformly bounded total dual diagonal was already removed exactly in PR #914; it must not be restored by an unsigned comparison.

For general k, when every repeated ideal is one, all 2k singleton scales are D. Equation (5.1) then returns only HD^(1+2(k-1)beta+epsilon). The new odd-incidence and core estimates do not supply the missing cancellation for that balanced region. The note identifies the exact limit of Hölder using the current one-variable inputs and a conditional interface describing what additional higher moments would unlock.

## 8. Sources and validation

| Role | Exact source |
|---|---|
| Parent signed diagonal and A2 arithmetic | PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103` |
| Moving-exclusion M2 and finite-order reciprocal adapter | PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1` |
| Coupled scalar, Ramanujan allocation, quadratic-cubic composition | PR #915, commit `9959364671f89b86f3992ec5ed5e19f804eb607b` |
| Imported theta and finite iteration interfaces | OpenAI/math, commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex` |

The exact dependency on the classical cusp coefficients is arXiv:2109.07463v3, equations (5.7), (5.13), and (5.14), with the source additive and conjugation normalizations checked explicitly. Its GRH-conditional main results are not used.

See [VALIDATION.md](VALIDATION.md) for the exact checks, review scope, and accepted corrections, and [PROVENANCE.json](PROVENANCE.json) for source and final-file hashes. Each mathematical note contains its hypotheses, normalization, proof, and remaining boundaries. Publication preserves proposed research; it does not promote these deductions into the integrated record.

The earlier frozen angular, all-cusp, cube-inverse, and exact-support notes describe their own narrower row and auxiliary scopes. The separate final ARBITRARY_ROW_MOMENTS.md supplies the quantitative all-row and single-auxiliary extension; its independent review is bound to that new source. The older boundary statements do not override this additional theorem. Their warning about the full signed covariance remains in force.
