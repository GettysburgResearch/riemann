# Review of the principal short/long covariance corollary

## Reviewed bytes and verdict

Reviewer: `/root/signed_sector`. I reviewed the new support-separation argument, the exact four-block identity, its normalization in the original signed comparison, and the diagnostic scope. During this audit I supplied the improvement from a cube-root to a sixth-root support threshold; this receipt discloses that contribution and checks the final written proof and its scope. It is not a claim of formal verification or wholly independent discovery of that sharpening.

**Verdict: the corollary is supported under its stated hypotheses.** No remaining defect was found after the physical-support, two-variable-profile, and off-product scope clarifications described below.

| Reviewed artifact | SHA-256 |
| --- | --- |
| `PRINCIPAL_SHORT_LONG_COVARIANCE.md` | `7de2f4fbf8b085bc37cc83d0767748eee1c8478a590b3551935870b616f9166e` |
| Its dependency `CENTERED_COVARIANCE_AND_CUBE_ALIASES.md` | `d121c94e9eaf8142d160ece29194d186cf2b915dfc53273d351e2baeec7becde` |
| `check_short_long_principal_blocks.py` | `1197b7e4eebc1c76909a272426365f4dde14e9afe78c37903508cf087c0edf8a` |
| Independent rerun `short_long_principal_independent_checks.json` | `191fc950937f84b33af16dce1e26e67ccb09ebe911cae3a7feb22ba31b26ce94` |

This is a theorem about complete-residue principal covariance with the actual product diagonal removed. It does not estimate the full finite-height oscillating covariance.

## 1. The sixth-root support argument

The raw products are genuinely squarefree. Every combined inverse term has physical product \(md^3\), where \(m\) is squarefree but need not be coprime to \(d\). A nonzero principal pairing with a raw product \(m_0\) requires

\[
m_0=m,\qquad d=j^2
\]

by reducing the exponent congruence first modulo three and then modulo two. This uses the exact zero-extended character kernel, not a replacement of its density by one.

A nonzero long coefficient

\[
c_R(d)=\sum_{h\mid d,\ Nh>R}\mu(h)
\]

requires an actual squarefree inverse divisor \(h\mid d\) with \(Nh>R\). Since \(d=j^2\), squarefreeness of \(h\) gives \(h\mid j\), hence \(Nj>R\). The physical product ratio is therefore

\[
\frac{N(md^3)}{Nm_0}=(Nj)^6>R^6.
\]

The support ratio in Lemma 2.1 bounds that same quotient above. Thus the stated sixth-root threshold suffices, and equality is included because the long inverse uses the strict condition \(Nh>R\). This is stronger than the preliminary argument using only \(Nd>R\).

The physical cross diagonal is empty even before the support comparison: a surviving long term has \(d\ne1\), so \(md^3\) is nonsquarefree and cannot equal a raw squarefree product. The two zero statements in (2.2) therefore follow separately and correctly.

The elementary threshold has an exact endpoint witness. For a prime of norm seven, take \(d=p^2\) and pair its physical product \(p^6\) with the raw unit. At \(R=6\), the long coefficient is \(\mu(p)=-1\) and the principal density is \(6/7\); at \(R=7\), the long coefficient is zero. The support-ratio sixth root is exactly seven. This is a finite coefficient/kernel witness, not a test of the source's individual Gauss phases.

## 2. Masks, phases, and physical support

The arbitrary overlaps of the two exclusion ideals and two auxiliary ideals are harmless here: they remain row-independent coefficients or delete physical coefficients. They cannot create a principal kernel entry between columns whose exponent classes disagree. The argument also keeps the possible overlap of \(m\) and \(d\); no extra coprimality condition is used.

The note appropriately excludes arbitrary extra row characters and independently shifted A2 products from this support threshold. A concrete reason is the pair of shifted raw product \(p^3\) and tail product \((pq^2)^3=p^3q^6\), with \(Np=61\), \(Nq=7\), and \(R=100\). The actual tail coefficient is \(c_R(pq^2)=\mu(pq)=1\). The products are distinct principal aliases, their norm ratio is \(7^6\), and \(R\) exceeds its sixth root. This does not contradict the corollary because \(p^3\) is not a squarefree raw product. It demonstrates why the stated exclusion matters.

The final note defines \(\ell_j,u_j\) from the physical profile support, and explicitly requires them to cover all reconstructed inverse terms. This resolves a real quantifier issue: the support of the summed raw polynomial can shrink or even become empty after masks or coefficient cancellation, without shrinking the support of its individual inverse summands. Bounding only the surviving raw coefficients would not justify the tail support used in the proof.

The extension to a fixed bounded smooth two-variable profile is also justified. At fixed physical \(d\), its value is

\[
V_j(Na/A_j,Nn(Nd)^3/B_j),
\]

independent of the chosen inverse divisor. The coefficient identity remains exact. The principal-tail proof uses only the bounded profile, divisor counting, and the product support \(Nm\asymp L_j/(Nd)^3\), so its estimate is unchanged. Multiplication by \(xy\) has the same properties. No analytic separation of a two-variable transform is required for this extension.

## 3. The four signed blocks and their bound

The centered form is defined after grouping every coefficient with the same physical reconstructed product. On squarefree raw products, principal equality is physical equality, so

\[
\mathcal C_{\rm pr}(P_1,P_2)=0.
\]

The support lemma supplies both mixed raw/tail vanishings. Substitution of \(S_j=P_j-T_j\) into the sesquilinear form then gives exactly

\[
\begin{pmatrix}
\mathcal C_{\rm pr}(S_1,S_2)&\mathcal C_{\rm pr}(S_1,T_2)\\
\mathcal C_{\rm pr}(T_1,S_2)&\mathcal C_{\rm pr}(T_1,T_2)
\end{pmatrix}
=
\begin{pmatrix}\mathcal T&-\mathcal T\\-\mathcal T&\mathcal T\end{pmatrix}.
\]

The same \(\mathcal T\) occurs in all four entries even for different left and right coefficients; it need not be real or nonnegative. There is no positivity argument for this centered matrix.

The dependency separately bounds the principal norm and physical diagonal coefficient mass of each long tail by \(D^\epsilon/R_j\). Applying their respective Cauchy–Schwarz inequalities, then subtracting the diagonal, gives

\[
|\mathcal T|\ll D^\epsilon(R_1R_2)^{-1/2}.
\]

The signs, centering, and use of the two distinct positive estimates are correct. This conclusion would not hold for the entire short-short principal energy, which retains its raw product diagonal as the cutoffs increase. The final Section 3 explicitly labels its corresponding quantities as off-product blocks.

## 4. Original coupled normalization

The zero-frequency weight at the original coupled scale is

\[
\mathfrak c_\Psi\frac{F^2}{H_{\rm orig}}N(N)N(N')\Pi(N,N').
\]

Its norm weights factor between the columns. Multiplication by the normalized product variable preserves the exact finite inverse and its support. This proves the stated off-product zero-frequency bound with the additional factor \(F^2L_1L_2/H_{\rm orig}\); it does not factor the nonzero-frequency remainder.

For the original PR #914 comparison, all allocations of one fixed \(bf\) have product scale \(L_{bf}=L/(Nb\,Nf)\). The exact prefactor, checked in the dependency against pinned PR #914, is \(H_{\rm orig}\mu(f)/(L\,Nf)\). Combining these quantities gives

\[
\frac{H_{\rm orig}}{L\,Nf}
\frac{(Nf)^2L_{bf}^2}{H_{\rm orig}R}
=\frac{L}{(Nb)^2Nf\,R}.
\]

The two allocations cost only a divisor subpower under the fixed polynomial ceiling. The ideal \(b\)-sum with exponent two converges; the physically truncated ideal \(f\)-sum with exponent one is harmonic. The resulting \(O(D^\epsilon L/R)\) bound for each off-product principal block is correct. Their four-block sum is exactly zero at every \(b,f\), so it remains zero with the original signed \(\mu(f)\) weights.

## 5. Diagnostic and remaining scope

I independently reran the frozen diagnostic with its expected-manuscript-hash gate, writing the report into my own work directory. It passed its 270 divisor-support cases, rational same-annulus principal kernel and four-sign example, and norm-seven endpoint witness. Its report is byte-identical to the author's stated final deterministic report.

The finite coefficient vectors used for the four-sign example are rational diagnostic vectors. The test does not reconstruct the literal Gauss coefficient family or certify the analytic tail bound. The proof of the latter is in the reviewed dependency, and the new support argument is proved directly in the manuscript.

The corollary isolates and bounds a principal truncation artifact and the three blocks that cancel it. It supplies no estimate for the remaining complete finite-height oscillating kernel, does not remove the PR #926 small-cube term, and does not establish a fourth moment, a new zero-free boundary, or RH.
