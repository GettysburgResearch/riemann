# Centered two-column kernels, cube aliases, and joint correction tails

**Status:** proposed finite arithmetic identities and elementary analytic deductions. This note identifies and cancels the artificial principal correlations introduced by cube completion, proves a uniform \(R^{-1}\) bound for the principal energy of the actual long cube inverse, and gives a rapid-decay estimate for a specified portion of the strict two-column A2 comparison. It also records an exact single-divisor formula for a joint inverse cutoff.

**Scope:** the Eisenstein field, fixed bad set and finite ray data; all element rows in a complete smooth radial sum; literal zeros on nonunits; independent moving exclusions and fourth-power auxiliaries on the two columns; the original reconstructed product diagonal. No arbitrary subset of the row set is substituted for a complete smooth sum. The principal-energy estimate is a complete-residue, zero-frequency statement, not a bound for the entire finite-height row energy.

**What remains open:** the oscillating two-column remainder at the adverse initial height. In particular, the small-cube term \(U+(EU)^{2/3}\) in PR #926 is not removed by the principal projection proved here. Neither the full fourth moment nor a new zeta zero-free boundary follows.

## 1. Frozen dependencies and normalizations

The exact finite input is the A2 and cube interface already available at the following sources.

| Source | Pin and interface |
|---|---|
| PR #914 | 0cc0428fedbbfc340044c7451b3d392c1da9a103, *standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md*, Theorem 4.1 and equations (6.3), (6.5), (6.9) |
| PR #914 | Same pin, *CONDUCTOR_SECTORS.md*, Section 4: smooth primitive-character Poisson with every principal mask |
| PR #918 | cfa102748b26f840ccc4b963a660711424db0ec3, *standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md*, equations (2.4), (3.4), (3.10) |
| PR #924 | 725b2d25ab47e57500049d93985560098c7ef3fa, *standalone/2026-10-10-sextic-moving-labels/MIXED_LABEL_COMPLETION.md* and *ANISOTROPIC_A2_NORM_TRANSFER.md* |
| PR #925 | 506e3808d2f1e86a31a6d1f70cc7da58367c9918, *standalone/2026-10-10-joint-divisor-covariance/MOVING_AUXILIARY_ADAPTER.md*, Section 6; *JOINT_DIVISOR_MEAN.md*, Sections 1–3 |
| PR #926 | 086bf0560c0c2679a1fe41418f583d2c5ca743c3, *standalone/2026-10-10-mobius-overlaps-and-sampled-moments/JOINT_REFLECTED_BLOCKS.md*, Sections 2 and 5 |

The complete formulas above were read. The analytic ingredients newly used below are elementary ideal counting, finite character orthogonality, the primitive Gauss identity, and smooth lattice Poisson. The imported theta and large-sieve foundations are not needed to prove Sections 2–7, although the exact objects to which the results are applied retain their source qualifications.

Let \(N\) denote the ideal norm. All physical column ideals avoid the fixed set \(S\). Write
\[
\lambda(n)=\overline{\alpha(n)}\xi(n),\qquad
a_\xi(n)=\lambda(n)\gamma_2(n)
\]
on squarefree \(n\). Fixed finite ray changes on either factor axis are permitted with their actual multiplicative coefficients.

For any ideal \(n\), \(\chi_n(k)\) denotes its multiplicative sextic symbol. At a prime present in \(n\), an exponent divisible by six still gives a coprimality mask. An absent prime contributes the constant one, including at zero.

For every uniform \(D^\epsilon\) assertion below, first fix a ceiling exponent \(B_0\ge1\), the bad set, the finite ray family, and the smooth tests and their support intervals. Then let \(D\ge2\) and allow the finite arithmetic labels and positive physical scales to vary with norm or size at most \(D^{B_0}\); positive scales appearing in denominators also have reciprocal at most \(D^{B_0}\). Enlarging \(B_0\) once covers the products and child labels forced by the finite physical support. The implied constants may depend on \(B_0\), the fixed data, \(\epsilon\), and any stated positive margin, but not on the varying labels, their overlaps or \(D\). No cutoff on the row \(k\) is imposed in a complete Schwartz sum. Theorem 3.1 is itself uniform for arbitrary ideals and every \(X>0\), independently of this polynomial convention. The precise finite coefficient budget required in Theorem 7.1 is stated there.

## 2. The exact principal row kernel is larger than the product diagonal

For two ideal columns \(n,n'\), put
\[
M=\operatorname{rad}(nn'),\qquad
f=\prod_{\substack{p\mid M\\v_p(n)-v_p(n')\not\equiv0\pmod6}}p,
\qquad q_0=M/f.
\tag{2.1}
\]
The exact row character is
\[
\chi_n(k)\overline{\chi_{n'}(k)}
=\psi_{n,n'}(k)\mathbf1_{(k,q_0)=1},
\tag{2.2}
\]
where \(\psi_{n,n'}\) is primitive modulo \(f\) if \(f\ne1\). Every prime of \(q_0\) remains a zero of the original product on nonunit rows.

Define
\[
\delta_6(n,n')=
\mathbf1_{\ v_p(n)\equiv v_p(n')\ (6)\ {\rm for\ every}\ p},
\qquad
\rho(M)=\prod_{p\mid M}(1-(Np)^{-1}).
\tag{2.3}
\]

### Lemma 2.1. Complete-residue principal correlation

For any common squarefree period containing \(M\), the normalized average of (2.2) over its residue classes is
\[
\boxed{\Pi(n,n')=\delta_6(n,n')\rho(M).}
\tag{2.4}
\]

**Proof.** At a present prime \(p\), the row \(0\bmod p\) contributes zero. The sum on the nonzero residue classes is zero unless the difference of exponents is divisible by six; in that case it is \(Np-1\). An absent prime contributes one on every class. Chinese remaindering gives (2.4), including primes which occur in only one column with exponent six or a higher multiple. \(\square\)

Thus \(n=n'\) always gives a principal pair, but its converse is false for cube-completed columns. The factor \(\rho(\operatorname{rad}(nn'))\) cannot be replaced by one.

For a finite coefficient vector \(z_n\), define its principal energy by
\[
\|z\|_{\rm pr}^2
=\sum_{n,n'}z_n\overline{z_{n'}}\Pi(n,n').
\tag{2.5}
\]
This is nonnegative: it is the complete-residue average of the squared row polynomial. Its sesquilinear version satisfies Cauchy–Schwarz. Multiplication of a row polynomial by any fixed residue character or fixed coprimality mask is a contraction for this norm.

The ordinary product-diagonal mass is
\[
\|z\|_{\rm diag}^2
=\sum_n|z_n|^2\rho(\operatorname{rad}n).
\tag{2.6}
\]
One must combine every ordered factorization with the same product \(n\) before forming (2.6).

### Corollary 2.2. The finite A2 support has no additional principal aliases

For the full A2 support, every prime exponent in a reconstructed product is in
\[
\{0,1,3,4\}.
\tag{2.7}
\]
Consequently \(\delta_6(n,n')=1\) on this support exactly when \(n=n'\). Its principal energy is its actual product diagonal.

This also applies after the inverse A2 projection: the outer correction primes are excluded from the full child, so composing correction triples preserves the same exponent set. It does not apply after inserting unrestricted physical theta cubes.

## 3. The principal term and rapid remainder of a complete smooth row sum

Let \(w(z)=\Psi(|z|^2)\) be a fixed radial Schwartz function on \(\mathbb C\). Write
\[
\mathfrak c_\Psi
=\operatorname{covol}(\mathcal O_K)^{-1}
\int_{\mathbb C}\Psi(|z|^2)\,dz.
\tag{3.1}
\]
This specifies the leading lattice constant without changing the imported Fourier convention.

### Theorem 3.1. A uniform principal/remainder decomposition

For every \(X>0\), every \(A>0\), and \(M,f,q_0\) from (2.1),
\[
\boxed{
\begin{aligned}
\sum_{k\in\mathcal O_K}\Psi(Nk/X)
\chi_n(k)\overline{\chi_{n'}(k)}
={}&\mathfrak c_\Psi X\,\Pi(n,n')\\
&+O_{A,\Psi,K}\left(
\tau_K(q_0)\sqrt{Nf}
\left(1+\frac{X}{NM}\right)^{-A}
\right).
\end{aligned}}
\tag{3.2}
\]
When \(f=1\), the square-root factor is one. Restricting the left side to \(k\ne0\) subtracts only
\[
\Psi(0)\mathbf1_{n=n'=1}.
\tag{3.3}
\]
In particular, no zero-row correction occurs on the strict product off-diagonal.

**Proof for \(f\ne1\).** Expand the exact principal mask:
\[
\sum_{d\mid q_0}\mu_K(d)\psi_{n,n'}(d)
\sum_{h\in\mathcal O_K}
\Psi\!\left(\frac{Nh}{X/Nd}\right)\psi_{n,n'}(h).
\tag{3.4}
\]
Radiality removes the rotation from the generator of \(d\). Primitive character Poisson has zero constant frequency and Gauss coefficients bounded by \(\sqrt{Nf}\). If \(T=(X/Nd)/Nf\), its absolute value is bounded by
\[
C_{\Psi,K}\sqrt{Nf}\,
T\sum_{h\ne0}(1+\sqrt T\,|h|)^{-B}
\tag{3.5}
\]
for every chosen Fourier decay order \(B\). Lattice counting bounds (3.5) by \(C_{A,\Psi,K}\sqrt{Nf}(1+T)^{-A}\): for \(T\le1\) use the two-dimensional integral bound, and for \(T\ge1\) choose \(B\) larger than \(2A+2\). Since
\[
T\ge X/(Nq_0Nf)=X/NM,
\]
summing (3.4) proves the asserted error. The main term is zero by Lemma 2.1.

**Proof for \(f=1\).** Inclusion–exclusion gives unweighted lattice sums at scales \(X/Nd\), \(d\mid M\). Their leading terms sum to
\[
\mathfrak c_\Psi X\sum_{d\mid M}\frac{\mu_K(d)}{Nd}
=\mathfrak c_\Psi X\rho(M).
\]
The full-lattice discrepancy at scale \(T\) is \(O_{A,\Psi,K}((1+T)^{-A})\): this follows from Poisson for \(T\ge1\), and from direct Schwartz counting for \(T\le1\). Sum that error over \(d\mid M\), using \(T\ge X/NM\). This proves (3.2). Formula (3.3) is the literal value of the original characters at zero. \(\square\)

This is the rapid-decay refinement already implicit in PR #914's completion proof, with the discarded Fourier tail now retained. Its new application below is to the two independently corrected physical columns and their actual coupled scale.

No statement here holds for an arbitrary sharp subset of rows. In particular, a finite ray component or a selected reflected-ratio component cannot be substituted into (3.2) without its own row-character reconstruction.

## 4. The exact mixed cube inverse and its artificial aliases

Fix squarefree \(q,f\), an outer exclusion \(r\), and positive factor scales \(A_1,B_1\). Put \(L=A_1B_1\). The normalized raw polynomial is
\[
P(k)=\frac1{\sqrt L}
\sum_{\substack{an\ {\rm squarefree}\\(an,qS)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
\mathbf1_{(a,r)=1}W_1(Na/A_1)W_2(Nn/B_1).
\tag{4.1}
\]
Let \(C_{q,rh}(A_1,B_1/(Nh)^3;k,f)\) be the literal mixed completion of the sources. The finite inverse is
\[
P(k)=\sum_{\substack{h\ {\rm squarefree}\\(h,qfS)=1}}
\frac{\mu_K(h)\lambda(h)^3\chi_h(k)^3}{Nh}
C_{q,rh}(A_1,B_1/(Nh)^3;k,f).
\tag{4.2}
\]

After expanding the physical cube \(b\), set \(d=hb\). The summand at fixed \(a,n,d\), apart from its inverse divisor sign, is
\[
\frac{\sqrt{Nd}\lambda(d)^3}{\sqrt L}
a_\xi(an)\chi_{an}(f)^4\,
\chi_{an d^3}(k)\,
W_1(Na/A_1)W_2(Nn(Nd)^3/B_1),
\tag{4.3}
\]
with precisely
\[
an\ {\rm squarefree},\quad
(a,rd)=1,\quad(an d,qfS)=1.
\tag{4.4}
\]
There is no condition \((n,d)=1\). The row phase identity includes all its zeros.

At fixed \(a,n,d\), (4.3)–(4.4) do not depend on which divisor \(h\mid d\) was selected. Hence
\[
\sum_{h\mid d}\mu_K(h)=\mathbf1_{d=1}.
\tag{4.5}
\]
This coefficient identity holds before a row norm or any kernel is introduced.

For two columns with independent parameters, introduce separate \(a,n,d\) and \(a',n',d'\), and conjugate the full second coefficient. Any finite kernel
\[
K(k,an d^3,a'n'(d')^3)
\tag{4.6}
\]
is constant during the two divisor sums. Therefore the exact double inverse preserves that kernel and the strict reconstructed product selector. This includes the principal kernel (2.4), the original row-dependent kernel, and both different moving auxiliaries.

### Lemma 4.1. Classification of the cube aliases

Write \(m=an\), \(m'=a'n'\); both are squarefree. Then
\[
\boxed{
\delta_6(md^3,m'(d')^3)=1
\iff
m=m'\quad\hbox{and}\quad v_p(d)\equiv v_p(d')\pmod2
\text{ for every }p.}
\tag{4.7}
\]

**Proof.** Reduce the congruence of exponents modulo three first. Since the exponents of \(m,m'\) are zero or one, this forces \(m=m'\). The remaining congruence is \(3(v_p(d)-v_p(d'))\equiv0\pmod6\), which is exactly parity equality. \(\square\)

Equivalently,
\[
d=sj^2,\qquad d'=s(j')^2
\tag{4.8}
\]
for the same squarefree \(s\); no coprimality between \(s\) and \(j,j'\) is imposed. Distinct \(j,j'\) give distinct physical products with a principal correlation. Its exact density is
\[
\rho(\operatorname{rad}(m d d')).
\tag{4.9}
\]

The complete double inverse cancels every pair involving \(d\ne1\) or \(d'\ne1\), including all these aliases. Their vanishing does not follow from subtracting only equality of physical products inside each completed block.

### A finite truncation where an alias survives

Take good prime ideals of norms \(7,61,67\), and
\[
R=100,\qquad
d=\mathfrak p_7\mathfrak p_{61}^{\,2},\qquad
d'=\mathfrak p_7\mathfrak p_{67}^{\,2},\qquad m=m'=1.
\tag{4.10}
\]
The truncated inverse coefficients satisfy
\[
\sum_{\substack{h\mid d\\Nh\le100}}\mu_K(h)
=\sum_{\substack{h'\mid d'\\Nh'\le100}}\mu_K(h')=-1.
\tag{4.11}
\]
Both underlying physical cube norms fit in a common factor-of-two interval, since
\[
1<(67/61)^6<2.
\]
Although \(d^3\ne(d')^3\), their principal correlation is
\[
\boxed{\frac{23760}{28609}
=(1-1/7)(1-1/61)(1-1/67).}
\tag{4.12}
\]
The complete inverse coefficients at both \(d,d'\) are zero. This is a finite local witness to the difference between product-diagonal centering and principal-character centering. It is not a lower bound for the full original covariance.

## 5. A quantitative principal-energy bound for the long inverse

Let \(L_R\) be the portion of (4.2) with \(Nh>R\), for \(R\ge1\). In the regrouping (4.3), its coefficient is
\[
c_R(d)=\sum_{\substack{h\mid d\\Nh>R}}\mu_K(h).
\tag{5.1}
\]
It vanishes unless \(Nd>R\), and \(|c_R(d)|\le\tau_K(d)\).

### Theorem 5.1. Principal energy of the literal long tail

Uniformly in the stated labels, overlaps, support scales and outer masks,
\[
\boxed{\|L_R\|_{\rm pr}^2\ll_\epsilon D^\epsilon R^{-1}.}
\tag{5.2}
\]
Its genuine physical product-diagonal coefficient mass satisfies the same bound:
\[
\boxed{\|L_R\|_{\rm diag}^2\ll_\epsilon D^\epsilon R^{-1}.}
\tag{5.3}
\]
For two independent long tails and bounded fixed residue-character multipliers \(u(k),u'(k)\),
\[
\boxed{
\left|\langle uL_R,u'L'_{R'}\rangle_{\rm pr}\right|
\ll_\epsilon D^\epsilon(RR')^{-1/2}.
}
\tag{5.4}
\]
The corresponding principal contribution restricted off the reconstructed product diagonal is bounded by twice the same type of majorant. Multiplying a column by a fixed product shift, as in an A2 correction, is permitted.

**Proof.** Combine the finitely many factorizations \(an=m\) into their coefficient first. Its absolute value, before the \(\sqrt{Nd}/\sqrt L\) factor, is \(D^{\epsilon_0}\), uniformly in every retained mask, by the ideal divisor bound. Its support has
\[
Nm\asymp L/(Nd)^3
\tag{5.5}
\]
with fixed comparison constants.

Write \(d=sj^2\), \(s\) squarefree. For each fixed \(j\),
\[
\chi_{m d^3}(k)=\chi_{m s^3}(k)\mathbf1_{(k,j)=1}.
\tag{5.6}
\]
The reduced column \(m s^3\) has exponents in \(\{0,1,3,4\}\), and uniquely determines both squarefree \(m\) and squarefree \(s\), including when they overlap. Therefore distinct such reduced columns are orthogonal in the principal norm. The fixed \(j\)-mask is a contraction and is retained.

The coefficient at \(m,s\), for fixed \(j\), has absolute value at most
\[
D^{\epsilon_0}\frac{Nj\sqrt{Ns}}{\sqrt L}.
\]
By (5.5), ideal counting gives its total squared coefficient mass at most
\[
D^{\epsilon_0}(Nj)^{-4}
\sum_{\substack{Ns>R/(Nj)^2\\s\ {\rm squarefree}}}(Ns)^{-2}
\ll
D^{\epsilon_0}(Nj)^{-4}
\min\{1,(Nj)^2/R\}.
\tag{5.7}
\]
Every nonempty subunit scale in this count has a fixed support-dependent lower bound; an empty scale contributes nothing.

Apply Minkowski in the positive complete-residue norm over \(j\). The square roots of (5.7) sum to
\[
D^{\epsilon_0}\left[
R^{-1/2}\sum_{Nj\le\sqrt R}(Nj)^{-1}
+\sum_{Nj>\sqrt R}(Nj)^{-2}
\right]
\ll D^{\epsilon_0}R^{-1/2}\log(2D).
\tag{5.8}
\]
The actual \(j\)-support is polynomially bounded; if \(R\) exceeds physical support the tail is zero. This proves (5.2) after squaring and redistributing epsilon.

For (5.3), the map \((m,d)\mapsto md^3\) is injective because \(m\) is squarefree. The squared coefficient mass is bounded directly by
\[
D^{\epsilon_0}\sum_{Nd>R}(Nd)^{-2}
\ll D^{\epsilon_0}R^{-1}.
\tag{5.9}
\]
The density factors only decrease this positive accounting sum.

Cauchy–Schwarz for the principal norm proves (5.4). For the product diagonal use ordinary coefficient-space Cauchy–Schwarz and (5.3), after inserting zero coefficients at missing reconstructed products. Subtracting that diagonal proves the asserted off-diagonal bound. Different fourth-power auxiliaries only alter bounded, row-independent coefficients and exclusions. The fixed exterior A2 row phases are contractions; their zeros are not deleted. \(\square\)

The \(R^{-1}\) statement concerns exactly the principal portion of the tail. The old finite-height tail estimate has additional oscillating terms. It would be incorrect to replace its whole \(H\) term by \(H/R\) solely on the basis of (5.2).

### The actual coupled zero-frequency kernel

In the first-Poisson comparison the pair scale is
\[
X_{N,N'}=\frac{F^2\mathrm N(N)\mathrm N(N')}{H_{\rm orig}},
\qquad F=Nf.
\tag{5.10}
\]
Its zero-frequency kernel is
\[
\mathfrak c_\Psi\frac{F^2}{H_{\rm orig}}
\mathrm N(N)\mathrm N(N')\,\Pi(N,N').
\tag{5.11}
\]
The norm weights in this kernel factor between the columns. On a fixed pair of product annuli they are absorbed by multiplying each column's fixed smooth test by its normalized product variable. Theorem 5.1 therefore controls this exact zero-frequency contribution, including differing corrected auxiliaries, with the displayed additional scale factor. It does not replace the coupled remainder by a positive norm.

## 6. A joint cutoff with one Möbius divisor

The two inverse labels admit a further exact organization. Instead of the rectangular restriction \(Nh\le R,\ Nh'\le R\), impose
\[
N\operatorname{lcm}(h,h')\le R.
\tag{6.1}
\]
All other factors and the full kernel are unchanged.

### Proposition 6.1. Joint lcm divisor identity

After fixing the physical cube products \(d=hb\), \(d'=h'b'\), the coefficient of this joint truncated inverse is
\[
\boxed{
\sum_{\substack{h\mid d,\ h'\mid d'\\
N\operatorname{lcm}(h,h')\le R}}
\mu_K(h)\mu_K(h')
=
\sum_{\substack{\ell\mid\operatorname{rad}(dd')\\N\ell\le R}}
\mu_K(\ell).
}
\tag{6.2}
\]

**Proof.** Group the left side by \(\ell=\operatorname{lcm}(h,h')\). At a prime which occurs in just one of \(d,d'\), the local coefficient for its occurrence in \(\ell\) is \(-1\). At a prime occurring in both, the three possible assignments have weights
\[
-1,\quad-1,\quad+1,
\]
whose sum is \(-1\). The empty assignment has coefficient one. Therefore the total coefficient for each squarefree \(\ell\mid\operatorname{rad}(dd')\) is \(\mu_K(\ell)\). This proves (6.2). \(\square\)

The identity retains all the original kernel dependence because the factors in (4.3)–(4.6) have already been reunited at fixed \(d,d'\). It is valid for different left and right characters, auxiliary ideals and masks: their constraints on the combined physical cube indices are fixed before the divisor sum.

This is a signed two-column operator identity. Its truncation is not positive and is not uniformly better than rectangular truncation. For instance, with \(d=\mathfrak p_7^2\), \(d'=\mathfrak p_{13}^2\), and \(R=20\), both separate truncated Möbius sums vanish, but the right side of (6.2) is \(-1\). The witness (4.10) gives \(-2\) for (6.2), compared with \(+1\) for the rectangular coefficient. A future estimate may use the single divisor variable, but positivity or an automatic saving is unavailable.

## 7. A rapid-decay region of the actual strict coupled comparison

For an ideal \(N\), define its radical defect
\[
\Delta(N)=\frac{\mathrm N(N)}{\mathrm N(\operatorname{rad}N)}.
\tag{7.1}
\]
For a pair put
\[
G(N,N')=N\gcd(\operatorname{rad}N,\operatorname{rad}N').
\]
The exact identity
\[
\mathrm N(\operatorname{rad}(NN'))
=\frac{\mathrm N(N)\mathrm N(N')}
{\Delta(N)\Delta(N')G(N,N')}
\tag{7.2}
\]
gives, at the physical coupled scale (5.10),
\[
\boxed{
\frac{X_{N,N'}}{\mathrm N(\operatorname{rad}(NN'))}
=
\frac{F^2\Delta(N)\Delta(N')G(N,N')}{H_{\rm orig}}
=:\Lambda(N,N';f).
}
\tag{7.3}
\]

### Theorem 7.1. Strict A2 covariance with large \(\Lambda\)

Consider any finite two-column expression obtained by the exact A2 forward or inverse identities from the physical comparison, before unrestricted theta cubes are introduced. Keep the two independent correction labels, both auxiliaries, every exterior phase, and the original strict selector \(N\ne N'\). On any subcollection with
\[
\Lambda(N,N';f)\ge D^\delta,\qquad \delta>0\text{ fixed},
\tag{7.4}
\]
its complete smooth row contribution is \(O_{J,\delta}(D^{-J})\) for every prescribed \(J>0\), after summing all its polynomially bounded labels and coefficients.

The same conclusion holds with the full original signed \(b,f\) weights and any row-independent column selector retained, provided the same polynomial support ceiling is kept.

More precisely, fix \(\delta>0\) and a coefficient-budget exponent \(C_0\). Write the selected expression as
\[
\sum_{i\in I_D} z_i
\sum_{k\ne0}\chi_{N_i}(k)\overline{\chi_{N'_i}(k)}
\Psi\!\left(\frac{H_iNk}{(Nf_i)^2\mathrm N(N_i)\mathrm N(N'_i)}\right),
\]
where \(I_D\) is finite, the coefficients \(z_i\) are row-independent, both columns have exponents in \(\{0,1,3,4\}\), and \(N_i\ne N'_i\). Put \(f_{{\rm res},i},q_{0,i}\) for the two ideals in (2.1). Assume exactly
\[
\sum_{i\in I_D}|z_i|\tau_K(q_{0,i})\sqrt{Nf_{{\rm res},i}}
\le D^{C_0}.
\tag{7.5a}
\]
Then for every \(J>0\), selecting any terms with
\(\Lambda(N_i,N'_i;f_i)\ge D^\delta\) gives
\(O_{\Psi,K,\delta,J,C_0}(D^{-J})\). An additional row-independent selector of modulus at most one is allowed. A fixed finite family of profiles \(\Psi\), or a family bounded in the finitely many Schwartz seminorms used for the selected decay order, is allowed with its stated seminorm constant. This formulation specifies all uniform quantifiers without an assumption of cancellation among the coefficients.

**Proof.** Corollary 2.2 makes every strict pair nonprincipal. Apply (3.2) at \(X=X_{N,N'}\). Its main term vanishes, and its error is
\[
O_{A,\Psi,K}\bigl(\tau_K(q_0)\sqrt{Nf_{N,N'}}(1+\Lambda)^{-A}\bigr).
\tag{7.5}
\]
Sum this bound with the coefficient budget (7.5a), and choose \(A>(J+C_0)/\delta\). This gives the asserted \(D^{-J}\) bound. The physical A2 application satisfies (7.5a) by the explicit count below. Signs were retained in the exact expression; taking absolute values after the complete row cancellation is valid. \(\square\)

This theorem controls a selected signed sesquilinear expression. It does not use monotonicity of an indefinite covariance or separate positive norms.

The only exterior row phases allowed here are the actual A2 phases already incorporated into \(N,N'\). The arbitrary bounded residue-character multipliers permitted in Theorem 5.1 do not automatically extend Theorem 7.1: with distinct primes \(N=p,N'=q\), multiplying the two columns by \(\overline{\chi_p(k)}\) and \(\overline{\chi_q(k)}\) changes their strict pair to the principal mask at \(pq\). Any proposed extra row twist requires recomputing the actual row conductor and principal term first.

### The literal outer coefficients and a finite counting ceiling

Here is the direct application to PR #914 equation (6.3), including its original normalization. Start with
\[
v(n)=\sum_{ab=n}V(Na/A,Nb/B),\qquad L=AB.
\]
For fixed original Poisson labels \(b,f\), distribute \(bf=r_1r_2\) between the two factor axes and put
\[
A_\alpha=A/Nr_1,\qquad B_\alpha=B/Nr_2,\qquad
V_*(x,y)=(xy)^{-1/2}\overline{V(x,y)}.
\]
The original residual coefficient is exactly
\[
R_L(bfm)=
\sum_{r_1r_2=bf}\ \sum_{an=m}
V_*(Na/A_\alpha,Nn/B_\alpha)
\]
on the surviving squarefree support; the fourth-power auxiliary character enforces \((m,f)=1\), and the original mask enforces \((m,bS)=1\). Both left and right allocations are retained independently.

Apply the normalized inverse A2 identity to each allocated raw column. For \(t=(c,d,e)\), let \(C=cde\), \(s_t=c^3d^3e^4\), and let \(A_{\alpha,t},B_{\alpha,t}\) be the exact child scales (4.3) of the source, starting from \(A_\alpha,B_\alpha\). A child full pair \((n_1,n_2)\) contributes row character \(\chi_N(k)\), where \(N=s_tn_1n_2\), with the row-independent coefficient
\[
\begin{split}
E_{\alpha,t,n_1,n_2}(f)
={}&
\frac{\mu_K(C)\lambda(C)^3a_\xi(e)\chi_e(f)^4}
{Nc\,Nd\,(Ne)^{3/2}\sqrt{A_{\alpha,t}B_{\alpha,t}}}\\
&\quad\times
\mathfrak a_\xi(n_1,n_2)\chi_{n_1n_2}(ef)^4
V_*(Nn_1/A_{\alpha,t},Nn_2/B_{\alpha,t}).
\end{split}
\tag{7.5b}
\]
Its exact support includes disjoint squarefree \(c,d,e\), \((C,bfS)=1\), and \((n_1n_2,bCS)=1\). In particular \(ef\) is squarefree and the overlap of the child exclusion \(bC\) with \(ef\) at \(e\) is retained. The exterior row factor is already absorbed into \(\chi_N(k)\); no row-dependent coefficient was silently placed in (7.5b).

The original strict form is consequently the finite sum
\[
\begin{split}
\mathcal O_\xi[v]
={}&\frac{H_{\rm orig}}L
\sum_{\substack{b,f\ {\rm squarefree}\\(b,f)=1\\(bf,S)=1}}
\frac{\mu_K(f)}{Nf}
\sum_{\alpha,\alpha'}\sum_{t,t'}\sum_{n_1,n_2,n'_1,n'_2}
E_{\alpha,t,n_1,n_2}(f)
\overline{E_{\alpha',t',n'_1,n'_2}(f)}
\mathbf1_{N\ne N'}\\
&\qquad\times
\sum_{k\ne0}\chi_N(k)\overline{\chi_{N'}(k)}
\Psi\!\left(
\frac{H_{\rm orig}Nk}{(Nf)^2\mathrm N(N)\mathrm N(N')}
\right).
\end{split}
\tag{7.5c}
\]
The prefactor follows from
\(A_\alpha B_\alpha=L/(Nb\,Nf)\): multiplying both normalized columns back changes \(H_{\rm orig}\mu_K(f)Nb/L^2\) to \(H_{\rm orig}\mu_K(f)/(L\,Nf)\). Thus the signed \(\mu_K(f)\), the original Poisson label \(b\), the two generally different auxiliaries \(ef,e'f\), and the exact original coupled scale all appear in (7.5c). The strict selector is imposed on the reconstructed products, not on the factor pairs.

For a concrete polynomial bound, enlarge the fixed ceiling \(B_0\) once so every ideal among \(b,f,c,d,e,n_1,n_2,c',d',e',n'_1,n'_2,N,N'\), and every starting positive scale and its needed reciprocal, is at most \(D^{B_0}\). There are twelve freely counted ideal indices before the two \(bf\)-allocations; ideal counting bounds their number by \(O_K(D^{12B_0})\). The two allocations cost at most \(\tau_K(bf)^2=D^\epsilon\). On a nonempty child the two scales have fixed positive lower bounds. The finite A2 coefficient formula gives
\(\lvert\mathfrak a_\xi(n_1,n_2)\rvert\le\sqrt{\mathrm N(n_1n_2)}\le D^{B_0}\); all other numerator phases in (7.5b) have modulus at most one. Hence each \(E\) is \(O(D^{B_0})\), the exterior \(H_{\rm orig}/(L\,Nf)\) is at most \(D^{2B_0}\), and \(\sqrt{Nf_{\rm res}}\le D^{B_0}\). The divisor factor in (7.5a) is another subpower. The entire coefficient budget is therefore
\[
O_{\epsilon,B_0,K,V}(D^{17B_0+\epsilon}).
\]
Increasing \(C_0\) by a fixed amount absorbs that implied constant for \(D\ge2\). This deliberately coarse ceiling is sufficient for every prescribed rapid-decay power. Forward A2 terms omit \(\mu_K(C)\) and satisfy the same accounting. A fixed finite number of further forward/inverse compositions changes the finite ceiling, while (7.5a) remains the exact hypothesis.

### Explicit correction labels

For a full A2 product
\[
N=ab\,c^3d^3e^4,\qquad C=cde,
\]
with the five labels disjoint and squarefree,
\[
\Delta(N)=(NC)^2Ne.
\tag{7.6}
\]
For outer inverse-projection labels \(t=(c,d,e)\), a full child can add further disjoint corrections, so at least
\[
\Delta(N)\ge (NC)^2Ne.
\tag{7.7}
\]
Consequently a sufficient correction condition in Theorem 7.1 is
\[
\boxed{
F^2(NC\,NC')^2\,Ne\,Ne'\,G(N,N')
\ge H_{\rm orig}D^\delta.
}
\tag{7.8}
\]
A simpler sufficient condition, independent of the inner full-child corrections, is
\[
F\,NC\,NC'\ge H_{\rm orig}^{1/2}D^{\delta/2}.
\tag{7.9}
\]

The selector can be imposed on the two outer correction labels before expanding their full children, using (7.7). It then specifies a genuine portion of the lifted comparison. It is generally not a selector of an original raw column alone: different correction subdivisions of the same reconstructed column may fall on opposite sides of that cutoff. All retained phases and the pulled-back equality are necessary for its meaning.

If one instead selects by the exact invariant \(\Lambda(N,N';f)\), all subdivisions of a fixed pair agree, and the exact inverse may be reunited before or after imposing the selector. This distinction prevents an artificial correction restriction from being mistaken for a new native moment sector.

### The raw first-Poisson auxiliary/gcd specialization

In PR #914's uncompleted strict expression, write
\[
m_1=g r_1,\qquad m_2=g r_2,\qquad(r_1,r_2)=1,
\qquad m_1\ne m_2.
\]
The primitive residual conductor is \(r_1r_2\), and the principal mask is \(g\). Thus
\[
\boxed{
\begin{aligned}
\left|\sum_{k\ne0}
\chi_{m_1}(k)\overline{\chi_{m_2}(k)}
\Psi\!\left(\frac{H_{\rm orig}Nk}
{F^2Nm_1Nm_2}\right)\right|
\ll_{A,\Psi,K}
\tau_K(g)\sqrt{N(r_1r_2)}
\left(1+\frac{F^2Ng}{H_{\rm orig}}\right)^{-A}.
\end{aligned}}
\tag{7.10}
\]
All \(f\)-twist phases and residual weights can multiply this exact kernel. Equation (7.10) is a quantified auxiliary/common-gcd cutoff in the literal signed comparison. It is an elementary Fourier-decay refinement, not a new subconvex theorem.

### Comparison with the existing completion tail

For the leading balanced initialization,
\[
L=D^2,\qquad H_{\rm orig}=D^{1+\vartheta},\qquad
H_{\rm dual}\asymp D^{3-\vartheta},\qquad F=1.
\]
The old positive A2 tail theorem controlled a single correction tail
\[
NC\ge D^{(1+\vartheta)/6}
\]
at energy \(O(D^\epsilon H_{\rm dual})\). The present joint strict-covariance estimate gives rapid decay when
\[
NC\,NC'\ge D^{(1+\vartheta)/2+\eta}
\tag{7.11}
\]
for any fixed positive \(\eta\), or a larger region when the \(e,e'\) and cross-radical factors in (7.8) are retained.

These conclusions have different objects and different strengths. The new statement gives a much stronger error on its joint region; it does not dominate the previous single-column tail cutoff. The all-unit, coprime pair has \(\Lambda=H_{\rm orig}^{-1}\), so it is untouched.

## 8. Why this does not delete the small-cube obstruction in PR #926

In the notation of *JOINT_REFLECTED_BLOCKS.md*, the grouped quadratic coefficient is
\[
\beta_m
=\sum_{gn=m}a_gc_n
\sum_e b_e\mathbf1_{(g,e)=1}\chi_n(e)^4.
\tag{8.1}
\]
Its bound contains the cubic coefficient energy
\[
E+U+(EU)^{2/3}.
\tag{8.2}
\]
The long-column term of the quadratic sieve leaves \(U+(EU)^{2/3}\) even after the improved \(g\)-average. These are not labels for the artificial aliases in Section 4.

A direct arbitrary-vector witness rules out removing the \(U\) contribution from a generally centered version of that theorem. Set \(E=G=H=1\), choose \(e=g=k=1\), and take \(c_n=1\) on \(M\) distinct squarefree columns in the \(U\)-annulus. Then
\[
\mathscr Q_1=M/\sqrt U,\qquad
\text{product diagonal}=M/U,
\]
so
\[
\boxed{\text{centered covariance}=(M^2-M)/U.}
\tag{8.3}
\]
All row masks are one in this example. There are no cube labels, no nonsquarefree columns and no sixth-power aliases. When the annulus has \(M\asymp U\) admissible ideals, (8.3) is of order \(U\). The finite diagnostic also checks the explicit two-column instance with norms \(7,13\) and \(U=7\).

This witness concerns the permitted arbitrary separate vectors in PR #926. Its \(c_n=1\) is not asserted to be the literal reflected Gauss vector. It proves the narrower, needed conclusion: product-diagonal subtraction alone does not justify deleting \(U\), and the principal-alias cancellation here does not supply a new bound for the literal \(\beta_m\) energy.

The new identities isolate the true remaining task: estimate the complete oscillating two-column kernel, or the actual reflected Gauss coefficient covariance, after the exact principal subtraction. A generic positive large-sieve envelope does not provide that estimate.

## 9. Finite diagnostics and their limits

The accompanying *check_principal_aliases.py* uses exact arithmetic in \(\mathbb Z[\zeta_6]\), rational densities and integer ideal-norm models. Its assertions exhaust:

- 784 local complete-residue correlations at prime norms \(7,13,61,67\), including absent primes and positive exponents divisible by six;
- 4,096 two-prime cube-pair classifications, finding 192 off-product principal pairs;
- 2,304 complete masked cube inverses, with overlapping auxiliary/exclusion masks;
- 160 cube phase identities at nonunits, including shared inverse/physical cube primes;
- 1,792 joint lcm cutoff identities;
- 256 A2 no-alias and radical-defect identities.

The report records the surviving alias (4.10), the failure of lcm and rectangular cutoffs to agree, and the finite centered witness (8.3). The local character choice is any primitive sixth-order residue character; orthogonality is orientation-independent. These tests do not reconstruct the source's individual Gauss phases.

The first diagnostic run caught a coding error that used a nonzero exponent rather than a Boolean support indicator in a radical norm. It was corrected before the passing report was produced. No mathematical theorem was inferred from that failed run.

The written proofs, rather than the finite checks, establish the uniform principal-energy and rapid-decay statements. No infinite theta theorem, finite-height centered moment, zero-free boundary, or RH claim was computationally verified.

The diagnostic refuses Python optimization mode, which would disable its assertions. Its output includes the SHA-256 of both its own source and this manuscript. An output-path option permits an independent rerun without overwriting the frozen report; an expected-manuscript-hash option rejects a mismatched manuscript before running the finite checks.

