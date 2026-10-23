# Independent review: primitive continuation for sixth-power-free labels

23 October 2026. Reviewed `../two-hour-boundary-20261023/PRIMITIVE_LABEL_CONTINUATION.md`, SHA256 `a10b7626fc5a7ab7315f8327c53b2fcbe1381a2f04816a04aa697309803976ee`, and `SIXTH_FREE_LABEL_EXTENSION.md`, SHA256 `3e4a3d902aa937d7a498ab1201a269e6891265a9b1c8a34945524c330797b507`.

Verdict: the scalar continuation P2 and the actual short-label projection P14 follow from the stated source-dependent inputs. No additional arithmetic, completion, or exponent defect was found. The projection is only part of the physical inverse vector; no bound for its orthogonal complement or for the full signed first-Poisson return follows.

## Fixed-prime inversion and the free coefficient

I compared P3 with paper10 v2 (3.1)--(3.7), including the changed ray component for j=0,2,4. Reduction of a+epsilon=6 to j=0 is valid precisely because the primitive modulus remains prime to that prime; its exclusion is retained. It would not be valid as a periodicity assertion for a full continuous series. The selected monomial is q^(-1/2)(q^(j+1))^(1-u), so the outside factor J^(-1/2) and physical scale U/t are correct. Expanding the fixed-prime denominator gives k_R^(-1) and k_R^(-6), including all supported powers.

After freezing g,J,k_R and the R-supported modulus part l, the subsequent squarefree m-prime inversion leaves the coefficient mu(m_free) times the inverse character at c0(e d0)^2 l t. The character from t is not folded into a supposedly fixed-conductor ray character. The m-prime extraction phases split it multiplicatively, and its free part stays in this inverse row. Every extra mask is either the row's natural zero or part of the fixed puncture QR and the frozen extracted factors. Multiplication of c0 by the frozen index is injective. Thus the actual-coefficient inverse theorem applies with the enlarged row length, without an arbitrary-coefficient replacement.

The original and reflected row lengths are respectively tT/(k_m^6 f^6) and t h'A k_m^6 d0^6/T. The h' enters only the reflected scale because the functional equation retains the numerator m h'd^2. The source's finite bad-prime matrix depends on its fixed local classes, which are split before estimating. The R-supported modulus norm cancels from the physical-modulus/inverse-row ratio. This verifies P4 rather than assuming conductor invariance.

The reciprocal-completion balance is V^(1/6)(Ah')^(-1/12)k_m^(-1)d^(-1/2); t cancels between the two inverse row lengths. Repeating the source's explicit sums gives A^(11/24)t^(1/12)(h')^(1/24). For the volume term, the intermediate factor sqrt(t)(Ah')^(1/4) multiplies the d0 cutoff power V^(1/2)(Ah')^(-1/4), leaving sqrt(tV). After the outside factors this is exactly the claimed U-volume cost. The unselected and selected exponents in P7 are -23epsilon/12+j/12 and -23epsilon/12+(j-6)/12, respectively. Both are at most a/12. The k_R amplitude Euler product costs a subpower, while all m-prime nonvolume sums retain smallest exponent 7/6.

## Pole collapse and finite tails

At u=7/6, use the residue density in both ray components of D_j=H_j+a_j H_partner. It gives a_j rho_partner=q^(-1)rho_original, with its phase, and forces the j=5 residue to vanish. The source paper8 full-residue sixth-power periodicity, stated for every integral numerator valuation in its fixed section family, also handles a+epsilon=6. No continuous periodicity is inferred. Iterating first at fixed R-primes and then at the selected m-primes therefore gives P8 on the original n coefficient, including J^(-1)d^(-1)k_R^(-2)k_m^(-2).

Writing n=b*l in that original progression pairing gives outside b^(-1/2), new length D/b, and label bR. The independently reviewed scalar residue bound yields exactly D^(2/3)b^(-5/3)+(DH)^(1/3)b^(-1), including the fixed gcd restriction as a puncture. Multiplication by the reciprocal-tail cutoff produces P10 and P11 with g exponents -11/12 and -7/12. The latter d^(-1) sum is only finite-supported and is bounded with a positive internal Rankin loss; it is not falsely claimed absolutely convergent. The fixed-prime factors are bounded by H^(1/12) in amplitude. This yields P12. Its D^(5/6)H^(1/6) term is dominated by the two terms of P2 on the two sides of H=D. Subunit physical scales remain negative-pole branches.

## Sixth-power-free vector and projection

For the companion extension I checked every principal local entry, including numerator valuation six/modulus valuation seven. The four Rankin weights reproduce the earlier squarefree-label finite vector norm. The optimized reference Y=max(D,D^(5/6)K^(7/6)) gives the stated full-residue vector; the short primitive vector remains D^(2/3) for K<=D^(1/7). Sixth-power extraction repeats the constant term K^(1/6) times, which the note retains. The full-series continuation S5 keeps the finite support of its original plateau and the complete subunit pole tail.

Paper10 Section7 identifies the actual adjoint pairing with the primitive series H(nR,u), including all nonunit zeros and unrestricted numerator valuations. Apply this to alpha=conjugate(b), with the original finite ray sectors. If V collects the specified Gauss vectors and G=V*V, then the actual row projection is V G^(-1) V*, and its squared norm on A alpha is at most ||G^(-1)|| times the sum of squared scalar pairings. The PR1013 `HYPERBOLIC_PUNCTURE_GRAM.md` theorem, not merely its earlier entrywise Gram note, supplies conditioning for K<=U^(1/2-delta), with polynomially bounded growing punctures. The residue vector supplies U^(1/3)D^(2/3), and summing P2 supplies KU+D^(11/12)K^(13/12) for K<=D. Hence P14 is a bound for the whole stated projection, including its continuous part.

At U=D^(6/7), K=D^(1/32), the three exponents are 199/224, 365/384, and 20/21. Their maximum is 20/21, while the inherited nonvolume inverse exponent is 41/42. The saving for this projection is 1/42; the orthogonal complement remains open.

## Source identity correction

Direct SHA256 of `git show origin/pr1015:standalone/2026-10-22-residue-remainder-followup/MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md` is `b45267a73c0123cb0a1d83c161ae5fe995e4493d7395bfcb21a67a790d54fcaf`. The earlier label-uniform note's displayed hash accidentally mixes this prefix with the paper10 snapshot hash. The file was read at the explicitly pinned commit `e87c5f669f81fe6371af926917d1c5b21023bce8`; this bibliographic typo does not change the above argument. The primitive source file hashes to `60a1615eefca1ed6c19572b2fa2296e2dbbf7146654b77a940ef1ecec469cf86`, and the completed kernel to `6f050d0e66769b4989a4b7c42f1a555ee10a2ee05a14ea1585595c784425066e`. The author and parent were notified so the packet can carry an explicit corrected source pin.

This review checks the new extension and its interfaces. It does not certify all upstream preprints or replace external analytic inputs by a formal proof.
