# Liu 2610.26835v1: source identification and focused audit

Audit date: 2026-10-20.

## Exact source

- Author: Baiying Liu.
- Title: *Zero-free half-planes for Hecke L-functions over number fields*.
- Pinned source: [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1); [HTML](https://arxiv.org/html/2610.26835v1); [PDF](https://arxiv.org/pdf/2610.26835v1).
- Submission timestamp: 2026-10-19 17:57:27 UTC; manuscript date: 2026-10-18.
- PDF: 136 pages; SHA-256 `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`.
- License reported by arXiv: perpetual non-exclusive arXiv license. Preserve a source locator and hash; the audit does not claim a general redistribution license for the PDF.

The screenshot matches this source. Its numerical assertion is an open half-plane for every finite-order Hecke character of every number field, with the principal pole permitted. Its boundary is the root near 0.8749 of

\[
 133488B^4-376596B^3+384534B^2-167541B+26231=0,
 \qquad B=B_\flat=0.874886647039964\ldots.
\]

Main theorem: 17.1. The cyclotomic analytic conclusion is Theorem 14.11; Theorem 18.2 transfers the analytic derivation to fields containing the twelfth roots of unity; Proposition 19.1 descends to an arbitrary field. These locators and the exact source version matter more than the tweet's four-decimal shorthand.

## What this audit checked

The main statement, its source-dependency disclosure, the root-of-unity field extension, the class-field descent, and the fixed-supremum contradiction were read against their proofs. The field-dimension calculations below were recomputed from standard local dimensions. The audit also inspected the numerator estimate in Proposition 14.3, its moment-capacity identity, and the special treatment of number-field degree in its approximate functional equation.

This is a focused mathematical audit. It is not a completed independent verification of the 136-page proof, in particular the two-transform inverse/product-moment inductions of Sections 10-12 and all exceptional-theta local normalizations. No defect is established in those uncompleted checks.

## 1. The descent does not lose any boundary

Let a number field \(K\) and a finite-order Hecke character \(\chi\) be fixed. Let \(M/K\) be the cyclic class field cut out by \(\ker\chi\), and put \(F=K(\zeta_{12})\), \(E=M(\zeta_{12})\).

Restriction shows that \(E/F\) is cyclic and \(E/M\) is abelian: their Galois groups embed in \(\operatorname{Gal}(M/K)\) and \((\mathbb Z/12\mathbb Z)^\times\), respectively. All-field Galois or abelian hypotheses over \(\mathbb Q\) are unnecessary here.

If every finite-order Hecke function over \(F\) has the prescribed zero-free half-plane, abelian factorization first makes \(\zeta_E\) zero-free. Factoring \(\zeta_E/\zeta_M\) into entire nonprincipal Hecke factors then makes \(\zeta_M\) zero-free there away from \(1\). Finally, the cyclic factorization of \(\zeta_M\) over \(K\) makes each factor \(L_K(s,\chi^j)\) zero-free. The principal poles at \(1\) are removed by taking the ratio of the two simple zeta residues; the nonprincipal values in the remaining finite product are then nonzero. This verifies the algebra of Proposition 19.1.

Two easy mistakes are avoided in that argument: a product can protect a factor only when the other factors have no poles in the region, and the argument at \(1\) must use residues rather than ordinary multiplication of finite values. Full Hecke factors also handle real-place ramification before passage to the totally complex auxiliary field.

## 2. What the root-of-unity hypothesis supplies

For any fixed \(F\supseteq\mu_{12}\), the following checks support Lemma 18.1 without assuming that \(F/\mathbb Q\) is Galois.

| Claim used in the transfer | Independent check |
|---|---|
| Total complexity | A real embedding cannot contain a primitive cube root of unity. |
| \(-1\) is both a square and a cube | In fact \(-1=\zeta_{12}^{6}\) is a sixth power in \(F\). |
| Finite-order archimedean type is trivial | A continuous map from the connected group \((\mathbb C^\times)^{r_F}\) into a finite group is trivial. |
| Principal \(S\)-integer ring | Include finite prime ideals generating the finite class group in \(S\). |
| \(S\)-unit quotient compactness | Dirichlet's \(S\)-unit theorem gives a lattice in the norm-one logarithmic directions; passing to sixth powers has finite index. |
| Local-power dimension balance | For \(\ell=2,3\), the sum of local dimensions is \(2|S_f|+[F:\mathbb Q]=2(|S_f|+r_F)\); the \(S\)-unit dimension modulo \(\ell\)th powers is \(|S_f|+r_F\). |
| Alternating Hilbert pairing | The identity \((x,-x)_\ell=1\), together with \(-1\in F_v^{\times\ell}\), gives \((x,x)_\ell=1\). |
| Local-to-global cubes | A nontrivial cyclic Kummer cubic extension has an inert unramified prime by Chebotarev; its defining element cannot be a cube in that completion. |

For the dimension row, a finite completion away from \(\ell\) contributes 2, a completion above \(\ell\) contributes \(2+[F_v:\mathbb Q_\ell]\), and a complex place contributes 0. The degrees above \(\ell\) sum to \([F:\mathbb Q]\). The unit rank is \(|S_f|+r_F-1\), with one further dimension from the \(\ell\)-torsion roots of unity. Thus the numbers match the half-dimensional isotropic setup used for allowed generators.

These checks validate the elementary field-general portion. They do not by themselves establish the theta-coefficient identities or the analytic moment inequalities. Theorem 18.2 still requires the particular local identities imported from the OpenAI source to have the same stated field scope and normalizations.

## 3. The supremum argument does not require uniform character constants

Write \(\beta=\beta_*(F)\) for the fixed-field supremum over finite-order characters. Suppose \(\beta>B_\flat\). The preliminary source result bounds \(\beta\) from above. Choosing \(\kappa=2\beta-1\) then satisfies the product moment's condition \(\beta\leq(1+\kappa)/2\) with equality. The scalar fixed-point inequality permits a strictly smaller target boundary, and the comparison continues each target reciprocal to a common smaller half-plane, contradicting the definition of the supremum.

The quantifiers here are sound provided the claimed scalar margins are uniform in the target as stated in the analytic comparison. The onset and implicit constant may depend on the fixed character. No zero has to attain the supremum, and no infinite passage of character-dependent constants is needed. The finite rational chain in Appendix B is a separate scalar verification, rather than a prerequisite to this contradiction.

## 4. Numerator and degree checks

The cancellation identity behind Proposition 14.3 is elementary and correct. For a central polynomial block of length exponent \(m\), select prime length \(z_p=v(1-2m)\), and set \(\theta=gv\). The exponent arising from the fourth-moment amplification and the shifted block coefficient is

\[
 -\theta m-\frac{g z_p}{2}
 =-gv m-\frac{gv(1-2m)}2=-\frac\theta2.
\]

The important issue in a number field is not this identity but the permitted moment lengths. An approximate-functional-equation block can have length exponent larger than \(1/2\) because the gamma factor has degree \([F:\mathbb Q]\). The proof separately invokes the zero-prime-factor clause of Theorem 12.14 for those longer blocks. Its allowed length is bounded for each fixed field, though it grows with the degree. Therefore this application is not a degree-uniform analytic estimate. An audit of Theorem 12.14 must preserve that long-block clause; replacing it with a short-range large sieve would leave a gap.

Other material points retained in the proof are the row-dependent conductor, the conductor deficit at repeated prime powers, the finite group of excluded inducing characters, and the ordering of the prime mesh before the target-dependent height choices. None can be dropped merely because the final exponent is field-independent.

## 5. Proof and formalization scope

Remark 3.1 explicitly separates the mathematical argument from the accompanying Lean work. The latter covers scalar statements and selected arithmetic implications; it does not formalize the entire analytic argument of Part II. The source uses earlier exceptional-theta local/global calculations, while deriving the varying moments in its own Sections 10-12. The moment's intermediate zero-free condition is discharged in the stated continuation argument.

The appropriate import status is therefore **external preprint theorem, with focused independent checks and inherited analytic dependencies**. Exact polynomial verification or a successful scalar script is evidence about the scalar step only. It should not be recorded as certification of the full all-field zero-free theorem.

## 6. Consequence that can be proved cleanly on top

The all-number-field quantifier allows a useful extension beyond the monomial statement in Corollary 19.2(2). Brauer induction expresses every finite-image Artin function as a finite integer product of finite-order Hecke functions over intermediate fields. Because every such factor is a holomorphic unit in the half-plane away from \(1\), negative exponents create no poles there. Frobenius reciprocity computes the exact principal-pole order at \(1\).

The companion note `artin_chebotarev.md` supplies the complete proof and a fixed-extension Chebotarev corollary, including a separately checked epsilon gap for intervals of length \(x^\alpha\), \(\alpha>B_\flat\). This is a boundary-preserving family extension. Its proof does not introduce a new analytic moment assumption beyond the external universal Hecke input.
