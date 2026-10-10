# Independent review of the two-variable cube inverse

**Verdict: PASS at the stated source-qualified scope.** The final note removes the cube completion from the literal squarefree two-factor polynomial over squarefree primary rows. Its exact inverse, three coprimality corrections, norm factors, support restriction, and exponent optimization are correct. The range \(H\le D^{19/36}\) additionally uses the named source-conditional scalar bound with \(\beta=11/12\). This review does not certify the full fourth moment, a centered covariance estimate, arbitrary rows, or RH.

## 1. Exact reviewed snapshot and dependencies

| Item | SHA-256 |
|---|---|
| cube_inverse_attack.md, reviewed final source | a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804 |
| centered_a2_attack.md | bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a |
| reunited_cusp_cutoff.md | 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340 |
| all_cusp_gauss_factorization.md | b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c |
| Independent all-cusp input review | 72f1161caedf998029d8f08a97ef52e5620b97f94476461fac80c1fde8db8988 |

I read the complete final source, the exact imported formulas labelled eq:T, eq:completed-twist, and eq:cube-inverse in the October 5 paper2.tex at OpenAI math pin adc7f1241b42e322a6451854ab7e4b4c146bf78a, and the coupled reflection and quadratic–cubic lemma in PR #915 at 9959364671f89b86f3992ec5ed5e19f804eb607b.

This review concerns the new inverse adapter. The all-cusp factorization and support theorem are expressly retained as companion inputs with their separate independent reviews. The imported automorphy and classical upper sieves have not been reconstructed here.

I first read the mathematical draft at 5f76ff573234e429cb5e97b66e80876f5694dfbbd8015cd0b392f967bd3dd150. That reading found no substantive defect and requested a precise direction for the initial smooth cutoff and proper inline math delimiters. The final version resolves both and replaces the valid Euler-correction argument by a simpler finite shared-divisor identity. I checked that replacement directly, rather than treating it as an editorial change. The affirmative verdict binds only the final snapshot above.

## 2. Cube inverse, normalization, and zero masks

The source identity has inverse coefficient exactly

\[
\frac{\mu(h)\alpha(h)^{-3}\Psi_{k,a}(h)^3}{Nh}.
\]

Its cube twist satisfies

\[
\Psi_{k,a}(h)^3
=\xi(h)^3\chi_h(k)^3\chi_h(a)^{12}
=\xi(h)^3\chi_h(k)^3\mathbf1_{(h,a)=1}.
\]

Thus the new condition is \((h,a)=1\). No \((h,n)=1\) or condition involving the later dual theta indices is produced.

The normalization can be verified without invoking the labelled source lemma. Substituting the definition of \(T\) and writing the total cube index as \(c=hb\) leaves the coefficient \(\alpha(c)^{-3}\Psi_{k,a}(c)^3/Nc\), multiplied by \(\sum_{h\mid c}\mu(h)\). This selects \(c=1\). The remaining test satisfies

\[
V_*(Nn/B)/\sqrt{Nn}=B^{-1/2}W_2(Nn/B).
\]

Multiplication by the outer \(A^{-1/2}\) and the coprime Gauss CRT identity gives exactly the normalized polynomial \(P_{A,B}\) in the note. No factor \(Nh^{1/2}\) or \(Nh^{3/2}\) is missing from the inverse coefficient.

The whole inverse term vanishes for \((Nh)^3>v_2B\). The final note inserts a smooth cutoff equal to one for \((Nh)^3\le v_2B\) and zero for \((Nh)^3\ge2v_2B\). This is an exact insertion and avoids applying the smooth scalar hypothesis to a sharp terminal interval.

## 3. Both scalar factors have the admitted angular type

After the fixed row ray class is chosen, quadratic reciprocity changes \(\chi_h(k)^3\) to \(\chi_k(h)^3\) times fixed finite ray factors and a bounded row scalar. Their nonunit zeros agree. The two remaining scalar factors therefore have the form

\[
\mu(r)\eta_i(r)\alpha(r)^{-3}\chi_k(r)^3,
\]

with possibly different fixed finite \(\eta_i\). The required angular exponent is \(-3\) in both sums. The companion scalar theorem covers each such finite twist. No theorem for arbitrary coefficients or a finite-order substitute is used.

For two coprime squarefree variables \(r_1,r_2\), expanding their common-divisor mask and writing \(r_i=\ell s_i\) gives

\[
B_C
=\sum_{(\ell,CS)=1}^{*}
\mu(\ell)\lambda_{1,k}(\ell)\lambda_{2,k}(\ell)
M_{\eta_1,C\ell}(k;L_1/N\ell)
M_{\eta_2,C\ell}(k;L_2/N\ell).
\]

The restrictions \((s_i,\ell)=1\) are necessary consequences of squarefreeness and are included through \(C\ell\). There is no residual \((s_1,s_2)=1\) condition. The extracted quadratic row factor is \(\chi_k(\ell)^6=\mathbf1_{(k,\ell)=1}\), so the common prime zero survives.

Applying the two uniform scalar estimates costs

\[
(L_1L_2)^\beta\sum_\ell(N\ell)^{-2\beta},
\]

which converges precisely under the stated \(2\beta>1\). The extracted angular power \(-6\) is used only as a bounded multiplier; no scalar input at angular type \(-6\) is asserted. The moving exclusions \(C\ell\) are polynomially bounded because only \(\ell\) bounded by both compact-support lengths can contribute.

## 4. Exact joint support and smooth separation

For each fixed inverse label \(h\), the reunited-divisor theorem applies with completion scale \(B/(Nh)^3\). The extra mask \((h,a)=1\) is independent of the theta frequency and therefore does not interfere with that pointwise theorem.

Consequently a reunited term with negative label \(g\) vanishes when

\[
(Ng)^2(Nh)^3>C_*B.
\]

The note inserts a smooth function of this ratio before dividing the positive label into the two frequency-dependent allocations \(e,f\). That order is essential. The proof never claims that an unmodified individual \(e,f,g\) component vanishes separately.

On a nonempty smooth block \(Ng\asymp G\), \(Nh\asymp Z\), the parameter \(G^2Z^3/B\) is bounded. The cutoff is therefore a smooth function of the normalized variables with uniform derivatives. The original smooth \(h\)-cutoff has the same property. These cutoffs may be separated with the source kernel before the scalar estimates.

After extracting \(g=d\ell g''\) and \(h=j\ell h''\), the normalized ratios are unchanged:

\[
\frac{Ng}{G}=\frac{Ng''}{G/(NdN\ell)},\qquad
\frac{Nh}{Z}=\frac{Nh''}{Z/(NjN\ell)}.
\]

Thus the Mellin seminorms and tail majorants remain uniform. Every scalar conductor and exclusion involves only the row and finite original allocation/inverse labels, not an uncontrolled dual theta frequency.

## 5. Two intersections with the squarefree theta allocation

The arithmetic expression retains

\[
\mathbf1_{(g,ef)=1}\mathbf1_{(h,efg)=1}
\mathbf1_{(k,ef)=1}\chi_{n_0}(e)^4.
\]

Keep \((g,h)=1\) while expanding the two masks involving \(e\). If \(d\mid e,g\) and \(j\mid e,h\), then \((d,j)=1\), and one may write

\[
e=dj e',\quad g=dg',\quad h=jh'.
\]

The remaining scalar exclusions are exactly \(fdj\), together with \((g',h')=1\). The \(e'\)-vector retains its separate \(djf\)-exclusion, and the \(n_0\)-vector retains \(\chi_{n_0}(dj)^4\) and its \(f\)-exclusion. The moving row mask \((k,e')=1\) survives.

There is no residual mask between \(e'\) and either scalar variable. The note explicitly uses the separated product expression as an extension away from its original coprime support inside this exact inclusion–exclusion. That is legitimate; it does not apply an arithmetic identity for a nonsquarefree outer index.

Applying the shared-divisor lemma to \(g',h'\) introduces \(\ell\), which is coprime to \(fdj\), but may share primes with \(e'\). The final text correctly forbids inserting \((e',\ell)=1\). Such an insertion would destroy the cancellation of the common three-variable patterns.

All factors depending on fixed extracted labels go into separate column vectors or retained row contractions. The two scalar sums consequently become a bounded row multiplier independent of \(e',n_0\), as required before using the quadratic–cubic norm.

## 6. Norm factors and all reflected tails

The additional inverse weight contributes \(1/Z\), so the common amplitude is

\[
\frac{3^{-m/3}}{Z\sqrt{AFG}\,Nb'}.
\]

The new effective squarefree length is

\[
U\lesssim\frac{Y}{3^mNn_S(Nb')^3},\qquad
Y=\frac{H^2EG^2Z^3}{BF}.
\]

The factor \(Z^3\) is exactly the result of replacing the completion length by \(B/(Nh)^3\).

After the two scalar bounds and Minkowski over the \(O(F)\) frozen \(f\)-labels, the squared prefactor is

\[
\frac{F^2}{AFGZ^2}
(G/Nd)^{2\beta}(Z/Nj)^{2\beta}
\frac{E}{NdNj}
\asymp
G^{2\beta-2}Z^{2\beta-2}
(Nd)^{-2\beta-1}(Nj)^{-2\beta-1}.
\]

Thus the two outer divisor sums have norm weights \((Nd)^{-\beta-1/2}\) and \((Nj)^{-\beta-1/2}\), both summable for \(\beta>1/2\). Together with the previous \((N\ell)^{-2\beta}\) cost, all three shared-prime corrections are controlled.

The residual quadratic–cubic lemma includes the moving mask \((k,e')=1\). Its expanded bracket is bounded by \(HE+Y+(EY)^{2/3}\) on the effective range. The source kernel handles the larger \(U\)-dyads by arbitrary decay. Nonempty shifted subunit lengths have fixed positive lower bounds from the compact dyadic supports, so counting handles them without an arithmetic-scale loss.

The full reflected cube index \(b'\), including every bad-prime power, is frozen before the sieves. On each dyad its reciprocal-norm mass is bounded. The ramified factor \(3^{-m/3}\) is summable for \(m\ge-4\); the finitely many negative exponents change constants only. The finite squarefree bad-prime part \(n_S\) and fixed ray families add constants. These are the previously reviewed all-cusp tail arguments with the new smooth \(h\)-ratio included; their uniformity survives the three divisor extractions.

## 7. Optimization and exact resulting scope

The proved block estimate is

\[
D^\epsilon G^{2\beta-2}Z^{2\beta-2}
[HE+Y+(EY)^{2/3}],
\quad EFG\asymp A,\quad G^2Z^3\ll B.
\]

Using these constraints, its three terms are bounded by

\[
HA,\qquad H^2A B^{(2\beta-2)/3},\qquad
H^{4/3}A^{4/3}B^{(2\beta-2)/3}.
\]

The powers of \(G\) left after applying the joint support are \((2\beta-5)/3\) and \((2\beta-6)/3\), both negative on the stated interval. This verifies the complete anisotropic estimate.

For \(A=B=D\), the energy is therefore at most

\[
D^\epsilon
[HD+H^2D^{(1+2\beta)/3}+H^{4/3}D^{(2+2\beta)/3}].
\]

The middle term imposes the strongest condition,

\[
H\le D^{(5-2\beta)/6}.
\]

At \(\beta=11/12\), the second and third column exponents are \(17/18\) and \(23/18\), and the range is \(H\le D^{19/36}\). At \(\beta=1\), elementary scalar counting gives only \(H\le D^{1/2}\). The completed range \(D^{19/24}\) is not carried unchanged through the inverse.

The conclusion estimates the literal cube-free polynomial, not only its completion. It still uses squarefree primary rows outside \(S\), no growing auxiliary family, and a positive norm. It does not cover the adverse initial dual range of the fourth moment or its centered signed covariance.

No new finite computation was used as a substitute for the analytic proof. This PASS verdict rests on the exact identities, the explicitly uniform scalar premise, the reviewed all-cusp/support inputs, and the norm calculation above. No mathematical repair remains outstanding in the reviewed final source.

