# Second independent review of the simultaneous cube inverse

**Verdict: PASS, subject to the explicitly named analytic inputs.**

The frozen argument correctly removes the cube completion and estimates the literal two-factor squarefree polynomial. Both angular Möbius sums can be bounded with the stated scalar exponent while retaining their mutual coprimality and their intersections with the positive squarefree divisor. The joint support restriction is inserted at the correct stage. The final balanced row exponent \(19/36\) follows; the larger completed-sum exponent \(19/24\) is not asserted after inversion.

## 1. Reviewed snapshot and dependency boundary

| Reviewed file | SHA-256 |
|---|---|
| cube_inverse_attack.md | a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804 |

The review is bound to these companion inputs:

| Input | SHA-256 |
|---|---|
| centered_a2_attack.md | bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a |
| reunited_cusp_cutoff.md | 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340 |
| all_cusp_gauss_factorization.md | b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c |

I read the complete frozen note and directly checked the imported source's eq:T, eq:completed-twist, and eq:cube-inverse at OpenAI/math commit adc7f1241b42e322a6451854ab7e4b4c146bf78a. The literal scalar cancellation and quadratic–cubic composition retain the PR #915 pin 9959364671f89b86f3992ec5ed5e19f804eb607b. The exact support cutoff and the all-cusp coefficient extension have separate independent reviews.

The present audit verifies the new finite inversion, arithmetic masks, interfaces between these inputs, norm factors, and exponent optimization. The classical automorphy and upper large sieves remain named inputs. The scalar exponent \(11/12\) remains conditional on the companion canonical/angular adapter. No imported global main theorem or full moment hierarchy is certified by this verdict.

## 2. The finite cube inverse and its normalization: PASS

The source inverse has the coefficient

\[
\frac{\mu(h)\alpha(h)^{-3}\Psi_{k,a}(h)^3}{Nh}.
\]

The exponent twelve in the auxiliary factor gives exactly

\[
\chi_h(a)^{12}=\mathbf1_{(h,a)=1},
\]

including its nonunit zeros. Thus the inverse introduces the outer-divisor mask \((h,a)=1\), and no condition \((h,n)=1\).

Substituting the full completion provides an independent normalization check. With total cube index \(c=hb\), complete multiplicativity gives \(1/Nc\), the combined angular/ray/row coefficient at \(c\), and the test argument \(Nn(Nc)^3/B\). The divisor sum \(\sum_{h\mid c}\mu(h)\) is zero unless \(c=1\). The remaining weight satisfies

\[
\frac{V_*(Nn/B)}{\sqrt{Nn}}
=\frac{W_2(Nn/B)}{\sqrt B}.
\]

After multiplying by the original outer coefficient and using Gauss CRT, the left side is exactly \(P_{A,B}(k)\) in (1.3). In particular there is no missing factor \(Nh^{\pm1/2}\), no extra inverse-cube weight, and no new coprimality mask involving the squarefree theta variable.

Compact support makes the unreflected inverse finite: each complete \(h\)-term is zero for \((Nh)^3>v_2B\). Inserting the specified smooth function of \((Nh)^3/B\) before reflection therefore preserves the inverse exactly. Its transition lies where the original complete term already vanishes.

## 3. Joint support insertion: PASS

For fixed inverse index \(h\), the completion scale is \(B/(Nh)^3\). The mask \((a,h)=1\) is constant in the theta frequency. The independently reviewed cutoff can therefore be applied to the full reunited positive/negative block \(a=qg\) without changing its second modulus.

It gives exact zero whenever

\[
(Ng)^2(Nh)^3>C_*B.
\]

The note inserts its smooth joint cutoff while the positive label \(q\) is reunited and the full theta frequency sum is still present. Only afterward does it split \(q=ef\). This is the valid order of operations. No support assertion is made for individual original split components before the insertion.

The resulting nonempty dyads obey \(G^2Z^3\ll B\). On them, the joint cutoff is uniformly smooth in \(Ng/G,Nh/Z\). Every common-divisor extraction preserves these ratios when the corresponding nominal length is divided by the extracted norm. Thus the inserted cutoff can be separated with the common norm kernel without invalidating the uniform scalar estimates.

The widened smooth inverse cutoff keeps the actual completion scale \(B/(Nh)^3\) bounded below by a fixed positive constant. The note explicitly treats any remaining bounded interval below one; it does not silently discard those original inverse terms.

## 4. The shared-divisor lemma: PASS

The two scalar coefficients have the same angular exponent \(-3\), but may have different fixed finite ray characters. After fixing the row's ray class, the inverse cube factor \(\chi_h(k)^3\) is converted to \(\chi_k(h)^3\) with only the admitted fixed ray correction and the same literal zeros.

For the pair of scalar variables, the identity

\[
\mathbf1_{(r_1,r_2)=1}
=\sum_{\ell\mid r_1,r_2}\mu(\ell)
\]

is applied before either pointwise estimate. Setting \(r_i=\ell s_i\), squarefreeness retains \((s_i,\ell)=1\), while no moving mask \((s_1,s_2)=1\) remains. The resulting two scalar sums have the common fixed exclusion \(C\ell\), at lengths \(L_i/N\ell\).

The coefficient of the shared divisor is

\[
\mu(\ell)\lambda_{1,k}(\ell)\lambda_{2,k}(\ell).
\]

Its quadratic row factor is \(\chi_k(\ell)^6=\mathbf1_{(k,\ell)=1}\), so no zero is replaced by one. Applying both scalar estimates leaves

\[
(L_1L_2)^\beta
\sum_\ell(N\ell)^{-2\beta},
\]

which converges for \(\beta>1/2\). The angular exponent \(-6\) at this fixed label is used only as a bounded coefficient in an absolutely convergent accounting sum. No additional scalar theorem at angular type \(-6\) is required.

The same derivation covers the norm-modulated tests produced by Mellin separation, with polynomial seminorm costs. It is a finite shared-divisor identity followed by a convergent bound, rather than cancellation asserted from an unexpanded Euler product.

## 5. All three coprimality interfaces: PASS

The reflected arithmetic expression has the three moving masks

\[
(e,g)=1,\qquad(e,h)=1,\qquad(g,h)=1,
\]

in addition to the fixed \(f\)-exclusions and the row mask. The note handles them in a sound sequence.

First retain \((g,h)=1\), expand the two masks involving \(e\), and write

\[
e=dj e',\qquad g=dg',\qquad h=jh'.
\]

The retained mask forces \((d,j)=1\). Original squarefreeness and coprimality yield exactly

\[
(e',djf)=1,\qquad
(g',fdj)=(h',fdj)=1,\qquad(g',h')=1.
\]

There is no residual condition between \(e'\) and either scalar variable. The Möbius factors cancel as displayed in (4.7). The character \(\chi_{n_0}(dj)^4\) belongs to the \(n_0\)-vector, and the extracted \(e\)-coefficient remains a bounded vector in \(e'\). The row mask splits into the fixed contraction \((k,djf)=1\) and the surviving moving mask \((k,e')=1\).

For fixed \(d,j,f\), the shared-divisor lemma applies to \(g',h'\) with exclusion \(fdj\). Its common label \(\ell\) is coprime to \(fdj\), but can overlap \(e'\). The note explicitly allows that overlap. Imposing \((e',\ell)=1\) would change the earlier inclusion–exclusion identity and obstruct the claimed independent scalar factorization.

The use of a product expression off the original coprime support is legitimate here: it supplies an algebraic extension only inside the exact signed mask expansion. It does not assert the original coefficient formula on previously excluded tuples.

After these steps the two scalar sums are independent of both surviving column indices. Taking their uniform pointwise bound before the remaining row norm is therefore justified. The quadratic–cubic composition still sees its actual moving row mask \((k,e')=1\).

## 6. Norm factors and the complete reflected support: PASS

The inverse coefficient contributes \(1/Z\), in addition to the first-reflection normalization. The full prefactor on a frozen ramified/cube piece is

\[
\frac{3^{-m/3}}{Z\sqrt{AFG}\,Nb'},
\]

up to fixed squarefree bad-part constants. The new effective squarefree length is

\[
\frac{Y}{3^mNn_S(Nb')^3},
\qquad
Y=\frac{H^2EG^2Z^3}{BF}.
\]

Both powers of \(Z\) are correct: \(1/Z\) comes from the inverse coefficient, while \(Z^3\) comes from replacing \(B\) by \(B/(Nh)^3\).

The squared factor after the two scalar estimates, the \(e'\)-normalization, and Minkowski over the \(O(F)\) choices of \(f\), is

\[
\frac{F^2}{AFGZ^2}
(G/Nd)^{2\beta}(Z/Nj)^{2\beta}\frac{E}{NdNj}
\asymp
G^{2\beta-2}Z^{2\beta-2}
(Nd)^{-2\beta-1}(Nj)^{-2\beta-1}.
\]

The two outer divisor sums therefore have convergent Minkowski costs \((Nd)^{-\beta-1/2}\) and \((Nj)^{-\beta-1/2}\). The shared label has already been summed with the convergent exponent \(2\beta\).

Expanding the remaining quadratic–cubic bound for \(U\ge1\) gives the bracket \(HE+Y+(EY)^{2/3}\). The source tail majorant handles lengths below one or above the effective range. All shifted nonempty subunit scales remain bounded away from zero by their original compact dyadic supports.

The unrestricted reflected cube index is frozen before the phase expansions. Its mass on each norm dyad is \(\sum_{b'}1/Nb'\ll1\), including all bad-prime powers. The geometric factor \(3^{-m/3}\) makes the ramified sum convergent in the row norm, and the fixed bad squarefree parts have only finitely many patterns. The smooth majorant controls the remaining large dyads and all Mellin-frequency costs. These are the same verified support interfaces as in the full-cusp coefficient note, now with the extra inverse length.

This proves the block estimate in (4.1) with the actual second saving \(Z^{2\beta-2}\). Taking the absolute dyadic mass of the inverse cube coefficients before this separation would lose that saving.

## 7. Optimization and literal-polynomial bound: PASS

Using \(EFG\asymp A\), the three terms of the block estimate are exactly

\[
\frac{HA}{F}G^{2\beta-3}Z^{2\beta-2},
\]

\[
\frac{H^2A}{BF^2}G^{2\beta-1}Z^{2\beta+1},
\]

and

\[
\left(\frac{H^2A^2}{B}\right)^{2/3}
F^{-2}G^{2\beta-2}Z^{2\beta}.
\]

The first is bounded by \(HA\). Substituting \(Z^3\ll B/G^2\) into the latter two leaves the powers \(G^{(2\beta-5)/3}\) and \(G^{(2\beta-6)/3}\), both negative on \(1/2<\beta\le1\). This proves

\[
\sum_{k\sim H}^*|P_{A,B}(k)|^2
\ll D^\epsilon
\left[
HA+H^2A B^{(2\beta-2)/3}
+H^{4/3}A^{4/3}B^{(2\beta-2)/3}
\right].
\]

All finite inverse terms have been included, and no cube completion remains on the left side.

At \(A=B=D\), the three allowable row exponents are

\[
1,\qquad (5-2\beta)/6,\qquad 1-\beta/2.
\]

The middle value is smallest for \(1/2<\beta\le1\). At \(\beta=11/12\), the two nontrivial conditions are \(19/36\) and \(13/24\), so \(19/36\) is the correct final range. The two powers of \(D\) in the nontrivial terms are \(17/18\) and \(23/18\). At \(\beta=1\), the range returns to \(H\le D^{1/2}\).

The worst remaining inverse block has bounded \(G,F\) and \(Z\asymp B^{1/3}\), consistent with the note's explanation of why the completed-sum range \(19/24\) is not inherited.

## 8. Independent finite-checker replay: PASS

I inspected the complete finite checker, then ran it independently under ordinary Python and under Python with optimization enabled. Both runs exited successfully and produced byte-identical reports, also identical to the author's frozen report.

| Artifact | SHA-256 |
|---|---|
| check_cube_inverse_algebra.py | 33b4354dc92c6864cc56bcc1cfff019c392a3fc19ea543c625ca86aece154553 |
| cube_inverse_algebra_report.json | abca23a4a4650e396e544a526d963c50339c3eeba8f29e9cdf93d6df2395e002 |
| cube_inverse_algebra_audit_normal.json | abca23a4a4650e396e544a526d963c50339c3eeba8f29e9cdf93d6df2395e002 |
| cube_inverse_algebra_audit_optimized.json | abca23a4a4650e396e544a526d963c50339c3eeba8f29e9cdf93d6df2395e002 |

The replay commands, run in /workspace/scratch/6ec6134c1535, were:

~~~bash
python check_cube_inverse_algebra.py --output cube_inverse_algebra_audit_normal.json
python -O check_cube_inverse_algebra.py --output cube_inverse_algebra_audit_optimized.json
~~~

The checker uses explicit exception-raising requirements, so optimization does not disable its checks. Its coefficient arithmetic is exact in \(\mathbb Z[\omega]\), and its exponent optimization uses exact rational arithmetic. The three prime labels are formal squarefree support coordinates; the program does not claim to evaluate sextic residue symbols.

The output records 9,216 instances of the shared-divisor identity with sixth-root and zero coefficients; 4,096 complete \(e,g,h,f\) mask cases; and 32,768 row and cubic zero-mask factorizations after \(e=dje'\). It also checks the three linear objectives at five rational values of \(\beta\), including \(11/12\) and \(1\), and verifies nonnegative slack certificates on the whole support polygon for those values.

Two deliberate incorrect formulas are detected. Adding a false condition \((e',\ell)=1\) fails in 91 support cases; already \(e=g=h=p,\ f=1\) changes the correct value zero to one. Replacing an extracted common row-character zero by the principal unit value changes a separate zero test to minus one. The valid mask expansion includes 469 terms with \(\ell\) sharing a prime with \(e'\), so that essential interface is actually exercised.

These finite checks corroborate the independently proved arithmetic identities and the rational optimization. They do not certify the analytic scalar input, the exact theta support theorem, the all-cusp formulas, the upper sieves, or any infinite moment estimate.

## 9. Remaining scope

The inverse identity itself holds for every nonzero row, but the scalar hypothesis and the quadratic–cubic norm argument used here still average squarefree primary rows outside \(S\). The separate arbitrary-row support addendum changes the exact support structure; it does not supply those missing norm estimates.

The bound is for the specific literal polynomial \(P_{A,B}\) with its fixed smooth tests and Gauss/character coefficients. It admits no arbitrary arithmetic weights in either Möbius scalar estimate. The \(\beta=11/12\) specialization retains the companion canonical/angular dependency.

The original adverse fourth-moment dual range, the arbitrary-row/auxiliary family, and the centered product-column covariance remain outside this result. No full fourth moment, higher moment hierarchy, or RH conclusion follows from this audit.

No unresolved mathematical defect was found in the frozen proof snapshot. The attached computational checks corroborate finite algebra only and do not certify the analytic inputs or the infinite estimates.
