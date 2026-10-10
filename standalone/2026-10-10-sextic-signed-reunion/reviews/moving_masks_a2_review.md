# Independent review of the moving-mask and A2 mean-square adapters

**Review outcome: PASS within the stated source-qualified scope.** No mathematical defect was found in the two reviewed files at the exact hashes below. The review independently reconstructed the local exponent-zero calculation, the physical-valuation sums, the correction weights on general rectangles, the two-cutoff estimate, and the displayed rational consequences. The review does not certify the imported analytic inputs, establish a new zero-free region, or prove the signed fourth moment.

The reviewer is the separate research subagent `/root/spectral_descent_attack`, which did not author either reviewed root file. This is an internal mathematical review, not external peer review or a proof-assistant certificate.

## 1. Frozen scope and dependencies

Both reviewed files are in `standalone/2026-10-10-sextic-signed-reunion/` of the local GettysburgResearch/riemann checkout.

| Reviewed file | SHA-256 | Bytes |
|---|---|---:|
| `MOVING_COLUMN_MASKS.md` | `068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee` | 13325 |
| `A2_MOVING_MEAN_SQUARE.md` | `6eed5695c672dab92620763f8df5b63f60dc416754367ed541cb854bf06854ba` | 14952 |

The mathematical sources checked for the composition were:

- PR #921, commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`, directory `standalone/2026-10-10-sextic-centered-covariance/`: `ARBITRARY_ROW_MOMENTS.md`, SHA-256 `a12605808006c07f1a413e743545441e0541577367c8ea1bbe09a7fc493cc52a`; `CUBE_INVERSE.md`, SHA-256 `a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804`; `ALL_CUSP_GAUSS_FACTORIZATION.md`, SHA-256 `b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c`; and `ANGULAR_THETA.md`, SHA-256 `bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a`.
- PR #914, commit `0cc0428fedbbfc340044c7451b3d392c1da9a103`, `standalone/2026-10-10-sextic-moment-conductor-core/A2_COMPLETION.md`, SHA-256 `d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`. The exact forward correction identity and the fixed-auxiliary normalization in its Sections 4–5 are essential here.
- PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md`, SHA-256 `6879e094fb63969ddc88c637bf633cf46360d144d2b1615573647e734b4141e8`, especially Theorem 3.4. The refined all-row cost is \(H+H^{1/6}L+(HL)^{2/3}\); the older sieve note alone would not justify the exponent \(1/6\).
- Imported source at OpenAI/math commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex`, SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`. The actual exponent-zero local transform and the complete reflection scalar were checked; a statement merely bounding the local transform by one would be insufficient.

The A2 short/long composition also depends on the reviewer's companion hybrid proof, intended for the packet name `HYBRID_CUBE_INVERSE.md`. Its frozen scratch file is `pass2_spectral_hybrid_cube.md`, SHA-256 `d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a` (17345 bytes). This version explicitly includes general ordered axes, the exact moving-mask block dependence, fixed smooth two-variable tests by Mellin separation, and the profile extension. An earlier presentation omission concerning two-variable tests was closed in this version.

The independent derivation supporting this review is `pass2_spectral_a2_cutoff.md`, SHA-256 `689d892366368dcec19ffcc2a45ef2788db5423bdcdbd6f58aadc98e3da2f2aa` (14618 bytes). It was developed separately from the root A2 proof. The two derivations agree on every cutoff exponent and correction weight checked below.

## 2. Moving original columns: exact zeros and the exponent-zero branch

The identity
\[
\chi_n(q_0^6)=\mathbf 1_{(n,q_0)=1}
\]
holds with the source's zero extension, including nonunits. Consequently the literal original-column exclusion is exactly the substitution \(k\mapsto kf^4q_0^6\). A prime already dividing \(f\) is redundant in the extra sixth power, so the effective new exclusion is \(q=q_0/(q_0,f)\). This is an identity of the original finite sum, not an assumed contraction of a theta norm.

The completed cube character also gives
\[
\chi_b(q_0^6)^3=\mathbf 1_{(b,q_0)=1}.
\]
Thus the same substitution includes the cube-index exclusion. The inverse coefficient retains its literal \(\chi_h(kf^4q^6)^3\), and therefore its zeros at \(f q\). The existing outer condition \((a,h)=1\) is retained; neither a condition between \(h\) and a reflected column nor a condition between a regrouped cube index and the remaining squarefree column is inserted.

For \(p\mid q\), write \(v=Np\). When the physical row has \(v_p(k)=0\), the shifted local exponent is zero. The source gives an inactive branch with scalar \(1-v^{-1}\), with \(p\) absent from both the denominator and the period, and an active branch with
\[
B_{p,0}(x)=v^{-1/2}\chi_p(x)^{-2}.
\]
The active Gauss scalar has modulus one, while the squared conductor enlarges the effective theta length by \(v^2\). The two squared-amplitude/length pairs are therefore
\[
((1-v^{-1})^2,1),\qquad(v^{-1},v^2).
\]
They give, by the two-term norm triangle inequality, costs bounded by constants times
\[
1,\qquad v,\qquad v^{1/3}
\]
on the three energy monomials. In particular, replacing the active amplitude by the weaker bound one would lose a real polynomial factor and would not prove the claimed adapter.

I also checked the interaction with the complete mixed scalar rather than just the local absolute value. The scalar exponent \(2j+2\), combined with the outer Gauss factor and row twist, is \(3j=0\) at \(j=0\). No theta-dependent character is introduced in either Möbius variable. In the transformed frequency
\[
x=u_\theta\lambda^{m+4}e n_S n_0(f_1b')^3,
\]
the local factor separates as a fixed phase times
\[
v^{-1/2}\chi_p(e)^{-2}\chi_p(n_0)^{-2}
\mathbf 1_{p\nmid b'}.
\]
The two nonconstant factors are separate bounded vectors in the positive norm estimate, and the cube zero remains present. This uses the source's conjugation and zero convention. The argument does not replace the complete reflected cusp contribution by an unconjugated or principal-cusp expression.

## 3. Positive physical valuations, products, and uniformity

The physical row sectors with \(\nu=v_p(k)\ge1\) are disjoint. Adding the artificial sixth power preserves their exponent modulo six. Their actual height is \(H/v^\nu\); using \(H/v^{\nu+6}\) would be incorrect.

With the source's exceptional amplitude and exponent-zero branch factor, the three local valuation sums are
\[
\begin{split}
&\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
v^{\mathbf1_{\nu\equiv4\ (6)}-\nu},\\
&\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
v^{\mathbf1_{\nu\equiv4\ (6)}+2-2\nu},\\
&\sum_{\nu\ge1}4^{\mathbf1_{\nu\equiv0\ (6)}}
v^{\mathbf1_{\nu\equiv4\ (6)}+4/3-4\nu/3}.
\end{split}
\]
I checked all six residue classes. The maximal exponents are \(-1,0,0\), at \(\nu=1\); the \(\nu\equiv4\) amplitude and the \(\nu\equiv0\) two-branch contribution are present. The successive terms of each residue-class progression have ratios \(v^{-6},v^{-12},v^{-8}\), respectively. These sums are \(O(v^{-1}),O(1),O(1)\), consistent with the larger physical-valuation-zero costs above.

At primes of \(f\), the PR #921 exponent-four adapter supplies the already proved costs \(1,v,v^{2/3}\). The sets of primes of \(f\) and \(q\) are disjoint. Their product gives precisely
\[
J=Nf\,Nq,\qquad K=(Nf)^{2/3}(Nq)^{1/3}.
\]
The finite per-prime constants produce \(C^{\omega(fq)}\), which is absorbed using \(C^{\omega(fq)}\ll_\eta(Nfq)^\eta\). The reviewed proof correctly avoids asserting a bounded Euler product for these constants. The other repeated-prime row sectors retain the convergent weights of the all-row source; bad powers and all six unit factors are included there.

The full block, and not merely the optimized completed mean, carries these three multipliers. The two Möbius separation costs remain
\[
(Nd_1)^{-\beta-1/2},\quad (Nd_2)^{-\beta-1/2},\quad
(N\ell)^{-2\beta}.
\]
They are summable for the stipulated fixed \(\beta>1/2\). The residual positive variable may meet \(\ell\), as in the source factorization. Both exact cutoffs, \(G^2\ll B\) and \(G^2Z^3\ll B\), are inserted before separating positive allocations. The new local phases do not alter either scalar variable or either cutoff.

Polynomially bounded moving ideals remain within polynomial conductor ceilings after the row substitution. The estimates are still taken at the original physical row height, with the artificial conductor already accounted for in \(J,K\). Fixed finite smooth seminorms, fixed two-variable tests via Mellin separation, and annular summation are sufficient. For outward Schwartz annuli the reference size is enlarged while all physical column parameters remain fixed; this avoids applying a fixed-reference estimate outside its range.

**Conclusion for `MOVING_COLUMN_MASKS.md`:** the local arithmetic, all-row valuation summation, exact \(J,K\) dependence, and their composition with the existing complete-cusp block are consistent. The theorem remains conditional on the named source analytic inputs and the exact uniform angular scalar premise. The \(\beta=1\) version uses counting for that scalar premise; \(\beta=11/12\) retains the stronger imported canonical/angular premise.

## 4. Independent A2 reconstruction: normalization and adaptive axes

The exact source correction has
\[
A'=\frac{A}{xy^2z^2},\qquad
B'=\frac{B}{x^2yz^2},\qquad
|\Omega_{c,d,e}|\le\sqrt{xyz},
\]
where \(x=Nc,y=Nd,z=Ne\). At a fixed original auxiliary, dividing by the normalizers yields the norm weight
\[
w(c,d,e)=\frac1{xyz^{3/2}}.
\]
Using the larger weight appropriate to a differently averaged auxiliary problem would change the convergence and would not be this proof.

Since \((cde,q_0f)=1\) and \(c,d,e\) are pairwise coprime and squarefree, the child exclusion quotient is exactly \(q'=qcd\). Thus
\[
J'=Jxyz,\qquad K'=K(xy)^{1/3}z^{2/3}.
\]
This includes both the original overlap of \(q_0\) with \(f\) and the forced new overlap at \(e\). The correction does not shift the physical row range.

For the rectangle theorem, take \(A\ge B\), \(t=A/B\), and \(\delta=(2\beta-2)/3\in(-1/3,0]\). I independently obtained the same dividing line \(y=tx\), since \(A'/B'=tx/y\). Choosing the smaller child axis as outer gives the following norm weights after the displayed original factors have been removed:

| Energy contribution | Correction norm weight or regional weight |
|---|---|
| First, bounded using \(m'\le B'\) | \(x^{-2}y^{-3/2}z^{-5/2}\) |
| Third | \(x^{-13/6-\delta/2}y^{-3/2-\delta}z^{-5/2-\delta}\) |
| Second, \(y\le tx\) | \(x^{-3/2-\delta/2}y^{-1-\delta}z^{-2-\delta}\) |
| Second, \(y>tx\) | \(t^{(1-\delta)/2}x^{-1-\delta}y^{-3/2-\delta/2}z^{-2-\delta}\) |

The first and third sums converge absolutely. Summing the regional second weights first in \(y\) gives, in each region,
\[
t^{-\delta}\sum_c x^{-3/2-3\delta/2}
\sum_e z^{-2-\delta}.
\]
The exact requirement is \(\delta>-1/3\), equivalent to \(\beta>1/2\). At \(\delta=0\), the first partial \(y\)-sum has a logarithm on the actual finite support; it is correctly absorbed in \(D^\epsilon\). Squaring gives
\[
JH^2 B A^\delta t^{-2\delta}
=JH^2 B^{1+2\delta}A^{-\delta}.
\]
This proves the stated rectangle term with \(m=\min(A,B)\), \(M=\max(A,B)\). The third term is \(KH^{4/3}m^{4/3}M^\delta\), and the first is \(Hm\). The raw polynomial bound is no larger because \(\delta\le0\). Transposing a fixed two-variable test when swapping axes preserves the exact finite polynomial and its seminorm control. Nonempty child scales below one lie in a fixed compact interval, so this convention costs constants only.

## 5. The correction tail and two independently retained cutoffs

For a raw child, the classical all-row energy is
\[
D^\epsilon[H+H^{1/6}A'B'+(HA'B')^{2/3}].
\]
Its twist and masks are bounded row-independent column coefficients in this particular sieve use. Combining with the fixed-auxiliary correction norm gives the weights
\[
x^{-1}y^{-1}z^{-3/2},\quad
x^{-5/2}y^{-5/2}z^{-7/2},\quad
x^{-2}y^{-2}z^{-17/6}.
\]
The first has finite harmonic logarithms. Grouping the other two by the full correction \(C=cde\), and using a fixed-order divisor bound, yields norm tails \(T^{-3/2+\eta}\) and \(T^{-1+\eta}\). The corresponding energy gains are \(T^{-3}\) and \(T^{-2}\), within the preliminary epsilon loss. No \(J\) or \(K\) is needed for these classical tails.

For the small correction range \(NC\le T\), take \(A=B=D\) and, by symmetry, \(x\le y\). The short inverse uses the independently retained cutoff \(R\). Its second contribution has exact correction norm weight
\[
x^{1/2-\beta}y^{-3/4-\beta/2}z^{-1/2-\beta}.
\]
This sum is not uniformly convergent as \(T\to\infty\); that is why a direct untruncated hybrid transfer would fail. With \(U=T/z\), splitting the \(y\)-sum at \(\sqrt U\) gives in each half the norm cost
\[
U^{7/8-3\beta/4}.
\]
The final \(z\)-exponent is \(-11/8-\beta/4<-1\). Therefore the energy costs
\[
T^{7/4-3\beta/2}.
\]
I obtained this exponent independently from the smaller-axis child formula. The first short term converges; the third has norm weights \(x^{-5/6}y^{-11/6}z^{-11/6}\) on \(x\le y\), whose inner sum leaves \(y^{-5/3}\), so it also converges without a power of \(T\).

Applying the classical long-inverse estimate to all short A2 children gives the same three correction weights as the large-correction tail. Its gains are \(R^{-3},R^{-2}\). The omitted corrections give the separate \(T^{-3},T^{-2}\) terms. The resulting independently derived energy is exactly
\[
\begin{split}
D^\epsilon\big[&HD+
JH^2D^{\beta-1/2}T^{7/4-3\beta/2}R^{5/2-\beta}
+KH^{4/3}D^{2/3}R^{2\beta}+H\\
&+H^{1/6}D^2(R^{-3}+T^{-3})
+H^{2/3}D^{4/3}(R^{-2}+T^{-2})\big].
\end{split}
\]
This matches `A2_MOVING_MEAN_SQUARE.md` (4.3). The separate cutoffs are used in distinct exact decompositions; no equality of the underlying truncations is assumed. The later choice \(R=T\) is a permitted optimization of the proved bound.

## 6. Exact rational consequences checked

At \(\beta=11/12\), the A2 correction and short inverse powers are \(T^{3/8}\) and \(R^{19/12}\); their sum when \(T=R\) is \(R^{47/24}\).

For \(R=T=H^{1/18}\), the second energy term is
\[
JD^{5/12}H^{911/432}.
\]
Hence the claimed range
\[
H\le D^{684/911}J^{-432/911}
\]
makes that term at most \(D^2\). The third term is \(KD^{2/3}H^{155/108}\). Using \(K\le J^{2/3}\) gives the sharper expression
\[
KD^{2/3}H^{155/108}
\le D^{31/18}H^{19/648}\le D^2,
\]
since the stated range implies \(H\le D\). The two cubic tails become \(D^2\); the mixed tails and \(HD,H\) are smaller. These calculations confirm Corollary 5.1.

At \(q_0=f=1\), \(H=D^{1/2}\), \(R=T=D^{16/119}\), the dominant second and cubic-tail exponents agree:
\[
\frac{17}{12}+\frac{47}{24}\frac{16}{119}
=\frac{25}{12}-\frac{48}{119}
=\frac{2399}{1428}.
\]
The other displayed exponents are exactly \(188/119\), \(499/357\), and \(3/2\), all smaller. These calculations confirm Corollary 5.2.

The supporting scratch diagnostic `pass2_spectral_check_exponents.md`, SHA-256 `905fa9f36182ed46e392d722b297f3a696672f6191ec57c183b5f7cc84d4b13b`, contains its complete executable producer. It uses exact rational arithmetic and exceptions rather than removable `assert` statements. Ordinary Python and optimized Python produced identical report bytes, SHA-256 `5422d589e5d944b0dc6d7106922c56b61d671b4b15e72f84f206890ec9ab4606`. These checks support the algebra; they are not analytic proofs. The finite smooth-regrouping diagnostic also includes zero characters and negative controls for two incorrect masks. It is a finite identity check, not a complete Eisenstein residue census.

## 7. Conclusion and limitations

The two exact reviewed hashes pass this scoped review. Their composition yields a source-qualified all-row positive A2 mean square with the actual moving original exclusion and fourth-power auxiliary. The hybrid companion at the frozen hash above closes the general-test interface, and the independent derivation confirms the correction exponent rather than assuming that the hybrid estimate transfers automatically.

The stronger \(\beta=11/12\) specializations retain their named uniform canonical/angular scalar premise, together with the theta and upper-sieve dependencies of the component proofs. This review does not independently prove those imported analytic theorems. Nor does it extend the precise reflected full-cusp identity of a different row family without the required coefficient adapter.

The established results are positive norms on the stated ranges. They do not identify the subtraction in the signed first-Poisson covariance with independently corrected columns, do not reach its original long dual-row scale, do not prove the generalized \(2k\)-moment theorem, and do not establish the full Riemann hypothesis. The reviewed files state those limitations accurately.
