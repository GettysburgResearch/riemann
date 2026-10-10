# A finite-cusp reflection and an exact cutoff for every reunited negative divisor

**Status:** new source-conditional analytic identity, proposed for independent review. The native argument below closes the finite cusp data needed for a second horizontal-derivative reflection. It proves an exact support cutoff before any positive/negative component is bounded. It then combines that cutoff with the separately reviewed angular component estimate to enlarge its standard-cusp range.

**Source pins:** OpenAI math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 build/paper2.tex; PR #915 9959364671f89b86f3992ec5ed5e19f804eb607b, COUPLED_THETA_COMPLETION.md and REFLECTION_SCALAR_AUDIT.md; fixed-angular reflection and component estimate in centered_a2_attack.md, frozen reviewed snapshot bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a. The standard all-negative specialization is independently recorded in double_reflection_attack.md.

**Exact imported inputs:** the source's scalar theta automorphy on \(\Gamma(3)\), the \(\mathrm{SL}_2(\mathbb Z)\) and \(\mathbb Z+3\mathcal O\) invariances, its three displayed cusp expansions, their coefficient/support bounds, and the already identified full mixed \(j=1,4\) reflection scalar. The finite-cusp closure, second Mellin transformation, and cutoff are proved here. No norm bound for a growing scattering matrix is assumed.

## 1. A common Fourier lattice for the finite cusp family

Let \(F(w)=\overline{\theta(w)}\), where \(w=(z,v)\). For \(\gamma\in\Gamma(3)\), the source gives

\[
F(\gamma w)=\overline{\kappa(\gamma)}F(w),\qquad
\kappa(\gamma)\in\mu_3.                                \tag{1.1}
\]

Write \(F_A(w)=F(Aw)\) for \(A\in\mathrm{SL}_2(\mathcal O)\).

### Lemma 1.1. Finite closure with a uniform nonzero Fourier gap

There is a fixed finite collection of functions \(F_\tau\) such that every \(F_A\) is a scalar of modulus one times one of these functions. Each \(F_\tau\) has an expansion

\[
F_\tau(z,v)=C_\tau(v)+
\sum_{0\ne\ell\in\lambda^{-4}\mathcal O}
d_\tau(\ell)vK_{1/3}(4\pi|\ell|v)\breve e(\ell z),        \tag{1.2}
\]

with polynomially bounded coefficients on the source's cubic support, up to fixed unit rotations. Its coefficient Dirichlet series is absolutely convergent for \(\Re s>1\). The constant term \(C_\tau(v)\) is independent of \(z\). Every nonzero frequency has

\[
N\ell\ge1/81.                                         \tag{1.3}
\]

**Proof.** Finiteness as a function family up to scalars follows already from the finite index of \(\Gamma(3)\), since (1.1) is scalar. We verify the Fourier expansions using the source's exact congruence reduction, without assuming that every coset has the standard coefficient sequence.

Take \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\). Right multiplication by \(D_u=\operatorname{diag}(u,u^{-1})\), for a unit \(u\), makes \(a\equiv1\pmod3\) when \(\lambda\mid c\), and makes \(c\equiv1\pmod3\) otherwise. The appropriate entry is a unit modulo \(3\), and the six units of \(\mathcal O\) represent the six units modulo \(3\).

After that normalization, right multiply by \(T_t=\left(\begin{smallmatrix}1&t\\0&1\end{smallmatrix}\right)\), choosing \(t\) from a fixed set of representatives modulo \(3\). If \(\lambda\mid c\), choose \(t\) to make the upper-right entry zero modulo \(3\). The determinant makes the lower-right entry one. If \((c,\lambda)=1\), choose \(t\) to make the lower-right entry zero; the upper-right entry is then \(-1\) modulo \(3\). Thus

\[
AD_uT_t\equiv H\pmod3,
\]

where \(H\) belongs to the fixed collection used in the source's cusp reduction:

\[
I,\qquad
\begin{pmatrix}1&0\\\lambda&1\end{pmatrix},\quad
\begin{pmatrix}1&0\\-\lambda&1\end{pmatrix},\qquad
\begin{pmatrix}u_0&-1\\1&0\end{pmatrix}
\quad(u_0\bmod3).
\]

In the middle case \(v_\lambda(c)=1\), its residue modulo \(3\) is \(\lambda\) or \(-\lambda\). Set \(\gamma=AD_uT_tH^{-1}\in\Gamma(3)\). Then

\[
A=\gamma H T_{-t}D_u^{-1}.                             \tag{1.4}
\]

Choose the actual representatives \(H_\tau\) from this fixed finite set of matrices \(H T_{-t}D_u^{-1}\), retaining one representative for each left coset of \(\Gamma(3)\). Define \(F_\tau(w)=F(H_\tau w)\). This choice is used in the matrix factorization in Lemma 2.1.

The source's \(\mathrm{SL}_2(\mathbb Z)\) invariance and translation invariance reduce \(F(Hw)\) to its three explicitly given cusp functions. This can also be checked directly: the upper-right representatives are \(T_{u_0}S\), so translations reduce \(u_0\) to \(0,\omega,-\omega\), followed by the \(\mathrm{SL}_2(\mathbb Z)\) inversion. For the two lower-left representatives, use \(\lambda=1+2\omega\), remove an integral lower translation, and then a \(3\mathcal O\) lower translation. The latter lies in \(\Gamma(3)\) and has multiplier \((c/1)_3=1\). The result is one of the same two nontrivial cusp representatives, up to an integral lower translation.

The right factor in (1.4) acts by \(z\mapsto u^{-2}z-t\) and leaves \(v\) unchanged. It only rotates Fourier frequencies by a unit and multiplies their coefficients by a fixed translation phase. The source's three expansions use \(\lambda^{-4}\mathcal O\), which is invariant under units. Their support and coefficient bounds are unchanged in magnitude. The choices of \(u,t,H\) are finite, proving (1.2)–(1.3).

To check the stated absolute-convergence domain explicitly, the source bounds a coefficient at \(\ell=u\lambda^mnb^3\) by a constant times \(3^{m/6}|b|\), with \(m\ge-4\) and \(n\) squarefree. For \(\sigma>1\), its absolute Dirichlet series is bounded by

\[
\left(\sum_{m\ge-4}3^{m(1/6-\sigma)}\right)
\left(\sum_n^*(Nn)^{-\sigma}\right)
\left(\sum_b(Nb)^{1/2-3\sigma}\right)<\infty.
\]

The unit rotations and translation phases preserve this bound. No equality between \(d_+,d_-\), and \(d_0\) was used. \(\square\)

## 2. A second reflection for an arbitrary finite periodic frequency multiplier

Let \(P:\mathcal O\to\mathbb C\) be periodic modulo a nonzero ideal \((q)\), and put

\[
S_{F_\tau,P,U}(X)=
\sum_{0\ne\ell\in\lambda^{-4}\mathcal O}
\frac{d_\tau(\ell)\alpha(\ell)}{\sqrt{N\ell}}
P(\lambda^4\ell)U(N\ell/X).                            \tag{2.1}
\]

Define the frequency-normalized gamma transform

\[
(\mathsf J_0U)(x)=\frac1{2\pi i}\int
\widehat U(-s)
\frac{\Gamma(5/6+s)\Gamma(7/6+s)}
{\Gamma(5/6-s)\Gamma(7/6-s)}
\bigl((2\pi)^4x\bigr)^{-s}\,ds.                        \tag{2.2}
\]

The contour is zero for compact smooth \(U\); for \(U=\mathsf JV_*\) below, it can be \(3/4\). Here \(\mathsf J\) is the source transform, whose scale constant is \((2\pi)^4/27\).

### Lemma 2.1. Exact finite Fourier reflection

For each finite Fourier translate of \(P\), let \(a_j/c_j\) be its reduced shift, with \(c_j\ne0\), and choose

\[
g_j=\begin{pmatrix}a_j&b_j\\c_j&d_j\end{pmatrix}
\in\mathrm{SL}_2(\mathcal O).
\]

Then \(S_{F_\tau,P,U}(X)\) is the finite sum of expressions

\[
\boxed{
-\widehat P(j)\,\zeta_j\alpha(c_j)^2
\sum_{\ell'\ne0}
\frac{d_{\tau_j}(\ell')\overline{\alpha(\ell')}}{\sqrt{N\ell'}}
\breve e(-d_j\ell'/c_j)
(\mathsf J_0U)\!\left(\frac{N\ell'X}{N(c_j)^2}\right),
}                                                       \tag{2.3}
\]

where \(|\zeta_j|=1\), \(\tau_j\) belongs to the fixed family of Lemma 1.1, and

\[
N(c_j)\le Nq.                                         \tag{2.4}
\]

The number of finite Fourier translates may depend on \(q\). The cusp family and the lattice gap do not.

**Proof.** With the source's additive character \(e\), finite Fourier inversion of \(P(x)\) uses \(e(xj/q)\). Since \(x=\lambda^4\ell\), its corresponding horizontal translate is

\[
z\mapsto z+\lambda^3j/q.
\]

Its reduced denominator \(c_j\) divides \(q\), up to a unit, proving (2.4). The zero shift is represented by \(a_j=0,c_j=1\), so it also satisfies this bound.

Write \(F_\tau(w)=F(H_\tau w)\) using a fixed representative. Factor \(H_\tau g_j=\gamma_jH_{\tau_j}\) with \(\gamma_j\in\Gamma(3)\), using the fixed finite coset family. Then

\[
F_\tau(z+a_j/c_j,v)
=\overline{\kappa(\gamma_j)}
F_{\tau_j}\bigl(g_j^{-1}(z+a_j/c_j,v)\bigr).
\]

Any further fixed scalar needed to choose the representatives is included in \(\zeta_j\). The archimedean inversion is \(g_j\), whose bottom-left entry is the reduced denominator \(c_j\); it is not \(H_\tau g_j\).

Take the pure derivative \(\partial_z\) at \(z=0\). The exact cusp-jet formula gives

\[
-\alpha(c_j)^2N(c_j)^{-1}v^{-2}
\partial_{\bar z}F_{\tau_j}
\left(-d_j/c_j,\frac1{N(c_j)v}\right).
\]

Both derivatives kill their constant Fourier modes. Mellin integration with \(v^{2s-1}\,dv\) contributes \(N(c_j)^{1-2s}\). In the frequency normalization of (2.1), the Bessel integral on the initial side is

\[
\frac{i}{4(2\pi)^{2s}}
\Gamma(s+1/2-1/6)\Gamma(s+1/2+1/6)
\sum_{\ell\ne0}d_\tau(\ell)\alpha(\ell)(N\ell)^{-s}.
\]

The opposite derivative gives the same prefactor and \(\overline{\alpha(\ell)}\). Taking the ratio at \(s\) and \(1-s\) produces

\[
-\zeta_j\alpha(c_j)^2N(c_j)^{1-2s}(2\pi)^{4s-2}
\frac{G(1-s)}{G(s)},
\qquad G(s)=\Gamma(s+1/2-1/6)\Gamma(s+1/2+1/6).
\]

Setting the smoothing Mellin variable to \(s-1/2\) gives (2.2)–(2.3). There is no factor \(27\) in (2.2), because both sides are sums on the Fourier lattice, without replacing \(\ell\) by \(\lambda^{-3}nb^3\).

Lemma 1.1 gives absolute convergence of each coefficient Dirichlet series for \(\Re s>1\). The finite cusp inversion gives exponential decay at both height ends after differentiation, hence an entire Mellin transform. The same strip argument as for the fixed-angular reflection justifies the contour shift. This proves the identity for compact smooth \(U\). Its extension to \(U=\mathsf JV_*\) is proved next. \(\square\)

### Lemma 2.2. The exact outgoing test is \(V_*(27x)\)

For compact smooth \(V_*\), (2.3) applies with \(U=\mathsf JV_*\), and

\[
\boxed{\mathsf J_0(\mathsf JV_*)(x)=V_*(27x).}           \tag{2.5}
\]

No polar term is added.

**Proof.** The Mellin transform of \(\mathsf JV_*\) is

\[
\widehat{\mathsf JV_*}(s)
=\widehat V_*(-s)R_1(s)
\left(\frac{(2\pi)^4}{27}\right)^{-s},
\qquad \Re s>-5/6,
\]

where \(R_1\) is the gamma quotient in (2.2). This follows by shifting the test contour up to the first possible pole at \(-5/6\), as proved in double_reflection_attack.md, Lemma 2.1. In the reflection shift, take the coefficient-series variable from \(\Re s=5/4\) to \(-1/4\). The smoothing Mellin argument stays in \([-3/4,3/4]\), strictly inside its holomorphy strip. The derivative kills every constant mode. There is no pole crossing or extra residue.

On the dual test contour \(\Re u=3/4\), the two gamma quotients cancel, while their constants give

\[
\widehat{\mathsf JV_*}(-u)R_1(u)(2\pi)^{-4u}
=\widehat V_*(u)27^{-u}.
\]

Mellin inversion proves (2.5). The fixed factor \(27\) is compulsory: the source transform and the frequency-normalized transform have different scale constants. \(\square\)

## 3. Reunite the positive Ramanujan terms before the second reflection

For squarefree \(a\), the exact local product satisfies

\[
\prod_{p\mid a}(Np)^{-1/2}
\bigl(-1+Np\,\mathbf1_{p\mid x}\bigr)
=\sum_{hg=a}\mu(g)\sqrt{\frac{Nh}{Ng}}\,
\mathbf1_{h\mid x}.                                   \tag{3.1}
\]

The factors \(h,g\) are squarefree and coprime. The label \(g\) records every negative choice, while \(h\) keeps the two positive possibilities reunited. This identity holds for every frequency, including all nonunit overlaps.

After the exact outer Gauss cancellation of PR #915, a fixed ray branch of the coupled reflection for \(a=hg\) is a bounded row scalar times

\[
\begin{aligned}
&A^{-1/2}\mu(g)\eta(hg)\alpha(hg)^{-3}
\chi_k(hg)^3\sqrt{Nh/Ng}\,W_1(N(hg)/A)\\
&\quad\times
S_{F_\sigma,P_{k,h},\mathsf JV_*}\!\left(
\frac{N(c_0)^2(Nk)^2(Nh)^2(Ng)^2}{B}\right),            \tag{3.2}
\end{aligned}
\]

where \(c_0\) ranges over a fixed finite family and

\[
P_{k,h}(x)=\psi(x)\chi_k(x)^3\mathbf1_{h\mid x}\Pi(x).   \tag{3.3}
\]

The source's fixed-ray additive CRT gives \(\psi\) a fixed finite period supported on \(S\). That periodicity is retained in this formula and in the choice of \(M\) below.

Here \(\Pi=1\) retains the entire cusp spectrum. Any fixed periodic projection at the bad primes is also permitted. In particular the standard face of \(d_0\) is selected by

\[
\Pi_{\mathrm{std}}(x)=
\mathbf1_{x\equiv\lambda\ (\lambda^3)}
\prod_{p\in S,\ p\nmid\lambda}\mathbf1_{p\nmid x}.        \tag{3.4}
\]

Indeed \(x=\lambda^4\ell\). On the source cubic support \(\ell=u\lambda^mnb^3\), the primary \(n,b\) are coprime to \(\lambda\). The congruence in (3.4) says \(x/\lambda\equiv1\pmod3\): it forces \(m=-3\) and \(u\equiv1\pmod3\). The unit residues are distinct modulo \(3\), so \(u=1\). The other factors say \((nb,S)=1\). Thus (3.4) is exactly the desired finite periodic projection, without any condition involving \(g\).

Choose a fixed \(S\)-supported nonzero \(M\) divisible by the periods of \(\psi\) and \(\Pi\). Since \(k,h\) are squarefree outside \(S\), the multiplier (3.3) is periodic modulo

\[
q=Mkh,\qquad Nq=N(M)NkNh.                              \tag{3.5}
\]

The original nonzero branch has \((k,hg)=1\); pairs failing this are already zero in the original coupled sum. The branch data may depend on fixed ray classes of \(k,h,g\); they are fixed before (3.2). The modulus bound (3.5) is uniform over that finite family.

### Theorem 3.1. Exact reunited-divisor cutoff at every cusp

There is a fixed constant \(C_*>0\), depending only on the fixed ray data, bad set, and upper endpoint of the support of \(V_*\), such that every reunited term (3.2) is identically zero whenever

\[
\boxed{(Ng)^2>C_*B.}                                   \tag{3.6}
\]

This holds at every source cusp, and also after any fixed periodic projection \(\Pi\), including the standard projection (3.4). It is uniform in \(k,h\) and uses no restriction on the row norm.

**Proof.** Apply Lemmas 2.1–2.2 to (3.2). Every resulting test argument is

\[
27\frac{N\ell'\,N(c_0)^2(Nk)^2(Nh)^2(Ng)^2}
{B\,N(c_j)^2}.
\]

By (2.4) and (3.5), \(N(c_j)\le N(M)NkNh\). Every nonzero frequency satisfies (1.3). The displayed argument is at least

\[
\frac{N(c_0)^2}{3N(M)^2}\frac{(Ng)^2}{B}.                \tag{3.7}
\]

The finite \(c_0\)-family has a positive minimum norm. If \(v_1=\sup\operatorname{supp}V_*\), take

\[
C_*=\frac{3N(M)^2v_1}{\min_{c_0}N(c_0)^2}.
\]

Then (3.6) places every test argument strictly beyond its support. Every term is zero, independently of the size or the \(\ell^1\)-norm of the finite Fourier expansion of \(P\). This is why no growing scattering-matrix norm estimate is needed for the cutoff. There is no constant mode or residue to restore, by Lemma 2.2. \(\square\)

The theorem concerns the reunited \(h,g\) block. It does not assert that an individual split \(e,f,g\) term vanishes; those terms can cancel when its positive choices are reunited.

## 4. A smooth exact restriction and the improved standard-cusp range

Choose a fixed smooth function \(\zeta\) that is one on \([0,1]\) and zero on \([2,\infty)\). Multiplying each reunited term by

\[
\zeta\!\left(\frac{Ng}{\sqrt{C_*B}}\right)               \tag{4.1}
\]

does not change the complete coupled reflection, by Theorem 3.1. Only after this exact operation, split \(h=ef\) by the original frequency-dependent positive allocations \(p\mid n\) and \(p\nmid n,\ p\mid b\). The resulting \(e,f,g\) expansion is the original one with the extra smooth factor (4.1). Summing it recovers the original reflected sum exactly.

On a smooth \(g\)-dyad, this extra test has uniform rescaled derivative bounds. All nonempty modified blocks have

\[
G\ll\sqrt B.                                          \tag{4.2}
\]

The scalar and quadratic–cubic estimates of centered_a2_attack.md, Theorem 7.1, therefore apply without a sharp cutoff or a changed character coefficient. The ratio \(Ng/G\) is unchanged after \(g=dg'\) and the scale replacement \(G\mapsto G/Nd\), so its smooth control also survives the moving-mask proof there.

### Corollary 4.1. Standard-cusp mean square up to \(H=D^{19/24}\)

At balanced \(A=B=D\), the complete standard-cusp reflected face satisfies

\[
\boxed{
\sum_{k\sim H}^*|\mathcal C^{(0)}_{D,D}(k)|^2
\ll D^\epsilon
\left[HD+H^2D^{5/12}+H^{4/3}D^{2/3}\right].
}                                                       \tag{4.3}
\]

The target \(D^{2+\epsilon}\) consequently holds on that entire specified face for

\[
\boxed{1\le H\le D^{19/24}.}                           \tag{4.4}
\]

**Proof.** Apply the reviewed smooth component estimate

\[
D^\epsilon G^{-1/6}
\left[HE+Y+(EY)^{2/3}\right],\qquad
Y=\frac{H^2EG^2}{DF},\quad EFG\asymp D,
\]

to the modified components just defined. As before,

\[
Y\asymp H^2G/F^2,\qquad EY\asymp H^2D/F^3.
\]

The first term is at most \(HD\). The second is now at most

\[
H^2G^{5/6}/F^2\ll H^2D^{5/12},
\]

by (4.2). The third is at most \(H^{4/3}D^{2/3}\). Sum the logarithmically many smooth blocks and the fixed ray branches by Minkowski, costing only \(D^\epsilon\). This proves (4.3); inserting \(H\le D^{19/24}\) proves (4.4).

More generally, if the scalar exponent is \(1/2<\beta\le1\), the same calculation gives

\[
D^\epsilon\left[HD+H^2D^{\beta-1/2}
+H^{4/3}D^{2/3}\right],
\qquad H\le D^{(5-2\beta)/4}.
\]

The upper restriction on \(\beta\) ensures that the third term does not grow with \(G\). Here the independently derived value is \(\beta=11/12\). \(\square\)

## 5. What closes, and what remains open

The second scalar reflection has a fixed finite cusp family and a proved common Fourier gap. For this support question, it also handles the entire moving finite multiplier, including \(h\mid\lambda^4\ell\) and the bad-prime projection. It keeps the full theta frequency sum and reunites the two positive Ramanujan allocations before applying the symmetry. The first conductor contains \(khg\); the second reduced denominators divide a fixed multiple of \(kh\). Their quotient supplies the exact \(g^2/B\) cutoff.

The analytic moment bound (4.3) still uses the standard-cusp Gauss factorization for its cubic sieve. The cutoff itself holds at all cusps, but the weaker all-cusp input has global envelope \(D^\epsilon(HD+H^2D)\) even after the cutoff: \(G=F=1\), \(E\asymp D\) remains possible. No quantitative norm theorem for the full growing Fourier/scattering family is proved here.

The initial fourth-moment dual range is \(H\asymp D^{3-\vartheta}\) at product length \(D^2\), far beyond (4.4). In addition, a positive completed mean square does not bound the covariance after the exact product-column diagonal is subtracted. A further argument must control that centered sesquilinear family, with distinct correction triples and their conductor masks, or work directly with the signed original Poisson expression. No full moment hierarchy or RH claim follows from the exact cutoff.

