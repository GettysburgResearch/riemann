# Averaging the negative allocation in the reflected theta family

**Status:** proposed proved deduction from the explicitly stated quadratic and cubic large sieves; source-conditional application to the literal, all-cusp reflected family. This note proves a stronger **squarefree-row block estimate**, and then a separate **physical all-row block estimate** using conductor-dependent reflected lengths. It does not prove the full fourth moment, the generalized moment hierarchy, an arbitrary-coefficient all-row extension, or a new zero-free region.

**Scope:** all positive scales below a fixed power of an ambient \(D\), all common divisors between the negative allocation and the reflected squarefree index, literal character zeros, and the moving row exclusion. The new block bound permits arbitrary bounded **separate** coefficient vectors. Its application to the physical family uses the literal arithmetic coefficient and exact completed-group pruning from the pinned sources.

**What is new:** the negative allocation \(g\) is averaged with the quadratic column instead of frozen before applying a sieve. Common divisors \(c=(g,n)\) are treated explicitly. In a legitimate long-dual block at \(H=D^{3-\theta}\), \(0\leq\theta<1/2\), the result gives squarefree-row energy \(D^{5/2-\theta+\epsilon}\), compared with \(D^{35/12-\theta+\epsilon}\) from the preceding angularly improved two-axis bound. The same new exponent is then proved over every nonzero row for a specified smooth reflected-ratio block.

**Smallest remaining gap:** the high-frequency, small-cube blocks still contain the term \(U\) from the cubic coefficient energy. At the largest relevant \(U\), the new averaging does not improve that term. No summable signed estimate for those blocks, with the moving auxiliary conductors required by the original moment comparison, is proved here.

## 1. Exact source locks and the analytic inputs

The repository files below were fetched directly from GettysburgResearch/riemann at these exact branch heads, with their returned Git blob hashes checked against the fetched bytes:

| PR | Pinned head | Packet |
|---|---|---|
| #920 | 2edc467ef4dea4aa685219ac6a558a158b88768d | standalone/2026-10-10-theta-support-descent |
| #922 | f71a9bc6ac3ce59a3c19d7e842a3fa082ecfbe32 | standalone/2026-10-10-signed-covariance-descent |
| #923 | 1a1152008706f7e24fa1efe4990588f8f99c5d8d | standalone/2026-10-10-sextic-separated-cores |

The load-bearing application source is [PR #923, PRUNED_COUPLED_MEAN_SQUARE.md](https://github.com/GettysburgResearch/riemann/blob/1a1152008706f7e24fa1efe4990588f8f99c5d8d/standalone/2026-10-10-sextic-separated-cores/PRUNED_COUPLED_MEAN_SQUARE.md), especially (2.1)--(3.5), (4.1), and Sections 5--6. Its SHA256 is
411d7b28c0dabc97807d21683d731126e742d16424b1809787c87849dfb9e8d1.

The exact coefficient and support inputs are:

| Pinned source file | SHA256 |
|---|---|
| #920 RAMANUJAN_SUPPORT_PRUNING.md | 9a019b2253a0f35ade96455bf5d249cd1ca09285c4f2d7e17c475b5b5522c3ea |
| #920 ALL_CUSP_REFLECTION.md | 4a0201c3de364c1747726b9561f91ffc825da0aca926528844c543c9bbcd908d |
| #920 HIGHER_ANGULAR_SECOND_MOMENT.md | 82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959 |
| #922 FINITE_RAY_REUNION.md | 8897088fb7e89c66e18bf0652a913983c5120a61d854591f990cce2a6261f2e0 |
| #922 FINITE_CUBE_HOMOGENEITY.md | e4f7b3ff0817c4b6deaf2e608657425c06ac97c1a7f4f60f3762eba7eca7b0e1 |
| #922 ALL_CUSP_COEFFICIENT_ADAPTER.md | bfabc37c5b16a32d6b29fe5767f58f5f5a8dc161aaa3d127ebf11236fa2d3ca1 |
| #922 SPECTRAL_ROW_MEAN.md | 5154dc7d0502555f9a198eed386b9926bf1769ac61ae6b7c6fa319eadec7ace1 |

These are proposed source-qualified branch statements, not a claim of independent integration or review of every upstream theorem. The canonical imported theta source is OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 paper2.tex, 169005 bytes, SHA256
d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d,
Git blob 2000faddbbebac5de0ecfe0b962534ea61a852d5. Its equation eq:Q states the quadratic input in precisely the orientation below.

Work over \(K=\mathbb Q(\sqrt{-3})\), using the source's primary generators and a fixed finite set \(S\) containing primes over 6. A star denotes squarefree primary ideals outside \(S\). Write
\[
\rho_k(m)=\chi_k(m)^3.
\tag{1.1}
\]
The characters are extended by zero at nonunits. In particular,
\[
\rho_k(c^2)=\mathbf1_{(k,c)=1}.
\tag{1.2}
\]
An even character exponent does not remove this zero.

For nonempty supports in fixed positive norm annuli, the two sieve inputs are
\[
\sum_{Nk\asymp H}^{*}
 \left|\sum_{Nm\asymp L}^{*}z_m\rho_k(m)\right|^2
\ll_\epsilon (HL)^\epsilon(H+L)\sum_m|z_m|^2
\tag{QLS}
\]
and
\[
\sum_{Nn\asymp U}^{*}
 \left|\sum_{Ne\asymp E}^{*}z_e\chi_n(e)^4\right|^2
\ll_\epsilon (EU)^\epsilon
 [E+U+(EU)^{2/3}]\sum_e|z_e|^2.
\tag{CLS}
\]
They permit arbitrary coefficient vectors and subsets of the row supports. Finitely many fixed ray partitions retain the displayed powers. The primary analytic references are Goldmakher--Louvel, *A quadratic large sieve inequality over number fields*, Theorem 1.1 and Corollary 1.2, [doi:10.1017/S0305004112000370](https://doi.org/10.1017/S0305004112000370), and Blomer--Goldmakher--Louvel, *L-functions with \(n\)-th-order twists*, Theorem 1.3, [doi:10.1093/imrn/rns257](https://doi.org/10.1093/imrn/rns257), specialized to order three. These are the same two sieve inputs used in the pinned two-axis lemma.

All scales \(H,E,G,U\geq1\) are at most \(D^{A_0}\), with \(A_0\) fixed. A scale between a fixed support floor and one is included by enlarging its annulus by a fixed constant; empty supports give zero. Constants may depend on the fixed annuli, \(S,A_0,\epsilon\). Fixed additional exclusions in separate coefficient vectors need not have bounded cardinality. Their conductor size does not enter either sieve, since their coefficients remain bounded.

For brevity put
\[
\mathcal B(E,U)=E+U+(EU)^{2/3},\qquad M=\min(G,U).
\tag{1.3}
\]

## 2. A three-variable squarefree-row theorem

Let \(a_g,b_e,c_n\) be separate coefficient vectors of modulus at most one, supported on \(Ng\asymp G\), \(Ne\asymp E\), \(Nn\asymp U\). They may include any fixed exclusions or phases. Define
\[
\mathscr Q_k(E,G,U)
=\frac1{G\sqrt{EU}}
 \sum_{g,e,n}^{*}a_gb_ec_n
 \mathbf1_{(g,e)=1}\mathbf1_{(k,e)=1}
 \rho_k(gn)\chi_n(e)^4.
\tag{2.1}
\]
There is no condition \((g,n)=1\) in this definition. The character in the last factor already retains its zero when \((e,n)\ne1\). The bound is unchanged by a row scalar of modulus at most one, or by restriction to any subset of the squarefree rows.

### Theorem 2.1

Under (QLS) and (CLS),
\[
\boxed{
\begin{aligned}
\sum_{Nk\asymp H}^{*}|\mathscr Q_k(E,G,U)|^2
\ll_\epsilon D^\epsilon\bigg[
 &\frac{HEM}{GU}+\frac HG
  +\frac{HE^{2/3}M^{1/3}}{G U^{1/3}}\\
 &+E+U+(EU)^{2/3}
\bigg].
\end{aligned}}
\tag{2.2}
\]

In the sector \((g,n)=1\), the stronger bound is
\[
\boxed{
\sum_k^{*}|\mathscr Q_k^{\,\mathrm{cop}}|^2
\ll_\epsilon D^\epsilon
 \frac{H+GU}{GU}\,\mathcal B(E,U).
}
\tag{2.3}
\]

The bound is for the actual sum with its moving row mask. The proof does not replace that mask by an arbitrary row-dependent coefficient inside (CLS).

### Step 1: group the coprime \(g,n\) product before the quadratic sieve

First omit the row mask \(\mathbf1_{(k,e)=1}\), but keep both \((g,e)=1\) and \((g,n)=1\). This temporary family will be used after an exact expansion of the row mask.

Since \(g,n\) are squarefree and coprime, \(m=gn\) is squarefree and \(Nm\asymp GU\). Its coefficient before the normalization is
\[
\beta_m=\sum_{\substack{gn=m\\Ng\asymp G,\ Nn\asymp U}}
a_gc_n
\sum_{Ne\asymp E}^{*}b_e\mathbf1_{(g,e)=1}\chi_n(e)^4.
\tag{2.4}
\]
The number of representations is at most the ideal divisor function of \(m\), which is \(O_\epsilon((Nm)^\epsilon)\). Cauchy on this finite representation set therefore gives
\[
\sum_m|\beta_m|^2
\ll_\epsilon D^{\epsilon_0}
\sum_{Ng\asymp G}^{*}
\sum_{Nn\asymp U}^{*}
\left|\sum_{Ne\asymp E}^{*}
b_e\mathbf1_{(g,e)=1}\chi_n(e)^4\right|^2.
\tag{2.5}
\]
Restrictions on \(n\), including \((n,g)=1\), have only been enlarged in a nonnegative sum. For each fixed \(g\), apply (CLS) to the coefficient vector
\(b_e\mathbf1_{(g,e)=1}\). Its squared mass is \(O(E)\). There are \(O(G)\) possible \(g\), so
\[
\sum_m|\beta_m|^2
\ll_\epsilon D^{\epsilon_0}GE\,\mathcal B(E,U).
\tag{2.6}
\]
Apply (QLS) to the product column \(m\), then divide by
\(G^2EU\), the squared normalization in (2.1). This proves (2.3) for the temporary family without the row mask.

### Step 2: restore the moving row mask exactly

Use the finite identity
\[
\mathbf1_{(k,e)=1}=\sum_{r\mid k,\ r\mid e}\mu_K(r).
\tag{2.7}
\]
For each row \(k\), Cauchy over its divisors costs at most
\(\tau_K(k)\ll_\epsilon D^{\epsilon_0}\). This gives a **sum of squared norms** over \(r\); no unsummable Minkowski bound over \(r\) is used.

Fix \(r\), put \(R=Nr\), and write \(k=rk'\), \(e=re'\). Both \(r\) and the two residual indices are squarefree, with
\((r,k'e')=1\). The surviving scales are \(H/R,E/R,G,U\). The original restrictions and characters give
\[
\begin{split}
\rho_{rk'}(gn)&=\rho_r(g)\rho_r(n)\rho_{k'}(gn),\\
\chi_n(re')^4&=\chi_n(r)^4\chi_n(e')^4.
\end{split}
\tag{2.8}
\]
The first restriction \((g,e)=1\) retains \((g,r)=1\) and \((g,e')=1\). If \(n\) is not coprime to \(r\), the factor \(\chi_n(r)^4\) is zero. The new \(g\)- and \(n\)-phases in (2.8) belong to separate coefficient vectors. The conditions involving \(r\) are fixed exclusions. The restriction \((k',r)=1\) restricts the row set and causes no loss. Thus Step 1 applies without deleting any zero.

The original normalized expression is \(R^{-1/2}\) times the normalized expression with \(E\) replaced by \(E/R\). Consequently the fixed-\(r\) squared bound is
\[
R^{-1}\frac{H/R+GU}{GU}\mathcal B(E/R,U).
\tag{2.9}
\]
Its six monomials are
\[
\frac{HE}{GU}R^{-3},\quad
\frac HG R^{-2},\quad
\frac{HE^{2/3}}{GU^{1/3}}R^{-8/3},\quad
ER^{-2},\quad UR^{-1},\quad (EU)^{2/3}R^{-5/3}.
\tag{2.10}
\]
The ideal sums of powers \(3,2,8/3,2,5/3\) converge. The power-one sum is logarithmic on the actual finite support \(R\ll\min(H,E)\), and is absorbed in \(D^\epsilon\). This proves (2.3), including the original moving mask.

### Step 3: retain every \(g,n\) collision

Partition (2.1) by the exact squarefree common divisor
\[
c=(g,n),\qquad g=cg',\quad n=cn'.
\tag{2.11}
\]
Then
\[
(g',n')=1,\qquad(c,g'n')=1.
\tag{2.12}
\]
For \(r=Nc\), the exact character identities are
\[
\begin{split}
\rho_k(gn)&=\mathbf1_{(k,c)=1}\rho_k(g'n'),\\
\chi_n(e)^4&=\chi_c(e)^4\chi_{n'}(e)^4.
\end{split}
\tag{2.13}
\]
The mask \(\mathbf1_{(k,c)=1}\) is essential. In particular, taking \(g=n=k\) equal to one prime would make its deletion change zero into one.

For fixed \(c\), the \(g'\)-vector is \(a_{cg'}\) with the fixed exclusions in (2.12), and similarly for \(n'\). The \(e\)-vector is multiplied by \(\chi_c(e)^4\) and retains \((c,e)=1\). The moving conditions are precisely those of (2.3), now at
\[
G'=G/r,\qquad U'=U/r.
\tag{2.14}
\]
No multiplicativity of the coefficient vectors is needed. The remaining row mask in (2.13) is a fixed row restriction.

The ratio of normalizations is exactly
\[
\frac{G'\sqrt{EU'}}{G\sqrt{EU}}=r^{-3/2}.
\tag{2.15}
\]
There are \(O(C)\) possible \(c\) in a norm dyad \(Nc\asymp C\). Minkowski over this finite dyad, followed by (2.3), therefore gives
\[
\begin{aligned}
\|\mathscr Q^{(C)}\|_{\ell^2(k)}^2
&\ll_\epsilon D^{\epsilon_0}C^{-1}
 \frac{H+GU/C^2}{GU/C^2}
 \mathcal B(E,U/C)\\
&=D^{\epsilon_0}\bigg[
\frac{HEC}{GU}+\frac HG
+\frac{HE^{2/3}C^{1/3}}{GU^{1/3}}
+\frac EC+\frac U{C^2}
+\frac{(EU)^{2/3}}{C^{5/3}}\bigg],
\end{aligned}
\tag{2.16}
\]
where equality in the second line denotes the expansion of the displayed majorant, with its common implicit constant.

The possible \(C\) are at most a fixed multiple of \(M=\min(G,U)\). A final Cauchy or Minkowski inequality over the logarithmically many dyads costs only \(D^\epsilon\). The increasing powers of \(C\) are bounded by \(M\) and \(M^{1/3}\); the negative powers are bounded by their values at a fixed lower support floor. Reassigning the preliminary \(\epsilon_0\)'s proves (2.2). \(\square\)

### Comparison with freezing \(g\)

The preceding two-axis procedure gives
\[
\frac{H+U}{U}\mathcal B(E,U)
=\frac{HE}{U}+H+
\frac{HE^{2/3}}{U^{1/3}}+E+U+(EU)^{2/3}.
\tag{2.17}
\]
Every term of (2.2) is at most the corresponding term of (2.17):
the three row-dependent multipliers are \(M/G\), \(1/G\), and
\(M^{1/3}/G\), all at most one because \(1\leq M\leq G\).
The last three terms are unchanged. The improvement is therefore in a specified part of the true bound, not in a formal comparison that discards collision terms.

## 3. Adapter to the actual all-cusp reflected block

This section uses the exact, pinned theta interfaces. It does not replace the source family by a model with arbitrary divisor coefficients.

The source physical completion is
\[
\mathcal C_{A,B}(k)=A^{-1/2}\sum_a^{*}
\overline{\alpha(a)}\gamma_2(a)\xi(a)\chi_a(k)
W_1(Na/A)\,T(B;k,a).
\tag{3.1}
\]
Here the original \(a\) and, initially, \(k\) are squarefree good primary indices. The reflected indices may meet the fixed bad set.

First retain the **entire** projected Ramanujan group
\[
\prod_{p\mid a}(-1+Np\,\mathbf1_{p\mid nb})
=\sum_{dg=a}\mu_K(g)Nd\,\mathbf1_{d\mid nb}.
\tag{3.2}
\]
The #920 all-cusp support theorem permits inserting a smooth cutoff
\[
Ng\ll\min(A,\sqrt B).
\tag{3.3}
\]
It is inserted on complete groups before the next expansion. No individual frequency block is declared zero.

Only after this step allocate \(d=ef\), \(n=en'\), \(b=fb'\), using the exact conditions
\[
(e,f)=(e,g)=(f,g)=1,\qquad(f,n')=1.
\tag{3.4}
\]
The squarefreeness of \(n=en'\) includes \((e,n')=1\); its character zero can equivalently retain this condition. There is no restriction \((g,n'b')=1\).
The dyadic lengths obey \(EFG\asymp A\).

Equation (3.4) of the pinned #923 note gives the exact size normalization and the remaining varying character:
\[
\frac1{\sqrt A}\,
\frac{\mu_K(g)}
 {\sqrt{Nf\,Ng}\sqrt{Nn'}\,Nb'}
\times\text{bounded separate arithmetic factors}
\times\rho_k(gn'b')\mathbf1_{(k,ef)=1}
\times\chi_{n'}(e)^4.
\tag{3.5}
\]
The scalar, ray and cusp data leading to this formula are retained as source data. In particular:

1. The product \(\gamma_2(a)\gamma_4(a)\) cancels with its full CRT phases, and the remaining \(g\)-angle is \(\overline{\alpha(g)}^3\). Its finite factor is a fixed ray character after a fixed finite expansion.
2. At every cusp the good squarefree coefficient is \(\gamma_2(n)\), in the source orientation. The exact CRT identity
   \[
   \gamma_2(en')=\gamma_2(e)\gamma_2(n')\chi_{n'}(e)^4
   \tag{3.6}
   \]
   is what supplies the cubic coupling used in (CLS).
3. All supplementary ray factors and the intrinsic nonstandard-cusp additive phases have a fixed bad denominator. A finite residue expansion separates their \(e,g,n'\) dependence, together with a finite row partition. This uses the full finite-ray/cusp coefficients, not the absolute coefficient envelope. The pinned #922 finite-ray and coefficient notes justify keeping the same fixed modulus as the good labels grow.
4. The fixed squarefree bad part of \(n'\) has finitely many possibilities. The arbitrary bad cube part \(b_S\) has weight \(1/Nb_S\), whose fixed-prime geometric sum converges. The ramified sectors have weight \(O(3^{-m/3})\), \(m\geq-4\), also summable. None of these dual primes is silently removed.

Fix \(f\), the cube label \(b'\), one of these finite branches, and a reflected squarefree dyad \(Nn'\asymp U\). The masks involving \(f\) belong to fixed \(e,g,n'\) coefficient vectors. The row mask \((k,f)=1\) and the factor \(\rho_k(b')\) are contractions on the row vector. The remaining moving row mask is \((k,e)=1\). The only remaining moving intercolumn restrictions are \((g,e)=1\) and the zeros of \(\chi_{n'}(e)^4\). Thus the arithmetic family is exactly (2.1).

The smooth norm factors must be separated before this assertion is used in a norm. The source logarithmic derivative bounds on the reflected weight give a common integrable Mellin majorant after dyadic partition. Norm powers modify only the three separate vectors and a row scalar. The support cutoff (3.3) is smooth on each surviving dyad and has the same uniform derivative property. This is also how the coupled weight \(W_1(Nefg/A)\) separates. No arithmetic character is differentiated.

The normalizer can be checked without suppressing an allocation count. For \(Nf\asymp F\), \(Ng\asymp G\), \(Nn'\asymp U\), \(Nb'\asymp C\), (3.5) has coefficient size
\[
\frac1{\sqrt A\sqrt F\sqrt G\sqrt U\,C}
\asymp\frac1{F C}\frac1{G\sqrt{EU}},
\qquad A\asymp EFG.
\tag{3.7}
\]
There are \(O(F)\) possible \(f\), and
\(\sum_{Nb'\asymp C}(Nb')^{-1}=O(1)\).
Minkowski in these frozen labels therefore leaves exactly the normalization of (2.1), up to fixed support constants and the common Mellin majorant. There is no additional factor \(G\) after applying Theorem 2.1: that average is already inside the theorem.

### Corollary 3.1: a physical reflected block

For squarefree rows \(Nk\asymp H\), the literal all-cusp block with fixed norm dyads \(E,F,G,U,C\) obeys (2.2), with \(n=n'\), up to \(D^\epsilon\), the summable bad/ramified weights, and the source's rapidly decreasing transformed-weight tails. Its effective range includes the smaller frequencies,
\[
1\leq U\ll \frac{Y}{3^m(Nb_S)^3 C^3},
\qquad
Y=\frac{H^2 E G^2}{BF}.
\tag{3.8}
\]
Comparability rather than just this upper bound holds after localizing the positive transformed-weight argument to a fixed compact annulus, as in Section 6.
The scalar and the support statement are source-conditional; the improvement from (2.17) to (2.2) is the native two-sieve proof above.

An original factorwise exclusion \((a,h)=1\) is permitted: it becomes the fixed masks on \(e,f,g\) and does not affect the argument. A general outer multiplier \(v(efg)\), even if divisor bounded and row independent, is **not** covered by this adapter, because it need not separate between \(e\) and \(g\). The preceding source theorem could freeze \(g\) and tolerate such a multiplier; this stronger estimate has a different coefficient hypothesis.

## 4. A strict gain in the long-dual range

Let \(0\leq\theta<1/2\) be fixed. Choose
\[
A=B=D,\qquad H=D^{3-\theta},\qquad
F=1,\quad E=G=D^{1/2}.
\tag{4.1}
\]
The cutoff \(G\ll\sqrt B\) allows these scales. Up to fixed support constants,
\[
Y=D^{13/2-2\theta}.
\tag{4.2}
\]
Take a reflected squarefree block of length \(U=D^2\), with the unramified, good cube dyad
\[
C=D^{3/2-2\theta/3}.
\tag{4.3}
\]
Then \(UC^3=Y\), so this is an actual block in the effective reflected range.

Here \(M=G=D^{1/2}\). The six terms in (2.2) have exponents
\[
\frac32-\theta,\quad
\frac52-\theta,\quad
\frac73-\theta,\quad
\frac12,\quad 2,\quad \frac53.
\tag{4.4}
\]
The largest is \(5/2-\theta\) for the stated range of \(\theta\). Hence
\[
\boxed{
\text{this reflected block has squarefree-row energy }
\ll_\epsilon D^{5/2-\theta+\epsilon}.}
\tag{4.5}
\]

By comparison, (2.17) has dominant term \(H=D^{3-\theta}\). For the literal Möbius \(g\)-coefficient, the #923 Sections 5--6 Mellin operator gives an additional factor \(G^{2\sigma-2}\), for each fixed \(\sigma>11/12\). The same argument is valid after the present smooth squarefree/cube dyadic localization: it uses the separated norm kernels and the same convergent moving-\(e\) operator. Choosing a fixed positive margin in terms of the final epsilon gives the earlier bound
\[
D^\epsilon G^{-1/6}\frac{H+U}{U}\mathcal B(E,U)
\asymp D^{35/12-\theta+\epsilon}.
\tag{4.6}
\]
Thus (4.5) improves the available block exponent by \(5/12\). No reciprocal estimate at the endpoint \(11/12\) is asserted. The new bound (4.5) itself does not use the angular reciprocal theorem or Möbius cancellation.

This is an upper-bound improvement for a legitimate block; it is not a lower-bound computation or a statement that this block saturates either inequality.

## 5. What survives after summing the squarefree and cube lengths

For \(1\leq U\ll Y\) and \(Y\geq1\), each of the first three terms in (2.2) is \(O(HE/G)\), since \(M\leq U\) and \(E\geq1\). Consequently the new whole-allocation majorant is
\[
\boxed{
D^\epsilon\left[\frac{HE}{G}+E+Y+(EY)^{2/3}\right].
}
\tag{5.1}
\]
The finitely many ramified branches and their summable tails, the cube dyads, and the squarefree dyads are treated using the same Mellin majorant as in the source. Frequencies beyond the effective range carry its rapid decay. The displayed claim is restricted to \(Y\geq1\); no subunit sieve is being invoked.

In the intended long-row range \(H\geq G\), the term \(E\) is absorbed in \(HE/G\). Without that inequality it must be retained. This minor term matters for the exact rectangular quantifiers.

For the literal coefficient, one can also take the smaller of (5.1) and the source bound
\[
D^\epsilon G^{-1/6}\,[HE+Y+(EY)^{2/3}].
\tag{5.2}
\]
These are bounds on the same retained allocation family. They are not multiplied together, and no independent-gain claim is made.

The obstruction is now explicit. At small cube length, \(C\asymp1\), equation (3.8) permits \(U\asymp Y\). The terms
\[
U+(EU)^{2/3}
\tag{5.3}
\]
in the new bound are exactly as large as in the two-axis bound. For the initial long-dual regime, they can dominate the improved row-dependent terms by a large power. Summing \(E,F,G\) therefore does not give the target higher-moment estimate from this lemma alone.

Theorem 2.1 remains a squarefree-row theorem. A direct extension to arbitrary row-independent coefficient vectors at a fixed column length would incur a square-part multiplicity loss. Section 6 below gives a separate physical block result that also uses the source's conductor-dependent shortening of the reflected column. It does not give an arbitrary-coefficient all-row version of (2.2).

## 6. A physical block estimate over every nonzero row

This section adds one pinned input: [PR #923, ALL_ROW_COMPLETION_AND_RAW_GAIN.md](https://github.com/GettysburgResearch/riemann/blob/1a1152008706f7e24fa1efe4990588f8f99c5d8d/standalone/2026-10-10-sextic-separated-cores/ALL_ROW_COMPLETION_AND_RAW_GAIN.md), Sections 2--4, SHA256
a0e6bd5517a81f44d2a18bd32dc4f0db623b9951c17068e56af7009c8914fdec.
Its local row-prime adapter and exact support cutoff are used with their stated source dependencies.

### The physical block being bounded

Choose a fixed smooth function \(\psi\) supported on a compact subinterval of \((0,\infty)\). Starting from the source completed family, insert the complete-group \(g\)-cutoff first. Next perform the allocations in Section 3 and restrict \(e,f,g,b'\) to the norm dyads \(E,F,G,C\). In every reflected summand, multiply the transformed weight \(W^\sharp(x)\) by \(\psi(x)\), where \(x\) is its **actual positive transformed-weight argument**.

Call the resulting row vector \(\mathcal C^\psi_{E,F,G,C}(k)\). This is a specified component of the reflected completed family after legitimate pruning. It is not the whole \(n'\)-sum at the same cube dyad. Frequencies with \(x\) tending to zero belong to other components and have not been included in this theorem.

Put
\[
U_0=\frac{H^2 E G^2}{B F C^3},\qquad
\Lambda=\min\{1,(G/U_0)^{1/3}\}.
\tag{6.1}
\]
All displayed scales are polynomially bounded in \(D\), and \(U_0\geq1\); bounded nonempty scales are included by the fixed support convention. The same fixed positive ratio profile is used for every row. It is not chosen after inspecting the arithmetic coefficients.

### Theorem 6.1

For the literal family, under the exact source interfaces just specified,
\[
\boxed{
\begin{aligned}
\sum_{0<Nk\asymp H}|\mathcal C^\psi_{E,F,G,C}(k)|^2
\ll_\epsilon D^\epsilon\bigg[
&\frac{HE}{G}\Lambda+\frac HG
+\frac{HE^{2/3}}G\Lambda\\
&+E\sqrt H+U_0+(EU_0)^{2/3}
\bigg].
\end{aligned}}
\tag{6.2}
\]
The sum includes all nonzero row elements, including units, fixed bad-prime parts, and all square factors. Constants may depend on the fixed profile \(\psi\). The permitted original mask \((a,h)=1\) is retained.

The exponent \(1/3\) in (6.1) is notation for bounds obtained with a fixed positive margin and then absorbed in \(D^\epsilon\). No endpoint Euler-product convergence is asserted.

### Step 1: the exact square-part and local row-prime adapter

For a good primary row write, at the ideal level,
\[
k=s v^2,\quad s\ {\rm squarefree},\qquad
t=(s,\operatorname{rad}v),\quad s=t s',
\tag{6.3}
\]
so \((s',v)=1\). Put \(V=Nv\), \(T=Nt\). For fixed \(v,t\), the varying squarefree row \(s'\) has scale
\[
H'=\frac{H}{T V^2}.
\tag{6.4}
\]
Fix one source active set at the row primes. Its good radical is
\[
R=s'r_v,\qquad r_v\mid\operatorname{rad}v,\quad R_v=Nr_v\leq V.
\tag{6.5}
\]
At a prime \(p\mid v\), write \(a=v_p(v)\geq1\) and
\(\varepsilon_p=\mathbf1_{p\mid t}\). The source local exponent is
\[
j_p\equiv 2a+\varepsilon_p\pmod6.
\tag{6.6}
\]
A prime can be inactive only if \(j_p=0\). In particular it is always active for \(a=1\) and \(a=2\). The only local amplitude larger than one is the \(j_p=4\) Ramanujan row factor; its squared amplitude is at most \(Np\). This case requires
\[
\varepsilon_p=0,\qquad a\equiv2\pmod3.
\tag{6.7}
\]
Writing the actual product of these squared losses as \(Q_4\), one has the useful uniform majorant
\[
Q_4\leq J(v):=\prod_{p^2\mid v}Np.
\tag{6.8}
\]

The source proves that, after freezing \(b'\), these local factors are separate \(e\)- and \(n'\)-coefficients, with \(n'\)-amplitude at most \(\sqrt{Q_4}\); they introduce no additional \(g\)-dependence. The \(g\)-phase from the row remains quadratic. More explicitly, the factors contributed by \(t,v\) to \(\rho_k(gn')\) are separate \(g,n'\) phases or literal fixed exclusions, leaving \(\rho_{s'}(gn')\). The moving \(e\)-mask is \((s',e)=1\), with all other factors fixed in the coefficient vectors or row set. Theorem 2.1 therefore applies at row length \(H'\), with the squared loss \(Q_4\).

For the moment fix the ramified and dual bad-prime labels at their base values. The source conductor in the transformed argument is \(H'R_v\), not \(H'\) or the original \(H\) alone. The profile \(\psi(x)\) therefore restricts the reflected squarefree variable to
\[
U_v\asymp U_0\frac{R_v^2}{T^2V^4}.
\tag{6.9}
\]
All original norm variables lie in fixed annuli; the comparisons here have uniform constants. If \(U_v\) is below the fixed nonempty support floor there is no such frequency, rather than an application of a subunit sieve. The profile and remaining weights have a common Mellin majorant as in Section 3.

### Step 2: the local Euler sum that controls the first and third terms

For every fixed \(0\leq\eta<1/3\), the following sum over \(v,t\) and their allowed active sets converges:
\[
\mathcal Z_\eta=
\sum_{v}\ \sum_{t\mid\operatorname{rad}v}\
\sum_{\text{allowed active sets}}
Q_4\,T^{2\eta-1}V^{4\eta-2}R_v^{-2\eta}<\infty.
\tag{6.10}
\]
There are no omitted row-count factors: the sum in (6.10) is over the actual ideals \(v\), and \(H'\) has already supplied the factor \(T^{-1}V^{-2}\).

Here is a direct local proof. Since \(2\eta-1<0\), one can discard the \(T\)-factor in an upper bound. Use (6.8); the local active-set count is bounded by an absolute constant for each exponent. The three relevant possibilities are:

| Valuation \(a=v_p(v)\) | Active status used | Squared loss used | Upper bound for the local summand |
|---|---|---|---|
| \(a=1\) | always active | \(1\) | \(O(q^{2\eta-2})\) |
| \(a=2\) | always active | \(q\) | \(O(q^{6\eta-3})\) |
| \(a=3\) | allow inactivity | \(1\) | \(O(q^{12\eta-6})\) |
| \(a\geq4\) | allow inactivity | \(q\) | \(O(q^{\,1+a(4\eta-2)})\) |

Here \(q=Np\). At \(a=3\), the exponents \(j=0,1\) have no \(Q_4\)-loss; its displayed bound includes the inactive \(j=0\) case. For a compact common majorant, one can also bound this row by \(q^{12\eta-5}\) and sum the last two rows geometrically starting at \(a=3\). All the displayed leading exponents are strictly less than \(-1\) when \(\eta<1/3\), and the higher valuations decrease geometrically. The local Euler factor is consequently
\[
1+O_\eta\!\left(
q^{2\eta-2}+q^{6\eta-3}
+\frac{q^{12\eta-5}}{1-q^{4\eta-2}}
\right).
\tag{6.11}
\]
The ideal-prime sum of this error converges. This proves (6.10). The \(a=2,j=4\) case explains why this proof cannot set \(\eta=1/3\): its term then has size \(q^{-1}\).

Let \(M_v=\min(G,U_v)\). The first term of Theorem 2.1 is
\[
\frac{H'E M_v}{G U_v}
=\frac{H'E}{G}\min(1,G/U_v).
\tag{6.12}
\]
For \(x>0\) and \(0\leq\eta\leq1\), \(\min(1,x)\leq x^\eta\). Substitute (6.4) and (6.9) into (6.12), and sum with \(Q_4\). Equation (6.10) gives
\[
\sum_{v,t,\text{active}}Q_4\frac{H'E M_v}{G U_v}
\ll_\eta \frac{HE}{G}(G/U_0)^\eta.
\tag{6.13}
\]
The choice \(\eta=0\) gives \(HE/G\). A fixed \(\eta<1/3\), chosen sufficiently close to \(1/3\) in terms of the final ambient epsilon, gives the other entry of
\[
D^\epsilon\min\!\left\{\frac{HE}{G},
\frac{HE}{G^{2/3}U_0^{1/3}}\right\}.
\tag{6.14}
\]
Polynomial scale bounds justify absorbing the positive margin. The two entries are separately proved bounds on the same sum.

The third term is
\[
\frac{H'E^{2/3}M_v^{1/3}}{G U_v^{1/3}}
=\frac{H'E^{2/3}}G
\min\{1,(G/U_v)^{1/3}\}.
\tag{6.15}
\]
For \(0\leq\eta<1/3\), the last minimum is also at most
\((G/U_v)^\eta\). The identical Euler sum proves
\[
D^\epsilon\min\!\left\{\frac{HE^{2/3}}G,
\frac{HE^{2/3}}{G^{2/3}U_0^{1/3}}\right\}.
\tag{6.16}
\]
The second term \(H'/G\) sums to \(O(H/G)\) by (6.10) at \(\eta=0\).

### Step 3: the three terms without the squarefree row length

The elementary Euler products
\[
\sum_v J(v)(Nv)^{-\rho}<\infty,\qquad \rho>1,
\tag{6.17}
\]
hold because the local terms are \(q^{-\rho}\) at valuation one and
\(q^{1-a\rho}\) at valuations \(a\geq2\). Divisor-bounded \(t\)- and branch counts can either be included in these local products with fixed positive margins, or be absorbed in \(D^\epsilon\).

All nonempty rows have \(V\ll\sqrt H\). Rankin's inequality applied with any fixed small positive margin in (6.17) gives
\[
\sum_{Nv\ll\sqrt H}J(v)\ll_\epsilon D^\epsilon\sqrt H.
\tag{6.18}
\]
Thus the \(E\) term costs \(D^\epsilon E\sqrt H\).

By \(R_v\leq V\) and \(T\geq1\),
\[
U_v\ll U_0/V^2.
\tag{6.19}
\]
Consequently the \(U_v\) and \((EU_v)^{2/3}\) terms sum, respectively, using (6.17) with exponents \(2\) and \(4/3\), to
\[
D^\epsilon U_0,\qquad
D^\epsilon(EU_0)^{2/3}.
\tag{6.20}
\]
This is the step that avoids a spurious \(\sqrt H\,U_0\) loss: the reflected length shrinks with the square part.

The decomposition of rows is disjoint in \(v,t\). Thus these row sums are added as energies. Only the source's finitely many or divisor-bounded branches for the same row require Cauchy or Minkowski, already accounted for above.

### Step 4: bad-prime parts, cusps and the fixed ratio profile

The dual ramified and bad cube labels replace \(U_0\) by
\[
U_0/[3^m(Nb_S)^3].
\tag{6.21}
\]
Their row-vector weights are \(O(3^{-m/3}/Nb_S)\). In (6.14) and (6.16), the worst negative frequency exponent in the squared bound is \(U_0^{-1/3}\). After taking square roots for Minkowski, the corresponding extra factor is
\([3^m(Nb_S)^3]^{1/6}\).
The remaining mass is
\[
O(3^{-m/6}(Nb_S)^{-1/2}),
\tag{6.22}
\]
which is summable over the fixed-prime and ramified towers. The other terms are easier. This proves both entries of each minimum after the bad-label sum and hence permits their minimum in (6.2). The finitely many cusp, unit and bad squarefree sectors are retained exactly as in Section 3.

Finally write a general row as \(k=u z k_0\), with \(z\) supported on \(S\) and \(k_0\) good. The source's physical identity absorbs \(u,z\) into a fixed finite set of supplementary ray twists on the original good columns, preserving the cube coefficient and the original mask. In its sector the good row length is \(H/Nz\). Every term of (6.2), after substituting this length into \(U_0\), has a strictly positive power of \(H\): for the negative-frequency branch it is \(H^{1/3}\), and for the others it is at least this large. The resulting fixed-prime geometric sums over \(z\) converge. No dual bad-prime deletion is used.

All multipliers are separated by the source's common Mellin majorant before a sieve is applied. The ratio profile is compact: there is no small-\(x\) tail to sum in this theorem. This finishes the proof of (6.2). \(\square\)

### Corollary 6.2: the long-dual example holds over all rows

Use (4.1)--(4.3) and any fixed ratio profile \(\psi\). Then \(U_0=D^2\). The six terms of (6.2) are bounded by powers with exponents
\[
\frac52-\theta,\quad
\frac52-\theta,\quad
\frac73-\theta,\quad
2-\frac\theta2,\quad 2,\quad\frac53.
\tag{6.23}
\]
For \(0\leq\theta<1/2\), their maximum is \(5/2-\theta\). Therefore
\[
\boxed{
\sum_{0<Nk\asymp D^{3-\theta}}
|\mathcal C^\psi_{D^{1/2},\,1,\,D^{1/2},\,
D^{3/2-2\theta/3}}(k)|^2
\ll_\epsilon D^{5/2-\theta+\epsilon}.}
\tag{6.24}
\]
This includes all row square factors, sixth-power copies and fixed bad-prime parts. It still concerns the specified reflected ratio component. No sum over all small positive ratio scales, all cube scales, or all allocations is asserted to satisfy (6.24).

## 7. Reassessment of the remaining analytic problem

The newer pinned branches remove two obstacles that appeared in the earlier factorwise reflection analysis.

First, #920 supplies a source-conditional angular adapter for fixed infinity types \(+3\) and \(-3\). It gives conductor-uniform reciprocal control on every fixed line strictly to the right of \(11/12\). The earlier observation that the imported finite-order theorem did not by itself cover infinity type \(-3\) remains logically correct, but is no longer the missing statement on this smaller half-plane once that adapter is supplied.

Second, #922's complete finite-ray reunion cancels the artificial pole of its \(v\)-variable Euler decomposition. With that source's local variables \(x_p,z_p\), the reunion identity is
\[
(1-x_p+z_p)+z_p(-1+Np\,\mathbf1_{p\mid m})
=1-x_p+Np\,z_p\mathbf1_{p\mid m}.
\tag{7.1}
\]
The matching multiplier \(\kappa(p)\) is proved using the entire finite Fourier sum and all cusp coefficients. The old separate-ray pole is therefore not a valid obstruction for the reunited family. Nor can a spurious residue at that pole be used as a source of a new main-term cancellation.

The #922 spectral-row mean and second-reflection argument remain scalar-envelope estimates after the relevant signed variables have been bounded separately. Their stated normal-convergence domain gives no gain for the initial physical long-dual mean square. Applying the same theta functional equation twice restores the original conductor; the opposite angular derivative and the complete projection must be retained to see this. The present theorem changes an earlier use of Cauchy by placing \(gn\) in the quadratic column, rather than pretending that this involution alone decreases a scale.

A precise next target, within the present physical decomposition, is a bound improving
\[
U+(EU)^{2/3}
\tag{7.2}
\]
for the **literal signed coefficients** on the blocks
\[
EFG\asymp A,\quad G\ll\sqrt B,\quad
U\asymp H^2EG^2/(BF C^3),\quad C\ \text{small},
\tag{7.3}
\]
uniformly in all retained zero masks and in the auxiliary conductors needed by the original moment's Poisson comparison. An improvement confined to the row-dependent terms of (2.2) cannot accomplish this.

Theorem 6.1 also shows why an arbitrary-row obstruction must be phrased carefully: the actual reflected column shortens with the row's square part, and its localized physical family does admit a better all-row bound. That theorem does not estimate the sum of all small-ratio components; each such component changes the frequency scale and the source weight. Summing them without retaining their exact weights is not an allowed inference.

Establishing the required signed coefficient energy, together with the missing moving-auxiliary interface and its actual moment comparison, is still necessary before claiming the generalized moment theorem.

## 8. Computation and review boundary

The proof of Theorem 2.1 is analytic, using exactly (QLS), (CLS), divisor counting, and finite algebra. Theorem 6.1 also uses the explicitly pinned source local adapter and transformed-weight formulas. These are distinguished from the native exponent and Euler-product argument in its proof.

The companion finite diagnostic uses exact Eisenstein integer arithmetic for primitive sextic symbols, exact finite sums for the product, common-divisor and moving-mask identities, and rational arithmetic for the exponent identities. It checks its declared finite coverage with explicit failures. Its execution evidence and content hashes are recorded separately. Such a diagnostic does not test either analytic large sieve, the theta support theorem, an infinite Euler-product convergence statement, the angular reciprocal premise, or an infinite moment estimate.

No Lean build, global numerical moment evidence, independent reconstruction of every imported theta theorem, or RH validation is claimed. Any later independent review must bind this note's exact content hash and distinguish the native squarefree-row theorem from its source-qualified physical applications.
