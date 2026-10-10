# Fixed angular types through the canonical second-moment argument

Status: proposed reviewable extension of the imported October 5 argument, conditional on that source's arithmetic identities, theta automorphy, quadratic large sieve, smooth separation, and finite descent. The new adapters are proved below. The all-order diagonal moment and the boundary 17/24 are not proved. This extension supplies a second moment and a fixed zero-free half-plane for a larger character class; it does not improve the zeta boundary.

Scope: a fixed integer infinity type r, a fixed finite ray character rho, and primary good ideals over Q(omega). The inverse full-row second moment below excludes r=-1. The canonical Gauss family excludes its own parameter r=+1. Their sign difference is established explicitly in Section 5. The fixed-row bound and zero-free consequence cover every integer r, using ordinary conjugation for the one exceptional inverse type. Constants may depend on r and rho. Moving exclusions and row characters retain their literal zeros.

Exact primary source: OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, locally in the October 7 import. Required interfaces: `eq:convert1`, `eq:quotient`, `eq:crt-a`, `prop:poisson-reduction`, `prop:canonical`, `eq:T`, `prop:R`, `lem:cube-reduction`, `prop:transfer`, and its two-Poisson proof. The pure-derivative calculation extends the source's `eq:theta-cusp-coordinates`, `eq:bessel-mellin`, and `eq:theta-mellin-functional-equation`. Transfer stability also follows directly from PR #913 at `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `FOURTH_MOMENT_ATTACK.md`, Lemma 3.1.

## 1. Pure higher horizontal derivatives have no unwanted lower terms

For m>=1 use the source cusp coordinates

\[
z'=-\delta'/c-\frac{\bar z}{c^2(v^2+z\bar z)},\quad
\overline{z'}=-\overline{\delta'}/\bar c-
             \frac{z}{\bar c^2(v^2+z\bar z)},\quad
v'=\frac{v}{Nc(v^2+z\bar z)}.
\tag{1.1}
\]

At z=0 the exact pure-derivative identity is

\[
\boxed{
\partial_z^m\{F(z',v')\}\big|_{z=0}
 =\left(-\frac1{\bar c^2v^2}\right)^m
 (\partial_{\bar z'}^mF)(-\delta'/c,1/(Nc\,v)).}
\tag{1.2}
\]

The companion formula exchanges z and bar-z and c and bar-c. To prove (1.2), compute the pure Taylor coefficient in z while setting bar-z=0. Then z' and v' are constant, while bar-z' is affine in z with the displayed slope. Equivalently, every discrepancy from these three simplified formulas is divisible by bar-z; taking only z derivatives cannot remove that factor. Thus no height derivative, mixed derivative, or lower horizontal derivative is generated. This is a local chain-rule identity and does not require F to be holomorphic.

For the plus angular component define

\[
G_m^+(s)=\sum_{\ell\ne0}d(\ell)\phi(\ell)\alpha(\ell)^m(N\ell)^{-s},
\]

with a finite periodic multiplier phi and an actual theta cusp coefficient. Use

\[
J_m^+(s)=\int_0^\infty
   (\partial_z^m\Theta_\phi)(0,v)v^{2s+m-2}dv.
\]

Initially in the right absolute-convergence half-plane, the Bessel Mellin integral gives

\[
\boxed{J_m^+(s)=
\frac{i^m\Gamma(s+m/2-1/6)\Gamma(s+m/2+1/6)}
     {4(2\pi)^{2s}}G_m^+(s).}
\tag{1.3}
\]

Indeed the differentiated Fourier mode is (2*pi*i*ell)^m times v*K_(1/3)(4*pi*|ell|v). The v exponent in the integrand is 2s+m-1, producing |ell|^(-2s-m), and ell^m restores exactly alpha(ell)^m(Nell)^(-s). The scalar simplifies to i^m/[4(2*pi)^(2s)]. For the minus angular component use partial_bar-z^m and alpha(ell)^(-m), with the same scalar and gamma factors.

Every m>=1 annihilates the constant mode at every cusp. The same exponential-decay argument as in the source therefore makes J_m^+ and J_m^- entire for each fixed periodic twist. Division by the gamma factors yields entire completed angular Dirichlet series. The argument fails in this form for m=0, which is deliberately excluded.

For each translate with denominator c, (1.2) and v -> (Nc*v)^(-1) give the Mellin factor

\[
\boxed{(-1)^m\alpha(c)^{2m}(Nc)^{1-2s}}
\tag{1.4}
\]

for a plus input, and its conjugate angular phase for a minus input. The norm exponent is independent of m: the factor (Nc)^(-m) in bar-c^(-2m) cancels the additional m in the v-Mellin exponent. At s=1/2+t the common reflection kernel is

\[
\mathcal R_m(t)=
 \frac{\Gamma((m+1)/2-1/6+t)\Gamma((m+1)/2+1/6+t)}
      {\Gamma((m+1)/2-1/6-t)\Gamma((m+1)/2+1/6-t)}.
\tag{1.5}
\]

Its first numerator pole to the left is at -m/2-1/3, which is at most -5/6 for m>=1. Thus the source's kernel shift to Re(t)=-1/4, rapid tail bounds, all required fixed smooth seminorms, and Mellin separation remain available. In norm(nb^3) coordinates the fixed scale factor is still (2*pi)^4/27, because the primal Fourier frequency remains lambda^(-3)nb^3. For m different from 1 one must use R_m, not the inherited R_1 kernel.

## 2. The enlarged coefficient family

For a fixed integer r and fixed finite ray character rho define

\[
\nu_{r,\rho}(n)=\alpha(n)^r\rho(n),\qquad
 a_{r,\rho}(n)=\alpha(n)^{r-1}\gamma_2(n)\rho(n)
\tag{2.1}
\]

on primary ideals outside S, extended by zero where required. Alpha is multiplicative on these chosen primary generators. Therefore a_(r,rho) has exactly the source CRT relation

\[
a_{r,\rho}(ab)=a_{r,\rho}(a)a_{r,\rho}(b)\chi_b(a)^4
\quad((a,b)=1).
\tag{2.2}
\]

Put

\[
\Psi_{r;k,f}(n)=\alpha(n)^r\rho(n)\chi_n(k)\chi_n(f)^4
\]

and define T_r(X;k,f) by the literal source completed sum T(X;Psi). Its squarefree theta coefficient has angular degree r-1, and its cube coefficient has degree 3(r-1). If r is not 1, put m=|r-1|>=1. The full theta realization uses the m-th plus or minus derivative from Section 1, as appropriate; its Fourier multiplier is the finite periodic function

\[
\phi_{k,f}(n)=\mathbf1_{n\text{ good primary}}
             \chi_n(\lambda)^2\rho(n)\chi_n(k)\chi_n(f)^4.
\tag{2.3}
\]

The angular factor is supplied by the derivative, so it is not falsely absorbed into this finite multiplier.


Here is the complete primal Mellin normalization. Put j=r-1, m=|j|, and let D_j mean partial_z^m for j>0 and partial_bar-z^m for j<0. Let mathcal T_r(s;k,f) be the exact Dirichlet series attached to the literal source completed T_r. Because alpha(lambda^(-3))=i, its raw Fourier Dirichlet series satisfies

\[
G_j(s)=i^j3^{5/2}27^s\mathcal T_r(s;k,f).
\tag{2.4}
\]

Consequently the Mellin transform using D_j and the power v^(2s+m-2) is

\[
\boxed{
J_j(s)=\frac{3^{5/2}}4 i^{m+j}
 \left(\frac{27}{(2\pi)^2}\right)^s
 \Gamma(s+m/2-1/6)\Gamma(s+m/2+1/6)
 \mathcal T_r(s;k,f).}
\tag{2.5}
\]

The unit i^(m+j) is 1 for j<0 and (-1)^j for j>0. Both its sign and the factor 27 are explicit. Thus the normalization used in the completed mean-square adapter below differs from the primary source only by a fixed unit and the displayed higher-order gamma factors.

## 3. Completed mean square at fixed angular degree

### Proposition 3.1

For every fixed r!=1, rho, epsilon>0, and C_0>=1 there is a finite J such that

\[
\boxed{
\sum_{0<Nk\ll\mathcal H}|T_r(X;k,f)|^2
 \ll D^\epsilon\|W\|_{C^J(I)}^2
 \left(\mathcal H+\frac{\mathcal H^2Nf}{X}\right)}
\tag{3.1}
\]

for 1<=Hcal,X,Nf<=D^(C_0), squarefree primary f outside S, and W smooth and supported in the fixed compact I. The constants may depend on r,rho,S,I,epsilon,C_0; no moving index is included in the constant.

**Proof adapter to the imported Proposition R.** Realize T_r using (2.3) and the order m derivative. At every good active prime the finite Fourier and cubic automorphy calculation is unchanged, so its local factor is still B_(p,j)(ell) from `eq:theta-local-factors`. In particular a row prime of local exponent j=1 still produces exactly the quadratic character chi_p^3. Formula (1.4) replaces only the unit-modulus archimedean scalar. For each grouped set of Fourier residues, its denominator is fixed; its extra phase factors as a row-only unit phase times a phase determined by the frozen auxiliary/active-set labels. It does not introduce a column-dependent row coefficient. The fixed-ray uniformity lemma for the cusp coefficients and additive phases is unchanged.

The normalized dual coefficient differs only by a fixed power of alpha(ell), of modulus one. Thus the source coefficient bounds, ramified decay, moving-prime masks, and effective scales Y_iota are unchanged. The transformed weight uses (1.5); the bounds from Section 1 give exactly the same fixed smooth majorants used in `eq:theta-separated-columns`. The quadratic large sieve therefore yields the same bounds a_iota^2(Hcal_0+Y_iota) in `eq:prepared-mean-square`, with the same a_iota and Y_iota estimates.

Finally the source decomposes every row k=u_0 s v^2 and uses the exact character identity chi_n(k)chi_n(f)^4=chi_n(u_0s)chi_n(fv^2)^4. This identity is independent of the angular coefficient, so its treatment of every repeated-prime row and its convergent v sum apply without change. This proves (3.1), with J enlarged for the fixed kernel order m. QED.

## 4. Cube inversion and both Poisson steps close in the same angular class

Cube inversion is an exact multiplicative identity for the full Psi_(r;k,f). Its added coefficient is

\[
\frac{\mu(b)\alpha(b)^{3(r-1)}\rho(b)^3\chi_b(k)^3
                \mathbf1_{(b,f)=1}}{Nb}.
\tag{4.1}
\]

All its nonzero character factors have modulus one. Therefore the source cube cutoff, short-cube bound from (3.1), and long-cube regrouping retain their precise norms and row zeros. In particular the canonical cube-reduction inequality has the same Sigma and the same smaller column scales X/(Nb)^3.

For the transfer, write a_(r,rho)(n)=a_(0,rho)(n)v(n) with v(n)=alpha(n)^r. The exact residual-coefficient identity in PR #913 Lemma 3.1 gives, after the two Poisson steps and complete signed regrouping,

\[
v(r_0 f'n_1)\overline{v(r_0 f'n_2)}
 =\alpha(n_1)^r\overline{\alpha(n_2)^r}.
\tag{4.2}
\]

The common factor alpha(r_0f')^r cancels exactly. Hence the child has the same angular r. In the first paired Gauss identity the finite-ray function rho*G is expanded in characters while alpha(n)^r remains outside that finite expansion. In the second paired identity the same rule applies to rho_1*G^(-1). No growing list of angular modes appears.

The inherited signed local cancellation, f'|k' support, geometric scale identities, and outer normalizer are therefore identical. The extra exclusion is removed using (2.2), and its exterior alpha(d)^r is again a unit phase. This proves the source transfer inequality at each fixed r, including the exact child-range conditions; it does not rely on an arbitrary-coefficient extension of the theta estimate.

### Proposition 4.1: fixed-angular canonical theorem

Define

\[
\mathcal E_r(\mathcal H,X,F;\rho,W)=\frac1{XF}
 \sum_{F\le Nf<2F}^{*}\sum_{0<Nk\le\mathcal H}
 \left|\sum_n^*a_{r,\rho}(n)\chi_n(k)\chi_n(f)^4
                   W(Nn/X)\right|^2.
\]

For fixed r!=1, kappa>0, C_0>=1 and epsilon>0, if

\[
\mathcal H,X,F\ge1,\qquad \Sigma=XF\le D^{C_0},\qquad
\mathcal H\le\Sigma D^{-\kappa},
\]

then

\[
\boxed{\mathcal E_r(\mathcal H,X,F;\rho,W)
 \ll D^\epsilon\Sigma\|W\|_{C^J(I)}^2.}
\tag{4.3}
\]

**Proof.** The imported finite induction `sec:canonical-proof` uses precisely the cube-reduction inequality, the transfer inequality with the source child-scale restrictions, and bounded-row counting. Sections 3-4 supply those same inequalities in the fixed-r family, with no changed geometric exponent. Counting uses |a_(r,rho)|<=1. Use the same finite number ceil(C_0/kappa) of induction steps and enlarge the finitely many derivative orders and constants to include the fixed r. This reproduces every hypothesis and conclusion of the source induction and proves (4.3). QED.

## 5. The angular inverse second moment and a limited zero-free consequence

For a fixed integer r different from -1, define the actual inverse family

\[
A_{u,r,\rho}(D;W)=\sum_{(n,S)=1}\mu_K(n)\alpha(n)^r\rho(n)
                         \chi_n(u)W(Nn/D).
\tag{5.1}
\]

### Theorem 5.1

For every fixed 0<theta<=1/10, H=D^(1+theta), and epsilon>0,

\[
\boxed{\sum_{0<Nu\le H}|A_{u,r,\rho}(D;W)|^2
       \ll D^{1+\epsilon}H\,\|W\|_{C^J(I)}^2.}
\tag{5.2}
\]

Here J is a finite integer depending only on the displayed fixed data, theta and epsilon. The sum includes all nonzero rows, with no deletion of sixth powers or local zeros.

**Proof.** The exact orientation of the source initial paired identity matters. For nu=alpha^r*rho, its `eq:initial-paired-gauss` becomes

\[
\begin{split}
&\mu(z_1)\mu(z_2)\overline{\nu(z_1)}\nu(z_2)
       \gamma(\overline{\chi_{z_1}}\chi_{z_2})\\
&\qquad=\sum_\xi c_\xi
       a_{-r,\xi}(z_1)\overline{a_{-r,\xi}(z_2)}.
\end{split}
\tag{5.2a}
\]

To verify this, expand only the finite-ray expression bar(rho(t))*G(t^(-1)) as in the source and retain the phase bar(alpha(z_1))^r*alpha(z_2)^r. Multiplication of the source r=0 identity by that phase is exactly (5.2a). Thus the child angular parameter is -r, and Section 4 shows that transfer preserves that parameter exactly. The common divisor phases also cancel against their conjugates at the two subsequent source splittings. No angular derivative of a row weight occurs: this phase stays on the column coefficients.

Since r!=-1, the parameter -r is not +1, so Proposition 4.1 applies. All absolute coefficient and zero-frequency estimates are unchanged. The initial scales remain

\[
\mathcal H\ll D^{1-\theta}/B^2,\qquad
\Sigma=D/B,\qquad \mathcal H/\Sigma\ll D^{-\theta}.
\]

Apply (4.3) with kappa=theta/2 and the source's polynomial scale ceiling, then the exact source Poisson comparison. Its diagonal and nonzero-frequency bounds give (5.2). Every smooth separation in those steps is controlled by finitely many C^J seminorms, and the fixed-r kernel changes only the necessary finite value of J. Bounded/empty scales are handled by the same counting argument. QED.

The source sixth-power-row extraction uses multiplicativity and |nu(p)|<=1, rather than finite order, in its prime-puncturing recursion. It therefore applies to (5.1). Together with (5.2) it gives for every compact smooth W

\[
\boxed{A_{1,r,\rho}(D;W)\ll_{r,\rho,S,I,\epsilon}
D^{11/12+\epsilon}\|W\|_{C^{J_1}(I)}.}
\tag{5.3}
\]

The index J_1 is finite. Indeed the extraction combines (5.2) with its own counting/prime-puncturing error, which uses only the supremum norm of the same W. It gives the source inequality

\[
|A_{1,r,\rho}(D;W)|^2
 \ll\|W\|_{C^{J_1}(I)}^2
   \left[D^{1+\epsilon_0}H^{5/6}+D^2H^{-1/3}\right].
\tag{5.3a}
\]

Taking H=D^(1+theta), and choosing fixed theta and epsilon_0 sufficiently small in terms of the final epsilon, proves (5.3) with finite seminorm control. The prime-puncturing identities use complete multiplicativity, its zero convention, and |nu(p)|=1; no finite-order hypothesis remains in that step.

For the remaining inverse type r=-1 and row u=1, ordinary complex conjugation gives

\[
A_{1,-1,\rho}(D;W)
 =\overline{A_{1,+1,\overline\rho}(D;\overline W)}.
\tag{5.3b}
\]

The r=+1 second moment was just proved, so (5.3) follows also for r=-1, with the same finite seminorm convention. This is only a fixed-row identity: it does not claim the missing r=-1 full-row second moment.

Consequently, for every integer fixed r, the ordinary reciprocal Dirichlet series

\[
L_S(s,\alpha^r\rho)^{-1}
   =\sum_n\mu_K(n)\alpha(n)^r\rho(n)(Nn)^{-s}
\quad(\Re s>1)
\]

extends holomorphically to Re(s)>11/12 by a smooth dyadic partition and (5.3). For normal convergence on a compact subset of that half-plane, apply (5.3) to W_s(x)=W(x)x^(-s): its finitely many C^(J_1) seminorms are bounded uniformly on the compact set. The dyadic scale factors then give a uniformly convergent geometric majorant. The continued reciprocal agrees with 1/L on Re(s)>1 and hence throughout their common meromorphic domain. Thus, conditional on the imported inputs, every fixed integer angular-type Hecke L-function in this normalization is zero-free in that half-plane. For r=+3 and r=-3 this applies to the two angular character types exposed by the reunited Euler product. The r=0 case recovers the source simplified bound. This argument does not transplant the separate stronger upstream 7/8 proof, nor improve the already available zeta boundary.

The missing full-row case r=-1 is a limit of this second-moment adapter, not a counterexample or a claim about its zeros. Its canonical parameter is +1, giving angular degree zero with theta constant terms and a different polar analysis. The m>=1 proof cannot simply be used for that missing mean square. Equation (5.3b) handles only the fixed-row consequence.

## 6. Conductor-uniform reciprocal control for the two angular types +/-3

The new fixed-character zero-free statement can be upgraded to a conductor-uniform reciprocal estimate on its fixed interior. The proof below does not claim that the implied constant in (5.3) was uniform.

### Lemma 6.1: polynomial growth at fixed odd angular type

Let r be a fixed odd integer. Let nu be a unitary Hecke character of type r, presented on principal ideals outside its finite modulus q as nu((z))=alpha(z)^r psi(z), with psi periodic modulo q and extended by zero on its nonunits. Enlarge q by the fixed primary modulus if necessary. Unit invariance of the ideal character requires psi(epsilon*z)=epsilon^(-r)psi(z); in particular psi(-z)=-psi(z). Then

\[
\boxed{\left|\sum_{N\mathfrak a\le x}\nu(\mathfrak a)\right|
 \ll_r\sqrt{xN\mathfrak q}+N\mathfrak q.}
\tag{6.1}
\]

**Proof.** Every ideal has six generators, and alpha(z)^r psi(z) is invariant under their six unit choices. Thus the ideal sum is one sixth of the corresponding sum over nonzero Eisenstein lattice points in the disk |z|<=sqrt(x). The Eisenstein ring is a principal ideal domain, so write q=(q_0). Partition the plane into translates of a half-open fundamental parallelogram for the ideal lattice q. Multiplication by q_0 rotates and scales O without changing its shape, so each cell has diameter O(sqrt(Nq)) and contains exactly Nq representatives of O/q. The constants are consequently independent of the orientation of q. The sum of psi over such a complete cell is zero, by its oddness.

For a full cell with center z_0 at distance at least a fixed multiple of sqrt(Nq) from the origin, subtract the constant alpha(z_0)^r. The angular function satisfies |gradient(alpha(z)^r)|<=C_r/|z| away from zero. Hence this cell contributes at most C_r (Nq)^(3/2)/|z_0|. Centers in the dyadic annulus of radius T>=C sqrt(Nq) number O(T^2/Nq). Their total error is O_r(sqrt(Nq)*T); summing the geometric annuli to T<=sqrt(x) gives O_r(sqrt(xNq)). The finitely many near-origin cells contribute O(Nq).

There are O(sqrt(x/Nq)+1) cells meeting the boundary of the disk, and each contains Nq lattice points. Their total contribution is O(sqrt(xNq)+Nq). These bounds also cover x<Nq by counting. Division by six proves (6.1). QED.

Partial summation therefore gives, for every fixed a>1/2,

\[
\boxed{|L(s,\nu)|\ll_{r,a}N\mathfrak q\,(1+|s|)
         \quad(\Re s\ge a).}
\tag{6.2}
\]

The series is continued by the partial-summation integral into Re(s)>1/2. This continuation agrees with the ordinary Hecke L-function by equality in Re(s)>1. It is holomorphic there; at nonzero odd angular type there is no principal-character pole.

### Theorem 6.2: the angular reciprocal at a moving finite conductor

Assume the source-dependent conclusions of Theorem 5.1 and its fixed-row extraction for r=+3 and r=-3. Put beta=11/12. For either fixed r, every delta>0 and epsilon>0,

\[
\boxed{|L(\sigma+it,\nu)^{-1}|
 \ll_{r,\delta,\epsilon}
 [N\mathfrak q\,(2+|t|)]^\epsilon,
 \qquad \sigma\ge\beta+\delta,}
\tag{6.3}
\]

uniformly over the finite-order part of nu and every finite modulus q through which the finite multiplier psi and its zero extensions factor. The full angular coefficient itself is not periodic. Imprimitive Euler masks and all excluded primes are allowed and must remain in q; enlarging a modulus by the fixed primary modulus changes its norm by only a fixed factor.

**Proof.** Theorem 5.1 and its smooth dyadic consequence (5.3), applied separately to each finite character, prove that every such L-function is zero-free in Re(s)>beta. This family-wide zero-free domain, rather than a uniform constant in (5.3), is the input here. Imprimitive Euler factors have their zeros on Re(s)=0, so their addition preserves the half-plane.

Choose the analytic logarithm g(s)=log L(s,nu) on this simply connected half-plane, agreeing with the Euler logarithm to the right of one. Lemma 6.1 gives a polynomial growth bound uniform in q on every fixed smaller half-plane. Borel--Caratheodory on fixed disks centered at 2+it, with left edge strictly between beta and a fixed a>beta, yields

\[
|g(a+it)|\ll_{r,a,\beta}\log[N\mathfrak q(2+|t|)].
\tag{6.4}
\]

The disk-center value is uniformly bounded by the Euler logarithm, and the real part of g is bounded above by the logarithm of (6.2). On any fixed b>1 the Euler logarithm directly gives |g(b+it)|=O_b(1).

Fix t_0 and apply the three-lines theorem on a<=Re(s)<=b to g(s) exp((s-it_0)^2). Its boundary suprema are O(log Q) and O(1), where Q=Nq(2+|t_0|); the Gaussian absorbs the extra logarithmic growth when t moves away from t_0. For a<sigma<b this gives

\[
|g(\sigma+it_0)|\ll(\log Q)^\omega,
\qquad \omega=(b-\sigma)/(b-a)<1.
\tag{6.5}
\]

If beta+delta>1, the Euler product already gives the desired bound uniformly on that half-plane. If beta+delta=1, prove the estimate first with the smaller margin delta/2, which includes this line. Otherwise choose a=beta+delta/2<1 and fixed b>1. Then the disks centered at 2 used above have their target line strictly to the left of 2, and omega is uniformly bounded away from one in the remaining strip. Exponentiation gives exp(C(log Q)^omega)<=C_epsilon Q^epsilon. For sigma>=b use the Euler product directly. This proves (6.3). The logarithm and polynomial growth argument can be applied to the literal imprimitive L-function itself, so no moving Euler factor is deleted. QED.

In particular the denominator chi^-_(k,eta)=eta*bar(alpha)^3*chi_k^3 in the reunited Euler product has finite modulus norm O_(eta,S)(Nk), and (6.3) proves

\[
|L_S(w,\chi^-_{k,\eta})^{-1}|
 \ll_{\eta,S,\delta,\epsilon}
 [Nk(2+|\Im w|)]^\epsilon
 \quad(\Re w\ge11/12+\delta).
\tag{6.6}
\]

This is an explicit conductor-uniform angular reciprocal interface. Its domain stops at 11/12 plus a fixed margin; it does not reach the critical line.

## 7. Remaining analytic boundaries

The fixed-angular canonical theorem is still confined to Hcal<=Sigma D^(-kappa). It does not change the higher-moment initial ratio D^(k-1-theta). Its character class remains one completely multiplicative angular twist; it does not include the divisor deformation E_(k,n)(w,v) in the reunited Ramanujan series.

Section 6 supplies the separate polynomial-growth/logarithm argument and proves the conductor-uniform reciprocal estimate for the needed angular types +/-3 in Re(w)>11/12. It does not control the divisor deformation E_(k,n)(w,v), nor justify moving that deformed squarefree Gauss series through its new v=1 divisor. The remaining analytic product must still be treated jointly.
