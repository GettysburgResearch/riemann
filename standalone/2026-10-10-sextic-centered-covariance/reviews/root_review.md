# Root review of the exact analytic and finite interfaces

**Status:** scoped review of the new standalone deductions, not acceptance of the imported October 5 theorem or of a generalized moment claim.

The primary agent independently checked the interfaces below, in addition to the separate reviews recorded in this directory. The statements depend on their expressly named source inputs. No integrated status file is changed.

## 1. Final angular source and canonical domain

Reviewed final source: ANGULAR_THETA.md, SHA-256
bbc139f956731482fcf9e33645bfe2832b7b7471594d9cbc1f21cd08eaf2ac5a.

The earlier independent review at checkpoint
3778538b60ea92cae9d16819c12d35599706033623797ffa7a0d5eba2109ae30
requested a correction to the canonical domain. In the final source, Theorem 5.1 explicitly uses

\[
\Sigma=XF,\qquad \mathcal H\le\Sigma D^{-\kappa}.
\]

The transfer envelope is not substituted for that equality. This resolves the recorded correction.

I independently recomputed the pure Wirtinger jet, its Bessel integral, and the two angular coefficient conversions. At the center of inversion, a pure derivative of order \(m\) has no height or lower-order terms. Its radial Mellin factor is \(N(c)^{1-2s}\), independent of \(m\). The initial factor \(i^{m+r}\) and the reflected scalar \(i^r/81\) recover the source's order \(-1\) case. The paired first and second Poisson identities carry the intermediate angular factor \(\alpha(n)^{r+1}\) and return the original fixed order \(r\).

The initial inverse sum with angular factor \(\alpha(n)^t\) therefore requires \(r=-t-1\). In particular \(t=-3\) uses \(r=2\), and the excluded order-zero case is not used. The new fixed-angle analytic conclusions require the named imported finite completion/transfer inputs; this audit has not reconstructed that entire imported proof.

For Sections 6–7, the independent final-source review in angular_component_review.md is supplemented by my checks of the translated-lattice estimate, the analytic-log argument, and the moving \(g/e\) exclusion. The latter is expanded before applying the scalar estimate; it is not treated as a column contraction. The divisor cost is \((Nd)^{-\beta-1/2}\), which is summable for the stated \(\beta>1/2\). The allocation profiles are smooth, including the \(g\)-profile, so the scalar bound is not applied to an indicator with uncontrolled derivatives.

**Verdict:** the new angular adapter and stated component conclusions pass, conditional on the source inputs explicitly listed in the proof.

## 2. Repeated reflection and reunited support

Reviewed sources:

| File | SHA-256 |
|---|---|
| DOUBLE_REFLECTION.md | b00bcc186dc830daf62341ac2d5cd80c202ceb5af05f09c043725486e8f5588d |
| REUNITED_SUPPORT_CUTOFF.md | 89cd204ae66ef615e7d630bf2c1e5524e134b76e30789dce7796a229e53a4340 |

I independently derived the generic raw-frequency functional equation. If \(L_+(s)\) is the coefficient series with phase \(\alpha(\ell)\), a reduced translate of denominator \(c\) gives

\[
L_+(s)=
-\zeta\,\alpha(c)^2N(c)^{1-2s}(2\pi)^{4s-2}
\frac{G(1-s)}{G(s)}L_-^\vee(1-s),
\quad
G(s)=\Gamma(s+1/3)\Gamma(s+2/3).
\]

The generic transform consequently has scale constant \((2\pi)^4\), whereas the source transform has \((2\pi)^4/27\). Their composition restores \(V_*(27x)\), not \(V_*(x)\), in the raw-frequency normalization. The standard squarefree/cube normalization in the separate specialization accounts for its additional factor 27 in the initial scale.

For input \(U=\mathsf J V_*\), its Mellin transform is holomorphic for \(\Re s>-5/6\). Moving the coefficient-series contour from \(5/4\) to \(-1/4\) evaluates that test transform only on the strip \([-3/4,3/4]\). The differentiated constant terms vanish. Thus this composition introduces neither a crossed Mellin pole nor a restored zero frequency.

The finite-cusp proof uses actual matrices in \(\mathrm{SL}_2(\mathcal O)\). Factoring \(H_\sigma g=\gamma H_\tau\) leaves the archimedean inversion denominator equal to the denominator of the translating matrix \(g\). It does not replace it by the denominator of the image of the cusp under \(H_\sigma\). The explicit modulo-3 reduction gives only fixed unit rotations and translations of the source cusp expansions, preserving their common lattice \(\lambda^{-4}\mathcal O\) and nonzero norm gap \(1/81\).

I also checked the identity

\[
\prod_{p\mid a}(Np)^{-1/2}(-1+Np\,\mathbf1_{p\mid x})
=\sum_{hg=a}\mu(g)\sqrt{Nh/Ng}\,\mathbf1_{h\mid x}.
\]

For fixed \(h,g\), the frequency multiplier has period dividing \(Mkh\). Its second-reflection denominator norm is at most \(N(M)NkNh\). The first scale contains \((NkNhNg)^2/B\). The row and positive-divisor norms therefore cancel from the lower bound for the restored test argument, leaving a fixed positive multiple of \((Ng)^2/B\). Compact support proves exact vanishing for \((Ng)^2>C_*B\).

The cutoff is inserted into the complete reunited expression, before splitting the positive choices into \(e\) and \(f\), or truncating squarefree/cube frequencies. Only that order of operations is authorized by the theorem. The standard projection is periodic and adds only a fixed bad-prime modulus.

**Verdict:** exact cutoff and its specified standard-face corollary pass at their stated scope. No norm estimate for a growing finite scattering family was used. The separately authored independent cutoff review binds the same final bytes.

## 3. Hermitian incidence source and typesetting erratum

Final source: HERMITIAN_INCIDENCE.md, SHA-256
5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9.

The independent incidence review binds the mathematical source at
714c9f69b9db58f3ada027c8902ded42b781d759b746c117f952748baafd4cc2.
The final source differs only by replacing two malformed control-byte sequences with the intended TeX command backslash-r-m. The exact original offsets and byte replacement are recorded in incidence_typesetting_erratum.json. Reversing precisely those two changes recovers the independently reviewed SHA-256. This check was run, not inferred from the author's description.

I checked the two-axis forward correction against the source's signed inverse factors, including the critical pair of half exponents. Finite subpower regularization is necessary there; the proof does not assert convergence of an Euler product at exponent one. The odd-incidence theorem uses only odd multiplicity with residual exponent congruent to \(1\) or \(-1\) as a native second-moment axis. A residual quadratic exponent is not promoted to that input.

The global-gcd identity is exact before taking absolute values. Its weight \(w_R(q)\) is a signed finite Möbius inversion, and the retained row mask and moving column exclusion both survive extraction. The resulting exponent \(\rho=1+2(k-1)\beta\) gives the stated cutoff \(R\ge D^{(2\beta-1)/(2\beta)}\); this is a Hermitian tuple sector, not a one-sided polynomial tail.

The final Schwartz adapter applies the native input on expanding row annuli with the corresponding reference scale. This resolves the earlier mismatch between compact row support and the Fourier-compact Schwartz profile in the parent A2 note. The zero- and one-active-axis sectors are treated separately in the proof.

**Verdict:** the final source inherits the independently verified mathematical claims after an exactly checked typesetting-only repair.

## 4. Genuine centered-sign witness

Reviewed source: CENTERED_NATIVE_SIGN.md, SHA-256
061927c467de2890d8c2e3ce14a5d5e0008154dc49c68e8c097ebd5556cc5a0b.

For an inert rational prime \(p>3\), the primary generator is \(-p\). The literal source additive character is \(\exp(-2\pi i b/p)\) on \(a+b\omega\). The nontrivial cubic character is trivial on the rational subfield. Its fiber sums are \(p-1\) at \(b=0\) and \(-1\) at every nonzero \(b\). This gives normalized cubic Gauss sum one and coefficient \(a_1((p))=-1\) exactly.

The three chosen norms uniquely identify the ideals \((53),(71),(55)\). The fixed nonnegative smooth window admits no additional norm. Equal pairs have the completed local exponent pair \((1,1)\), whose coefficient is zero; distinct pairs are coprime. Thus the full completion equals the squarefree face in this particular window.

The sextic symbols of the three product ideals equal one on all six unit rows. Combining ordered factorizations before subtracting the product diagonal yields the exact centered value \(48t(t-2)\). The opposite signs at \(t=1/2\) and \(t=3\) follow without rounding.

**Verdict:** this disproves universal positivity of the specified centered form. It does not disprove its conjectural asymptotic upper bound, and does not identify this finite witness with the full signed first-Poisson sum.

## 5. Every cusp and its actual Gauss coefficient

Reviewed final source: ALL_CUSP_GAUSS_FACTORIZATION.md, SHA-256
b596f3f7c43bb84c699201f3b14c81eae18ae89d3b45e2357bcdccfb9eb3ea1c.

I read the actual HTML equations (5.7), (5.13), (5.14), and (5.16) of Dunn–Radziwiłł, arXiv:2109.07463v3. The complex conjugates over the Gauss sums are essential; plain extracted PDF text can lose those bars. The companion proof uses the conjugated cusp coefficients, so the remaining factor is the native cubic Gauss sum after the fixed numerator conversion by lambda. No GRH-conditional dispersion or prime asymptotic from that paper is used.

The squarefree bad-prime part uses only a cubic Gauss sum. The free good index and the positive squarefree divisor retain the cubic CRT interaction. The fixed additive phases can be separated on the relevant finite unit group after the complete cube index is frozen, even when the frozen bad multiplier is a nonunit. Ramified amplitudes and the common factor 3^(-m/3) agree with the source's coefficient bound; all allowed cube and ramified valuations remain in the sum.

The resulting exact arithmetic expression is the previously reviewed standard composition with only fixed finite characters and bounded factors added. The cutoff is inserted into the reunited expression before allocation splitting. Optimizing the complete block then gives

\[
\sum_{k\sim H}^{*}|\mathcal C_{D,D}(k)|^2
\ll D^\epsilon[HD+H^2D^{\beta-1/2}+H^{4/3}D^{2/3}].
\]

Elementary scalar counting gives the range H <= D^(3/4); the additional angular scalar premise gives H <= D^(19/24). Both ranges concern squarefree primary rows outside S and the completed object. They are not zero-free boundaries.

**Verdict:** exact factorization and the all-cusp quantitative adapter pass at their stated scope, in agreement with all_cusp_review.md.

## 6. Literal polynomial after the cube inverse

Reviewed final source: CUBE_INVERSE.md, SHA-256
a865338882111bf3bc96ffc539dd93f3b2ee59390499caaf14852ed8cde77804.

I independently checked the inverse coefficient against the imported eq:cube-inverse. It is exactly 1/Nh times the angular Möbius factor. Its only additional column restriction is (a,h)=1. Substitution of the completed squarefree/cube sum and total cube variable c=hb gives the finite identity sum_(h|c) mu(h)=1_(c=1), including its zero-extended character factors. The surviving weight is B^(-1/2)W_2(Nn/B), giving the asserted normalization of the literal two-factor polynomial.

The restored support condition at length B/(Nh)^3 is (Ng)^2(Nh)^3 <= C_*B. The initial h cutoff and this joint cutoff are inserted smoothly before scalar estimates. The joint cutoff precedes the e/f split. Its derivatives remain uniformly bounded on each nonempty rescaled dyad and after every divisor extraction.

I checked the exact two-variable coprimality expansion and then the two intersections with e. Retaining (g,h)=1 forces (d,j)=1 and gives e=dj e', g=dg', h=jh'. The scalar exclusions are fdj. Applying the common-divisor identity to g',h' leaves the shared label ell free to intersect e'. Imposing a further exclusion there would change the sum. No such exclusion appears in the final proof.

Both scalar factors have angular type -3, with possibly different fixed finite parts. The common-label factor of angular type -6 is only bounded in absolute value and receives no unproved scalar estimate. The exact norm costs are d^(-beta-1/2), j^(-beta-1/2), and ell^(-2beta), with ideal norms understood. They converge for beta>1/2. The remaining moving row mask stays inside the quadratic-cubic norm.

Finally I recomputed the prefactor after summing f, the effective squarefree scale H^2 E G^2 Z^3/(BF), and the three block maxima subject to EFG comparable to A and G^2 Z^3 bounded by a constant times B. The resulting literal-polynomial bound is

\[
D^\epsilon[HA+H^2A B^{(2\beta-2)/3}
+H^{4/3}A^{4/3}B^{(2\beta-2)/3}].
\]

At beta=11/12 and A=B=D, the exponents are 17/18 and 23/18 and the strongest row constraint is H <= D^(19/36). At beta=1 it is H <= D^(1/2). The completed exponent 19/24 is not transferred unchanged.

**Verdict:** the cube-inverse transfer passes, subject to the specified scalar and all-cusp inputs. Its quantitative row restriction and lack of additional auxiliary parameters remain explicit.

## 7. Exact support for arbitrary nonzero rows

Reviewed final source: ARBITRARY_ROW_SUPPORT.md, SHA-256
f859936fb555de1afd0215fa74e89ce10b8afa1b9a193e4d355be3da3f542dd5.

I read the imported eq:theta-row-twist and its adjacent finite-family assertion directly. At a good prime with a positive row exponent divisible by six, the factor remains the nonunit mask chi_p^0=1_(p does not divide n). The active/inactive decomposition retains this factor. At the fixed bad primes the original indices are already coprime to S, so their row exponents reduce modulo six within a fixed ray family without discarding a zero.

For a fixed row, first-reflection branch, and outer squarefree a=hg, let r be the active good row radical. Every a-prime has exponent four and is active. The first denominator is c_0 r h g; after reuniting only the a-prime Ramanujan factors, the remaining multiplier has period dividing Mrh. The row factors with exponents zero through five, including possibly large Ramanujan factors, stay inside that periodic multiplier. No outer Gauss scalar simplification is needed.

Each second reduced denominator divides Mrh. The raw kernel composition restores V_*(27x), and the common frequency gap is 1/81. Its outgoing argument is therefore bounded below by

\[
\frac{N(c_0)^2}{3N(M)^2}\frac{(Ng)^2}{B}.
\]

The constants are uniform over the fixed S/unit/ray family. Every outgoing term is zero when (Ng)^2 exceeds the resulting constant times B. Neither large finite Fourier coefficients nor a growing number of first branches affect an exact termwise zero. The proof never needs to sum their norms uniformly.

**Verdict:** the cutoff holds for every nonzero row, including units, sixth powers, and arbitrary bad valuations. This adds exact support only; the quantitative squarefree-row theorems are not silently extended.

## 8. All-row quantitative bounds and the refined auxiliary cost

Reviewed final candidate: ARBITRARY_ROW_MOMENTS.md, SHA-256
a12605808006c07f1a413e743545441e0541577367c8ea1bbe09a7fc493cc52a.

I independently derived the mixed local scalar from the imported full scalar and compared the derivation with the complete new note. For every active local exponent j, including the special cases zero and four, the variable c/p has exponent 2j+2 modulo six. Aggregating the outer a-primes gives their native gamma_4(a) CRT factor and a cross exponent four. Reciprocity and multiplication by the external row twist make the final a/row exponent 3j. The gamma_2(a) factor cancels, and the angular factor is exactly alpha(a)^(-3). Fixed bad-ray and multiplier data can be separated on the source's fixed ray classes; an arbitrary a-dependent scalar is not placed into a native Möbius estimate.

The original (a,k)=1 exclusion is essential. It makes every outer allocation divisor a unit at each repeated row prime. The row exponent-four Ramanujan factor therefore depends only on the remaining squarefree theta index and the frozen cube index. Its squared amplitude is at most the prime norm. All other row factors separate into bounded vectors. After fixing k=u k_S tau k_0, the scalar index is the squarefree k_0 rad_odd(tau), with the full rad(tau) retained in the moving exclusion. The scalar bound is used on the actual rows before the residual positive k_0 norm is enlarged.

I recomputed the three fixed-sector norm weights, including active/inactive branch counts. The disjoint row sectors contribute Euler factors 1+O(q^(-2)), 1+O(q^(-2)), and 1+O(q^(-4/3)). All converge. No Minkowski loss is introduced over the row sectors themselves. Bad-prime powers have fixed geometric sums, and all six units and the nonempty H_0 in (1/2,1) cases are covered.

The exact auxiliary replacement is k -> k q^4, with no assumed coprimality between k and q. The initial simpler envelope in the new source is correct. I independently checked the sharper Corollary 7.2 as well. At an auxiliary prime absent from the original row, retain the negative, positive-squarefree, and positive-cube terms separately. Reindexing n_0=p n_1 or b'=p b_1 gives the pairs

\[
(\text{squared amplitude},\text{length multiplier})
=(q^{-1},q^2),\quad(1,q),\quad(q^{-1},q^{-1}).
\]

In the squarefree term, normalized cubic Gauss CRT adds only separate bounded e- and n_1-factors. The original exclusion of p from a and the inverse h is retained; the cube term keeps p not dividing n_0 while allowing arbitrary p powers in b_1. Thus no new scalar interaction is introduced. The exact reunited cutoff is inserted before this expansion, and its g/h variables do not change.

The three energy costs are consequently bounded by constants times 1,q,q^(2/3). At physical valuations nu>=1, the full six-residue amplitude and active-branch indicators give local tails O(q^(-1)),O(1),O(1). I checked these exponent maxima with exact rational arithmetic as well as deriving them directly. The resulting finite allocation counts and mild prime products cost Q^epsilon, not a uniformly bounded Euler product. Hence the refined completed and literal-polynomial bounds have auxiliary factors 1,Q,Q^(2/3), with all row overlaps included.

Finally, the sharp-ball proof sums the three positive row powers geometrically. For a fixed rapidly decreasing row profile, D_j=2^j D and H_j=2^j H preserve a common fixed polynomial ceiling on every tail annulus. The preliminary factor D_j^epsilon_0 is absorbed by profile decay of order greater than 2+epsilon_0. The constants and test seminorms remain uniform. This does not separate the original coupled bilinear covariance kernel or admit arbitrary original arithmetic column weights.

**Verdict:** the all-row and moving-auxiliary quantitative adapters pass at the stated dependency level. For the principal auxiliary, the completed ranges are 3/4 from counting and 19/24 from the source-conditional angular input; the corresponding literal-polynomial ranges are 1/2 and 19/36. For auxiliary norm Q, each sufficient balanced row bound gains the factor Q^(-1/2). The strict signed off-diagonal at the initial long dual range remains outside this verdict.

## 9. Exact finite checks and analytic boundary

The checkers were run normally and with Python optimization enabled. Their JSON outputs were byte-identical in both modes. The independent reviewers also reproduced the specified checks.

| Checker | Exact predicates | What is authenticated |
|---|---:|---|
| check_incidence_adapters.py | 36,190 | Mixed-sign local correction, native incidence eligibility, literal sextic row masks, finite full Hermitian gcd extraction, rational cutoffs |
| check_centered_native_sign.py | 8,230 | Finite-field Gauss fibers, actual character values, full finite completion, exact centered witness |
| check_support_algebra.py | 11,134 | All 648 modulo-3 matrices, fixed-unit cusp reduction, standard projection cases, reunited local product, rational exponent maxima |
| check_cube_inverse_algebra.py | 46,080 principal cases, plus rational certificates | Both inverse-factor corrections with zero-extended sixth-root phases; exact allocation and row/cubic masks; explicit failures of the two forbidden mask changes; exact rational optimization |
| check_arbitrary_row_algebra.py | 872 local cases, 24 parity cases, and valuation progressions | All active scalar phases; mixed reciprocity and literal zeros; exponent-four row factor separation; six-residue powerful and auxiliary exponents |

I read the complete cube-inverse checker and independently ran its repository copy both normally and with optimization. Both reports match the frozen result byte for byte. Its formal prime-support scope is explicit; the finite phase grid is not falsely represented as evaluation of all arithmetic residue symbols. The three earlier checker counts are exact predicate counts; the cube checker instead reports separate configuration counts and its rational certificates.

I also read and independently replayed the arbitrary-row checker in both modes. Both outputs match its frozen report. Its Gauss factors remain formal monomials, and the report distinguishes its local phase and valuation checks from the proposed analytic theorem. The sharper auxiliary allocation is covered by the additional source-level derivation and exact rational computation described above; it is not falsely included in the earlier amplitude-only report's coverage.

These are integer and rational finite predicates. They do not prove a theta transformation, an infinite contour shift, a source large sieve, a generalized moment asymptotic, or RH. The proofs and explicit analytic hypotheses carry those parts of the proposed deductions.

The full generalized moment and the strict signed off-diagonal estimate in the parent A2 note remain outside every PASS verdict here.
