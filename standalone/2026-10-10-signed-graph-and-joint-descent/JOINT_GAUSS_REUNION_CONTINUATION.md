# Joint Gauss summation continues the reunited series through v = 1

**Status:** proposed source-conditional analytic theorem. This note proves a new domain of holomorphy for the actual reunited three-cusp object of PR #922 by summing its two Gauss factors jointly. Its proof uses the counting version of PR #924's completed estimate and exact inverse, and does not require the angular reciprocal input. The original signed Möbius covariance and its short-row fourth moment remain unproved.

**Main conclusion.** The exact function \(\mathcal Y_k(s,v)\) of PR #922 continues to

\[
\boxed{\mathcal J=\{\Re s<\tfrac12,\quad
\Re(v-s)>\tfrac12,\quad \Re(v-2s)>\tfrac35\}.}
\tag{0.1}
\]

On strict closed real subregions, its squarefree-row energy is
\(O(H^{10/7+\epsilon})\), with polynomial vertical growth. In particular the same reunited function is holomorphic across \(v=1\) whenever \(\Re s<1/5\). The previously proved crossing had \(\Re s<0\). The larger domain has a weaker row exponent than the previously established square-root row mean on its smaller domain; both estimates remain available in their proper regions.

**Exact sources.**

- PR #924, commit **`725b2d25ab47e57500049d93985560098c7ef3fa`**, `standalone/2026-10-10-sextic-moving-labels/ANISOTROPIC_A2_NORM_TRANSFER.md`, Theorem 2.1, supplies the all-row anisotropic raw estimate for every positive inverse cutoff. Its mathematical input is the companion `MIXED_LABEL_COMPLETION.md`, Theorem 2.1 and Section 7, with the sixth-power stratification in `SIXTH_POWER_STRATIFIED_INVERSE.md`. The counting version permits bounded row-independent outer multipliers, as explicitly stated in the mixed theorem. All character zeros, moving exclusions and physical support caps are retained.
- PR #922, commit **`f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32`**, `standalone/2026-10-10-signed-covariance-descent/SECOND_REFLECTION_BOOTSTRAP.md`, Sections 1–3, supplies the exact cube-summed and conditioned Gauss formulas. `FULL_CUSP_DESCENT.md`, Sections 1–2, supplies the exact all-cusp expansion and its summable bad-label mass. `FINITE_RAY_REUNION.md` and `FINITE_CUBE_HOMOGENEITY.md` give its original finite coefficients and their entire dependence on \(s\).
- The same #924 packet's `OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md` supplies the existing \(4/7\) canonical mean and is used only for comparison here. The main theorem below does not require its additional external large-sieve input.
- The common imported theta foundation remains OpenAI/math commit **`adc7f1241b42e322a6451854ab7e4b4c146bf78a`**, October 5 `paper2.tex`, with the exact fixed cusp and ray conventions recorded in those source proofs. No independent reconstruction of that foundation is claimed.

The source-conditional inputs are assertions about the actual Gauss coefficient family. They are not higher moments of the original Möbius polynomial. This distinction is maintained throughout.

## 1. Two fixed finite characters on the raw factor axes

Use the Eisenstein field, multiplicative primary generators and fixed excluded-prime set \(S\) of the sources. Write

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n)
\]

on squarefree good ideals. The character \(\xi\) is fixed finite ray data, and the good-prime Gauss CRT identity is

\[
a_\xi(ab)=a_\xi(a)a_\xi(b)\chi_b(a)^4
\qquad((a,b)=1).
\tag{1.1}
\]

Fix one further finite ray character \(\omega\). For a squarefree auxiliary ideal \(f\) outside \(S\), let

\[
P_{k,f}^{\xi,\omega}(A,B)
=\frac1{\sqrt{AB}}\sum_{ab\ {\rm squarefree}} 
a_\xi(ab)\omega(b)\chi_{ab}(k)\chi_{ab}(f)^4
W_1(Na/A)W_2(Nb/B),
\tag{1.2}
\]

where all physical indices avoid \(S\). This includes the literal zeros when either row or auxiliary meets a column. The two fixed smooth weights have compact positive-norm support. Put \(F=Nf\), and use all nonzero element rows in \(H\le Nk<2H\), or any subset of that annulus.

### Lemma 1.1. The counting inverse accepts these two orientations

The counting version of #924's anisotropic inverse gives, for every \(R>0\),

\[
\begin{aligned}
\sum_{k\asymp H}|P_{k,f}^{\xi,\omega}(A,B)|^2
\ll (2H F A B)^\epsilon\bigl[
&HA+F H^2 A B^{-1/2}R^{3/2}
+F^{2/3}H^{4/3}A^{4/3}B^{-2/3}R^2\\
&+H+ABR^{-3}+(HAB)^{2/3}R^{-2}\bigr].
\end{aligned}
\tag{1.3}
\]

It also gives the same bound with \(A,B\) interchanged and the corresponding fixed weights interchanged.

**Proof of the finite-character adapter.** For the orientation displayed in (1.2), use the canonical coefficient with inner ray \(\xi\omega\), because

\[
a_\xi(ab)\omega(b)=a_{\xi\omega}(ab)\overline{\omega(a)}.
\tag{1.4}
\]

The last factor is a bounded row-independent outer multiplier. The counting version of the mixed completed theorem permits it. The exact cube inverse preserves it on the outer axis; after freezing an inverse index, its added outer mask is multiplied by the same factor. The long raw child still has a divisor-bounded row-independent coefficient vector, so the sixth-power-free sieve applies without a change. Thus the proof of the anisotropic inverse gives (1.3).

For the opposite orientation take \(b\) as the outer variable and use ray \(\xi\), with the outer multiplier \(\omega(b)\). This is again a permitted fixed multiplier. In each orientation the inverse uses the cube character belonging to its own inner ray. The two completed families need not be identical: their exact inverses both recover the same raw polynomial in (1.2). No invariance of a one-axis theta completion under interchanging its axes is assumed.

Equivalently, in the complete reflected scalar the new multiplier replaces the fixed finite character \(\eta(g)\) by another fixed finite character. It introduces no new archimedean type. The counting bound is uniform for this finite enlarged family. This proof does not assert the same extension for arbitrary row-dependent coefficients.

The source estimate was stated with every parameter bounded by a fixed power of an ambient reference scale. For (1.3) choose that scale to dominate \(2,H,F,A,B\), and start with a sufficiently small loss. The resulting loss is bounded by the one written in (1.3). Empty rectangles vanish; nonempty scales below one are bounded below by fixed support constants and are treated exactly as in the source. \(\square\)

### Lemma 1.2. A bound independent of the longer axis

For the same family,

\[
\boxed{
\sum_{k\asymp H}|P_{k,f}^{\xi,\omega}(A,B)|^2
\ll (2H F A B)^\epsilon
H^{10/7}F^{2/3}\min(A,B)^{6/5}.}
\tag{1.5}
\]

This holds for all nonempty scales, with the support convention above. It is a convenient bound for joint Mellin summation, not an assertion that it is the best physical estimate.

**Proof.** By Lemma 1.1 orient the shorter factor as \(A\), so \(1\le A\le B\) after the harmless bounded-scale convention. Choose

\[
R=B^{1/3}A^{-1/15}H^{-8/21}F^{-2/9}>0.
\tag{1.6}
\]

The exact source theorem allows this even when it is below one. Its physical caps and the empty-short-part argument remain in force. Substitution into the six terms of (1.3) gives respectively

| Source term | Power of \(H\) | Power of \(F\) | Power of \(A\) |
| --- | ---: | ---: | ---: |
| \(HA\) | \(1\) | \(0\) | \(1\) |
| middle short term | \(10/7\) | \(2/3\) | \(9/10\) |
| third short term | \(4/7\) | \(2/9\) | \(6/5\) |
| \(H\) | \(1\) | \(0\) | \(0\) |
| \(ABR^{-3}\) | \(8/7\) | \(2/3\) | \(6/5\) |
| mixed long tail | \(10/7\) | \(4/9\) | \(4/5\) |

Every power of \(B\) cancels. Since \(H,F,A\ge1\), each row is bounded by \(H^{10/7}F^{2/3}A^{6/5}\). This proves (1.5), with the opposite orientation handling \(B<A\). \(\square\)

The leading source term \(HA\) is fully included in this calculation. It is not replaced by \(H\), and it is bounded only after choosing the shorter physical factor.

## 2. A joint two-variable Gauss Dirichlet series

Initially for \(\Re t,\Re u>1\), define

\[
\mathcal B_{k,f}^{\xi,\omega}(t,u)
=\sum_{ab\ {\rm squarefree}}
\frac{a_\xi(ab)\omega(b)\chi_{ab}(k)\chi_{ab}(f)^4}
{(Na)^t(Nb)^u},
\tag{2.1}
\]

again with all indices outside \(S\). The squarefree-product condition includes \((a,b)=1\). Both factors retain the same auxiliary twist, and no assumption \((k,f)=1\) is made.

### Theorem 2.1. Joint continuation and row mean

The function (2.1) has a holomorphic continuation to the convex tube

\[
\boxed{\mathcal D_2=\{\Re t>\tfrac12,\quad
\Re u>\tfrac12,\quad \Re(t+u)>\tfrac85\}.}
\tag{2.2}
\]

For every closed bounded real subregion with strict margins, some finite \(M\) satisfies

\[
\boxed{
\left(\sum_{k\in\mathcal K_H}
|\mathcal B_{k,f}^{\xi,\omega}(t,u)|^2\right)^{1/2}
\ll H^{5/7+\epsilon}F^{1/3+\epsilon}
(2+|\Im t|+|\Im u|)^M,}
\tag{2.3}
\]

where \(\mathcal K_H\) is any subset of the original all-row annulus. Fixed finite ray partitions of the rows are permitted.

**Proof.** Choose a smooth dyadic partition of one on the ideal norms \(\ge1\), with fixed positive compact supports and a fixed first block. On the dyad \(A=2^j,B=2^\ell\), the series (2.1) is

\[
A^{1/2-t}B^{1/2-u}
P_{k,f}^{\xi,\omega}(A,B;W_t,W_u),
\qquad W_t(x)=x^{-t}W_0(x),
\tag{2.4}
\]

with the analogous first-block definition. Every required fixed seminorm of these weights is bounded by a polynomial in the imaginary parts on the specified real subregion.

Put \(T=\Re t\), \(U=\Re u\). Lemma 1.2 bounds the row norm of (2.4), apart from arbitrary small powers and the vertical polynomial, by

\[
H^{5/7}F^{1/3}
A^{1/2-T}B^{1/2-U}\min(A,B)^{3/5}.
\tag{2.5}
\]

For \(A\le B\), summing the dyadic \(B\)-tail first is allowed because \(U>1/2\), and gives a constant times

\[
H^{5/7}F^{1/3}A^{8/5-T-U}.
\]

This is summable in dyadic \(A\) because \(T+U>8/5\). The region \(B\le A\) is identical using \(T>1/2\). Choose all preliminary losses below the strict margins; their \(H,F\) contributions are absorbed in the stated \(\epsilon\). These estimates are locally uniform in both complex variables.

Every block is a finite entire sum. Its normally convergent sum in the finite-dimensional row Hilbert space is therefore holomorphic on (2.2). On \(T,U>1\) it equals (2.1) by absolute convergence. This proves continuation of that same series and the bound (2.3). \(\square\)

The convergence mechanism uses the raw **joint** coefficient \(a_\xi(ab)\). It does not take separate absolute values of its Gauss factors or insert a general coefficient into the native Möbius moment theorem.

## 3. The exact coefficient identity for the reunited function

Retain exactly #922's variables and finite characters:

\[
t=1-s,\quad u=v-s,\quad w=v-3s+\tfrac32=u+2t-\tfrac12,
\]

\[
\kappa=\eta\rho^3,\qquad \varrho^3=\overline\rho^{\,3}.
\tag{3.1}
\]

As in that source, write

\[
a_k(n)=a_\varrho(n)\chi_k(n),\quad
c_k(b)=\overline\alpha(b)^3\varrho(b)^3\chi_k(b)^3,
\quad\chi_k^-=\eta\overline\alpha^{\,3}\chi_k^3,
\tag{3.2}
\]

with the source reciprocal-primary convention and every zero retained. At a good prime \(p\nmid k\), put

\[
x_p=\chi_k^-(p)(Np)^{-w},\quad
K_p=\kappa(p)(Np)^{1-v},\quad
y_p=c_k(p)(Np)^{-(3t-1/2)}.
\]

The source identity is \(K_py_p=x_p\). Summing all cubes first gives its exact formula

\[
\mathcal Z_k(s,v;\varrho)
=L_{S,k}(3t-\tfrac12,c_k)
\sum_n^*\frac{a_k(n)}{(Nn)^t}
\prod_{p\mid n}(1-x_p+K_p).
\tag{3.3}
\]

All products here omit \(kS\), as in the source. Equivalently one can keep the row-character zeros.

### Proposition 3.1. Joint Gauss representation after cube reunion

On the initial absolute domain \(\Re v<1,\Re u>1\),

\[
\boxed{
\begin{aligned}
\mathcal Z_k(s,v;\varrho)
={}&L_{S,k}(3t-\tfrac12,c_k)
\sum_{z\ {\rm squarefree},\ (z,S)=1}
\frac{\mu_K(z)a_k(z)\chi_k^-(z)}{(Nz)^{t+w}}
\mathcal B_{k,z}^{\varrho,\kappa}(t,u).
\end{aligned}}
\tag{3.4}
\]

In (3.4), the row orientation in \(\mathcal B\) is the literal \(\chi_k(ab)\) of (3.2). To use Theorem 2.1, partition the rows into the fixed primary reciprocity classes and absorb the resulting multiplicative finite character into \(\varrho\). This is exactly the same fixed-family conversion used in #922 and #924. The auxiliary is \(f=z\), and the effective additional exclusion is one: the fourth-power twist already imposes \((ab,z)=1\).

**Proof.** In #922's conditioned representation write

\[
h_p=K_p^{-1}-y_p=K_p^{-1}(1-x_p).
\tag{3.5}
\]

The source's outer variable \(d\) and inner variable \(m\) are squarefree and coprime. Since \(\widetilde a_k(n)=\kappa(n)a_k(n)\), its exact coefficient becomes

\[
\frac{\widetilde a_k(d)h(d)}{(Nd)^u}
\frac{\widetilde a_k(m)\chi_m(d)^4}{(Nm)^u}
=\frac{a_k(dm)\kappa(m)}{(Nd)^t(Nm)^u}
\prod_{p\mid d}(1-x_p).
\tag{3.6}
\]

Here \(u+1-v=t\), and (1.1) was used with its genuine coprimality condition. This calculation specifies which factor carries \(\kappa\); it is the inner factor \(m\).

Expand the last finite product as

\[
\prod_{p\mid d}(1-x_p)
=\sum_{z\mid d}\mu_K(z)\chi_k^-(z)(Nz)^{-w},
\]

and write \(d=za\). The ideals \(z,a,m\) are pairwise coprime and squarefree. The Gauss CRT formula gives

\[
a_k(zam)=a_k(z)a_k(am)\chi_{am}(z)^4.
\tag{3.7}
\]

The \(z\)-denominator is exactly \((Nz)^{t+w}\), and the remaining \((a,m)\)-sum is (2.1) with auxiliary \(z\), inner finite character \(\kappa\), and the indicated row orientation. This proves (3.4). At \((z,k)>1\), the exterior \(a_k(z)\chi_k^-(z)\) is zero, so extending the sum to all good squarefree \(z\) is exact. At \((am,z)>1\), the inner fourth-power character is zero, not one. All rearrangements in this paragraph are absolutely convergent on the initial domain. \(\square\)

## 4. Holomorphy on the larger tube

### Theorem 4.1. The complete reunited object

For every original squarefree primary good row \(k\), the same \(\mathcal Z_k\), and the actual complete \(\mathcal Y_k\) of #922, continue holomorphically to \(\mathcal J\) in (0.1). Uniformly on strict closed bounded real subregions,

\[
\boxed{
\sum_{\substack{H\le Nk<2H\\k\ {\rm squarefree},\ (k,S)=1}}
|\mathcal Y_k(s,v)|^2
\ll H^{10/7+\epsilon}
(2+|\Im s|+|\Im v|)^M.}
\tag{4.1}
\]

The same estimate holds for \(\mathcal Z\) and any subset of these rows. The squarefree restriction here belongs to the exact source identity for the reflected object; the all-row theorem for \(\mathcal B\) does not remove it.

**Proof for \(\mathcal Z\).** In \((t,u)\)-coordinates, (0.1) is exactly (2.2). The cube factor in (3.4) is in its absolute Euler half-plane because \(\Re(3t-1/2)>1\). It is uniformly bounded, including all row omissions.

Each exterior character factor in the \(z\)-sum has modulus at most one. Theorem 2.1 bounds its inner row norm by \(H^{5/7+\epsilon}(Nz)^{1/3+\epsilon}\) times a vertical polynomial. Moreover throughout (2.2),

\[
\Re(t+w)=\Re(u+3t)-\tfrac12
=\Re(t+u)+2\Re t-\tfrac12>\tfrac{21}{10}.
\tag{4.2}
\]

Thus the full ideal sum

\[
\sum_z(Nz)^{-\Re(t+w)+1/3+\epsilon}
\tag{4.3}
\]

converges locally uniformly with ample margin. This proves local normal convergence of (3.4) in the row Hilbert space, holomorphy and its norm bound. It agrees with the original function on the nonempty initial absolute domain, so it continues the same \(\mathcal Z\).

**Proof for all cusps.** Use the exact coefficient identity in #922 `FULL_CUSP_DESCENT.md`, equation (2.5):

\[
\mathcal Y_k(s,v)=\sum_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}
B_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}(s,k)
\mathcal Z_k(s,v;\varrho).
\tag{4.4}
\]

All original cusp, bad-squarefree, ramified and bad-cube labels remain in this sum. Its fixed finite character family satisfies the required cube relation in (3.1). The exact coefficients are holomorphic in \(s\): before the finite Fourier expansion they are finite combinations of the source factors

\[
\widehat\phi_\rho(h)\overline{\kappa_{0,h}(k)}
\alpha(c_{0,h})^2(Nc_{0,h})^{1-2s}\Gamma_{c_{0,h}}(k)
\]

and fixed norm powers. The Fourier expansion is over a fixed finite group. In particular it introduces no new pole in \(s\).

Their source bound is

\[
\sup_k|B_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}(s,k)|
\ll 3^{-j(\Re t-1/6)}
(Nb_0)^{-(3\Re t-1/2)}.
\tag{4.5}
\]

This is stated on every bounded real strip, not only where \(\Re s<0\). Its total mass converges as soon as \(\Re t>1/6\); our new tube has \(\Re t>1/2\). Hence (4.4) is locally normally convergent on the new tube and its complete row norm is bounded by Minkowski using the sum of these suprema. No cross-cusp terms are discarded. It agrees with the old exact function on the initial overlap. Squaring proves (4.1). \(\square\)

### Corollary 4.2. The original reflected function and the v = 1 crossing

Retain the source identity

\[
\mathscr R_k(w,s)=\mathfrak H(s)(Nk)^{1-2s}\mathcal Y_k(s,v),
\]

where

\[
\mathfrak H(s)=\frac{i}{3^{5/2}}27^{-s}(2\pi)^{4s-2}
\frac{\Gamma(4/3-s)\Gamma(5/3-s)}
{\Gamma(s+1/3)\Gamma(s+2/3)}.
\tag{4.6}
\]

The numerator gamma factors have no poles on \(\Re s<1/2\), and the reciprocal denominator factors are entire. Thus the same \(\mathscr R\) is holomorphic on \(\mathcal J\). It obeys the corresponding energy bound

\[
\sum_{k\asymp H}^*|\mathscr R_k(w,s)|^2
\ll H^{24/7-4\Re s+\epsilon}
(2+|\Im s|+|\Im v|)^{M'}.
\tag{4.7}
\]

Stirling's formula contributes only a fixed-strip polynomial. The row power is included explicitly.

On \(v=1\), both \(\Re t\) and \(\Re u\) equal \(1-\Re s\). The strict conditions become \(\Re s<1/5\). Therefore the same complete reunited function is holomorphic in a neighborhood of each such point on \(v=1\), including \(0\le\Re s<1/5\). This is a statement about the full reunited function; no isolated artificial finite ray is assigned a vanishing residue without its own continuation.

## 5. Comparison with the 4/7 canonical mean and with physical bounds

Put \(a=\Re(v-s)\), \(\tau=\Re v\). The new tube can also be written

\[
a>\tfrac12,\qquad
\tau<\min(a+\tfrac12,\,2a-\tfrac35).
\tag{5.1}
\]

It strictly contains #922's old domain
\(a>1/2,\ \tau<\min(a,(3a-1)/2)\). For example
\((s,v)=(1/10,1)\) is in the new domain and not in the old one. The new proof pays row energy exponent \(10/7\). The #924 canonical mean still gives row energy \(H^{1+\epsilon}\) in its established smaller region

\[
4/7<a<1,\qquad \tau<(3a-1)/2.
\]

The new theorem does not claim the latter row exponent throughout (5.1).

The formal balanced Mellin scalar is \(D^{v-2s}=D^{t+u-1}\), whose infimum in the new tube is \(D^{3/5}\). This is **not** a new physical moment bound: a valid contour transfer must still include the original complete integrand, its transforms and all crossed singularities. Even if that transfer yielded the candidate positive energy

\[
H^{10/7}D^{6/5},
\tag{5.2}
\]

it would already be dominated by available bounds for the same coupled completed family. The #924 counting completion gives

\[
HD+H^2D^{1/2}+H^{4/3}D^{2/3},
\tag{5.3}
\]

which is termwise at most a constant times (5.2) when \(H\le D^{49/40}\). The classical full-cube all-row estimate gives

\[
H+H^{1/6}D^2+(HD^2)^{2/3},
\tag{5.4}
\]

which is termwise at most a constant times (5.2) when \(H\ge D^{168/265}\): the repeated-row term gives that threshold, and the mixed term only needs \(H\ge D^{7/40}\). The two ranges overlap and cover all \(H,D\ge1\). Thus this separate scalar route supplies no improvement of the existing physical envelope.

**Why (5.4) bounds the same completed family.** This comparison uses the literal physical cube expansion of #924 `MIXED_LABEL_COMPLETION.md`, equation (7.5), with \(q=f=r=1\):

\[
\mathcal C_{1,1}(A,B;k,1)
=\sum_{\substack{b\ {\rm arbitrary}\\(b,S)=1}}
\frac{\lambda(b)^3\chi_b(k)^3}{Nb}
\mathscr P_{1,b}\left(A,\frac{B}{(Nb)^3};k,1\right).
\tag{5.5}
\]

The same identity holds with a fixed bounded multiplier on the outer factor, retaining it in every raw child. In particular it covers the fixed finite characters in the two orientations of Lemma 1.1. The new mask \((a,b)=1\) is on the outer factor only; the inner squarefree index may overlap \(b\). The cube label is unrestricted and finite on physical support, \(Nb\ll B^{1/3}\), so this is the entire completion, including all physical cube terms.

For each fixed \(b\), group the raw child's ordered factors by their squarefree product. The normalized coefficient mass is \(O((HAB)^\epsilon)\), and the actual \(b\)-mask and fixed ray factors stay in that coefficient vector. Section 2 of #924 `SIXTH_POWER_STRATIFIED_INVERSE.md` gives the sixth-power-free operator bound \(U+L+(UL)^{2/3}\). Decompose all rows as \(k=u v^6k_0\), inserting the literal column zero mask at \(v\). For fixed \(v\), apply that operator at \(U\ll H/(Nv)^6\). The \(U\) and \((UL)^{2/3}\) terms are summable over \(v\); the \(L\) term is repeated over \(Nv\ll H^{1/6}\). Ideal counting therefore gives the all-row operator \(H+H^{1/6}L+(HL)^{2/3}\), with every fixed coefficient mask retained. At the child's length \(L\asymp AB/(Nb)^3\), this proves

\[
\sum_{k\asymp H}
\left|\mathscr P_{1,b}\left(A,\frac{B}{(Nb)^3};k,1\right)\right|^2
\ll (HAB)^\epsilon
\left[H+\frac{H^{1/6}AB}{(Nb)^3}
+\frac{(HAB)^{2/3}}{(Nb)^2}\right].
\tag{5.6}
\]

Use (5.5), Minkowski, and the exterior phase as a contraction for each fixed \(b\). At norm level the three ideal sums have weights \((Nb)^{-1}\), \((Nb)^{-5/2}\), and \((Nb)^{-2}\). The first is harmonic and physically truncated; the other two converge. This gives

\[
\sum_{k\asymp H}|\mathcal C_{1,1}(A,B;k,1)|^2
\ll (HAB)^\epsilon
\left[H+H^{1/6}AB+(HAB)^{2/3}\right].
\tag{5.7}
\]

Setting \(A=B=D\) is exactly (5.4). Thus (5.3) and (5.4) estimate the same coupled completed object, with fixed ray data; this argument does not compare a raw norm to a completed norm by an unsupported inequality.

The substantive new output is holomorphy of the **actual** reunited coefficient system on a larger tube, with a complete quantitative row bound and the explicit \(v=1\) crossing. Its proof preserves the coupled Gauss coefficient in the \((d,m)\) sum instead of applying the canonical one-factor mean separately to each \(d\).

## 6. Relation to signed scale sampling, and remaining gap

PR #926 at `086bf0560c0c2679a1fe41418f583d2c5ca743c3`, `SAMPLED_MOMENT_CRITERION.md`, Section 8, already shows that averaging the original nonnegative test over a fixed logarithmic scale interval produces a nonnegative tuple kernel that is bounded below on a full balanced shell. It also accounts for the aperture loss of its wide modulation average. Those results prevent treating scale smoothing or sparse sampling alone as the missing arithmetic cancellation. They are consistent with the explicit domination above.

The new identity (3.4) may be used inside a future two-column covariance argument because its auxiliary, finite characters, exterior row phases and convergent correction weights are all specified. This note does not prove that inserting it into both columns preserves the strict original product-column diagonal or estimates their centered signed difference. The original Möbius coefficients, signed auxiliary sum, coupled row-dependent kernel and long initial dual height still require an additional argument. No full fourth moment, 17/24 zero-free boundary or cofinal moment hierarchy is claimed.
