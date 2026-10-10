# The principal covariance of short inverses is a long-tail covariance

**Status:** proved elementary corollary of the exact masked cube inverse and the principal-tail estimate. This is a statement about the complete-residue, zero-frequency part of the covariance. It does not bound the oscillating remainder of the complete finite-height comparison.

**Exact dependency:** *CENTERED_COVARIANCE_AND_CUBE_ALIASES.md*, SHA-256 **d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde**, especially equations (4.3)–(4.7) and Theorem 5.1. Its finite coefficient identities come from the pinned PR #918/#924 interfaces recorded there. The original signed normalization used in Section 3 below is the explicit PR #914 application (7.5b,c) of that manuscript.

**New point:** on comparable fixed product annuli, the raw column and the opposite long inverse tail have exactly zero principal correlation once the cutoff exceeds a fixed support ratio. Thus the principal off-product covariance of two short inverses is controlled at order \((R_1R_2)^{-1/2}\), without introducing separate raw-versus-tail estimates of order \(R_j^{-1/2}\).

## 1. Exact columns, supports and centering

For \(j=1,2\), let \(P_j\) be the normalized raw mixed polynomial (4.1) of the dependency, with its own factor scales, squarefree exclusion \(q_j\), squarefree auxiliary \(f_j\), outer mask \(r_j\), fixed finite ray data and fixed bounded smooth two-variable profile \(V_j\) of compact support in the positive quadrant. The tensor test in that definition is included. The two exclusions or auxiliaries may overlap arbitrarily, within or between the two columns. Let \(L_j=A_jB_j\). Choose positive constants \(\ell_j,u_j\) from the physical test support, so
\[
V_j(x,y)=0\quad\text{unless}\quad \ell_j\le xy\le u_j.
\]
These constants are a premise about every physical inverse term, not merely about the smaller set of raw coefficients left after masks or cancellations. In particular every nonzero coefficient of \(P_j\) has
\[
\ell_jL_j\le Nm\le u_jL_j.
\tag{1.1}
\]
For tensor tests one may take the products of their lower and upper support endpoints.

Split the exact finite cube inverse as
\[
P_j=S_j+T_j,
\]
where \(S_j\) uses inverse labels \(Nh\le R_j\), and \(T_j\) uses \(Nh>R_j\), with \(R_j\ge1\). The letters \(T_j\) here mean long inverse tails, not an isolated theta series.

After grouping the physical cube with the inverse label, every tail coefficient is on a reconstructed product
\[
N=m d^3,\qquad m\ \text{squarefree},\qquad Nd>R_j,
\tag{1.2}
\]
and has the same physical support
\[
\ell_jL_j\le \mathrm N(N)\le u_jL_j.
\tag{1.3}
\]
Its coefficient contains the exact divisor sum
\[
c_{R_j}(d)=\sum_{\substack{h\mid d\\Nh>R_j}}\mu_K(h).
\]
In particular the coefficient vanishes unless \(Nd>R_j\); no condition \((m,d)=1\) has been added. All masks and zero extensions remain those of the exact inverse.

The elementary identities and principal-tail estimate used here extend from the dependency's tensor test to the stated \(V_j\). At fixed combined cube product \(d\), the test is exactly \(V_j(Na/A_j,Nn(Nd)^3/B_j)\), independent of the inverse divisor \(h\mid d\). The inverse cancellation is therefore coefficientwise unchanged. The principal-tail proof only combines the factorizations \(an=m\), uses their divisor-bounded coefficient with the fixed bound for \(V_j\), and counts \(Nm\asymp L_j/(Nd)^3\). Its estimates (5.7) and (5.9) and the subsequent ideal sums are unchanged. This extension uses no separation of an analytic two-variable transform. It also applies after multiplying the physical profile by \(xy\), which preserves its fixed support and boundedness.

For finite column polynomials \(X=\sum_Nx_N\chi_N\) and \(Y=\sum_Ny_N\chi_N\), combine all coefficients with the same reconstructed product first and define
\[
\mathcal C_{\rm pr}(X,Y)
=\langle X,Y\rangle_{\rm pr}
-\sum_Nx_N\overline{y_N}\rho(\operatorname{rad}N).
\tag{1.4}
\]
This subtracts the true product-column diagonal from the complete-residue principal kernel. It is a sesquilinear form, and it need not be positive. Equality of factor pairs, cube labels or reduced sixth-power classes is not the diagonal in (1.4).

No arbitrary additional row character is permitted in the next support-separation claim. The actual reconstructed characters are those in (1.2). The independent finite rays and fourth-power auxiliaries are already retained in the row-independent coefficients.

In particular, independently shifted A2 product columns are not covered by this support threshold. The theorem is applied to the actual squarefree raw columns; a different product shift on each side requires a new alias and support calculation.

## 2. Exact support separation and the four blocks

### Lemma 2.1. The raw column is principal-orthogonal to the opposite tail

If
\[
R_2\ge
\left(\frac{u_2L_2}{\ell_1L_1}\right)^{1/6},
\tag{2.1}
\]
then
\[
\langle P_1,T_2\rangle_{\rm pr}=0,
\qquad
\mathcal C_{\rm pr}(P_1,T_2)=0.
\tag{2.2}
\]
The analogous conclusions with the two indices exchanged hold if
\[
R_1\ge
\left(\frac{u_1L_1}{\ell_2L_2}\right)^{1/6}.
\tag{2.3}
\]
The endpoints in (2.1) and (2.3) are included.

**Proof.** A potentially nonzero principal pairing of a squarefree raw product \(m_0\) with a tail product \(m d^3\) requires
\[
m_0=m,\qquad v_p(d)\equiv0\pmod2\quad\text{for every }p
\tag{2.4}
\]
by the exact cube-alias classification. Write \(d=j^2\). A nonzero coefficient \(c_{R_2}(d)\) requires at least one squarefree inverse divisor \(h\mid d\) with \(Nh>R_2\). Squarefreeness gives \(h\mid j\), so \(Nj>R_2\). On the other hand, the support inequalities imply
\[
(Nj)^6=(Nd)^3
=\frac{\mathrm N(md^3)}{Nm_0}
\le\frac{u_2L_2}{\ell_1L_1}.
\]
This contradicts (2.1), including at equality. Thus every principal kernel entry vanishes. The actual product-diagonal cross term also vanishes: \(d>1\) makes \(md^3\) nonsquarefree, whereas every raw product is squarefree. This proves (2.2). The other direction is identical. \(\square\)

The proof keeps the possibility that \(m\) overlaps \(d\). It needs only the exact alias classification and support, so independent auxiliary phases and stricter exclusions cannot spoil it. If the two product scales are comparable by fixed constants and the support intervals are fixed, the sufficient cutoff thresholds are fixed constants, independent of the growing scales.

The use of the squarefree inverse divisor improves a preliminary cube-root support condition to the sixth root in (2.1). This sharpening was identified during the independent audit by signed_sector.

### Theorem 2.2. The principal four-block identity

Assume (2.1) and (2.3), as well as \(R_1,R_2\ge1\). Put
\[
\mathcal T=\mathcal C_{\rm pr}(T_1,T_2).
\]
Then the exact matrix of principal off-product covariances is
\[
\boxed{
\begin{pmatrix}
\mathcal C_{\rm pr}(S_1,S_2)&\mathcal C_{\rm pr}(S_1,T_2)\\
\mathcal C_{\rm pr}(T_1,S_2)&\mathcal C_{\rm pr}(T_1,T_2)
\end{pmatrix}
=
\begin{pmatrix}\mathcal T&-\mathcal T\\-\mathcal T&\mathcal T\end{pmatrix}.}
\tag{2.5}
\]
Under the fixed polynomial support convention of the dependency, each entry satisfies
\[
\boxed{|\mathcal T|\ll_\epsilon D^\epsilon(R_1R_2)^{-1/2}.}
\tag{2.6}
\]
For a common cutoff \(R\), the short-short principal off-product covariance is therefore \(O(D^\epsilon/R)\).

**Proof.** On squarefree products, principal equality of the two sixth-power classes is exactly equality of the products. Thus \(\mathcal C_{\rm pr}(P_1,P_2)=0\), even when the coefficients, masks and auxiliaries differ. Lemma 2.1 gives the two cross vanishings. Substitute \(S_j=P_j-T_j\) into the sesquilinear form to obtain all four signs in (2.5).

The principal-tail norm and the separate physical diagonal-mass bound in Theorem 5.1 of the dependency give
\[
|\langle T_1,T_2\rangle_{\rm pr}|
\ll D^\epsilon(R_1R_2)^{-1/2},
\]
and the same bound for the product-diagonal term, by their respective Cauchy–Schwarz inequalities. Their difference proves (2.6). All phases in the tails were retained before these norm bounds. \(\square\)

This is an exact cancellation identity between four possibly signed or complex blocks. It does not assign a positive sign to \(\mathcal T\). Their full sum is zero, in agreement with the absence of principal off-product pairs in the original raw squarefree covariance.

## 3. The actual coupled zero-frequency normalization

At the physical kernel
\[
\Psi\!\left(\frac{H_{\rm orig}Nk}
{F^2\mathrm N(N)\mathrm N(N')}\right),
\]
the zero-frequency contribution is
\[
\mathfrak c_\Psi\frac{F^2}{H_{\rm orig}}
\mathrm N(N)\mathrm N(N')\Pi(N,N').
\tag{3.1}
\]
Multiply the left and right coefficients by \(\mathrm N(N)/L_1\) and \(\mathrm N(N')/L_2\), respectively. On the fixed support these are bounded smooth column multipliers; in the underlying tensor tests this simply replaces \(W_1(x)W_2(y)\) by \(xW_1(x)yW_2(y)\). The inverse identity, masks, supports and every argument above remain valid. Hence all four off-product zero-frequency blocks have the same sign pattern and bound
\[
\boxed{
O\!\left(
D^\epsilon\frac{F^2L_1L_2}{H_{\rm orig}\sqrt{R_1R_2}}
\right).}
\tag{3.2}
\]
The constant includes the fixed \(\mathfrak c_\Psi\). This estimate concerns the actual coupled zero-frequency term; it does not replace the remaining kernel by a separable weight.

For the original balanced first-Poisson expression of PR #914, take one common \(R\ge\max(1,(u/\ell)^{1/6})\) for every allocated raw column before introducing A2 corrections. At fixed original \(b,f\), both allocated product scales equal
\[
L_{bf}=\frac{L}{Nb\,Nf}.
\]
The exact normalized outer coefficient is \(H_{\rm orig}\mu_K(f)/(L\,Nf)\), as derived in equation (7.5c) of the dependency. Combining it with (3.2) leaves the absolute accounting weight
\[
O\!\left(D^\epsilon\frac{L}{(Nb)^2\,Nf\,R}\right).
\tag{3.3}
\]
The independent allocations of \(bf\) cost a divisor subpower. The \(b\)-sum in (3.3) converges, and the physically truncated \(f\)-sum is harmonic. Thus each of the four off-product principal blocks, with the full original signed \(b,f\) weights retained, is
\[
\boxed{O_\epsilon(D^\epsilon L/R).}
\tag{3.4}
\]
Their signed four-block sum is still exactly zero. Equation (3.4) records the size of a truncation artifact and the size of the terms that cancel it; it is not an additional term in the original untruncated off-diagonal.

No bound for the complete finite-height covariance follows from (2.6), (3.2) or (3.4). The nonzero dual frequencies of the smooth row kernel remain. Neither the PR #926 small-cube \(U\) term nor the original fourth-moment target is removed by this principal-block identity.

## 4. Finite diagnostic boundary

The separate *check_short_long_principal_blocks.py* checks the exact four signs on explicit off-product cube aliases, using rational complete-residue densities and a nonempty squarefree raw column in the same fixed product annulus. It also checks the endpoint support contradiction and an example outside that support condition where a raw/tail principal correlation survives. Its report binds this note and the checker by SHA-256. The diagnostic does not verify the analytic \(R^{-1}\) bound or the source's Gauss phases; those are supplied by the cited proof and its stated imports.
