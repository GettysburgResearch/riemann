# A second theta reflection kills the completed negative branch beyond its support

Status: proposed reviewable theorem, conditional on the theta automorphy and cusp expansions imported in the October 5 primary source. The argument below proves a new exact support statement for the standard infinity-cusp face. It does not prove the full fourth moment or the generalized moment hierarchy. The cube completion is retained throughout.

Scope: all squarefree primary rows k outside a fixed set S; the explicitly specified standard infinity-cusp component of the coupled reflection; all fixed ray characters rho in its finite decomposition. Constants depend on the fixed ray modulus, S, the original compact smooth weight, and the fixed scale constant in the inherited negative-branch identity. They are independent of k and of the outer divisor g.

Exact dependencies: PR #915 at `9959364671f89b86f3992ec5ed5e19f804eb607b`, particularly `NEGATIVE_BRANCH_DIRICHLET_SERIES.md`, equation (3.1), and `COUPLED_THETA_COMPLETION.md`, equations (2.1), (2.4), and (6.1). Primary analytic source: OpenAI/math `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`, equations `eq:theta-cusp-automorphy`, `eq:theta-cusp-coordinates`, `eq:cusp-coefficient-definition`, `eq:theta-weight`, `eq:bessel-mellin`, and the derivative-Mellin argument following `eq:ray-mellin`. No unproved zero-free estimate for an angular Hecke L-function is used.

What was actually run: direct symbolic derivation of the opposite horizontal derivative, scale constants, Mellin transform composition, and support cutoff. No numerical evidence is used to justify the theorem.

Smallest remaining gap for the full target: the remaining divisor allocations and removal of cube completion still require a joint estimate. The theorem is an exact cancellation of one completed component; it does not permit discarding cube terms or separately bounding an uncompleted face by this zero.

## 1. Normalizations

Write K=Q(omega), O=Z[omega], lambda=1+2omega=i sqrt(3), N(a)=|a|^2, and alpha(a)=a/|a|. Let d_0(ell) be the Fourier coefficients of the conjugate cubic theta function in the primary source. On the standard good-primary face,

\[
\ell=\lambda^{-3}nb^3,\qquad
 d_0(\ell)=3^{5/2}\sqrt{Nb}\,\vartheta(n)\gamma_2(n),
\quad \vartheta(n)=\overline{\chi_n(\lambda)^2},
\]

with n squarefree, n,b primary, and (nb,S)=1. In particular alpha(lambda^{-3})=i and N(lambda^{-3})=1/27.

Fix V in C_c^infinity((0,infinity)); write supp(V) subset [u,R], with 0<u<R<infinity. In the inherited reflection V is the original compact input V_*(x)=sqrt(x)W_2(x). Set

\[
\mathcal R(t)=
\frac{\Gamma(7/6+t)\Gamma(5/6+t)}
     {\Gamma(7/6-t)\Gamma(5/6-t)},
\qquad \mathcal R(t)\mathcal R(-t)=1.
\]

The inherited transformed weight is

\[
F(x)=V^\sharp(x)=\frac1{2\pi i}\int_{(0)}
 \widehat V(-t)\mathcal R(t)
 \left(\frac{(2\pi)^4 x}{27}\right)^{-t}dt.
\tag{1.1}
\]

The factor 27 in this formula matters. For a theta series indexed directly by its Fourier frequency ell, rather than by nb^3, define

\[
(\mathscr H_0 U)(x)=\frac1{2\pi i}\int_{(0)}
 \widehat U(-t)\mathcal R(t)((2\pi)^4x)^{-t}dt.
\tag{1.2}
\]

Then F(x)=(H_0 V)(x/27), and therefore

\[
\boxed{\mathscr H_0F(x)=V(27x).}
\tag{1.3}
\]

This is an exact Mellin identity, not a heuristic cancellation of oscillatory kernels. On Re(t)>-5/6,

\[
\widehat F(t)=\widehat V(-t)\mathcal R(t)
       ((2\pi)^4/27)^{-t}.
\tag{1.4}
\]

To justify this domain, move the defining Mellin contour to Re(t)=-a for any 0<a<5/6, giving F(x)=O_a(x^a) as x tends to zero; there are no numerator gamma poles before -5/6. At infinity one can shift to any positive line. Smooth compact support gives rapid vertical decay of V-hat, and Stirling bounds control the gamma quotient. Mellin inversion first proves (1.4) on a common line and then throughout the indicated half-plane. Substitution into (1.2) gives (1.3).

## 2. The opposite derivative has the same kernel and the opposite angular factor

Let phi:O->C be periodic modulo q, supported on good primary elements. Form the finite periodic twist

\[
\Theta_\phi(z,v)=\sum_{\ell\ne0}d_0(\ell)
 \phi(\lambda^3\ell)vK_{1/3}(4\pi|\ell|v)
 \breve e(\ell z),
\quad \breve e(\ell z)=e^{2\pi i(\ell z+\overline{\ell z})}.
\]

The coefficient is understood to be zero unless lambda^3 ell is in O. Finite Fourier inversion, with the conventions of the source, writes Theta_phi as a finite linear combination of translates bar(theta(z+lambda^2 h/q,v)); the horizontal derivative also makes any constant term irrelevant.

For each h, reduce lambda^2 h/q=a_h/c_h with (a_h,c_h)=1, and choose g_h in SL_2(O) with first column (a_h,c_h). We may choose a denominator c_h dividing q, so

\[
Nc_h\le Nq.
\tag{2.1}
\]

Use the source decomposition g_h=g_{1,h}H_h, with g_{1,h} in the level-three group and H_h represented by one of the fixed cusp expansions. Put kappa_h=kappa(g_{1,h}), and let d_{sigma_h} be the corresponding conjugate-theta coefficients. The coordinate formula of the source gives, at z=0,

\[
\partial_z z'=0,\qquad
\partial_z\overline{z'}=-\frac1{\overline{c_h}^{\,2}v^2},
\qquad \partial_zv'=0.
\tag{2.2}
\]

Consequently the derivative in z transforms to

\[
-\overline{\kappa_h}\,(\overline{c_h}v)^{-2}
                  \partial_{\overline{z'}}.
\tag{2.3}
\]

This is the conjugate-coordinate companion of the source's calculation with partial_bar-z. It changes the source scalar bar(alpha(c_h))^2 to alpha(c_h)^2 and swaps the input angular coefficient alpha(ell) to bar(alpha(ell')). The two gamma factors stay the same, since the Bessel order and the absolute frequency power stay the same.

For Re(s)>1 define

\[
G^+_\phi(s)=\sum_{\ell\ne0}
 d_0(\ell)\phi(\lambda^3\ell)\alpha(\ell)(N\ell)^{-s}.
\]

The Mellin transform of partial_z Theta_phi is

\[
J^+_\phi(s)=\frac{i\,\Gamma(s+1/3)\Gamma(s+2/3)}
                   {4(2\pi)^{2s}}G^+_\phi(s).
\tag{2.4}
\]

It is entire: at infinity use the differentiated Fourier series, and at zero use each rational-cusp transformation (2.3). The horizontal derivative removes every constant mode, leaving exponential decay at both ends for each fixed periodic twist. This is the same entire-continuation argument as in the imported source, now with the other horizontal derivative.

Write

\[
G^-_h(s)=\sum_{\ell'\ne0}
 d_{\sigma_h}(\ell')\overline{\alpha(\ell')}
 \breve e(-\delta'_h\ell'/c_h)(N\ell')^{-s},
\]

where delta'_h is the lower-right entry of g_h. Applying (2.3), changing v to (Nc_h v)^(-1), and using (2.4) gives

\[
\begin{split}
G^+_\phi(1/2+t)
={}&-\sum_{h\bmod q}\widehat\phi(h)
 \overline{\kappa_h}\alpha(c_h)^2
 (Nc_h)^{-2t}(2\pi)^{4t}\mathcal R(t)^{-1}
 G^-_h(1/2-t).
\end{split}
\tag{2.5}
\]

This is an exact functional equation for this finite periodic theta twist. No angular Hecke L-function is introduced or divided by.

## 3. Exact transformed support

Define

\[
S^+_\phi(X;F)=\sum_{\ell\ne0}
 \frac{d_0(\ell)\phi(\lambda^3\ell)\alpha(\ell)}{\sqrt{N\ell}}
 F(N\ell/X).
\tag{3.1}
\]

### Theorem 3.1

For F=V-sharp from (1.1), every X>0 has the exact expansion

\[
\boxed{
\begin{split}
S^+_\phi(X;V^\sharp)
={}&-\sum_{h\bmod q}\widehat\phi(h)
 \overline{\kappa_h}\alpha(c_h)^2
 \sum_{\ell'\ne0}
 \frac{d_{\sigma_h}(\ell')\overline{\alpha(\ell')}}{\sqrt{N\ell'}}
 \breve e(-\delta'_h\ell'/c_h)
 V\!\left(\frac{27N\ell'X}{(Nc_h)^2}\right).
\end{split}}
\tag{3.2}
\]

In particular,

\[
\boxed{X>3R(Nq)^2\quad\Longrightarrow\quad
 S^+_\phi(X;V^\sharp)=0.}
\tag{3.3}
\]

**Proof.** Mellin-invert (3.1) on Re(t)=3/4. The Dirichlet series G^+_phi(1/2+t) is absolutely convergent there. Shift to Re(t)=-3/4: G^+ is entire, while F-hat is holomorphic in Re(t)>-5/6. Polynomial growth in the strip follows by the same Mellin splitting, functional equation, and Phragmen-Lindelof argument as the source. Rapid decay of F-hat on these fixed vertical lines makes the shift legitimate. Thus no pole or constant-mode residue is crossed.

Insert (2.5), replace t by -t, and interchange the dual Dirichlet series on Re(t)=3/4, where G^-_h(1/2+t) is absolutely convergent. Formula (1.4) and R(t)R(-t)=1 turn the resulting kernel exactly into V(27x). Mellin inversion gives (3.2).

The nonzero dual frequencies belong to lambda^(-4)O, so N(ell')>=1/81. By (2.1), every argument of V on the right side of (3.2) is at least X/(3(Nq)^2). It exceeds the support endpoint R under (3.3). Every summand is then zero. The right side is actually a finite sum for each h by compact support. This proves the exact vanishing. QED.

The number of additive translates can grow with Nq. The vanishing proof does not bound or sum their absolute values; each individual dual sum is already zero on the same domain. Therefore it causes no conductor loss.

## 4. Application to the inherited all-negative branch

Fix a ray character rho from the inherited standard-face decomposition and a squarefree primary k outside S. Choose a fixed S-supported modulus M such that the function

\[
\phi_k(m)=\mathbf1_{m\text{ good and primary}}\rho(m)\chi_k(m)^3
\tag{4.1}
\]

is periodic modulo q=Mk. This retains the literal zero of chi_k^3 at every prime of k and the zeros at S. Such a fixed M exists by the definitions of the good-primary condition and the fixed ray character. Notice that the supplementary theta factor vartheta appears in d_0, so it must not be inserted a second time into (4.1).

This is a periodic selection of actual Fourier modes, not a nonperiodic deletion of the inconvenient terms. Indeed, put m=lambda^3 ell. The good-prime support theorem for the source theta coefficients says that, whenever d_0(ell) is nonzero and (m,S)=1, every good-prime exponent in m is 0 or 1 modulo 3. The good-primary condition then gives the unique representation m=n b^3 with n squarefree and n,b primary and prime to S: divide every prime exponent by 3, putting its remainder in n. The remaining unit must be 1, since m,n,b are primary and the only primary unit is 1. The condition (m,S)=1 also fixes the ramified normalization ell=lambda^(-3)m, so it excludes all other ramified/unit faces through this same finite periodic mask. Conversely every inherited good-primary n,b term has precisely this Fourier index and survives the mask unless the actual row character vanishes. Therefore (4.1) selects exactly the inherited standard infinity-cusp face in (4.2), while retaining the entire periodic-theta realization needed for the second reflection.

For g outside S and c>0 the fixed scale constant of the inherited equation (3.1), let

\[
\begin{split}
I_{k,g}:=\sum_{n\text{ squarefree}}\sum_b
 &\frac{\gamma_2(n)\rho(n)\vartheta(n)\alpha(n)\chi_k(n)^3
       \rho(b)^3\alpha(b)^3\chi_k(b)^3}
      {\sqrt{Nn}\,Nb}\,
 V^\sharp\!\left(\frac{cNn(Nb)^3B}{(Ng)^2(Nk)^2}\right).
\end{split}
\tag{4.2}
\]

The sums use the exact good-primary restrictions from the inherited standard face. There is no condition that g be coprime to n or b; introducing one would invalidate this identification.

Set

\[
X=\frac{(Ng)^2(Nk)^2}{27cB}.
\tag{4.3}
\]

Using alpha(lambda^(-3))=i and the theta coefficient formula gives, term by term,

\[
\boxed{S^+_{\phi_k}(X;V^\sharp)=81i\,I_{k,g}.}
\tag{4.4}
\]

The factor 81 combines 3^(5/2) from d_0 and 3^(3/2) from 1/sqrt(N(lambda^(-3))); the unit i is the angular factor. In particular, Theorem 3.1 proves

\[
\boxed{(Ng)^2>81cR(NM)^2B\quad\Longrightarrow\quad I_{k,g}=0.}
\tag{4.5}
\]

The bound is uniform in the row k. It is an identity, not an asymptotic estimate. All moving k Euler masks remain inside phi_k throughout.

The inherited all-negative branch multiplies I_{k,g} by

\[
\frac{\mu_K(g)\eta(g)\overline{\alpha(g)}^3\chi_k(g)^3}
 {\sqrt A\sqrt{Ng}}W_1(Ng/A)
\]

and sums over squarefree g. Thus the completed standard-face negative branch can be restricted exactly to

\[
Ng\le C\sqrt B,\qquad C=9\sqrt{cR}\,NM.
\tag{4.6}
\]

If supp(W_1) subset [u_1,v_1] with u_1>0, then this entire completed component is zero whenever

\[
u_1^2A^2>81cR(NM)^2B.
\tag{4.7}
\]

In particular, at A=B=D the component vanishes for all sufficiently large D, uniformly in every row k. The former long-dual bound H^2 A^2/B for this component was a loss from applying a quadratic large sieve before the available second theta reflection. It does not represent an unavoidable arithmetic term.

## 5. What is and is not removed

This calculation establishes the analytic meaning of the formal T(s,Psi^+) in the negative-branch note: it is the opposite-horizontal-derivative periodic theta series with finite Fourier multiplier rho*chi_k^3, with the inherited vartheta factor already in d_0. Its angular +1 coefficient is allowed because it comes from partial_z. The completed Dirichlet series is entire by the derivative-cusp argument. This does not supply an inverse bound for the separate angular L(w,chi^-) factor in the two-variable representation.

The exact support theorem requires the full n,b cube completion and the exact inherited V-sharp. A cutoff in b, a single squarefree face b=1, a separately truncated n dyad, or a replacement of V-sharp by its pointwise majorant need not vanish. The cancellation therefore has to be used before any dyadic absolute-value bound that destroys the completed theta series.

More explicitly, let Psi^+_{k,rho}=rho*vartheta*alpha^2*chi_k^3, with all inherited zero extensions. The completed Dirichlet series defined formally in the negative-branch note obeys, initially for Re(s)>1,

\[
\boxed{G^+_{\phi_k}(s)
  =i3^{5/2}27^s\,\mathcal T(s,\Psi^+_{k,\rho}).}
\tag{5.1}
\]

Equivalently, G^+_{phi_k}(1/2+t)=81i 27^t T(1/2+t,Psi^+_{k,rho}). The proof is the same coefficient calculation as (4.4), with the Dirichlet exponent s retained: the cube exponent is 1/2-3s, and vartheta(b)^3=1. By Section 2, G^+ is entire. The factor i3^(5/2)27^s has no zeros or poles, so (5.1) continues the exact source-defined T(s,Psi^+) to an entire function. This closes the angular-continuation interface for this particular coefficient and character class. It does not assert the same result for arbitrary angular multipliers or arbitrary divisor deformations.

The result removes the entire completed standard-face all-negative component in the balanced large-scale regime. General two-term Ramanujan allocations can retain a divisor d by the periodic condition d|ell and should be treated before splitting primes between squarefree and cube indices. Their finite-periodic transform and row-averaged estimates are separate work. No claim about the full moment or 17/24 follows from (4.5) alone.

## 6. Why this does not lower the conductor of the reunited whole

At a good prime p of norm q, the unnormalized Ramanujan factor is R_p(x)=-1+q*1_{x=0} on O/(p). Its normalized additive Fourier transform is exactly

\[
\frac1q\sum_{x\bmod p}R_p(x)e(-hx/p)
  =\begin{cases}0,&h=0,\\1,&h\ne0.\end{cases}
\tag{6.1}
\]

The constant negative allocation contributes -1 only at h=0; the positive term q*1_{x=0} contributes +1 at every h. Thus their inactive h=0 transforms cancel exactly, while every active residue survives. On reuniting all prime allocations before the second reflection, this restores activity at every prime of the original divisor a. The full conductor can therefore return to a*k. The support pruning of a separated completed component is valid, but it does not itself prove that the reunited complete sum has smaller conductor. The remaining moment problem must exploit further structure of the active part, rather than iterating the two reciprocal theta transforms and treating the resulting involution as a new saving.
