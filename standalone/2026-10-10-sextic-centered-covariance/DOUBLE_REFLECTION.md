# Exact disappearance of the long all-negative standard-cusp component

**Status:** source-conditional exact analytic identity, proposed for independent review. The result is an exact support cutoff, stronger than a mean-square saving for this component. It uses the fixed angular reflection proved in centered_a2_attack.md, Sections 2–3, and the literal standard-cusp expression from PR #915. It does not use the angular zero-free corollary, either large sieve, or an unproved centered rank-two functional equation.

**Source pins:** OpenAI math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 build/paper2.tex; parent PR #914 0cc0428fedbbfc340044c7451b3d392c1da9a103; adjacent PR #915 9959364671f89b86f3992ec5ed5e19f804eb607b, NEGATIVE_BRANCH_DIRICHLET_SERIES.md (2.1)–(3.1), COUPLED_THETA_COMPLETION.md Sections 1–3 and 6, and REFLECTION_SCALAR_AUDIT.md (4.1)–(4.2).

**Exact scope:** the all-negative Ramanujan allocation \(a=g,\ e=f=1\), restricted to the complete standard-cusp coefficient face \(\ell=\lambda^{-3}nb^3,\ (nb,S)=1\). All squarefree \(n\) and all cube indices \(b\) are retained, including overlaps with \(g\). The outer rows \(k\) and the divisor \(g\) are squarefree primary and outside the fixed bad set. Noncoprime pairs \((k,g)>1\) are already zero in the original coupled sum. The angular order used in the new reflection is the fixed order \(+1\).

## 1. The exact inner series to which the second reflection applies

Put \(\alpha(z)=z/|z|\), \(\lambda=\sqrt{-3}\), and

\[
\vartheta(n)=\overline{\chi_n(\lambda)^2},\qquad
\vartheta^3=1
\]

on ideals outside \(S\). For a fixed ray character \(\rho\), define the finite periodic twist

\[
\Psi_{k,\rho}(n)=\rho(n)\vartheta(n)\chi_k(n)^3,
\]

with zero extension at \(S\) and at primes dividing \(k\). This is the finite part of the source completion; the angular factor is placed in its coefficient explicitly.

For a test \(U\), let

\[
\begin{aligned}
T_{1,U}(X;\Psi_{k,\rho})
={}&\sum_n^*\sum_b
\frac{\alpha(n)\gamma_2(n)\Psi_{k,\rho}(n)
      \alpha(b)^3\Psi_{k,\rho}(b)^3}
{\sqrt{Nn}\,Nb}\,
U(Nn(Nb)^3/X).                                         \tag{1.1}
\end{aligned}
\]

The primary-generator and excluded-prime conventions are those of the source. Since \(\vartheta^3=1\) and \(\chi_k(b)^9=\chi_k(b)^3\), including their nonunit zeros, (1.1) is exactly

\[
\sum_n^*\sum_b
\frac{\gamma_2(n)\rho(n)\vartheta(n)\alpha(n)\chi_k(n)^3
      \rho(b)^3\alpha(b)^3\chi_k(b)^3}
{\sqrt{Nn}\,Nb}\,
U(Nn(Nb)^3/X).                                         \tag{1.2}
\]

On the standard-cusp face, a fixed term of the source's first reflection has denominator \(c_0kg\), with \(c_0\) in a fixed finite family. Because \(N(\lambda^{-3})=1/27\), its inner all-negative sum is precisely (1.1) with

\[
U=\mathsf J V_*,\qquad
X=\frac{27N(c_0)^2(Nk)^2(Ng)^2}{B},                    \tag{1.3}
\]

where \(V_*(x)=\sqrt{x}\,W_2(x)\) is the original compactly supported test and \(\mathsf J\) is the source order-one gamma transform defined below.

The fixed finite ray expansion is performed before asserting (1.3). The first reflection's additive phase is a function of \(nb^3\) modulo a fixed \(S\)-supported ideal. On the standard face, \(nb^3\) is a unit at that ideal. Expanding that function in the characters of its finite unit group gives factors \(\rho(n)\rho(b)^3\). The supplementary factor satisfies \(\vartheta(b)^3=1\). All remaining fixed branch restrictions on \(g,k\) are handled by their prescribed ray splitting or finite character expansion. Hence no dependence on an individual \(n\) or \(b\) has been silently placed outside (1.1).

In particular, the full all-negative expression has the form of a fixed finite sum of

\[
\frac{R(k)}{\sqrt A}\sum_g^*
\frac{\mu(g)\eta(g)\alpha(g)^{-3}\chi_k(g)^3}{\sqrt{Ng}}
W_1(Ng/A)\,
T_{1,\mathsf JV_*}\!\left(
\frac{27N(c_0)^2(Nk)^2(Ng)^2}{B};\Psi_{k,\rho}\right).
                                                               \tag{1.4}
\]

The bounded row scalar \(R(k)\), fixed characters \(\eta,\rho\), and finite branch restrictions are exactly those supplied by PR #915. There is no mask \((g,nb)=1\). Its absence is essential: the negative term of the Ramanujan factor is present at every dual index.

## 2. The order-one weight transform is an involution on this test pair

For the Mellin convention \(\widehat V(s)=\int_0^\infty V(x)x^s\,dx/x\), write

\[
R_1(s)=\frac{\Gamma(5/6+s)\Gamma(7/6+s)}
{\Gamma(5/6-s)\Gamma(7/6-s)},\qquad
\mathfrak c=\frac{(2\pi)^4}{27}.
\]

Define

\[
(\mathsf JV)(x)=\frac1{2\pi i}\int_{(0)}
\widehat V(-s)R_1(s)(\mathfrak c x)^{-s}\,ds.             \tag{2.1}
\]

### Lemma 2.1. Exact kernel composition and the required Mellin strip

For \(V\in C_c^\infty((0,\infty))\), its transform satisfies

\[
\widehat{\mathsf JV}(s)
=\widehat V(-s)R_1(s)\mathfrak c^{-s},
\qquad \Re s>-5/6,                                    \tag{2.2}
\]

as a holomorphic identity, and

\[
\boxed{\mathsf J(\mathsf JV)=V.}                        \tag{2.3}
\]

For every \(0<a<5/6\), fixed logarithmic derivative order \(j\), and every \(L>0\),

\[
|(x\partial_x)^j(\mathsf JV)(x)|
\ll_{a,j,L,V}\min(x^a,x^{-L}).                          \tag{2.4}
\]

**Proof.** In (2.1), the first possible numerator gamma pole to the left is at \(s=-5/6\); the reciprocal gamma factors are entire. The compact smooth test has an entire Mellin transform with arbitrarily rapid vertical decay on every fixed strip. Stirling's formula shows that the gamma quotient contributes only a polynomial on such vertical lines. Move the contour to \(\Re s=-a\) for the small-\(x\) bound and to any positive \(\Re s=L\) for the large-\(x\) bound. No pole is crossed in the stated range. The same proof applies to logarithmic derivatives. Mellin inversion gives (2.2).

On, for example, the line \(\Re s=3/4\), both \(\widehat{\mathsf JV}(-s)\) and (2.2) are defined, because \(-3/4>-5/6\). Their product in the second transform is

\[
\widehat{\mathsf JV}(-s)R_1(s)\mathfrak c^{-s}
=\widehat V(s)R_1(-s)R_1(s)=\widehat V(s).
\]

Here \(R_1(-s)R_1(s)=1\) as a meromorphic identity, with all cancellations interpreted analytically. The integrals converge absolutely on the chosen line. Mellin inversion of the original test proves (2.3). This proves the involution for this exact pair of tests; it does not assume a Mellin transform outside the strip (2.2). \(\square\)

### Lemma 2.2. The second reflection is legitimate for \(U=\mathsf JV_*\)

The fixed-angular reflection of centered_a2_attack.md, Theorem 3.3, with order \(r=+1\), applies to (1.1) with \(U=\mathsf JV_*\). Its transformed weight is exactly \(V_*\), with no additional residue.

**Proof.** In the Dirichlet-series Mellin formula, the input test is evaluated at Mellin argument \(s-1/2\). Begin, for example, at \(\Re s=5/4\), where the squarefree/cube product series is absolutely convergent. Shift to \(\Re s=-1/4\), where its reflected Dirichlet series is absolutely convergent. Throughout this strip,

\[
-3/4\le\Re(s-1/2)\le3/4,
\]

which stays strictly to the right of the first pole \(-5/6\) in (2.2). The completed coefficient series is entire by the nonzero pure horizontal derivative argument; no constant Fourier mode survives at either cusp. The rapid Mellin decay on these fixed strips, together with the source's finite-order strip bounds, justifies the shift. The proof of Theorem 3.3 therefore applies to this transformed input, without requiring compact support of \(U\) itself. The outgoing kernel is \(\mathsf JU\), which is \(V_*\) by Lemma 2.1. No pole or constant-mode residue is crossed. \(\square\)

## 3. Exact reflected formula and support cutoff

In the second reflection the twist \(\Psi_{k,\rho}\) has local exponent \(j=3\) at every prime of \(k\). All these primes are active. Its denominator has the form \(c_1k\), with \(c_1\) in a fixed finite family depending only on the fixed ray data. The local transformed factor is

\[
B_{p,3}(x)=\chi_p(x)^{-5}=\chi_p(x),                     \tag{3.1}
\]

including its zero at \(p\mid x\). No moving factor \(g\) is present in this second conductor.

### Theorem 3.1. The all-negative standard face vanishes beyond \(Ng\asymp\sqrt B\)

The inner expression in (1.4) equals the fixed finite sum

\[
\boxed{
\sum_{\jmath}C_{1,\jmath}(k)
\sum_{0\ne\ell\in\lambda^{-4}\mathcal O}
\frac{d_{\sigma_\jmath}(\ell)\overline{\alpha(\ell)}}{\sqrt{N\ell}}
\psi_\jmath(\lambda^4\ell)\chi_k(\lambda^4\ell)
V_*\!\left(
\frac{27N(c_0)^2}{N(c_{1,\jmath})^2}
\frac{N\ell\,(Ng)^2}{B}\right).
}                                                       \tag{3.2}
\]

The scalars and cusp data are precisely the source's finite local reflection at \(r=+1,j=3\). In particular the exact scalar is

\[
C_{1,\jmath}(k)=\frac{i}{81}\alpha(c_{1,\jmath}k)^2
\widehat\phi_\jmath(h_0)\overline{\kappa_{0,\jmath}}
\prod_{p\mid k}\chi_p(\sigma_p)^{-2}\omega_{p,3},          \tag{3.3}
\]

where \(\sigma_p=\lambda^2c_{1,\jmath}k/p\), \(\epsilon_p=-\lambda^{-5}(c_{1,\jmath}k/p)^{-2}\), and

\[
\omega_{p,3}=\chi_p(-1)^3\gamma_3(p)\gamma_5(p)
\chi_p(\epsilon_p)^{-5}.
\]

These local arguments are units; all nonunit zeros occur in the displayed characters, as in the source.

Let \(v_1=\sup\operatorname{supp}V_*\). There is a fixed finite constant \(C_*>0\), depending only on \(S\), the initial fixed ray characters, and \(v_1\), such that every inner sum in (1.4) is identically zero whenever

\[
\boxed{(Ng)^2>C_*B.}                                   \tag{3.4}
\]

Consequently, if the outer weight is supported in \(Na\in[a_1A,a_2A]\) with \(a_1>0\), the complete all-negative standard-cusp component vanishes for every squarefree primary row whenever

\[
A^2>(C_*/a_1^2)B.                                      \tag{3.5}
\]

In particular it vanishes identically at balanced \(A=B=D\) for all sufficiently large \(D\), uniformly in the row norm.

**Proof.** Apply Lemma 2.2 and the order-\(+1\) reflection. The original \(X\) in (1.3), divided by the square norm of the second conductor, gives

\[
\frac{N\ell\,X}{N(c_1k)^2}
=\frac{27N(c_0)^2}{N(c_1)^2}\frac{N\ell\,(Ng)^2}{B}.
\]

The row norm cancels exactly. Equations (3.1), (2.3), and the literal scalar in the fixed-angular reflection give (3.2)–(3.3), with the finite cusp and additive families retained. This is an identity before any absolute-value estimate.

Every nonzero \(\ell\in\lambda^{-4}\mathcal O\) has \(N\ell\ge1/81\). For the finite collection of first- and second-reflection branches, put

\[
a_*:=\min_{c_0,c_1}\frac{27N(c_0)^2}{N(c_1)^2}>0,
\qquad C_*:=\frac{81v_1}{a_*}.
\]

If \((Ng)^2>C_*B\), the argument of \(V_*\) in every summand of (3.2) is strictly larger than \(v_1\). Every summand is zero. There is no zero Fourier mode or residue to add, by Lemma 2.2. This proves (3.4), and the outer support gives (3.5). The strict inequality avoids an endpoint convention. Pairs \((k,g)>1\) were already zero before reflection, so the final component statement includes them without extending the branch formula to their different local exponents. \(\square\)

## 4. Interpretation and exact boundary

The angular change matters analytically. After the first reflection the standard theta coefficient has angular type \(+1\). Keeping that angle permits a second scalar-theta reflection at the moving quadratic twist. The second local transformation is \(j=3\mapsto1\), its conductor contains \(k\) but no \(g\), and its gamma transform inverts the first one. The compact original weight then supplies the exact support cutoff.

This does not rest on canceling two unrelated Euler factors in independent Mellin variables. In the two-variable representation of PR #915, the reflection is applied to the entire completed numerator with the actual transformed test, before any bound or contour manipulation of the reciprocal \(g\)-series. It retains every cube term.

The theorem removes a specific previously troublesome corner at balanced scales, uniformly even for long rows. It is not the full balanced theorem. If \(e\) or \(f\) is nontrivial, the surviving \(n,b'\) sum has zero masks at these primes in its squarefree part but does not generally have the corresponding cube-part exclusions. Directly identifying it with (1.1) would insert missing masks. A repeated-reflection treatment of those split blocks must restore the exact cube-prime terms or reunite the positive Ramanujan choices before reflection. Other cusp components require their literal scalar realization, rather than replacing their coefficients by the standard face.

The full fourth moment, the generalized hierarchy, and RH remain unproved here. The new exact contribution is (3.2), with its support consequence (3.4).

